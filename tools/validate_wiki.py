#!/usr/bin/env python3
"""Validate the minimal LLM wiki scaffold."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_DIRS = [
    "tests",
    "wiki",
    "schema",
    "tools",
    "raw/sources",
]
REQUIRED_FILES = [
    "wiki/index.md",
    "wiki/log.md",
]
FRONTMATTER_EXEMPT = {
    ROOT / "wiki" / "index.md",
    ROOT / "wiki" / "log.md",
}
WIKILINK_RE = re.compile(r"!?\[\[([^\]]+)\]\]")
SOURCE_QA_SECTION = "## Ingestion QA"
EQUATION_INVENTORY_SECTION = "## Equation inventory"
OBSIDIAN_DISCOURAGED_MATH_RE = re.compile(r"\\\[|\\\]")


def has_frontmatter(path: Path) -> bool:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return False
    return any(line.strip() == "---" for line in lines[1:])


def wiki_markdown_pages() -> list[Path]:
    return [
        path
        for path in (ROOT / "wiki").rglob("*.md")
        if ".git" not in path.parts and not path.name.startswith(".")
    ]


def build_link_index(paths: list[Path]) -> set[str]:
    index: set[str] = set()
    for path in paths:
        rel = path.relative_to(ROOT).as_posix()
        index.add(rel)
        index.add(rel.removesuffix(".md"))
        index.add(path.stem)
    return index


def target_exists(target: str, link_index: set[str]) -> bool:
    target = target.split("|", 1)[0].split("#", 1)[0].split("^", 1)[0].strip()
    if not target:
        return True

    path_target = target if Path(target).suffix else f"{target}.md"
    if target in link_index or path_target in link_index:
        return True

    candidate = ROOT / path_target
    if candidate.exists():
        return True

    basename = Path(target).stem
    return basename in link_index


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    for directory in REQUIRED_DIRS:
        if not (ROOT / directory).is_dir():
            errors.append(f"Missing required directory: {directory}")

    for file_path in REQUIRED_FILES:
        if not (ROOT / file_path).is_file():
            errors.append(f"Missing required file: {file_path}")

    wiki_pages = sorted(wiki_markdown_pages())
    for path in wiki_pages:
        if path not in FRONTMATTER_EXEMPT and not has_frontmatter(path):
            errors.append(f"Missing YAML frontmatter: {path.relative_to(ROOT)}")

    for path in wiki_pages:
        text = path.read_text(encoding="utf-8")
        if OBSIDIAN_DISCOURAGED_MATH_RE.search(text):
            warnings.append(
                "Obsidian math warning in "
                f"{path.relative_to(ROOT)}: prefer $$ display math over \\[ ... \\]"
            )
        if "ingestion_status: complete" in text and SOURCE_QA_SECTION not in text:
            errors.append(f"Complete source page missing ingestion QA section: {path.relative_to(ROOT)}")
        if (
            path.parent == ROOT / "wiki" / "sources"
            and (
                "coverage_profile: math-standard" in text
                or "coverage_profile: math-deep" in text
            )
            and EQUATION_INVENTORY_SECTION not in text
        ):
            errors.append(f"Math-heavy source page missing equation inventory section: {path.relative_to(ROOT)}")

    link_index = build_link_index(wiki_pages)
    for path in wiki_pages:
        text = path.read_text(encoding="utf-8")
        for match in WIKILINK_RE.finditer(text):
            target = match.group(1)
            if not target_exists(target, link_index):
                rel = path.relative_to(ROOT)
                errors.append(f"Broken wikilink in {rel}: [[{target}]]")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    for warning in warnings:
        print(f"WARN: {warning}", file=sys.stderr)

    print("Wiki validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
