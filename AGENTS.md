# Repository Guidelines

## Project Structure & Module Organization

This repository currently contains no source files, tests, assets, or build configuration. As the project grows, keep the top-level layout predictable and easy to scan:

- `src/` for application or library code.
- `tests/` for automated tests that mirror the `src/` structure.
- `docs/` for design notes, usage guides, and architecture decisions.
- `assets/` for static files such as images, fixtures, or sample data.

Avoid placing generated files, dependency folders, or local environment artifacts in version control.

## Build, Test, and Development Commands

No build or test commands are configured yet. When tooling is introduced, document the canonical commands here and prefer scripts that can be run from the repository root. Examples:

- `npm test` to run a JavaScript or TypeScript test suite.
- `make build` to compile or package the project.
- `python -m pytest` to run Python tests.

Keep commands deterministic and avoid requiring machine-specific paths.

## Coding Style & Naming Conventions

Follow the conventions of the language or framework added to the repository. Until a formatter or linter is configured, use clear names, consistent indentation, and small modules with focused responsibilities. Prefer descriptive file names such as `user_service.py`, `api-client.ts`, or `camera_config.c`, depending on the language in use.

When formatters are added, commit their configuration and make formatting part of the normal development workflow.

## Testing Guidelines

Add tests alongside new functionality. Mirror source paths where practical, and use recognizable names such as `test_<feature>.py`, `<feature>.test.ts`, or `<module>_test.go`. Include regression tests for bug fixes and document any required fixtures under `tests/fixtures/`.

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
  assets/

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

tests/
```

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
[[concepts/example-concept]]
[[entities/example-entity]]
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

When answering a question using the wiki:

1. Read `wiki/index.md` first.
2. Read only the most relevant pages.
3. Answer from the wiki where possible.
4. Identify gaps where the wiki is silent or uncertain.
5. If the answer creates a useful synthesis, propose a page to add or update.

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
