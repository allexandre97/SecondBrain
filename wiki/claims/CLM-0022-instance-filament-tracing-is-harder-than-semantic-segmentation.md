---
type: claim
status: active
created: 2026-07-01
updated: 2026-07-01
claim_status: supported
claim_scope: cross-source
areas:
  - research
categories:
  - research/bioimage-analysis/filament-segmentation
  - research/computer-vision/biomedical-imaging
tags:
  - claim
  - instance-segmentation
  - filament-tracing
related:
  - "[[wiki/concepts/filament-instance-and-semantic-segmentation]]"
  - "[[wiki/concepts/cytoskeleton-segmentation-and-tracing]]"
sources:
  - SRC-0004
  - SRC-0029
  - SRC-0030
  - SRC-0031
  - SRC-0035
sensitivity: public
encryption: none
---

# Instance Filament Tracing Is Harder Than Semantic Segmentation

## Claim

Separating individual filaments in dense networks is harder than labeling filament foreground, because crossings, overlaps, uniform appearance, noise, and blurred structures make object identity ambiguous. [SRC-0004; SRC-0029; SRC-0030; SRC-0031; SRC-0035]

## Scope

This claim applies to microscopy filament networks where downstream analysis depends on individual objects or graph structure. It does not deny the value of semantic segmentation as a first stage. [SRC-0029; SRC-0031]

## Evidence

- SRC-0029 improves semantic segmentation but explicitly leaves full instance reconstruction and time tracking as future work. [SRC-0029, section 5]
- SRC-0030 contrasts semantic segmentation with instance-level filament extraction and uses orientation-aware branches plus terminus pairing to handle intersections. [SRC-0030]
- SRC-0031 treats length and count estimation as requiring segmentation plus keypoint detection and graph traversal, not segmentation alone. [SRC-0031]
- SRC-0035 uses active-contour centerline extraction and local connectivity repair because network tracing is not equivalent to thresholding foreground pixels. [SRC-0035]

## Links

- [[wiki/concepts/filament-instance-and-semantic-segmentation]]
- [[wiki/concepts/cytoskeleton-segmentation-and-tracing]]
