# Page Templates

Use these starter patterns when adding new wiki pages. Include only fields that are relevant, but prefer stable metadata so pages can be searched, reviewed, and reorganized without moving files.

## Standard Frontmatter

```yaml
---
type: concept | entity | source | claim | tension | question | answer | overview | category
status: seed | active | needs-review | deprecated
created: YYYY-MM-DD
updated: YYYY-MM-DD
areas: []
categories: []
tags: []
related: []
sources: []
sensitivity: public
encryption: none
graph_exclude: true | false
---
```

Use `graph_exclude: true` for navigation-heavy pages that should be filterable out of Obsidian Graph view, including dashboards, most README index pages, `wiki/index.md`, and `wiki/log.md`. Category pages under `wiki/categories/` should use `graph_exclude: false` so they can act as useful grouping nodes in Obsidian Graph view. Omit the field or use `false` for normal content pages.

Source pages should also include:

```yaml
ingestion_status: complete | partial | needs-review
coverage_profile: minimal | standard | deep | math-standard | math-deep
source_bundle: optional-bundle-slug
bundle_role: main | supplement
authors: []
author_entities: []
year:
venue:
doi:
arxiv:
metadata_review_status: unchecked | partial | reviewed | not-applicable
citation_match_status: unchecked | partial | reviewed
cqt_review_status: unchecked | none-needed | source-local | linked
```

For source pages, `coverage_profile` defaults to `standard` unless there is a reason to choose `minimal`, `deep`, `math-standard`, or `math-deep`.

Use `authors` for literal author names from the source. Use `author_entities` only for optional durable author entity pages. Do not store author names only as ordinary tags.

Use `metadata_review_status` to distinguish missing bibliographic review from sources where bibliographic paper metadata does not apply. Use `reviewed` when the page has been checked even if `authors` or `year` are unavailable from the source. Use `not-applicable` only for non-paper, admin, or project-design sources where paper-style authorship/year metadata would be misleading.

Use `cqt_review_status` to distinguish unreviewed source pages from reviewed pages where first-class claim, question, or tension pages are unnecessary. Use `none-needed` when the source was reviewed and no durable semantic object is warranted, `source-local` when source-page notes are sufficient, and `linked` when first-class claim, question, or tension pages are linked.

## Concept Page

```md
---
type: concept
status: active
created: YYYY-MM-DD
updated: YYYY-MM-DD
areas:
  - research
categories:
  - research/example-topic
tags:
  - concept
related:
  - "[[wiki/concepts/related-page]]"
sources:
  - SRC-0000
sensitivity: public
encryption: none
---

# Example Concept

## Summary

## Key Points

## Evidence

## Links

## Open Questions

```

Mathematically important concept pages may also include:

```md
## Core equations

**Equation name, source Eq. (...) [SRC-XXXX]:**

$$
...
$$

## Variable glossary

## Derivation sketch

## Implementation consequences

## Caveats
```

## Source Page

```md
---
type: source
status: active
created: YYYY-MM-DD
updated: YYYY-MM-DD
source_id: SRC-0000
display_title: "Source Title"
short_title: "Short Source Title"
aliases:
  - "SRC-0000"
  - "Short Source Title"
  - "Source Title"
source_path: raw/sources/SRC-0000-example.md
imported_path: raw/sources/SRC-0000-example.md
original_filename: "SRC-0000-example.md"
original_path_note: "Original local path omitted from wiki metadata."
sha256: optional-sha256-when-available
authors: []
author_entities: []
year:
venue:
doi:
arxiv:
metadata_review_status: unchecked | partial | reviewed | not-applicable
areas: []
categories: []
tags: []
related:
  - "[[wiki/concepts/related-page]]"
  - "[[wiki/sources/SRC-0000-example]]"
sources:
  - SRC-0000
cites_sources: []
citation_match_status: unchecked | partial | reviewed
cqt_review_status: unchecked | none-needed | source-local | linked
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: standard
source_bundle: optional-bundle-slug
bundle_role: main
---

# Source Title

Source ID: `SRC-0000`

## Raw source

- Repository path: `raw/sources/SRC-0000-example.md`
- Open raw source: [raw/sources/SRC-0000-example.md](../../raw/sources/SRC-0000-example.md)

## Summary

## Key Points

## Links

## Open Questions

## Metadata notes

## Citation links

- Confirmed cited ingested sources belong in frontmatter `cites_sources`.
- Use `citation_match_status: partial` when some references were inspected and accepted citation links were added.
- Use `citation_match_status: reviewed` only when the source's references were inspected thoroughly.
- Do not add `cited_by_sources`; reverse citation links are generated information.

## Semantic-object review

- Use `cqt_review_status: unchecked` before source-local claims, questions, and tensions have been reviewed for durable extraction.
- Use `cqt_review_status: none-needed` when no first-class claim, question, or tension page would add useful retrieval value.
- Use `cqt_review_status: source-local` when the useful claim, question, or tension material is intentionally kept on the source page.
- Use `cqt_review_status: linked` when dedicated claim, question, or tension pages are linked from the source page or cite this source in frontmatter.
- Do not create first-class claim, question, or tension pages mechanically.

## Mathematical structure

## Key equations

## Equation inventory

| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |

## Algorithmic recursions

## Proof map

## Implementation notes

## Mathematical gaps

## Ingestion QA

### Retrieval questions checked

### Coverage decision

### Known gaps
```

## Answer Page

```md
---
type: answer
status: active
created: YYYY-MM-DD
updated: YYYY-MM-DD
question: ""
answer_status: answered | partially-answered | needs-review
areas: []
categories: []
tags: []
related: []
sources: []
sensitivity: public
encryption: none
wiki_pages_used: []
raw_sources_consulted: []
wiki_pages_updated: []
---

# Question

## Short answer

## Detailed answer

## Key equations

## Sources used

## Wiki pages used

## Wiki updates made

## Remaining gaps
```

## Claim Page

Name claim pages with stable IDs:

```text
wiki/claims/CLM-XXXX-short-slug.md
```

Create dedicated claim pages only when a claim is central, reusable, debatable, comparative, validation-relevant, connected to multiple sources, or important for future reasoning. Keep ordinary source-local statements on the source or concept page.

```md
---
type: claim
status: active
created: YYYY-MM-DD
updated: YYYY-MM-DD
claim_status: supported | contested | limited | needs-review
claim_scope: local | cross-source
areas: []
categories: []
tags:
  - claim
related: []
sources:
  - SRC-0000
sensitivity: public
encryption: none
---

# Claim Short Title

## Claim

State the claim in one concise sentence. [SRC-0000]

## Scope

State whether this is local to one source or cross-source, and what conditions limit the claim.

## Evidence

- Supporting evidence with local citations. [SRC-0000]

## Caveats

- Validation boundaries, assumptions, or reasons not to overgeneralize. [SRC-0000]

## Links

```

## Question Page

Name new question pages with stable IDs:

```text
wiki/questions/QST-XXXX-short-slug.md
```

Do not rename existing question pages solely to match this convention; use stable IDs for new question pages.

```md
---
type: question
status: active
created: YYYY-MM-DD
updated: YYYY-MM-DD
question_status: open | partially-answered | answered | needs-review
areas: []
categories: []
tags:
  - question
related: []
sources:
  - SRC-0000
sensitivity: public
encryption: none
---

# Question Short Title

## Question

State the open question or validation boundary. [SRC-0000]

## Context

Explain why the question remains open and what source evidence motivates it. [SRC-0000]

## Current Position

Summarize what the wiki can currently say without resolving beyond the sources.

## Links

```

## Tension Page

Name tension pages with stable IDs:

```text
wiki/tensions/TEN-XXXX-short-slug.md
```

Create tension pages only for real contradictions, limitations, unresolved conflicts, incompatible assumptions, or important validation tradeoffs.

```md
---
type: tension
status: active
created: YYYY-MM-DD
updated: YYYY-MM-DD
tension_status: active | resolved | needs-review
areas: []
categories: []
tags:
  - tension
related: []
related_claims: []
related_questions: []
sources:
  - SRC-0000
sensitivity: public
encryption: none
---

# Tension Short Title

## Tension

State the conflict, limitation, or unresolved tradeoff. [SRC-0000]

## Positions

- Source or page position with citation. [SRC-0000]
- Competing source or limiting position with citation. [SRC-0000]

## Why it matters

Explain why future retrieval or reasoning should preserve this tension.

## Resolution status

State whether the tension is active, resolved, or needs review.

## Links

```

## Source Page Claim / Question / Tension Links

Source pages may include compact link sections when dedicated pages exist:

```md
## Claims

- [[wiki/claims/CLM-0001-example-claim]]

## Questions

- [[wiki/questions/QST-0001-example-question]]

## Tensions

- [[wiki/tensions/TEN-0001-example-tension]]
```

## Author Entity Convention

Author entity pages are optional. Create them when an author appears in multiple ingested sources or is especially relevant to the wiki. Do not create an author page for every one-off author by default. Source pages may list authors in frontmatter without corresponding author entity pages.

Author entity pages live under:

```text
wiki/entities/authors/author-name.md
```

Use this frontmatter:

```md
---
type: entity
status: active
created: YYYY-MM-DD
updated: YYYY-MM-DD
entity_type: author
aliases: []
areas: []
categories: []
tags:
  - author
related: []
sources: []
sensitivity: public
encryption: none
graph_exclude: false
---

# Author Name

## Summary

## Sources

## Links
```
