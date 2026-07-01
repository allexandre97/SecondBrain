---
type: concept
status: active
created: 2026-07-01
updated: 2026-07-01
areas:
  - research
categories:
  - research/biomolecules/proteins
  - research/computer-vision/biomedical-imaging
tags:
  - tau
  - tauopathy
  - neuronal-culture
  - seeded-aggregation
  - cryo-EM
  - STED
related:
  - "[[wiki/concepts/super-resolution-imaging-of-tau-pathology]]"
  - "[[wiki/concepts/topology-aware-tubular-structure-segmentation]]"
sources:
  - SRC-0064
  - SRC-0004
  - SRC-0029
  - SRC-0030
  - SRC-0032
  - SRC-0034
sensitivity: private
encryption: none
---

# Neuronal Templated Tau Assembly Systems

## Summary

Neuronal templated tau assembly systems are culture models designed to test whether disease-derived tau seeds can induce expressed tau to assemble into disease-relevant filaments inside neurons. SRC-0064 reports a draft mixed primary murine cortical culture system using AAV-mediated expression of full-length human tau isoforms, brain-derived tau seeds, biochemical extraction, cryo-EM, live imaging, and STED microscopy. [SRC-0064]

## Key Points

- The model-system goal is to preserve a neuronal cellular environment while retaining experimental control over the tau construct, isoform, tag, mutation, promoter, and seed source. [SRC-0064]
- AAV-mediated expression makes the system modular compared with fixed transgenic lines, but also raises overexpression and viral-titre caveats. [SRC-0064]
- In the draft, AD seeds are reported to template HA-tagged tau assemblies whose cryo-EM structure matches Alzheimer's paired helical filaments; the V337M construct is used to help rule out simple re-extraction of input seed. [SRC-0064]
- The manuscript positions STED morphology as a way to compare aggregate organization across seeds from different tauopathies, while noting that quantification is still in progress. [SRC-0064]
- Because the STED readout is filament and bundle morphology rather than only aggregate presence, a reusable analysis target is a topology-aware segmentation-to-graph pipeline: U-Net-like mask prediction, centerline and junction-aware outputs, topology-preserving losses such as soft-clDice, and graph extraction for length, curvature, connectedness, branch, and bundle-width comparisons. [SRC-0004] [SRC-0029] [SRC-0030] [SRC-0032] [SRC-0034] See [[wiki/answers/sted-tau-filament-topology-model-architecture]].

## Evidence

- SRC-0064 reports pFTAA and AT100 co-labelling, sarkosyl-insoluble tau, immuno-EM, and cryo-EM readouts after AD seeding.
- SRC-0064 reports late-stage STED morphology differences between AD-, Pick's disease-, corticobasal degeneration-, and progressive supranuclear palsy-seeded cultures.

## Links

- [[wiki/sources/SRC-0064-versatile-neuronal-culture-system-templated-tau-assembly]]
- [[wiki/concepts/super-resolution-imaging-of-tau-pathology]]
- [[wiki/concepts/topology-aware-tubular-structure-segmentation]]
- [[wiki/answers/sted-tau-filament-topology-model-architecture]]

## Caveats

- SRC-0064 is an unpublished manuscript draft, not a peer-reviewed article.
- Seed concentration, endogenous mouse tau, culture maturity, and tau overexpression are explicit interpretation boundaries for this model system. [SRC-0064]

## Open Questions

- How much seed can be used before re-extraction becomes a practical cryo-EM confound?
- Which STED morphology features remain robust after full quantification across donors, tauopathy classes, time points, and culture batches?
