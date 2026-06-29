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

A request of the form `Ingest <path>` means: inspect the source enough to determine a human-readable title when practical, import the source if needed using the `Source import workflow` in `schema/workflows.md`, pass `--title` or `--slug` to the importer when appropriate, normalize it into `raw/sources/`, then ingest exactly that one source.

Future ingestion tasks automatically include source import if needed, semantic filename normalization, source summary creation, concept extraction or concept updates, representation of important limitations and validation boundaries, source-specific retrieval QA, and an explicit completion decision under the `Ingestion completion contract` in `schema/workflows.md`.


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
type: concept | entity | source | claim | tension | question | overview | category
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

When asked to ingest a source:

1. Inspect the source.
2. Import it into `raw/sources/` if needed, assign or confirm a stable source ID, and normalize the imported filename semantically.
3. Create or update a source summary page in `wiki/sources/`.
4. Extract key claims into existing or new pages.
5. Update relevant concept/entity pages.
6. Add or update tension pages if the source contradicts existing claims.
7. Represent important limitations, caveats, contradictions, validation boundaries, and open questions.
8. Update `wiki/index.md`.
9. Append an entry to `wiki/log.md`.
10. Run source-specific retrieval QA and record it in the source page.
11. Run available validation checks.
12. Decide whether the ingestion is complete, partial, or needs review using the ingestion completion contract.
13. Summarize changed files and unresolved issues using the default report format.

Do not perform a broad refactor during ingestion unless requested.

## Query workflow

When answering a question using the wiki:

1. Read `wiki/index.md` first.
2. Read only the most relevant pages.
3. Answer from the wiki where possible.
4. Identify gaps where the wiki is silent or uncertain.
5. If the answer creates a useful synthesis, propose a page to add or update.

## Lint workflow

When asked to lint or health-check the wiki:

Check for:

* Broken wikilinks.
* Orphan pages.
* Pages missing frontmatter.
* Claims marked `needs-source`.
* Contradictions without a tension page.
* Thin pages that should be merged or expanded.
* Important repeated terms that deserve concept/entity pages.
* Stale pages superseded by newer sources.

Prefer deterministic checks in `tools/` before asking the model to reason over many files.

## Development rules

* Keep tooling simple and local-first.
* Prefer Python standard library unless a dependency is clearly justified.
* Do not add large dependencies without asking.
* Add or update tests when adding validation/search tools.
* After changing tooling, run the relevant tests or validation command.
* Keep generated caches out of git unless explicitly needed.

