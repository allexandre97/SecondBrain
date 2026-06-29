---
type: concept
status: active
created: 2026-06-29
updated: 2026-06-29
areas:
  - research
categories:
  - research/llm-wiki/organization
tags:
  - categories
  - metadata
related:
  - "[[concepts/wiki-page-metadata]]"
  - "[[categories/README]]"
sources:
  - SRC-0002
sensitivity: public
encryption: none
---

# Multi-Category Wiki Organization

## Summary

Multi-category organization lets a wiki page belong to several contexts through frontmatter instead of forcing it into one folder-based category. [SRC-0002]

## Key Points

- Category membership should come from page frontmatter, not from folder location alone. [SRC-0002]
- Category pages, when present, should work as navigational indexes rather than the source of truth. [SRC-0002]
- During ingestion, Codex should prefer existing categories and suggest new ones only when no existing category fits. [SRC-0002]

## Links

- [[sources/SRC-0002-project-design-note]]
- [[concepts/wiki-page-metadata]]
- [[categories/README]]
