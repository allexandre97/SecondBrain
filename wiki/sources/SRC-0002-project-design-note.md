---
type: source
status: active
created: 2026-06-29
updated: 2026-06-29
source_id: SRC-0002
source_path: raw/sources/SRC-0002-project-design-note.md
areas:
  - research
categories:
  - research/llm-wiki/design
  - admin/wiki-governance
tags:
  - design-note
  - llm-wiki
related:
  - "[[concepts/local-first-personal-work-knowledge-base]]"
  - "[[concepts/multi-category-wiki-organization]]"
  - "[[concepts/optional-encryption-and-sensitivity-metadata]]"
sources:
  - SRC-0002
sensitivity: public
encryption: none
---

# SRC-0002: Project Design Note

## Summary

This source specifies the current repository design: a local-first LLM knowledge base for personal and work information, with immutable raw sources, synthesized wiki pages, Obsidian-friendly Markdown, multi-category metadata, selective privacy controls, and reusable Codex task rules. [SRC-0002]

## Key Points

- The repository should remain local-first, plain Markdown by default, and easy to inspect in Git, Obsidian, and Codex. [SRC-0002]
- Pages should use metadata for areas, categories, tags, related pages, sensitivity, and encryption state rather than relying on one folder-based category. [SRC-0002]
- Sensitive material should be handled selectively: avoid storing secrets, use redacted summaries where useful, and do not commit decrypted copies. [SRC-0002]
- The project should initially avoid embeddings, vector databases, web apps, Obsidian plugins, MCP servers, complex dependencies, mandatory encryption, and opaque compression. [SRC-0002]
- Recurring Codex constraints and report formats should live in `AGENTS.md` and `schema/workflows.md`. [SRC-0002]

## Links

- [[concepts/local-first-personal-work-knowledge-base]]
- [[concepts/multi-category-wiki-organization]]
- [[concepts/wiki-page-metadata]]
- [[concepts/optional-encryption-and-sensitivity-metadata]]
- [[concepts/reusable-codex-task-contracts]]
- [[concepts/raw-wiki-schema-layers]]
- [[concepts/source-ingestion]]

## Open Questions

- Which concrete category vocabulary should be used first as personal and work sources are added? [SRC-0002]
