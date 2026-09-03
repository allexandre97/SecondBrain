---
type: tension
status: active
created: 2026-07-01
updated: 2026-09-03
tension_status: active
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/experimental-benchmarking
tags:
  - tension
  - force-field-training
  - transferability
related_claims:
  - "[[wiki/claims/CLM-0009-observable-fitting-needs-held-out-validation]]"
  - "[[wiki/claims/CLM-0012-forcebalance-reduces-manual-fitting-noise]]"
  - "[[wiki/claims/CLM-0042-lennard-jones-refinement-outperforms-charge-scaling-after-shared-osmometry-fit]]"
related_questions:
  - "[[wiki/questions/force-field-training-validation-scope]]"
sources:
  - SRC-0014
  - SRC-0021
  - SRC-0025
  - SRC-0078
sensitivity: public
encryption: none
---

# Observable Fitting Gain vs Transferability Tradeoff

## Tension

Directly fitting force-field parameters to experimental observables can improve the fitted target while exposing or creating transferability failures on other observables or systems. Distinct parameterizations can also fit the same target yet behave differently after transfer. [SRC-0014] [SRC-0021] [SRC-0078]

## Evidence

- SRC-0014 improves SAXS agreement for the training-like lipid system and selected solvent-stress tests, but the source emphasizes that SAXS alone has transferability limits. [SRC-0014]
- SRC-0021 improves host-guest binding free energies after OBC2 cavity-radius optimization, but the same radii make hydration free energies excessively favorable. [SRC-0021]
- SRC-0025 shows how ForceBalance can make optimization systematic, but systematic optimization still depends on the selected training data and regularization. [SRC-0025]
- SRC-0078 obtains similarly successful osmometry fits through charge scaling and Lennard-Jones refinement, but the former does not improve the held-out 16-IDR FRET benchmark while the latter does. Calibration agreement therefore underdetermines transfer quality. [SRC-0078]

## Current Status

Active. The scoped cluster supports observable-driven fitting, but it also argues for held-out observables, held-out systems, and regularization before accepting transferability.

## Links

- [[wiki/sources/SRC-0014-lipid-force-field-saxs-reparameterization]]
- [[wiki/sources/SRC-0021-tuning-potential-functions-host-guest-binding-data]]
- [[wiki/sources/SRC-0025-building-force-fields-automatic-systematic-reproducible-approach]]
- [[wiki/sources/SRC-0078-predictive-all-atom-simulations-of-disordered-proteins-and]]
- [[wiki/concepts/osmometry-guided-force-field-optimization]]
- [[wiki/questions/force-field-training-validation-scope]]
