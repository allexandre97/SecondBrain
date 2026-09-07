---
type: claim
status: active
created: 2026-07-01
updated: 2026-09-07
claim_status: limited
claim_scope: local
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/machine-learning/molecular-modeling
  - research/biomolecules/proteins
tags:
  - claim
  - garnet
  - force-fields
related:
  - "[[wiki/concepts/garnet-force-field]]"
  - "[[wiki/concepts/automated-force-field-training]]"
  - "[[wiki/questions/garnet-validation-scope]]"
  - "[[wiki/tensions/TEN-0002-garnet-broad-coverage-vs-validation-gaps]]"
sources:
  - SRC-0003
sensitivity: public
encryption: none
---

# Garnet Automates Force-Field Parameter Assignment

## Claim

Garnet uses a graph neural network to predict molecular mechanics parameters for supported proteins and small molecules from topology, using continuous atom typing rather than fixed manually assigned atom types. [SRC-0003]

## Scope

This claim is local to SRC-0003 and limited to the molecule classes and tasks validated or discussed there. It does not establish universal biomolecular transferability. [SRC-0003]

## Evidence

- SRC-0003 describes Garnet as assigning bond, angle, torsion, charge, and double-exponential non-bonded parameters from molecular topology. [SRC-0003]
- The source reports benchmarks across small molecules, folded proteins, protein complexes, disordered proteins, water, and selected RBFE systems. [SRC-0003]

## Caveats

- The revised source records possible GB3 overfitting, IDP over-compaction, occasional aromatic-ring planarity failures, over-polarized dipoles, overestimated small-molecule density and enthalpy of vapourisation, and RBFE testing on only 8 of 58 public benchmark systems. These limits constrain the validated scope but do not alter the parameter-assignment mechanism. [SRC-0003]

## Links

- [[wiki/sources/SRC-0003-training-a-force-field-from-scratch]]
- [[wiki/concepts/garnet-force-field]]
- [[wiki/concepts/automated-force-field-training]]
- [[wiki/questions/garnet-validation-scope]]
- [[wiki/tensions/TEN-0002-garnet-broad-coverage-vs-validation-gaps]]
