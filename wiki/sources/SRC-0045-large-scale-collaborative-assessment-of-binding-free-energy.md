---
type: source
status: active
created: 2026-06-30
updated: 2026-07-01
source_id: SRC-0045
display_title: "Large-scale Collaborative Assessment of Binding Free Energy Calculations for Drug Discovery Using OpenFE"
short_title: "OpenFE RBFE Benchmark"
aliases:
  - "SRC-0045"
  - "OpenFE RBFE Benchmark"
  - "Large-scale Collaborative Assessment of Binding Free Energy Calculations for Drug Discovery Using OpenFE"
source_path: raw/sources/SRC-0045-large-scale-collaborative-assessment-of-binding-free-energy.pdf
original_filename: "chemrxiv-2025-7sthd_v2.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 13b864deeb88b30b8c9fd482b7640bb7b6fdf8fa6977a3d79af034a8feb48563
authors:
  - "Hannah M. Baumann"
  - "Joshua T. Horton"
  - "Michael M. Henry"
  - "Alyssa Travitz"
  - "Benjamin Ries"
  - "Richard J. Gowers"
  - "David W. H. Swenson"
  - "Iván Pulido"
  - "Dominic Rufa"
  - "David L. Dotson"
  - "Nupur Bansal"
  - "Joseph P. Bluck"
  - "Howard Broughton"
  - "Kira Campbell"
  - "Lili Cao"
  - "Sirish Kaushik Lakkaraju"
  - "Benedikt Frieg"
  - "Vytautas Gapsys"
  - "Hendrik Göddeke"
  - "Marco Klähn"
  - "Stephanie M. Linker"
  - "Thomas Löhr"
  - "Aniket Magarkar"
  - "Sergio Pérez-Conesa"
  - "Hans E. Purkey"
  - "Hayk Saribekyan"
  - "Jenke Scheen"
  - "Christina E. M. Schindler"
  - "Thomas Steinbrecher"
  - "Chaya D. Stern"
  - "Patricia Suriana"
  - "William C. Swope"
  - "Gary Tresadern"
  - "Lev Tsidilkovski"
  - "Binqing Wei"
  - "Alexander H. Williams"
  - "Yao Wu"
  - "Ivy Zhang"
  - "John D. Chodera"
  - "James R. B. Eastwood"
  - "David L. Mobley"
  - "Irfan Alibay"
author_entities:
  - "[[wiki/entities/authors/john-d-chodera]]"
year: 2026
venue: "ChemRxiv"
doi: "10.26434/chemrxiv-2025-7sthd/v2"
arxiv:
metadata_review_status: reviewed
areas:
  - research
categories:
  - research/molecular-simulation/free-energy
  - research/computational-drug-discovery
  - research/experimental-benchmarking
  - research/biomolecules/proteins
tags:
  - RBFE
  - OpenFE
  - benchmarking
  - drug-discovery
related:
  - "[[wiki/sources/SRC-0061-openfe-rbfe-benchmark-journal-version]]"
  - "[[wiki/sources/SRC-0062-openfe-rbfe-benchmark-supporting-information]]"
  - "[[wiki/concepts/relative-binding-free-energy-benchmarking]]"
  - "[[wiki/concepts/free-energy-estimation]]"
sources:
  - SRC-0045
cites_sources:
  - SRC-0023
  - SRC-0046
citation_match_status: partial
cqt_review_status: linked
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: math-standard
---

# Large-scale Collaborative Assessment of Binding Free Energy Calculations for Drug Discovery Using OpenFE

Source ID: `SRC-0045`

## Raw source

- Repository path: `raw/sources/SRC-0045-large-scale-collaborative-assessment-of-binding-free-energy.pdf`
- Open raw source: [raw/sources/SRC-0045-large-scale-collaborative-assessment-of-binding-free-energy.pdf](../../raw/sources/SRC-0045-large-scale-collaborative-assessment-of-binding-free-energy.pdf)

## Summary

This ChemRxiv preprint benchmarks the OpenFE relative binding free energy protocol across a large public/private drug-discovery corpus. The study evaluates public systems selected from the Ross et al. benchmark and blinded private industry datasets, reporting lower accuracy on private real-world datasets than on curated public datasets. [SRC-0045]

The later journal version and supporting information are ingested separately as [[wiki/sources/SRC-0061-openfe-rbfe-benchmark-journal-version]] and [[wiki/sources/SRC-0062-openfe-rbfe-benchmark-supporting-information]]. [SRC-0061] [SRC-0062]

## Key Points

- The public benchmark contains 58 protein-ligand systems and 876 ligands selected from the Schroedinger 2023 benchmark set; the private benchmark contains 37 anonymized industry datasets and 842 ligands. [SRC-0045, section 2.1]
- The OpenFE protocol uses a hybrid-topology RBFE approach implemented in `openfe-v1.0.1`, OpenMM dynamics, Amber14SB for protein, TIP3P water, OpenFF Sage-2.2.0 for ligands/cofactors, Hamiltonian replica exchange, and MBAR analysis via `pymbar`. [SRC-0045, sections 2.4-2.5]
- Public benchmark performance is reported as a weighted all-to-all pairwise RMSE of about 1.72 kcal/mol, with 10 systems reaching sub-kcal/mol accuracy. [SRC-0045, section 3.1.1]
- Private benchmark performance is worse, with a weighted RMSE of about 2.44 kcal/mol and only 2 systems reaching sub-kcal/mol accuracy. [SRC-0045, abstract]
- The paper emphasizes that OpenFE was used with default protocol settings, while the FEP+ comparison used previously published, manually tuned results. [SRC-0045, section 4.1]
- Performance was system-dependent; the study did not identify a single dominant error source. [SRC-0045, abstract]

## Key equations

**Weighted RMSE aggregation, source Eq. (3) [SRC-0045]:**

$$
\mathrm{RMSE} =
\sqrt{
\frac{1}{\sum_i^M w_i}
\sum_i^M w_i \mathrm{RMSE}_i^2
}.
$$

Here $w_i$ is the number of ligands in system $i$ for the all-to-all pairwise benchmark. [SRC-0045, section 3.1.1]

## Variable glossary

- $\Delta\Delta G$: relative binding free energy between two ligands. [SRC-0045]
- $\mathrm{RMSE}_i$: root mean squared error for benchmark system $i$. [SRC-0045, section 3.1.1]
- $w_i$: aggregation weight, set to the number of ligands in the system for pairwise RMSE. [SRC-0045, section 3.1.1]
- $M$: number of benchmark systems included in the aggregate. [SRC-0045, section 3.1.1]

## Equation inventory

| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |
| Weighted RMSE | Eq. (3), section 3.1.1 | Key equations | Aggregates per-system benchmark error | $\mathrm{RMSE}_i$, $w_i$, $M$ | Needed to compare benchmark summaries |

## Limitations

- The preprint had not been peer reviewed at posting. [SRC-0045]
- Membrane-bound systems were excluded because of OpenFE tooling limitations at the time of the study. [SRC-0045, section 2.1]
- Large topological changes such as ring breaking in macrocycles were excluded, although smaller scaffold-hop-like cases were included. [SRC-0045, section 2.1]
- The FEP+ comparison is not a clean controlled-method comparison because sampling lengths, manual setup, force fields, enhanced water sampling, and protocol tuning differ. [SRC-0045, section 4.1]
- Private datasets include assay-limit, stereochemical, tautomeric, pose, metal, water-sampling, and large-transformation complications that make benchmark interpretation harder. [SRC-0045, section 4.2]

## Claims

- [[wiki/claims/CLM-0017-experimental-reproducibility-bounds-rbfe-error-interpretation]]
- [[wiki/claims/CLM-0018-public-rbfe-benchmarks-can-be-easier-than-private-active-project-data]]
- [[wiki/claims/CLM-0019-edgewise-rbfe-metrics-can-overstate-arbitrary-comparison-quality]]

## Questions

- [[wiki/questions/rbfe-benchmark-prospective-use-scope]]

## Tensions

- [[wiki/tensions/TEN-0010-rbfe-benchmark-success-vs-prospective-use]]

## Links

- [[wiki/concepts/relative-binding-free-energy-benchmarking]]
- [[wiki/concepts/free-energy-estimation]]
- [[wiki/sources/SRC-0061-openfe-rbfe-benchmark-journal-version]]
- [[wiki/sources/SRC-0062-openfe-rbfe-benchmark-supporting-information]]

## Citation Links

- `SRC-0046`: The references list Ross, Lu, Scarabelli, Albanese, Houang, Abel, Harder, and Wang, "The maximal and current accuracy of rigorous protein-ligand binding free energy calculations," Communications Chemistry 2023, 6, 222. This is an exact title, first-author, and year match to the ingested FEP+ accuracy source. [SRC-0045, reference 42]
- `SRC-0023`: The references list Shirts and Chodera, "Statistically optimal analysis of samples from multiple equilibrium states," Journal of Chemical Physics 2008, 129, 124105. This is an exact title, first-author, and year match to the ingested original MBAR source. [SRC-0045, reference 89]
- Partial citation review: the targeted pass confirmed cluster-relevant links to FEP+ and MBAR, but did not exhaustively normalize every benchmark-method reference in this preprint because the journal version is the canonical OpenFE source in the wiki. [SRC-0045]

## Ingestion QA

### Retrieval questions checked

- What was the central OpenFE benchmark contribution?
- How many public and private systems/ligands were evaluated?
- What protocol and force-field choices define the OpenFE workflow?
- What weighted RMSE did OpenFE achieve on public and private data?
- Why is comparison with FEP+ not a controlled apples-to-apples comparison?
- Which systems or transformations were excluded?
- What limitations were identified for prospective industrial use?

### Coverage decision

Complete at `coverage_profile: math-standard`. The source page captures benchmark scope, protocol settings, central metrics, limitations, and the aggregation equation needed for later retrieval.

### Known gaps

- The wiki does not reproduce all public/private dataset tables, per-target metrics, or supplementary protocol-difference tables.
