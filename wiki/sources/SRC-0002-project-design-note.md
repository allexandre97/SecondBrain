---
type: source
status: active
created: 2026-06-29
updated: 2026-07-01
source_id: SRC-0002
display_title: "Project Design Note"
short_title: "Project Design Note"
aliases:
  - "SRC-0002"
  - "Project Design Note"
source_path: raw/sources/SRC-0002-project-design-note.md
areas:
  - research
categories:
  - research/llm-wiki/design
  - admin/wiki-governance
metadata_review_status: not-applicable
citation_match_status: reviewed
cqt_review_status: source-local
tags:
  - design-note
  - llm-wiki
related:
  - "[[wiki/concepts/local-first-personal-work-knowledge-base]]"
  - "[[wiki/concepts/multi-category-wiki-organization]]"
  - "[[wiki/concepts/optional-encryption-and-sensitivity-metadata]]"
sources:
  - SRC-0002
sensitivity: public
encryption: none
---

# Project Design Note

Source ID: `SRC-0002`

## Raw source

- Repository path: `raw/sources/SRC-0002-project-design-note.md`
- Open raw source: [raw/sources/SRC-0002-project-design-note.md](../../raw/sources/SRC-0002-project-design-note.md)

## Summary

This source specifies the current repository design: a local-first LLM knowledge base for personal and work information, with immutable raw sources, synthesized wiki pages, Obsidian-friendly Markdown, multi-category metadata, selective privacy controls, and reusable Codex task rules. [SRC-0002]

## Key Points

- The repository should remain local-first, plain Markdown by default, and easy to inspect in Git, Obsidian, and Codex. [SRC-0002]
- Pages should use metadata for areas, categories, tags, related pages, sensitivity, and encryption state rather than relying on one folder-based category. [SRC-0002]
- Sensitive material should be handled selectively: avoid storing secrets, use redacted summaries where useful, and do not commit decrypted copies. [SRC-0002]
- The project should initially avoid embeddings, vector databases, web apps, Obsidian plugins, MCP servers, complex dependencies, mandatory encryption, and opaque compression. [SRC-0002]
- Recurring Codex constraints and report formats should live in `AGENTS.md` and `schema/workflows.md`. [SRC-0002]

## Links

- [[wiki/concepts/local-first-personal-work-knowledge-base]]
- [[wiki/concepts/multi-category-wiki-organization]]
- [[wiki/concepts/wiki-page-metadata]]
- [[wiki/concepts/optional-encryption-and-sensitivity-metadata]]
- [[wiki/concepts/reusable-codex-task-contracts]]
- [[wiki/concepts/raw-wiki-schema-layers]]
- [[wiki/concepts/source-ingestion]]

## Metadata notes

This is an internal project-design source rather than an ordinary scientific paper. Paper-style author/year metadata is not central for migration status; semantic review is intentionally kept source-local.

## Open Questions

- Which concrete category vocabulary should be used first as personal and work sources are added? [SRC-0002]
