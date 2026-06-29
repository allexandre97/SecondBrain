# SecondBrain

An LLM-assisted wiki workspace for turning raw source material into reviewed Markdown notes.

## Structure

- `raw/sources/` stores source material waiting to be ingested.
- `wiki/` stores curated wiki pages.
- `schema/` documents page templates, glossary terms, workflows, and lint rules.
- `tools/` stores local maintenance scripts.
- `src/`, `tests/`, `docs/`, and `assets/` are reserved for future project code, tests, documentation, and static assets.

## Basic Workflow

1. Add one source file or source note under `raw/sources/`.
2. Ask Codex to ingest that one source into the wiki.
3. Review the changed files under `wiki/` and `schema/`.
4. Run `python3 tools/validate_wiki.py`.
5. Commit the reviewed wiki changes.

Do not ingest multiple sources at once unless the review scope is intentionally broad.

## Validation

Run the local smoke check from the repository root:

```sh
python3 tools/validate_wiki.py
```

The validator checks required directories, core wiki entry files, wiki page frontmatter, and obvious broken Obsidian wikilinks.
