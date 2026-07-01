---
type: source
status: active
created: 2026-06-30
updated: 2026-07-01
source_id: SRC-0035
display_title: "SOAX: A Software for Quantification of 3D Biopolymer Networks"
short_title: "SOAX"
aliases:
  - "SRC-0035"
  - "SOAX"
  - "SOAX: A Software for Quantification of 3D Biopolymer Networks"
source_path: raw/sources/SRC-0035-soax-software-for-quantification-of-3d-biopolymer-networks.pdf
original_filename: "Xu15.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: fa2ba6561f02ad8fc4f309dc30b3ed928af074364ea55fd96555de1f93fc6d49
authors:
  - "Ting Xu"
  - "Dimitrios Vavylonis"
  - "Feng-Ching Tsai"
  - "Gijsje H. Koenderink"
  - "Wei Nie"
  - "Eddy Yusuf"
  - "I-Ju Lee"
  - "Jian-Qiu Wu"
  - "Xiaolei Huang"
author_entities: []
year: 2015
venue: "Scientific Reports"
doi: "10.1038/srep09081"
arxiv:
metadata_review_status: reviewed
citation_match_status: reviewed
cqt_review_status: linked
cites_sources: []
areas:
  - research
categories:
  - research/bioimage-analysis/filament-segmentation
  - research/computer-vision/biomedical-imaging
tags:
  - SOAX
  - SOAC
  - biopolymer-networks
  - filament-tracing
related:
  - "[[wiki/concepts/stretching-open-active-contours]]"
  - "[[wiki/concepts/cytoskeleton-segmentation-and-tracing]]"
sources:
  - SRC-0035
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: standard
---

# SOAX: A Software for Quantification of 3D Biopolymer Networks

Source ID: `SRC-0035`

## Raw source

- Repository path: `raw/sources/SRC-0035-soax-software-for-quantification-of-3d-biopolymer-networks.pdf`
- Open raw source: [raw/sources/SRC-0035-soax-software-for-quantification-of-3d-biopolymer-networks.pdf](../../raw/sources/SRC-0035-soax-software-for-quantification-of-3d-biopolymer-networks.pdf)

## Summary

Xu et al. present SOAX, an open-source software tool for extracting centerlines and junctions of 2D and 3D biopolymer networks using Stretching Open Active Contours (SOACs). It supports visualization, manual editing, parameter optimization, and quantitative analysis of actin, microtubule, and fibrin-like networks. [SRC-0035]

## Key Points

- SOAX initializes multiple short active contours along image intensity ridges, evolves them through image and stretching forces, merges or stops them at filament tips or junctions, and then reconfigures local connectivity by cutting and splicing contours near junctions. [SRC-0035, figure 1 and Results]
- The software fills a gap for user-friendly 3D biopolymer network tracing and junction localization, where many prior methods produced disconnected centerline pixels or required thresholded tubularity maps. [SRC-0035]
- Parameter choice matters, especially ridge threshold and stretch factor; the paper introduces an unsupervised F-function to help select candidate parameter sets without ground truth. [SRC-0035]
- The F-function favors complete extracted centerlines while penalizing contour segments in low-signal regions, helping users select among parameter scans. [SRC-0035]
- Demonstrations include actin bundles in emulsion droplets, microtubules in adhered cells, actin cables in fission yeast, and synthetic networks. [SRC-0035]

## Limitations

- SOAX parameters must be adjusted for filament type and image signal-to-noise ratio, and final selection may still involve user judgment. [SRC-0035]
- SOAX works best when filaments or bundles are sufficiently separated relative to the point-spread-function width; dense unresolved structures and wide-field out-of-focus background can degrade performance. [SRC-0035]
- Anisotropic confocal resolution along the z-axis can produce artifacts unless analysis is configured carefully. [SRC-0035]
- Pairwise contour-overlap checking can become a computational bottleneck for much larger images. [SRC-0035]

## Claims

- [[wiki/claims/CLM-0021-fiber-analysis-needs-graph-measurements-not-only-masks]] - SOAX extracts centerlines and junctions to support quantitative biopolymer-network analysis. [SRC-0035]
- [[wiki/claims/CLM-0022-instance-filament-tracing-is-harder-than-semantic-segmentation]] - The active-contour workflow and connectivity repair illustrate why tracing is more than foreground thresholding. [SRC-0035]

## Citation Links

- Targeted citation review found no new confirmed `cites_sources` links to add for currently ingested sources. [SRC-0035]

## Links

- [[wiki/concepts/stretching-open-active-contours]]
- [[wiki/concepts/cytoskeleton-segmentation-and-tracing]]
- [[wiki/claims/CLM-0021-fiber-analysis-needs-graph-measurements-not-only-masks]]
- [[wiki/claims/CLM-0022-instance-filament-tracing-is-harder-than-semantic-segmentation]]

## Ingestion QA

### Retrieval questions checked

- What is SOAX?
- What are SOACs?
- How does SOAX extract network topology?
- How are parameters chosen?
- What biological examples does the paper show?
- What image conditions limit SOAX?
- Why is SOAX relevant to later deep-learning filament papers?

### Coverage decision

Complete at `coverage_profile: standard`. The source page covers the software purpose, method stages, parameter optimization, demonstrations, limitations, and links to tracing concepts.

### Known gaps

- The wiki does not reproduce the full SOAC force equations or supplementary implementation details.
- The historical software URL is recorded only through the source summary, not verified externally.
