---
type: claim
status: active
created: 2026-07-01
updated: 2026-07-01
claim_status: supported
claim_scope: implementation
areas:
  - research
categories:
  - research/data-management
  - research/molecular-simulation/datasets
  - research/biomolecules/lipids
tags:
  - claim
  - overlay-databank
  - FAIR-data
  - simulation-quality
related:
  - "[[wiki/concepts/overlay-databanks-for-biomolecular-simulation-data]]"
  - "[[wiki/claims/CLM-0015-molecular-datasets-have-distinct-intended-uses]]"
  - "[[wiki/tensions/TEN-0015-data-access-standardization-vs-simulation-quality]]"
sources:
  - SRC-0057
  - SRC-0058
sensitivity: public
encryption: none
---

# Overlay Databanks Solve Access and Standardization, Not Simulation Quality

## Claim

Overlay databanks make scattered biomolecular simulation data programmatically accessible and comparable through metadata, naming, analysis, and quality-evaluation layers, but they do not by themselves guarantee force-field accuracy, convergence, or unbiased simulation coverage. [SRC-0057] [SRC-0058]

## Evidence

- SRC-0057 defines an overlay structure with data, databank, and application layers, leaving raw trajectories in public repositories while adding metadata, mapping, quality evaluation, and analysis programs. [SRC-0057]
- SRC-0057 explicitly notes that databank-trained ML models inherit limits from available lipid compositions, force fields, temperatures, and simulation quality. [SRC-0057]
- SRC-0058 documents the implementation-facing metadata keys, force-field lists, workflow diagrams, and application-layer scripts that make the overlay layer usable. [SRC-0058]

## Implementation Use

For biomolecular data infrastructure, treat overlay databanks as a reuse and standardization mechanism. They need separate validation gates for raw simulation quality, force-field transferability, experimental comparison, and downstream ML generalization. [SRC-0057] [SRC-0058]

## Links

- [[wiki/sources/SRC-0057-overlay-databank-unlocks-data-driven-analyses-of-biomolecules]]
- [[wiki/sources/SRC-0058-supplementary-information-for-overlay-databank-unlocks-data-driven]]
- [[wiki/concepts/overlay-databanks-for-biomolecular-simulation-data]]
