---
type: source
status: active
created: 2026-06-30
updated: 2026-06-30
source_id: SRC-0043
display_title: "Structure-Based Experimental Datasets for Benchmarking Protein Simulation Force Fields"
short_title: "Protein Force-Field Benchmark Datasets"
aliases:
  - "SRC-0043"
  - "Protein Force-Field Benchmark Datasets"
  - "Structure-Based Experimental Datasets for Benchmarking Protein Simulation Force Fields"
source_path: raw/sources/SRC-0043-structure-based-experimental-datasets-for-benchmarking-protein-simulation.pdf
original_filename: "LiveCoMS_Article_v1.0.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 95c85906eb59d36b73563e7b4c92f09255f368b94c4b806194a1f4f9e263649e
authors:
  - "Chapin E. Cavender"
  - "David A. Case"
  - "Julian C.-H. Chen"
  - "Lillian T. Chong"
  - "Daniel A. Keedy"
  - "Kresten Lindorff-Larsen"
  - "David L. Mobley"
  - "O. H. Samuli Ollila"
  - "Chris Oostenbrink"
  - "Paul Robustelli"
  - "Vincent A. Voelz"
  - "Michael E. Wall"
  - "David C. Wych"
  - "Michael K. Gilson"
author_entities: []
year: 2025
venue: "Living Journal of Computational Molecular Science"
doi: "10.33011/livecoms.6.1.3871"
arxiv:
metadata_review_status: reviewed
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/biomolecules/proteins
  - research/data-management
  - research/experimental-benchmarking
  - research/molecular-simulation/datasets
tags:
  - datasets
  - protein-force-fields
  - benchmarking
  - experimental-observables
related:
  - "[[wiki/concepts/protein-force-field-benchmark-datasets]]"
  - "[[wiki/concepts/force-field-training-from-experimental-observables]]"
sources:
  - SRC-0043
cites_sources: []
citation_match_status: reviewed
cqt_review_status: linked
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: standard
---

# Structure-Based Experimental Datasets for Benchmarking Protein Simulation Force Fields

Source ID: `SRC-0043`

## Raw source

- Repository path: `raw/sources/SRC-0043-structure-based-experimental-datasets-for-benchmarking-protein-simulation.pdf`
- Open raw source: [raw/sources/SRC-0043-structure-based-experimental-datasets-for-benchmarking-protein-simulation.pdf](../../raw/sources/SRC-0043-structure-based-experimental-datasets-for-benchmarking-protein-simulation.pdf)

## Summary

This LiveCoMS perpetual review surveys structurally oriented experimental datasets for benchmarking protein force fields, focusing on NMR spectroscopy and room-temperature protein crystallography. It explains what observables report about protein structure and dynamics, how they can be compared with molecular simulations, and how benchmark simulations should be set up and analyzed. [SRC-0043]

## Key Points

- A minimal benchmark should include at least one dataset each for peptides, folded proteins, and disordered proteins. [SRC-0043]
- The review prioritizes chemical shifts, scalar couplings, residual dipolar couplings, and Bragg electron/nuclear densities because they offer useful combinations of uncertainty, convergence, consensus methodology, and structural information. [SRC-0043]
- It deprioritizes NOE intensities, spin relaxation rates, paramagnetic relaxation enhancement, crystallographic B-factors, alternate conformations, and diffuse scattering when resources are limited, while noting that they still provide useful ensemble information. [SRC-0043]
- The dataset table covers NMR datasets such as Beauchamp short peptides, designed beta-hairpins/Trp-cage miniproteins, Stroet folded proteins, Mao folded proteins, Robustelli folded/disordered proteins, spin relaxation datasets, and salt-bridge stabilities. [SRC-0043, table 1]
- The crystallography coverage includes scorpion toxin, hen egg-white lysozyme, crambin, cyclophilin A, ubiquitin variants, PTP1B, endoglucanase, and staphylococcal nuclease. [SRC-0043, table 1]
- Comparison is never directly between simulation coordinates and raw experiment; forward models and structural models mediate comparison and carry assumptions. [SRC-0043]

## Benchmarking Notes

- Benchmark simulations should replicate experimental conditions as closely as possible, including initial coordinates, solvation, ions/co-solutes, and thermodynamic ensemble. [SRC-0043, section 5]
- For crystal benchmarks, box construction may need to reflect crystal conditions and sometimes supercells, especially for diffuse scattering. [SRC-0043, section 5]
- Analysis should account for equilibration, convergence, and statistical uncertainty before attributing disagreement to force-field error. [SRC-0043, section 5.2]

## Limitations

- The article is a review and recommendation document, not a single benchmark dataset release. [SRC-0043]
- Several observables lack consensus best practices for comparison to simulations. [SRC-0043]
- The review focuses on water-soluble proteins and peptides without ligands, cofactors, membranes, or noncanonical chemistry. [SRC-0043]

## Claims

- Protein force-field benchmarks should distinguish benchmark observables from training labels and should include setup, forward-model, convergence, and uncertainty considerations. [SRC-0043]
- [[wiki/claims/CLM-0015-molecular-datasets-have-distinct-intended-uses]]

## Questions

- [[wiki/questions/mlip-foundation-model-validation-scope]]
- [[wiki/questions/force-field-training-validation-scope]]

## Citation Links

- Citation review status: reviewed for strong links to currently ingested dataset/biomolecule sources in this cluster; no strong source-to-source link was promoted. Full bibliography normalization of the perpetual review remains out of scope. [SRC-0043]

## Links

- [[wiki/concepts/protein-force-field-benchmark-datasets]]
- [[wiki/concepts/force-field-training-from-experimental-observables]]
- [[wiki/questions/force-field-training-validation-scope]]

## Ingestion QA

### Retrieval questions checked

- What experimental dataset types does the review cover?
- Which observables are recommended first for limited resources?
- What protein classes should a minimal benchmark include?
- What NMR and crystallography datasets are listed?
- Why are forward models necessary for simulation-experiment comparison?
- What setup and analysis practices are recommended?
- What scope limits does the review set?

### Coverage decision

Complete at `coverage_profile: standard`. The page captures benchmark recommendations, observable priorities, dataset categories, setup guidance, and limitations.

### Known gaps

- The wiki does not reproduce the full per-dataset discussion or all appendix equations for NMR relaxation.
