---
type: tension
status: active
created: 2026-07-01
updated: 2026-07-01
tension_status: active
areas:
  - research
categories:
  - research/molecular-simulation/free-energy
  - research/computational-drug-discovery
  - research/experimental-benchmarking
tags:
  - tension
  - rbfe
  - benchmarking
  - drug-discovery
related_claims:
  - "[[wiki/claims/CLM-0017-experimental-reproducibility-bounds-rbfe-error-interpretation]]"
  - "[[wiki/claims/CLM-0018-public-rbfe-benchmarks-can-be-easier-than-private-active-project-data]]"
  - "[[wiki/claims/CLM-0019-edgewise-rbfe-metrics-can-overstate-arbitrary-comparison-quality]]"
related_questions:
  - "[[wiki/questions/rbfe-benchmark-prospective-use-scope]]"
sources:
  - SRC-0045
  - SRC-0046
  - SRC-0061
  - SRC-0062
sensitivity: public
encryption: none
---

# RBFE Benchmark Success vs Prospective Use

## Tension

RBFE benchmarks can show strong retrospective performance while still overpredicting prospective utility if experimental reproducibility, private active-project difficulty, setup ambiguity, and metric choice are not made explicit. [SRC-0046] [SRC-0061]

## Evidence

- SRC-0046 argues that retrospective FEP+ accuracy can approach experimental reproducibility after careful preparation, but also cautions that prospective use can be harder. [SRC-0046]
- SRC-0061 reports better OpenFE performance on curated public benchmarks than on blinded private active-project datasets. [SRC-0061]
- SRC-0062 shows that protocol differences, atom mapping, convergence, private problematic ligands, and edge-difficulty diagnostics materially affect interpretation. [SRC-0062]
- SRC-0045 records the same public/private performance gap in the preprint version. [SRC-0045]

## Current Status

Active. The cluster supports RBFE as useful for drug discovery, but only with benchmark reporting that separates retrospective public success from prospective deployment risk.

## Links

- [[wiki/sources/SRC-0045-large-scale-collaborative-assessment-of-binding-free-energy]]
- [[wiki/sources/SRC-0046-the-maximal-and-current-accuracy-of-rigorous-protein]]
- [[wiki/sources/SRC-0061-openfe-rbfe-benchmark-journal-version]]
- [[wiki/sources/SRC-0062-openfe-rbfe-benchmark-supporting-information]]
- [[wiki/concepts/relative-binding-free-energy-benchmarking]]
- [[wiki/questions/rbfe-benchmark-prospective-use-scope]]
