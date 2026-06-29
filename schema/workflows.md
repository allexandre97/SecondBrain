# Workflows

## Single-Source Ingestion

1. Place the source in `raw/sources/`.
2. Ask Codex to ingest only that source.
3. Review new or changed wiki pages.
4. Run `python3 tools/validate_wiki.py`.
5. Commit the reviewed changes.
