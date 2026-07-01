---
type: concept
status: active
created: 2026-07-01
updated: 2026-07-01
areas:
  - research
categories:
  - research/machine-learning/molecular-modeling
  - research/molecular-simulation/force-fields
  - research/molecular-simulation/datasets
  - research/experimental-benchmarking
tags:
  - response-properties
  - dipole-moments
  - polarizabilities
  - spectroscopy
  - MACE
  - foundation-models
related:
  - "[[wiki/concepts/machine-learned-interatomic-potential-foundation-models]]"
  - "[[wiki/concepts/machine-learning-potential-datasets]]"
sources:
  - SRC-0065
sensitivity: public
encryption: none
---

# Molecular Response-Property Foundation Models

## Summary

Molecular response-property foundation models extend atomistic machine-learning beyond potential-energy surfaces to electronic response quantities such as dipole moments and polarizability tensors. SRC-0065 presents MACE-MDP as a foundation-style model for organic molecular dipoles and polarizabilities, intended to combine with MLIPs for IR and Raman spectroscopy. [SRC-0065]

## Key Points

- Potential-energy MLIPs model structures, energies, and forces, but dielectric response and vibrational spectroscopy also require electronic response properties. [SRC-0065]
- MACE-MDP predicts dipoles and full anisotropic polarizability tensors, while an external MLIP supplies geometries, normal modes, or molecular-dynamics trajectories. [SRC-0065]
- The SPICE-alpha dataset is a response-property extension of SPICE, adding first-principles polarizabilities to organic molecule, dimer, and solvated-complex structures. [SRC-0065]
- Equivariance matters because dipoles and polarizabilities are tensorial rather than scalar properties. [SRC-0065]
- Downstream spectroscopy accuracy can be limited by either the response-property model or the underlying potential-energy surface; in the reported trimer and crystal tests, force/frequency errors in the MLIP are a major limitation. [SRC-0065]

## Evidence

- SRC-0065 reports low random-split dipole and polarizability errors on SPICE-alpha and high IR/Raman spectral match scores for gas-phase molecules when MACE-MDP is combined with MACE-OFF23 models.
- SRC-0065 reports lower but still useful Raman spectral match scores for non-covalent trimers and encouraging anharmonic Raman polymorph identification for paracetamol crystals.

## Links

- [[wiki/sources/SRC-0065-mace-mdp-molecular-dipole-moments-polarizabilities]]
- [[wiki/concepts/machine-learned-interatomic-potential-foundation-models]]
- [[wiki/concepts/machine-learning-potential-datasets]]

## Caveats

- SRC-0065 is a preprint, not peer reviewed.
- Response-property models do not remove the need for a reliable potential-energy model when spectroscopy depends on vibrational frequencies, normal modes, or finite-temperature trajectories. [SRC-0065]

## Open Questions

- How much molecular-crystal, charged-system, or long-range response data is needed before zero-shot response-property models become reliable outside neutral organic training distributions?
- Which spectroscopy benchmarks best separate errors in response surfaces from errors in the underlying potential-energy surface?
