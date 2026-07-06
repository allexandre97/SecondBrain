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
  - human-domainome
  - missense-variants
  - protein-stability
  - variant-effect-prediction
related:
  - "[[wiki/concepts/cdna-display-proteolysis-stability-measurements]]"
  - "[[wiki/claims/CLM-0031-stability-explains-many-but-not-all-missense-effects]]"
sources:
  - SRC-0071
sensitivity: public
encryption: none
---

# Human Domainome Variant-Stability Mapping

## Summary

Human domainome variant-stability mapping uses high-throughput mutagenesis of many human protein domains to measure how missense variants affect domain abundance and inferred stability. SRC-0071 shows that this can be scaled to hundreds of domains and more than half a million measured variants, creating a reference dataset for clinical variant interpretation and computational variant-effect prediction. [SRC-0071]

## Key Points

- Domain-level saturation mutagenesis makes broad human variant-effect measurement experimentally tractable because domains are smaller and often independently folding. [SRC-0071]
- aPCA measures cellular abundance effects, which correlate with folding-stability changes but are still an assay-specific proxy. [SRC-0071]
- The dataset supports mechanistic interpretation of missense variants by separating stability-driven effects from likely functional-site effects. [SRC-0071]
- Combining abundance data with protein language model predictions can identify residues where evolutionary fitness is affected more than stability alone predicts. [SRC-0071]
- Homologous-domain energy models suggest that representative domain mutagenesis can support stability-effect prediction across full protein families. [SRC-0071]

## Evidence

- SRC-0071 reports 563,534 measured variants in 522 retained domains.
- SRC-0071 reports median replicate Pearson correlation `r = 0.85`.
- SRC-0071 reports that about 60% of pathogenic missense variants reduce protein stability.
- SRC-0071 validates abundance effects against independent in vitro folding data and high-throughput proteolysis data from SRC-0070.

## Links

- [[wiki/sources/SRC-0071-site-saturation-mutagenesis-of-500-human-protein-domains]]
- [[wiki/sources/SRC-0070-mega-scale-experimental-analysis-of-protein-folding-stability]]
- [[wiki/concepts/cdna-display-proteolysis-stability-measurements]]
- [[wiki/claims/CLM-0031-stability-explains-many-but-not-all-missense-effects]]

## Caveats

- Isolated-domain measurements may miss full-length protein context, interactions, localization, or regulation. [SRC-0071]
- Abundance assays do not directly measure all mechanisms of disease, such as altered binding specificity, gain of function, aggregation, localization, or allostery. [SRC-0071]
- Domains that fail quality filters are themselves informative but are not part of the main high-confidence dataset. [SRC-0071]

## Open Questions

- How often do isolated-domain abundance effects transfer quantitatively to full-length proteins and native cellular contexts?
- Which additional assays should be paired with abundance maps to classify non-stability disease mechanisms?
