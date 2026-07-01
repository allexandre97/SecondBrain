---
type: source
status: active
created: 2026-07-01
updated: 2026-07-01
source_id: SRC-0066
display_title: "Fast Training of Bespoke SMIRNOFF-Format Molecular Mechanics Force Fields Using Machine Learning Potentials"
short_title: "presto Bespoke SMIRNOFF Force Fields"
aliases:
  - "SRC-0066"
  - "presto Bespoke SMIRNOFF Force Fields"
  - "Fast training of bespoke SMIRNOFF-format molecular mechanics force fields using machine learning potentials"
source_path: raw/sources/SRC-0066-presto-bespoke-smirnoff-force-fields-mlps.pdf
imported_path: raw/sources/SRC-0066-presto-bespoke-smirnoff-force-fields-mlps.pdf
original_filename: "chemrxiv.15004169_v1.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 49f06717b000f07299d1c2c332b83b5987feeb3bd6ac2227b8cb86e2a6ca9ab3
authors:
  - "Finlay Clark"
  - "Thomas Pope"
  - "Sarah Maier"
  - "Simon Boothroyd"
  - "Joshua T. Horton"
  - "Kevin Ryczko"
  - "Andrea Bortolato"
  - "Daniel J. Cole"
author_entities: []
year: 2026
venue: "ChemRxiv"
doi: "10.26434/chemrxiv.15004169/v1"
arxiv:
metadata_review_status: reviewed
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/machine-learning/molecular-modeling
  - research/computational-drug-discovery
  - research/experimental-benchmarking
tags:
  - preprint
  - presto
  - SMIRNOFF
  - OpenFF
  - bespoke-force-fields
  - machine-learning-potentials
related:
  - "[[wiki/concepts/mlp-driven-bespoke-smirnoff-force-field-fitting]]"
  - "[[wiki/concepts/automated-force-field-training]]"
  - "[[wiki/concepts/forcebalance]]"
  - "[[wiki/concepts/machine-learned-interatomic-potential-foundation-models]]"
sources:
  - SRC-0066
cites_sources:
  - SRC-0042
  - SRC-0044
citation_match_status: reviewed
cqt_review_status: linked
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: standard
peer_review_status: not-peer-reviewed
---

# Fast Training of Bespoke SMIRNOFF-Format Molecular Mechanics Force Fields Using Machine Learning Potentials

Source ID: `SRC-0066`

## Raw source

- Repository path: `raw/sources/SRC-0066-presto-bespoke-smirnoff-force-fields-mlps.pdf`
- Open raw source: [raw/sources/SRC-0066-presto-bespoke-smirnoff-force-fields-mlps.pdf](../../raw/sources/SRC-0066-presto-bespoke-smirnoff-force-fields-mlps.pdf)

## Status note

This is a ChemRxiv preprint posted on 2026-06-01 under CC-BY 4.0 and explicitly marked as not peer reviewed. Treat its results as preliminary until peer-reviewed or independently reproduced. [SRC-0066]

## Summary

Clark et al. introduce `presto`, an open-source Python package for quickly fitting molecule-specific or congeneric-series SMIRNOFF-format valence parameters using machine-learning potentials as reference models. The workflow generates high-temperature molecular-dynamics and metadynamics samples, evaluates MLP energies and forces, and trains bonds, angles, proper torsions, and improper torsions on GPU through PyTorch-based OpenFF tooling. [SRC-0066]

## Key Points

- `presto` targets the speed bottleneck in bespoke force-field fitting by replacing direct quantum-mechanical reference calculations with transferable MLP evaluations. [SRC-0066]
- The default workflow starts from an OpenFF force field, creates bespoke valence SMARTS/SMIRKS patterns, initializes bond and angle parameters from an MLP Hessian using a modified Seminario method, samples off-equilibrium structures, and fits valence parameters to MLP energies and forces. [SRC-0066]
- Sampling uses high-temperature MD with concurrent well-tempered metadynamics on flexible torsions, plus short MLP and MM minimizations to improve torsion-profile fitting. [SRC-0066]
- Training is GPU-accelerated using `smee` and `descent`, with SMIRNOFF-format force fields represented in PyTorch for automatic differentiation. [SRC-0066]
- The authors report a full automated workflow of roughly 15 minutes for a 50-atom molecule on a single NVIDIA RTX A4500 GPU using AceFF 2.0. [SRC-0066]
- On 400 TorsionNet500 test molecules, `presto` reduces torsion-scan RMSE by about a factor of three relative to OpenFF Sage 2.3.0 and improves heavy-atom RMSD and Jensen-Shannon distance metrics. [SRC-0066]
- On JACS set fragments, `presto` gives torsion-scan performance comparable to direct QM torsion fitting with OpenFF BespokeFit while being faster. [SRC-0066]
- On the Folmsbee and Hutchison conformer set, `presto` improves relative conformer energies over Sage and espaloma but remains bounded by nonbonded intramolecular interaction and MLP-reference limitations. [SRC-0066]
- `presto` supports simultaneous fitting of congeneric series, allowing shared parameters for shared molecular substructures. [SRC-0066]
- In relative binding free-energy tests on CDK2, TYK2, and JNK1 with Tango/ATM, `presto` gives performance broadly comparable to OpenFF 1.3.1, with possible improvements where initial parameters are especially poor. [SRC-0066]

## Limitations and Caveats

- The source is a preprint and has not been peer reviewed. [SRC-0066]
- `presto` fits valence terms only; inaccurate intramolecular nonbonded interactions can limit agreement with MLP reference data and downstream conformer performance. [SRC-0066]
- Some fitting failures were observed for sulfonamides and protonated phosphates under default protocol choices, requiring protocol adjustments such as disabling MLP minimization or modified Seminario initialization. [SRC-0066]
- The default protocol is not exhaustively optimized and may trade speed for robustness; different molecule classes may need different settings. [SRC-0066]
- Free-energy benchmarks show comparable average performance to Parsley on systems where Parsley already performs well, so broad RBFE superiority is not established. [SRC-0066]
- Large molecules or systems with strong intramolecular nonbonded interactions may require fragmentation, filtering, or future method changes. [SRC-0066]

## Claims

- MLP-driven bespoke fitting can reduce reference-data cost while leaving downstream validation and failure-mode checks central to force-field usefulness. [SRC-0066]
- [[wiki/claims/CLM-0013-energy-force-error-is-not-downstream-md-reliability]]
- [[wiki/questions/force-field-training-validation-scope]]

## Citation Links

- `SRC-0042`: The paper cites the Open Molecules 2025 dataset in its discussion of MLP/foundation-model training data, matching the ingested OMol25 source. [SRC-0066]
- `SRC-0044`: The paper cites the SPICE dataset in its discussion of MLP/foundation-model training data, matching the ingested SPICE source. [SRC-0066]

## Links

- [[wiki/concepts/mlp-driven-bespoke-smirnoff-force-field-fitting]]
- [[wiki/concepts/automated-force-field-training]]
- [[wiki/concepts/forcebalance]]
- [[wiki/concepts/machine-learned-interatomic-potential-foundation-models]]
- [[wiki/questions/force-field-training-validation-scope]]

## Metadata notes

- DOI shown by the source: `10.26434/chemrxiv.15004169/v1`.
- Data/code availability in the source points to `presto`, `smee`, `descent`, and a Snakemake benchmarking workflow on GitHub; Tango free-energy software is described as not publicly available, while computed values and downstream analysis code are provided. [SRC-0066]

## Ingestion QA

### Retrieval questions checked

- What is `presto`?
- What problem does it address relative to QM-based bespoke fitting?
- Which SMIRNOFF terms are fit?
- How are training data generated?
- What role do MLPs play?
- What benchmark improvements are reported?
- Does it improve RBFE performance broadly?
- What limitations and failure modes are acknowledged?
- Is the source peer reviewed?

### Coverage decision

Complete at `coverage_profile: standard`. The source page captures source status, workflow, fitted parameter scope, major benchmarks, RBFE results, limitations, and links to durable force-field training concepts.

### Known gaps

- The wiki does not reproduce all method equations, supplementary analyses, benchmark figures, or software command-line options.
- Tango implementation details remain summarized because the source states Tango is not publicly available.
