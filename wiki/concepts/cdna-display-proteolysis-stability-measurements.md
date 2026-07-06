---
type: concept
status: active
created: 2026-07-02
updated: 2026-07-02
areas:
  - research
categories:
  - research/biomolecules/proteins
  - research/experimental-benchmarking
  - research/data-management
  - research/machine-learning/scientific-modeling
tags:
  - proteins
  - protein-stability
  - cDNA-display
  - proteolysis
  - deep-mutational-scanning
related:
  - "[[wiki/concepts/protein-energy-landscape-profiling]]"
  - "[[wiki/concepts/human-domainome-variant-stability-mapping]]"
  - "[[wiki/claims/CLM-0030-cdna-display-proteolysis-is-scalable-but-assumption-limited]]"
sources:
  - SRC-0070
  - SRC-0071
sensitivity: public
encryption: none
---

# cDNA Display Proteolysis Stability Measurements

## Summary

cDNA display proteolysis is a high-throughput protein-stability assay that links each protein variant to its encoding cDNA, exposes pooled protein-cDNA complexes to protease titrations, and uses sequencing counts to infer folding free energies for very large libraries. SRC-0070 uses the method to curate 776,298 high-quality folding stabilities across natural and designed small protein domains. [SRC-0070]

## Key Points

- The assay depends on unfolded proteins being cleaved faster than folded proteins, so protease resistance can be converted into folding-stability estimates when the folding and cleavage assumptions hold. [SRC-0070]
- Orthogonal trypsin and chymotrypsin experiments help correct for protease-specific unfolded-state susceptibility and identify unreliable measurements. [SRC-0070]
- The method scales deep mutational scanning from individual proteins to hundreds of small domains under common experimental conditions. [SRC-0070]
- The resulting data support analyses of amino acid fitness environments, pairwise and higher-order thermodynamic couplings, evolutionary amino acid usage, and protein-design methods. [SRC-0070]
- The method complements protein energy-landscape profiling: cDNA display proteolysis measures global folding stability at much larger variant scale, while mHDX-MS-style profiling can expose partially open conformational states. [SRC-0067] [SRC-0070]

## Evidence

- SRC-0070 reports about 1.8 million measurements and a curated set of 776,298 high-quality folding stabilities.
- SRC-0070 compares cDNA display proteolysis results with traditional purified-protein measurements for 1,188 variants of 10 proteins and reports Pearson correlations above 0.75.
- SRC-0070 reports trypsin/chymotrypsin agreement of `R = 0.94` for the combined high-quality stability estimates.
- SRC-0070 uses the dataset to identify 2,600 mutations that increase folding stability by at least 1 kcal mol^-1.
- SRC-0071 uses high-throughput proteolysis stability data from SRC-0070 as an external comparison for its aPCA abundance measurements.

## Links

- [[wiki/sources/SRC-0070-mega-scale-experimental-analysis-of-protein-folding-stability]]
- [[wiki/sources/SRC-0071-site-saturation-mutagenesis-of-500-human-protein-domains]]
- [[wiki/sources/SRC-0067-protein-energy-landscape-discovery-analysis-design]]
- [[wiki/concepts/protein-energy-landscape-profiling]]
- [[wiki/concepts/human-domainome-variant-stability-mapping]]
- [[wiki/claims/CLM-0030-cdna-display-proteolysis-is-scalable-but-assumption-limited]]

## Caveats

- The assay can underestimate stability when folded or partially folded states are cleaved without global unfolding. [SRC-0070]
- Stability estimates become unreliable near folded-state or unfolded-state protease-susceptibility limits and for proteins outside the assay's dynamic range. [SRC-0070]
- Applicability to larger, less cooperative, complex-stabilized, aggregating, or difficult-to-express proteins remains limited. [SRC-0070]

## Open Questions

- How should cDNA-display stability datasets be combined with local opening-energy data to benchmark protein simulation and design models?
- Which assay filters best predict when an individual variant-level stability estimate is trustworthy enough for model training?
