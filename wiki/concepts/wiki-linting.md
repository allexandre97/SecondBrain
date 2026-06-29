---
type: concept
status: active
created: 2026-06-29
updated: 2026-06-29
areas:
  - admin
categories:
  - admin/wiki-maintenance
tags:
  - maintenance
related:
  - "[[concepts/reusable-codex-task-contracts]]"
sources:
  - SRC-0001
  - SRC-0002
sensitivity: public
encryption: none
---

# Wiki Linting

## Summary

Wiki linting is periodic maintenance that checks the knowledge base for structural and content health issues. [SRC-0001]

## Key Points

- Suggested checks include broken links, orphan pages, missing cross-references, stale claims, contradictions, and important concepts without pages. [SRC-0001]
- Deterministic tools are useful for repeatable checks before asking an LLM to reason across many pages. [SRC-0001]
- In this repository, `tools/validate_wiki.py` is the current minimal lint check. [SRC-0001]
- SRC-0002 reinforces that Codex should run validation before reporting completion. [SRC-0002]

## Links

- [[sources/SRC-0001-karpathy-llm-knowledge-base]]
- [[sources/SRC-0002-project-design-note]]
- [[concepts/source-ingestion]]
- [[concepts/reusable-codex-task-contracts]]
