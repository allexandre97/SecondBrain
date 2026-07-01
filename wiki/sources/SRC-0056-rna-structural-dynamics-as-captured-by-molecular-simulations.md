---
type: source
status: active
created: 2026-06-30
updated: 2026-06-30
source_id: SRC-0056
display_title: "RNA Structural Dynamics As Captured by Molecular Simulations: A Comprehensive Overview"
short_title: "RNA Molecular Simulations Review"
authors:
  - Jiri Sponer
  - Giovanni Bussi
  - Miroslav Krepl
  - Pavel Banas
  - Sandro Bottaro
  - Richard A. Cunha
  - Alejandro Gil-Ley
  - Giovanni Pinamonti
  - Simon Poblete
  - Petr Jurecka
  - Nils G. Walter
  - Michal Otyepka
year: 2018
venue: "Chemical Reviews"
doi: "10.1021/acs.chemrev.7b00427"
aliases:
  - "SRC-0056"
  - "RNA Molecular Simulations Review"
  - "RNA Structural Dynamics As Captured by Molecular Simulations: A Comprehensive Overview"
source_path: raw/sources/SRC-0056-rna-structural-dynamics-as-captured-by-molecular-simulations.pdf
original_filename: "rna-structural-dynamics-as-captured-by-molecular-simulations-a-comprehensive-overview-1-128.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: c9ad68c1495c58dd02bd1354076653867d6c2dc63af268dc5c3303dfc8033d3e
areas:
  - research
categories:
  - research/molecular-simulation/molecular-dynamics
  - research/biomolecules/rna
  - research/molecular-simulation/force-fields
tags:
  - RNA
  - molecular-dynamics
  - enhanced-sampling
  - force-fields
  - review
related:
  - "[[wiki/concepts/rna-molecular-dynamics-simulations]]"
  - "[[wiki/concepts/rna-force-field-limitations]]"
  - "[[wiki/concepts/adaptive-enhanced-sampling]]"
sources:
  - SRC-0056
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: standard
metadata_review_status: reviewed
citation_match_status: reviewed
cqt_review_status: linked
---

# RNA Structural Dynamics As Captured by Molecular Simulations: A Comprehensive Overview

Source ID: `SRC-0056`

## Raw source

- Repository path: `raw/sources/SRC-0056-rna-structural-dynamics-as-captured-by-molecular-simulations.pdf`
- Open raw source: [raw/sources/SRC-0056-rna-structural-dynamics-as-captured-by-molecular-simulations.pdf](../../raw/sources/SRC-0056-rna-structural-dynamics-as-captured-by-molecular-simulations.pdf)

## Summary

This Chemical Reviews article surveys RNA structural dynamics as studied by molecular simulations, with emphasis on atomistic MD, RNA force fields, enhanced sampling, coarse-grained models, ion interactions, RNA motifs, riboswitches, ribozymes, ribosomes, and protein/RNA complexes. [SRC-0056]

## Key Points

- RNA function is tightly connected to structure and dynamics, making MD a useful complement to structural biology and single-molecule experiments. [SRC-0056]
- The review identifies atomistic force-field accuracy and access to long time scales as central bottlenecks for RNA simulation. [SRC-0056]
- RNA force-field sections cover AMBER and CHARMM nucleic-acid force fields, validation by reweighting, and limitations of pairwise-additive molecular mechanics. [SRC-0056]
- Enhanced sampling methods are presented as essential for accessing RNA thermodynamics and kinetics beyond ordinary MD time scales. [SRC-0056]
- Coarse-grained models are reviewed as complementary tools with different goals, including physical thermodynamics, structure prediction, refinement, and elastic network descriptions. [SRC-0056]
- The source explicitly cautions that contemporary atomistic simulations are not sufficient for blind RNA structure prediction. [SRC-0056, summary and outlook]
- The review argues that close collaboration between simulation and experiment is necessary because MD can provide atomistic interpretation but can also mislead if its limits are ignored. [SRC-0056, summary and outlook]

## Scope

- Methodological sections: force fields, enhanced sampling, convergence, coarse graining, and ion interactions. [SRC-0056]
- RNA systems: tetranucleotides, tetraloops, internal loops, A-form helices, kissing loops, TAR, riboswitches, ribozymes, ribosome regions, protein/RNA complexes, and other RNA systems. [SRC-0056]
- Future directions: force-field improvement, multiscale simulation, enhanced sampling, coarse-grained models, QM methods, and stronger simulation-experiment coupling. [SRC-0056]

## Limitations

- The review is broad and not a protocol for any single RNA system. [SRC-0056]
- It predates later force-field and ML developments, so its state-of-the-art assessment should be paired with newer sources for current recommendations. [SRC-0056]
- The source emphasizes that failures and limitations should be reported, because overconfident use of MD can backfire. [SRC-0056]

## Links

- [[wiki/concepts/rna-molecular-dynamics-simulations]]
- [[wiki/concepts/rna-force-field-limitations]]
- [[wiki/concepts/adaptive-enhanced-sampling]]

## Claims

- [[wiki/claims/CLM-0028-rna-force-field-validation-needs-motif-level-and-coupled-error-checks]]

## Questions

- [[wiki/questions/rna-force-field-motif-validation-scope]]

## Tensions

- [[wiki/tensions/TEN-0014-rna-motif-specific-fixes-vs-general-force-field-transfer]]

## Citation Links

- Citation review status: reviewed for strong local RNA-cluster links. No newer source-to-source citation from this 2018 review to SRC-0055 was possible by publication date.

## Ingestion QA

### Retrieval questions checked

- What methodological bottlenecks dominate RNA MD?
- What classes of RNA force fields and models are reviewed?
- Why are enhanced sampling and coarse graining important?
- What RNA systems are surveyed?
- What does the review say about blind RNA structure prediction?
- What future directions does it emphasize?

### Coverage decision

Complete at `coverage_profile: standard`. The page records the review's scope, major claims, limitations, and future-facing guidance.

### Known gaps

- The wiki does not reproduce the 128-page source's exhaustive system-by-system survey or bibliography.
