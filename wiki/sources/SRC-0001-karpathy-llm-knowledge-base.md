---
type: source
status: active
created: 2026-06-29
updated: 2026-06-30
source_id: SRC-0001
display_title: "LLM Wiki"
short_title: "LLM Wiki"
aliases:
  - "SRC-0001"
  - "LLM Wiki"
source_path: raw/sources/SRC-0001-karpathy-llm-knowledge-base.md
tags:
  - llm-wiki
---

# LLM Wiki

Source ID: `SRC-0001`

## Raw source

- Repository path: `raw/sources/SRC-0001-karpathy-llm-knowledge-base.md`
- Local relative link: [Open raw source](../../raw/sources/SRC-0001-karpathy-llm-knowledge-base.md)

## Summary

This source proposes an LLM-maintained knowledge base where raw documents are compiled into a persistent, interlinked Markdown wiki instead of being re-retrieved from scratch for each query. The wiki becomes a cumulative artifact: source summaries, concept pages, contradictions, and cross-references are maintained over time. [SRC-0001]

## Key Points

- The core contrast is between ordinary retrieval-augmented generation and a persistent wiki that preserves synthesis between sessions. [SRC-0001]
- The proposed system has three layers: immutable raw sources, an LLM-maintained wiki, and a schema that governs structure and workflows. [SRC-0001]
- Ingestion should process sources into summaries, concept/entity pages, links, contradictions, index updates, and log entries. [SRC-0001]
- Query answers can become durable wiki pages when they produce useful synthesis. [SRC-0001]
- Periodic linting should check broken links, orphan pages, stale claims, contradictions, and missing concept pages. [SRC-0001]

## Links

- [[concepts/persistent-llm-wiki]]
- [[concepts/raw-wiki-schema-layers]]
- [[concepts/source-ingestion]]
- [[concepts/wiki-index-and-log]]
- [[concepts/wiki-linting]]

## Open Questions

- [[questions/optional-tooling-for-llm-wiki]] - Decide whether any optional tools or formats from the source should be adopted later. [SRC-0001]
