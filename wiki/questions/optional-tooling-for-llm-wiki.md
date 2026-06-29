---
type: question
status: active
created: 2026-06-29
updated: 2026-06-29
areas:
  - research
categories:
  - research/llm-wiki/tooling
tags:
  - tooling
related:
  - "[[concepts/wiki-linting]]"
sources:
  - SRC-0001
  - SRC-0002
sensitivity: public
encryption: none
---

# Optional Tooling for LLM Wiki

## Question

Which optional tools or formats from SRC-0001 and SRC-0002, if any, should this repository adopt later? [SRC-0001] [SRC-0002]

## Context

SRC-0001 mentions examples such as local search tools, Obsidian workflows, slide formats, and plugins, but presents them as optional and modular rather than required architecture. [SRC-0001]

SRC-0002 says the repository should initially avoid vector databases, embedding pipelines, web apps, complex dependencies, Obsidian plugins, MCP servers, opaque compression, and mandatory encryption systems, though some may be evaluated later. [SRC-0002]

## Current Position

No optional tooling has been adopted. Revisit this only after the wiki grows enough that the current index and validator are insufficient. [SRC-0001] [SRC-0002]

## Links

- [[sources/SRC-0001-karpathy-llm-knowledge-base]]
- [[sources/SRC-0002-project-design-note]]
- [[concepts/wiki-linting]]
