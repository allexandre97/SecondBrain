---
type: concept
status: active
created: 2026-06-29
updated: 2026-06-29
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/machine-learning/scientific-modeling
tags:
  - automation
  - molecular-dynamics
related:
  - "[[concepts/garnet-force-field]]"
sources:
  - SRC-0003
sensitivity: public
encryption: none
---

# Automated Force Field Training

## Summary

Automated force-field training aims to learn molecular mechanics parameters and functional-form choices from data with less manual tuning than conventional force-field development. [SRC-0003]

## Key Points

- SRC-0003 frames manual force-field tuning as a source of limited transferability and weak reproducibility. [SRC-0003]
- Garnet combines DFT-derived force, potential-energy-difference, and charge data from SPICE, Espaloma, GEMS, and MACE-OFF with condensed-phase enthalpy data and protein NMR observables. [SRC-0003]
- Condensed-phase training includes enthalpies of vapourisation for water, methanol, and benzene, plus enthalpies of mixing for selected molecular pairs. [SRC-0003]
- Protein training uses GB3 NMR data through ensemble reweighting, with gradients reused across batches because the protein simulations are expensive. [SRC-0003]
- The paper argues that automated training enables systematic exploration of force-field functional forms. [SRC-0003]
- The approach is not fully universal yet; future work should expand validated species to nucleic acids, lipids, metals, carbohydrates, IDPs, and other polymers. [SRC-0003]

## Links

- [[sources/SRC-0003-training-a-force-field-from-scratch]]
- [[concepts/garnet-force-field]]
- [[concepts/double-exponential-potential]]
