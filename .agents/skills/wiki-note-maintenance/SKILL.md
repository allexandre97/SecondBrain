# Wiki Note Maintenance

Use this skill for validation, cleanup, duplicate detection, formatting repair, concept splitting or merging, index/log consistency, and wiki health checks.

## Required contracts

- Apply the `Default Wiki Task Contract` and `Default Report Format` in `schema/workflows.md`.
- Keep maintenance changes focused on the requested task.
- Do not ingest or re-ingest sources.
- Do not change scientific wiki content unless the requested maintenance task requires a narrow provenance-preserving edit.
- Preserve citations, source provenance, sensitivity metadata, encryption metadata, uncertainty, contradictions, limitations, and open questions.
- Run deterministic tools before broad model reasoning where practical.
- Run `python3 tools/validate_wiki.py` before reporting completion.

## Health checks and linting

When asked to lint, validate, or health-check the wiki, check for:

- Broken wikilinks.
- Orphan pages.
- Pages missing frontmatter.
- Unknown page types.
- Claims marked `needs-source`.
- Complete source pages missing `## Ingestion QA`.
- Math-heavy source pages missing `## Equation inventory`.
- Obsidian-discouraged math delimiters such as `\[ ... \]`.
- Contradictions without a tension page.
- Thin pages that should be merged or expanded.
- Important repeated terms that deserve concept/entity pages.
- Stale pages superseded by newer sources.
- `wiki/index.md` links missing for important source, concept, entity, or answer pages.
- `wiki/log.md` entries missing for wiki content changes.

Prefer deterministic checks in `tools/` before asking the model to reason over many files. At minimum, run `python3 tools/validate_wiki.py` before reporting completion.

## Duplicate detection

For duplicate or near-duplicate pages:

1. Search by page title, slug, aliases, wikilinks, source IDs, and repeated headings.
2. Compare provenance before merging; do not merge pages that represent distinct concepts, entities, claims, tensions, or questions.
3. Preserve all citations, source IDs, sensitivity metadata, encryption metadata, contradictions, caveats, and open questions.
4. Prefer a redirect-style note only when this wiki has an established convention for it; otherwise update links and leave a short deprecation note with frontmatter status when needed.
5. Update incoming wikilinks, `wiki/index.md`, and `wiki/log.md`.
6. Run validation.

## Math-format repair

When repairing math formatting:

- Convert `\[ ... \]` display math to `$$ ... $$`.
- Use `$...$` for inline math.
- Put display math on its own lines, with blank lines around it when practical.
- Do not put important equations in code fences.
- Do not alter mathematical meaning while reformatting.
- Do not guess missing formulas. Mark uncertain formulas under `## Mathematical gaps` on the relevant source page.
- Preserve source equation numbers, local labels, source IDs, and variable definitions.
- For long formulas in tables, move the display equation into normal Markdown and let the table link to that section.

## Concept splitting and merging

When splitting or merging concept pages:

- Preserve provenance for every non-trivial claim.
- Preserve sensitivity and encryption metadata from all affected pages.
- Keep uncertainty and contradictions explicit.
- Move reusable definitions, evidence, links, open questions, and limitations to the most appropriate durable page.
- Create or update tension pages if the split or merge reveals incompatible claims.
- Update backlinks, related frontmatter, `wiki/index.md`, and `wiki/log.md`.
- Run validation.

## Index and log consistency

When changing wiki content:

- Ensure `wiki/index.md` links important new or renamed pages.
- Append a concise entry to `wiki/log.md` for source ingestion, answer notes, durable page creation, merges, splits, deprecations, major repairs, and validation-focused maintenance.
- Do not log purely mechanical edits outside wiki content unless they affect wiki behavior or instructions.
- Preserve existing chronology and style in the log.

## Maintenance report

Use the default report format. Include unresolved structural issues, validation warnings, or remaining `needs-source` items when relevant. If no issues remain, report `None` under unresolved issues.
