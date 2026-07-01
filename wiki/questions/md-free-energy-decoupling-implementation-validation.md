---
type: question
status: active
created: 2026-07-01
updated: 2026-07-01
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

## Links

- [[wiki/sources/SRC-0047-performing-solvation-free-energy-calculations-in-lammps-using]]
- [[wiki/claims/CLM-0023-decoupling-implementations-must-preserve-intramolecular-solute-terms]]
