---
type: question
status: active
created: 2026-06-29
updated: 2026-06-29
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
tags:
  - validation
  - garnet
related:
  - "[[concepts/garnet-force-field]]"
sources:
  - SRC-0003
sensitivity: public
encryption: none
---

# Garnet Validation Scope

## Question

Which molecule classes and simulation tasks still need validation before treating Garnet as broadly transferable? [SRC-0003]

## Context

SRC-0003 reports promising results on small molecules, folded proteins, protein complexes, IDPs, water, and selected RBFE tasks, but it also notes validation gaps and future targets such as nucleic acids, lipids, metals, carbohydrates, IDPs, and other polymers. Caveats include possible overfitting on GB3 because it was used during training, IDP over-compaction, occasional aromatic-ring planarity failures, over-polarized charges from MBIS-charge fitting, and limited RBFE coverage relative to the full public benchmark. [SRC-0003]

## Current Position

Treat Garnet as a promising automated force-field discovery platform, not as fully validated universal coverage. Future validation and development should test broader biomolecular species and explore functional-form additions such as richer valence terms, torsion corrections, soft-core potentials, polarization, charge flux, and direct training against binding free energy data. [SRC-0003]

## Links

- [[sources/SRC-0003-training-a-force-field-from-scratch]]
- [[concepts/garnet-force-field]]
- [[concepts/automated-force-field-training]]
