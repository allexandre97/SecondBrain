---
type: claim
status: active
created: 2026-07-01
updated: 2026-07-01
claim_status: supported
claim_scope: cross-source
areas:
  - research
categories:
  - research/molecular-simulation/molecular-dynamics
tags:
  - claim
  - pressure-tensor
  - stress-tensor
  - virial
  - many-body-potentials
related:
  - "[[wiki/concepts/md-pressure-and-stress-tensor-calculation]]"
  - "[[wiki/questions/md-virial-pressure-implementation-for-autodiff-and-many-body-potentials]]"
  - "[[wiki/tensions/TEN-0013-analytic-constraint-virials-vs-autodiff-energy-gradients]]"
sources:
  - SRC-0048
  - SRC-0051
sensitivity: public
encryption: none
---

# Force-Based Virials Generalize Pressure and Stress to Many-Body MD

## Claim

Pressure and stress tensor implementations for many-body MD should be based on force/virial expressions that match the actual potential and boundary bookkeeping, because pair-decomposition formulas do not automatically generalize to arbitrary many-body interactions. [SRC-0048] [SRC-0051]

## Evidence

- SRC-0048 derives atom-cell, atom, and group virial forms under periodic boundary conditions and frames the result as implementation-ready because the formulas use forces rather than pair-energy decompositions. [SRC-0048]
- SRC-0048 explicitly treats arbitrary many-body interatomic potentials, where assigning pressure by pair terms can be ill-defined. [SRC-0048]
- SRC-0051 shows that pressure tensor calculations in realistic periodic molecular systems may need mixed mechanical and thermodynamic contributions, especially when constraints and Ewald electrostatics are present. [SRC-0051]

## Implementation Use

For differentiable or many-body potentials, the virial expression should be chosen at the same abstraction level as the force calculation. Pairwise virial shortcuts are implementation assumptions, not neutral rewrites, when the potential is many-body, constrained, or coupled to periodic-image bookkeeping. [SRC-0048] [SRC-0051]

## Caveats

SRC-0048 supplies the general force-based framework, while SRC-0051 is motivated by a constrained crystalline polymer case. Implementation details still require the full tensor formulas in the sources. [SRC-0048] [SRC-0051]

## Links

- [[wiki/sources/SRC-0048-general-formulation-of-pressure-and-stress-tensor-for]]
- [[wiki/sources/SRC-0051-a-general-pressure-tensor-calculation-for-molecular-dynamics]]
- [[wiki/concepts/md-pressure-and-stress-tensor-calculation]]
