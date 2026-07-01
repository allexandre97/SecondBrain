---
type: tension
status: active
created: 2026-07-01
updated: 2026-07-01
tension_status: active
areas:
  - research
categories:
  - research/molecular-simulation/datasets
  - research/machine-learning/molecular-modeling
  - research/experimental-benchmarking
tags:
  - tension
  - datasets
  - validation
  - foundation-models
related_claims:
  - "[[wiki/claims/CLM-0013-energy-force-error-is-not-downstream-md-reliability]]"
  - "[[wiki/claims/CLM-0014-dataset-scale-does-not-replace-coverage-validation]]"
related_questions:
  - "[[wiki/questions/mlip-foundation-model-validation-scope]]"
sources:
  - SRC-0042
  - SRC-0044
  - SRC-0059
  - SRC-0060
sensitivity: public
encryption: none
---

# Dataset Scale vs Downstream Validation

## Tension

Large molecular datasets make broad MLIP training possible, but downstream reliability still depends on coverage, label fidelity, long-range physics, benchmark design, and task-specific simulation validation. [SRC-0042] [SRC-0044] [SRC-0059] [SRC-0060]

## Evidence

- SPICE and OMol25 expand training data in different ways, but both still define intended chemistry and coverage limits. [SRC-0044] [SRC-0042]
- SRC-0059 warns against treating larger datasets, larger models, or single benchmark metrics as sufficient evidence for foundation-model quality. [SRC-0059]
- UBio-MolFM adds biology-focused data and downstream tests because OMol25-style molecular breadth does not by itself validate biomolecular MD, while its own limitations still require class-specific follow-up. [SRC-0060]

## Current Status

Active. The cluster supports dataset scaling as necessary infrastructure while rejecting scale-only validation.

## Links

- [[wiki/sources/SRC-0042-the-open-molecules-2025-omol25-dataset-evaluations-and]]
- [[wiki/sources/SRC-0044-spice-a-dataset-of-drug-like-molecules-and]]
- [[wiki/sources/SRC-0059-six-open-questions-in-machine-learned-interatomic-potential]]
- [[wiki/sources/SRC-0060-ubio-molfm-universal-molecular-foundation-model]]
- [[wiki/questions/mlip-foundation-model-validation-scope]]
