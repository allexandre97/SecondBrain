---
type: concept
status: active
created: 2026-06-29
updated: 2026-06-29
areas:
  - personal
  - work
  - research
categories:
  - research/llm-wiki/design
tags:
  - local-first
  - llm-wiki
related:
  - "[[concepts/persistent-llm-wiki]]"
sources:
  - SRC-0002
sensitivity: public
encryption: none
---

# Local-First Personal/Work Knowledge Base

## Summary

The repository is intended to hold both personal and work-related knowledge in local Markdown files that remain readable in Git, Obsidian, and Codex. [SRC-0002]

## Key Points

- The default storage mode should remain plain Markdown so the wiki is searchable, reviewable, and easy to maintain. [SRC-0002]
- Chat agents should retrieve relevant wiki pages before answering project-specific questions. [SRC-0002]
- Useful chat-derived synthesis should be written back into the wiki when appropriate. [SRC-0002]
- The design prioritizes traceability, low token use, incremental growth, multi-context retrieval, and durable memory across projects. [SRC-0002]

## Links

- [[sources/SRC-0002-project-design-note]]
- [[concepts/persistent-llm-wiki]]
- [[concepts/raw-wiki-schema-layers]]
