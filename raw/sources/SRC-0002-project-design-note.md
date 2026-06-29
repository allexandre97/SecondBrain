# Project design note

This repository is intended to be a local-first LLM knowledge base for both work-related and personal information.

The main workflow is:

* raw sources are stored in `raw/sources/`
* raw sources are treated as immutable records
* Codex ingests sources one at a time
* synthesized knowledge lives in `wiki/`
* Obsidian is used as a human browsing/editing interface
* chat agents should retrieve relevant wiki pages before answering project-specific questions
* useful chat-derived synthesis should be written back into the wiki when appropriate

The repo should initially avoid (although these may be required later):

* vector databases
* embedding pipelines
* web apps
* complex external dependencies
* Obsidian plugins
* MCP servers
* opaque compression schemes
* mandatory encryption systems that make the basic wiki hard to inspect or maintain

The system should support multi-category organization.

Pages should not belong to only one folder-based category. Instead, wiki pages should use metadata fields such as:

```yaml id="wi9z9y"
areas:
  - personal
  - work

categories:
  - personal/travel/vacation-planning
  - work/absence

tags:
  - planning
  - calendar

related:
  - "[[concepts/annual-leave]]"
```

Use `areas` for broad top-level contexts such as:

* work
* personal
* research
* admin
* finance

Use `categories` for hierarchical multi-label organization.

Use `tags` for looser descriptors.

Use `related` for explicit links to connected pages.

Category pages, if present, should be navigational indexes. The source of truth for category membership should be page frontmatter.

When ingesting a new source, codex should suggest categories (or tags or related) for it. Currently existing categories should be prioritised, and if none is fitting, suggest new ones. If the user wants to assign a category to a source, codex should check if that category exist or if something equivalent is already present.

The system should support optional encryption for sensitive material.

Encryption should be selective, not mandatory for the whole repository. The default mode should remain plain markdown so the wiki stays searchable, reviewable in Git, usable from Obsidian, and readable by Codex.

Sensitive material should be classified with frontmatter metadata such as:

```yaml id="h2wwug"
sensitivity: public | internal | private | restricted
encryption: none | optional | required
```

Suggested meanings:

* `public`: safe to store as normal plaintext.
* `internal`: not public, but acceptable as plaintext in the private repo.
* `private`: personal or sensitive information; summarize carefully.
* `restricted`: should not be stored in plaintext unless explicitly justified.

Encryption expectations:

* raw sensitive sources may be stored as encrypted files
* encrypted files may have safe plaintext index pages or redacted summaries
* decrypted copies should not be committed
* credentials, passwords, private keys, API tokens, and recovery codes should not be stored in the repo, even encrypted
* filenames and metadata may still leak information, so sensitive filenames should be generic
* Codex should not attempt to decrypt files unless explicitly instructed and the decrypted material is available locally
* if a source is encrypted and unavailable, wiki pages should mark the relevant claims as inaccessible or pending review
* encryption choices should be documented before implementation

The initial encryption design should stay tool-agnostic. Possible future tools can be evaluated later, but the schema should not depend on a specific encryption backend yet.

Compression should be achieved through:

* short pages
* stable source IDs
* claim IDs where useful
* compact summaries
* tables
* explicit abbreviations in `schema/glossary.md`

Compression should not rely on unexplained shorthand, private codes, or cryptic notation that would make the wiki hard to search, review, or maintain.

The system should optimize for:

* traceability
* low token use
* easy review in Git
* compatibility with Codex
* compatibility with Obsidian
* incremental growth
* multi-context retrieval
* durable memory across projects
* selective privacy controls

Privacy and safety expectations:

* the repository may contain personal and work-related information
* the repo should not store passwords, API keys, private tokens, recovery codes, or credentials
* sensitive information should be summarized only when useful
* raw source files should not be modified during ingestion
* provenance should be preserved so synthesized claims can be traced back to sources
* sensitive sources should have clear sensitivity metadata
* plaintext wiki pages derived from sensitive sources should avoid unnecessary personal details

Codex interaction expectations:

* recurring task constraints should live in `AGENTS.md` and `schema/workflows.md`, not in every prompt
* common report formats should be defined once and reused
* Codex tasks should remain focused and contained
* Codex should run validation before reporting completion
* Codex should preserve sensitivity and encryption metadata when editing pages
