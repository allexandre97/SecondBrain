---
type: tension
status: active
created: 2026-07-01
updated: 2026-07-01
tension_status: active
areas:
  - research
categories:
  - research/molecular-simulation/molecular-dynamics
  - research/high-performance-computing
tags:
  - tension
  - GPU
  - electrostatics
  - neighbor-lists
  - performance
related_claims:
  - "[[wiki/claims/CLM-0026-gpu-md-neighbor-and-nonbonded-performance-is-data-layout-limited]]"
  - "[[wiki/claims/CLM-0027-ewald-pme-family-choices-trade-accuracy-smoothness-and-cost]]"
related_questions:
  - "[[wiki/questions/gpu-md-neighbor-list-layout-choice-for-molly-enzyme]]"
sources:
  - SRC-0049
  - SRC-0050
  - SRC-0053
  - SRC-0054
sensitivity: public
encryption: none
---

# Exact Electrostatics and Neighbor Accounting vs Practical GPU Performance

## Tension

MD implementations need accurate neighbor and long-range electrostatic accounting, but practical GPU and cluster performance often requires layouts, kernels, cutoffs, grids, and communication patterns that are optimized for hardware rather than mathematical directness. [SRC-0049] [SRC-0050] [SRC-0053] [SRC-0054]

## Evidence

- SRC-0050 improves PME smoothness and analytic gradients through B-spline gridding, already replacing direct reciprocal sums with controlled mesh approximations. [SRC-0050]
- SRC-0054 changes Ewald kernels again to reduce grid size and communication, with speedups tied to target error tolerances. [SRC-0054]
- SRC-0053 uses block/tile screening to avoid GPU-unfriendly atom-pair neighbor-list indirection, accepting a coarser interaction-screening unit. [SRC-0053]
- SRC-0049 compresses clustered neighbor data and uses SFC ordering, making memory layout part of the algorithmic contract. [SRC-0049]

## Current Status

Active. The practical resolution is not to choose exactness or speed in isolation, but to make tolerance, layout, and force/virial error tests explicit in the implementation. [SRC-0050] [SRC-0054]

## Links

- [[wiki/sources/SRC-0049-gpu-native-compressed-neighbor-lists-with-a-space]]
- [[wiki/sources/SRC-0050-a-smooth-particle-mesh-ewald-method]]
- [[wiki/sources/SRC-0053-efficient-nonbonded-interactions-for-molecular-dynamics-on-a]]
- [[wiki/sources/SRC-0054-accelerating-molecular-dynamics-simulations-using-fast-ewald-summation]]
- [[wiki/questions/gpu-md-neighbor-list-layout-choice-for-molly-enzyme]]
