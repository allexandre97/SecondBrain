---
type: tension
status: active
created: 2026-07-01
updated: 2026-07-01
tension_status: active
areas:
  - research
categories:
  - research/molecular-simulation/molecular-dynamics
tags:
  - tension
  - autodiff
  - constraints
  - virial
  - pressure-tensor
related_claims:
  - "[[wiki/claims/CLM-0024-force-based-virials-generalize-pressure-and-stress-to-many-body-md]]"
  - "[[wiki/claims/CLM-0025-constraints-and-long-range-electrostatics-change-pressure-tensor-accounting]]"
related_questions:
  - "[[wiki/questions/md-virial-pressure-implementation-for-autodiff-and-many-body-potentials]]"
sources:
  - SRC-0048
  - SRC-0051
  - SRC-0052
sensitivity: public
encryption: none
---

# Analytic Constraint Virials vs Autodiff Energy Gradients

## Tension

Autodiff encourages deriving forces and virials from differentiable energy expressions, but constrained MD and some pressure-tensor contributions introduce analytic force, multiplier, or cell-derivative terms that may not be represented by a simple unconstrained energy gradient. [SRC-0048] [SRC-0051] [SRC-0052]

## Evidence

- SRC-0048 emphasizes force-based virials for arbitrary many-body potentials under periodic boundary conditions rather than relying on pair energy decompositions. [SRC-0048]
- SRC-0051 separates constraint and potential contributions in a pressure tensor method for periodic constrained systems with Ewald electrostatics. [SRC-0051]
- SRC-0052 writes constrained equations of motion with $B^T\lambda$ terms, making constraint forces explicit in the dynamics. [SRC-0052, eq. 5]

## Current Status

Active. The implementation issue is whether the MD engine exposes pressure and virial as pure autodiff products, analytic algorithm terms, or an explicit composition of both. [SRC-0048] [SRC-0051] [SRC-0052]

## Links

- [[wiki/sources/SRC-0048-general-formulation-of-pressure-and-stress-tensor-for]]
- [[wiki/sources/SRC-0051-a-general-pressure-tensor-calculation-for-molecular-dynamics]]
- [[wiki/sources/SRC-0052-lincs-a-linear-constraint-solver-for-molecular-simulations]]
- [[wiki/questions/md-virial-pressure-implementation-for-autodiff-and-many-body-potentials]]
