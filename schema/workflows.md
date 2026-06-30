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

## Answer-note workflow

Use `.agents/skills/wiki-answer-note/SKILL.md` for persistent answer notes, targeted source lookup, and durable wiki updates before or alongside answer notes.

## Maintenance workflow

Use `.agents/skills/wiki-note-maintenance/SKILL.md` for validation, cleanup, duplicate detection, wiki linting, math-format repair, concept splitting or merging, index/log consistency, and wiki health checks.

Category pages under `wiki/categories/` are generated from frontmatter with `python3 tools/build_category_indexes.py`; use `python3 tools/audit_categories.py` to inspect category drift before broad taxonomy cleanup.
