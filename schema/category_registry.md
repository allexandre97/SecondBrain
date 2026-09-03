# Category Registry

This registry documents the reusable category paths for the wiki. It is intentionally small: prefer assigning multiple broad facets from this list before adding a narrower one-off branch.

## Vault model

Open the repository root, not `wiki/`, as the Obsidian vault.

Repository-root vaults keep `raw/sources/`, `wiki/`, `schema/`, and `tools/` visible from one local-first workspace without duplicating source PDFs under `wiki/`.

## Allowed top-level roots

- `admin` - wiki governance, maintenance, privacy, and repository operating notes.
- `research` - source-derived scientific and technical knowledge.
- `personal` - personal-life documents, including personal finance and banking paperwork.

## Multi-facet assignment

Pages may have several categories when each facet is supported by the page itself. Prefer combining:

- domain or object facets, such as `research/biomolecules/lipids`;
- method facets, such as `research/molecular-simulation/free-energy`;
- data or benchmark facets, such as `research/experimental-benchmarking`.

Do not encode source IDs, dates, authors, or individual paper titles in category names.

## Registered categories and match terms

- `personal/finance/banking` - personal banking accounts, terms and conditions, product terms, and related banking paperwork.
  - Match terms: banking, current account, building society, Nationwide, FlexDirect, FlexPlus, FlexAccount, FlexBasic, FlexOne, overdraft, internet banking, debit card, switch service, FSCS
- `admin/privacy` - privacy, sensitivity, and encryption metadata.
  - Match terms: privacy, sensitivity, encryption, access control
- `admin/wiki-governance` - repository-wide wiki policies and operating agreements.
  - Match terms: governance, working agreement, task contract, policy
- `admin/wiki-maintenance` - validation, linting, generated indexes, and maintenance workflows.
  - Match terms: validation, linting, maintenance, generated index, category audit
- `research/adaptive-sampling` - adaptive sampling and enhanced sampling algorithms.
  - Match terms: adaptive sampling, enhanced sampling, accelerated weight histogram, AWH, OPES, metadynamics
- `research/bioimage-analysis/filament-segmentation` - microscopy filament, fiber, vessel, cytoskeleton, and tubular-structure segmentation or tracing.
  - Match terms: filament, filaments, fiber, fibers, cytoskeleton, cytoskeletal, actin, tubular, vessel, segmentation, tracing, centerline, SOAX, clDice, ToFiE
- `research/biomolecules/lipids` - lipid membranes, bilayers, and lipid-focused biomolecular datasets or force fields.
  - Match terms: lipid, lipids, membrane, bilayer, NMRlipids, cholesterol
- `research/biomolecules/proteins` - proteins, peptides, protein-ligand complexes, and protein force-field benchmarks.
  - Match terms: protein, proteins, peptide, peptides, folded protein, disordered protein, protein force field, protein-ligand
- `research/biomolecules/rna` - RNA, RNA motifs, and nucleic-acid molecular simulation.
  - Match terms: RNA, tetraloop, nucleic acid, nucleic acids
- `research/computational-drug-discovery` - host-guest, ligand, binding, and drug-like molecular modeling.
  - Match terms: ligand, drug-like, host-guest, binding affinity, binding free energy, FEP+
- `research/computer-vision/biomedical-imaging` - biomedical image analysis beyond filament-specific browsing.
  - Match terms: biomedical imaging, microscopy, image segmentation, CNN, U-Net, keypoint, vessel
- `research/data-management` - reusable datasets, databanks, overlays, and local-first data organization.
  - Match terms: dataset, datasets, databank, databanks, overlay, FAIR
- `research/experimental-benchmarking` - use of experimental observables or benchmark datasets for validation.
  - Match terms: benchmark, benchmarking, experimental dataset, experimental observable, validation dataset, reproducibility
- `research/high-performance-computing` - GPU, neighbor-list, and performance-oriented scientific computing.
  - Match terms: GPU, CUDA, neighbor list, space-filling curve, acceleration, performance
- `research/llm-wiki/architecture` - wiki architecture and repository layering.
  - Match terms: wiki architecture, raw wiki schema, repository structure
- `research/llm-wiki/design` - design of the LLM-maintained wiki workflow.
  - Match terms: LLM wiki, knowledge base, local-first, design note
- `research/llm-wiki/metadata` - page metadata, frontmatter, and source IDs.
  - Match terms: frontmatter, source_id, source ID
- `research/llm-wiki/navigation` - index, log, category, and Obsidian navigation.
  - Match terms: navigation, Obsidian, vault, wikilink, index, log
- `research/llm-wiki/organization` - multi-category organization and page placement.
  - Match terms: category, categories, organization, multi-category
- `research/llm-wiki/privacy` - optional wiki privacy and sensitivity controls.
  - Match terms: privacy, sensitivity, encryption
- `research/llm-wiki/tooling` - optional tooling around the wiki.
  - Match terms: tool, tooling, script, validator, search helper
- `research/llm-wiki/workflows` - ingestion, answer-note, maintenance, and task workflows.
  - Match terms: source ingestion, answer note, maintenance workflow
- `research/machine-learning/molecular-modeling` - ML potentials, Boltzmann generators, molecular datasets, and molecular ML models.
  - Match terms: machine learning force field, MLFF, Boltzmann generator, graph neural network, GNN, neural network potential, molecular modeling, normalizing flow
- `research/machine-learning/scientific-modeling` - machine learning methods for scientific systems outside a narrower molecular-modeling category.
  - Match terms: physics-informed, PINN, symbolic regression, mixture of experts, multi-task
- `research/machine-learning/statistical-modeling` - probabilistic or statistical machine-learning models.
  - Match terms: statistical modeling, mixture of experts, probabilistic, gating
- `research/molecular-simulation/datasets` - molecular datasets for simulation, ML potentials, or benchmark studies.
  - Match terms: molecular dataset, DFT dataset, quantum-chemistry dataset, SPICE, OMol25, dataset
- `research/molecular-simulation/force-fields` - molecular mechanics, water models, ML force fields, and force-field optimization.
  - Match terms: force field, force fields, force-field, force-field fitting, ForceBalance, water model, MLFF, potential function
- `research/molecular-simulation/free-energy` - free-energy estimation, alchemical methods, reweighting, PMFs, and binding or solvation free energies.
  - Match terms: free energy, free-energy, MBAR, reweighting, alchemical, lambda dynamics, solvation free energy, binding free energy, PMF
- `research/molecular-simulation/molecular-dynamics` - molecular dynamics methods, constraints, electrostatics, pressure tensors, and simulation engines.
  - Match terms: molecular dynamics, MD, trajectory, simulation, Ewald, PME, LINCS, pressure tensor, nonbonded
- `research/scientific-computing` - numerical algorithms and implementation patterns that are not specific to one scientific domain.
  - Match terms: implementation pattern, numerical, algorithm, computation
- `research/statistics/monte-carlo` - Monte Carlo, reweighting, estimators, sampling statistics, and uncertainty estimators.
  - Match terms: Monte Carlo, estimator, sampling, variance, uncertainty, effective sample size, Bennett, MBAR

## Naming rules

- Use lowercase path segments separated by `/`.
- Use hyphens inside a segment, not spaces or underscores.
- Keep category paths broad enough to collect multiple pages.
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

Suggest missing categories without applying changes with:

```sh
python3 tools/suggest_categories.py
```
