---
type: concept
status: active
created: 2026-06-29
updated: 2026-06-29
areas:
  - research
categories:
  - research/llm-wiki/navigation
tags:
  - workflow
related:
  - "[[concepts/multi-category-wiki-organization]]"
sources:
  - SRC-0001
  - SRC-0002
sensitivity: public
encryption: none
---

# Wiki Index and Log

## Summary

`wiki/index.md` is the content-oriented map of the wiki, while `wiki/log.md` is the chronological record of ingests, queries, and maintenance. [SRC-0001]

## Key Points

- The index helps both humans and LLMs find relevant pages before deeper reading. [SRC-0001]
- The log records what changed over time and can be made parseable with consistent entry prefixes. [SRC-0001]
- Inferred point: this repository should update both files on each ingest to preserve navigation and history. [SRC-0001]
- SRC-0002 qualifies navigation by making frontmatter the source of truth for categories, while category pages remain optional navigational indexes. [SRC-0002]

## Links

- [[index]]
- [[log]]
- [[sources/SRC-0001-karpathy-llm-knowledge-base]]
- [[sources/SRC-0002-project-design-note]]
- [[concepts/multi-category-wiki-organization]]
