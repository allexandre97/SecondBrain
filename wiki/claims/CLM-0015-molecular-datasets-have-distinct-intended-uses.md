---
type: claim
status: active
created: 2026-07-01
updated: 2026-07-01
claim_status: limited
claim_scope: cross-source
areas:
  - research
categories:
  - research/molecular-simulation/datasets
  - research/experimental-benchmarking
  - research/machine-learning/molecular-modeling
tags:
  - claim
  - datasets
  - benchmarks
  - validation
related:
  - "[[wiki/concepts/machine-learning-potential-datasets]]"
  - "[[wiki/concepts/protein-force-field-benchmark-datasets]]"
  - "[[wiki/concepts/overlay-databanks-for-biomolecular-simulation-data]]"
  - "[[wiki/concepts/protein-energy-landscape-profiling]]"
sources:
  - SRC-0042
  - SRC-0043
  - SRC-0044
  - SRC-0057
  - SRC-0058
  - SRC-0060
  - SRC-0065
  - SRC-0067
sensitivity: public
encryption: none
---

# Molecular Datasets Have Distinct Intended Uses

## Claim

Molecular datasets should be compared by intended use: quantum-chemistry training labels, benchmark observables, response-property labels, curation/API layers, and downstream simulation validation are different dataset roles. [SRC-0042] [SRC-0043] [SRC-0044] [SRC-0057] [SRC-0065] [SRC-0067]

## Scope

This claim separates dataset semantics across the current cluster. It does not imply that one source must fill every role. [SRC-0042] [SRC-0043] [SRC-0044] [SRC-0057] [SRC-0060]

## Evidence

- SPICE and OMol25 primarily provide quantum-chemistry labels for training and evaluating molecular ML potentials, though OMol25 adds richer task evaluations. [SRC-0044] [SRC-0042]
- The protein force-field benchmark review is a benchmark-observable guide, not a single model-training dataset release. [SRC-0043]
- The NMRlipids overlay databank is a curation, metadata, naming, quality-evaluation, and API layer over existing simulation data rather than a new force-field benchmark or quantum-label dataset. [SRC-0057] [SRC-0058]
- UBio-Mol26 is a biology-focused training and evaluation dataset paired with a foundation-model framework. [SRC-0060]
- SPICE-alpha extends SPICE toward dipole and polarizability response properties for spectroscopy workflows. [SRC-0065]
- The protein energy-landscape paper creates high-throughput experimental fluctuation measurements that can serve as benchmark or learning targets for conformational energy landscapes. [SRC-0067]

## Caveats

- A dataset can play multiple roles, but the validation standard changes with the role: training-label quality, benchmark uncertainty, and downstream simulation relevance are not interchangeable. [SRC-0043] [SRC-0059]

## Links

- [[wiki/sources/SRC-0042-the-open-molecules-2025-omol25-dataset-evaluations-and]]
- [[wiki/sources/SRC-0043-structure-based-experimental-datasets-for-benchmarking-protein-simulation]]
- [[wiki/sources/SRC-0044-spice-a-dataset-of-drug-like-molecules-and]]
- [[wiki/sources/SRC-0057-overlay-databank-unlocks-data-driven-analyses-of-biomolecules]]
- [[wiki/sources/SRC-0058-supplementary-information-for-overlay-databank-unlocks-data-driven]]
- [[wiki/sources/SRC-0060-ubio-molfm-universal-molecular-foundation-model]]
- [[wiki/sources/SRC-0065-mace-mdp-molecular-dipole-moments-polarizabilities]]
- [[wiki/sources/SRC-0067-protein-energy-landscape-discovery-analysis-design]]
- [[wiki/concepts/machine-learning-potential-datasets]]
- [[wiki/concepts/protein-force-field-benchmark-datasets]]
