---
type: concept
status: active
created: 2026-06-29
updated: 2026-06-29
areas:
  - admin
categories:
  - admin/privacy
  - research/llm-wiki/privacy
tags:
  - privacy
  - metadata
related:
  - "[[concepts/wiki-page-metadata]]"
sources:
  - SRC-0002
sensitivity: public
encryption: none
---

# Optional Encryption and Sensitivity Metadata

## Summary

The repository should support selective privacy controls without making encryption mandatory for the whole wiki. [SRC-0002]

## Key Points

- Sensitivity values describe whether material is `public`, `internal`, `private`, or `restricted`. [SRC-0002]
- Encryption values describe whether encryption is `none`, `optional`, or `required`. [SRC-0002]
- Credentials, passwords, private keys, API tokens, recovery codes, and secrets should not be stored in the repo, even encrypted. [SRC-0002]
- Encrypted sources may have safe plaintext index pages or redacted summaries, but decrypted copies should not be committed. [SRC-0002]
- Codex should not attempt to decrypt files unless explicitly instructed and the decrypted material is locally available. [SRC-0002]

## Links

- [[sources/SRC-0002-project-design-note]]
- [[concepts/wiki-page-metadata]]
