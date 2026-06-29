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

## Source Page

```md
---
type: source
status: active
created: YYYY-MM-DD
updated: YYYY-MM-DD
source_id: SRC-0000
source_path: raw/sources/example.md
areas: []
categories: []
tags: []
related: []
sources:
  - SRC-0000
sensitivity: public
encryption: none
---

# SRC-0000: Source Title

## Summary

## Key Points

## Links

## Open Questions
```
