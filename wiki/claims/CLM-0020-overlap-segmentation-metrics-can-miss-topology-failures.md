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
  - research/computer-vision/biomedical-imaging
  - research/bioimage-analysis/filament-segmentation
tags:
  - claim
  - segmentation-metrics
  - topology
related:
  - "[[wiki/concepts/topology-aware-tubular-structure-segmentation]]"
  - "[[wiki/concepts/topology-aware-fiber-network-reconstruction]]"
  - "[[wiki/claims/CLM-0003-cldice-connectivity-aware-tubular-segmentation]]"
sources:
  - SRC-0004
  - SRC-0029
  - SRC-0032
  - SRC-0033
  - SRC-0034
  - SRC-0069
sensitivity: public
encryption: none
---

# Overlap Segmentation Metrics Can Miss Topology Failures

## Claim

For thin or curvilinear biological structures, high foreground-overlap scores can still hide broken centerlines, missing branches, spurious connections, or disconnected fine structures that matter for downstream analysis. [SRC-0004; SRC-0029; SRC-0032; SRC-0033; SRC-0034; SRC-0069]

## Scope

This claim applies to filament, vessel, cytoskeletal, and fiber-network image analysis where the desired output is not only a mask but also a connected structure or graph. It does not imply that overlap metrics are useless; it means they are insufficient alone for topology-sensitive questions. [SRC-0004; SRC-0032]

## Evidence

- SRC-0004 separates foreground segmentation from tracing and tracking, and notes that cytoskeletal-network analysis depends on geometry and connectivity, not only pixels. [SRC-0004]
- SRC-0029 introduces skeletonized IoU because ordinary pixel IoU can be poorly aligned with thin-filament biological usefulness. [SRC-0029, section 4.1]
- SRC-0032 proposes clDice to make tubular segmentation evaluation more sensitive to skeleton-mask connectivity. [SRC-0032, section 2]
- SRC-0033 treats vessel segmentation, centerline prediction, and bifurcation detection as distinct sparse tasks. [SRC-0033]
- SRC-0034 evaluates reconstructed edge-length, orientation, and node recovery rather than relying on mask overlap alone. [SRC-0034]
- SRC-0069 reports that a general segmentation model can miss fine structures and small disconnected components, which is directly relevant to thin microscopy structures. [SRC-0069, section 7.6]

## Links

- [[wiki/concepts/topology-aware-tubular-structure-segmentation]]
- [[wiki/concepts/topology-aware-fiber-network-reconstruction]]
- [[wiki/claims/CLM-0003-cldice-connectivity-aware-tubular-segmentation]]
