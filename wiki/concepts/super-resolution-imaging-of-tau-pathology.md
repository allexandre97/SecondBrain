---
type: concept
status: active
created: 2026-07-01
updated: 2026-07-01
areas:
  - research
categories:
  - research/computer-vision/biomedical-imaging
  - research/biomolecules/proteins
tags:
  - STED
  - tau
  - Alzheimer-disease
  - super-resolution-microscopy
  - neurofibrillary-tangles
related:
  - "[[wiki/concepts/topology-aware-tubular-structure-segmentation]]"
  - "[[wiki/concepts/neuronal-templated-tau-assembly-systems]]"
sources:
  - SRC-0063
  - SRC-0064
sensitivity: public
encryption: none
---

# Super-Resolution Imaging of Tau Pathology

## Summary

Super-resolution imaging of tau pathology uses optical nanoscopy to inspect tau filaments, bundles, and puncta in diseased brain tissue at a scale below conventional confocal microscopy. In autopsied Alzheimer's disease cortical grey matter, STED microscopy resolved immunolabelled tau filaments at about 77 nm lateral resolution, improving over confocal imaging while remaining less structurally detailed than TEM or AFM. [SRC-0063]

## Key Points

- The practical motivation is to obtain nanoscale information from banked human brain tissue where routine fluorescence microscopy lacks sufficient resolution and electron microscopy may be difficult to apply broadly. [SRC-0063]
- In SRC-0063, STED revealed individual filaments within neurofibrillary tangles, filaments outside tangles, and small tau-positive puncta that were not separated clearly by confocal microscopy. [SRC-0063]
- Fluorophore and tissue background matter: STAR 635P performed better than Alexa Fluor 568 or Alexa Fluor 647 for phospho-tau STED imaging in the tested human brain sections. [SRC-0063]
- STED can support questions about tau aggregate organization and spread, but it cannot replace TEM or AFM for resolving fine paired-helical-filament substructure or axial crossover repeats. [SRC-0063]
- A manuscript draft extends the STED use case from autopsied tissue to fixed seeded neuronal cultures, where HA-tagged tau aggregates are reported to resolve at 71 nm in a representative STED image and show tauopathy-seed-dependent morphologies. Treat this as draft-level evidence. [SRC-0064]

## Evidence

- Benda et al. report a mean tau filament width of 77 nm by STED versus about 245 nm for the smallest resolved confocal structures in matched images. [SRC-0063]
- The same study reports retained x-y filament resolution across a 20 micrometer z-stack, while noting that axial z-resolution remains limited. [SRC-0063]
- The authors explicitly frame STED as complementary to, not a substitute for, TEM and AFM in tau filament structural analysis. [SRC-0063]

## Links

- [[wiki/sources/SRC-0063-sted-imaging-tau-filaments-alzheimer-disease]]
- [[wiki/sources/SRC-0064-versatile-neuronal-culture-system-templated-tau-assembly]]
- [[wiki/concepts/neuronal-templated-tau-assembly-systems]]
- [[wiki/concepts/topology-aware-tubular-structure-segmentation]]

## Open Questions

- How reproducible are STED-visible tau puncta and dispersed filaments across tauopathies, brain regions, fixation protocols, and antibody panels?
- Which STED-derived structural features correlate with tau propagation, clinical heterogeneity, or disease-specific tau aggregate forms?
