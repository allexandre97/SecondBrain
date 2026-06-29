# Glossary

Record shared terms, abbreviations, and definitions used across the wiki.

- **Area**: A broad top-level context such as `work`, `personal`, `research`, `admin`, or `finance`.
- **Category**: A hierarchical label used for organization, such as `personal/travel/vacation-planning`.
- **Tag**: A loose descriptor for search and filtering; tags are less structured than categories.
- **Related page**: An explicit wikilink in frontmatter or page content that points to a connected wiki page.
- **Multi-category page**: A page whose frontmatter lists more than one category because it belongs in multiple organizational contexts.
- **Sensitivity**: Frontmatter metadata describing how safe the page is to store or summarize, using values such as `public`, `internal`, `private`, or `restricted`.
- **Encryption**: Frontmatter metadata describing whether encryption is unnecessary, optional, or required for the source or derived material; the schema is tool-agnostic and does not implement encryption.
- **Ingestion status**: Source-page frontmatter that records whether the source representation is `complete`, `partial`, or `needs-review` under the current ingestion completion contract.
- **Coverage profile**: Source-page frontmatter that records how deeply the wiki represents a source. `minimal` means enough for indexing and later rediscovery, but not enough for full retrieval. `standard` means enough to answer the main future questions about the source. `deep` means detailed enough for close technical use. The default is `standard`.
- **Source-specific retrieval QA**: The ingestion-time check where Codex derives likely future retrieval questions from the source type and verifies that the source page and related wiki pages can answer them.
- **Ingestion completion contract**: The checklist that must pass before an ingestion is reported complete, including stable source ID, source metadata, broad source coverage, concept extraction, limitations and open questions, index and log updates, validator success, and source-specific retrieval QA.
