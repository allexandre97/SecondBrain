---
type: concept
status: active
created: 2026-06-30
updated: 2026-06-30
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
tags:
  - forcebalance
  - parameter-optimization
  - force-field-training
sources:
  - SRC-0025
  - SRC-0026
  - SRC-0014
  - SRC-0021
  - SRC-0066
related:
  - "[[wiki/concepts/automated-force-field-training]]"
  - "[[wiki/concepts/force-field-training-from-experimental-observables]]"
  - "[[wiki/concepts/mlp-driven-bespoke-smirnoff-force-field-fitting]]"
sensitivity: public
encryption: none
---

# ForceBalance

## Summary

ForceBalance is a force-field parameter optimization framework that fits simulated properties to reference data using weighted objectives, regularization, and property-gradient information. [SRC-0025]

## Key Points

- ForceBalance was introduced to make force-field construction more automatic, systematic, and reproducible. [SRC-0025]
- It can combine experimental and theoretical reference data. [SRC-0025]
- It uses simulation engine interfaces to evaluate properties and optimization routines to update force-field parameters. [SRC-0025]
- Later ingested sources use ForceBalance variants for SAXS lipid fitting and host-guest binding-data fitting. [SRC-0014] [SRC-0021]
- `presto` is a contrasting modern OpenFF-oriented fitting workflow: it optimizes SMIRNOFF valence parameters against MLP energy/force labels rather than ForceBalance-style simulated property targets. [SRC-0066]

## Core equation

$$
\mathcal L(\theta)
=
\sum_i
\left[
\frac{y_i(\theta)-y_i^{\mathrm{ref}}}{\sigma_i}
\right]^2
+
R(\theta).
$$

[SRC-0025]

## Caveats

ForceBalance improves the reproducibility of the fitting workflow, but the fitted model is only as transferable as the chosen functional form, reference data, regularization, and validation set. [SRC-0025]

## Links

- [[wiki/sources/SRC-0025-building-force-fields-automatic-systematic-reproducible-approach]]
- [[wiki/sources/SRC-0014-lipid-force-field-saxs-reparameterization]]
- [[wiki/sources/SRC-0021-tuning-potential-functions-host-guest-binding-data]]
- [[wiki/concepts/force-field-training-from-experimental-observables]]
- [[wiki/concepts/mlp-driven-bespoke-smirnoff-force-field-fitting]]
