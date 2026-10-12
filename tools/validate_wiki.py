#!/usr/bin/env python3
"""Validate the minimal LLM wiki scaffold."""

from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path

from wiki_currency import currency_issues, currency_metadata, index_marker_issues
from wiki_markdown import parse_frontmatter


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
VALID_PAGE_TYPES = {
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
LOCAL_PATH_RE = re.compile(r"/lmb/home/|/home/")


def has_frontmatter(path: Path) -> bool:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return False
    return any(line.strip() == "---" for line in lines[1:])


def frontmatter_value(path: Path, key: str) -> str | None:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return None

    for line in lines[1:]:
        if line.strip() == "---":
            return None
        if line.startswith(f"{key}:"):
            return line.split(":", 1)[1].strip()
    return None


def frontmatter_lines(path: Path) -> list[str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return []
    try:
        end = next(i for i, line in enumerate(lines[1:], 1) if line.strip() == "---")
    except StopIteration:
        return []
    return lines[1:end]


def has_frontmatter_key(path: Path, key: str) -> bool:
    return any(line.startswith(f"{key}:") for line in frontmatter_lines(path))


def wiki_markdown_pages() -> list[Path]:
    return [
        path
        for path in (ROOT / "wiki").rglob("*.md")
        if ".git" not in path.parts and not path.name.startswith(".")
    ]


def skill_files() -> list[Path]:
    return sorted((ROOT / ".agents" / "skills").glob("*/SKILL.md"))


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

    for path in skill_files():
        if not has_frontmatter(path):
            errors.append(f"Skill file missing YAML frontmatter: {path.relative_to(ROOT)}")
            continue
        for key in ("name", "description"):
            if not has_frontmatter_key(path, key):
                errors.append(f"Skill file missing {key}: {path.relative_to(ROOT)}")

    for path in wiki_pages:
        if path not in FRONTMATTER_EXEMPT and not has_frontmatter(path):
            errors.append(f"Missing YAML frontmatter: {path.relative_to(ROOT)}")
            continue

        page_type = frontmatter_value(path, "type")
        if page_type and page_type not in VALID_PAGE_TYPES:
            errors.append(f"Unknown page type in {path.relative_to(ROOT)}: {page_type}")

        source_path = frontmatter_value(path, "source_path")
        if source_path:
            candidate = ROOT / source_path.strip().strip('"').strip("'")
            if not candidate.is_file():
                errors.append(f"Source page source_path does not exist in {path.relative_to(ROOT)}: {source_path}")

    currency_by_target: dict[str, str | None] = {}
    for path in wiki_pages:
        text = path.read_text(encoding="utf-8")
        if LOCAL_PATH_RE.search(text):
            errors.append(f"Wiki Markdown contains local absolute path: {path.relative_to(ROOT)}")
        if OBSIDIAN_DISCOURAGED_MATH_RE.search(text):
            warnings.append(
                "Obsidian math warning in "
                f"{path.relative_to(ROOT)}: prefer $$ display math over \\[ ... \\]"
            )
        if path not in FRONTMATTER_EXEMPT:
            frontmatter, body_lines = parse_frontmatter(text)
            page_errors, page_warnings = currency_issues(frontmatter, body_lines, date.today())
            rel = path.relative_to(ROOT)
            currency_by_target[rel.with_suffix("").as_posix()] = currency_metadata(frontmatter)["currency"]
            errors.extend(f"Currency in {rel}: {message}" for message in page_errors)
            warnings.extend(f"Currency in {rel}: {message}" for message in page_warnings)
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

    index_page = ROOT / "wiki" / "index.md"
    if index_page.is_file():
        index_lines = index_page.read_text(encoding="utf-8").split("\n")
        errors.extend(
            f"Currency marker in wiki/index.md {message}"
            for message in index_marker_issues(index_lines, currency_by_target)
        )

    navigation_pages = {
        ROOT / "wiki" / "index.md",
        ROOT / "wiki" / "log.md",
    }
    navigation_pages.update((ROOT / "wiki").rglob("README.md"))
    navigation_pages.update((ROOT / "wiki" / "dashboards").rglob("*.md"))
    navigation_pages.discard(ROOT / "wiki" / "categories" / "README.md")
    for path in sorted(path for path in navigation_pages if path.exists()):
        if frontmatter_value(path, "graph_exclude") != "true":
            errors.append(f"Navigation page missing graph_exclude: true: {path.relative_to(ROOT)}")

    for path in sorted((ROOT / "wiki" / "dashboards").rglob("*.md")):
        if frontmatter_value(path, "generated") == "true":
            if frontmatter_value(path, "graph_exclude") != "true":
                errors.append(f"Generated dashboard missing graph_exclude: true: {path.relative_to(ROOT)}")

    for path in sorted((ROOT / "wiki" / "graph").rglob("*.md")):
        if frontmatter_value(path, "graph_exclude") != "true":
            errors.append(f"Generated graph Markdown missing graph_exclude: true: {path.relative_to(ROOT)}")

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
