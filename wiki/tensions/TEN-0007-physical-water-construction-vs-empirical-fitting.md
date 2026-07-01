---
type: tension
status: active
created: 2026-07-01
updated: 2026-07-01
tension_status: active
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
tags:
  - tension
  - water-models
  - force-field-fitting
related_claims: []
related_questions:
  - "[[wiki/questions/force-field-training-validation-scope]]"
sources:
  - SRC-0025
  - SRC-0027
  - SRC-0028
sensitivity: public
encryption: none
---

# Physical Water Construction vs Empirical Fitting

## Tension

Water-model development can start from empirical property fitting or from physically motivated charge-geometry construction, but both routes still require broad validation because rigid fixed-charge models have representational limits. [SRC-0025] [SRC-0027]

## Evidence

- SRC-0025 fits TIP3P-FB and TIP4P-FB with ForceBalance against water-property targets, emphasizing reproducible optimization. [SRC-0025]
- SRC-0027 builds OPC by first matching low-order electrostatic multipoles before fitting nonbonded behavior and validating bulk and hydration properties. [SRC-0027]
- SRC-0028 supplies the analytical point-charge construction details behind OPC. [SRC-0028]

## Current Status

Active. The routes are complementary rather than mutually exclusive: physical constraints can narrow the search space, while empirical targets remain necessary to test liquid and solvation behavior.

## Links

- [[wiki/sources/SRC-0025-building-force-fields-automatic-systematic-reproducible-approach]]
- [[wiki/sources/SRC-0027-building-water-models-different-approach-opc]]
- [[wiki/sources/SRC-0028-building-water-models-different-approach-supporting-information]]
- [[wiki/concepts/forcebalance]]
- [[wiki/concepts/opc-water-model]]
- [[wiki/questions/force-field-training-validation-scope]]
