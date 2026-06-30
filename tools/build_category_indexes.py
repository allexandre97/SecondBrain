#!/usr/bin/env python3
"""Build deterministic category index pages from wiki frontmatter."""

from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WIKI_DIR = ROOT / "wiki"
CATEGORY_DIR = WIKI_DIR / "categories"
GENERATED_DATE = "2026-06-30"
INDEXED_TYPES = ("source", "concept", "answer", "question", "tension", "claim", "entity")
TYPE_HEADINGS = {
    "source": "Sources",
    "concept": "Concepts",
    "answer": "Answers",
    "question": "Questions",
    "tension": "Tensions",
    "claim": "Claims",
    "entity": "Entities",
}


def split_frontmatter(text: str) -> tuple[dict[str, object], list[str]]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, lines

    try:
        end = next(i for i, line in enumerate(lines[1:], 1) if line.strip() == "---")
    except StopIteration:
        return {}, lines

    data: dict[str, object] = {}
    key: str | None = None
    for line in lines[1:end]:
        if not line.strip():
            continue
        if not line.startswith(" ") and ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            if value == "[]":
                data[key] = []
            elif value:
                data[key] = unquote(value)
            else:
                data[key] = []
        elif key and line.strip().startswith("- "):
            data.setdefault(key, [])
            if isinstance(data[key], list):
                data[key].append(unquote(line.strip()[2:].strip()))

    return data, lines[end + 1 :]


def unquote(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def wiki_pages() -> list[Path]:
    return sorted(
        path
        for path in WIKI_DIR.rglob("*.md")
        if ".obsidian" not in path.parts and path.name != "README.md"
    )


def as_list(value: object) -> list[str]:
    if isinstance(value, list):
        return [str(item) for item in value if str(item).strip()]
    if isinstance(value, str) and value.strip():
        return [value.strip()]
    return []


def h1(lines: list[str]) -> str:
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def page_label(path: Path, frontmatter: dict[str, object], body: list[str]) -> str:
    for key in ("short_title", "display_title"):
        value = frontmatter.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    heading = h1(body)
    return heading or path.stem.replace("-", " ").title()


def category_ancestors(category: str) -> list[str]:
    parts = category.split("/")
    return ["/".join(parts[:i]) for i in range(1, len(parts) + 1)]


def category_path(category: str) -> Path:
    return CATEGORY_DIR / f"{category}.md"


def category_title(category: str) -> str:
    return category.split("/")[-1].replace("-", " ").title()


def wiki_link(path: Path, label: str) -> str:
    target = path.relative_to(WIKI_DIR).with_suffix("").as_posix()
    return f"[[{target}|{label}]]"


def load_pages() -> tuple[dict[str, dict[str, list[tuple[str, Path]]]], set[str]]:
    members: dict[str, dict[str, list[tuple[str, Path]]]] = defaultdict(lambda: defaultdict(list))
    all_categories: set[str] = set()

    for path in wiki_pages():
        frontmatter, body = split_frontmatter(path.read_text(encoding="utf-8"))
        page_type = str(frontmatter.get("type", "")).strip()
        if page_type not in INDEXED_TYPES:
            continue

        categories = as_list(frontmatter.get("categories", []))
        label = page_label(path, frontmatter, body)
        for category in categories:
            all_categories.update(category_ancestors(category))
            members[category][page_type].append((label, path))

    return members, all_categories


def render_category(
    category: str,
    members: dict[str, dict[str, list[tuple[str, Path]]]],
    all_categories: set[str],
) -> str:
    children = sorted(
        candidate
        for candidate in all_categories
        if candidate.startswith(f"{category}/") and "/" not in candidate[len(category) + 1 :]
    )
    lines = [
        "---",
        "type: category",
        "status: active",
        f"created: {GENERATED_DATE}",
        f"updated: {GENERATED_DATE}",
        "areas: []",
        "categories: []",
        "tags:",
        "  - generated",
        "  - navigation",
        "related:",
        '  - "[[categories/README]]"',
        "sources: []",
        "sensitivity: public",
        "encryption: none",
        "generated: true",
        f"category_path: {category}",
        "---",
        "",
        f"# {category_title(category)}",
        "",
        f"Category path: `{category}`",
        "",
        "This page is generated from wiki page frontmatter. Edit page categories at the source pages, then rerun `python3 tools/build_category_indexes.py`.",
        "",
    ]

    if "/" in category:
        parent = category.rsplit("/", 1)[0]
        lines.extend(["## Parent category", "", f"- [[categories/{parent}|{parent}]]", ""])

    if children:
        lines.extend(["## Subcategories", ""])
        for child in children:
            lines.append(f"- [[categories/{child}|{child}]]")
        lines.append("")

    exact_members = members.get(category, {})
    for page_type in INDEXED_TYPES:
        pages = sorted(exact_members.get(page_type, []), key=lambda item: (item[0].casefold(), item[1].as_posix()))
        if not pages:
            continue
        lines.extend([f"## {TYPE_HEADINGS[page_type]}", ""])
        for label, path in pages:
            lines.append(f"- {wiki_link(path, label)}")
        lines.append("")

    if not children and not any(exact_members.values()):
        lines.extend(["## Pages", "", "- No pages are directly assigned to this category.", ""])

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    CATEGORY_DIR.mkdir(parents=True, exist_ok=True)
    members, all_categories = load_pages()

    for category in sorted(all_categories):
        path = category_path(category)
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.name == "README.md":
            continue
        path.write_text(render_category(category, members, all_categories), encoding="utf-8")

    print(f"Generated {len(all_categories)} category index pages.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
