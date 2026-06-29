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
  - garnet
  - molecular-dynamics
  - graph-neural-networks
related:
  - "[[concepts/automated-force-field-training]]"
  - "[[concepts/double-exponential-potential]]"
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
- The result should not be overgeneralized to universal coverage: the paper identifies validation gaps, possible GB3 overfitting, IDP over-compaction, occasional aromatic-ring planarity failures, and over-polarized charges. [SRC-0003]

## Links

- [[sources/SRC-0003-training-a-force-field-from-scratch]]
- [[concepts/automated-force-field-training]]
- [[concepts/double-exponential-potential]]
- [[questions/garnet-validation-scope]]
