---
type: source
status: active
created: 2026-06-30
updated: 2026-06-30
source_id: SRC-0053
display_title: "Efficient Nonbonded Interactions for Molecular Dynamics on a Graphics Processing Unit"
short_title: "OpenMM GPU Nonbonded Interactions"
authors:
  - Peter Eastman
  - Vijay S. Pande
year: 2010
venue: "Journal of Computational Chemistry"
doi: "10.1002/jcc.21413"
aliases:
  - "SRC-0053"
  - "OpenMM GPU Nonbonded Interactions"
  - "Efficient Nonbonded Interactions for Molecular Dynamics on a Graphics Processing Unit"
source_path: raw/sources/SRC-0053-efficient-nonbonded-interactions-for-molecular-dynamics-on-a.pdf
original_filename: "J Comput Chem - 2009 - Eastman - Efficient nonbonded interactions for molecular dynamics on a graphics processing unit.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: b2407640c91a3e3cd3da12f0dd4b6f812a634a7c3e927db1565fd42c18298169
areas:
  - research
categories:
  - research/molecular-simulation/molecular-dynamics
  - research/high-performance-computing
tags:
  - GPU
  - nonbonded-interactions
  - OpenMM
  - cutoff
related:
  - "[[wiki/concepts/gpu-md-neighbor-and-nonbonded-acceleration]]"
sources:
  - SRC-0053
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: math-standard
metadata_review_status: reviewed
citation_match_status: partial
cqt_review_status: linked
---

# Efficient Nonbonded Interactions for Molecular Dynamics on a Graphics Processing Unit

Source ID: `SRC-0053`

## Raw source

- Repository path: `raw/sources/SRC-0053-efficient-nonbonded-interactions-for-molecular-dynamics-on-a.pdf`
- Open raw source: [raw/sources/SRC-0053-efficient-nonbonded-interactions-for-molecular-dynamics-on-a.pdf](../../raw/sources/SRC-0053-efficient-nonbonded-interactions-for-molecular-dynamics-on-a.pdf)

## Summary

Eastman and Pande describe a GPU algorithm for cutoff nonbonded interactions implemented in OpenMM. The method uses block/tile-level interaction screening rather than a conventional atom-pair neighbor list, improving memory access patterns on GPUs while retaining linear scaling for practical cutoff simulations. [SRC-0053]

## Key Points

- GPU memory systems favor contiguous/direct memory access and penalize indirect atom access typical of standard neighbor lists. [SRC-0053]
- The algorithm partitions atoms into blocks of 32 and treats the full interaction matrix as tiles; it excludes tiles whose bounding boxes are beyond the cutoff. [SRC-0053]
- Tile screening is analogous to a neighbor list over blocks rather than over atom pairs. [SRC-0053]
- The source reports linear scaling across a range of systems and large speedups relative to contemporaneous CPU MD packages. [SRC-0053]
- The method became part of OpenMM's early GPU MD infrastructure. [SRC-0053]

## Key equations

Pair-interaction enumeration without cutoffs is $O(N^2)$, while cutoff interactions ideally scale as:

$$
O(N n_c),
$$

where $n_c$ is the average number of atoms within the cutoff and is approximately independent of $N$ at fixed density. [SRC-0053]

## Variable glossary

- $N$: number of atoms. [SRC-0053]
- $n_c$: average cutoff-neighbor count. [SRC-0053]
- Tile: block-pair of 32-by-32 possible interactions. [SRC-0053]
- Cutoff: distance beyond which interactions are omitted or approximated. [SRC-0053]

## Equation inventory

| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |
| Cutoff scaling | Background | Key equations | Explains target linear scaling | $N$, $n_c$ | Performance model |
| Bounding-box tile exclusion | Algorithm section | Mathematical gaps | Removes distant block pairs | block boxes, cutoff | Main GPU screening rule |

## Limitations

- The paper targets cutoff/reaction-field style nonbonded interactions, not full PME electrostatics. [SRC-0053]
- Hardware conclusions reflect 2009-era GPUs and must be reinterpreted for modern architectures. [SRC-0053]

## Mathematical gaps

- Exact tile-screening formulas and benchmark tables are summarized rather than reproduced.

## Links

- [[wiki/concepts/gpu-md-neighbor-and-nonbonded-acceleration]]

## Claims

- [[wiki/claims/CLM-0026-gpu-md-neighbor-and-nonbonded-performance-is-data-layout-limited]]

## Questions

- [[wiki/questions/gpu-md-neighbor-list-layout-choice-for-molly-enzyme]]

## Tensions

- [[wiki/tensions/TEN-0012-exact-electrostatics-and-neighbor-accounting-vs-practical-gpu-performance]]

## Citation links

- Citation review status: partial. Bibliographic metadata was checked from the PDF first page; no source-to-source citation link within SRC-0047 through SRC-0054 was promoted without direct bibliography evidence.

## Ingestion QA

### Retrieval questions checked

- Why are standard neighbor lists awkward on GPUs?
- What is the block/tile idea?
- How does the method avoid computing all $N^2$ interactions?
- What scaling and performance claims are made?
- What hardware-era caveats apply?

### Coverage decision

Complete at `coverage_profile: math-standard`. The page captures the algorithmic contribution and performance interpretation.
