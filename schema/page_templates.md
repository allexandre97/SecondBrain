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
---
```

Source pages should also include:

```yaml
ingestion_status: complete | partial | needs-review
coverage_profile: minimal | standard | deep | math-standard | math-deep
source_bundle: optional-bundle-slug
bundle_role: main | supplement
```

For source pages, `coverage_profile` defaults to `standard` unless there is a reason to choose `minimal`, `deep`, `math-standard`, or `math-deep`.

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
  - "[[concepts/related-page]]"
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
source_path: raw/sources/example.md
imported_path: raw/sources/example.md
original_filename: "example.md"
original_path_note: "Original local path omitted from wiki metadata."
sha256: optional-sha256-when-available
areas: []
categories: []
tags: []
related: []
sources:
  - SRC-0000
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

- Repository path: `raw/sources/example.md`
- Local relative link: [Open raw source](../../raw/sources/example.md)

## Summary

## Key Points

## Links

## Open Questions

## Metadata notes

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
