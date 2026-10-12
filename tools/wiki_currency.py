#!/usr/bin/env python3
"""Shared rules for page time scope and currency metadata.

Every page has one time scope:

- ``timeless`` (the default when ``scope`` is absent): literature, concepts,
  claims, derivations; knowledge that does not describe a moment in time.
- ``living``: always describes the present; rewritten in place when it changes.
- ``snapshot``: describes one moment; frozen afterwards except for currency
  metadata and the currency banner.

Living and snapshot pages carry ``currency`` (current, historical, or
superseded) and ``as_of`` (the date the content describes). Superseded pages
name their replacements in ``superseded_by``. Historical and superseded pages
start their body, directly under the H1, with a ``> [!currency]`` banner, and
their ``wiki/index.md`` entry starts its description with ``**Superseded:**`` or
``**Historical:**``. Answer pages and pages with ``project_evidence`` must
declare ``scope`` explicitly.
"""

from __future__ import annotations

import re
from datetime import date
from typing import Any

from wiki_markdown import as_list


SCOPES = ("timeless", "living", "snapshot")
CURRENCIES = ("current", "historical", "superseded")
NOT_CURRENT = ("historical", "superseded")
BANNER_PREFIX = "> [!currency]"
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
# <repository>@<commit>, for example "FFRefine@6b20031".
COMMIT_RE = re.compile(r"^[A-Za-z0-9_.-]+@[0-9a-f]{7,40}$")
WIKILINK_VALUE_RE = re.compile(r"^\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]$")
FENCE_RE = re.compile(r"^ {0,3}(`{3,}|~{3,})")
# Living pages record changes in a "## Changes" list, so any dated heading is an appended update.
DATED_HEADING_RE = re.compile(r"^#{2,6}\s.*\b\d{4}-\d{2}-\d{2}\b")
# On every page, a dated "update" or "status" heading is a later development appended to old text.
DATED_UPDATE_HEADING_RE = re.compile(
    r"^#{2,6}\s.*(?:\b\d{4}-\d{2}-\d{2}\b.*\b(?:updates?|status)\b|\b(?:updates?|status)\b.*\b\d{4}-\d{2}-\d{2}\b)",
    re.IGNORECASE,
)
STALE_LIVING_DAYS = 90
# Index entries look like "- [[wiki/answers/page]] - Description".
INDEX_ENTRY_RE = re.compile(r"^(- \[\[([^\]|#]+)[^\]]*\]\] - )(?:\*\*(Superseded|Historical):\*\* )?(.*)$")


def _scalar(frontmatter: dict[str, Any], key: str) -> str:
    value = frontmatter.get(key, "")
    return value.strip() if isinstance(value, str) else ""


def link_target(value: str) -> str:
    """Return the page target of a ``[[target]]`` value, or the value unchanged."""
    match = WIKILINK_VALUE_RE.match(value.strip())
    return match.group(1).strip() if match else value.strip()


def currency_metadata(frontmatter: dict[str, Any]) -> dict[str, Any]:
    """Normalised currency fields; scope defaults to timeless."""
    return {
        "scope": _scalar(frontmatter, "scope") or "timeless",
        "currency": _scalar(frontmatter, "currency") or None,
        "as_of": _scalar(frontmatter, "as_of") or None,
        "as_of_commit": as_list(frontmatter.get("as_of_commit", [])),
        "superseded_by": [link_target(value) for value in as_list(frontmatter.get("superseded_by", []))],
    }


def parse_date(value: str) -> date | None:
    if not DATE_RE.match(value):
        return None
    try:
        return date.fromisoformat(value)
    except ValueError:
        return None


def h1_index(body_lines: list[str]) -> int | None:
    """Index of the first H1 outside fenced code, or None."""
    fence = ""
    for index, line in enumerate(body_lines):
        match = FENCE_RE.match(line)
        if fence:
            if match and match.group(1)[0] == fence[0] and len(match.group(1)) >= len(fence):
                fence = ""
        elif match:
            fence = match.group(1)
        elif line.startswith("# "):
            return index
    return None


def first_line_after_h1(body_lines: list[str]) -> str | None:
    """First non-blank body line after the H1, or after the start when there is no H1."""
    index = h1_index(body_lines)
    start = 0 if index is None else index + 1
    return next((line for line in body_lines[start:] if line.strip()), None)


def currency_issues(
    frontmatter: dict[str, Any], body_lines: list[str], today: date
) -> tuple[list[str], list[str]]:
    """Return (errors, warnings) for one page's currency metadata and banner."""
    errors: list[str] = []
    warnings: list[str] = []
    meta = currency_metadata(frontmatter)
    scope, currency, as_of = meta["scope"], meta["currency"], meta["as_of"]

    if "scope" not in frontmatter and ("project_evidence" in frontmatter or _scalar(frontmatter, "type") == "answer"):
        errors.append("answer pages and pages with project_evidence must declare scope (timeless, living, or snapshot)")
    if scope not in SCOPES:
        errors.append(f"unknown scope {scope!r}; expected one of {', '.join(SCOPES)}")
    if currency is not None and currency not in CURRENCIES:
        errors.append(f"unknown currency {currency!r}; expected one of {', '.join(CURRENCIES)}")
    if scope in ("living", "snapshot"):
        if currency is None:
            errors.append(f"{scope} page must declare currency")
        if as_of is None:
            errors.append(f"{scope} page must declare as_of")
    if scope == "timeless" and currency == "current":
        errors.append("timeless pages carry currency only when historical or superseded; use set_currency.py --clear-currency")
    if scope == "living" and currency == "historical":
        errors.append("living page cannot be historical; mark it superseded or make it a snapshot")
    as_of_date = parse_date(as_of) if as_of is not None else None
    if as_of is not None and as_of_date is None:
        errors.append(f"as_of must be a valid YYYY-MM-DD date, got {as_of!r}")
    for commit in meta["as_of_commit"]:
        if not COMMIT_RE.match(commit):
            errors.append(f"as_of_commit entry must look like Repository@abc1234, got {commit!r}")

    raw_superseded_by = as_list(frontmatter.get("superseded_by", []))
    if currency == "superseded" and not raw_superseded_by:
        errors.append("superseded page must name its replacement in superseded_by")
    if raw_superseded_by and currency != "superseded":
        errors.append("superseded_by is only allowed on superseded pages")
    for value in raw_superseded_by:
        if not WIKILINK_VALUE_RE.match(value.strip()):
            errors.append(f"superseded_by entries must be wikilinks, got {value!r}")

    first_line = first_line_after_h1(body_lines) or ""
    has_banner = first_line.startswith(BANNER_PREFIX)
    if currency in NOT_CURRENT and not has_banner:
        errors.append(f"{currency} page must start with a '{BANNER_PREFIX}' banner directly under the H1")
    if currency not in NOT_CURRENT and has_banner:
        errors.append(f"page has a '{BANNER_PREFIX}' banner but is not historical or superseded")

    if scope == "living" and currency == "current":
        if any(DATED_HEADING_RE.match(line) for line in body_lines):
            warnings.append("living page has a dated heading; fold the update into the page body and list it under ## Changes")
        if as_of_date and (today - as_of_date).days > STALE_LIVING_DAYS:
            warnings.append(f"living page as_of {as_of} is more than {STALE_LIVING_DAYS} days old; recheck it")
    elif any(DATED_UPDATE_HEADING_RE.match(line) for line in body_lines):
        warnings.append("dated update/status heading; restructure per the Currency workflow (Recording change over time)")

    return errors, warnings


def index_marker(currency: str | None) -> str:
    return f"**{currency.capitalize()}:** " if currency in NOT_CURRENT else ""


def set_index_marker(index_lines: list[str], target: str, currency: str | None) -> list[str]:
    """Add, replace, or remove the currency marker on index entries linking to target."""
    updated = []
    for line in index_lines:
        match = INDEX_ENTRY_RE.match(line)
        if match and match.group(2).strip() == target:
            line = match.group(1) + index_marker(currency) + match.group(4)
        updated.append(line)
    return updated


def index_marker_issues(index_lines: list[str], currency_by_target: dict[str, str | None]) -> list[str]:
    """Errors for index entries whose currency marker disagrees with the linked page."""
    errors = []
    for number, line in enumerate(index_lines, 1):
        match = INDEX_ENTRY_RE.match(line)
        if not match:
            continue
        target = match.group(2).strip()
        expected = index_marker(currency_by_target.get(target))
        actual = f"**{match.group(3)}:** " if match.group(3) else ""
        if actual != expected:
            fix = f"start its description with {expected.strip()!r}" if expected else "not carry a currency marker"
            errors.append(f"line {number}: entry for {target} should {fix}; run tools/set_currency.py on the page")
    return errors
