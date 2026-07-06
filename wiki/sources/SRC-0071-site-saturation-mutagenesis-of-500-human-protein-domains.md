---
type: source
status: active
created: 2026-07-02
updated: 2026-07-02
source_id: SRC-0071
display_title: "Site-saturation mutagenesis of 500 human protein domains"
short_title: "Human Domainome 1"
aliases:
  - "SRC-0071"
  - "Human Domainome 1"
  - "Site-saturation mutagenesis of 500 human protein domains"
source_path: raw/sources/SRC-0071-site-saturation-mutagenesis-of-500-human-protein-domains.pdf
imported_path: raw/sources/SRC-0071-site-saturation-mutagenesis-of-500-human-protein-domains.pdf
original_filename: "s41586-024-08370-4.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: cbcf88bbd8440e9ec6c8f284d8cd16189778c148b5569f167fd4ce9522976926
authors:
  - "Antoni Beltran"
  - "Xiang'er Jiang"
  - "Yue Shen"
  - "Ben Lehner"
author_entities: []
year: 2025
venue: "Nature"
doi: "10.1038/s41586-024-08370-4"
arxiv:
metadata_review_status: reviewed
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
  - missense-variants
  - variant-effect-prediction
  - deep-mutational-scanning
  - human-domainome
related:
  - "[[wiki/concepts/human-domainome-variant-stability-mapping]]"
  - "[[wiki/concepts/cdna-display-proteolysis-stability-measurements]]"
  - "[[wiki/claims/CLM-0031-stability-explains-many-but-not-all-missense-effects]]"
sources:
  - SRC-0071
cites_sources:
  - SRC-0070
citation_match_status: partial
cqt_review_status: linked
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: standard
peer_review_status: peer-reviewed
---

# Site-Saturation Mutagenesis of 500 Human Protein Domains

Source ID: `SRC-0071`

## Raw source

- Repository path: `raw/sources/SRC-0071-site-saturation-mutagenesis-of-500-human-protein-domains.pdf`
- Open raw source: [raw/sources/SRC-0071-site-saturation-mutagenesis-of-500-human-protein-domains.pdf](../../raw/sources/SRC-0071-site-saturation-mutagenesis-of-500-human-protein-domains.pdf)

## Status note

This is a peer-reviewed Nature article published online on 2025-01-08 and in volume 637 on 2025-01-23. [SRC-0071]

## Summary

Beltran et al. report Human Domainome 1, a large-scale site-saturation mutagenesis dataset measuring effects of human missense variants on cellular abundance of protein domains. Using microchip-based massive parallel DNA synthesis and an abundance protein fragment complementation assay (aPCA), the study quantifies 563,534 variants in 522 protein domains after filtering, including 503 domains from human proteins. The paper uses the dataset to connect missense effects with stability, pathogenicity, functional-site annotation, and family-level stability prediction. [SRC-0071]

## Key Points

- The initial library designed 1,230,584 amino acid variants across 1,248 domains, mutating every amino acid position to all 19 alternatives. [SRC-0071]
- After 27 transformation, selection, and sequencing experiments and quality filtering, the final dataset contains abundance measurements for 563,534 variants in 522 domains. [SRC-0071]
- The retained domains span 127 domain families and include 275 domains encoded by human disease genes, with 108 domains containing annotated pathogenic variants. [SRC-0071]
- aPCA abundance measurements were reproducible, with median Pearson correlation `r = 0.85` between replicates. [SRC-0071]
- The abundance measurements correlated with independent in vitro folding free-energy data and with high-throughput proteolysis stability measurements from SRC-0070. [SRC-0071] [SRC-0070]
- The paper estimates that about 60% of pathogenic missense variants reduce protein stability, with stability effects especially important for recessive disorders. [SRC-0071]
- Combining abundance-derived stability effects with ESM1v evolutionary-fitness predictions identifies variants and residues whose evolutionary effects are larger than expected from stability alone, enriching for annotated functional sites. [SRC-0071]
- Family-level two-state thermodynamic models fitted with MoCHI suggest that stability effects are largely conserved across homologous domains, enabling prediction of stability effects across entire domain families. [SRC-0071]

## Methods and Measurements

- The assay uses aPCA, where a domain is fused to part of an essential enzyme; unstable variants reduce enzyme concentration and cell growth, and sequencing tracks variant frequency changes through selection. [SRC-0071]
- Domain quality filtering retained folded domains with adequate wild-type fitness, replicate correlation, measurement coverage, and expected relationships between mutation effects and structural features such as solvent accessibility. [SRC-0071]
- Functional-site analysis fitted sigmoid relationships between normalized aPCA fitness and ESM1v-predicted fitness, then used residuals to find variants whose evolutionary impact was not explained by stability. [SRC-0071]
- Clinical variant analysis compared aPCA-derived destabilization classes with ClinVar, UniProt, and gnomAD variant classes. [SRC-0071]
- Family modelling used PFAM alignments and MoCHI two-state models with shared folding energies across homologous domains. [SRC-0071]

## Limitations and Caveats

- Human Domainome 1 assays isolated domains rather than full-length proteins, so context-dependent effects from neighbouring domains, localization, interactions, or regulation remain an open issue. [SRC-0071]
- The dataset focuses on small structurally diverse domains and does not yet cover all human proteins, extracellular proteins, transmembrane proteins, insertions, deletions, or complex variants. [SRC-0071]
- Many domains did not produce sufficient aPCA signal or had mutational effects incompatible with simple two-state folding interpretation. [SRC-0071]
- aPCA primarily measures cellular abundance as a proxy for stability; the same variant libraries would need other assays to measure binding, localization, aggregation, allostery, or cell-context-specific abundance. [SRC-0071]
- Computational variant effect predictors remain benchmarked against this dataset, but the source does not claim that any predictor is sufficient alone for clinical classification. [SRC-0071]

## Claims

- [[wiki/claims/CLM-0031-stability-explains-many-but-not-all-missense-effects]]
- Human Domainome 1 is a standardized experimental reference dataset for variant-effect predictors and clinical variant interpretation, but it measures domain abundance rather than every disease mechanism. [SRC-0071]
- Stability effects are sufficiently conserved within many homologous domain families that representative mutagenesis can support family-wide stability prediction. [SRC-0071]

## Links

- [[wiki/concepts/human-domainome-variant-stability-mapping]]
- [[wiki/concepts/cdna-display-proteolysis-stability-measurements]]
- [[wiki/sources/SRC-0070-mega-scale-experimental-analysis-of-protein-folding-stability]]

## Citation Links

- Confirmed cited source: SRC-0071 cites SRC-0070 as the mega-scale protein folding stability study and uses high-throughput proteolysis measurements as external comparison data. [SRC-0071] [SRC-0070]
- Partial citation review: broader bibliography matching was not exhaustive; the targeted review focused on currently ingested protein-stability sources.

## Metadata notes

- DOI shown by the source and PDF metadata: `10.1038/s41586-024-08370-4`.
- Data availability states that sequencing data were deposited in GEO under accession `GSE265942`; aPCA measurements, residuals, family-averaged stability effects, and VEP comparisons are provided in supplementary tables. [SRC-0071]
- Code availability lists analysis code at `github.com/lehner-lab/domainome` and supporting analysis files at Zenodo record `10.5281/zenodo.11043642`. [SRC-0071]

## Ingestion QA

### Retrieval questions checked

- What dataset does the paper introduce?
- How many domains and variants are in the final filtered dataset?
- What assay was used to measure variant effects?
- How do aPCA measurements relate to protein stability?
- What does the paper conclude about pathogenic missense variants and stability?
- How are functional sites identified from abundance and language-model predictions?
- How are homologous domain families modelled?
- What limitations constrain use of the dataset for clinical interpretation?
- Where are the data and code available?

### Coverage decision

Complete at `coverage_profile: standard`. The source page captures source status, assay design, dataset scale, validation, clinical variant interpretation, functional-site analysis, family modelling, links to SRC-0070, data/code availability, and limitations.

### Known gaps

- The wiki does not reproduce the full per-domain maps, supplementary tables, MoCHI model fits, or all predictor benchmark figures.
- GEO, Zenodo, and GitHub artifacts were recorded from the paper but not separately ingested.
- Supplementary material linked by the paper was not provided as a separate source file.
