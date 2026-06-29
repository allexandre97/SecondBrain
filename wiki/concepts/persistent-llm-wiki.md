---
type: concept
status: active
created: 2026-06-29
updated: 2026-06-29
areas:
  - research
categories:
  - research/llm-wiki/design
tags:
  - llm-wiki
related:
  - "[[concepts/local-first-personal-work-knowledge-base]]"
  - "[[concepts/raw-wiki-schema-layers]]"
sources:
  - SRC-0001
  - SRC-0002
sensitivity: public
encryption: none
---

# Persistent LLM Wiki

## Summary

A persistent LLM wiki is a Markdown knowledge base that an LLM incrementally maintains from raw sources, so synthesis accumulates instead of being regenerated for every question. [SRC-0001]

## Key Points

- The wiki is positioned as an intermediate layer between raw documents and answers. [SRC-0001]
- Its value comes from durable cross-references, summaries, contradictions, and evolving synthesis. [SRC-0001]
- The source frames Obsidian as a possible browsing interface, with the LLM acting as the maintainer of the wiki files. [SRC-0001]
- SRC-0002 narrows this project's implementation toward a local-first personal/work knowledge base that stays plain Markdown by default. [SRC-0002]

## Links

- [[sources/SRC-0001-karpathy-llm-knowledge-base]]
- [[sources/SRC-0002-project-design-note]]
- [[concepts/local-first-personal-work-knowledge-base]]
- [[concepts/raw-wiki-schema-layers]]
- [[concepts/source-ingestion]]
