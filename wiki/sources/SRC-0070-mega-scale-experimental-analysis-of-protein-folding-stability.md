---
type: source
status: active
created: 2026-07-02
updated: 2026-07-02
source_id: SRC-0070
display_title: "Mega-scale experimental analysis of protein folding stability in biology and design"
short_title: "Mega-scale Protein Folding Stability"
aliases:
  - "SRC-0070"
  - "Mega-scale Protein Folding Stability"
  - "cDNA display proteolysis"
source_path: raw/sources/SRC-0070-mega-scale-experimental-analysis-of-protein-folding-stability.pdf
imported_path: raw/sources/SRC-0070-mega-scale-experimental-analysis-of-protein-folding-stability.pdf
original_filename: "s41586-023-06328-6.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 08c9969af56253f56fb8d5148c2fb0c518d39bae918030863ba2ea093becf0c6
authors:
  - "Kotaro Tsuboyama"
  - "Justas Dauparas"
  - "Jonathan Chen"
  - "Elodie Laine"
  - "Yasser Mohseni Behbahani"
  - "Jonathan J. Weinstein"
  - "Niall M. Mangan"
  - "Sergey Ovchinnikov"
  - "Gabriel J. Rocklin"
author_entities: []
year: 2023
venue: "Nature"
doi: "10.1038/s41586-023-06328-6"
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
  - deep-mutational-scanning
  - cDNA-display
  - proteolysis
  - protein-design
related:
  - "[[wiki/concepts/cdna-display-proteolysis-stability-measurements]]"
  - "[[wiki/concepts/protein-energy-landscape-profiling]]"
  - "[[wiki/concepts/human-domainome-variant-stability-mapping]]"
  - "[[wiki/claims/CLM-0030-cdna-display-proteolysis-is-scalable-but-assumption-limited]]"
sources:
  - SRC-0070
cites_sources: []
citation_match_status: partial
cqt_review_status: linked
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: standard
peer_review_status: peer-reviewed
---

# Mega-scale Experimental Analysis of Protein Folding Stability in Biology and Design

Source ID: `SRC-0070`

## Raw source

- Repository path: `raw/sources/SRC-0070-mega-scale-experimental-analysis-of-protein-folding-stability.pdf`
- Open raw source: [raw/sources/SRC-0070-mega-scale-experimental-analysis-of-protein-folding-stability.pdf](../../raw/sources/SRC-0070-mega-scale-experimental-analysis-of-protein-folding-stability.pdf)

## Status note

This is a peer-reviewed Nature article published online on 2023-07-19 and in volume 620 on 2023-08-10. [SRC-0070]

## Summary

Tsuboyama et al. introduce cDNA display proteolysis, a sequencing-based assay for measuring thermodynamic folding stability across very large libraries of short protein domains. The paper reports about 1.8 million measurements and curates 776,298 high-quality absolute folding stabilities covering all single amino acid variants and selected double mutants of 331 natural domains and 148 de novo designed domains. The dataset is used to analyze amino acid fitness environments, thermodynamic coupling between sites, divergence between evolutionary amino acid usage and folding stability, and stability effects in protein design. [SRC-0070]

## Key Points

- cDNA display proteolysis links each protein variant to its cDNA, digests pooled protein-cDNA complexes with protease titrations, and uses sequencing counts after pulldown to infer protease resistance for each sequence. [SRC-0070]
- The authors used trypsin and chymotrypsin as orthogonal proteases to help separate sequence-specific protease susceptibility from folding-stability effects. [SRC-0070]
- A single one-week experiment can assay up to about 900,000 sequences, with reagent costs reported around US$2,000 excluding DNA synthesis and sequencing. [SRC-0070]
- The curated dataset includes all single substitutions, single deletions, and Gly/Ala insertions for hundreds of small natural and designed domains under common experimental conditions. [SRC-0070]
- Agreement with traditional purified-protein measurements across 1,188 variants of 10 proteins had Pearson correlations above 0.75, supporting the assay for cooperative small domains. [SRC-0070]
- Principal-component analysis of site-level stability landscapes found dominant axes corresponding to buried versus exposed sites, helix preference, aliphatic versus aromatic preference, charge preference, and dense/small-residue environments. [SRC-0070]
- Double-mutant scans over 559 amino acid pairs revealed thermodynamic couplings that were often 0.5-1.0 kcal mol^-1 and sometimes above 2 kcal mol^-1. [SRC-0070]
- The paper reports 2,600 mutations that increased folding stability by at least 1 kcal mol^-1, including examples of stabilizing insertions and deletions. [SRC-0070]
- In 727 PROSS redesigns across 172 domains, the average stability increase was 0.6 +/- 1.0 kcal mol^-1, and 40% of domains were stabilized by more than 1 kcal mol^-1. [SRC-0070]

## Assay Model

The source models survival under single-turnover proteolysis as an exponential decay:

$$
\mathrm{Survival} = \exp(-k_{\mathrm{obs}}t)
$$

with observed cleavage rate:

$$
k_{\mathrm{obs}} = \frac{k_{\max}[E]}{K_{50} + [E]}.
$$

For thermodynamic folding stability, the model separates idealized folded and unfolded states and uses:

$$
\Delta G = -RT \ln\left(\frac{[U]}{[F]}\right).
$$

Under the paper's rapid-equilibrium approximation, the inferred unfolded-to-folded ratio is estimated from the measured overall $K_{50}$, an unfolded-state susceptibility $K_{50,U}$, and a folded-state reference $K_{50,F}$:

$$
\frac{[U]}{[F]} \approx
\frac{1/K_{50} - 1/K_{50,F}}{1/K_{50,U} - 1/K_{50}}.
$$

These equations are central because the assay is not just measuring raw protease resistance; it is converting protease titration curves into inferred folding free energies. [SRC-0070]

## Limitations and Caveats

- The assay is best suited to proteins that express in the cell-free system, are monomeric, are not stabilized by complexes, and satisfy the size and chemistry constraints of cDNA display. [SRC-0070]
- Inferred folding stabilities are accurate only when folding is cooperative, folding is equilibrated during digestion, unfolded-state protease susceptibility is accurately inferred, cleavage releases the cDNA-linked tag, and cleavage rates fall in the measurable dynamic range. [SRC-0070]
- The paper reports a current dynamic range of roughly 5 kcal mol^-1, so very stable variants can be difficult to resolve. [SRC-0070]
- Cleavage from folded or partially folded states can make stability estimates too low, and such artifacts can be hard to detect if both proteases are affected similarly. [SRC-0070]
- The designed-domain structures used in the study include models from Rosetta, trRosetta hallucination, and AlphaFold; some are not experimentally validated structures. [SRC-0070]
- Multiplexed measurements and automated analysis can introduce inaccuracies, so notable individual results may require raw-data inspection. [SRC-0070]

## Claims

- [[wiki/claims/CLM-0030-cdna-display-proteolysis-is-scalable-but-assumption-limited]]
- Large-scale stability datasets can expose rare stabilizing mutations and non-additive interactions that are hard to discover from smaller protein-stability databases. [SRC-0070]
- Protein-stability measurements provide a benchmark observable distinct from native structure prediction: deep-learning structure accuracy does not directly solve quantitative folding-stability prediction. [SRC-0070]

## Links

- [[wiki/concepts/cdna-display-proteolysis-stability-measurements]]
- [[wiki/concepts/protein-energy-landscape-profiling]]
- [[wiki/sources/SRC-0067-protein-energy-landscape-discovery-analysis-design]]
- [[wiki/sources/SRC-0071-site-saturation-mutagenesis-of-500-human-protein-domains]]

## Citation Links

- Partial citation review: SRC-0070 cites no later ingested sources. SRC-0067 and SRC-0071 use cDNA-display proteolysis as comparison or validation data and are linked from their source pages. [SRC-0070]

## Metadata notes

- DOI shown by the source and PDF metadata: `10.1038/s41586-023-06328-6`.
- Data availability states that data are available in the article, extended data, supplementary material, or Zenodo record `10.5281/zenodo.7992926`. [SRC-0070]
- Code availability lists the analysis pipeline at `github.com/Rocklin-Lab/cdna-display-proteolysis-pipeline`. [SRC-0070]

## Ingestion QA

### Retrieval questions checked

- What method does the paper introduce?
- How many stability measurements and high-quality curated stabilities does it report?
- What protein domains and mutation types are covered?
- How does the assay infer folding stability from protease titration and sequencing?
- What validation supports the high-throughput measurements?
- What did the single-mutant and double-mutant scans reveal?
- How was the dataset used to evaluate protein design methods?
- What limitations constrain interpretation of individual measurements?
- Where are the data and code available?

### Coverage decision

Complete at `coverage_profile: standard`. The source page captures the assay, dataset scale, central kinetic/stability equations, validation evidence, major biological/design findings, reusable claim, links to adjacent protein landscape content, data/code availability, and caveats.

### Known gaps

- The wiki does not reproduce the supplementary derivation, Bayesian inference implementation, filtering scripts, every library design detail, or per-domain mutational scan results.
- The Zenodo dataset and GitHub code were recorded from the source but not separately ingested.
- The paper's supplementary information was not provided as a separate file, so supplementary-only details are represented only where they appear in the main PDF text.
