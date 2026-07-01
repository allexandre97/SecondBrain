---
type: concept
status: active
created: 2026-07-01
updated: 2026-07-01
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/machine-learning/molecular-modeling
  - research/computational-drug-discovery
tags:
  - SMIRNOFF
  - OpenFF
  - bespoke-force-fields
  - machine-learning-potentials
  - valence-parameters
related:
  - "[[wiki/concepts/automated-force-field-training]]"
  - "[[wiki/concepts/forcebalance]]"
  - "[[wiki/concepts/machine-learned-interatomic-potential-foundation-models]]"
sources:
  - SRC-0066
sensitivity: public
encryption: none
---

# MLP-Driven Bespoke SMIRNOFF Force-Field Fitting

## Summary

MLP-driven bespoke SMIRNOFF force-field fitting uses transferable machine-learning potentials as fast surrogates for quantum-mechanical reference calculations while fitting molecule-specific molecular-mechanics parameters in the OpenFF/SMIRNOFF format. SRC-0066 presents `presto` as an automated valence-parameter workflow for individual molecules or congeneric series. [SRC-0066]

## Key Points

- The main speed gain comes from replacing many direct QM calculations with MLP energy and force evaluations, then training SMIRNOFF valence parameters on GPU. [SRC-0066]
- The approach preserves a conventional molecular-mechanics functional form, so fitted force fields remain compatible with OpenMM, OpenFE, and exported simulation formats. [SRC-0066]
- `presto` fits bonds, angles, proper torsions, and improper torsions rather than only rotatable-bond torsions. [SRC-0066]
- High-temperature MD and well-tempered metadynamics are used to sample conformations and torsion barriers without explicit relaxed torsion scans. [SRC-0066]
- Congeneric-series fitting can share parameters across common substructures, which is important for relative free-energy calculations where inconsistent shared parameters can add noise. [SRC-0066]

## Evidence

- SRC-0066 reports about a threefold reduction in torsion-scan RMSE versus OpenFF Sage 2.3.0 on the TorsionNet500 test subset.
- SRC-0066 reports similar torsion-scan performance to OpenFF BespokeFit on JACS fragments, while using MLP reference data rather than direct QM torsion fitting.
- SRC-0066 reports RBFE performance comparable to OpenFF 1.3.1 on CDK2, TYK2, and JNK1, with specific improvements where baseline torsional parameters were poor.

## Links

- [[wiki/sources/SRC-0066-presto-bespoke-smirnoff-force-fields-mlps]]
- [[wiki/concepts/automated-force-field-training]]
- [[wiki/concepts/forcebalance]]
- [[wiki/concepts/machine-learned-interatomic-potential-foundation-models]]

## Caveats

- SRC-0066 is a preprint, not peer reviewed.
- Valence refitting cannot fully repair inaccurate intramolecular nonbonded terms; future workflows may need intramolecular Lennard-Jones fitting or co-training against condensed-phase properties. [SRC-0066]
- Default protocol choices can fail on some chemistries and may require class-specific adjustments. [SRC-0066]

## Open Questions

- Which molecules benefit most from MLP-driven bespoke fitting before RBFE calculations?
- How should intramolecular nonbonded parameters be trained without degrading condensed-phase transferability?
