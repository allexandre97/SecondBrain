# Repository Guidelines

## Project Structure & Module Organization

This repository is a local-first LLM-maintained wiki, not an application scaffold. Keep the top-level layout focused on the wiki architecture:

- `raw/sources/` for immutable source material.
- `wiki/` for synthesized Markdown knowledge base pages.
- `schema/` for conventions, templates, workflows, and validation rules.
- `tools/` for local maintenance scripts.
- `tests/` for smoke tests and validation-tool tests.

Avoid placing generated caches, dependency folders, or local environment artifacts in version control.

## Build, Test, and Development Commands

Run wiki tooling from the repository root:

- `python3 tools/validate_wiki.py` to validate required structure, frontmatter, and Obsidian wikilinks.
- `python3 tools/search_wiki.py <query>` for deterministic first-pass topical retrieval.
- `python3 tools/suggest_categories.py` to report deterministic category suggestions without applying them.
- `python3 tools/audit_categories.py` to inspect category drift.
- `python3 tools/build_category_indexes.py` to regenerate category and dashboard navigation pages.

Keep commands deterministic and avoid requiring machine-specific paths.

## Coding Style & Naming Conventions

Keep tooling simple, readable, and standard-library-only unless a dependency is explicitly justified. Use clear names, consistent indentation, and small modules with focused responsibilities.

## Testing Guidelines

Add tests alongside new tooling changes when practical. Use recognizable names such as `test_<feature>.py` or small shell smoke tests, and document any required fixtures under `tests/fixtures/`.

## Commit & Pull Request Guidelines

This repository has no commit history yet, so no established commit convention exists. Use short, imperative commit subjects, for example `Add camera configuration parser` or `Document setup workflow`.

Pull requests should include a concise summary, testing performed, linked issues when applicable, and screenshots or logs for user-facing behavior changes.

# LLM Wiki Repository Instructions

## Purpose

This repository is an LLM-maintained knowledge base.

The repo has three layers:

* `raw/`: immutable source material. The agent may read from this directory but must not modify source files.
* `wiki/`: synthesized markdown knowledge base maintained by the agent.
* `schema/`: conventions, templates, workflows, and validation rules that govern the wiki.

The goal is not ordinary RAG. The goal is to compile source material into a persistent, interlinked wiki that accumulates synthesis over time.

## Core rules

* Do not modify files in `raw/` unless explicitly instructed.
* Prefer small, focused changes.
* Do not ingest more than one source at a time unless explicitly asked.
* Every non-trivial claim added to `wiki/` must be traceable to one or more sources.
* Do not let chat-only conclusions disappear. If a useful synthesis is produced, propose filing it into `wiki/`.
* Preserve uncertainty, contradictions, and open questions instead of smoothing them away.
* Use concise but human-readable writing. Do not use unexplained shorthand.
* Use abbreviations only if they are defined in `schema/glossary.md`.

## Default wiki task behavior

For wiki-related work, apply the `Default wiki task contract` in `schema/workflows.md` unless the user explicitly overrides it. Use the `Default report format` from `schema/workflows.md` when reporting completion. Preserve provenance, sensitivity metadata, encryption metadata, and the narrow scope of the requested task.

For `Ingest <path>`, `Ingest <these files/folder>`, source import, source-bundle ingestion, or math-heavy source ingestion, use the repository-scoped Codex skill at `.agents/skills/wiki-source-ingestion/SKILL.md`.

For `Answer in the wiki: <question>` or `Write a wiki answer for: <question>`, use the repository-scoped Codex skill at `.agents/skills/wiki-answer-note/SKILL.md`.

For validation, cleanup, duplicate detection, math-format repair, concept splitting or merging, index/log consistency, or wiki health checks, use the repository-scoped Codex skill at `.agents/skills/wiki-note-maintenance/SKILL.md`.


## Expected structure

Use this structure unless the user explicitly changes it:

```text
raw/
  sources/

wiki/
  index.md
  log.md
  overview.md
  answers/
  sources/
  concepts/
  entities/
  claims/
  tensions/
  questions/
  categories/

schema/
  glossary.md
  page_templates.md
  workflows.md
  lint_rules.md

tools/
  validate_wiki.py
  search_wiki.py
  import_source.py
  suggest_categories.py
  audit_categories.py
  build_category_indexes.py

tests/
```

Open the repository root, not `wiki/`, as the Obsidian vault.

## Page conventions

All wiki pages should use YAML frontmatter where practical:

```yaml
---
type: concept | entity | source | claim | tension | question | answer | overview | category
status: seed | active | needs-review | deprecated
created: YYYY-MM-DD
updated: YYYY-MM-DD
areas: []
categories: []
tags: []
related: []
sources: []
sensitivity: public
encryption: none
---
```

Use Obsidian-style wikilinks for internal links:

```md
[[wiki/concepts/example-concept]]
[[wiki/entities/example-entity]]
```

Prefer short sections:

* Summary
* Key points
* Evidence
* Links
* Open questions
* Contradictions / tensions

## Source IDs and citations

Assign each source a stable source ID, for example:

```text
SRC-0001
SRC-0002
```

When adding claims, cite source IDs locally in the wiki. Use this style:

```md
Claim text. [SRC-0001]
```

If the source has page numbers, sections, timestamps, or line numbers, include them:

```md
Claim text. [SRC-0001, p. 12]
Claim text. [SRC-0002, section 3.1]
```

Do not invent citations. If provenance is unclear, mark the claim as `needs-source`.

## Ingest workflow

When asked to ingest a source, use `.agents/skills/wiki-source-ingestion/SKILL.md`.

Do not perform a broad refactor during ingestion unless requested.

## Query workflow

When retrieving topical knowledge from the wiki:

1. Run `python3 tools/search_wiki.py <query>` first unless the exact target path is already known.
2. Inspect and read only the strongest relevant sections/pages.
3. Use `tools/query_graph.py` afterwards when relationship traversal would help.
4. Answer from the wiki where possible, then consult raw sources only when provenance or missing detail requires it.
5. Identify gaps and propose a durable page update when the answer creates reusable synthesis.

Do not broadly grep or scan `wiki/` when deterministic search can identify candidates first. Targeted `grep`, `find`, and direct reads remain appropriate after retrieval has narrowed the scope. `wiki/index.md` remains an orientation aid. Search scores rank lexical relevance, not truth, confidence, evidence strength, or source quality.

Requests such as:

```text
Answer in the wiki: <question>
```

or:

```text
Write a wiki answer for: <question>
```

mean Codex should apply `.agents/skills/wiki-answer-note/SKILL.md`: search the wiki first, answer from existing wiki pages when possible, consult raw sources only if the wiki is insufficient, update durable wiki pages when missing reusable knowledge is found, create a readable answer note under `wiki/answers/`, run validation, and report the answer note path and any durable pages updated.

## Lint workflow

When asked to lint, validate, clean up, detect duplicates, repair formatting, split or merge concepts, or health-check the wiki, use `.agents/skills/wiki-note-maintenance/SKILL.md`. Prefer deterministic checks in `tools/` before asking the model to reason over many files.

## Development rules

* Keep tooling simple and local-first.
* Prefer Python standard library unless a dependency is clearly justified.
* Do not add large dependencies without asking.
* Add or update tests when adding validation/search tools.
* After changing tooling, run the relevant tests or validation command.
* Keep generated caches out of git unless explicitly needed.
