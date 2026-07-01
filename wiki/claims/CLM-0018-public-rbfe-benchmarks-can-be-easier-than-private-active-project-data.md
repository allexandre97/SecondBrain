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
  - benchmark-representativeness
  - drug-discovery
related:
  - "[[wiki/concepts/relative-binding-free-energy-benchmarking]]"
  - "[[wiki/tensions/TEN-0010-rbfe-benchmark-success-vs-prospective-use]]"
sources:
  - SRC-0045
  - SRC-0046
  - SRC-0061
  - SRC-0062
sensitivity: public
encryption: none
---

# Public RBFE Benchmarks Can Be Easier Than Private Active-Project Data

## Claim

Curated public RBFE benchmarks can look easier than blinded private active-project datasets, so retrospective public accuracy should not be treated as prospective drug-discovery accuracy without qualification. [SRC-0045] [SRC-0046] [SRC-0061]

## Scope

This claim covers RBFE/FEP benchmark representativeness, not every difference between public and private datasets. The causes include data curation, setup quality, assay limits, transformation class, and project-stage heterogeneity. [SRC-0061] [SRC-0062]

## Evidence

- SRC-0061 reports substantially better weighted all-to-all pairwise RMSE on 58 public systems than on 37 blinded private industry datasets. [SRC-0061, sections 3.1.1 and 3.2]
- SRC-0061 attributes private-set difficulty partly to assay-limit, stereochemical, tautomer, pose, water, metal, and large-transformation issues. [SRC-0061, section 4.2]
- SRC-0062 documents private problematic-ligand notes and protocol/outlier diagnostics that are not captured by a single aggregate RMSE. [SRC-0062]
- SRC-0046 cautions that retrospective FEP benchmarks can be optimistic relative to prospective drug-discovery use, especially when careful expert preparation is applied. [SRC-0046]

## Caveats

- Public benchmarks remain useful for reproducibility and method comparison; the problem is overgeneralizing public benchmark performance to live project performance. [SRC-0061]

## Links

- [[wiki/sources/SRC-0045-large-scale-collaborative-assessment-of-binding-free-energy]]
- [[wiki/sources/SRC-0046-the-maximal-and-current-accuracy-of-rigorous-protein]]
- [[wiki/sources/SRC-0061-openfe-rbfe-benchmark-journal-version]]
- [[wiki/sources/SRC-0062-openfe-rbfe-benchmark-supporting-information]]
- [[wiki/concepts/relative-binding-free-energy-benchmarking]]
- [[wiki/tensions/TEN-0010-rbfe-benchmark-success-vs-prospective-use]]
