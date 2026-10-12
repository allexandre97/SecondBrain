# Workflows

## Default Wiki Task Contract

Apply this contract to wiki-related tasks unless the user explicitly overrides it:

- Keep changes focused on the requested task.
- Do not ingest extra sources.
- Do not add embeddings, databases, MCP, plugins, app code, encryption tooling, or dependencies unless explicitly requested.
- Preserve citations and provenance for non-trivial claims.
- Preserve sensitivity and encryption metadata when editing pages.
- Update `wiki/index.md` and `wiki/log.md` when changing wiki content.
- Run `python3 tools/validate_wiki.py` before reporting completion.
- Keep source pages readable in Obsidian: preserve `source_id`, use human-readable `display_title`, `short_title`, aliases, and H1 titles, and include raw-source links when the repository copy exists.
- Prefer categories from `schema/category_registry.md`; record uncertain category candidates instead of silently inventing new taxonomy branches.
- Open the repository root, not `wiki/`, as the Obsidian vault.

## Default Report Format

Use this format when reporting completed wiki work:

```md
## Result

Short summary of what changed.

## Files Changed

- `path/to/file.md` - brief reason.

## Validation

- `python3 tools/validate_wiki.py`: passed or failed, with the key error if failed.

## Unresolved Issues

- Remaining structural issues, open questions, or `None`.
```

## Minimal ingestion prompts

Use `.agents/skills/wiki-source-ingestion/SKILL.md` for detailed source import, ingestion mode inference, source-bundle handling, math-heavy ingestion, source-specific retrieval QA, Obsidian-compatible math, and ingestion completion rules. Detailed user-provided metadata is optional. Codex should accept minimal ingestion prompts and infer the needed metadata where practical. Examples:

```text
Ingest /path/to/source.pdf
```

```text
Ingest these two files as one source bundle:
Main paper: /path/to/main.pdf
Supplement: /path/to/supplement.pdf
```

```text
Ingest this folder as one source bundle: /path/to/project_docs/
```

When metadata is absent, infer title, slug, source type, bundle role, areas, categories, sensitivity, encryption, and coverage profile from filenames, document metadata, headings, source content, repository context, and user wording. Use the category registry before adding new category paths. Record meaningful uncertainty in the source page instead of forcing the user to specify everything upfront. Ask for clarification only when ambiguity blocks safe ingestion, such as unclear sensitivity for private material, unclear bundle boundaries, conflicting source roles, or a taxonomy decision that would create a new top-level branch.

## Knowledge retrieval workflow

For topical retrieval, run `python3 tools/search_wiki.py <query>` before broad wiki scanning, inspect only the strongest sections/pages (each result reports the section's file line range as `line_start`/`line_end`), and then use `tools/query_graph.py` if relationship traversal would help. Skip lexical search when the exact path is already known. Targeted file search remains appropriate after candidate selection. Search scores express lexical relevance only, not truth, confidence, evidence strength, or source quality. Consult raw sources only as required by provenance and source-verification workflows.

## Currency workflow

Time scope and currency fields are defined in `schema/page_templates.md` under `Time Scope and Currency`.

When retrieving:

- Every search result reports `scope`, `currency`, `as_of`, and `superseded_by`. Treat `historical` and `superseded` results as records of a past state, not as the current state; follow `superseded_by` for current information. Use `python3 tools/search_wiki.py --current <query>` when only the present state matters, and the default search when rationale or history matters.
- When reaching a page by wikilink rather than by search, read its first 20 or so lines (frontmatter and any `> [!currency]` banner) before relying on a section.
- For project state, the project repository is authoritative. When a page has `as_of_commit` and the repository is available, compare that commit with the repository's current state before relying on implementation details.

When project state changes:

1. Rewrite affected `living` pages in place and update their `as_of`; add one line to their `## Changes` list. Do not append dated update sections.
2. For each affected `snapshot`, run `python3 tools/set_currency.py <page> --superseded-by <replacement> --note "<one-line reason>"`, or `--currency historical --note "..."` when no single page replaces it. Do not otherwise edit the snapshot's body.
3. Move lessons that remain valid into claim or concept pages rather than leaving them only in a superseded snapshot.
4. New project-state pages must declare `scope`, `currency`, and `as_of` from the start, and list their dated `project_evidence`. Every answer page declares `scope`, even when it is `timeless`.
5. `tools/set_currency.py` also adds or removes the `**Superseded:**`/`**Historical:**` marker on the page's `wiki/index.md` entry; do not edit those markers by hand. When writing a new index entry for a non-current page, run the tool on the page afterwards.

### Recording change over time

Readers often see only one section, so each section must be true as written, without a later section correcting it.

- **Timeless pages** (claims, questions, tensions, concepts): lead with the current statement or status, rewritten when evidence changes it. Record dated observations as bullets in a `## Evidence timeline` section (`- 2026-10-05: observation. [[evidence page]]`), oldest first. Do not add dated update or status headings. A question that is moot for a project but scientifically open says so in its status line.
- **Living pages**: rewrite the body to describe the present; add one line per change to `## Changes` (`- 2026-10-11: what changed. [[evidence page]]`).
- **Snapshots**: the body describes only the `as_of` state. Later developments go to the relevant living page or a newer snapshot, and the old snapshot is marked with `tools/set_currency.py`; never append to it.

`tools/validate_wiki.py` warns on dated update or status headings on any page, and on any dated heading on a living page.

## Answer-note workflow

Use `.agents/skills/wiki-answer-note/SKILL.md` for persistent answer notes, targeted source lookup, and durable wiki updates before or alongside answer notes.

## Maintenance workflow

Use `.agents/skills/wiki-note-maintenance/SKILL.md` for validation, cleanup, duplicate detection, wiki linting, math-format repair, concept splitting or merging, index/log consistency, and wiki health checks.

Category pages and dashboard indexes under `wiki/categories/` and `wiki/dashboards/` are generated from frontmatter with `python3 tools/build_category_indexes.py`; use `python3 tools/suggest_categories.py` and `python3 tools/audit_categories.py` to inspect category drift before broad taxonomy cleanup.
