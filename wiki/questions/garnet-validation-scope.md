---
type: question
status: active
created: 2026-06-29
updated: 2026-09-07
question_status: partially-answered
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
tags:
  - validation
  - garnet
related:
  - "[[wiki/sources/SRC-0003-training-a-force-field-from-scratch]]"
  - "[[wiki/concepts/garnet-force-field]]"
  - "[[wiki/concepts/automated-force-field-training]]"
  - "[[wiki/claims/CLM-0002-garnet-automates-parameter-assignment]]"
  - "[[wiki/tensions/TEN-0002-garnet-broad-coverage-vs-validation-gaps]]"
sources:
  - SRC-0003
sensitivity: public
encryption: none
---

# Garnet Validation Scope

## Question

Which molecule classes and simulation tasks still need validation before treating Garnet as broadly transferable? [SRC-0003]

## Context

SRC-0003 reports promising results on small molecules, folded proteins, protein complexes, IDPs, water, and selected RBFE tasks, but it also notes validation gaps and future targets such as nucleic acids, lipids, metals, carbohydrates, IDPs, and other polymers. Caveats include possible overfitting on GB3 because it was used during training, IDP over-compaction, occasional aromatic-ring planarity failures, MBIS-driven over-polarization that affects dipole magnitude and direction, overestimated density and enthalpy of vapourisation on a 12-molecule test, and RBFE coverage of only 8 of 58 public benchmark systems. [SRC-0003]

## Current Position

Treat Garnet as a promising automated force-field discovery platform, not as fully validated universal coverage. Priority tests include broader small-molecule condensed-phase and solvation-free-energy datasets, electrostatics beyond direct MBIS-charge fitting, net-charge-changing alchemical transformations, independent protein targets, and additional biomolecular species. Functional-form work should also assess richer valence terms, torsion corrections, soft-core potentials, polarization, charge flux, and direct training against binding free energy data. [SRC-0003]

## Links

- [[wiki/sources/SRC-0003-training-a-force-field-from-scratch]]
- [[wiki/concepts/garnet-force-field]]
- [[wiki/concepts/automated-force-field-training]]
- [[wiki/claims/CLM-0002-garnet-automates-parameter-assignment]]
- [[wiki/tensions/TEN-0002-garnet-broad-coverage-vs-validation-gaps]]
