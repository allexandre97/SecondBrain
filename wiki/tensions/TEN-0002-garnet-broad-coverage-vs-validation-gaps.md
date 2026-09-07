---
type: tension
status: active
created: 2026-07-01
updated: 2026-09-07
tension_status: active
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/machine-learning/molecular-modeling
  - research/experimental-benchmarking
tags:
  - tension
  - garnet
  - validation
related:
  - "[[wiki/concepts/garnet-force-field]]"
related_claims:
  - "[[wiki/claims/CLM-0002-garnet-automates-parameter-assignment]]"
related_questions:
  - "[[wiki/questions/garnet-validation-scope]]"
sources:
  - SRC-0003
sensitivity: public
encryption: none
---

# Garnet Broad Coverage Versus Validation Gaps

## Tension

Garnet is presented as an automated force-field system covering proteins and small molecules, but the source also records validation gaps and failure modes that prevent treating it as universally transferable. [SRC-0003]

## Positions

- SRC-0003 reports competitive benchmark performance across several small-molecule, protein, water, IDP, and selected RBFE tasks. Its revision adds dipole and condensed-phase small-molecule tests. [SRC-0003]
- The added tests also sharpen the limitations: dipole magnitudes and orientations reflect over-polarization, density and enthalpy of vapourisation tend to be overestimated, and the latter errors suggest attractive intermolecular interactions are too strong. [SRC-0003, section "Small molecule benchmark"]
- SRC-0003 also notes possible GB3 overfitting, IDP over-compaction, occasional aromatic-ring planarity failures, RBFE coverage limited to 8 of 58 systems, net-charge-change problems, and future validation needs for additional biomolecular species. [SRC-0003]

## Why it matters

Future force-field answers should preserve both sides: Garnet is a promising automated platform, but its validation boundaries remain material for downstream use.

## Resolution status

Active. Broader validation and functional-form development remain future work. [SRC-0003]

## Links

- [[wiki/claims/CLM-0002-garnet-automates-parameter-assignment]]
- [[wiki/questions/garnet-validation-scope]]
- [[wiki/concepts/garnet-force-field]]
