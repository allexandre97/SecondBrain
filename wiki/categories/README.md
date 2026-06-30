---
type: category
status: active
created: 2026-06-29
updated: 2026-06-29
areas: []
categories: []
tags:
  - navigation
related:
  - "[[index]]"
sources:
  - SRC-0002
sensitivity: public
encryption: none
---

# Categories

Category pages are navigational indexes for browsing the wiki. They can group useful links, summarize category scope, and point to related areas. [SRC-0002]

Page frontmatter is the source of truth for category membership. Do not rely on folder location alone to decide whether a page belongs to a category. [SRC-0002]

Generated category pages are derived from frontmatter with `python3 tools/build_category_indexes.py`. Prefer category paths documented in [Category Registry](../../schema/category_registry.md) when assigning categories, and record uncertain candidates in page notes instead of creating a new taxonomy branch without review.
