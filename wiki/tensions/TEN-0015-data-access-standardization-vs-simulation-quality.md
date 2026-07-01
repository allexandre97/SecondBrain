---
type: tension
status: active
created: 2026-07-01
updated: 2026-07-01
tension_status: active
areas:
  - research
categories:
  - research/data-management
  - research/molecular-simulation/datasets
tags:
  - tension
  - overlay-databank
  - data-management
  - simulation-quality
related_claims:
  - "[[wiki/claims/CLM-0015-molecular-datasets-have-distinct-intended-uses]]"
  - "[[wiki/claims/CLM-0029-overlay-databanks-solve-access-and-standardization-not-simulation-quality]]"
related_questions: []
sources:
  - SRC-0057
  - SRC-0058
sensitivity: public
encryption: none
---

# Data Access Standardization vs Simulation Quality

## Tension

Making biomolecular simulation data searchable, standardized, and programmatically accessible increases reuse, but it can also make heterogeneous simulations look more comparable than their force fields, convergence, compositions, and experimental agreement justify. [SRC-0057] [SRC-0058]

## Evidence

- SRC-0057 shows how the NMRlipids overlay databank enables GUI and API access across heterogeneous membrane simulations. [SRC-0057]
- SRC-0057 also states that ML and analysis results inherit the limits of available simulation compositions, force fields, temperatures, and quality. [SRC-0057]
- SRC-0058 documents metadata and workflow details that support standardization, but those implementation layers do not remove the need for quality evaluation. [SRC-0058]

## Current Status

Active. Overlay databanks should expose quality and provenance metadata rather than imply that standardized access makes all trajectories equally reliable. [SRC-0057] [SRC-0058]

## Links

- [[wiki/sources/SRC-0057-overlay-databank-unlocks-data-driven-analyses-of-biomolecules]]
- [[wiki/sources/SRC-0058-supplementary-information-for-overlay-databank-unlocks-data-driven]]
- [[wiki/claims/CLM-0029-overlay-databanks-solve-access-and-standardization-not-simulation-quality]]
