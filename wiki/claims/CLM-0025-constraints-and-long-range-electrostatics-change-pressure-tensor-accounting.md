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
  - research/molecular-simulation/molecular-dynamics
tags:
  - claim
  - constraints
  - pressure-tensor
  - virial
  - Ewald-summation
related:
  - "[[wiki/concepts/md-pressure-and-stress-tensor-calculation]]"
  - "[[wiki/concepts/molecular-dynamics-constraint-solvers]]"
  - "[[wiki/tensions/TEN-0013-analytic-constraint-virials-vs-autodiff-energy-gradients]]"
sources:
  - SRC-0048
  - SRC-0051
  - SRC-0052
sensitivity: public
encryption: none
---

# Constraints and Long-Range Electrostatics Change Pressure Tensor Accounting

## Claim

Constrained MD pressure and virial calculations must account for constraint forces and long-range electrostatic terms explicitly; a force expression that is correct for unconstrained short-range interactions can miss implementation-relevant pressure tensor contributions. [SRC-0051] [SRC-0052] [SRC-0048]

## Evidence

- SRC-0051 separates potential and constraint contributions in a pressure-tensor method for periodic systems with holonomic constraints and Ewald electrostatics. [SRC-0051]
- SRC-0052 formulates constraints through gradients and Lagrange multipliers in the constrained equations of motion, giving the mathematical objects that can contribute forces beyond unconstrained potentials. [SRC-0052, eq. 5]
- SRC-0048 provides force-based virial forms under periodic boundary conditions, showing that implementation-level image and force bookkeeping is part of the pressure/stress definition. [SRC-0048]

## Implementation Use

For Molly/Enzyme/MD work, constraint solvers should not be treated as postprocessing that leaves pressure untouched. If constrained dynamics, reciprocal electrostatics, and differentiable energy paths coexist, the pressure/virial API needs an explicit policy for which terms are analytic, which are differentiated, and how constraint impulses or multipliers enter the tensor. [SRC-0051] [SRC-0052]

## Caveats

The claim is limited because SRC-0052 is primarily a constraint-solver paper, not a pressure-tensor paper; the cross-link is about the constraint-force objects needed by pressure accounting. [SRC-0051] [SRC-0052]

## Links

- [[wiki/sources/SRC-0048-general-formulation-of-pressure-and-stress-tensor-for]]
- [[wiki/sources/SRC-0051-a-general-pressure-tensor-calculation-for-molecular-dynamics]]
- [[wiki/sources/SRC-0052-lincs-a-linear-constraint-solver-for-molecular-simulations]]
- [[wiki/concepts/md-pressure-and-stress-tensor-calculation]]
- [[wiki/concepts/molecular-dynamics-constraint-solvers]]
