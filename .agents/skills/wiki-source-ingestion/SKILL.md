---
name: wiki-source-ingestion
description: Use for importing and ingesting source files into the SecondBrain wiki, including source bundles, math-heavy sources, provenance, retrieval QA, and ingestion completion checks.
---

# Wiki Source Ingestion

Use this skill for `Ingest <path>`, `Ingest <these files/folder>`, source-bundle ingestion, source import, math-heavy source ingestion, and source-specific retrieval QA.

## Required contracts

- Apply the `Default Wiki Task Contract` and `Default Report Format` in `schema/workflows.md`.
- Do not ingest extra sources.
- Do not modify files in `raw/` unless explicitly instructed, except importing requested source files into `raw/sources/`.
- Preserve source provenance, sensitivity metadata, encryption metadata, uncertainty, contradictions, limitations, and open questions.
- Every non-trivial wiki claim must cite one or more stable source IDs.
- Run `python3 tools/validate_wiki.py` before reporting completion.

## Minimal ingestion prompts

Detailed user-provided metadata is optional. Accept minimal prompts such as:

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

When metadata is absent, infer title, slug, source type, bundle role, areas, categories, sensitivity, encryption, and coverage profile from filenames, document metadata, headings, source content, repository context, and user wording. Prefer category paths already documented in `schema/category_registry.md`; record uncertain category candidates instead of silently inventing new taxonomy branches. Record meaningful uncertainty in the source page instead of forcing the user to specify everything upfront. Ask for clarification only when ambiguity blocks safe ingestion, such as unclear sensitivity for private material, unclear bundle boundaries, conflicting source roles, or a taxonomy decision that would create a new top-level branch.

## Ingestion mode inference

Before creating wiki pages, infer the ingestion mode from the provided file or files:

- Treat a single file as a single-source ingestion unless its content clearly refers to required supplementary material that has also been provided.
- Treat multiple files as a source bundle when user wording, filenames, document titles, cross-references, or folder organization indicate that the files must be understood together.
- Infer bundle roles such as `main`, `supplement`, `appendix`, `data`, `code`, or `notes` when practical.
- Detect source type, including math-heavy, code-heavy, admin/personal, project-design, scientific paper, review, or ordinary prose.
- Select applicable guidance from this skill, including math-heavy source ingestion, source bundle guidance, sensitive material handling, and source-specific retrieval QA.
- If the source appears math-heavy, automatically apply the math-heavy source ingestion workflow.
- If a folder is supplied as one source bundle, inspect the folder enough to identify likely source files and exclude obvious generated files, dependency folders, caches, and local environment artifacts unless the user explicitly asks to ingest them.

## Source import workflow

Use this workflow when a source is provided from any local path, not only from `raw/sources/`. User-provided title, slug, source type, and metadata are optional; infer them where practical and record uncertainty when inference is weak:

1. If the source is outside `raw/sources/`, copy it into `raw/sources/` before ingestion.
2. Assign the next available source ID using the pattern `SRC-XXXX`.
3. Preserve the original file extension.
4. Normalize the imported filename as `SRC-XXXX-short-slug.ext`.
5. Choose the slug using this priority: explicit `--slug`; explicit `--title`; inferred document title or first clear heading; first meaningful content line; original filename stem.
6. Keep the slug lowercase, ASCII where practical, hyphen-separated, and short.
7. Do not modify the original file.
8. Do not modify the imported raw source after copying.
9. Record the original filename, imported path, source ID, and hash where practical. Do not expose machine-specific absolute local paths in public wiki metadata.
10. Then continue with the normal one-source ingestion workflow.

For simple imports, use `python3 tools/import_source.py /path/to/source.ext`, pass `--title` or `--slug` when a better name is known, or preview with `python3 tools/import_source.py --dry-run /path/to/source.ext`.

## Single-source ingestion

1. Place or import exactly one requested source into `raw/sources/`.
2. Apply the source import workflow if the source is not already normalized in `raw/sources/`.
3. Create or update the source summary page and relevant concept, entity, claim, tension, or question pages.
4. Give the source page a human-readable H1, `display_title`, `short_title`, aliases, and a visible `Source ID: SRC-XXXX` line near the top.
5. Add a `## Raw source` section with the repository path and local relative link when the raw source exists; record a gap if it is missing.
6. Run source-specific retrieval QA and record the checked questions, coverage decision, and known gaps in the source page.
7. Apply the ingestion completion contract before reporting the ingestion as complete.
8. Review new or changed wiki pages.
9. If the source is math-heavy, confirm the equation inventory, proof map, implementation notes, and mathematical gaps before marking the source complete.
10. Run `python3 tools/validate_wiki.py`.

Do not perform a broad refactor during ingestion unless requested.

## Structured bibliographic metadata

During future source ingestion, extract structured bibliographic metadata when it is available from document metadata, the first page, or obvious citation information:

```yaml
authors: []
author_entities: []
year:
venue:
doi:
arxiv:
metadata_review_status: unchecked | partial | reviewed | not-applicable
cites_sources: []
citation_match_status: unchecked | partial | reviewed
cqt_review_status: unchecked | none-needed | source-local | linked
```

Use `authors` for literal author names from the source. Extract author names, year, venue, DOI, and arXiv ID only when they are visible or reliably present in source metadata. Do not guess author names. If a field is uncertain, leave it empty or record the uncertainty under `## Metadata notes`.

Use `author_entities` only when an optional durable author entity page exists under `wiki/entities/authors/`. Create author entity pages when an author appears in multiple ingested sources or is especially relevant; do not create one author page for every one-off paper author by default. Do not use ordinary `tags` for author names unless the tag already has a non-person semantic meaning.

Set `metadata_review_status` during ingestion. Use `reviewed` when bibliographic metadata has been checked, `partial` when only some metadata was checked, `unchecked` when it was not reviewed, and `not-applicable` only for non-paper, admin, or project-design sources where paper-style authorship/year metadata would be misleading.

## Citation matching

During future ingestion, inspect the bibliography or references section enough to identify whether the source cites already-ingested sources. This is a conservative review aid, not a mandate to fully extract every reference.

Use source-page metadata from existing ingested sources when matching:

- DOI or arXiv exact match: strong.
- Exact title match: strong.
- Title plus first author plus year: strong.
- Fuzzy title only: candidate, not confirmed.
- Author/year only: candidate, not confirmed.

Do not invent citation links. When a match is manually accepted, add it to the citing source:

```yaml
cites_sources:
  - SRC-XXXX
citation_match_status: partial
```

Use `citation_match_status: reviewed` only when the source's references were inspected thoroughly. Leave `citation_match_status: unchecked` or absent when references have not been inspected. Do not add `cited_by_sources` to source frontmatter; reverse citation links are generated information.

The helper `python3 tools/match_cited_sources.py` reports conservative candidate matches from explicit source-page reference sections and never modifies source pages automatically.

## Claim, question, and tension extraction

During future source ingestion, extract first-class claim, question, and tension pages only when they improve durable retrieval.

For sources with reusable claims, create about 3-7 central claim pages when appropriate. Do not create claim pages for every source-page bullet point. Use dedicated claim pages when the claim is:

- central to the source;
- likely to be reused;
- debatable;
- comparative;
- validation-relevant;
- connected to multiple sources;
- important for future reasoning.

Otherwise keep the claim local to the source page.

Create about 1-3 question pages when the source raises open questions, validation boundaries, unresolved assumptions, or future-work questions that should be reusable. Existing question pages may be updated and linked instead of creating duplicates.

Create tension pages only when there is a real contradiction, limitation, unresolved conflict, incompatible assumption, or disagreement with existing wiki content. Do not turn every caveat into a tension page.

Set `cqt_review_status` during ingestion:

- `unchecked` before claim, question, and tension extraction has been reviewed.
- `none-needed` when no first-class semantic object would add durable retrieval value.
- `source-local` when source-page notes are enough.
- `linked` when one or more first-class claim, question, or tension pages are linked or cite the source.

Do not force claim, question, or tension pages when they would add noise.

Use stable IDs for new pages:

```text
wiki/claims/CLM-XXXX-short-slug.md
wiki/questions/QST-XXXX-short-slug.md
wiki/tensions/TEN-XXXX-short-slug.md
```

Source pages may include compact link sections when dedicated pages exist:

```md
## Claims

- [[wiki/claims/CLM-0001-example-claim]]

## Questions

- [[wiki/questions/QST-0001-example-question]]

## Tensions

- [[wiki/tensions/TEN-0001-example-tension]]
```

## Source bundles

A source bundle is allowed when the user provides a main document plus supplementary material, appendices, data, code, notes, or a folder of related files that must be understood together. The user does not need to provide detailed bundle metadata; infer bundle membership and roles where practical.

For source bundles:

- Import each physical source file as its own `SRC-XXXX`.
- Infer a stable `source_bundle` slug from the main title, folder name, or user wording.
- Infer `bundle_role` values such as `main`, `supplement`, `appendix`, `data`, `code`, or `notes` from filenames, headings, metadata, and cross-references.
- Link the sources using shared metadata such as:

```yaml
source_bundle: times-square-sampling-2024
bundle_role: main | supplement | appendix | data | code | notes
```

- Judge ingestion completion on the combined bundle, while still giving each physical file its own source page.
- The main source page should link to supplement, appendix, data, code, or notes source pages.
- Non-main source pages should link back to the main source page when one can be inferred.
- Record inferred metadata and uncertainty in the source pages, especially when bundle boundaries or roles are inferred rather than explicit.
- Ask for clarification only when ambiguity blocks safe ingestion, such as when a folder contains unrelated documents or when it is unclear which files should be treated as source material.
- Record bundle-level known gaps on the main source page when any bundled file is not fully represented.

## Math-heavy source ingestion

Automatically use this workflow for sources containing substantial equations, derivations, proofs, algorithms, mathematical definitions, theorem statements, or implementation recursions. Math-heavy ingestion does not require full proof reproduction unless explicitly requested, but it must preserve enough mathematical structure for future retrieval and implementation-oriented review.

For math-heavy sources, ingestion must include:

- Central definitions.
- Central equations.
- Algorithmic recursions.
- Theorem or proposition statements when important.
- A proof map for long proofs.
- Implementation-relevant formulas.
- Variable definitions.
- Equation dependencies.
- Known omissions.

Use `coverage_profile: math-standard` when the wiki captures the main mathematical structure well enough for retrieval and orientation. Use `coverage_profile: math-deep` when the wiki is detailed enough for close technical use, including important dependencies between equations and implementation-relevant formulas.

## Obsidian math formatting

Mathematical wiki content must use Obsidian-compatible Markdown math:

- Use inline math with single dollar delimiters, for example `$F_k = -\log Z_k$`.
- Use display math with double dollar delimiters:

```md
$$
\rho_\lambda(x) = \frac{e^{-H_\lambda(x)}}{Z_\lambda}
$$
```

- Prefer `$$ ... $$` display blocks over `\[ ... \]` for this wiki.
- Put display math on its own lines, with a blank line before and after when practical.
- Do not put important equations inside code fences.
- Do not store equations only as screenshots or images if they can be represented in LaTeX.
- Use standard LaTeX math syntax supported by MathJax and Obsidian where practical.
- Avoid full LaTeX document constructs such as `\documentclass`, `\usepackage`, `\begin{document}`, and custom preamble-dependent macros.
- Avoid relying on automatic equation numbering, `\label`, or `\ref`. Instead, identify equations in surrounding Markdown text.
- For multi-line equations, use environments inside display math:

```md
$$
\begin{aligned}
Z_k &= e^{-F_k}, \\
\xi_{km} &= e^{-F_k}\mu_{km}.
\end{aligned}
$$
```

- For equation inventories, keep very long formulas out of Markdown tables. Put the equation in a normal display block and let the table link to the section containing it.
- Define symbols in a `Variable glossary` section.
- If a formula cannot be reliably reconstructed from the PDF, do not guess. Mark it under `## Mathematical gaps`.

## Equation inventory

For math-heavy sources, the source page should include an equation inventory table with columns like:

```md
| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |
```

Each inventory row should cite the source ID and source equation number, section, page, or local label when available. If an important equation is omitted from the wiki, list it under `## Mathematical gaps` and explain why it is omitted.

## Source-specific retrieval QA

During ingestion, generate 5-10 likely retrieval questions from the source itself and check whether the wiki can answer them using the source page and relevant concept, entity, claim, tension, and question pages. The questions should match the source type and should test retrieval of the source's central contribution, practical implications, evidence, limitations, and unresolved issues.

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

## Ingestion completion contract

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

For math-heavy sources, `ingestion_status: complete` also requires that key equations are present in wiki pages using Markdown/LaTeX math, equations have source IDs and source equation numbers where available, variables are explained, implementation-relevant formulas are represented, long proofs are summarized as proof maps, and mathematical gaps are explicitly listed.

If any item is missing, mark the source page with `ingestion_status: partial` or `ingestion_status: needs-review`, document the gap under `## Ingestion QA`, and do not report the ingestion as complete.

## Sensitive material handling

- Do not store credentials, passwords, private keys, API tokens, recovery codes, or secrets in the repo.
- Encrypted sources may have safe plaintext index pages or redacted summaries.
- Decrypted copies should not be committed.
- Codex should not attempt to decrypt files unless explicitly instructed and the decrypted material is locally available.
- Sensitive filenames should be generic when possible.
- If encrypted material is unavailable, mark related claims as inaccessible or pending review instead of guessing.
- Keep the encryption design tool-agnostic unless implementation is explicitly requested.
