---
type: tension
status: active
created: 2026-07-01
updated: 2026-07-01
tension_status: active
areas:
  - research
categories:
  - research/bioimage-analysis/filament-segmentation
  - research/computer-vision/biomedical-imaging
tags:
  - tension
  - STED
  - segmentation
  - domain-adaptation
related:
  - "[[wiki/concepts/deep-learning-cytoskeleton-image-analysis]]"
  - "[[wiki/concepts/self-configuring-u-net-medical-image-segmentation]]"
  - "[[wiki/concepts/promptable-segmentation-foundation-models]]"
related_claims:
  - "[[wiki/claims/CLM-0020-overlap-segmentation-metrics-can-miss-topology-failures]]"
  - "[[wiki/claims/CLM-0021-fiber-analysis-needs-graph-measurements-not-only-masks]]"
related_questions:
  - "[[wiki/questions/sted-tau-fiber-analysis-validation-scope]]"
sources:
  - SRC-0004
  - SRC-0063
  - SRC-0064
  - SRC-0068
  - SRC-0069
sensitivity: private
encryption: none
---

# General Segmentation Frameworks Versus STED Fiber Domain Adaptation

## Tension

General segmentation systems can provide strong baselines and fast annotation workflows, but STED/tau-fiber analysis may need domain adaptation, topology-aware postprocessing, and morphology-specific validation before outputs support biological conclusions. [SRC-0004; SRC-0063; SRC-0064; SRC-0068; SRC-0069]

## Positions

- SRC-0068 presents nnU-Net as a self-configuring framework that can perform strongly across biomedical segmentation tasks. [SRC-0068]
- SRC-0069 presents SAM as a promptable segmentation model with broad zero-shot transfer and fast interactive use after image encoding. [SRC-0069]
- SRC-0004 and the STED/tau sources emphasize that microscopy modality, fine structures, connectivity, and downstream biological measurement determine whether segmentation is scientifically adequate. [SRC-0004; SRC-0063; SRC-0064]
- SRC-0069's own limitations include missed fine structures and small disconnected components, which are failure modes for fiber analysis. [SRC-0069, section 7.6]

## Resolution Status

Active. General frameworks can be included as baselines or annotation aids, but the SRC-0064-style workflow still needs validation on STED/tau morphology outputs rather than only foreground masks. [SRC-0064]

## Links

- [[wiki/questions/sted-tau-fiber-analysis-validation-scope]]
- [[wiki/concepts/deep-learning-cytoskeleton-image-analysis]]
- [[wiki/concepts/self-configuring-u-net-medical-image-segmentation]]
- [[wiki/concepts/promptable-segmentation-foundation-models]]
