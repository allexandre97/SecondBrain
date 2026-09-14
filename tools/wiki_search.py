#!/usr/bin/env python3
"""Deterministic section-level SQLite FTS5 search for the local wiki."""

from __future__ import annotations

import json
import os
import re
import sqlite3
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

from wiki_markdown import as_list, parse_frontmatter


SCHEMA_VERSION = "1"
INDEX_DIRNAME = ".cache"
INDEX_NAME = "wiki-search.sqlite3"
GENERATED_INDEX_NAME = "wiki-search-generated.sqlite3"
# FTS columns: section_id (UNINDEXED), title, aliases, heading, metadata, body.
BM25_WEIGHTS = (0.0, 12.0, 8.0, 6.0, 3.0, 1.0)
DEFAULT_PER_PAGE = 2
HEADING_RE = re.compile(r"^ {0,3}(#{1,6})(?:[ \t]+(.*)|[ \t]*)$")
FENCE_RE = re.compile(r"^ {0,3}(`{3,}|~{3,})")
TOKEN_RE = re.compile(r"[^\W_]+(?:['’][^\W_]+)*", re.UNICODE)


class SearchError(RuntimeError):
    pass


@dataclass(frozen=True)
class Section:
    heading: str
    section_path: str
    order: int
    body: str


@dataclass(frozen=True)
class SearchResponse:
    query: str
    match_mode: str
    results: list[dict[str, Any]]


def ensure_fts5() -> None:
    try:
        connection = sqlite3.connect(":memory:")
        try:
            connection.execute("CREATE VIRTUAL TABLE fts5_check USING fts5(value)")
        finally:
            connection.close()
    except sqlite3.Error as error:
        raise SearchError(
            "SQLite FTS5 support is required. Use a Python sqlite3 build with FTS5 enabled."
        ) from error


def wiki_files(root: Path) -> list[Path]:
    wiki_dir = root / "wiki"
    if not wiki_dir.is_dir():
        raise SearchError(f"wiki/ directory not found under {root}")
    paths = [
        path
        for path in wiki_dir.rglob("*.md")
        if not any(part.startswith(".") for part in path.relative_to(wiki_dir).parts)
        and "__pycache__" not in path.parts
    ]
    return sorted(paths, key=lambda path: path.relative_to(root).as_posix())


def corpus_manifest(root: Path) -> list[tuple[str, int, int]]:
    manifest = []
    for path in wiki_files(root):
        stat = path.stat()
        manifest.append((path.relative_to(root).as_posix(), stat.st_size, stat.st_mtime_ns))
    return manifest


def index_path(root: Path, include_generated: bool = False) -> Path:
    name = GENERATED_INDEX_NAME if include_generated else INDEX_NAME
    return root / INDEX_DIRNAME / name


def _clean_heading(value: str) -> str:
    return re.sub(r"[ \t]+#+[ \t]*$", "", value.strip())


def parse_sections(lines: list[str]) -> tuple[str, list[Section]]:
    """Split Markdown on ATX headings while leaving fenced-code headings untouched."""
    raw_sections: list[tuple[int, str, list[str]]] = []
    current_level = 0
    current_heading = ""
    current_body: list[str] = []
    hierarchy: list[tuple[int, str]] = []
    section_paths: list[str] = []
    fence_marker = ""

    def finish() -> None:
        body = "\n".join(current_body).strip()
        if current_heading or body:
            raw_sections.append((current_level, current_heading, list(current_body)))
            section_paths.append(" > ".join(value for _level, value in hierarchy))

    for line in lines:
        if fence_marker:
            current_body.append(line)
            closing_fence = re.match(
                rf"^ {{0,3}}{re.escape(fence_marker[0])}{{{len(fence_marker)},}}[ \t]*$",
                line,
            )
            if closing_fence:
                fence_marker = ""
            continue

        fence = FENCE_RE.match(line)
        if fence:
            fence_marker = fence.group(1)
            current_body.append(line)
            continue

        heading_match = HEADING_RE.match(line)
        if not heading_match:
            current_body.append(line)
            continue

        finish()
        level = len(heading_match.group(1))
        heading = _clean_heading(heading_match.group(2) or "")
        hierarchy = [(old_level, value) for old_level, value in hierarchy if old_level < level]
        hierarchy.append((level, heading))
        current_level = level
        current_heading = heading
        current_body = []

    finish()
    title = next((heading for level, heading, _body in raw_sections if level == 1 and heading), "")
    sections = [
        Section(
            heading=heading,
            section_path=section_paths[order],
            order=order,
            body="\n".join(body).strip(),
        )
        for order, (_level, heading, body) in enumerate(raw_sections)
    ]
    if not sections:
        sections = [Section(heading="", section_path="", order=0, body="")]
    return title, sections


def _scalar(frontmatter: dict[str, Any], key: str) -> str:
    value = frontmatter.get(key, "")
    return value.strip() if isinstance(value, str) else ""


def _is_generated(frontmatter: dict[str, Any]) -> bool:
    value = frontmatter.get("generated", False)
    return value is True or (isinstance(value, str) and value.lower() == "true")


def _unique(values: Iterable[str]) -> list[str]:
    return list(dict.fromkeys(value.strip() for value in values if value.strip()))


def _create_schema(connection: sqlite3.Connection) -> None:
    connection.executescript(
        """
        CREATE TABLE metadata (key TEXT PRIMARY KEY, value TEXT NOT NULL);
        CREATE TABLE manifest (path TEXT PRIMARY KEY, size INTEGER NOT NULL, mtime_ns INTEGER NOT NULL);
        CREATE TABLE pages (
            id INTEGER PRIMARY KEY,
            path TEXT NOT NULL UNIQUE,
            title TEXT NOT NULL,
            page_type TEXT NOT NULL,
            status TEXT NOT NULL,
            source_id TEXT NOT NULL,
            aliases_json TEXT NOT NULL,
            categories_json TEXT NOT NULL,
            tags_json TEXT NOT NULL
        );
        CREATE TABLE page_categories (page_id INTEGER NOT NULL, value TEXT NOT NULL, PRIMARY KEY(page_id, value));
        CREATE TABLE page_tags (page_id INTEGER NOT NULL, value TEXT NOT NULL, PRIMARY KEY(page_id, value));
        CREATE TABLE page_sources (page_id INTEGER NOT NULL, value TEXT NOT NULL, PRIMARY KEY(page_id, value));
        CREATE TABLE sections (
            id INTEGER PRIMARY KEY,
            page_id INTEGER NOT NULL,
            path TEXT NOT NULL,
            title TEXT NOT NULL,
            section TEXT NOT NULL,
            section_path TEXT NOT NULL,
            section_order INTEGER NOT NULL,
            page_type TEXT NOT NULL,
            status TEXT NOT NULL,
            source_id TEXT NOT NULL,
            aliases_json TEXT NOT NULL,
            categories_json TEXT NOT NULL,
            tags_json TEXT NOT NULL
        );
        CREATE VIRTUAL TABLE section_fts USING fts5(
            section_id UNINDEXED,
            title,
            aliases,
            heading,
            metadata,
            body,
            tokenize='unicode61 remove_diacritics 2'
        );
        CREATE INDEX sections_page_id ON sections(page_id);
        CREATE INDEX sections_path_order ON sections(path, section_order);
        CREATE INDEX pages_type ON pages(page_type);
        CREATE INDEX pages_status ON pages(status);
        CREATE INDEX categories_value ON page_categories(value, page_id);
        CREATE INDEX tags_value ON page_tags(value, page_id);
        CREATE INDEX sources_value ON page_sources(value, page_id);
        """
    )


def build_index(root: Path, include_generated: bool = False) -> Path:
    ensure_fts5()
    root = root.resolve()
    manifest = corpus_manifest(root)
    destination = index_path(root, include_generated)
    destination.parent.mkdir(parents=True, exist_ok=True)
    file_descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{destination.name}.", suffix=".tmp", dir=destination.parent
    )
    os.close(file_descriptor)
    temporary = Path(temporary_name)

    try:
        connection = sqlite3.connect(temporary)
        try:
            _create_schema(connection)
            connection.execute("INSERT INTO metadata VALUES (?, ?)", ("schema_version", SCHEMA_VERSION))
            connection.execute(
                "INSERT INTO metadata VALUES (?, ?)",
                ("include_generated", "1" if include_generated else "0"),
            )
            connection.executemany("INSERT INTO manifest VALUES (?, ?, ?)", manifest)

            page_id = 0
            section_id = 0
            for relative_path, _size, _mtime_ns in manifest:
                path = root / relative_path
                text = path.read_text(encoding="utf-8", errors="replace")
                frontmatter, body_lines = parse_frontmatter(text)
                if _is_generated(frontmatter) and not include_generated:
                    continue

                h1_title, sections = parse_sections(body_lines)
                display_title = _scalar(frontmatter, "display_title")
                short_title = _scalar(frontmatter, "short_title")
                title = h1_title or display_title or short_title or path.stem.replace("-", " ").title()
                title_terms = _unique([title, display_title, short_title])
                aliases = _unique(as_list(frontmatter.get("aliases", [])))
                categories = _unique(as_list(frontmatter.get("categories", [])))
                tags = _unique(as_list(frontmatter.get("tags", [])))
                areas = _unique(as_list(frontmatter.get("areas", [])))
                sources = _unique(as_list(frontmatter.get("sources", [])))
                source_id = _scalar(frontmatter, "source_id")
                if source_id:
                    sources = _unique([source_id, *sources])
                page_type = _scalar(frontmatter, "type")
                status = _scalar(frontmatter, "status")
                aliases_json = json.dumps(aliases, ensure_ascii=False)
                categories_json = json.dumps(categories, ensure_ascii=False)
                tags_json = json.dumps(tags, ensure_ascii=False)

                page_id += 1
                connection.execute(
                    "INSERT INTO pages VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (
                        page_id,
                        relative_path,
                        title,
                        page_type,
                        status,
                        source_id,
                        aliases_json,
                        categories_json,
                        tags_json,
                    ),
                )
                connection.executemany(
                    "INSERT INTO page_categories VALUES (?, ?)",
                    [(page_id, value) for value in categories],
                )
                connection.executemany(
                    "INSERT INTO page_tags VALUES (?, ?)", [(page_id, value) for value in tags]
                )
                connection.executemany(
                    "INSERT INTO page_sources VALUES (?, ?)", [(page_id, value) for value in sources]
                )
                metadata = " ".join(_unique([*categories, *tags, *areas, *sources]))
                for section in sections:
                    section_id += 1
                    connection.execute(
                        "INSERT INTO sections VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                        (
                            section_id,
                            page_id,
                            relative_path,
                            title,
                            section.heading,
                            section.section_path,
                            section.order,
                            page_type,
                            status,
                            source_id,
                            aliases_json,
                            categories_json,
                            tags_json,
                        ),
                    )
                    connection.execute(
                        "INSERT INTO section_fts VALUES (?, ?, ?, ?, ?, ?)",
                        (
                            section_id,
                            " ".join(title_terms),
                            " ".join(aliases),
                            section.section_path or section.heading,
                            metadata,
                            section.body,
                        ),
                    )
            connection.commit()
        finally:
            connection.close()
        os.chmod(temporary, 0o600)
        os.replace(temporary, destination)
    except Exception:
        temporary.unlink(missing_ok=True)
        raise
    return destination


def index_is_stale(root: Path, include_generated: bool = False) -> bool:
    root = root.resolve()
    database = index_path(root, include_generated)
    if not database.is_file():
        return True
    try:
        connection = sqlite3.connect(f"file:{database}?mode=ro", uri=True)
        try:
            schema = connection.execute(
                "SELECT value FROM metadata WHERE key = 'schema_version'"
            ).fetchone()
            mode = connection.execute(
                "SELECT value FROM metadata WHERE key = 'include_generated'"
            ).fetchone()
            stored = connection.execute(
                "SELECT path, size, mtime_ns FROM manifest ORDER BY path"
            ).fetchall()
            connection.execute("SELECT 1 FROM section_fts LIMIT 1").fetchone()
        finally:
            connection.close()
    except sqlite3.Error:
        return True
    expected_mode = "1" if include_generated else "0"
    return schema != (SCHEMA_VERSION,) or mode != (expected_mode,) or stored != corpus_manifest(root)


def ensure_index(root: Path, include_generated: bool = False, rebuild: bool = False) -> Path:
    ensure_fts5()
    if rebuild or index_is_stale(root, include_generated):
        return build_index(root, include_generated)
    return index_path(root.resolve(), include_generated)


def query_tokens(query: str) -> list[str]:
    return _unique(match.group(0).casefold() for match in TOKEN_RE.finditer(query))


def fts_query(tokens: list[str], mode: str) -> str:
    operator = " AND " if mode == "and" else " OR "
    return operator.join(f'"{token.replace(chr(34), chr(34) * 2)}"' for token in tokens)


def _like_value(value: str) -> str:
    return "%" + value.replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_") + "%"


def _run_query(
    connection: sqlite3.Connection,
    expression: str,
    *,
    limit: int,
    page_type: str | None,
    category: str | None,
    path: str | None,
    status: str | None,
    source: str | None,
    tag: str | None,
    per_page: int,
) -> list[dict[str, Any]]:
    conditions = ["section_fts MATCH ?"]
    parameters: list[Any] = [expression]
    if page_type:
        conditions.append("p.page_type = ?")
        parameters.append(page_type)
    if category:
        conditions.append(
            "EXISTS (SELECT 1 FROM page_categories c WHERE c.page_id = p.id AND c.value = ?)"
        )
        parameters.append(category)
    if path:
        conditions.append("s.path LIKE ? ESCAPE '\\'")
        parameters.append(_like_value(path))
    if status:
        conditions.append("p.status = ?")
        parameters.append(status)
    if source:
        conditions.append(
            "EXISTS (SELECT 1 FROM page_sources x WHERE x.page_id = p.id AND x.value = ?)"
        )
        parameters.append(source)
    if tag:
        conditions.append("EXISTS (SELECT 1 FROM page_tags t WHERE t.page_id = p.id AND t.value = ?)")
        parameters.append(tag)

    weights = ", ".join(str(weight) for weight in BM25_WEIGHTS)
    # Rank the complete match set, then stream until the per-page cap yields
    # enough results. A finite SQL LIMIT could let one long page hide others.
    rows = connection.execute(
        f"""
        SELECT s.path, s.title, s.section, s.section_path, s.section_order,
               s.page_type, s.status, s.source_id, s.aliases_json,
               s.categories_json, s.tags_json,
               -bm25(section_fts, {weights}) AS score,
               snippet(section_fts, 5, '⟦', '⟧', ' … ', 24) AS body_snippet,
               snippet(section_fts, -1, '⟦', '⟧', ' … ', 24) AS best_snippet
        FROM section_fts
        JOIN sections s ON s.id = CAST(section_fts.section_id AS INTEGER)
        JOIN pages p ON p.id = s.page_id
        WHERE {' AND '.join(conditions)}
        ORDER BY bm25(section_fts, {weights}) ASC, s.path ASC, s.section_order ASC
        """,
        parameters,
    )

    results: list[dict[str, Any]] = []
    page_counts: dict[str, int] = {}
    for row in rows:
        result_path = row[0]
        if page_counts.get(result_path, 0) >= per_page:
            continue
        page_counts[result_path] = page_counts.get(result_path, 0) + 1
        body_snippet = row[12] or ""
        selected_snippet = body_snippet if "⟦" in body_snippet else (row[13] or "")
        results.append(
            {
                "path": result_path,
                "title": row[1],
                "section": row[2] or None,
                "section_path": row[3] or None,
                "section_order": row[4],
                "score": round(float(row[11]), 8),
                "snippet": re.sub(r"\s+", " ", selected_snippet).strip(),
                "type": row[5] or None,
                "status": row[6] or None,
                "categories": json.loads(row[9]),
                "tags": json.loads(row[10]),
                "source_id": row[7] or None,
                "aliases": json.loads(row[8]),
            }
        )
        if len(results) >= limit:
            break
    return results


def search(
    root: Path,
    query: str,
    *,
    limit: int = 10,
    page_type: str | None = None,
    category: str | None = None,
    path: str | None = None,
    status: str | None = None,
    source: str | None = None,
    tag: str | None = None,
    include_generated: bool = False,
    rebuild: bool = False,
    per_page: int = DEFAULT_PER_PAGE,
) -> SearchResponse:
    if limit < 1:
        raise SearchError("--limit must be at least 1")
    if per_page < 1:
        raise SearchError("per-page result cap must be at least 1")
    tokens = query_tokens(query)
    if not tokens:
        raise SearchError("query must contain at least one letter or number")
    database = ensure_index(root, include_generated, rebuild)
    connection = sqlite3.connect(f"file:{database}?mode=ro", uri=True)
    try:
        options = {
            "limit": limit,
            "page_type": page_type,
            "category": category,
            "path": path,
            "status": status,
            "source": source,
            "tag": tag,
            "per_page": per_page,
        }
        results = _run_query(connection, fts_query(tokens, "and"), **options)
        match_mode = "and"
        if not results and len(tokens) > 1:
            results = _run_query(connection, fts_query(tokens, "or"), **options)
            match_mode = "or"
    except sqlite3.Error as error:
        raise SearchError(f"search index query failed: {error}") from error
    finally:
        connection.close()
    return SearchResponse(query=query, match_mode=match_mode, results=results)
