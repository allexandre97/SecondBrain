---
type: source
status: active
created: 2026-06-30
updated: 2026-06-30
source_id: SRC-0045
display_title: "Large-scale Collaborative Assessment of Binding Free Energy Calculations for Drug Discovery Using OpenFE"
short_title: "OpenFE RBFE Benchmark"
aliases:
  - "SRC-0045"
  - "OpenFE RBFE Benchmark"
  - "Large-scale Collaborative Assessment of Binding Free Energy Calculations for Drug Discovery Using OpenFE"
source_path: raw/sources/SRC-0045-large-scale-collaborative-assessment-of-binding-free-energy.pdf
original_filename: "chemrxiv-2025-7sthd_v2.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 13b864deeb88b30b8c9fd482b7640bb7b6fdf8fa6977a3d79af034a8feb48563
areas:
  - research
categories:
  - research/molecular-simulation/binding-free-energy
tags:
  - RBFE
  - OpenFE
  - benchmarking
  - drug-discovery
related:
  - "[[concepts/relative-binding-free-energy-benchmarking]]"
  - "[[concepts/free-energy-estimation]]"
sources:
  - SRC-0045
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: math-standard
---

# Large-scale Collaborative Assessment of Binding Free Energy Calculations for Drug Discovery Using OpenFE

Source ID: `SRC-0045`

## Raw source

- Repository path: `raw/sources/SRC-0045-large-scale-collaborative-assessment-of-binding-free-energy.pdf`
- Local relative link: [Open raw source](../../raw/sources/SRC-0045-large-scale-collaborative-assessment-of-binding-free-energy.pdf)

## Summary

This ChemRxiv preprint benchmarks the OpenFE relative binding free energy protocol across a large public/private drug-discovery corpus. The study evaluates public systems selected from the Ross et al. benchmark and blinded private industry datasets, reporting lower accuracy on private real-world datasets than on curated public datasets. [SRC-0045]

## Key Points

- The public benchmark contains 58 protein-ligand systems and 876 ligands selected from the Schroedinger 2023 benchmark set; the private benchmark contains 37 anonymized industry datasets and 842 ligands. [SRC-0045, section 2.1]
- The OpenFE protocol uses a hybrid-topology RBFE approach implemented in `openfe-v1.0.1`, OpenMM dynamics, Amber14SB for protein, TIP3P water, OpenFF Sage-2.2.0 for ligands/cofactors, Hamiltonian replica exchange, and MBAR analysis via `pymbar`. [SRC-0045, sections 2.4-2.5]
- Public benchmark performance is reported as a weighted all-to-all pairwise RMSE of about 1.72 kcal/mol, with 10 systems reaching sub-kcal/mol accuracy. [SRC-0045, section 3.1.1]
- Private benchmark performance is worse, with a weighted RMSE of about 2.44 kcal/mol and only 2 systems reaching sub-kcal/mol accuracy. [SRC-0045, abstract]
- The paper emphasizes that OpenFE was used with default protocol settings, while the FEP+ comparison used previously published, manually tuned results. [SRC-0045, section 4.1]
- Performance was system-dependent; the study did not identify a single dominant error source. [SRC-0045, abstract]

## Key equations

**Weighted RMSE aggregation, source Eq. (3) [SRC-0045]:**

$$
\mathrm{RMSE} =
\sqrt{
\frac{1}{\sum_i^M w_i}
\sum_i^M w_i \mathrm{RMSE}_i^2
}.
$$

Here $w_i$ is the number of ligands in system $i$ for the all-to-all pairwise benchmark. [SRC-0045, section 3.1.1]

## Variable glossary

- $\Delta\Delta G$: relative binding free energy between two ligands. [SRC-0045]
- $\mathrm{RMSE}_i$: root mean squared error for benchmark system $i$. [SRC-0045, section 3.1.1]
- $w_i$: aggregation weight, set to the number of ligands in the system for pairwise RMSE. [SRC-0045, section 3.1.1]
- $M$: number of benchmark systems included in the aggregate. [SRC-0045, section 3.1.1]

## Equation inventory

| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |
| Weighted RMSE | Eq. (3), section 3.1.1 | Key equations | Aggregates per-system benchmark error | $\mathrm{RMSE}_i$, $w_i$, $M$ | Needed to compare benchmark summaries |

## Limitations

- The preprint had not been peer reviewed at posting. [SRC-0045]
- Membrane-bound systems were excluded because of OpenFE tooling limitations at the time of the study. [SRC-0045, section 2.1]
- Large topological changes such as ring breaking in macrocycles were excluded, although smaller scaffold-hop-like cases were included. [SRC-0045, section 2.1]
- The FEP+ comparison is not a clean controlled-method comparison because sampling lengths, manual setup, force fields, enhanced water sampling, and protocol tuning differ. [SRC-0045, section 4.1]
- Private datasets include assay-limit, stereochemical, tautomeric, pose, metal, water-sampling, and large-transformation complications that make benchmark interpretation harder. [SRC-0045, section 4.2]

## Links

- [[concepts/relative-binding-free-energy-benchmarking]]
- [[concepts/free-energy-estimation]]

## Ingestion QA

### Retrieval questions checked

- What was the central OpenFE benchmark contribution?
- How many public and private systems/ligands were evaluated?
- What protocol and force-field choices define the OpenFE workflow?
- What weighted RMSE did OpenFE achieve on public and private data?
- Why is comparison with FEP+ not a controlled apples-to-apples comparison?
- Which systems or transformations were excluded?
- What limitations were identified for prospective industrial use?

### Coverage decision

Complete at `coverage_profile: math-standard`. The source page captures benchmark scope, protocol settings, central metrics, limitations, and the aggregation equation needed for later retrieval.

### Known gaps

- The wiki does not reproduce all public/private dataset tables, per-target metrics, or supplementary protocol-difference tables.
