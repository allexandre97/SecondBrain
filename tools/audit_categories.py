#!/usr/bin/env python3
"""Audit category strings used by wiki page frontmatter."""

from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WIKI_DIR = ROOT / "wiki"
REGISTRY = ROOT / "schema" / "category_registry.md"
INDEXED_TYPES = {"source", "concept", "answer", "question", "tension", "claim", "entity", "overview"}
CATEGORY_LINE_RE = re.compile(r"^- `([^`]+)`")


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


def as_list(value: object) -> list[str]:
    if isinstance(value, list):
        return [str(item) for item in value if str(item).strip()]
    if isinstance(value, str) and value.strip():
        return [value.strip()]
    return []


def wiki_pages() -> list[Path]:
    return sorted(path for path in WIKI_DIR.rglob("*.md") if ".obsidian" not in path.parts)


def registry_categories() -> set[str]:
    if not REGISTRY.exists():
        return set()
    categories: set[str] = set()
    for line in REGISTRY.read_text(encoding="utf-8").splitlines():
        match = CATEGORY_LINE_RE.match(line.strip())
        if match:
            categories.add(match.group(1))
    return categories


def normalize(category: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", category.casefold())


def main() -> int:
    used: dict[str, list[Path]] = defaultdict(list)
    no_categories: list[Path] = []

    for path in wiki_pages():
        frontmatter, _ = split_frontmatter(path.read_text(encoding="utf-8"))
        page_type = str(frontmatter.get("type", "")).strip()
        if page_type not in INDEXED_TYPES:
            continue
        categories = as_list(frontmatter.get("categories", []))
        if not categories:
            no_categories.append(path)
        for category in categories:
            used[category].append(path)

    registered = registry_categories()
    unknown = sorted(category for category in used if registered and category not in registered)
    normalized: dict[str, list[str]] = defaultdict(list)
    for category in used:
        normalized[normalize(category)].append(category)
    duplicates = {key: values for key, values in normalized.items() if len(values) > 1}

    print("All categories currently used:")
    for category in sorted(used):
        print(f"- {category} ({len(used[category])})")

    print("\nCategories with only one page:")
    singletons = [category for category, pages in used.items() if len(pages) == 1]
    if singletons:
        for category in sorted(singletons):
            print(f"- {category}: {used[category][0].relative_to(ROOT).as_posix()}")
    else:
        print("- None")

    print("\nUnknown categories relative to schema/category_registry.md:")
    if unknown:
        for category in unknown:
            print(f"- {category}")
    elif registered:
        print("- None")
    else:
        print("- Registry missing or no registered categories found")

    print("\nPossible duplicate category strings by simple normalization:")
    if duplicates:
        for values in sorted(duplicates.values(), key=lambda item: item[0]):
            print("- " + ", ".join(sorted(values)))
    else:
        print("- None")

    print("\nPages with no categories:")
    if no_categories:
        for path in no_categories:
            print(f"- {path.relative_to(ROOT).as_posix()}")
    else:
        print("- None")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
