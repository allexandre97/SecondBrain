---

name: wiki-source-ingestion
description: Import and ingest source files into the SecondBrain wiki, including source bundles, scientific and math-heavy material, provenance, retrieval QA, and ingestion validation.
---

# Wiki Source Ingestion

Use this skill for requests such as:

* `Ingest /path/to/source.pdf`
* ingesting a paper and its supporting material;
* ingesting a folder as one source bundle;
* importing external source material into SecondBrain;
* math-heavy source ingestion;
* source-specific retrieval QA.

# Core contract

Apply the repository's `Default Wiki Task Contract` and `Default Report Format` from `schema/workflows.md`.

Do not ingest sources the user did not request.

Do not modify existing files in `raw/` except when explicitly instructed. Requested external source files may be copied into `raw/sources/` as part of ingestion.

Preserve:

* provenance;
* sensitivity and encryption metadata;
* uncertainty;
* contradictions;
* limitations;
* open questions.

Every non-trivial wiki claim must be traceable to one or more stable source IDs.

Do not guess content that cannot be reliably extracted from a source.

Run the required repository validation before reporting completion.

# Workflow ownership

For a delegated ingestion task, own the complete ingestion workflow:

1. understand the requested source or source bundle;
2. inspect only the existing wiki context needed for integration;
3. import and identify the source files;
4. analyse the source material;
5. update the wiki;
6. perform retrieval QA;
7. run validation and generated-index tools required by the repository;
8. report the result and any remaining gaps.

Avoid redundant full-source passes.

Reuse information already extracted during the current ingestion. Re-open source sections only when needed to verify a claim, equation, metadata field, citation, discrepancy, or gap.

Do not spawn additional agents.

# Minimal prompts and inference

Detailed metadata is optional.

Accept minimal requests such as:

```text
Ingest /path/to/source.pdf
```

```text
Ingest these as one source bundle:
Main paper: /path/to/paper.pdf
Supplement: /path/to/supplement.pdf
```

```text
Ingest /path/to/project_docs/ as one source bundle.
```

Infer metadata where practical from:

* user wording;
* filenames;
* document metadata;
* titles and headings;
* source content;
* cross-references;
* repository context.

Infer, where possible:

* title;
* slug;
* source type;
* bundle membership and role;
* areas and categories;
* sensitivity;
* encryption status;
* coverage profile.

Prefer existing category paths from `schema/category_registry.md`.

Record meaningful uncertainty rather than forcing a confident classification.

Ask for clarification only when ambiguity prevents safe ingestion, for example:

* unclear sensitivity of private material;
* uncertain bundle boundaries;
* conflicting source roles;
* a taxonomy decision requiring a new top-level branch.

# Determine ingestion mode

Before writing wiki content, determine whether the request is:

* a single source;
* a source bundle;
* a folder bundle;
* math-heavy;
* code-heavy;
* scientific;
* review material;
* project/design documentation;
* administrative or personal material.

Treat multiple files as a bundle when they are intended to be understood together.

For a folder, inspect enough of its contents to identify likely source files and exclude obvious:

* generated output;
* caches;
* dependency trees;
* virtual environments;
* build artifacts;

unless explicitly requested.

# Source import

For each physical source file:

1. Copy it into `raw/sources/` if it is not already there.

2. Assign the next available `SRC-XXXX` identifier.

3. Preserve the original extension.

4. Normalize the repository filename to:

   `SRC-XXXX-short-slug.ext`

5. Choose the slug from, in order of preference:

   * explicit user title or slug;
   * document title;
   * clear first heading;
   * meaningful first content line;
   * original filename stem.

6. Keep the slug concise, lowercase, ASCII where practical, and hyphen-separated.

7. Do not modify the original external file.

8. Do not modify the imported raw source after copying.

9. Record the original filename, source ID, imported path, and hash where practical.

10. Do not expose unnecessary machine-specific absolute paths in public wiki metadata.

Use `tools/import_source.py` when appropriate rather than manually reproducing its behavior.

# Source bundles

When a main document has supporting material, appendices, data, code, or notes that must be interpreted together, ingest them as one source bundle.

Each physical file receives its own `SRC-XXXX` identifier and source page.

Use shared metadata such as:

```yaml
source_bundle: stable-bundle-slug
bundle_role: main
```

Typical roles include:

* `main`
* `supplement`
* `appendix`
* `data`
* `code`
* `notes`

The main source page should link to related bundle members.

Non-main source pages should link back to the main source when one can be identified.

Judge overall coverage across the complete bundle, not the main document alone.

Do not repeatedly reread both files in full merely because they form a bundle. Use cross-references and targeted source reads once the structure is understood.

# Source page

Each source should have a source page under `wiki/sources/`.

Include:

* human-readable H1;
* stable source ID;
* `display_title`;
* `short_title`;
* useful aliases;
* source type;
* sensitivity and encryption metadata;
* areas, categories, and tags;
* imported raw-source link;
* bibliographic metadata where applicable;
* summary;
* methods or approach;
* central results or claims;
* limitations and caveats;
* important open questions;
* relevant concepts and entities;
* bundle relationships where applicable;
* ingestion QA;
* known gaps.

Keep source pages useful for future retrieval rather than reproducing the source verbatim.

# Bibliographic metadata

For papers and similar sources, extract metadata when clearly available:

```yaml
authors: []
author_entities: []
year:
venue:
doi:
arxiv:
metadata_review_status: unchecked
cites_sources: []
citation_match_status: unchecked
cqt_review_status: unchecked
```

Do not guess missing bibliographic fields.

Use `metadata_review_status` as follows:

* `reviewed`: metadata was checked;
* `partial`: some metadata was checked;
* `unchecked`: not reviewed;
* `not-applicable`: paper-style metadata is inappropriate.

Create durable author entity pages only when useful, for example when an author appears repeatedly or is important to the knowledge base.

# Existing-wiki integration

Before creating new concept, entity, claim, question, or tension pages, search for relevant existing pages.

Prefer updating or linking an existing durable page over creating a near-duplicate.

Do not perform broad wiki cleanup or taxonomy refactoring during ingestion unless requested.

Use the current source to enrich existing knowledge only when the source genuinely supports the addition.

# Claims, questions, and tensions

Create first-class semantic pages only when they improve future retrieval.

Create claim pages for statements that are:

* central;
* reusable;
* debatable;
* comparative;
* validation-relevant;
* connected to multiple sources;
* important for future reasoning.

Do not create a claim page for every bullet point.

Create question pages for meaningful:

* unresolved assumptions;
* future work;
* validation boundaries;
* open scientific or technical questions.

Create tension pages only for genuine:

* contradictions;
* incompatible assumptions;
* important limitations;
* disagreements between sources or existing knowledge.

Do not turn every caveat into a tension.

Use stable IDs:

```text
wiki/claims/CLM-XXXX-short-slug.md
wiki/questions/QST-XXXX-short-slug.md
wiki/tensions/TEN-XXXX-short-slug.md
```

Set `cqt_review_status` appropriately:

* `unchecked`
* `none-needed`
* `source-local`
* `linked`

# Citation matching

Inspect the source bibliography enough to detect citations to already-ingested sources when doing so is useful.

Prefer strong matches:

* DOI exact match;
* arXiv exact match;
* exact title;
* title + first author + year.

Treat fuzzy title or author/year-only matches as candidates, not confirmed links.

Do not invent citation relationships.

Use `tools/match_cited_sources.py` when appropriate.

# Scientific and math-heavy sources

Automatically apply this section when the material contains substantial:

* equations;
* derivations;
* algorithms;
* mathematical definitions;
* theorem or proposition statements;
* implementation recursions.

Capture enough mathematical structure for future retrieval and technical use.

Include, where relevant:

* central definitions;
* central equations;
* algorithmic recursions;
* important theorem or proposition statements;
* implementation-relevant formulas;
* variable definitions;
* equation dependencies;
* proof maps for long proofs;
* known mathematical omissions.

Do not reproduce long proofs unless needed.

Use:

* `coverage_profile: math-standard` when the central mathematical structure is captured adequately;
* `coverage_profile: math-deep` when the representation supports close technical or implementation-oriented use.

# Mathematical formatting

Use Obsidian-compatible Markdown math.

Inline:

```md
$F_k = -\log Z_k$
```

Display:

```md
$$
\rho_\lambda(x) = \frac{e^{-H_\lambda(x)}}{Z_\lambda}
$$
```

Do not use `\[ ... \]`.

Do not store reconstructable equations only as screenshots.

Do not guess formulas that cannot be reliably reconstructed.

Put uncertain or missing mathematical content under `## Mathematical gaps`.

Define important symbols in a variable glossary when useful.

# Equation inventory

For math-heavy material, maintain an equation inventory when it materially improves retrieval or implementation.

Recommended columns:

```md
| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |
```

Each important equation should have a traceable source location such as:

* equation number;
* page;
* section;
* local label.

If an important equation is intentionally omitted, record it under `## Mathematical gaps`.

# Source-specific retrieval QA

Before considering ingestion complete, generate a small set of likely future questions and verify that the wiki can answer them.

Usually 5–10 questions are sufficient.

For a scientific paper, cover topics such as:

* central contribution;
* problem addressed;
* methods;
* evidence or benchmarks;
* key results;
* limitations;
* validation boundaries;
* future work;
* claims that should not be overgeneralized.

For a source bundle, include questions that require information from the supporting material where relevant.

Record the checked questions under `## Ingestion QA`.

State whether coverage is:

* complete;
* partial;
* needs review.

Record known gaps explicitly.

# Review before completion

Before reporting success:

1. Review the new or modified source pages.
2. Check that central claims are traceable.
3. Check bundle relationships.
4. Check bibliographic metadata where applicable.
5. Check that important limitations and uncertainty were preserved.
6. For math-heavy material, check equations, symbols, dependencies, and mathematical gaps.
7. Run source-specific retrieval QA.
8. Run repository validation.
9. Run required generated-index or knowledge-graph builders.

# Validation

Run:

```bash
python3 tools/validate_wiki.py
python3 tools/build_category_indexes.py
python3 tools/build_concept_indexes.py
python3 tools/build_knowledge_graph.py
```

Run additional repository tools when required by the current workflow.

Do not report validation as passed if it was not run or failed.

If validation fails because of a clearly pre-existing unrelated problem, report that distinction rather than silently modifying unrelated content.

# Completion contract

An ingestion is complete only when:

* every requested physical source has a stable source ID;
* every requested source has a source page;
* imported raw sources are linked where applicable;
* source provenance is preserved;
* the major topics, methods, claims, evidence, limitations, and open questions are represented;
* important concepts are linked or represented;
* bundle relationships are recorded;
* important caveats and contradictions are preserved;
* source-specific retrieval QA was completed;
* `wiki/index.md` and `wiki/log.md` were updated as required;
* required repository validation passed.

For math-heavy material, completion also requires that important mathematical structure is represented or explicitly recorded as a gap.

If these conditions are not met, mark the ingestion:

* `partial`, or
* `needs-review`

and record the reason.

# Independent review handoff

A substantial or high-risk ingestion may be reviewed independently by the parent harness after completion.

Make that review efficient by leaving:

* clear source IDs;
* explicit known gaps;
* ingestion QA;
* equation inventories where relevant;
* concise validation results.

Do not perform a redundant second full-source review yourself unless required to resolve a specific uncertainty.

# Sensitive material

Do not store:

* credentials;
* passwords;
* private keys;
* API tokens;
* recovery codes;
* other secrets.

Do not commit decrypted copies of encrypted material.

Do not attempt to decrypt sources unless explicitly instructed and the necessary plaintext access is already available.

If protected material cannot be inspected, record the limitation instead of guessing.
