---
type: source
status: active
created: 2026-06-29
updated: 2026-07-01
source_id: SRC-0001
display_title: "LLM Wiki"
short_title: "LLM Wiki"
aliases:
  - "SRC-0001"
  - "LLM Wiki"
source_path: raw/sources/SRC-0001-karpathy-llm-knowledge-base.md
categories:
  - research/llm-wiki/design
  - research/llm-wiki/architecture
  - research/llm-wiki/workflows
metadata_review_status: not-applicable
citation_match_status: reviewed
cqt_review_status: source-local
tags:
  - llm-wiki
---

# LLM Wiki

Source ID: `SRC-0001`

## Raw source

- Repository path: `raw/sources/SRC-0001-karpathy-llm-knowledge-base.md`
- Open raw source: [raw/sources/SRC-0001-karpathy-llm-knowledge-base.md](../../raw/sources/SRC-0001-karpathy-llm-knowledge-base.md)

## Summary

This source proposes an LLM-maintained knowledge base where raw documents are compiled into a persistent, interlinked Markdown wiki instead of being re-retrieved from scratch for each query. The wiki becomes a cumulative artifact: source summaries, concept pages, contradictions, and cross-references are maintained over time. [SRC-0001]

## Key Points

- The core contrast is between ordinary retrieval-augmented generation and a persistent wiki that preserves synthesis between sessions. [SRC-0001]
- The proposed system has three layers: immutable raw sources, an LLM-maintained wiki, and a schema that governs structure and workflows. [SRC-0001]
- Ingestion should process sources into summaries, concept/entity pages, links, contradictions, index updates, and log entries. [SRC-0001]
- Query answers can become durable wiki pages when they produce useful synthesis. [SRC-0001]
- Periodic linting should check broken links, orphan pages, stale claims, contradictions, and missing concept pages. [SRC-0001]

## Links

- [[wiki/concepts/persistent-llm-wiki]]
- [[wiki/concepts/raw-wiki-schema-layers]]
- [[wiki/concepts/source-ingestion]]
- [[wiki/concepts/wiki-index-and-log]]
- [[wiki/concepts/wiki-linting]]

## Metadata notes

This is a wiki-design source rather than an ordinary scientific paper. Paper-style author/year metadata is not central for migration status; semantic review is intentionally kept source-local.

## Open Questions

- [[wiki/questions/optional-tooling-for-llm-wiki]] - Decide whether any optional tools or formats from the source should be adopted later. [SRC-0001]
