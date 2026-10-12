#!/usr/bin/env python3
"""Set a page's time scope, currency metadata, and currency banner deterministically.

Examples:

    python3 tools/set_currency.py wiki/answers/x.md --scope snapshot --currency current \\
        --as-of 2026-10-01 --as-of-commit FFRefine@6b20031
    python3 tools/set_currency.py wiki/answers/x.md --superseded-by wiki/answers/y \\
        --note "Gates were retired on 2026-10-07."

Fields not given on the command line keep their current values; an existing
banner note is kept unless --note replaces it. The tool rewrites only the
managed frontmatter keys, the `updated` date, the `> [!currency]` banner
under the H1, and the page's currency marker in `wiki/index.md`; it refuses
to write a page that would fail the currency validation rules.
"""

from __future__ import annotations

import argparse
import sys
from datetime import date
from pathlib import Path
from typing import Sequence

from wiki_currency import (
    BANNER_PREFIX,
    CURRENCIES,
    NOT_CURRENT,
    SCOPES,
    currency_issues,
    currency_metadata,
    h1_index,
    link_target,
    set_index_marker,
)
from wiki_markdown import parse_frontmatter


ROOT = Path(__file__).resolve().parents[1]
MANAGED_KEYS = ("scope", "currency", "as_of", "as_of_commit", "superseded_by")


class CurrencyError(RuntimeError):
    pass


def resolve_page(root: Path, value: str) -> Path:
    target = link_target(value)
    relative = target if target.endswith(".md") else f"{target}.md"
    path = (root / relative).resolve()
    if not path.is_file() or (root / "wiki").resolve() not in path.parents:
        raise CurrencyError(f"page not found under wiki/: {value}")
    return path


def page_target(root: Path, path: Path) -> str:
    return path.relative_to(root.resolve()).with_suffix("").as_posix()


def frontmatter_end(lines: list[str]) -> int:
    if not lines or lines[0].strip() != "---":
        raise CurrencyError("page has no YAML frontmatter")
    for index, line in enumerate(lines[1:], 1):
        if line.strip() == "---":
            return index
    raise CurrencyError("page frontmatter is not closed")


def strip_keys(frontmatter_lines: list[str], keys: Sequence[str]) -> list[str]:
    """Remove top-level keys together with their continuation lines.

    Blank lines do not end a key's block, matching parse_frontmatter, which
    keeps appending list items to the last key across blank lines.
    """
    kept: list[str] = []
    skipping = False
    for line in frontmatter_lines:
        if line.strip() and not line.startswith((" ", "\t", "- ")) and ":" in line:
            skipping = line.split(":", 1)[0].strip() in keys
        if not skipping:
            kept.append(line)
    return kept


def managed_lines(meta: dict[str, object], write_scope: bool) -> list[str]:
    lines: list[str] = [f"scope: {meta['scope']}"] if write_scope else []
    if meta["currency"]:
        lines.append(f"currency: {meta['currency']}")
    if meta["as_of"]:
        lines.append(f"as_of: {meta['as_of']}")
    if meta["as_of_commit"]:
        lines.append("as_of_commit:")
        lines.extend(f"  - {commit}" for commit in meta["as_of_commit"])
    if meta["superseded_by"]:
        lines.append("superseded_by:")
        lines.extend(f'  - "[[{target}]]"' for target in meta["superseded_by"])
    return lines


def banner_lines(meta: dict[str, object], note_lines: list[str]) -> list[str]:
    when = f"as of {meta['as_of']}" if meta["as_of"] else "at an earlier date"
    if meta["as_of_commit"]:
        when += f" ({', '.join(meta['as_of_commit'])})"
    if meta["currency"] == "superseded":
        links = ", ".join(f"[[{target}]]" for target in meta["superseded_by"])
        lines = [f"{BANNER_PREFIX} Superseded — describes the state {when}. Current information: {links}"]
    else:
        lines = [f"{BANNER_PREFIX} Historical — describes the state {when}; kept as a record, not as the current state."]
    return lines + note_lines


def without_banner(body: list[str], h1: int | None) -> tuple[list[str], list[str]]:
    """Remove an existing banner; return the body and the banner's note lines."""
    start = 0 if h1 is None else h1 + 1
    index = start
    while index < len(body) and not body[index].strip():
        index += 1
    if index >= len(body) or not body[index].startswith(BANNER_PREFIX):
        return body, []
    end = index + 1
    while end < len(body) and body[end].startswith(">"):
        end += 1
    note_lines = body[index + 1 : end]
    while end < len(body) and not body[end].strip():
        end += 1
    return body[:start] + ([""] if h1 is not None else []) + body[end:], note_lines


def apply_currency(
    root: Path,
    path: Path,
    *,
    scope: str | None = None,
    currency: str | None = None,
    as_of: str | None = None,
    as_of_commit: list[str] | None = None,
    superseded_by: list[str] | None = None,
    note: str | None = None,
    clear_currency: bool = False,
    today: date | None = None,
) -> str:
    """Return the page text with updated currency metadata and banner."""
    today = today or date.today()
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")
    end = frontmatter_end(lines)
    frontmatter, _ = parse_frontmatter(text)
    meta = currency_metadata(frontmatter)
    # Never write a default scope: an unmigrated page must keep failing
    # validation until someone chooses its scope explicitly.
    write_scope = bool(scope) or "scope" in frontmatter

    if clear_currency:
        if currency or as_of or as_of_commit or superseded_by:
            raise CurrencyError("--clear-currency cannot be combined with other currency fields")
        meta.update(currency=None, as_of=None, as_of_commit=[], superseded_by=[])
    if superseded_by:
        if currency not in (None, "superseded"):
            raise CurrencyError("--superseded-by can only be combined with --currency superseded")
        replacements = [resolve_page(root, value) for value in superseded_by]
        if path.resolve() in replacements:
            raise CurrencyError("a page cannot supersede itself")
        meta["superseded_by"] = [page_target(root, replacement) for replacement in replacements]
        currency = "superseded"
    if scope:
        meta["scope"] = scope
    if currency:
        meta["currency"] = currency
    if as_of:
        meta["as_of"] = as_of
    if as_of_commit is not None:
        meta["as_of_commit"] = as_of_commit
    if meta["currency"] != "superseded":
        meta["superseded_by"] = []

    frontmatter_lines = strip_keys(lines[1:end], MANAGED_KEYS)
    frontmatter_lines = [
        f"updated: {today.isoformat()}" if line.startswith("updated:") else line
        for line in frontmatter_lines
    ]
    frontmatter_lines.extend(managed_lines(meta, write_scope))

    body = lines[end + 1 :]
    h1 = h1_index(body)
    body, old_note_lines = without_banner(body, h1)
    if meta["currency"] in NOT_CURRENT:
        # A new note replaces the old one; otherwise the recorded reason is kept.
        note_lines = [f"> {' '.join(note.split())}"] if note else old_note_lines
        insert_at = 0 if h1 is None else h1 + 1
        rest = body[insert_at:]
        while rest and not rest[0].strip():
            rest = rest[1:]
        prefix = [""] if h1 is not None else []
        body = body[:insert_at] + prefix + banner_lines(meta, note_lines) + [""] + rest

    new_text = "\n".join(["---", *frontmatter_lines, "---", *body])
    new_frontmatter, new_body = parse_frontmatter(new_text)
    errors, _warnings = currency_issues(new_frontmatter, new_body, today)
    if errors:
        raise CurrencyError("; ".join(errors))
    return new_text


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("page", help="Wiki page path, with or without .md, or a [[wikilink]].")
    parser.add_argument("--scope", choices=SCOPES)
    parser.add_argument("--currency", choices=CURRENCIES)
    parser.add_argument("--as-of", help="Date the content describes, YYYY-MM-DD.")
    parser.add_argument(
        "--as-of-commit",
        action="append",
        help="Repository@commit the content describes; repeatable; replaces existing entries.",
    )
    parser.add_argument(
        "--superseded-by",
        action="append",
        help="Replacement page; repeatable; implies --currency superseded.",
    )
    parser.add_argument("--note", help="One-line explanation added to the banner; replaces an existing note.")
    parser.add_argument(
        "--clear-currency",
        action="store_true",
        help="Remove currency, as_of, as_of_commit, and superseded_by, e.g. when a page becomes timeless.",
    )
    parser.add_argument("--dry-run", action="store_true", help="Print the new page instead of writing it.")
    return parser


def main(argv: Sequence[str] | None = None, *, root: Path = ROOT) -> int:
    args = build_parser().parse_args(argv)
    try:
        path = resolve_page(root, args.page)
        new_text = apply_currency(
            root,
            path,
            scope=args.scope,
            currency=args.currency,
            as_of=args.as_of,
            as_of_commit=args.as_of_commit,
            superseded_by=args.superseded_by,
            note=args.note,
            clear_currency=args.clear_currency,
        )
    except CurrencyError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    if args.dry_run:
        print(new_text, end="")
        return 0
    path.write_text(new_text, encoding="utf-8")
    print(f"Updated {path.relative_to(root.resolve()).as_posix()}")

    index_page = root / "wiki" / "index.md"
    if index_page.is_file():
        frontmatter, _ = parse_frontmatter(new_text)
        index_text = index_page.read_text(encoding="utf-8")
        new_index = "\n".join(
            set_index_marker(index_text.split("\n"), page_target(root, path), currency_metadata(frontmatter)["currency"])
        )
        if new_index != index_text:
            index_page.write_text(new_index, encoding="utf-8")
            print("Updated wiki/index.md entry")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
