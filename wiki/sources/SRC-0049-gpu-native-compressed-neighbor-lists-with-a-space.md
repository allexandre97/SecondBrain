---
type: source
status: active
created: 2026-06-30
updated: 2026-06-30
source_id: SRC-0049
display_title: "GPU-Native Compressed Neighbor Lists with a Space-Filling-Curve Data Layout"
short_title: "GPU Compressed Neighbor Lists"
aliases:
  - "SRC-0049"
  - "GPU Compressed Neighbor Lists"
  - "GPU-Native Compressed Neighbor Lists with a Space-Filling-Curve Data Layout"
source_path: raw/sources/SRC-0049-gpu-native-compressed-neighbor-lists-with-a-space.pdf
original_filename: "2602.19873v1.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: c84aea4ce94c06fe3b8a44346e35390bd76b699184bc8d92f1ecfcc8a13c5294
areas:
  - research
categories:
  - research/molecular-simulation/molecular-dynamics
  - research/high-performance-computing
tags:
  - GPU
  - neighbor-lists
  - space-filling-curves
  - particle-simulation
related:
  - "[[concepts/gpu-md-neighbor-and-nonbonded-acceleration]]"
sources:
  - SRC-0049
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: math-standard
---

# GPU-Native Compressed Neighbor Lists with a Space-Filling-Curve Data Layout

Source ID: `SRC-0049`

## Raw source

- Repository path: `raw/sources/SRC-0049-gpu-native-compressed-neighbor-lists-with-a-space.pdf`
- Local relative link: [Open raw source](../../raw/sources/SRC-0049-gpu-native-compressed-neighbor-lists-with-a-space.pdf)

## Summary

This arXiv paper presents a GPU-native compressed neighbor-list method based on a space-filling-curve data layout and particle clusters. It targets short-range particle interactions across MD-like and astrophysical/SPH settings, with support for GPU construction, variable interaction radii, and octree integration. [SRC-0049]

## Key Points

- The method stores clustered neighbor information in a compressed form with reported memory footprint below 4 bytes per particle for about 200 neighbors. [SRC-0049, abstract]
- It aims to match GROMACS-style clustered neighbor-list performance while improving construction on GPUs and handling nonuniform density distributions. [SRC-0049]
- Space-filling-curve ordering gives spatial locality and connects naturally to octree domain decomposition and long-range methods. [SRC-0049]
- Benchmarks compare against LAMMPS-like full neighbor lists and GROMACS-like clustered lists on NVIDIA GH200 and AMD MI300A GPUs. [SRC-0049]
- The paper demonstrates weak scaling in an Evrard collapse benchmark up to 1024 NVIDIA GH200 GPUs. [SRC-0049]

## Key equations

The source is primarily algorithmic. The implementation-relevant mathematical objects are neighbor sets:

$$
\mathcal{N}_i(r_i) = \{j : \|x_i-x_j\| < r_i\},
$$

where $r_i$ may vary by particle. [SRC-0049]

## Variable glossary

- $\mathcal{N}_i$: neighbor set for particle $i$. [SRC-0049]
- $r_i$: interaction or search radius for particle $i$. [SRC-0049]
- SFC: space-filling curve used to order particles for locality. [SRC-0049]
- Super-cluster: group of clusters sharing one compressed neighbor-list record. [SRC-0049]

## Equation inventory

| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |
| Radius neighbor set | Algorithmic definition | Key equations | Defines per-particle search target | $\mathcal{N}_i$, $r_i$ | Conceptual basis for variable-radius lists |
| Variable-length encoding | Section II-B | Mathematical gaps | Compresses neighbor indices | encoded deltas, nibbles | Implementation details remain in source |

## Limitations

- The preprint had been submitted for publication; final peer-reviewed details may differ. [SRC-0049]
- Performance tradeoffs are hardware-dependent; the paper reports different behavior on NVIDIA GH200 and AMD MI300A. [SRC-0049]
- The approach is a neighbor-list infrastructure contribution, not a complete MD accuracy validation by itself. [SRC-0049]

## Mathematical gaps

- Compression bit layout, SFC/octree construction details, and code-level API examples are summarized rather than reproduced.

## Links

- [[concepts/gpu-md-neighbor-and-nonbonded-acceleration]]

## Ingestion QA

### Retrieval questions checked

- What data layout does the neighbor-list method use?
- What memory-footprint claim is central?
- How does it compare with GROMACS and LAMMPS-style lists?
- Why is SFC ordering useful?
- What hardware and scaling tests are reported?
- What limitations are hardware-dependent?

### Coverage decision

Complete at `coverage_profile: math-standard`. The page captures algorithmic scope, performance claims, and known implementation gaps.
