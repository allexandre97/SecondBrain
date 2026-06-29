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

## Sensitive Material Handling

- Do not store credentials, passwords, private keys, API tokens, recovery codes, or secrets in the repo.
- Encrypted sources may have safe plaintext index pages or redacted summaries.
- Decrypted copies should not be committed.
- Codex should not attempt to decrypt files unless explicitly instructed and the decrypted material is locally available.
- Sensitive filenames should be generic when possible.
- If encrypted material is unavailable, mark related claims as inaccessible or pending review instead of guessing.
- Keep the encryption design tool-agnostic unless implementation is explicitly requested.

## Single-Source Ingestion

1. Place the source in `raw/sources/`.
2. Ask Codex to ingest only that source.
3. Review new or changed wiki pages.
4. Run `python3 tools/validate_wiki.py`.
5. Commit the reviewed changes.
