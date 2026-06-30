# SecondBrain

An LLM-assisted wiki workspace for turning raw source material into reviewed Markdown notes.

## Structure

- `raw/sources/` stores source material waiting to be ingested.
- `wiki/` stores curated wiki pages.
- `schema/` documents page templates, glossary terms, workflows, and lint rules.
- `tools/` stores local maintenance scripts.
- `tests/` stores local smoke tests for wiki tooling.

## Basic Workflow

1. Add one source file or source note under `raw/sources/`, or import a local file with `tools/import_source.py`.
2. Ask Codex to ingest that one source into the wiki.
3. Review the changed files under `wiki/` and `schema/`.
4. Run `python3 tools/validate_wiki.py`.
5. Commit the reviewed wiki changes.

Do not ingest multiple sources at once unless the review scope is intentionally broad.

Source pages should keep stable `SRC-XXXX` IDs while using human-readable `display_title`, `short_title`, aliases, and H1 titles. When a source file is present in `raw/sources/`, include a visible raw-source link on the source page. Do not expose machine-specific absolute original paths in public wiki metadata; keep only the original filename and an omission note when useful.

## Validation

Run the local smoke check from the repository root:

```sh
python3 tools/validate_wiki.py
```

The validator checks required directories, core wiki entry files, wiki page frontmatter, and obvious broken Obsidian wikilinks.

## Categories

Category membership comes from page frontmatter. Prefer category paths listed in `schema/category_registry.md`; record uncertain category candidates in notes instead of silently inventing new branches.

Regenerate category browsing pages from frontmatter with:

```sh
python3 tools/build_category_indexes.py
```

Audit category usage with:

```sh
python3 tools/audit_categories.py
```

## Search

Use the local plain-text search helper to find compact snippets from Markdown files under `wiki/`:

```sh
python3 tools/search_wiki.py wiki
python3 tools/search_wiki.py source ingestion
```

The search is case-insensitive, recursive, and uses only the Python standard library.

## Source Import

Import a local file into `raw/sources/` before ingestion:

```sh
python3 tools/import_source.py /path/to/source.pdf
python3 tools/import_source.py /path/to/source.pdf --title "Training a force field for proteins and small molecules from scratch"
python3 tools/import_source.py /path/to/source.pdf --slug garnet-force-field
python3 tools/import_source.py --dry-run /path/to/source.pdf
```

The importer assigns the next `SRC-XXXX` ID, creates a normalized filename, copies the file without modifying the original, and prints the imported path, slug source, and SHA256 hash. Future prompts can use `Ingest /path/to/file.ext`; Codex should inspect the file for a human-readable title and import it first if it is not already in `raw/sources/`.
