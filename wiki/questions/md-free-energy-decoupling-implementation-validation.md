---
type: question
status: active
created: 2026-07-01
updated: 2026-10-02
question_status: open
areas:
  - research
categories:
  - research/molecular-simulation/free-energy
tags:
  - question
  - decoupling
  - solvation-free-energy
  - validation
related:
  - "[[wiki/concepts/solvation-free-energy-decoupling-in-lammps]]"
  - "[[wiki/claims/CLM-0023-decoupling-implementations-must-preserve-intramolecular-solute-terms]]"
  - "[[wiki/answers/molly-master-migration-constraints-for-ffrefine]]"
sources:
  - SRC-0047
sensitivity: public
encryption: none
---

# MD Free-Energy Decoupling Implementation Validation

## Question

What minimal validation suite should a Molly/Enzyme/MD decoupling implementation pass to show that solute-solvent staging preserves intramolecular solute terms and produces correct $\langle dU/d\lambda\rangle_\lambda$ integrands? [SRC-0047]

## Context

SRC-0047 validates a LAMMPS overlay correction against GROMACS for ethanol and biphenyl hydration free energies. That is strong enough for the demonstrated implementation mechanism, but it does not define a reusable validation suite for new engines, autodiff force paths, charge-scaling APIs, or estimator variants beyond thermodynamic integration. [SRC-0047]

## Current Position

Use both endpoint energy checks and integrand checks. A useful suite should compare intramolecular Coulomb energy before and after charge scaling, verify the overlay formula, and compare staged $\langle dU/d\lambda\rangle_\lambda$ values against an independent implementation for small systems. [SRC-0047]

## Project evidence: Molly backend comparison (2026-10-02)

An FFRefine investigation into migrating from Molly's `AWHGrads` branch to Molly's `master` branch probed exactly this kind of implementation detail on an ethanol-in-water-plus-vacuum alchemical setup (soft-core DEXP sterics, scaled reaction-field/plain Coulomb electrostatics, solute given the Insert role, `DefaultLambdaScheduler`, λ from 1 to 0). It found that "scale charges" is implemented differently by the two branches in a way that changes intermediate-λ energies while leaving endpoints unchanged:

- `AWHGrads` scales each solute charge individually, so a solute-solute pair scales as $\lambda_e^2$, where $\lambda_e$ is the electrostatic coupling; master scales the pair energy by the pair λ, so the same pair scales as $\lambda_e$. At λ = 0.75 this gave solvated energies of −62427.81 kJ/mol (`AWHGrads`) versus −62441.01 kJ/mol (master), and vacuum energies of 11.909 versus 8.083 kJ/mol. Both branches annihilate intramolecular solute electrostatics rather than decoupling them, consistent with the overlay-correction caveat in [[wiki/claims/CLM-0023-decoupling-implementations-must-preserve-intramolecular-solute-terms]] — neither branch's default charge-scaling behaviour preserves intramolecular solute Coulomb terms without an explicit choice to do so.
- Master's `DefaultLambdaScheduler` defaults to `intraLJ=false` (annihilating solute-solute steric pairs), while `AWHGrads` kept them on (decoupling); `intraLJ=true` reproduces `AWHGrads` exactly at λ > 0.
- `AWHGrads`' `LJZeroShortcut` skips pairs touching any atom at λ = 0, so intra-solute steric (DEXP) interactions are discontinuous exactly at the λ = 0 endpoint (about 0.05 kJ/mol for ethanol in vacuum: 15.786 at λ = 0 versus 15.736 at λ = 0.25 and 0.5); master with `intraLJ=true` is continuous.
- Alchemical role indices were also renumbered between branches (`AWHGrads`: Core=0, Insert=1, Delete=2; master: Env=0, Core=1, CoreI=2, CoreD=3, Insert=4, Delete=5), so serialized alchemical states are not portable between them.

This is FFRefine project evidence from diffs and small Julia probes against FFRefine's own force-field files on 2026-10-02 (probe scripts not kept), not a new literature claim; it generalizes the question's validation concern beyond LAMMPS/SRC-0047 to a second, independent engine pair (two Molly branches), and shows that intermediate-λ Hamiltonian parity, not just endpoint parity, must be checked whenever a decoupling implementation's internal charge- or role-scaling convention changes. See [[wiki/answers/molly-master-migration-constraints-for-ffrefine]] for the full comparison.

## Links

- [[wiki/sources/SRC-0047-performing-solvation-free-energy-calculations-in-lammps-using]]
- [[wiki/claims/CLM-0023-decoupling-implementations-must-preserve-intramolecular-solute-terms]]
- [[wiki/answers/molly-master-migration-constraints-for-ffrefine]]
