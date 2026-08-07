---
type: question
status: active
created: 2026-08-05
updated: 2026-08-05
question_status: open
areas:
  - research
categories:
  - research/molecular-simulation/molecular-dynamics
  - research/molecular-simulation/force-fields
tags:
  - question
  - energy-conservation
  - virial
  - reaction-field
  - cutoff
related:
  - "[[wiki/concepts/conservative-reaction-field-cutoff-schemes]]"
  - "[[wiki/concepts/md-pressure-and-stress-tensor-calculation]]"
sources:
  - SRC-0077
sensitivity: public
encryption: none
---

# Corrected Energy and Virial Policy for Modified Cutoffs

## Question

When a shifted or switched reaction-field/LJ interaction is used in production MD, which modified, corrected, and virial quantities should be exposed separately for dynamics, pressure, free energies, and reported thermodynamic observables?

## Evidence and current position

The modified potential is the conservative force model, while the long-range constant energy term has no force or virial and can be removed in corrected-energy postprocessing. For LJ modifications, the paper finds that adding a virial correction can improve density and vaporization-enthalpy agreement, but does not adopt a universal policy. [SRC-0077, §§2.3, 2.6, and 4.2]

## Links

- [[wiki/sources/SRC-0077-reaction-field-electrostatics-in-molecular-dynamics-simulations-development]]
- [[wiki/concepts/conservative-reaction-field-cutoff-schemes]]
- [[wiki/concepts/md-pressure-and-stress-tensor-calculation]]
