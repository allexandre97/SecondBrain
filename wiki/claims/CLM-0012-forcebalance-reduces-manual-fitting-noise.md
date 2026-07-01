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
  - research/molecular-simulation/force-fields
tags:
  - claim
  - forcebalance
  - reproducibility
related:
  - "[[wiki/concepts/forcebalance]]"
  - "[[wiki/concepts/automated-force-field-training]]"
  - "[[wiki/concepts/force-field-training-from-experimental-observables]]"
  - "[[wiki/tensions/TEN-0006-observable-fitting-gain-vs-transferability-tradeoff]]"
sources:
  - SRC-0025
  - SRC-0014
  - SRC-0021
sensitivity: public
encryption: none
---

# ForceBalance Reduces Manual Fitting Noise

## Claim

ForceBalance-style optimization makes force-field fitting more systematic and reproducible by modularizing targets, engines, gradients, and regularized optimization, but it does not eliminate transferability limits imposed by the chosen data and functional form. [SRC-0025] [SRC-0014] [SRC-0021]

## Scope

This claim spans the original ForceBalance water-model paper and later observable-fitting applications in the scoped cluster. [SRC-0025] [SRC-0014] [SRC-0021]

## Evidence

- SRC-0025 presents ForceBalance as an automatic, systematic, reproducible framework and demonstrates convergence to TIP3P-FB and TIP4P-FB water models. [SRC-0025]
- SRC-0014 and SRC-0021 reuse ForceBalance-style optimization for SAXS and host-guest binding targets, respectively. [SRC-0014] [SRC-0021]

## Caveats

- A reproducible optimizer can reproducibly optimize a limited or biased target; validation still needs held-out observables and systems. [SRC-0014] [SRC-0021]

## Links

- [[wiki/sources/SRC-0025-building-force-fields-automatic-systematic-reproducible-approach]]
- [[wiki/sources/SRC-0014-lipid-force-field-saxs-reparameterization]]
- [[wiki/sources/SRC-0021-tuning-potential-functions-host-guest-binding-data]]
- [[wiki/concepts/forcebalance]]
- [[wiki/questions/force-field-training-validation-scope]]
