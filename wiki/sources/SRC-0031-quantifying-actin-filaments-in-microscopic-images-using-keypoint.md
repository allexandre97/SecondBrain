---
type: source
status: active
created: 2026-06-30
updated: 2026-06-30
source_id: SRC-0031
display_title: "Quantifying Actin Filaments in Microscopic Images Using Keypoint Detection and Fast Marching"
short_title: "Actin Filament Quantification"
aliases:
  - "SRC-0031"
  - "Actin Filament Quantification"
  - "Quantifying Actin Filaments in Microscopic Images Using Keypoint Detection and Fast Marching"
source_path: raw/sources/SRC-0031-quantifying-actin-filaments-in-microscopic-images-using-keypoint.pdf
original_filename: "Liu20.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: bd5642d9e200725b68382d716dbf193c6cddf5de354006702e9cf05d33c6d683
areas:
  - research
categories:
  - research/bioimage-analysis/cytoskeleton
  - research/computer-vision/biomedical-imaging
tags:
  - actin
  - filament-quantification
  - keypoint-detection
  - fast-marching
related:
  - "[[concepts/filament-instance-and-semantic-segmentation]]"
  - "[[concepts/cytoskeleton-segmentation-and-tracing]]"
sources:
  - SRC-0031
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: standard
---

# Quantifying Actin Filaments in Microscopic Images Using Keypoint Detection and Fast Marching

Source ID: `SRC-0031`

## Raw source

- Repository path: `raw/sources/SRC-0031-quantifying-actin-filaments-in-microscopic-images-using-keypoint.pdf`
- Local relative link: [Open raw source](../../raw/sources/SRC-0031-quantifying-actin-filaments-in-microscopic-images-using-keypoint.pdf)

## Summary

Liu et al. propose a hybrid pipeline for estimating actin filament count and length in microscopy images. The workflow first segments actin filaments with a CNN, detects junctions and endpoints with a ResNet-based keypoint detector trained on synthetic data, then uses fast marching to infer paths and filament lengths. [SRC-0031]

## Key Points

- The paper targets quantification rather than only segmentation: actin filament number and length are treated as core measurements for studying dynamic actin networks. [SRC-0031, section 1]
- The actin dataset contains 10 microscopy images of size 1740 x 840 pixels with 17 z-slices projected by maximum intensity projection. [SRC-0031, section 3.1.1]
- Synthetic keypoint data are generated because real junction and endpoint labels are unavailable; images contain random one-pixel curves with junction types, then dilation makes them resemble binary segmentation outputs. [SRC-0031, section 3.1.2]
- Fast marching computes geodesic distances from junctions and endpoints; doubled local peak values estimate filament lengths, and peak counts estimate filament counts. [SRC-0031, section 3.4]
- In two manually counted images, the proposed method's counts are closer to manual counts than SOAX or a skeleton-disconnect baseline: 2576 vs. manual 2210 and 818 vs. manual 743. [SRC-0031, table 2]

## Limitations

- Only two images were manually counted for direct ground-truth comparison, because dense actin annotation is labor-intensive. [SRC-0031, section 4]
- The method cannot yet quantify orientation angles or curvatures, which the authors identify as future work. [SRC-0031, section 5]
- The pipeline depends on the quality of the prior binary segmentation and synthetic-to-real transfer for keypoint detection. [SRC-0031, sections 3.2-3.3]

## Links

- [[concepts/filament-instance-and-semantic-segmentation]]
- [[concepts/cytoskeleton-segmentation-and-tracing]]

## Ingestion QA

### Retrieval questions checked

- What quantity does this paper estimate?
- How are junctions and endpoints detected?
- Why is synthetic training data used?
- How does fast marching turn keypoints into length estimates?
- What evidence supports the method?
- What limitations remain?

### Coverage decision

Complete at `coverage_profile: standard`. The page preserves the pipeline, dataset, evaluation evidence, and validation limits needed for later retrieval.

### Known gaps

- The wiki does not reproduce the full fast-marching implementation or threshold settings.
- Ground-truth coverage is thin in the source itself, so broad accuracy claims should stay limited.
