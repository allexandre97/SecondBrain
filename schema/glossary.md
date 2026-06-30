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
- **Coverage profile**: Source-page frontmatter that records how deeply the wiki represents a source. `minimal` means enough for indexing and later rediscovery, but not enough for full retrieval. `standard` means enough to answer the main future questions about the source. `deep` means detailed enough for close technical use. `math-standard` means the main mathematical structure is captured for retrieval and orientation. `math-deep` means the mathematical structure is detailed enough for close technical use, including equation dependencies and implementation-relevant formulas. The default is `standard`.
- **Source-specific retrieval QA**: The ingestion-time check where Codex derives likely future retrieval questions from the source type and verifies that the source page and related wiki pages can answer them.
- **Ingestion completion contract**: The checklist that must pass before an ingestion is reported complete, including stable source ID, source metadata, broad source coverage, concept extraction, limitations and open questions, index and log updates, validator success, and source-specific retrieval QA.
- **Math-heavy source**: A source containing substantial equations, derivations, proofs, algorithms, or implementation recursions whose important mathematical structure must be represented in the wiki.
- **Obsidian-compatible math**: Markdown math written in syntax that Obsidian can render through MathJax, using `$...$` for inline math and `$$...$$` display blocks for standalone equations.
- **Inline math**: A short mathematical expression embedded in prose with single dollar delimiters, such as `$F_k = -\log Z_k$`.
- **Display math**: A standalone mathematical expression or aligned equation block written between double dollar delimiters on their own lines.
- **Equation label in Markdown**: Plain surrounding Markdown text that identifies an equation by name, source ID, and source equation number or section instead of relying on LaTeX `\label` and `\ref`.
- **Equation inventory**: A source-page table that records important equations, their source locations, wiki locations, purpose, variables, and implementation relevance.
- **Variable glossary**: A section that defines the symbols used in equations, including indices, parameters, estimated quantities, source-specific notation, and units where relevant.
- **Proof map**: A concise outline of a long proof's structure, key lemmas or propositions, dependencies, and conclusion without reproducing the full proof.
- **Source bundle**: A set of physical source files, such as a main paper and supplement, that must be understood together for ingestion completion.
- **Bundle role**: Source-page metadata indicating whether a file is the `main` source or a `supplement` within a source bundle.
- **Mathematical gap**: An explicitly listed omission, uncertainty, or underrepresented equation, proof step, variable definition, dependency, or implementation detail in a math-heavy source ingestion.
