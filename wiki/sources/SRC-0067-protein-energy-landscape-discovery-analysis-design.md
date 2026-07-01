---
type: source
status: active
created: 2026-07-01
updated: 2026-07-01
source_id: SRC-0067
display_title: "Large-scale discovery, analysis and design of protein energy landscapes"
short_title: "Protein Energy Landscapes"
aliases:
  - "SRC-0067"
  - "Protein Energy Landscapes"
  - "Large-scale discovery, analysis and design of protein energy landscapes"
source_path: raw/sources/SRC-0067-protein-energy-landscape-discovery-analysis-design.pdf
imported_path: raw/sources/SRC-0067-protein-energy-landscape-discovery-analysis-design.pdf
original_filename: "s41586-026-10465-z.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 1d9d568495e4a2e89eeb42df9b3b5f07a05b04ba0abf4c111a80baab7eb2c39f
areas:
  - research
categories:
  - research/biomolecules/proteins
  - research/experimental-benchmarking
  - research/data-management
  - research/machine-learning/scientific-modeling
tags:
  - proteins
  - energy-landscapes
  - hydrogen-deuterium-exchange
  - mass-spectrometry
  - protein-stability
  - machine-learning
related:
  - "[[wiki/concepts/protein-energy-landscape-profiling]]"
  - "[[wiki/concepts/protein-force-field-benchmark-datasets]]"
sources:
  - SRC-0067
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: standard
peer_review_status: peer-reviewed
---

# Large-scale discovery, analysis and design of protein energy landscapes

Source ID: `SRC-0067`

## Raw source

- Repository path: `raw/sources/SRC-0067-protein-energy-landscape-discovery-analysis-design.pdf`
- Open raw source: [raw/sources/SRC-0067-protein-energy-landscape-discovery-analysis-design.pdf](../../raw/sources/SRC-0067-protein-energy-landscape-discovery-analysis-design.pdf)

## Status note

This is a peer-reviewed Nature article published online on 2026-05-13 and in volume 654 on 2026-06-25. [SRC-0067]

## Summary

Ferrari et al. introduce multiplex intact-protein hydrogen-deuterium exchange mass spectrometry (mHDX-MS) for measuring conformational fluctuation energy profiles across thousands of small protein domains. The study analyzes 5,778 domains between 28 and 64 amino acids, identifies 3,590 measurably stable domains, validates the high-throughput measurements against HDX NMR and cDNA-display proteolysis, and uses the resulting dataset to study sequence and structural determinants of local opening energies and opening cooperativity. [SRC-0067]

## Key Points

- mHDX-MS expresses and purifies large mixtures of designed and natural domains, measures deuterium uptake across pH 6 and pH 9 time courses, and infers residue-level exchange-rate distributions and opening free energies with automated Bayesian analysis. [SRC-0067]
- The approach estimates global unfolding stability from the most stable residues, while the full opening-energy distribution reports lower-energy partially open states that can be missed by global stability assays. [SRC-0067]
- Validation against 13 domains measured by HDX NMR gave close agreement, with reported errors of 1.9-fold for exchange-rate distributions and 0.53 kcal mol^-1 for opening free energies. [SRC-0067]
- cDNA-display proteolysis global-stability measurements correlated with mHDX-MS global stability across thousands of domains, with reported correlation around `r = 0.78`. [SRC-0067]
- The dataset revealed hidden variation in conformational fluctuations between structurally related domains and even between domains with similar global folding stability. [SRC-0067]
- The authors define opening cooperativity as a normalized measure of whether many residues have high opening energies relative to proteins with similar global stability, hydrogen bonding, and net charge. [SRC-0067]
- Site-resolved HDX NMR on exemplar low-cooperativity proteins showed that low-stability regions can correspond to entire secondary-structure elements, not just terminal fraying or isolated residues. [SRC-0067]
- Feature analysis found correlations between cooperativity and structural or sequence features such as compactness, proline count, AlphaFold2 confidence, Rosetta energy terms, buried non-polar surface area, and disorder predictions, but no single feature dominated. [SRC-0067]
- Family-specific regression models predicted global stability better than opening cooperativity; the best unseen-data `R^2` values were about 0.40-0.53 for global stability and 0.16-0.24 for family-normalized cooperativity. [SRC-0067]
- Machine-learning-guided double-mutant libraries identified rare mutations predicted to improve opening cooperativity while preserving or improving stability, and experiments found multiple designed variants that improved both properties. [SRC-0067]

## Limitations and Caveats

- The mHDX-MS inference depends on approximations about back exchange, chemical exchange rates, EX2-like kinetics, and combining measurements collected at different pH values. [SRC-0067]
- Intact-protein multiplexed measurements infer distributions of opening energies but do not directly localize high- and low-stability segments without follow-up experiments such as HDX NMR. [SRC-0067]
- Automated processing, expression success, MS identification, and HDX data-quality filters reduce coverage from the initial designed library; the paper reports 3,590 measurably stable domains from the broader input set. [SRC-0067]
- The study focuses on short domains of 28-64 amino acids from selected designed and natural families, so transfer to larger proteins and other experimental conditions remains a future extension. [SRC-0067]
- The machine-learning models are useful for exploration but not quantitatively accurate enough to fully predict conformational fluctuation energy landscapes. [SRC-0067]

## Links

- [[wiki/concepts/protein-energy-landscape-profiling]]
- [[wiki/concepts/protein-force-field-benchmark-datasets]]

## Metadata notes

- DOI shown by the source: `10.1038/s41586-026-10465-z`.
- The source states that supporting data are available online and that MS proteomics data are deposited through ProteomeXchange/PRIDE under dataset identifier `PXD061702`. [SRC-0067]
- The source lists code repositories for `hdxrate_pipeline` and `mhdx_analysis`. [SRC-0067]

## Ingestion QA

### Retrieval questions checked

- What experimental method does the paper introduce?
- How many domains were analyzed and how many were measurably stable?
- What does mHDX-MS infer from deuterium exchange data?
- How were the measurements validated?
- What is opening cooperativity?
- What did HDX NMR reveal about low-cooperativity domains?
- How accurately did machine-learning models predict stability and cooperativity?
- Did designed mutations experimentally improve cooperativity?
- What limitations does the paper acknowledge?

### Coverage decision

Complete at `coverage_profile: standard`. The source page captures source status, experimental design, dataset scale, validation, main biological and modelling results, design experiment, data availability, and caveats.

### Known gaps

- The wiki does not reproduce the full Bayesian inference model, all supplementary filters, or every feature-engineering and regression detail.
- Detailed per-domain results remain in the raw paper and associated datasets rather than duplicated in the wiki.
