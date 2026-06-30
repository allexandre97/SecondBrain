---
type: source
status: active
created: 2026-06-30
updated: 2026-06-30
source_id: SRC-0033
display_title: "DeepVesselNet: Vessel Segmentation, Centerline Prediction, and Bifurcation Detection in 3-D Angiographic Volumes"
short_title: "DeepVesselNet"
aliases:
  - "SRC-0033"
  - "DeepVesselNet"
  - "DeepVesselNet: Vessel Segmentation, Centerline Prediction, and Bifurcation Detection in 3-D Angiographic Volumes"
source_path: raw/sources/SRC-0033-deepvesselnet-vessel-segmentation-centerline-prediction-and-bifurcation-detection.pdf
original_filename: "Tet18.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 1e1c4eb2ffb0b4e17130c417463eba22af1f312ff1eafe8b5537290b882c6607
areas:
  - research
categories:
  - research/computer-vision/biomedical-imaging
  - research/machine-learning/scientific-modeling
tags:
  - vessel-segmentation
  - centerline-prediction
  - bifurcation-detection
  - deep-learning
related:
  - "[[concepts/topology-aware-tubular-structure-segmentation]]"
  - "[[concepts/deep-learning-cytoskeleton-image-analysis]]"
sources:
  - SRC-0033
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: standard
---

# DeepVesselNet: Vessel Segmentation, Centerline Prediction, and Bifurcation Detection in 3-D Angiographic Volumes

Source ID: `SRC-0033`

## Raw source

- Repository path: `raw/sources/SRC-0033-deepvesselnet-vessel-segmentation-centerline-prediction-and-bifurcation-detection.pdf`
- Local relative link: [Open raw source](../../raw/sources/SRC-0033-deepvesselnet-vessel-segmentation-centerline-prediction-and-bifurcation-detection.pdf)

## Summary

Tetteh et al. present DeepVesselNet, a neural architecture for extracting vascular networks and features from 3D angiographic volumes. It addresses memory and speed limits of full 3D convolution, extreme class imbalance in vessel/centerline/bifurcation labels, and scarcity of annotated 3D vessel data. [SRC-0033]

## Key Points

- DeepVesselNet uses cross-hair filters built from orthogonal 2D filters to retain 3D context with lower computational cost than full 3D convolutions. [SRC-0033, sections 1 and 3.3.1]
- A class-balancing cross-entropy loss with false-positive-rate correction is introduced to avoid precision/recall imbalance in sparse vessel, centerline, and bifurcation prediction. [SRC-0033, sections 1 and 3.3.2]
- The authors generate synthetic vascular trees with labels for vessel segmentation, centerlines, and bifurcations, then use them for pretraining and transfer to clinical MRA and micro-CTA data. [SRC-0033, section 3.1]
- Cross-hair filters reduce parameter count and execution time relative to corresponding full 3D VNet and UNet variants; for example, DeepVesselNet-UNet uses 4.45 million convolutional parameters versus 7.41 million for UNet. [SRC-0033, table 1]
- On TOF MRA vessel segmentation, finetuned DeepVesselNet-FCN reports precision 86.44, recall 86.93, and Dice 86.68. [SRC-0033, table 3]
- For bifurcation detection, DeepVesselNet-FCN reports precision 78.80, recall 92.97, detection 86.87%, and mean error 0.209 voxels. [SRC-0033, table 5]

## Limitations

- The paper studies vascular networks, not cytoskeletal or collagen fibers directly, so transfer to other filament systems is conceptual unless separately validated. [SRC-0033]
- Centerline and bifurcation prediction remain difficult because target structures are voxel-sized and extremely sparse. [SRC-0033, sections 1 and 4]
- The authors suggest future integrated hierarchical or multi-level approaches rather than treating vessel segmentation, centerline prediction, and bifurcation detection only as separate binary tasks. [SRC-0033, section 4]

## Links

- [[concepts/topology-aware-tubular-structure-segmentation]]
- [[concepts/deep-learning-cytoskeleton-image-analysis]]

## Ingestion QA

### Retrieval questions checked

- What challenges does DeepVesselNet address?
- What are cross-hair filters?
- Why is class balancing needed?
- How is synthetic data used?
- What tasks are evaluated?
- What are the main performance signals?
- How does this relate to fiber or cytoskeletal image analysis?

### Coverage decision

Complete at `coverage_profile: standard`. The page covers the architecture, training strategy, datasets, results, limitations, and its relevance as adjacent tubular-network methodology.

### Known gaps

- The wiki does not reproduce the full loss-function derivation.
- Dataset download details and code availability are noted only at a high level.
