---
type: claim
status: active
created: 2026-07-01
updated: 2026-07-01
claim_status: limited
claim_scope: cross-source
areas:
  - research
categories:
  - research/molecular-simulation/free-energy
  - research/computational-drug-discovery
  - research/experimental-benchmarking
tags:
  - claim
  - rbfe
  - benchmark-metrics
  - alchemical-networks
related:
  - "[[wiki/concepts/relative-binding-free-energy-benchmarking]]"
  - "[[wiki/questions/rbfe-benchmark-prospective-use-scope]]"
sources:
  - SRC-0045
  - SRC-0061
  - SRC-0062
sensitivity: public
encryption: none
---

# Edgewise RBFE Metrics Can Overstate Arbitrary Comparison Quality

## Claim

Edgewise RBFE benchmark metrics can be more optimistic than all-to-all pairwise metrics because planned alchemical networks preferentially include easier or more similar ligand transformations, while medicinal-chemistry use may require arbitrary comparisons within a series. [SRC-0061]

## Scope

This claim applies to RBFE benchmark metric design. It does not mean edgewise metrics are useless; they diagnose simulated transformations directly, while all-to-all metrics better represent arbitrary ranking and pairwise comparison quality. [SRC-0045] [SRC-0061]

## Evidence

- SRC-0061 reports both edgewise and all-to-all pairwise metrics and states that edgewise results are more optimistic because network planning connects more similar ligands. [SRC-0061, section 3.1.1]
- SRC-0045 uses the same all-to-all pairwise framing in the preprint benchmark. [SRC-0045]
- SRC-0062 adds convergence, redundant-edge removal, and edge-difficulty analyses, showing that edge-level diagnostics are useful but not sufficient as the only benchmark summary. [SRC-0062, sections S5-S7]

## Caveats

- All-to-all metrics can also hide mechanism-specific failures; a useful benchmark should report both network-edge behavior and task-oriented pairwise/ranking behavior. [SRC-0061] [SRC-0062]

## Links

- [[wiki/sources/SRC-0045-large-scale-collaborative-assessment-of-binding-free-energy]]
- [[wiki/sources/SRC-0061-openfe-rbfe-benchmark-journal-version]]
- [[wiki/sources/SRC-0062-openfe-rbfe-benchmark-supporting-information]]
- [[wiki/concepts/relative-binding-free-energy-benchmarking]]
- [[wiki/questions/rbfe-benchmark-prospective-use-scope]]
