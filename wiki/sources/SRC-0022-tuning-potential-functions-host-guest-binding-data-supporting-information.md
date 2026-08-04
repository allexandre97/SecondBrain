---
type: source
status: active
created: 2026-06-30
updated: 2026-08-04
source_id: SRC-0022
display_title: "Supporting Information for Tuning Potential Functions to Host-Guest Binding Data"
short_title: "Host-Guest Potential Tuning Supplement"
aliases:
  - "SRC-0022"
  - "Host-Guest Potential Tuning Supplement"
  - "Supporting Information for Tuning Potential Functions to Host-Guest Binding Data"
source_path: raw/sources/SRC-0022-tuning-potential-functions-host-guest-binding-data-supporting.pdf
imported_path: raw/sources/SRC-0022-tuning-potential-functions-host-guest-binding-data-supporting.pdf
original_filename: "ct3c01050_si_001.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 67d0ff5c51327dd598abdf838c6d8a12e65edeb3529f2dd970dcebc177a9c822
authors:
  - "Jeffry Setiadi"
  - "Simon Boothroyd"
  - "David R. Slochower"
  - "David L. Dotson"
  - "Matthew W. Thompson"
  - "Jeffrey R. Wagner"
  - "Lee-Ping Wang"
  - "Michael K. Gilson"
author_entities: []
year: 2024
venue: "Journal of Chemical Theory and Computation"
doi: "10.1021/acs.jctc.3c01050"
arxiv:
metadata_review_status: reviewed
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/computational-drug-discovery
  - research/molecular-simulation/free-energy
  - research/biomolecules/proteins
  - research/experimental-benchmarking
tags:
  - supporting-information
  - host-guest
  - binding-free-energy
  - implicit-solvent
related:
  - "[[wiki/sources/SRC-0021-tuning-potential-functions-host-guest-binding-data]]"
  - "[[wiki/concepts/force-field-training-from-experimental-observables]]"
sources:
  - SRC-0022
cites_sources: []
citation_match_status: reviewed
cqt_review_status: source-local
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: standard
source_bundle: tuning-potential-functions-host-guest-binding-2024
bundle_role: supplement
---

# Supporting Information for Tuning Potential Functions to Host-Guest Binding Data

Source ID: `SRC-0022`

## Raw source

- Repository path: `raw/sources/SRC-0022-tuning-potential-functions-host-guest-binding-data-supporting.pdf`
- Open raw source: [raw/sources/SRC-0022-tuning-potential-functions-host-guest-binding-data-supporting.pdf](../../raw/sources/SRC-0022-tuning-potential-functions-host-guest-binding-data-supporting.pdf)
## Source bundle

Supporting information in the `tuning-potential-functions-host-guest-binding-2024` bundle; [[wiki/sources/SRC-0021-tuning-potential-functions-host-guest-binding-data|SRC-0021]] is the main paper. The requested SI file is byte-identical to this repository source (SHA256 `67d0ff5c51327dd598abdf838c6d8a12e65edeb3529f2dd970dcebc177a9c822`). [SRC-0021] [SRC-0022]

## Summary

This supporting information contains host-guest ABFE setup details, train/test complexes, binding free-energy tables, protein-ligand transfer benchmarks, hydration free-energy benchmarks, and prior-width sensitivity analysis for the OBC2 cavity-radius optimization in SRC-0021. [SRC-0022]

## Key Points

- The SI specifies host conformational restraints for cyclodextrins, cucurbiturils, and octa-acids. [SRC-0022]
- It provides the 36-system training set and 90-system test set binding free energies. [SRC-0022]
- It reports error statistics for host-guest training and test sets. [SRC-0022]
- It includes protein-ligand benchmark tables for different protein/ligand force-field combinations. [SRC-0022]
- It includes hydration free-energy benchmark error statistics showing the binding/HFE tradeoff discussed in the main text. [SRC-0022]
- The prior-width section explains how the Bayesian/prior penalty controls maximum parameter displacement in ForceBalance. [SRC-0022]
- A gradient check compares the implemented binding-free-energy parameter derivatives with finite differences for one alpha-cyclodextrin complex. [SRC-0022, section S1]
- Tables S4 and S5 give bootstrap confidence intervals and per-host statistics, preventing the aggregate improvement from hiding distinct behavior across cyclodextrin, cucurbituril, and octa-acid systems. [SRC-0022]

## Evidence

Figure S5 documents ForceBalance objective reduction over optimization and the evolution of selected GB cavity radii. [SRC-0022]

- Training RMSE changes from 21.0 to 2.94 kcal/mol and test RMSE from 19.49 to 2.07 kcal/mol under the HG-optimized radii; the test-set $R^2$ changes from 0.52 to 0.78. [SRC-0022, Tables S4-S5]
- Hydration RMSE changes from 2.11 to 19.12 kcal/mol, with mean signed error changing from 0.23 to -8.40 kcal/mol and $R^2$ from 0.79 to 0.35. [SRC-0022, Table S13]
- At optimization step 16, the objective is 13.86, the binding RMSE is 2.94 kcal/mol, and the penalty contributes 5.20. The SI estimates that halving the effective parameter displacement would raise RMSE to no more than about 5.10 kcal/mol, whereas a wider prior would drive H and N radii further from physical expectations. [SRC-0022, section S4]

## Links

- [[wiki/sources/SRC-0021-tuning-potential-functions-host-guest-binding-data]]
- [[wiki/concepts/force-field-training-from-experimental-observables]]
- [[wiki/questions/force-field-training-validation-scope]]

## Citation links

- Source-local review only; no separate first-class citation links were added beyond the main-paper bundle relationship. [SRC-0022]

## Open Questions

- Which host classes dominate the optimized-radius direction and the hydration-free-energy failure mode? [SRC-0022]

## Ingestion QA

### Retrieval questions checked

- What ABFE setup details are provided?
- Where are train/test binding free energies tabulated?
- What protein-ligand and hydration benchmarks are included?
- How is prior-width sensitivity discussed?
- Which host classes drive the baseline error and fitted parameter direction?
- What do the protein-stability, timing, and gradient checks add to the main paper?

### Coverage decision

Complete at `coverage_profile: standard` as the supplement to SRC-0021. The page records the supplement's main reproducibility role, quantitative validation tables, gradient check, regularization sensitivity, and bundle linkage. [SRC-0021] [SRC-0022]

### Known gaps

- Large numeric tables are summarized rather than transcribed.
- Referenced repositories, structures, and trajectories are external to the requested two-file bundle and were not ingested.
