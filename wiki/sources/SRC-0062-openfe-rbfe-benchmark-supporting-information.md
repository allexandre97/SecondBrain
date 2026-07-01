---
type: source
status: active
created: 2026-06-30
updated: 2026-07-01
source_id: SRC-0062
display_title: "Supporting Information: Large-Scale Collaborative Assessment of Binding Free Energy Calculations for Drug Discovery Using OpenFE"
short_title: "OpenFE RBFE Benchmark Supporting Information"
aliases:
  - "SRC-0062"
  - "OpenFE RBFE Benchmark Supporting Information"
  - "OpenFE SI"
source_path: raw/sources/SRC-0062-openfe-rbfe-benchmark-supporting-information.pdf
imported_path: raw/sources/SRC-0062-openfe-rbfe-benchmark-supporting-information.pdf
original_filename: "ci6c00089_si_001.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 1187e247dea52b5eb12c7ce890ec695bc062cacaf46fb28a6039601efe85e1a0
authors:
  - "Hannah M. Baumann"
  - "Joshua T. Horton"
  - "Michael M. Henry"
  - "Alyssa Travitz"
  - "Benjamin Ries"
  - "Richard J. Gowers"
  - "David W. H. Swenson"
  - "Ivan Pulido"
  - "Dominic Rufa"
  - "David L. Dotson"
  - "Nupur Bansal"
  - "Joseph P. Bluck"
  - "Howard Broughton"
  - "Kira A. Campbell"
  - "Lili Cao"
  - "Benedikt Frieg"
  - "Vytautas Gapsys"
  - "Hendrik Goddeke"
  - "Marco Klahn"
  - "Sirish Kaushik Lakkaraju"
  - "Stephanie M. Linker"
  - "Thomas Lohr"
  - "Aniket Magarkar"
  - "Sergio Perez-Conesa"
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
venue: "Journal of Chemical Information and Modeling"
doi: "10.1021/acs.jcim.6c00089"
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
  - rbfe
  - openfe
  - benchmarking
  - supporting-information
related:
  - "[[wiki/sources/SRC-0061-openfe-rbfe-benchmark-journal-version]]"
  - "[[wiki/concepts/relative-binding-free-energy-benchmarking]]"
  - "[[wiki/concepts/free-energy-estimation]]"
sources:
  - SRC-0061
  - SRC-0062
cites_sources:
  - SRC-0046
citation_match_status: reviewed
cqt_review_status: source-local
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: standard
source_bundle: openfe-rbfe-benchmark-2026
bundle_role: supplement
---

# Supporting Information: Large-Scale Collaborative Assessment of Binding Free Energy Calculations for Drug Discovery Using OpenFE

Source ID: `SRC-0062`

## Raw source

- Repository path: `raw/sources/SRC-0062-openfe-rbfe-benchmark-supporting-information.pdf`
- Open raw source: [raw/sources/SRC-0062-openfe-rbfe-benchmark-supporting-information.pdf](../../raw/sources/SRC-0062-openfe-rbfe-benchmark-supporting-information.pdf)

## Summary

This supporting information is the supplement to [[wiki/sources/SRC-0061-openfe-rbfe-benchmark-journal-version]]. It provides public-system lists, the OpenFE lambda schedule, private problematic-ligand notes, OpenFE/FEP+ protocol-difference tables, public and private diagnostic figures, outlier analyses, convergence and redundant-edge removal checks, and edge-difficulty metric analyses. [SRC-0061] [SRC-0062]

## Key Points

- Table S1 lists the public systems included in the benchmark and their grouping labels. [SRC-0062, table S1]
- Figure S1 shows the relative hybrid-topology lambda schedule used by the OpenFE protocol. [SRC-0062, figure S1]
- Table S2 records private-set problematic ligands and associated issues such as alternate conformers, weaker tautomers, and stereochemical/tautomeric ambiguities. [SRC-0062, table S2]
- Table S3 summarizes key OpenFE versus Ross et al. FEP+ protocol differences: default automation versus manual tuning, 5 ns/20 ns OpenFE windows versus 20 ns FEP+ windows, triplicates versus a single FEP+ simulation, Hamiltonian replica exchange versus REST2/GCMC, and OpenFF/TIP3P/FF14SB versus OPLS4/SPC/custom torsions. [SRC-0062, table S3]
- Figures S2-S6 compare OpenFE, FEP+, and Prime MM-GBSA public-dataset accuracy and ranking metrics. [SRC-0062]
- Figures S10-S14 document public outlier causes, including poor ligand alignment, moving formal charges, partial fused rings, and a Kartograf atom-mapper bug that introduced bond breaks before being fixed. [SRC-0062, section S3]
- Figures S15-S20 provide private-dataset diagnostics, including raw uncurated private performance, per-system ranking metrics, edgewise error distributions, and public/private edge-metric comparisons. [SRC-0062, section S4]
- Figures S21-S31 support protocol analysis: repeat behavior, MBAR uncertainty comparisons, 80% versus 100% sampling-time checks, convergence diagnostics, redundant-edge removal, and edge-score/convergence relationships. [SRC-0062, sections S5-S7]

## Evidence

- The supplement states that public input structures, scripts, and selected results are provided in the `IndustryBenchmarks2024` repository. [SRC-0062]
- The Kartograf bug investigation found bond-breaking mappings in PFKFB3 outlier edges; rerunning after the mapping fix gave results close to experiment for the cited edges. [SRC-0062, section S3]
- Redundant unconverged-edge removal did not consistently improve RMSE or Kendall tau across public and private datasets. [SRC-0062, section S6.1]
- Edge-difficulty metrics such as LOMAP score, volume score, and heavy-atom changes are correlated with convergence, but they do not perfectly separate easy and hard transformations. [SRC-0062, section S7]

## Links

- Main article: [[wiki/sources/SRC-0061-openfe-rbfe-benchmark-journal-version]]
- [[wiki/concepts/relative-binding-free-energy-benchmarking]]
- [[wiki/concepts/free-energy-estimation]]
- [[wiki/questions/rbfe-benchmark-prospective-use-scope]]

## Open Questions

- Which convergence or edge-difficulty metrics can be turned into reliable prospective network-planning rules? [SRC-0062, sections S6-S7]
- When should a user remove, rerun, remap, or keep an unconverged edge in an RBFE network? [SRC-0062, section S6.1]
- Which diagnostic figures should become automated OpenFE quality-control reports? [SRC-0062]

## Citation Links

- `SRC-0046`: The supporting information reference list contains one entry: Ross, Lu, Scarabelli, Albanese, Houang, Abel, Harder, and Wang, "The maximal and current accuracy of rigorous protein-ligand binding free energy calculations," Communications Chemistry 2023, 6, 222. This is an exact title, first-author, and year match to the ingested FEP+ accuracy source. [SRC-0062, reference 1]

## Metadata notes

This file was provided by the user as supporting material for SRC-0061. It is treated as the supplement in the `openfe-rbfe-benchmark-2026` source bundle.

## Ingestion QA

### Retrieval questions checked

- What does the supporting information add to the main article?
- Which public systems are listed?
- What are the key OpenFE versus FEP+ protocol differences?
- Which outlier causes are documented?
- What does the supplement say about private-data curation?
- What diagnostics support repeat, sampling-length, and convergence conclusions?
- Did removing unconverged redundant edges reliably improve results?

### Coverage decision

Complete at `coverage_profile: standard` as a supporting-information source. The wiki captures the supplement's table/figure structure, protocol-difference information, outlier details, convergence diagnostics, and links to the main source. [SRC-0062]

### Known gaps

- Individual figures, public system tables, and private problematic-ligand rows are summarized rather than reproduced.
- Private structures and identifiers remain unavailable by design.
