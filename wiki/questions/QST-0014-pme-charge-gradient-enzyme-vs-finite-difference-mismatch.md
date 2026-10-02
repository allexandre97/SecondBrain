---
type: question
status: active
created: 2026-10-02
updated: 2026-10-02
question_status: open
areas:
  - research
categories:
  - research/molecular-simulation/molecular-dynamics
  - research/molecular-simulation/force-fields
  - research/scientific-computing
tags:
  - question
  - pme
  - enzyme
  - autodiff
  - charge-gradient
  - molly
related:
  - "[[wiki/answers/molly-master-migration-constraints-for-ffrefine]]"
  - "[[wiki/answers/ffrefine-average-observable-trainability-validation]]"
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
sources: []
sensitivity: public
encryption: none
---

# PME Charge-Gradient Enzyme-vs-Finite-Difference Mismatch

## Question

Why does Molly's Enzyme-differentiated PME path give a potential-energy derivative with respect to an atomic charge that disagrees with central finite differences at about $3.8\times10^{-3}$ relative error, when the same PME system's σ and DEXP α gradients agree with finite differences at $10^{-10}$-$10^{-9}$?

## Context

Found during a 2026-10-02 FFRefine investigation into migrating from Molly's `AWHGrads` branch to `master` (the mismatch itself is identical on both branches, so it is not a migration artifact). Setup: water with the garnet force field (2661 atoms), PME with `grad_safe=true`, CPU, Float64, single thread, derivative of potential energy with respect to the shared O charge ($q=-0.9052$).

Measured values: Enzyme $9.415971\times10^{4}$ versus central finite difference $9.380141\times10^{4}$ ($h=10^{-6}$), relative error $3.8\times10^{-3}$, total. Split by component:

- real-space pair part: relative error $6.4\times10^{-9}$ (agrees)
- Ewald exclusion-correction part: relative error $8.4\times10^{-10}$ (agrees)
- PME reciprocal + self part: Enzyme $3.308299\times10^{5}$ versus finite difference $3.304716\times10^{5}$, relative error $1.1\times10^{-3}$ (disagrees)

Finite differences are trusted as the reference here because the energy is quadratic in the charges, so central finite differences carry no truncation error; rounding is estimated at about $10^{-9}$ relative. The disagreement is therefore localized to the PME reciprocal-space and self-energy terms' charge derivative, specifically, not to the real-space or exclusion-correction parts, and not to a generic Enzyme/PME incompatibility, since σ and DEXP α gradients through the identical PME system match finite differences at $10^{-10}$ and $10^{-9}$. This is FFRefine project evidence from a one-off probe script (not kept) run against FFRefine's own garnet force-field files; it has not been checked against a literature source or an independent PME implementation.

## Current Position

The wiki cannot currently identify the root cause. Candidates noted during the investigation: the Enzyme reverse-mode rule for the PME reciprocal/self terms, or the self-energy term's own charge derivative (the self-energy term is quadratic in charge and should be easy to differentiate by hand as a cross-check, but this was not done). The mismatch matters specifically for training charges (e.g. QEq latent charges) under PME; it does not affect FFRefine's current water and hexane runs, which default to reaction-field electrostatics rather than PME. A related but distinct PME dielectric check already exists in [[wiki/answers/ffrefine-average-observable-trainability-validation]]; that check measures a different quantity (dielectric permittivity gradient recovery) and does not resolve this one.

## Suggested next checks

- Differentiate the PME self-energy term by hand with respect to charge and compare against both Enzyme and finite differences in isolation, to localize the error further within "reciprocal + self".
- Re-run with a smaller, hand-checkable PME system (e.g. a handful of point charges) where an independent reference implementation or symbolic derivative is tractable.
- Check whether the error scales with mesh/grid resolution or Ewald splitting parameter, which would implicate a specific term in the reciprocal-space sum.
- Re-run with `grad_safe=false` and other PME configuration variants to see whether the mismatch is specific to the `grad_safe` code path.

## Links

- [[wiki/answers/molly-master-migration-constraints-for-ffrefine]]
- [[wiki/answers/ffrefine-average-observable-trainability-validation]]
- [[wiki/concepts/awh-replay-force-field-optimization]]
