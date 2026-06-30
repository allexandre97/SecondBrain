---
type: source
status: active
created: 2026-06-30
updated: 2026-06-30
source_id: SRC-0042
display_title: "The Open Molecules 2025 (OMol25) Dataset, Evaluations, and Models"
short_title: "OMol25 Dataset"
aliases:
  - "SRC-0042"
  - "OMol25 Dataset"
  - "The Open Molecules 2025 (OMol25) Dataset, Evaluations, and Models"
source_path: raw/sources/SRC-0042-the-open-molecules-2025-omol25-dataset-evaluations-and.pdf
original_filename: "2505.08762v2.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 409286c94d38222c5893d9f34c4c346dd07b33806f5e4f0a22dd82f3382bf360
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/machine-learning/scientific-modeling
tags:
  - datasets
  - machine-learning-potentials
  - quantum-chemistry
  - OMol25
related:
  - "[[concepts/machine-learning-potential-datasets]]"
  - "[[concepts/automated-force-field-training]]"
sources:
  - SRC-0042
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: standard
---

# The Open Molecules 2025 (OMol25) Dataset, Evaluations, and Models

Source ID: `SRC-0042`

## Raw source

- Repository path: `raw/sources/SRC-0042-the-open-molecules-2025-omol25-dataset-evaluations-and.pdf`
- Local relative link: [Open raw source](../../raw/sources/SRC-0042-the-open-molecules-2025-omol25-dataset-evaluations-and.pdf)

## Summary

OMol25 is a large-scale quantum-chemistry dataset for training and evaluating machine-learning interatomic potentials across broad molecular chemistry. It contains more than 140 million DFT single-point calculations at the $\omega$B97M-V/def2-TZVPD level, covers 83 elements, and includes small molecules, biomolecules, metal complexes, electrolytes, reactive structures, charge/spin variation, explicit solvation, and systems up to 350 atoms. [SRC-0042]

## Key Points

- OMol25 responds to the lack of molecular MLIP datasets that combine scale, high DFT accuracy, broad elemental diversity, chemical diversity, and structural diversity. [SRC-0042, section 1]
- It recomputes several existing community datasets at a consistent high level of theory and adds biomolecule, metal-complex, electrolyte, main-group, and reactive subsets. [SRC-0042, sections 2 and 2.5]
- Calculations use ORCA 6.0.0 with $\omega$B97M-V/def2-TZVPD, acceleration techniques, tight convergence settings, and quality-control checks. [SRC-0042, section 2.7]
- The dataset profile includes charges from -10 to +10, spin multiplicities from 1 to 11, atom counts from 2 to 350, and additional properties beyond energies and forces. [SRC-0042, section 2.8]
- Splits are composition-based, with full, 4M, and neutral training variants plus explicit out-of-distribution splits for metal-ligand bonds, metal-containing protein structures, reactions, experimental crystal structures, and anions. [SRC-0042, section 2.9]
- Evaluations include energy/force prediction and chemistry-oriented tasks such as ligand-pocket interactions, ligand strain, conformer ranking, protonation energies, ionization energies, electron affinities, spin gaps, and distance scaling. [SRC-0042]

## Access and Licensing

- The paper reports dataset and model availability through Hugging Face and code through `fairchem`; it states the data are released under CC BY 4.0, while model weights use a commercially permissive license with geographic and acceptable-use restrictions. [SRC-0042]

## Limitations

- Baseline models need explicit charge and spin inputs; the paper uses a simple charge/spin embedding and notes that more complex schemes may be needed. [SRC-0042]
- Energy/force MAE alone is insufficient for practical chemistry, motivating the task suite but not eliminating downstream validation needs. [SRC-0042]
- OMol25 is broad but still defined by its generation protocols, DFT level, quality-control filters, and subdomain sampling choices. [SRC-0042]

## Links

- [[concepts/machine-learning-potential-datasets]]
- [[concepts/automated-force-field-training]]
- [[questions/force-field-training-validation-scope]]

## Ingestion QA

### Retrieval questions checked

- What is OMol25?
- What level of theory does it use?
- What chemistry domains and elements does it cover?
- How are train/validation/test splits defined?
- What out-of-distribution evaluations are included?
- What baseline limitations are noted?
- Where is the dataset reported as available?

### Coverage decision

Complete at `coverage_profile: standard`. The page captures the dataset purpose, size, level of theory, coverage, splits, evaluations, access notes, and limitations.

### Known gaps

- The wiki does not reproduce every subdataset generation protocol or baseline result table.
