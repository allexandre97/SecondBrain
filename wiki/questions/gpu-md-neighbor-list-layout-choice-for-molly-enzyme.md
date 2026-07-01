---
type: question
status: active
created: 2026-07-01
updated: 2026-07-01
question_status: open
areas:
  - research
categories:
  - research/molecular-simulation/molecular-dynamics
  - research/high-performance-computing
tags:
  - question
  - GPU
  - neighbor-lists
  - nonbonded-interactions
  - Molly
  - Enzyme
related:
  - "[[wiki/concepts/gpu-md-neighbor-and-nonbonded-acceleration]]"
  - "[[wiki/concepts/particle-mesh-ewald-and-long-range-electrostatics]]"
  - "[[wiki/claims/CLM-0026-gpu-md-neighbor-and-nonbonded-performance-is-data-layout-limited]]"
  - "[[wiki/claims/CLM-0027-ewald-pme-family-choices-trade-accuracy-smoothness-and-cost]]"
  - "[[wiki/tensions/TEN-0012-exact-electrostatics-and-neighbor-accounting-vs-practical-gpu-performance]]"
sources:
  - SRC-0049
  - SRC-0053
  - SRC-0054
sensitivity: public
encryption: none
---

# GPU MD Neighbor-List Layout Choice for Molly/Enzyme

## Question

Which neighbor-list and nonbonded data layout should Molly/Enzyme/MD use on GPUs: atom-pair lists, block/tile screening, clustered compressed lists, SFC/octree layouts, or a hybrid selected by system and hardware? [SRC-0049] [SRC-0053]

## Context

SRC-0053 avoids atom-pair neighbor-list indirection by screening 32-atom block tiles, a design suited to early GPU memory behavior. SRC-0049 uses clustered compressed neighbor lists with SFC ordering and reports different behavior on NVIDIA and AMD systems. SRC-0054 adds that long-range electrostatics choices can dominate performance through grid and communication costs, so short-range layout cannot be chosen in isolation. [SRC-0053] [SRC-0049] [SRC-0054]

## Current Position

Keep the question open. The implementation should benchmark construction, traversal, memory footprint, rebuild frequency, force reproducibility, and interaction with long-range electrostatics on the target hardware rather than adopting a layout solely from asymptotic pair-count reasoning. [SRC-0049] [SRC-0053] [SRC-0054]

## Links

- [[wiki/sources/SRC-0049-gpu-native-compressed-neighbor-lists-with-a-space]]
- [[wiki/sources/SRC-0053-efficient-nonbonded-interactions-for-molecular-dynamics-on-a]]
- [[wiki/sources/SRC-0054-accelerating-molecular-dynamics-simulations-using-fast-ewald-summation]]
- [[wiki/claims/CLM-0026-gpu-md-neighbor-and-nonbonded-performance-is-data-layout-limited]]
- [[wiki/claims/CLM-0027-ewald-pme-family-choices-trade-accuracy-smoothness-and-cost]]
