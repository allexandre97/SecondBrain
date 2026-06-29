---
type: concept
status: active
created: 2026-06-29
updated: 2026-06-29
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
tags:
  - nonbonded-potentials
  - molecular-dynamics
related:
  - "[[concepts/garnet-force-field]]"
sources:
  - SRC-0003
sensitivity: public
encryption: none
---

# Double Exponential Potential

## Summary

The double exponential potential is the non-bonded potential used by Garnet as an alternative to Lennard-Jones interactions. [SRC-0003]

## Key Points

- In SRC-0003, Lennard-Jones training became unstable when simulations were introduced during training, for example when fitting condensed-phase properties. [SRC-0003]
- The double exponential potential trained effectively and is described as flexible for intermolecular interactions because it uses exponential repulsion and a flexible attractive term. [SRC-0003]
- The potential adds global parameters beyond atom-level sigma and epsilon values and remains practical in OpenMM through custom forces. [SRC-0003]
- The authors do not claim Lennard-Jones is generally unstable; the claim is specific to their automated training pipeline. [SRC-0003]
- Future functional-form work could explore other bonded and non-bonded terms, soft-core potentials, polarization, and charge flux. [SRC-0003]

## Links

- [[sources/SRC-0003-training-a-force-field-from-scratch]]
- [[concepts/garnet-force-field]]
- [[concepts/automated-force-field-training]]
