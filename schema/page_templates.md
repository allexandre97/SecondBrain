# Page Templates

Use these starter patterns when adding new wiki pages. Include only fields that are relevant, but prefer stable metadata so pages can be searched, reviewed, and reorganized without moving files.

## Standard Frontmatter

```yaml
---
type: concept | entity | source | claim | tension | question | overview | category
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
source_path: raw/sources/example.md
original_path: /original/path/or/filename.md
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

# SRC-0000: Source Title

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
