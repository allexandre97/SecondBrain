---
type: concept
status: active
created: 2026-06-29
updated: 2026-06-29
areas:
  - research
categories:
  - research/llm-wiki/workflows
tags:
  - workflow
related:
  - "[[concepts/multi-category-wiki-organization]]"
  - "[[concepts/reusable-codex-task-contracts]]"
sources:
  - SRC-0001
  - SRC-0002
sensitivity: public
encryption: none
---

# Source Ingestion

## Summary

Source ingestion is the workflow for turning one raw source into reviewed wiki updates: a source summary, relevant concept or entity changes, links, index updates, and a log entry. [SRC-0001]

## Key Points

- The source recommends ingesting one source at a time when close human review matters. [SRC-0001]
- A single ingest may touch multiple wiki pages because new material can update existing concepts or introduce new ones. [SRC-0001]
- Inferred point: this repository should keep ingests narrow until its conventions and review habits are stable. [SRC-0001]
- SRC-0002 adds that Codex should suggest categories, tags, and related pages during ingestion, prioritizing existing categories when possible. [SRC-0002]
- SRC-0002 also reinforces that raw source files should not be modified during ingestion. [SRC-0002]

## Links

- [[sources/SRC-0001-karpathy-llm-knowledge-base]]
- [[sources/SRC-0002-project-design-note]]
- [[concepts/wiki-index-and-log]]
- [[concepts/wiki-linting]]
- [[concepts/multi-category-wiki-organization]]
- [[concepts/reusable-codex-task-contracts]]
