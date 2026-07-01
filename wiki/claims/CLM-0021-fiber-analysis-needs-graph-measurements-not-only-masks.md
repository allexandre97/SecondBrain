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
  - fiber-analysis
  - graph-measurements
related:
  - "[[wiki/concepts/cytoskeleton-segmentation-and-tracing]]"
  - "[[wiki/concepts/topology-aware-fiber-network-reconstruction]]"
  - "[[wiki/concepts/filament-instance-and-semantic-segmentation]]"
sources:
  - SRC-0004
  - SRC-0030
  - SRC-0031
  - SRC-0034
  - SRC-0035
  - SRC-0064
sensitivity: public
encryption: none
---

# Fiber Analysis Needs Graph Measurements, Not Only Masks

## Claim

Many biological fiber-analysis questions require centerlines, endpoints, junctions, lengths, curvature, branch connectivity, or per-filament instances, so a binary foreground mask is often only an intermediate product. [SRC-0004; SRC-0030; SRC-0031; SRC-0034; SRC-0035; SRC-0064]

## Scope

This claim is most relevant to cytoskeletal, collagen, vessel-like, and STED tau-fiber workflows where biological interpretation depends on object geometry or network organization. It is less central when the task is only foreground area or coarse occupancy. [SRC-0004]

## Evidence

- SRC-0004 distinguishes semantic segmentation, instance segmentation, tracing, and tracking as different cytoskeletal-image tasks. [SRC-0004]
- SRC-0030 motivates instance-level filament extraction by the need to count filaments and measure individual length, curvature, and motion. [SRC-0030]
- SRC-0031 combines binary segmentation, endpoint and junction detection, and fast marching to estimate actin filament number and length. [SRC-0031]
- SRC-0034 reconstructs 3D fibers, junctions, and graph connectivity for biological fiber networks. [SRC-0034]
- SRC-0035 extracts centerlines and junctions for quantitative 2D and 3D biopolymer-network analysis. [SRC-0035]
- SRC-0064 frames the unfinished tau-project analysis around morphology and image-analysis measurements, where masks alone would not capture fiber organization. [SRC-0064]

## Links

- [[wiki/concepts/cytoskeleton-segmentation-and-tracing]]
- [[wiki/concepts/topology-aware-fiber-network-reconstruction]]
- [[wiki/concepts/filament-instance-and-semantic-segmentation]]
