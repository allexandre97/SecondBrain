---
type: concept
status: active
created: 2026-06-30
updated: 2026-07-01
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/biomolecules/proteins
  - research/data-management
  - research/experimental-benchmarking
  - research/molecular-simulation/datasets
tags:
  - protein-force-fields
  - benchmarking
  - experimental-observables
  - datasets
sources:
  - SRC-0043
  - SRC-0067
related:
  - "[[wiki/concepts/force-field-training-from-experimental-observables]]"
  - "[[wiki/concepts/ensemble-and-force-field-refinement]]"
  - "[[wiki/concepts/protein-energy-landscape-profiling]]"
  - "[[wiki/claims/CLM-0015-molecular-datasets-have-distinct-intended-uses]]"
  - "[[wiki/questions/mlip-foundation-model-validation-scope]]"
sensitivity: public
encryption: none
---

# Protein Force Field Benchmark Datasets

## Summary

Protein force-field benchmark datasets compare simulations against experimental observables that report on protein structural ensembles. Useful benchmarks should include peptides, folded proteins, and disordered proteins, and should account for experimental uncertainty, simulation convergence, and forward-model assumptions. [SRC-0043]

## Key Points

- Recommended first-tier observables include chemical shifts, scalar couplings, residual dipolar couplings, and Bragg electron/nuclear densities. [SRC-0043]
- NMR benchmarks are valuable because solution conditions resemble many protein simulations and observables can report on ensemble excursions from native structures. [SRC-0043]
- Room-temperature crystallography benchmarks add tertiary-structure and crystal-environment information, but often need larger/longer crystal simulations and less standardized comparison workflows. [SRC-0043]
- Benchmarks should separate sampling precision from force-field accuracy by checking equilibration, convergence, and statistical uncertainty. [SRC-0043]
- Simulation-experiment comparison depends on forward models and experimental structural models, so disagreement is not automatically a force-field error. [SRC-0043]
- Large-scale mHDX-MS datasets add a complementary benchmark direction by measuring conformational fluctuation energy profiles and local opening stability across thousands of protein domains rather than only native structures or global folding stabilities. [SRC-0067]

## Links

- [[wiki/sources/SRC-0043-structure-based-experimental-datasets-for-benchmarking-protein-simulation]]
- [[wiki/sources/SRC-0067-protein-energy-landscape-discovery-analysis-design]]
- [[wiki/concepts/force-field-training-from-experimental-observables]]
- [[wiki/concepts/ensemble-and-force-field-refinement]]
- [[wiki/concepts/protein-energy-landscape-profiling]]
- [[wiki/claims/CLM-0015-molecular-datasets-have-distinct-intended-uses]]
- [[wiki/questions/mlip-foundation-model-validation-scope]]

## Open Questions

- Which benchmark observables should be used as first-tier filters versus second-tier diagnostics when evaluating new protein force fields or protein ensemble generators?
- How can mHDX-MS opening-energy distributions be forward-modeled from simulations without overinterpreting intact-protein HDX measurements?
