# Category Registry

This registry documents the category roots and category paths currently used in the wiki. It is intentionally small: prefer reusing an existing path before adding a new branch.

## Allowed top-level roots

- `admin` - wiki governance, maintenance, privacy, and repository operating notes.
- `research` - source-derived scientific and technical knowledge.

## Existing category hierarchy

- `admin/privacy`
- `admin/wiki-governance`
- `admin/wiki-maintenance`
- `research/adaptive-sampling`
- `research/bioimage-analysis/cytoskeleton`
- `research/biomolecules/rna`
- `research/computational-drug-discovery`
- `research/computer-vision/biomedical-imaging`
- `research/data-management`
- `research/free-energy`
- `research/high-performance-computing`
- `research/llm-wiki/architecture`
- `research/llm-wiki/design`
- `research/llm-wiki/metadata`
- `research/llm-wiki/navigation`
- `research/llm-wiki/organization`
- `research/llm-wiki/privacy`
- `research/llm-wiki/tooling`
- `research/llm-wiki/workflows`
- `research/machine-learning/scientific-modeling`
- `research/machine-learning/statistical-modeling`
- `research/molecular-simulation/binding-free-energy`
- `research/molecular-simulation/datasets`
- `research/molecular-simulation/force-fields`
- `research/molecular-simulation/free-energy`
- `research/molecular-simulation/molecular-dynamics`
- `research/scientific-computing`
- `research/statistics/monte-carlo`

## Naming rules

- Use lowercase path segments separated by `/`.
- Use hyphens inside a segment, not spaces or underscores.
- Keep category paths broad enough to collect multiple pages.
- Do not encode source IDs, dates, authors, or one-off paper titles in category names.
- Prefer existing branches unless a page clearly needs a reusable new browsing path.

## Alias and synonym guidance

Record common synonyms in page `tags`, `aliases`, or prose instead of creating parallel category paths. For example, prefer one category path for a topic and use tags for narrower terms, acronyms, method names, or spelling variants.

## Uncertain candidates

If a candidate category is plausible but not clearly reusable, do not silently invent a new branch. Record the uncertainty in the page notes, leave the page on the closest existing category, and revisit the registry during a maintenance pass.

## Generated indexes

Category index pages under `wiki/categories/` are generated from page frontmatter with:

```sh
python3 tools/build_category_indexes.py
```

Audit category usage with:

```sh
python3 tools/audit_categories.py
```
