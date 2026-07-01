---
type: question
status: active
created: 2026-07-01
updated: 2026-07-01
question_status: open
areas:
  - research
categories:
  - research/molecular-simulation/molecular-dynamics
tags:
  - question
  - pressure-tensor
  - virial
  - autodiff
  - constraints
related:
  - "[[wiki/concepts/md-pressure-and-stress-tensor-calculation]]"
  - "[[wiki/concepts/molecular-dynamics-constraint-solvers]]"
  - "[[wiki/claims/CLM-0024-force-based-virials-generalize-pressure-and-stress-to-many-body-md]]"
  - "[[wiki/claims/CLM-0025-constraints-and-long-range-electrostatics-change-pressure-tensor-accounting]]"
  - "[[wiki/tensions/TEN-0013-analytic-constraint-virials-vs-autodiff-energy-gradients]]"
sources:
  - SRC-0048
  - SRC-0050
  - SRC-0051
  - SRC-0052
sensitivity: public
encryption: none
---

# MD Virial/Pressure Implementation for Autodiff and Many-Body Potentials

## Question

How should Molly/Enzyme/MD expose virial and pressure tensor calculation when forces may come from many-body potentials, long-range electrostatics, and constraint solvers rather than a simple pairwise energy decomposition? [SRC-0048] [SRC-0051] [SRC-0052]

## Context

SRC-0048 argues for force-based virial forms that generalize to arbitrary many-body potentials under periodic boundary conditions. SRC-0051 shows that constrained periodic molecular systems with Ewald electrostatics may need hybrid pressure-tensor accounting. SRC-0052 provides the Lagrange-multiplier constraint-force structure that can matter for virials, while SRC-0050 records reciprocal-space electrostatics terms whose virials must also be handled. [SRC-0048] [SRC-0051] [SRC-0052] [SRC-0050]

## Current Position

The implementation decision is unresolved. A defensible API should separate force accumulation, cell/strain derivatives, constraint contributions, and reciprocal-space virial terms, while making clear which contributions are obtained by autodiff and which are analytic algorithmic terms. [SRC-0048] [SRC-0051] [SRC-0052]

## Links

- [[wiki/sources/SRC-0048-general-formulation-of-pressure-and-stress-tensor-for]]
- [[wiki/sources/SRC-0050-a-smooth-particle-mesh-ewald-method]]
- [[wiki/sources/SRC-0051-a-general-pressure-tensor-calculation-for-molecular-dynamics]]
- [[wiki/sources/SRC-0052-lincs-a-linear-constraint-solver-for-molecular-simulations]]
- [[wiki/claims/CLM-0024-force-based-virials-generalize-pressure-and-stress-to-many-body-md]]
- [[wiki/claims/CLM-0025-constraints-and-long-range-electrostatics-change-pressure-tensor-accounting]]
