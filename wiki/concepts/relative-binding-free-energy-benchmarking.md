---
type: concept
status: active
created: 2026-06-29
updated: 2026-06-29
areas:
  - research
categories:
  - research/molecular-simulation/binding-free-energy
tags:
  - rbfe
  - drug-discovery
related:
  - "[[concepts/garnet-force-field]]"
sources:
  - SRC-0003
sensitivity: public
encryption: none
---

# Relative Binding Free Energy Benchmarking

## Summary

Relative binding free energy benchmarking evaluates how well simulations rank or predict ligand binding differences against experimental binding data. [SRC-0003]

## Key Points

- SRC-0003 evaluates Garnet on selected systems from a public OpenFE benchmark set, including targets such as Tyk2, Cdk2, P38, Mcl1, chk1, galectin, BACE, T4 lysozyme, and c-Met. [SRC-0003]
- The authors modified OpenFE to support the double exponential potential and related soft-core potential. [SRC-0003]
- Garnet is reported as broadly comparable to OpenFE on the tested systems, with a chk1 outlier noted. [SRC-0003]
- Some transformations failed in the BACE and c-Met systems; the authors removed redundant failed edges from the analysis network. [SRC-0003]
- The benchmark is limited relative to the full 58-system public benchmark set, so it supports promising but not definitive RBFE generalization. [SRC-0003]

## Links

- [[sources/SRC-0003-training-a-force-field-from-scratch]]
- [[concepts/garnet-force-field]]
- [[questions/garnet-validation-scope]]
