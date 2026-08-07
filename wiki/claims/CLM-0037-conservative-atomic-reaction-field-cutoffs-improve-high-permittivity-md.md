---
type: claim
status: active
created: 2026-08-05
updated: 2026-08-05
claim_status: supported
claim_scope: source-specific
areas:
  - research
categories:
  - research/molecular-simulation/molecular-dynamics
  - research/molecular-simulation/force-fields
tags:
  - claim
  - reaction-field
  - atomic-cutoff
  - energy-conservation
  - validation
related:
  - "[[wiki/concepts/conservative-reaction-field-cutoff-schemes]]"
  - "[[wiki/concepts/dipole-moment-fluctuation-dielectric-constant]]"
sources:
  - SRC-0077
sensitivity: public
encryption: none
---

# Conservative Atomic Reaction-Field Cutoffs Improve High-Permittivity MD

## Claim

For high-permittivity liquids, reaction-field electrostatics with atomic truncation plus a force- and curvature-regularizing shift or switch can reduce cutoff artifacts while preserving conservative dynamics and agreement with lattice-sum reference properties. [SRC-0077]

## Evidence

Across 57 organic liquids, the selected 4–6 SH and 0.75 SW RF/AT schemes improved or maintained agreement with lattice-sum calculations for density, vaporization enthalpy, dielectric permittivity, and self-diffusion relative to standard RF/AT. [SRC-0077, §§4–5]

For SPC water and other model liquids, the modifications removed or reduced cutoff artifacts in radial distribution functions, dipole-orientation correlations, and distance-dependent Kirkwood factors. [SRC-0077, §§2 and 4]

## Scope and caveats

The result is a validation against lattice-sum references for GROMOS-compatible organic-liquid models, not a guarantee for all force fields, charged biomolecules, interfaces, or nonuniform dielectric environments. [SRC-0077]

## Links

- [[wiki/concepts/conservative-reaction-field-cutoff-schemes]]
- [[wiki/sources/SRC-0077-reaction-field-electrostatics-in-molecular-dynamics-simulations-development]]
