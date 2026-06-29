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

## Source Import Workflow

Use this workflow when a source is provided from any local path, not only from `raw/sources/`:

1. If the source is outside `raw/sources/`, copy it into `raw/sources/` before ingestion.
2. Assign the next available source ID using the pattern `SRC-XXXX`.
3. Preserve the original file extension.
4. Normalize the imported filename as `SRC-XXXX-short-slug.ext`.
5. Choose the slug using this priority: explicit `--slug`; explicit `--title`; inferred document title or first clear heading; first meaningful content line; original filename stem.
6. Keep the slug lowercase, ASCII where practical, hyphen-separated, and short.
7. Do not modify the original file.
8. Do not modify the imported raw source after copying.
9. Record the original path or filename, imported path, source ID, and hash where practical.
10. Then continue with the normal one-source ingestion workflow.

For simple imports, use `python3 tools/import_source.py /path/to/source.ext`, pass `--title` or `--slug` when a better name is known, or preview with `python3 tools/import_source.py --dry-run /path/to/source.ext`.

## Ingestion Completion Contract

An ingestion is complete only when all of the following are true:

- The source has been imported or identified with a stable `SRC-XXXX` ID.
- The source summary page exists in `wiki/sources/`.
- The source summary page records source ID, imported path, original path or filename when available, SHA256 hash when available, sensitivity, encryption, areas, categories, and tags.
- The source has been skimmed broadly enough to identify its main topics, claims, methods, evidence, limitations, and open questions.
- All major concepts introduced by the source are represented either in existing concept pages or newly created concept pages.
- Important limitations, caveats, contradictions, and validation boundaries are represented in source, concept, question, claim, or tension pages as appropriate.
- `wiki/index.md` links the source and the main concept pages.
- `wiki/log.md` records the ingestion.
- `python3 tools/validate_wiki.py` passes.
- Codex has run a source-specific retrieval QA check, recorded it in the source page, and verified that the wiki can answer the main questions a future user would naturally ask about the source.

If any item is missing, mark the source page with `ingestion_status: partial` or `ingestion_status: needs-review`, document the gap under `## Ingestion QA`, and do not report the ingestion as complete.

## Source-Specific Retrieval QA

During ingestion, Codex must generate 5-10 likely retrieval questions from the source itself and check whether the wiki can answer them using the source page and relevant concept, entity, claim, tension, and question pages. The questions should match the source type and should test retrieval of the source's central contribution, practical implications, evidence, limitations, and unresolved issues.

For a scientific paper, likely questions include:

- What is the central contribution?
- What problem does it address?
- What methods were used?
- What evidence or benchmarks support it?
- What are the main limitations?
- What future work does it identify?
- What claims should not be overgeneralized?

For a project note, likely questions include:

- What decision or design does this note establish?
- What constraints does it introduce?
- What workflow changes are required?
- What remains unresolved?

For an admin or personal document, likely questions include:

- What action, deadline, obligation, or decision does it contain?
- What people, institutions, dates, or dependencies are involved?
- What sensitivity level should it have?
- What should be retrievable later?

Record the checked questions under the source page's `## Ingestion QA` section. The coverage decision must state whether the wiki representation is complete, partial, or needs review, and known gaps must be listed explicitly.

## Sensitive Material Handling

- Do not store credentials, passwords, private keys, API tokens, recovery codes, or secrets in the repo.
- Encrypted sources may have safe plaintext index pages or redacted summaries.
- Decrypted copies should not be committed.
- Codex should not attempt to decrypt files unless explicitly instructed and the decrypted material is locally available.
- Sensitive filenames should be generic when possible.
- If encrypted material is unavailable, mark related claims as inaccessible or pending review instead of guessing.
- Keep the encryption design tool-agnostic unless implementation is explicitly requested.

## Single-Source Ingestion

1. Place or import exactly one source into `raw/sources/`.
2. Ask Codex to ingest only that source.
3. Apply the source import workflow if the source is not already normalized in `raw/sources/`.
4. Create or update the source summary page and relevant concept, entity, claim, tension, or question pages.
5. Run source-specific retrieval QA and record the checked questions, coverage decision, and known gaps in the source page.
6. Apply the ingestion completion contract before reporting the ingestion as complete.
7. Review new or changed wiki pages.
8. Run `python3 tools/validate_wiki.py`.
9. Commit the reviewed changes.
