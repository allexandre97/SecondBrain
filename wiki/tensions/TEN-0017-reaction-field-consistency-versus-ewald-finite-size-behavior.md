---
type: tension
status: active
created: 2026-08-05
updated: 2026-08-05
tension_status: active
areas:
  - research
categories:
  - research/molecular-simulation/molecular-dynamics
tags:
  - tension
  - dielectric-constant
  - finite-size-effects
  - reaction-field
  - Ewald-summation
related:
  - "[[wiki/concepts/dipole-moment-fluctuation-dielectric-constant]]"
  - "[[wiki/questions/QST-0003-reaction-field-versus-ewald-dielectric-limit]]"
sources:
  - SRC-0075
sensitivity: public
encryption: none
---

# Reaction-Field Consistency Versus Ewald Finite-Size Behavior

## Tension

Reaction-field simulations were internally consistent across the tested reaction-field dielectric values, but their dielectric constants were substantially higher than published Ewald results for the same Stockmayer state. Theory predicts agreement between reaction-field and Ewald-plus-reaction-field treatments in the thermodynamic limit, so the finite-size and numerical origins of the discrepancy remain open. [SRC-0075, §§5–6]

## Interpretation

The result is a warning against treating agreement across reaction-field parameters as sufficient validation. System-size scaling, exact long-range reference calculations, and careful matching of interaction conventions are still needed.

## Links

- [[wiki/sources/SRC-0075-dipole-moment-fluctuation-formulas-in-computer-simulations-of]]
- [[wiki/questions/QST-0003-reaction-field-versus-ewald-dielectric-limit]]
- [[wiki/concepts/particle-mesh-ewald-and-long-range-electrostatics]]
