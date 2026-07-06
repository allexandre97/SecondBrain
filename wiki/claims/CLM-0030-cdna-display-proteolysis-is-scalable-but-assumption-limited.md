---
type: claim
status: active
created: 2026-07-02
updated: 2026-07-02
claim_status: supported
claim_scope: method
areas:
  - research
categories:
  - research/biomolecules/proteins
  - research/experimental-benchmarking
  - research/data-management
tags:
  - claim
  - protein-stability
  - cDNA-display
  - assay-validation
related:
  - "[[wiki/concepts/cdna-display-proteolysis-stability-measurements]]"
  - "[[wiki/concepts/protein-energy-landscape-profiling]]"
sources:
  - SRC-0070
sensitivity: public
encryption: none
---

# cDNA Display Proteolysis Is Scalable but Assumption-Limited

## Claim

cDNA display proteolysis can scale absolute folding-stability measurements to hundreds of thousands of protein variants, but individual stability estimates should be trusted only within the assay's assumptions about expression, cooperative folding, equilibrium, protease susceptibility, cleavage-linked cDNA release, and dynamic range. [SRC-0070]

## Evidence

- SRC-0070 reports up to about 900,000 sequences per one-week experiment and curates 776,298 high-quality folding stabilities from about 1.8 million measurements. [SRC-0070]
- Validation against purified-protein measurements across 1,188 variants of 10 proteins produced Pearson correlations above 0.75, supporting the method for cooperative small domains. [SRC-0070]
- The source explicitly lists failure modes including cleavage from folded or partially folded states, inaccurate unfolded-state susceptibility estimates, non-equilibrium or aggregating behavior, and cleavage rates outside the measurable range. [SRC-0070]

## Implementation Use

Use cDNA-display proteolysis data as large-scale experimental supervision for protein-stability modelling only after preserving assay filters and provenance. For variant-level decisions, treat measurements near dynamic-range boundaries, low-quality protease agreement, non-cooperative domains, and unvalidated designed structures as requiring follow-up review. [SRC-0070]

## Links

- [[wiki/sources/SRC-0070-mega-scale-experimental-analysis-of-protein-folding-stability]]
- [[wiki/concepts/cdna-display-proteolysis-stability-measurements]]
