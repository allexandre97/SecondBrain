#!/usr/bin/env python3
"""Small deterministic helpers for the wiki's limited Markdown/frontmatter format."""

from __future__ import annotations

import csv
from typing import Any


def unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def parse_scalar(value: str) -> Any:
    value = value.strip()
    if value == "[]":
        return []
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        try:
            return [unquote(item.strip()) for item in next(csv.reader([inner], skipinitialspace=True))]
        except (csv.Error, StopIteration):
            return value
    if value.lower() in {"true", "false"}:
        return value.lower() == "true"
    return unquote(value)


def parse_frontmatter(text: str) -> tuple[dict[str, Any], list[str]]:
    """Parse top-level scalars and lists; unsupported YAML constructs are ignored."""
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
        if not line.startswith((" ", "\t")) and ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            if not key:
                key = None
                continue
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
