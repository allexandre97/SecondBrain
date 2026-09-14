#!/usr/bin/env python3
"""Build a deterministic knowledge graph from wiki Markdown frontmatter and links."""

from __future__ import annotations

import json
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from wiki_markdown import as_list, h1, parse_frontmatter


ROOT = Path(__file__).resolve().parents[1]
WIKI_DIR = ROOT / "wiki"
GRAPH_DIR = WIKI_DIR / "graph"
GRAPH_JSON = GRAPH_DIR / "knowledge_graph.json"
GRAPH_SUMMARY = GRAPH_DIR / "knowledge_graph_summary.md"
GENERATED_DATE = "2026-07-01"
WIKILINK_RE = re.compile(r"!?\[\[([^\]]+)\]\]")
SOURCE_ID_RE = re.compile(r"^SRC-\d{4}$")
PAGE_TYPES = {
    "answer",
    "category",
    "claim",
    "concept",
    "entity",
    "overview",
    "question",
    "source",
    "tension",
}


@dataclass(frozen=True)
class Page:
    path: Path
    page_id: str
    frontmatter: dict[str, Any]
    body: list[str]
    label: str
    page_type: str


def page_id(path: Path) -> str:
    return path.relative_to(ROOT).with_suffix("").as_posix()


def wiki_pages() -> list[Path]:
    return sorted(
        path
        for path in WIKI_DIR.rglob("*.md")
        if ".obsidian" not in path.parts
        and not path.name.startswith(".")
        and GRAPH_DIR not in path.parents
    )


def label_for(path: Path, frontmatter: dict[str, Any], body: list[str]) -> str:
    for key in ("short_title", "display_title", "question"):
        value = frontmatter.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    heading = h1(body)
    return heading or path.stem.replace("-", " ").title()


def load_pages() -> list[Page]:
    pages: list[Page] = []
    for path in wiki_pages():
        frontmatter, body = parse_frontmatter(path.read_text(encoding="utf-8"))
        raw_type = str(frontmatter.get("type", "")).strip()
        page_type = raw_type if raw_type in PAGE_TYPES else "concept"
        pages.append(
            Page(
                path=path,
                page_id=page_id(path),
                frontmatter=frontmatter,
                body=body,
                label=label_for(path, frontmatter, body),
                page_type=page_type,
            )
        )
    return pages


def build_page_index(pages: list[Page]) -> dict[str, str]:
    index: dict[str, str] = {}
    for page in sorted(pages, key=lambda item: item.page_id):
        rel_md = page.path.relative_to(ROOT).as_posix()
        rel_no_suffix = page.page_id
        keys = {
            rel_md,
            rel_no_suffix,
            page.path.stem,
            page.path.name,
        }
        for key in keys:
            index.setdefault(key, page.page_id)
    return index


def normalize_wikilink_target(raw_target: str, page_index: dict[str, str]) -> str | None:
    target = raw_target.split("|", 1)[0].split("#", 1)[0].split("^", 1)[0].strip()
    if not target:
        return None

    candidates = [target]
    if Path(target).suffix != ".md":
        candidates.append(f"{target}.md")

    for candidate in candidates:
        if candidate in page_index:
            return page_index[candidate]

    basename = Path(target).stem
    return page_index.get(basename)


def clean_wikilink_value(value: str) -> str:
    match = WIKILINK_RE.search(value)
    if match:
        return match.group(1)
    return value


def node(
    node_id: str,
    node_type: str,
    label: str,
    *,
    path: str | None = None,
    value: str | None = None,
    categories: list[str] | None = None,
    sources: list[str] | None = None,
) -> dict[str, Any]:
    item: dict[str, Any] = {
        "id": node_id,
        "type": node_type,
        "label": label,
        "categories": categories or [],
    }
    if path is not None:
        item["path"] = path
    if value is not None:
        item["value"] = value
    if sources is not None:
        item["sources"] = sources
    return item


def edge(source: str, target: str, edge_type: str, evidence: str | None = None) -> dict[str, str]:
    item = {"source": source, "target": target, "type": edge_type}
    if evidence:
        item["evidence"] = evidence
    return item


def add_node(nodes: dict[str, dict[str, Any]], item: dict[str, Any]) -> None:
    nodes.setdefault(item["id"], item)


def add_edge(edges: dict[tuple[str, str, str], dict[str, str]], item: dict[str, str]) -> None:
    key = (item["source"], item["target"], item["type"])
    if key not in edges:
        edges[key] = item
    elif "evidence" not in edges[key] and "evidence" in item:
        edges[key]["evidence"] = item["evidence"]


def source_id_node_id(source_id: str) -> str:
    return f"source_id:{source_id}"


def category_node_id(category: str) -> str:
    return f"category:{category}"


def source_bundle_node_id(bundle: str) -> str:
    return f"source_bundle:{bundle}"


def author_node_id(author: str) -> str:
    normalized = re.sub(r"\s+", " ", author).strip()
    return f"author:{normalized}"


def source_page_by_source_id(pages: list[Page]) -> dict[str, str]:
    mapping: dict[str, str] = {}
    for page in pages:
        source_id = str(page.frontmatter.get("source_id", "")).strip()
        if source_id:
            mapping[source_id] = page.page_id
    return mapping


def iter_wikilinks(lines: list[str]) -> list[tuple[str, str]]:
    links: list[tuple[str, str]] = []
    for line_number, line in enumerate(lines, 1):
        for match in WIKILINK_RE.finditer(line):
            if match.group(0).startswith("!"):
                continue
            links.append((match.group(1), f"line {line_number}: {line.strip()}"))
    return links


def build_graph() -> dict[str, list[dict[str, Any]]]:
    pages = load_pages()
    page_index = build_page_index(pages)
    source_pages = source_page_by_source_id(pages)
    nodes: dict[str, dict[str, Any]] = {}
    edges: dict[tuple[str, str, str], dict[str, str]] = {}

    for page in pages:
        categories = sorted(as_list(page.frontmatter.get("categories", [])))
        sources = sorted(as_list(page.frontmatter.get("sources", [])))
        add_node(
            nodes,
            node(
                page.page_id,
                page.page_type,
                page.label,
                path=f"{page.page_id}.md",
                categories=categories,
                sources=sources,
            ),
        )

    for page in pages:
        for source_id in sorted(as_list(page.frontmatter.get("sources", []))):
            target = source_id_node_id(source_id)
            add_node(
                nodes,
                node(target, "source_id", source_id, value=source_id, sources=[source_id]),
            )
            add_edge(edges, edge(page.page_id, target, "source_ref", "frontmatter:sources"))

        for category in sorted(as_list(page.frontmatter.get("categories", []))):
            target = category_node_id(category)
            add_node(nodes, node(target, "category", category, value=category))
            add_edge(edges, edge(page.page_id, target, "category", "frontmatter:categories"))

        for raw_related in sorted(as_list(page.frontmatter.get("related", []))):
            target = normalize_wikilink_target(clean_wikilink_value(raw_related), page_index)
            if target:
                add_edge(edges, edge(page.page_id, target, "related", "frontmatter:related"))

        if page.page_type == "source":
            source_id = str(page.frontmatter.get("source_id", "")).strip()
            if source_id:
                target = source_id_node_id(source_id)
                add_node(
                    nodes,
                    node(target, "source_id", source_id, value=source_id, sources=[source_id]),
                )
                add_edge(edges, edge(page.page_id, target, "source_page_id", "frontmatter:source_id"))

            source_bundle = str(page.frontmatter.get("source_bundle", "")).strip()
            if source_bundle:
                target = source_bundle_node_id(source_bundle)
                add_node(
                    nodes,
                    node(target, "source_bundle", source_bundle, value=source_bundle),
                )
                add_edge(edges, edge(page.page_id, target, "source_bundle", "frontmatter:source_bundle"))

            for cited in sorted(as_list(page.frontmatter.get("cites_sources", []))):
                cited_value = clean_wikilink_value(cited)
                target = normalize_wikilink_target(cited_value, page_index)
                if not target and cited_value in source_pages:
                    target = source_pages[cited_value]
                if target:
                    add_edge(edges, edge(page.page_id, target, "cites_source", "frontmatter:cites_sources"))

            authors = as_list(page.frontmatter.get("authors", [])) or as_list(page.frontmatter.get("author", []))
            for author in sorted(authors):
                target = author_node_id(author)
                add_node(nodes, node(target, "entity", author, value=author))
                add_edge(edges, edge(page.page_id, target, "author", "frontmatter:authors"))

            for raw_author_entity in sorted(as_list(page.frontmatter.get("author_entities", []))):
                author_entity = clean_wikilink_value(raw_author_entity)
                target = normalize_wikilink_target(author_entity, page_index)
                if target:
                    add_edge(edges, edge(page.page_id, target, "author", "frontmatter:author_entities"))
                else:
                    target = author_node_id(author_entity)
                    add_node(nodes, node(target, "entity", author_entity, value=author_entity))
                    add_edge(edges, edge(page.page_id, target, "author", "frontmatter:author_entities"))

        for raw_target, evidence in iter_wikilinks(page.body):
            target = normalize_wikilink_target(raw_target, page_index)
            if target:
                add_edge(edges, edge(page.page_id, target, "wikilink", evidence))

    return {
        "nodes": sorted(nodes.values(), key=lambda item: item["id"]),
        "edges": sorted(
            edges.values(),
            key=lambda item: (item["source"], item["target"], item["type"], item.get("evidence", "")),
        ),
    }


def write_summary(graph: dict[str, list[dict[str, Any]]]) -> None:
    node_counts = Counter(item["type"] for item in graph["nodes"])
    edge_counts = Counter(item["type"] for item in graph["edges"])
    lines = [
        "---",
        "type: overview",
        "status: active",
        f"created: {GENERATED_DATE}",
        f"updated: {GENERATED_DATE}",
        "areas: []",
        "categories:",
        "  - admin/wiki-maintenance",
        "tags:",
        "  - generated",
        "  - knowledge-graph",
        "  - navigation",
        "related:",
        '  - "[[wiki/index]]"',
        "sources: []",
        "sensitivity: public",
        "encryption: none",
        "graph_exclude: true",
        "generated: true",
        "---",
        "",
        "# Knowledge Graph Summary",
        "",
        "This page is generated by `python3 tools/build_knowledge_graph.py`. Do not edit it by hand.",
        "",
        "## Outputs",
        "",
        "- JSON graph: `wiki/graph/knowledge_graph.json`",
        "- Summary page: `wiki/graph/knowledge_graph_summary.md`",
        "",
        "## Node Counts",
        "",
    ]
    for node_type, count in sorted(node_counts.items()):
        lines.append(f"- `{node_type}`: {count}")
    lines.extend(["", "## Edge Counts", ""])
    for edge_type, count in sorted(edge_counts.items()):
        lines.append(f"- `{edge_type}`: {count}")
    lines.extend(
        [
            "",
            "## Query Examples",
            "",
            "```sh",
            "python3 tools/query_graph.py --start wiki/concepts/free-energy-estimation --depth 2",
            "python3 tools/query_graph.py --category research/molecular-simulation/free-energy",
            "python3 tools/query_graph.py --source-id SRC-0005",
            "```",
            "",
        ]
    )
    GRAPH_SUMMARY.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    GRAPH_DIR.mkdir(parents=True, exist_ok=True)
    graph = build_graph()
    GRAPH_JSON.write_text(json.dumps(graph, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_summary(graph)
    print(f"Wrote {GRAPH_JSON.relative_to(ROOT)}")
    print(f"Wrote {GRAPH_SUMMARY.relative_to(ROOT)}")
    print(f"Nodes: {len(graph['nodes'])}")
    print(f"Edges: {len(graph['edges'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
