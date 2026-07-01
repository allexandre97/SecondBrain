---
type: question
status: active
created: 2026-07-01
updated: 2026-07-01
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/machine-learning/molecular-modeling
  - research/experimental-benchmarking
tags:
  - validation
  - foundation-models
  - machine-learning-potentials
related:
  - "[[wiki/concepts/machine-learned-interatomic-potential-foundation-models]]"
  - "[[wiki/concepts/machine-learning-potential-datasets]]"
  - "[[wiki/claims/CLM-0013-energy-force-error-is-not-downstream-md-reliability]]"
  - "[[wiki/claims/CLM-0014-dataset-scale-does-not-replace-coverage-validation]]"
  - "[[wiki/tensions/TEN-0008-dataset-scale-vs-downstream-validation]]"
sources:
  - SRC-0042
  - SRC-0043
  - SRC-0059
  - SRC-0060
  - SRC-0065
  - SRC-0067
sensitivity: public
encryption: none
---

# MLIP Foundation Model Validation Scope

## Question

What validation evidence is sufficient to treat a machine-learned interatomic-potential foundation model as reliable for a specific molecular or biomolecular simulation regime?

## Current Position

The cluster points to a stratified answer: static energy/force accuracy is necessary but not sufficient, dataset scale must be matched to chemical and conformational coverage, and validation should be organized by downstream task, biomolecular class, observable, timescale, and long-range-physics requirement. [SRC-0042] [SRC-0059] [SRC-0060]

## Validation Boundaries

- Dataset splits should test domain-relevant out-of-distribution behavior rather than only random in-distribution energy and force errors. [SRC-0042]
- Foundation-model claims should report useful simulation scale, memory behavior, throughput, and long-range limitations in addition to benchmark accuracy. [SRC-0059]
- Biology-focused MLIPs should be stratified across proteins, nucleic acids, solvents, ions, ligand binding, and interfaces; UBio-MolFM's protein gains do not remove its reported DNA and longer-timescale gaps. [SRC-0060]
- Benchmark-observable datasets require forward models, uncertainty, and convergence checks before using them as simulation validation targets. [SRC-0043]
- Response-property models need validation on the coupled spectroscopy workflow, including the underlying potential-energy model. [SRC-0065]
- Experimental energy-landscape datasets can expose conformational fluctuation behavior that native structure prediction or global stability does not capture. [SRC-0067]

## Links

- [[wiki/concepts/machine-learned-interatomic-potential-foundation-models]]
- [[wiki/concepts/machine-learning-potential-datasets]]
- [[wiki/concepts/protein-force-field-benchmark-datasets]]
- [[wiki/concepts/ubio-molfm-biological-molecular-foundation-model]]
- [[wiki/claims/CLM-0013-energy-force-error-is-not-downstream-md-reliability]]
- [[wiki/claims/CLM-0014-dataset-scale-does-not-replace-coverage-validation]]
- [[wiki/tensions/TEN-0008-dataset-scale-vs-downstream-validation]]
