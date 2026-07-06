---
type: source
status: active
created: 2026-07-02
updated: 2026-07-02
source_id: SRC-0073
display_title: "Supplementary material for Machine-learned molecular mechanics force fields from large-scale quantum chemical data"
short_title: "espaloma-0.3 Supplement"
aliases:
  - "SRC-0073"
  - "espaloma-0.3 Supplement"
source_path: raw/sources/SRC-0073-supplementary-material-for-machine-learned-molecular-mechanics-force.pdf
imported_path: raw/sources/SRC-0073-supplementary-material-for-machine-learned-molecular-mechanics-force.pdf
original_filename: "d4sc00690a1_suppl.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 5c998405942d6c9e247f67e4723aa0def7585b3abf0ca7ef9eb331278987eb19
authors:
  - "Kenichiro Takaba"
  - "Anika J. Friedman"
  - "Chapin E. Cavender"
  - "Pavan Kumar Behara"
  - "Ivan Pulido"
  - "Michael M. Henry"
  - "Hugo MacDermott-Opeskin"
  - "Christopher R. Iacovella"
  - "Arnav M. Nagle"
  - "Alexander Matthew Payne"
  - "Michael R. Shirts"
  - "David L. Mobley"
  - "John D. Chodera"
  - "Yuanqing Wang"
author_entities:
  - "[[wiki/entities/authors/michael-r-shirts]]"
year: 2024
venue: "Chemical Science supplementary information"
doi: "10.1039/D4SC00690A"
arxiv:
metadata_review_status: reviewed
source_bundle: espaloma-0-3-ml-mm-force-fields
bundle_role: supplement
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/machine-learning/molecular-modeling
  - research/molecular-simulation/datasets
  - research/computational-drug-discovery
tags:
  - force-fields
  - molecular-mechanics
  - machine-learning
  - espaloma
  - supplementary-material
related:
  - "[[wiki/sources/SRC-0072-machine-learned-molecular-mechanics-force-fields-from-large]]"
  - "[[wiki/concepts/espaloma-machine-learned-mm-force-fields]]"
sources:
  - SRC-0072
  - SRC-0073
cites_sources:
  - SRC-0023
  - SRC-0044
citation_match_status: partial
cqt_review_status: source-local
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: standard
peer_review_status: supplementary-material
---

# Supplementary Material for Machine-Learned Molecular Mechanics Force Fields

Source ID: `SRC-0073`

## Raw source

- Repository path: `raw/sources/SRC-0073-supplementary-material-for-machine-learned-molecular-mechanics-force.pdf`
- Open raw source: [raw/sources/SRC-0073-supplementary-material-for-machine-learned-molecular-mechanics-force.pdf](../../raw/sources/SRC-0073-supplementary-material-for-machine-learned-molecular-mechanics-force.pdf)
- Main source: [[wiki/sources/SRC-0072-machine-learned-molecular-mechanics-force-fields-from-large]]

## Summary

The supplementary material provides the implementation and benchmark details for the espaloma-0.3 paper. It documents software dependencies, QCArchive datasets, training and hyperparameter choices, small-molecule geometry benchmarking, peptide and folded-protein MD protocols, alchemical protein-ligand binding free-energy calculations, and Tyk2 protein-ligand MD simulations. [SRC-0073]

## Key Points

- Core dependencies include modified Espaloma 0.3.0, PyTorch, Deep Graph Library, Open Force Field Toolkit, OpenMMForceFields, Perses, and cinnabar. [SRC-0073]
- QCArchive datasets include small-molecule, peptide, and RNA sets such as SPICE-PubChem, SPICE-DES-Monomers, SPICE-Dipeptide, OpenFF Gen2 optimization/torsion datasets, peptide conformation datasets, RNA-Diverse, RNA-Trinucleotide, and RNA-Nucleoside. [SRC-0073]
- Data preparation removed molecules with a large energy range, used OpenFF 2.0.0 van der Waals parameters, and fit charges through an electronegativity/hardness model against AM1-BCC ELF10 reference charges. [SRC-0073]
- Hyperparameter search and production training details include GraphSAGE layers, Janossy pooling/readout layers, energy/force/charge losses, torsion regularization, dropout, and early stopping. [SRC-0073]
- The protein-ligand free-energy benchmark used Perses/OpenMM with 12 alchemical states, replica exchange, PyMBAR, and a modified cinnabar workflow. [SRC-0073]
- Tyk2 unbiased MD compared self-consistent espaloma-0.3 protein-ligand parametrization against Amber ff14SB plus OpenFF 2.1.0. [SRC-0073]

## Links

- [[wiki/sources/SRC-0072-machine-learned-molecular-mechanics-force-fields-from-large]]
- [[wiki/concepts/espaloma-machine-learned-mm-force-fields]]
- [[wiki/sources/SRC-0044-spice-a-dataset-of-drug-like-molecules-and]]
- [[wiki/sources/SRC-0023-statistically-optimal-analysis-multiple-equilibrium-states-mbar]]

## Ingestion QA

### Retrieval questions checked

- What implementation dependencies are needed to reproduce the paper?
- Which QCArchive datasets were used?
- How were data split, augmented, and filtered?
- What training losses and regularization choices were used?
- How were protein-ligand free-energy calculations run?
- What details does the supplement add beyond the main paper?

### Coverage decision

Complete as a supplement page with `coverage_profile: standard`. The page preserves the supplement's role, main reproducibility details, benchmark protocols, bundle linkage, and confirmed source links without duplicating all tables and figures.

### Known gaps

- Detailed per-dataset tables, all repository commit hashes, and every figure caption are left in the raw supplement.
- The supplement's referenced external repositories and datasets were not separately ingested.
