---
type: question
status: active
created: 2026-10-02
updated: 2026-10-15
question_status: partially-answered
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

Found during a 2026-10-02 FFRefine investigation into migrating from Molly's `AWHGrads` branch to `master`. Setup: water with the garnet force field (2661 atoms), PME with `grad_safe=true`, CPU, Float64, single thread, derivative of potential energy with respect to the shared O charge ($q=-0.9052$), on `AWHGrads`.

Measured values: Enzyme $9.415971\times10^{4}$ versus central finite difference $9.380141\times10^{4}$ ($h=10^{-6}$), relative error $3.8\times10^{-3}$, total. Split by component:

- real-space pair part: relative error $6.4\times10^{-9}$ (agrees)
- Ewald exclusion-correction part: relative error $8.4\times10^{-10}$ (agrees)
- PME reciprocal + self part: Enzyme $3.308299\times10^{5}$ versus finite difference $3.304716\times10^{5}$, relative error $1.1\times10^{-3}$ (disagrees)

Finite differences are trusted as the reference here because the energy is quadratic in the charges, so central finite differences carry no truncation error; rounding is estimated at about $10^{-9}$ relative. The disagreement is therefore localized to the PME reciprocal-space and self-energy terms' charge derivative, specifically, not to the real-space or exclusion-correction parts, and not to a generic Enzyme/PME incompatibility, since σ and DEXP α gradients through the identical PME system match finite differences at $10^{-10}$ and $10^{-9}$. This is FFRefine project evidence from a one-off probe script (not kept) run against FFRefine's own garnet force-field files; it has not been checked against a literature source or an independent PME implementation. At the time, the mismatch was believed to be branch-independent; the 2026-10-15 finding below shows that belief was itself an artifact of how the PME interaction was passed to Enzyme.

## Current Position

**Resolved on Molly master, for the probed case (CPU, Float64, water, single thread), with a probable but unverified cause on `AWHGrads`.** Molly master's PME stores mutable `charge_grid`/`recip_grid` fields that are written in place on every call, with custom Enzyme rules (in MollyEnzymeExt) for the FFTs that write into `charge_grid.dval`/`recip_grid.dval`. Enzyme therefore requires the PME interaction to be passed as `Duplicated(general_inters, Enzyme.make_zero(general_inters))`, as Molly's own tests do; passing it `Const`, which was FFRefine's pattern, throws `FieldError: type Const has no field dval` rather than silently mismatching. Once PME is passed `Duplicated` on master, the same water system's $\partial U/\partial q$ matches central finite differences to $10^{-10}$ (O) and $1.1\times10^{-9}$ (H), and the `AWHGrads`-era Enzyme values recorded above turn out to be the wrong ones (they differ from the master `Duplicated` result by $3.8\times10^{-3}$ and $5.7\times10^{-3}$ for O and H respectively, matching the originally observed mismatch). The working hypothesis, **not independently verified on `AWHGrads`**, is that `AWHGrads`' PME path lost part of the charge gradient through its own mutable grids being differentiated without an Enzyme shadow, analogous to master. See [[wiki/answers/molly-master-migration-constraints-for-ffrefine]], section F, for the full numbers and section H for the related Enzyme/PME thread-safety finding.

Not yet checked: GPU PME charge gradients, and hexane/ethanol PME charge gradients (only water was probed). The mismatch's practical relevance is unchanged: it matters for training charges (e.g. QEq latent charges) under PME, and does not affect FFRefine's current water and hexane runs, which default to reaction-field electrostatics rather than PME. A related but distinct PME dielectric check already exists in [[wiki/answers/ffrefine-average-observable-trainability-validation]]; that check measures a different quantity (dielectric permittivity gradient recovery) and does not resolve this one.

## Evidence timeline

- 2026-10-02: Original observation on Molly `AWHGrads`: Enzyme vs central finite-difference relative error $3.8\times10^{-3}$ for $\partial U/\partial q(\mathrm O)$ on water PME, localized to the PME reciprocal+self part ($1.1\times10^{-3}$ relative); real-space pair and exclusion-correction parts agreed to $10^{-9}$/$10^{-10}$. Believed at the time to be identical on Molly master. [[wiki/answers/molly-master-migration-constraints-for-ffrefine]]
- 2026-10-15: On Molly master (`623d314a`) plus the unmerged system-conversion PR branch (U2, head `0e4b8819`), the same water PME system reproduces the finite-difference value from 2026-10-02 ($9.380141\times10^4$) and the Enzyme/finite-difference mismatch resolves to $10^{-10}$ once PME is passed `Duplicated` instead of `Const`; passing it `Const` throws rather than silently disagreeing. `AWHGrads`' recorded Enzyme values differ from the master `Duplicated` result by the originally observed amount, consistent with (but not proof of) an un-shadowed-mutable-grid mechanism on `AWHGrads`; master cannot reproduce the wrong value, because `Const` throws there. [[wiki/answers/molly-master-migration-constraints-for-ffrefine]]

## Suggested next checks

- Verify the un-shadowed-mutable-grid hypothesis directly on `AWHGrads` (confirm whether its PME path mutates grids through a `Const`-like path without an Enzyme shadow, analogous to master).
- Check PME charge gradients on GPU (not yet probed on either branch).
- Check PME charge gradients for hexane and ethanol, not only water.

## Links

- [[wiki/answers/molly-master-migration-constraints-for-ffrefine]]
- [[wiki/answers/ffrefine-average-observable-trainability-validation]]
- [[wiki/concepts/awh-replay-force-field-optimization]]
