---
type: question
status: active
created: 2026-07-01
updated: 2026-07-01
areas:
  - research
categories:
  - research/molecular-simulation/free-energy
  - research/computational-drug-discovery
  - research/experimental-benchmarking
tags:
  - rbfe
  - validation
  - benchmarking
  - drug-discovery
related:
  - "[[wiki/concepts/relative-binding-free-energy-benchmarking]]"
  - "[[wiki/concepts/free-energy-estimation]]"
  - "[[wiki/claims/CLM-0017-experimental-reproducibility-bounds-rbfe-error-interpretation]]"
  - "[[wiki/claims/CLM-0018-public-rbfe-benchmarks-can-be-easier-than-private-active-project-data]]"
  - "[[wiki/claims/CLM-0019-edgewise-rbfe-metrics-can-overstate-arbitrary-comparison-quality]]"
  - "[[wiki/tensions/TEN-0010-rbfe-benchmark-success-vs-prospective-use]]"
sources:
  - SRC-0045
  - SRC-0046
  - SRC-0061
  - SRC-0062
sensitivity: public
encryption: none
---

# RBFE Benchmark Prospective Use Scope

## Question

What benchmark evidence is sufficient to trust an RBFE protocol for prospective computational drug-discovery use?

## Current Position

The cluster supports a qualified answer: prospective trust requires more than a public retrospective RMSE. It needs experimental reproducibility context, public/private benchmark separation, both edgewise and all-to-all metrics, setup-quality diagnostics, transformation-class coverage, and transparent protocol differences when comparing methods. [SRC-0046] [SRC-0061] [SRC-0062]

## Validation Boundaries

- Experimental assay reproducibility constrains how precisely RBFE errors can be interpreted. [SRC-0046]
- Public curated systems and private active-project datasets should be reported separately, because private datasets expose more assay, setup, transformation, and ambiguity issues. [SRC-0061]
- Edgewise metrics should be paired with all-to-all pairwise or ranking metrics when the intended use is arbitrary ligand prioritization. [SRC-0061]
- Cross-protocol comparisons, such as default OpenFE versus published FEP+, must disclose preparation, force-field, sampling, enhanced-water, and tuning differences. [SRC-0061] [SRC-0062]
- Force-field tuning to binding data should be checked against other observables, because binding gains can conflict with hydration-free-energy transfer. [SRC-0021]

## Links

- [[wiki/concepts/relative-binding-free-energy-benchmarking]]
- [[wiki/concepts/free-energy-estimation]]
- [[wiki/questions/force-field-training-validation-scope]]
- [[wiki/claims/CLM-0017-experimental-reproducibility-bounds-rbfe-error-interpretation]]
- [[wiki/claims/CLM-0018-public-rbfe-benchmarks-can-be-easier-than-private-active-project-data]]
- [[wiki/claims/CLM-0019-edgewise-rbfe-metrics-can-overstate-arbitrary-comparison-quality]]
- [[wiki/tensions/TEN-0010-rbfe-benchmark-success-vs-prospective-use]]
