---
type: source
status: active
created: 2026-06-30
updated: 2026-06-30
source_id: SRC-0029
display_title: "Densely Connected Stacked U-network for Filament Segmentation in Microscopy Images"
short_title: "Stacked U-Net Filament Segmentation"
aliases:
  - "SRC-0029"
  - "Stacked U-Net Filament Segmentation"
  - "Densely Connected Stacked U-network for Filament Segmentation in Microscopy Images"
source_path: raw/sources/SRC-0029-densely-connected-stacked-u-network-for-filament-segmentation.pdf
original_filename: "Liu18.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: c0c2bfb54e9f9eec9a79757c3c5ad72b0166c6e350277136517e45697e4b300a
areas:
  - research
categories:
  - research/bioimage-analysis/cytoskeleton
  - research/computer-vision/biomedical-imaging
tags:
  - filament-segmentation
  - microscopy
  - deep-learning
  - u-net
related:
  - "[[concepts/cytoskeleton-segmentation-and-tracing]]"
  - "[[concepts/deep-learning-cytoskeleton-image-analysis]]"
  - "[[concepts/filament-instance-and-semantic-segmentation]]"
sources:
  - SRC-0029
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: standard
---

# Densely Connected Stacked U-network for Filament Segmentation in Microscopy Images

Source ID: `SRC-0029`

## Raw source

- Repository path: `raw/sources/SRC-0029-densely-connected-stacked-u-network-for-filament-segmentation.pdf`
- Local relative link: [Open raw source](../../raw/sources/SRC-0029-densely-connected-stacked-u-network-for-filament-segmentation.pdf)

## Summary

Liu et al. introduce a densely connected stacked U-Net architecture for semantic segmentation of filamentous structures in confocal microscopy images. The paper targets noisy, blurred, cluttered images where classical parameter-sensitive methods such as SOAX can fragment filaments or require extensive tuning. It also proposes a semi-automatic annotation strategy and reports microtubule and actin filament datasets. [SRC-0029]

## Key Points

- The method stacks multiple U-Net-like modules and uses cross-connections and weighted losses across module outputs to improve filament segmentation while reducing false disconnections. [SRC-0029, section 3]
- The authors argue that ordinary pixel IoU can be overly sensitive for thin filaments, so they introduce skeletonized IoU (SKIoU) to emphasize centerline overlap and reduce sensitivity to small thickness or alignment differences. [SRC-0029, section 4.1]
- On microtubule images, the best proposed model reports IoU 0.9439 and SKIoU 0.9775, compared with SOAX IoU 0.6189 and SKIoU 0.8833. [SRC-0029, table 1]
- On actin filament images, the proposed network reports IoU 0.9140 and SKIoU 0.9580, compared with SOAX IoU 0.6247 and SKIoU 0.8946. [SRC-0029, table 2]
- The biological motivation is not merely pixel segmentation: false gaps and fragments can be misinterpreted as separate filaments in downstream length, curvature, and movement analysis. [SRC-0029, section 4.2]

## Limitations

- The paper's annotations are built through semi-automatic correction, so evaluation depends on the quality and possible bias of those labels. [SRC-0029, sections 3-4]
- It addresses semantic segmentation, not full instance reconstruction or time tracking; the authors list length, curvature, and motion tracking as future work. [SRC-0029, section 5]
- The actin experiment applies a network trained on microtubules, so cross-domain performance should be interpreted as a limited transfer result rather than broad biological generalization. [SRC-0029, section 4.3]

## Links

- [[concepts/deep-learning-cytoskeleton-image-analysis]]
- [[concepts/filament-instance-and-semantic-segmentation]]
- [[concepts/cytoskeleton-segmentation-and-tracing]]

## Ingestion QA

### Retrieval questions checked

- What architecture did the paper introduce?
- Why is filament segmentation harder than generic semantic segmentation?
- What is SKIoU and why was it used?
- How did the method compare with SOAX on microtubules and actin?
- What downstream biological analyses motivate reducing false filament gaps?
- What are the main limitations and future work?

### Coverage decision

Complete at `coverage_profile: standard`. The source page and linked concept pages cover the central contribution, metrics, evidence, limitations, and relation to existing cytoskeleton segmentation pages.

### Known gaps

- The wiki does not reproduce the full layer-by-layer architecture or training implementation.
- Dataset availability and exact annotation provenance would need follow-up before reuse.
