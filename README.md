# SecondBrain

An LLM-assisted wiki workspace for turning raw source material into reviewed Markdown notes.

## Structure

- `raw/sources/` stores source material waiting to be ingested.
- `wiki/` stores curated wiki pages.
- `schema/` documents page templates, glossary terms, workflows, and lint rules.
- `tools/` stores local maintenance scripts.
- `tests/` stores local smoke tests for wiki tooling.

## Obsidian Vault

Open the repository root, not `wiki/`, as the Obsidian vault.

This keeps raw sources, wiki pages, schemas, and tools in one local-first workspace. Source pages link to files under `raw/sources/` without duplicating large PDFs under `wiki/`.

## Obsidian Graph View

Recommended graph filter:

```text
path:wiki/ -[graph_exclude:true]
```

Also turn off Attachments in Graph view to keep raw PDFs and other source files out of the graph.

## Basic Workflow

1. Add one source file or source note under `raw/sources/`, or import a local file with `tools/import_source.py`.
2. Ask Codex to ingest that one source into the wiki.
3. Review the changed files under `wiki/` and `schema/`.
4. Run `python3 tools/validate_wiki.py`.
5. Commit the reviewed wiki changes.

Do not ingest multiple sources at once unless the review scope is intentionally broad.

Source pages should keep stable `SRC-XXXX` IDs while using human-readable `display_title`, `short_title`, aliases, and H1 titles. When a source file is present in `raw/sources/`, include a visible raw-source link on the source page. Do not expose machine-specific absolute original paths in public wiki metadata; keep only the original filename and an omission note when useful.

Older ingested sources should be migrated with source-migration audits and focused cluster backfills, not blindly re-ingested. Use `python3 tools/audit_source_migration.py` to inventory missing authors, citation links, claims, questions, tensions, graph links, and raw-source metadata before planning those backfills.

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

Suggest missing categories without applying changes with:

```sh
python3 tools/suggest_categories.py
```

## Concept Browsing

Concept pages stay flat under `wiki/concepts/` to keep Obsidian wikilinks stable and avoid link churn. Semantic browsing is provided by generated dashboards built from concept frontmatter instead of by moving files into nested folders.

Regenerate concept dashboards with:

```sh
python3 tools/build_concept_indexes.py
```

This writes concept views under `wiki/dashboards/`, including category, method, biomolecule, source-cluster, and high-connectivity concept dashboards.

## Deterministic Wiki Search

Use search as the cheap first pass for locating topical wiki content before opening pages or traversing the knowledge graph:

```sh
python3 tools/search_wiki.py "force field optimization"
python3 tools/search_wiki.py "free energy" --type concept --limit 5
python3 tools/search_wiki.py "Garnet experimental observables" --json --limit 5
```

The tool uses Python's SQLite FTS5 and built-in BM25 ranking. It indexes each Markdown page under `wiki/` as logical heading-based sections, including page/display/short titles, aliases, headings, body text, categories, tags, areas, and source IDs. Ordinary queries are safely tokenized and use AND matching first, then deterministic OR fallback only if AND returns no filtered results. Shell quoting only groups arguments; it does not request raw FTS syntax.

Supported filters are exact `--type`, `--category`, `--status`, `--source`, and `--tag`; `--path` performs an ASCII-case-insensitive repository-relative substring match. `--json` emits JSON only. Results are capped at two sections per page. The displayed `score` is `-bm25(...)`, so higher is better. Fixed FTS column weights are title/display/short title `12`, aliases `8`, section hierarchy `6`, categories/tags/areas/source IDs `3`, and body `1`.

Pages marked `generated: true` are excluded by default. `--include-generated` uses a separate index containing them. Regenerable databases live in `.cache/wiki-search.sqlite3` and `.cache/wiki-search-generated.sqlite3`; a sorted path/size/high-resolution-mtime manifest triggers a full rebuild when the Markdown corpus changes. Force a rebuild with:

```sh
python3 tools/search_wiki.py --rebuild
```

Search is lexical retrieval, not semantic inference: ranking does not express truth, confidence, evidence strength, or source quality. Use `tools/query_graph.py` separately after selecting candidate pages when relationships matter, and verify sources according to the provenance workflow. Limitations include exact-token rather than fuzzy/semantic matching, simple frontmatter parsing, and heading-based rather than full CommonMark parsing. SQLite FTS5 support is required; there is no degraded fallback.

## Knowledge Graph

Build a deterministic graph of wiki pages, source IDs, categories, source bundles, citations, authors, and wikilinks:

```sh
python3 tools/build_knowledge_graph.py
```

This writes `wiki/graph/knowledge_graph.json` and `wiki/graph/knowledge_graph_summary.md`. Query graph neighborhoods before deeper answer-note work when useful:

```sh
python3 tools/query_graph.py --start wiki/concepts/free-energy-estimation --depth 2
python3 tools/query_graph.py --category research/molecular-simulation/free-energy
python3 tools/query_graph.py --source-id SRC-0005
```

The graph tooling uses only the Python standard library and is intended for deterministic traversal, not embeddings or vector search.

## Source Import

Import a local file into `raw/sources/` before ingestion:

```sh
python3 tools/import_source.py /path/to/source.pdf
python3 tools/import_source.py /path/to/source.pdf --title "Training a force field for proteins and small molecules from scratch"
python3 tools/import_source.py /path/to/source.pdf --slug garnet-force-field
python3 tools/import_source.py --dry-run /path/to/source.pdf
```

The importer assigns the next `SRC-XXXX` ID, creates a normalized filename, copies the file without modifying the original, and prints the original filename, metadata omission note, imported path, slug source, and SHA256 hash. Use `--show-original-path` only when local debugging requires printing the absolute original path. Future prompts can use `Ingest /path/to/file.ext`; Codex should inspect the file for a human-readable title and import it first if it is not already in `raw/sources/`.
