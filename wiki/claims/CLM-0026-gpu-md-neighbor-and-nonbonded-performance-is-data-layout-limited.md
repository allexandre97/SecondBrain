---
type: claim
status: active
created: 2026-07-01
updated: 2026-07-01
claim_status: supported
claim_scope: cross-source
areas:
  - research
categories:
  - research/molecular-simulation/molecular-dynamics
  - research/high-performance-computing
tags:
  - claim
  - GPU
  - neighbor-lists
  - nonbonded-interactions
  - data-layout
related:
  - "[[wiki/concepts/gpu-md-neighbor-and-nonbonded-acceleration]]"
  - "[[wiki/questions/gpu-md-neighbor-list-layout-choice-for-molly-enzyme]]"
  - "[[wiki/tensions/TEN-0012-exact-electrostatics-and-neighbor-accounting-vs-practical-gpu-performance]]"
sources:
  - SRC-0049
  - SRC-0053
sensitivity: public
encryption: none
---

# GPU MD Neighbor and Nonbonded Performance Is Data-Layout Limited

## Claim

GPU MD neighbor and nonbonded performance depends on data layout, locality, compression, and memory movement at least as much as on reducing arithmetic interaction counts. [SRC-0049] [SRC-0053]

## Evidence

- SRC-0053 argues that conventional atom-pair neighbor lists create indirect memory access patterns that fit CPUs better than GPUs, then replaces atom-pair list traversal with block/tile screening. [SRC-0053]
- SRC-0053 partitions atoms into blocks of 32 and screens block-pair tiles by bounding boxes, trading some extra pair checks for more regular GPU memory access. [SRC-0053]
- SRC-0049 stores clustered neighbor information in compressed form and uses space-filling-curve ordering to improve locality and integrate with octree decomposition. [SRC-0049]
- SRC-0049 reports hardware-dependent behavior across NVIDIA GH200 and AMD MI300A GPUs, reinforcing that the best neighbor representation is architecture-sensitive. [SRC-0049]

## Implementation Use

For Molly/Enzyme/MD work, an accelerator design should expose neighbor-list layout as a first-class implementation choice. Benchmarks should measure construction cost, traversal cost, memory footprint, locality, and rebuild policy, not only the count of mathematically necessary pair interactions. [SRC-0049] [SRC-0053]

## Caveats

SRC-0053 reflects 2009-era GPU constraints, while SRC-0049 is a 2026 preprint with modern GPU targets; the reusable claim is about layout sensitivity, not a fixed best algorithm. [SRC-0049] [SRC-0053]

## Links

- [[wiki/sources/SRC-0049-gpu-native-compressed-neighbor-lists-with-a-space]]
- [[wiki/sources/SRC-0053-efficient-nonbonded-interactions-for-molecular-dynamics-on-a]]
- [[wiki/concepts/gpu-md-neighbor-and-nonbonded-acceleration]]
