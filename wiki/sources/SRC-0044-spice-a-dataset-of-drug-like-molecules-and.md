---
type: source
status: active
created: 2026-06-30
updated: 2026-06-30
source_id: SRC-0044
display_title: "SPICE, a Dataset of Drug-like Molecules and Peptides for Training Machine Learning Potentials"
short_title: "SPICE Dataset"
aliases:
  - "SRC-0044"
  - "SPICE Dataset"
  - "SPICE, a Dataset of Drug-like Molecules and Peptides for Training Machine Learning Potentials"
source_path: raw/sources/SRC-0044-spice-a-dataset-of-drug-like-molecules-and.pdf
original_filename: "s41597-022-01882-6.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 838f07c41bc888ff5181f66719a5e9f5966c360d8d5913a7f672e1b9bdb8a4dd
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/machine-learning/scientific-modeling
tags:
  - datasets
  - machine-learning-potentials
  - SPICE
  - quantum-chemistry
related:
  - "[[concepts/machine-learning-potential-datasets]]"
  - "[[concepts/automated-force-field-training]]"
sources:
  - SRC-0044
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: standard
---

# SPICE, a Dataset of Drug-like Molecules and Peptides for Training Machine Learning Potentials

Source ID: `SRC-0044`

## Raw source

- Repository path: `raw/sources/SRC-0044-spice-a-dataset-of-drug-like-molecules-and.pdf`
- Local relative link: [Open raw source](../../raw/sources/SRC-0044-spice-a-dataset-of-drug-like-molecules-and.pdf)

## Summary

SPICE is a quantum-chemistry dataset for training machine-learning potentials relevant to drug-like small molecules interacting with proteins. The described release contains more than 1.1 million conformations spanning small molecules, dimers, dipeptides, solvated amino acids, and ion pairs, with DFT energies and forces at the $\omega$B97M-D3(BJ)/def2-TZVPPD level. [SRC-0044]

## Key Points

- SPICE is designed for transferable, ready-to-use molecular ML potentials rather than system-specific models. [SRC-0044]
- It includes 19,238 molecules or clusters and 1,132,808 conformations across 15 elements: H, Li, C, N, O, F, Na, Mg, P, S, Cl, K, Ca, Br, and I. [SRC-0044, table 1]
- Subsets include dipeptides, solvated amino acids, DES370K dimers and monomers, PubChem drug-like molecules, and ion pairs. [SRC-0044]
- It includes forces as well as energies, plus additional properties such as dipole and quadrupole moments, MBIS multipoles, Wiberg bond orders, and Mayer bond orders. [SRC-0044]
- The dataset is deposited on Zenodo as `SPICE-1.1.2.hdf5`, and generation scripts are reported as available in the `openmm/spice-dataset` repository. [SRC-0044]
- A proof-of-concept equivariant transformer ensemble reached MAE 4.663 kJ/mol across the complete dataset, with median absolute error 2.912 kJ/mol, while the authors emphasize the models are not production-ready. [SRC-0044]

## Dataset Design Criteria

- Broad chemical-space coverage for drug-like molecules and protein targets. [SRC-0044]
- Relevant conformational-space coverage, including higher-energy conformations encountered in MD and conformer search, but excluding bond-forming/breaking reactive conformations in the initial release. [SRC-0044]
- Forces as well as energies. [SRC-0044]
- A high practical level of theory, plus extra inexpensive quantum-chemistry properties. [SRC-0044]
- Dynamic, growing, versioned releases for reproducibility and future expansion. [SRC-0044]

## Limitations

- The initial release does not target covalent bond formation/breaking or reactive potentials. [SRC-0044]
- The proof-of-concept model uses a simple formal-charge atom typing scheme, and charge handling remains open. [SRC-0044]
- Error outliers are associated with unusual chemistries, suggesting that additional data are needed for rare motifs. [SRC-0044]

## Links

- [[concepts/machine-learning-potential-datasets]]
- [[concepts/automated-force-field-training]]
- [[questions/force-field-training-validation-scope]]

## Ingestion QA

### Retrieval questions checked

- What is SPICE intended to train?
- What subsets and chemical elements does it contain?
- What quantum-chemistry level is used?
- Does it include forces?
- Where is the dataset stored?
- What proof-of-concept validation is reported?
- What limitations and future expansions are identified?

### Coverage decision

Complete at `coverage_profile: standard`. The page captures the dataset purpose, composition, generation principles, access, validation, and limitations.

### Known gaps

- The wiki does not reproduce every subset construction detail or proof-of-concept model hyperparameter.
