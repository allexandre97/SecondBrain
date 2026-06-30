# Wiki Answer Note

Use this skill for prompts such as `Answer in the wiki: <question>` or `Write a wiki answer for: <question>`.

## Required contracts

- Apply the `Default Wiki Task Contract` and `Default Report Format` in `schema/workflows.md`.
- Start from the wiki, not from broad raw-source reading.
- Preserve citations, source provenance, sensitivity metadata, encryption metadata, uncertainty, contradictions, limitations, and open questions.
- Do not ingest or re-ingest sources unless explicitly asked.
- Run `python3 tools/validate_wiki.py` before reporting completion.

## Answer-note workflow

1. Start from `wiki/index.md`.
2. Search relevant wiki pages.
3. Identify whether the wiki already answers the question.
4. If the wiki is sufficient, write the answer note using wiki pages only.
5. If the wiki is insufficient, consult original sources using targeted source lookup.
6. Use source summaries, source outlines, equation inventories, proof maps, headings, local text search, and relevant sections before reading an entire source.
7. Read the whole source only when the query is broad, the source is short, or targeted lookup fails.
8. If raw-source lookup reveals reusable knowledge, update the relevant durable wiki pages before or alongside the answer note.
9. Preserve citations and provenance.
10. Record which wiki pages and raw sources were used.
11. Record which wiki pages were updated.
12. Mark remaining gaps clearly.
13. Run `python3 tools/validate_wiki.py`.
14. Report the answer note path and any durable pages updated.

Answer notes belong under `wiki/answers/` and should use the answer-page template in `schema/page_templates.md`. They are readable generated responses, not replacements for durable source, concept, question, claim, or tension pages.

## Targeted source lookup

When the wiki lacks an answer, do not blindly re-read or re-ingest the entire source. Use this staged strategy:

```text
source page summary
-> source outline / table of contents
-> equation inventory / proof map, if present
-> local search in raw source text
-> relevant section/page
-> neighboring section/page
-> broader scan only if needed
```

Prefer the narrowest lookup that can answer the question with provenance. Move to broader source reading only when the query is broad, the source is short, or targeted lookup fails to find the needed context. Raw-source consultation during a query is not ingestion unless the user explicitly asks to ingest or re-ingest a source.

## Durable wiki updates

Before or alongside an answer note, update durable pages when the answer depends on reusable knowledge that is missing or underrepresented in the wiki:

- Source pages for missing summary, limitations, retrieval QA notes, source outline pointers, equation inventories, or proof-map pointers.
- Concept or entity pages for reusable definitions, relationships, or context.
- Claim pages for discrete cited claims that should be retrievable independently.
- Tension pages for contradictions, conflicts, or incompatible interpretations.
- Question pages for open questions that remain unresolved after lookup.

Keep durable updates narrow and cite them locally. Preserve existing sensitivity and encryption metadata. Do not turn answer-note work into a broad cleanup unless requested.

## Answer note expectations

- Use YAML frontmatter matching the answer-page template where practical.
- Include a concise answer, the evidence used, gaps or uncertainty, and links to durable wiki pages.
- Cite source IDs for non-trivial claims.
- Do not invent citations. If provenance is unclear, mark the claim as `needs-source` or list it as a gap.
- If the answer creates a useful synthesis, keep it in the answer note and ensure reusable parts are represented in durable pages where appropriate.
