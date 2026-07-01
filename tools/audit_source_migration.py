#!/usr/bin/env python3
"""Audit source pages for semantic-pipeline migration coverage."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
WIKI_DIR = ROOT / "wiki"
SOURCE_DIR = WIKI_DIR / "sources"
DASHBOARD_PATH = WIKI_DIR / "dashboards" / "source-migration-status.md"
GENERATED_DATE = "2026-07-01"

WIKILINK_RE = re.compile(r"!?\[\[([^\]]+)\]\]")
SOURCE_ID_RE = re.compile(r"SRC-\d{4}")
CLAIM_SECTIONS = {"claims", "claim links"}
QUESTION_SECTIONS = {"questions", "open questions", "question links"}
TENSION_SECTIONS = {"tensions", "contradictions / tensions", "tension links"}
VALID_CITATION_STATUSES = {"unchecked", "partial", "reviewed"}
VALID_METADATA_REVIEW_STATUSES = {"unchecked", "partial", "reviewed", "not-applicable"}
VALID_CQT_REVIEW_STATUSES = {"unchecked", "none-needed", "source-local", "linked"}
MIGRATED_CQT_REVIEW_STATUSES = {"none-needed", "source-local", "linked"}


@dataclass(frozen=True)
class Page:
    path: Path
    page_id: str
    frontmatter: dict[str, Any]
    body: list[str]
    text: str


@dataclass(frozen=True)
class SourceAudit:
    source_id: str
    label: str
    path: Path
    page_id: str
    source_path_status: str
    raw_source_exists: str
    authors_status: str
    year_status: str
    metadata_review_status: str
    citation_match_status: str
    cqt_review_status: str
    cites_sources_count: int
    linked_claims_count: int
    linked_questions_count: int
    linked_tensions_count: int
    source_bundle_status: str
    coverage_profile: str
    ingestion_status: str
    graph_density_proxy: int
    metadata_backfill_reasons: tuple[str, ...]
    citation_review_reasons: tuple[str, ...]
    partial_citation_review_reasons: tuple[str, ...]
    cqt_review_reasons: tuple[str, ...]
    raw_file_reasons: tuple[str, ...]
    manual_review_reasons: tuple[str, ...]

    @property
    def needs_metadata_backfill(self) -> bool:
        return bool(self.metadata_backfill_reasons)

    @property
    def needs_citation_review(self) -> bool:
        return bool(self.citation_review_reasons)

    @property
    def has_partial_citation_review(self) -> bool:
        return bool(self.partial_citation_review_reasons)

    @property
    def needs_cqt_review(self) -> bool:
        return bool(self.cqt_review_reasons)

    @property
    def has_missing_raw_source_file(self) -> bool:
        return bool(self.raw_file_reasons)

    @property
    def needs_manual_review(self) -> bool:
        return bool(self.manual_review_reasons)

    @property
    def appears_current(self) -> bool:
        return not (
            self.needs_metadata_backfill
            or self.needs_citation_review
            or self.has_partial_citation_review
            or self.needs_cqt_review
            or self.has_missing_raw_source_file
            or self.needs_manual_review
        )


def unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def parse_scalar(value: str) -> Any:
    value = value.strip()
    if value == "[]":
        return []
    if value in {"true", "false"}:
        return value == "true"
    return unquote(value)


def parse_frontmatter(text: str) -> tuple[dict[str, Any], list[str]]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, lines
    try:
        end = next(i for i, line in enumerate(lines[1:], 1) if line.strip() == "---")
    except StopIteration:
        return {}, lines

    data: dict[str, Any] = {}
    key: str | None = None
    for line in lines[1:end]:
        if not line.strip():
            continue
        if not line.startswith(" ") and ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            data[key] = parse_scalar(value) if value else []
        elif key and line.strip().startswith("- "):
            current = data.setdefault(key, [])
            if not isinstance(current, list):
                current = [current]
                data[key] = current
            current.append(unquote(line.strip()[2:].strip()))
    return data, lines[end + 1 :]


def as_list(value: Any) -> list[str]:
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    if isinstance(value, str) and value.strip():
        return [value.strip()]
    return []


def h1(lines: list[str]) -> str:
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def page_id(path: Path) -> str:
    return path.relative_to(ROOT).with_suffix("").as_posix()


def wiki_link(path: Path, label: str) -> str:
    target = path.relative_to(ROOT).with_suffix("").as_posix()
    return f"[[{target}|{label}]]"


def clean_wikilink(value: str) -> str:
    match = WIKILINK_RE.search(value)
    if match:
        return match.group(1).split("|", 1)[0].split("#", 1)[0].strip()
    return value.split("|", 1)[0].split("#", 1)[0].strip()


def source_sort_key(source: SourceAudit) -> tuple[int, str]:
    match = re.match(r"^SRC-(\d{4})$", source.source_id)
    return (int(match.group(1)) if match else 10**9, source.source_id)


def load_wiki_pages() -> list[Page]:
    pages: list[Page] = []
    for path in sorted(WIKI_DIR.rglob("*.md")):
        if ".obsidian" in path.parts or path.name.startswith("."):
            continue
        text = path.read_text(encoding="utf-8")
        frontmatter, body = parse_frontmatter(text)
        pages.append(Page(path=path, page_id=page_id(path), frontmatter=frontmatter, body=body, text=text))
    return pages


def source_label(page: Page) -> str:
    for key in ("short_title", "display_title"):
        value = page.frontmatter.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    return h1(page.body) or page.path.stem.replace("-", " ").title()


def section_targets(body: list[str], headings: set[str]) -> set[str]:
    active = False
    targets: set[str] = set()
    for line in body:
        if line.startswith("## "):
            title = line[3:].strip().casefold()
            active = title in headings
            continue
        if active:
            targets.update(clean_wikilink(match.group(1)) for match in WIKILINK_RE.finditer(line))
    return {target for target in targets if target}


def build_backrefs(pages: list[Page]) -> dict[str, dict[str, set[str]]]:
    backrefs: dict[str, dict[str, set[str]]] = {
        "claim": {},
        "question": {},
        "tension": {},
    }
    for page in pages:
        page_type = str(page.frontmatter.get("type", "")).strip()
        if page_type not in backrefs:
            continue
        for source_id in as_list(page.frontmatter.get("sources", [])):
            if SOURCE_ID_RE.fullmatch(source_id):
                backrefs[page_type].setdefault(source_id, set()).add(page.page_id)
    return backrefs


def count_linked_items(
    source: Page,
    source_id: str,
    backrefs: dict[str, dict[str, set[str]]],
    page_type: str,
    headings: set[str],
) -> int:
    targets = section_targets(source.body, headings)
    targets.update(backrefs.get(page_type, {}).get(source_id, set()))
    return len(targets)


def raw_source_exists(frontmatter: dict[str, Any]) -> tuple[str, str]:
    source_path = str(frontmatter.get("source_path", "")).strip()
    if not source_path:
        return "missing", "no"
    candidate = ROOT / source_path.strip('"').strip("'")
    return "present", "yes" if candidate.is_file() else "no"


def authors_status(frontmatter: dict[str, Any]) -> str:
    authors = as_list(frontmatter.get("authors", []))
    author_entities = as_list(frontmatter.get("author_entities", []))
    if authors and author_entities:
        return "entity-linked"
    if authors:
        return "present"
    return "missing"


def citation_status(frontmatter: dict[str, Any]) -> str:
    value = str(frontmatter.get("citation_match_status", "")).strip()
    return value if value else "missing"


def metadata_review_status(frontmatter: dict[str, Any]) -> str:
    value = str(frontmatter.get("metadata_review_status", "")).strip()
    return value if value else "missing"


def cqt_review_status(frontmatter: dict[str, Any]) -> str:
    value = str(frontmatter.get("cqt_review_status", "")).strip()
    return value if value else "missing"


def bundle_status(frontmatter: dict[str, Any]) -> str:
    bundle = str(frontmatter.get("source_bundle", "")).strip()
    role = str(frontmatter.get("bundle_role", "")).strip()
    if bundle and role:
        return f"present ({bundle}; {role})"
    if bundle:
        return f"present ({bundle}; role missing)"
    if role:
        return f"role only ({role})"
    return "none"


def graph_density_proxy(frontmatter: dict[str, Any], text: str) -> int:
    related_count = len(as_list(frontmatter.get("related", [])))
    source_ref_count = len(SOURCE_ID_RE.findall(text))
    wikilink_count = len(WIKILINK_RE.findall(text))
    return related_count + source_ref_count + wikilink_count


def audit_sources() -> list[SourceAudit]:
    pages = load_wiki_pages()
    backrefs = build_backrefs(pages)
    audits: list[SourceAudit] = []
    for page in sorted((item for item in pages if item.path.parent == SOURCE_DIR), key=lambda item: item.path.name):
        if str(page.frontmatter.get("type", "")).strip() != "source":
            continue
        source_id = str(page.frontmatter.get("source_id", "")).strip()
        source_path_status, raw_exists = raw_source_exists(page.frontmatter)
        author_status = authors_status(page.frontmatter)
        year_status = "present" if str(page.frontmatter.get("year", "")).strip() else "missing"
        metadata_status = metadata_review_status(page.frontmatter)
        citation_match_status = citation_status(page.frontmatter)
        cqt_status = cqt_review_status(page.frontmatter)
        linked_claims = count_linked_items(page, source_id, backrefs, "claim", CLAIM_SECTIONS)
        linked_questions = count_linked_items(page, source_id, backrefs, "question", QUESTION_SECTIONS)
        linked_tensions = count_linked_items(page, source_id, backrefs, "tension", TENSION_SECTIONS)
        coverage_profile = str(page.frontmatter.get("coverage_profile", "")).strip() or "missing"
        ingestion_status = str(page.frontmatter.get("ingestion_status", "")).strip() or "missing"

        metadata_reasons: list[str] = []
        if not source_id:
            metadata_reasons.append("missing source_id")
        if source_path_status == "missing":
            metadata_reasons.append("missing source_path")
        if source_path_status == "present" and raw_exists == "no":
            metadata_reasons.append("source_path file is missing")
        metadata_review_satisfies = metadata_status in {"reviewed", "not-applicable"}
        bibliographic_metadata_satisfies = author_status != "missing" and year_status == "present"
        if not metadata_review_satisfies and not bibliographic_metadata_satisfies:
            metadata_reasons.append("missing authors/year or metadata_review_status")

        citation_reasons: list[str] = []
        partial_citation_reasons: list[str] = []
        if citation_match_status == "missing":
            citation_reasons.append("missing citation_match_status")
        elif citation_match_status == "unchecked":
            citation_reasons.append(f"citation_match_status is {citation_match_status}")
        elif citation_match_status == "partial":
            partial_citation_reasons.append("citation_match_status is partial")

        cqt_reasons: list[str] = []
        if cqt_status == "missing":
            cqt_reasons.append("missing cqt_review_status")
        elif cqt_status == "unchecked":
            cqt_reasons.append("cqt_review_status is unchecked")

        raw_reasons: list[str] = []
        if source_path_status == "present" and raw_exists == "no":
            raw_reasons.append("source_path file is missing")

        manual_reasons: list[str] = []
        if not source_id:
            manual_reasons.append("cannot assign stable source identity")
        if metadata_status not in VALID_METADATA_REVIEW_STATUSES and metadata_status != "missing":
            manual_reasons.append(f"unknown metadata_review_status `{metadata_status}`")
        if citation_match_status not in VALID_CITATION_STATUSES and citation_match_status != "missing":
            manual_reasons.append(f"unknown citation_match_status `{citation_match_status}`")
        if cqt_status not in VALID_CQT_REVIEW_STATUSES and cqt_status != "missing":
            manual_reasons.append(f"unknown cqt_review_status `{cqt_status}`")
        if cqt_status == "linked" and linked_claims + linked_questions + linked_tensions == 0:
            manual_reasons.append("cqt_review_status is linked but no first-class claim/question/tension links were found")
        if bundle_status(page.frontmatter).startswith("role only") or "role missing" in bundle_status(page.frontmatter):
            manual_reasons.append("incomplete source_bundle metadata")
        if ingestion_status not in {"complete", "partial", "needs-review", "missing"}:
            manual_reasons.append(f"unknown ingestion_status `{ingestion_status}`")
        if coverage_profile not in {"minimal", "standard", "deep", "math-standard", "math-deep", "missing"}:
            manual_reasons.append(f"unknown coverage_profile `{coverage_profile}`")

        audits.append(
            SourceAudit(
                source_id=source_id or page.path.stem,
                label=source_label(page),
                path=page.path,
                page_id=page.page_id,
                source_path_status=source_path_status,
                raw_source_exists=raw_exists,
                authors_status=author_status,
                year_status=year_status,
                metadata_review_status=metadata_status,
                citation_match_status=citation_match_status,
                cqt_review_status=cqt_status,
                cites_sources_count=len(as_list(page.frontmatter.get("cites_sources", []))),
                linked_claims_count=linked_claims,
                linked_questions_count=linked_questions,
                linked_tensions_count=linked_tensions,
                source_bundle_status=bundle_status(page.frontmatter),
                coverage_profile=coverage_profile,
                ingestion_status=ingestion_status,
                graph_density_proxy=graph_density_proxy(page.frontmatter, page.text),
                metadata_backfill_reasons=tuple(metadata_reasons),
                citation_review_reasons=tuple(citation_reasons),
                partial_citation_review_reasons=tuple(partial_citation_reasons),
                cqt_review_reasons=tuple(cqt_reasons),
                raw_file_reasons=tuple(raw_reasons),
                manual_review_reasons=tuple(manual_reasons),
            )
        )
    return sorted(audits, key=source_sort_key)


def status_tags(source: SourceAudit) -> str:
    tags: list[str] = []
    if source.needs_metadata_backfill:
        tags.append("metadata")
    if source.needs_citation_review:
        tags.append("citation")
    if source.has_partial_citation_review:
        tags.append("partial-citation")
    if source.needs_cqt_review:
        tags.append("claims/questions/tensions")
    if source.has_missing_raw_source_file:
        tags.append("raw-missing")
    if source.needs_manual_review:
        tags.append("manual")
    if source.appears_current:
        tags.append("current")
    return ", ".join(tags)


def reason_text(reasons: tuple[str, ...]) -> str:
    return "; ".join(reasons) if reasons else "none"


def render_group(title: str, sources: list[SourceAudit], reason_getter) -> list[str]:
    lines = [f"## {title}", ""]
    if not sources:
        lines.extend(["- None", ""])
        return lines
    for source in sources:
        reason = reason_getter(source)
        suffix = f" - {reason}" if reason else ""
        lines.append(f"- {wiki_link(source.path, source.label)} (`{source.source_id}`){suffix}")
    lines.append("")
    return lines


def render_inventory_table(sources: list[SourceAudit]) -> list[str]:
    lines = [
        "## Full Inventory",
        "",
        "| Source | source_path | raw | authors | year | metadata review | citation | C/Q/T review | cites | claims | questions | tensions | bundle | coverage | ingestion | graph proxy | status |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | ---: | --- |",
    ]
    for source in sources:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"{wiki_link(source.path, source.label)}<br>`{source.source_id}`",
                    source.source_path_status,
                    source.raw_source_exists,
                    source.authors_status,
                    source.year_status,
                    source.metadata_review_status,
                    source.citation_match_status,
                    source.cqt_review_status,
                    str(source.cites_sources_count),
                    str(source.linked_claims_count),
                    str(source.linked_questions_count),
                    str(source.linked_tensions_count),
                    source.source_bundle_status.replace("|", "\\|"),
                    source.coverage_profile,
                    source.ingestion_status,
                    str(source.graph_density_proxy),
                    status_tags(source),
                ]
            )
            + " |"
        )
    lines.append("")
    return lines


def write_dashboard(sources: list[SourceAudit]) -> None:
    DASHBOARD_PATH.parent.mkdir(parents=True, exist_ok=True)
    metadata = [source for source in sources if source.needs_metadata_backfill]
    citation = [source for source in sources if source.needs_citation_review]
    partial_citation = [source for source in sources if source.has_partial_citation_review]
    cqt = [source for source in sources if source.needs_cqt_review]
    current = [source for source in sources if source.appears_current]
    missing_raw = [source for source in sources if source.has_missing_raw_source_file]
    manual = [source for source in sources if source.needs_manual_review]

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
        "  - dashboard",
        "  - generated",
        "  - source-migration",
        "related:",
        '  - "[[wiki/index]]"',
        '  - "[[wiki/dashboards/source-citation-links]]"',
        "sources: []",
        "sensitivity: public",
        "encryption: none",
        "graph_exclude: true",
        "generated: true",
        "dashboard: source-migration-status",
        "---",
        "",
        "# Source Migration Status",
        "",
        "This dashboard is generated by `python3 tools/audit_source_migration.py`.",
        "",
        "It inventories older source pages for semantic-pipeline backfill without re-ingesting or rewriting source summaries.",
        "",
        "## Summary",
        "",
        f"- Total source pages: {len(sources)}",
        f"- Needing metadata backfill: {len(metadata)}",
        f"- Needing citation review: {len(citation)}",
        f"- Partial citation review: {len(partial_citation)}",
        f"- Needing claims/questions/tensions review: {len(cqt)}",
        f"- Appearing current: {len(current)}",
        f"- Missing raw source files: {len(missing_raw)}",
        f"- Needing manual review: {len(manual)}",
        "",
    ]
    lines.extend(render_group("Needs Metadata Backfill", metadata, lambda source: reason_text(source.metadata_backfill_reasons)))
    lines.extend(render_group("Needs Citation Review", citation, lambda source: reason_text(source.citation_review_reasons)))
    lines.extend(
        render_group(
            "Partial Citation Review",
            partial_citation,
            lambda source: reason_text(source.partial_citation_review_reasons),
        )
    )
    lines.extend(
        render_group(
            "Needs Claims/Questions/Tensions Review",
            cqt,
            lambda source: reason_text(source.cqt_review_reasons),
        )
    )
    lines.extend(render_group("Appears Current", current, lambda source: ""))
    lines.extend(render_group("Has Missing Raw Source File", missing_raw, lambda source: reason_text(source.raw_file_reasons)))
    lines.extend(render_group("Needs Manual Review", manual, lambda source: reason_text(source.manual_review_reasons)))
    lines.extend(render_inventory_table(sources))
    DASHBOARD_PATH.write_text("\n".join(lines), encoding="utf-8")


def print_report(sources: list[SourceAudit]) -> None:
    metadata = [source for source in sources if source.needs_metadata_backfill]
    citation = [source for source in sources if source.needs_citation_review]
    partial_citation = [source for source in sources if source.has_partial_citation_review]
    cqt = [source for source in sources if source.needs_cqt_review]
    current = [source for source in sources if source.appears_current]
    missing_raw = [source for source in sources if source.has_missing_raw_source_file]

    print("# Source Migration Audit")
    print()
    print(f"Dashboard: {DASHBOARD_PATH.relative_to(ROOT)}")
    print(f"Total source pages: {len(sources)}")
    print(f"Needing metadata backfill: {len(metadata)}")
    print(f"Needing citation review: {len(citation)}")
    print(f"Partial citation review: {len(partial_citation)}")
    print(f"Needing claims/questions/tensions review: {len(cqt)}")
    print(f"Appearing current: {len(current)}")
    print(f"Missing raw source files: {len(missing_raw)}")
    print()
    print("| source_id | title | source_path | raw | authors | year | metadata review | citation | C/Q/T review | cites | claims | questions | tensions | bundle | coverage | ingestion | graph proxy | status |")
    print("| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | ---: | --- |")
    for source in sources:
        print(
            "| "
            + " | ".join(
                [
                    source.source_id,
                    source.label.replace("|", "\\|"),
                    source.source_path_status,
                    source.raw_source_exists,
                    source.authors_status,
                    source.year_status,
                    source.metadata_review_status,
                    source.citation_match_status,
                    source.cqt_review_status,
                    str(source.cites_sources_count),
                    str(source.linked_claims_count),
                    str(source.linked_questions_count),
                    str(source.linked_tensions_count),
                    source.source_bundle_status.replace("|", "\\|"),
                    source.coverage_profile,
                    source.ingestion_status,
                    str(source.graph_density_proxy),
                    status_tags(source),
                ]
            )
            + " |"
        )
    if missing_raw:
        print()
        print("## Missing Raw Source Files")
        print()
        for source in missing_raw:
            print(f"- {source.source_id}: {source.page_id}")


def main() -> int:
    sources = audit_sources()
    write_dashboard(sources)
    print_report(sources)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
