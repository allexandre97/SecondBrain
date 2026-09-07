---
type: concept
status: active
created: 2026-06-29
updated: 2026-09-07
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/biomolecules/proteins
  - research/machine-learning/molecular-modeling
tags:
  - garnet
  - molecular-dynamics
  - graph-neural-networks
related:
  - "[[wiki/concepts/automated-force-field-training]]"
  - "[[wiki/concepts/double-exponential-potential]]"
sources:
  - SRC-0003
sensitivity: public
encryption: none
---

# Garnet Force Field

## Summary

Garnet is a graph-neural-network force field that predicts molecular mechanics parameters for arbitrary supported molecules from topology, using continuous atom typing instead of manually assigned atom types. [SRC-0003]

## Key Points

- Garnet is trained on quantum mechanical data, condensed-phase properties, and protein NMR data. [SRC-0003]
- It is intended to cover proteins and small molecules with one automated parameterization scheme. [SRC-0003]
- The graph neural network maps molecular topology to continuous atom, bond, angle, and torsion embeddings, then predicts molecular mechanics parameters rather than relying on fixed human-assigned atom types. [SRC-0003]
- Water is not treated as a fixed legacy model; its parameters are trained by Garnet. [SRC-0003]
- The authors report competitive benchmark performance across small molecules, proteins, protein complexes, IDPs, water, and selected RBFE tasks. [SRC-0003]
- Revised small-molecule tests show that the over-polarized charges affect both dipole magnitude and orientation. [SRC-0003, section "Small molecule benchmark"]
- On 12 condensed-phase test molecules, Garnet tends to overestimate density and enthalpy of vapourisation and has larger RMSEs than OpenFF 2.2.1, consistent with attractive intermolecular interactions being too strong. [SRC-0003, section "Small molecule benchmark"]
- The result should not be overgeneralized to universal coverage: the paper identifies validation gaps, possible GB3 overfitting, IDP over-compaction, occasional aromatic-ring planarity failures, over-polarized charges, condensed-phase overbinding, and RBFE testing on only 8 of 58 public benchmark systems. [SRC-0003]

## Links

- [[wiki/sources/SRC-0003-training-a-force-field-from-scratch]]
- [[wiki/concepts/automated-force-field-training]]
- [[wiki/concepts/double-exponential-potential]]
- [[wiki/questions/garnet-validation-scope]]
- [[wiki/sources/SRC-0044-spice-a-dataset-of-drug-like-molecules-and]]
