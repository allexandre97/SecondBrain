---
type: claim
status: active
created: 2026-07-01
updated: 2026-07-01
claim_status: limited
claim_scope: local
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/machine-learning/scientific-modeling
tags:
  - claim
  - machine-learning-force-fields
  - simulation-stability
related:
  - "[[wiki/concepts/stability-aware-mlff-training]]"
  - "[[wiki/concepts/automated-force-field-training]]"
  - "[[wiki/questions/force-field-training-validation-scope]]"
sources:
  - SRC-0024
sensitivity: public
encryption: none
---

# Stability-Aware MLFF Training Targets MD Stability

## Claim

StABlE treats downstream molecular-dynamics stability and observable recovery as training targets, not merely as post hoc checks after energy and force fitting. [SRC-0024]

## Scope

This claim is local to SRC-0024 and should not be generalized to every MLFF architecture or simulation regime without additional validation. [SRC-0024]

## Evidence

- SRC-0024 alternates MD-based instability discovery with observable-matching updates through a differentiable Boltzmann Estimator. [SRC-0024]
- The paper reports improved simulation stability and observable agreement across organic molecules, alanine tetrapeptide, and water examples. [SRC-0024]

## Caveats

- Stability-aware training still depends on the systems, observables, architectures, and simulation conditions used during training and validation. [SRC-0024]

## Links

- [[wiki/sources/SRC-0024-stable-training-machine-learning-force-fields-boltzmann-estimators]]
- [[wiki/concepts/stability-aware-mlff-training]]
- [[wiki/questions/force-field-training-validation-scope]]
