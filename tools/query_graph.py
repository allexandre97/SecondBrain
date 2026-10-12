#!/usr/bin/env python3
"""Query the generated wiki knowledge graph."""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict, deque
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
GRAPH_JSON = ROOT / "wiki" / "graph" / "knowledge_graph.json"


def load_graph() -> tuple[dict[str, dict[str, Any]], list[dict[str, str]]]:
    if not GRAPH_JSON.is_file():
        print(
            "ERROR: wiki/graph/knowledge_graph.json not found. Run "
            "`python3 tools/build_knowledge_graph.py` first.",
            file=sys.stderr,
        )
        raise SystemExit(1)
    graph = json.loads(GRAPH_JSON.read_text(encoding="utf-8"))
    nodes = {item["id"]: item for item in graph.get("nodes", [])}
    edges = list(graph.get("edges", []))
    return nodes, edges


def normalize_page_id(value: str, nodes: dict[str, dict[str, Any]]) -> str:
    value = value.strip()
    if value in nodes:
        return value
    if value.endswith(".md") and value[:-3] in nodes:
        return value[:-3]
    if not value.endswith(".md") and f"{value}.md" in {node.get("path") for node in nodes.values()}:
        for node in nodes.values():
            if node.get("path") == f"{value}.md":
                return node["id"]
    if value.startswith("SRC-"):
        source_id = f"source_id:{value}"
        if source_id in nodes:
            return source_id
    return value


def node_line(node: dict[str, Any]) -> str:
    label = node.get("label", node["id"])
    node_type = node.get("type", "")
    path = node.get("path")
    value = node.get("value")
    detail = path or value or node["id"]
    line = f"- `{node['id']}` ({node_type}) - {label} [{detail}]"
    if node.get("currency") in ("historical", "superseded"):
        line += f" **{node['currency'].upper()}** (as of {node.get('as_of', 'unknown')})"
    return line


def print_node_list(title: str, node_ids: list[str], nodes: dict[str, dict[str, Any]]) -> None:
    print(f"## {title}")
    print()
    if not node_ids:
        print("- No matching nodes.")
        print()
        return
    for node_id in node_ids:
        print(node_line(nodes[node_id]))
    print()


def edge_line(edge: dict[str, str], nodes: dict[str, dict[str, Any]]) -> str:
    source_label = nodes.get(edge["source"], {}).get("label", edge["source"])
    target_label = nodes.get(edge["target"], {}).get("label", edge["target"])
    evidence = f" - {edge['evidence']}" if edge.get("evidence") else ""
    return (
        f"- `{edge['type']}`: `{edge['source']}` ({source_label}) -> "
        f"`{edge['target']}` ({target_label}){evidence}"
    )


def parse_types(value: str | None) -> set[str] | None:
    if not value:
        return None
    return {item.strip() for item in value.split(",") if item.strip()}


def query_neighborhood(
    start: str,
    depth: int,
    type_filter: set[str] | None,
    nodes: dict[str, dict[str, Any]],
    edges: list[dict[str, str]],
) -> int:
    start_id = normalize_page_id(start, nodes)
    if start_id not in nodes:
        print(f"ERROR: start node not found: {start}", file=sys.stderr)
        return 2

    adjacency: dict[str, list[tuple[str, dict[str, str]]]] = defaultdict(list)
    for edge in edges:
        adjacency[edge["source"]].append((edge["target"], edge))
        adjacency[edge["target"]].append((edge["source"], edge))
    for values in adjacency.values():
        values.sort(key=lambda item: (item[0], item[1]["type"], item[1].get("evidence", "")))

    distances = {start_id: 0}
    queue: deque[str] = deque([start_id])
    while queue:
        current = queue.popleft()
        if distances[current] >= depth:
            continue
        for neighbor, _edge in adjacency.get(current, []):
            if neighbor not in distances:
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)

    print(f"# Graph Neighborhood: `{start_id}`")
    print()
    print(f"- Depth: {depth}")
    if type_filter:
        print(f"- Node type filter: {', '.join(sorted(type_filter))}")
    print()

    for level in range(depth + 1):
        ids = sorted(
            node_id
            for node_id, distance in distances.items()
            if distance == level
            and (level == 0 or not type_filter or nodes[node_id].get("type") in type_filter)
        )
        print_node_list(f"Depth {level}", ids, nodes)

    visible_nodes = {
        node_id
        for node_id, distance in distances.items()
        if distance == 0 or not type_filter or nodes[node_id].get("type") in type_filter
    }
    visible_edges = sorted(
        (
            edge
            for edge in edges
            if edge["source"] in distances
            and edge["target"] in distances
            and edge["source"] in visible_nodes
            and edge["target"] in visible_nodes
            and abs(distances[edge["source"]] - distances[edge["target"]]) == 1
        ),
        key=lambda item: (item["source"], item["target"], item["type"], item.get("evidence", "")),
    )
    print("## Traversal Edges")
    print()
    if not visible_edges:
        print("- No matching edges.")
    else:
        for edge in visible_edges:
            print(edge_line(edge, nodes))
    return 0


def query_category(category: str, nodes: dict[str, dict[str, Any]], edges: list[dict[str, str]]) -> int:
    target = f"category:{category}"
    if target not in nodes:
        print(f"ERROR: category node not found: {category}", file=sys.stderr)
        return 2
    members = sorted(edge["source"] for edge in edges if edge["type"] == "category" and edge["target"] == target)
    print(f"# Category: `{category}`")
    print()
    print_node_list("Members", members, nodes)
    return 0


def query_source_id(source_id: str, nodes: dict[str, dict[str, Any]], edges: list[dict[str, str]]) -> int:
    target = f"source_id:{source_id}"
    if target not in nodes:
        print(f"ERROR: source_id node not found: {source_id}", file=sys.stderr)
        return 2
    referencing = sorted(
        {
            edge["source"]
            for edge in edges
            if edge["target"] == target and edge["type"] in {"source_ref", "source_page_id"}
        }
    )
    source_pages = sorted(
        {edge["source"] for edge in edges if edge["target"] == target and edge["type"] == "source_page_id"}
    )
    print(f"# Source ID: `{source_id}`")
    print()
    print_node_list("Source Pages", source_pages, nodes)
    print_node_list("Pages Referencing This Source ID", referencing, nodes)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Query wiki/graph/knowledge_graph.json.")
    parser.add_argument("--start", help="Start node/page path for a graph neighborhood query.")
    parser.add_argument("--depth", type=int, default=1, help="Neighborhood depth for --start.")
    parser.add_argument("--types", help="Comma-separated node types to display for --start queries.")
    parser.add_argument("--category", help="List pages assigned to a category path.")
    parser.add_argument("--source-id", help="List pages connected to a source ID such as SRC-0005.")
    args = parser.parse_args()

    selected = sum(bool(value) for value in (args.start, args.category, args.source_id))
    if selected != 1:
        print("ERROR: provide exactly one of --start, --category, or --source-id", file=sys.stderr)
        return 2
    if args.depth < 0:
        print("ERROR: --depth must be non-negative", file=sys.stderr)
        return 2

    nodes, edges = load_graph()
    if args.start:
        return query_neighborhood(args.start, args.depth, parse_types(args.types), nodes, edges)
    if args.category:
        return query_category(args.category, nodes, edges)
    if args.source_id:
        return query_source_id(args.source_id, nodes, edges)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
