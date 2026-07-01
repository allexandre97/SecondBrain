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
  - research/machine-learning/molecular-modeling
  - research/experimental-benchmarking
tags:
  - claim
  - datasets
  - validation
  - machine-learning-potentials
related:
  - "[[wiki/concepts/machine-learning-potential-datasets]]"
  - "[[wiki/concepts/machine-learned-interatomic-potential-foundation-models]]"
  - "[[wiki/tensions/TEN-0008-dataset-scale-vs-downstream-validation]]"
sources:
  - SRC-0042
  - SRC-0044
  - SRC-0059
  - SRC-0060
sensitivity: public
encryption: none
---

# Dataset Scale Does Not Replace Coverage and Validation

## Claim

For molecular ML potentials, larger datasets do not by themselves solve transferability; coverage, label fidelity, long-range physics, benchmark design, and downstream simulation validation remain separate requirements. [SRC-0042] [SRC-0044] [SRC-0059] [SRC-0060]

## Scope

This claim compares dataset and validation logic across SPICE, OMol25, foundation-model MLIP perspective work, and UBio-MolFM. It does not rank the datasets or claim that one coverage strategy dominates all others. [SRC-0042] [SRC-0044] [SRC-0059]

## Evidence

- SPICE defines dataset usefulness through chemical-space coverage, conformational-space coverage, forces, level of theory, and extensibility, not just conformation count. [SRC-0044]
- OMol25 expands scale and diversity while also adding composition-based splits and task-oriented evaluations for chemistry use cases. [SRC-0042]
- SRC-0059 argues that data size, data fidelity, model expressivity, optimization, long-range behavior, and benchmarking must improve together. [SRC-0059, sections 2 and 6]
- UBio-MolFM treats OMol25 as useful but insufficient for biological macromolecules, adding UBio-Mol26 while still identifying nucleic-acid and longer-timescale validation gaps. [SRC-0060]

## Caveats

- Dataset size can still be essential when the relevant domain is underrepresented; the claim is that scale is not a substitute for coverage and validation, not that scale is unimportant. [SRC-0059]

## Links

- [[wiki/sources/SRC-0042-the-open-molecules-2025-omol25-dataset-evaluations-and]]
- [[wiki/sources/SRC-0044-spice-a-dataset-of-drug-like-molecules-and]]
- [[wiki/sources/SRC-0059-six-open-questions-in-machine-learned-interatomic-potential]]
- [[wiki/sources/SRC-0060-ubio-molfm-universal-molecular-foundation-model]]
- [[wiki/concepts/machine-learning-potential-datasets]]
- [[wiki/tensions/TEN-0008-dataset-scale-vs-downstream-validation]]
