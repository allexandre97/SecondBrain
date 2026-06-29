---
type: concept
status: active
created: 2026-06-29
updated: 2026-06-29
areas:
  - research
categories:
  - research/llm-wiki/architecture
tags:
  - llm-wiki
related:
  - "[[concepts/wiki-page-metadata]]"
sources:
  - SRC-0001
  - SRC-0002
sensitivity: public
encryption: none
---

# Raw, Wiki, and Schema Layers

## Summary

The proposed architecture separates source truth, synthesized knowledge, and operating rules into `raw/`, `wiki/`, and `schema` layers. [SRC-0001]

## Key Points

- `raw/` holds immutable source material that the agent may read but should not modify. [SRC-0001]
- `wiki/` holds LLM-generated Markdown summaries, concept pages, comparisons, and synthesis. [SRC-0001]
- `schema/` defines conventions and workflows that make the LLM behave like a disciplined wiki maintainer. [SRC-0001]
- SRC-0002 adds that raw sources live under `raw/sources/`, synthesized knowledge lives under `wiki/`, and schema/task contracts should preserve local-first, Obsidian-compatible Markdown. [SRC-0002]

## Links

- [[sources/SRC-0001-karpathy-llm-knowledge-base]]
- [[sources/SRC-0002-project-design-note]]
- [[concepts/persistent-llm-wiki]]
- [[concepts/wiki-page-metadata]]
