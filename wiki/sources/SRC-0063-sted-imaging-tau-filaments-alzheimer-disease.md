---
type: source
status: active
created: 2026-07-01
updated: 2026-07-01
source_id: SRC-0063
display_title: "STED Imaging of Tau Filaments in Alzheimer's Disease Cortical Grey Matter"
short_title: "STED Tau Filaments"
aliases:
  - "SRC-0063"
  - "STED Tau Filaments"
  - "STED imaging of tau filaments in Alzheimer's disease cortical grey matter"
source_path: raw/sources/SRC-0063-sted-imaging-tau-filaments-alzheimer-disease.pdf
imported_path: raw/sources/SRC-0063-sted-imaging-tau-filaments-alzheimer-disease.pdf
original_filename: "1-s2.0-S1047847716301447-main.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 0eb22f443d31069b44bea749bc6fa5e1113a4f05aa780cf8cb10cec8c46590b2
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
  - "[[wiki/concepts/super-resolution-imaging-of-tau-pathology]]"
  - "[[wiki/concepts/topology-aware-tubular-structure-segmentation]]"
sources:
  - SRC-0063
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: standard
---

# STED Imaging of Tau Filaments in Alzheimer's Disease Cortical Grey Matter

Source ID: `SRC-0063`

## Raw source

- Repository path: `raw/sources/SRC-0063-sted-imaging-tau-filaments-alzheimer-disease.pdf`
- Open raw source: [raw/sources/SRC-0063-sted-imaging-tau-filaments-alzheimer-disease.pdf](../../raw/sources/SRC-0063-sted-imaging-tau-filaments-alzheimer-disease.pdf)

## Summary

Benda et al. evaluate stimulated emission depletion microscopy for imaging phospho-tau structures in autopsied human Alzheimer's disease cortical grey matter. The paper shows that STED can resolve immunolabelled tau filaments in 50 micrometer brain sections at about 77 nm lateral resolution, distinguish filaments within neurofibrillary tangles better than confocal microscopy, and visualize 70-80 nm tau-positive puncta. [SRC-0063]

## Key Points

- The study addresses the gap between routine optical microscopy, which resolves pathology outlines at roughly 250 nm, and electron microscopy, which is higher resolution but less routine for banked human brain tissue. [SRC-0063]
- Human formalin-fixed inferior temporal cortex sections from Alzheimer's disease cases were labelled with phospho-tau antibody 12E8 and tested with Alexa Fluor 568, Alexa Fluor 647, and STAR 635P secondary labels. [SRC-0063, Materials and methods]
- STAR 635P was the best fluorophore tested because it gave stronger STED performance in autofluorescent human brain tissue and showed minimal photobleaching under the protocol. [SRC-0063]
- STED measured individual tau filaments at a mean full-width-half-maximum of 77 nm, compared with about 245 nm for the smallest resolved structures in confocal images of the same labelled tissue. [SRC-0063, Results]
- STED resolved tau filaments inside neurofibrillary tangles, dispersed filaments outside tangles, and 70-80 nm tau-positive puncta that may represent oligomeric or fragmented tau structures. [SRC-0063]
- STED z-stacks through 20 micrometers of tissue retained x-y resolution for individual filaments, although z-axis resolution remained confocal-like. [SRC-0063]

## Limitations

- STED did not resolve the 60-80 nm axial crossover repeats seen by transmission electron microscopy for paired helical filaments, so TEM or AFM remains necessary for fine tau filament substructure. [SRC-0063]
- Occasional axial undulations of 100-250 nm were visible, but the authors could not exclude antibody-labelling inhomogeneity as a cause. [SRC-0063]
- The work validates an imaging protocol and reports structural observations, but it does not by itself establish mechanisms of tau propagation or distinguish disease-specific tau strains. [SRC-0063]
- Alexa Fluor 647 was limited by photoswitching and photobleaching in this STED setup, while Alexa Fluor 568 improved over confocal but did not match STAR 635P resolution. [SRC-0063]

## Links

- [[wiki/concepts/super-resolution-imaging-of-tau-pathology]]
- [[wiki/concepts/topology-aware-tubular-structure-segmentation]]

## Ingestion QA

### Retrieval questions checked

- What is the central contribution of this paper?
- What problem does STED address for human Alzheimer's brain sections?
- What tissue, antibody, and fluorophores were used?
- What resolution did STED achieve for tau filaments compared with confocal microscopy?
- Which fluorophore worked best and why?
- What tau structures beyond neurofibrillary tangles were observed?
- What limitations remain relative to TEM or AFM?
- What claims should not be overgeneralized?

### Coverage decision

Complete at `coverage_profile: standard`. The source page covers the paper's purpose, tissue and labelling setup, imaging findings, fluorophore comparison, limitations, and links to a durable concept page for STED-based tau pathology imaging.

### Known gaps

- The wiki does not reproduce the full microscopy hardware configuration or acquisition timing details.
- Supplementary figures are not separately ingested.
