#!/usr/bin/env python3
"""Command-line interface for deterministic section-level wiki search."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Sequence

from wiki_search import SearchError, ensure_index, index_path, search


ROOT = Path(__file__).resolve().parents[1]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Search wiki Markdown sections with SQLite FTS5 and BM25."
    )
    parser.add_argument(
        "terms",
        nargs="*",
        help="Ordinary lexical query words; shell quoting does not request phrase syntax.",
    )
    parser.add_argument("--limit", type=int, default=10, help="Maximum results (default: 10).")
    parser.add_argument("--json", action="store_true", help="Write machine-readable JSON only.")
    parser.add_argument("--type", dest="page_type", help="Exact frontmatter type filter.")
    parser.add_argument("--category", help="Exact frontmatter category filter.")
    parser.add_argument("--path", help="Repository-relative path substring filter (ASCII case-insensitive).")
    parser.add_argument("--status", help="Exact frontmatter status filter.")
    parser.add_argument("--source", help="Exact source_id or frontmatter sources filter.")
    parser.add_argument("--tag", help="Exact frontmatter tag filter.")
    parser.add_argument(
        "--include-generated",
        action="store_true",
        help="Use a separate index that includes pages with generated: true.",
    )
    parser.add_argument(
        "--rebuild",
        action="store_true",
        help="Force rebuilding the selected index before searching; without a query, rebuild and exit.",
    )
    return parser


def response_payload(response: object) -> dict[str, object]:
    return {
        "query": response.query,
        "match_mode": response.match_mode,
        "score_semantics": "higher_is_better_negative_bm25",
        "results": response.results,
    }


def print_human(response: object) -> None:
    if not response.results:
        print("No matches found.")
        return
    print(f"Match mode: {response.match_mode.upper()} (higher score is better)")
    for number, result in enumerate(response.results, 1):
        print(f"{number}. {result['path']}")
        section = result["section_path"] or "(page introduction)"
        print(f"   Section: {section}")
        print(f"   Score: {result['score']:.6f}")
        if result["snippet"]:
            print(f"   {result['snippet']}")


def main(argv: Sequence[str] | None = None, *, root: Path = ROOT) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    query = " ".join(args.terms).strip()
    if not query and not args.rebuild:
        parser.error("provide a query or --rebuild")

    try:
        if not query:
            database = ensure_index(root, args.include_generated, rebuild=True)
            payload = {"rebuilt": database.relative_to(root.resolve()).as_posix()}
            if args.json:
                print(json.dumps(payload, ensure_ascii=False, sort_keys=True))
            else:
                print(f"Rebuilt {payload['rebuilt']}")
            return 0

        response = search(
            root,
            query,
            limit=args.limit,
            page_type=args.page_type,
            category=args.category,
            path=args.path,
            status=args.status,
            source=args.source,
            tag=args.tag,
            include_generated=args.include_generated,
            rebuild=args.rebuild,
        )
    except SearchError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(response_payload(response), ensure_ascii=False, sort_keys=True))
    else:
        print_human(response)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
