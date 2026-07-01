---
type: source
status: active
created: 2026-06-30
updated: 2026-06-30
source_id: SRC-0058
display_title: "Supplementary Information for Overlay Databank Unlocks Data-driven Analyses of Biomolecules for All"
short_title: "Overlay Databank Supplement"
authors:
  - "Kiirikki, Anne M. et al."
year: 2024
venue: "Nature Communications Supplementary Information"
parent_doi: "10.1038/s41467-024-45189-z"
aliases:
  - "SRC-0058"
  - "Overlay Databank Supplement"
  - "Supplementary Information for Overlay Databank Unlocks Data-driven Analyses of Biomolecules for All"
source_path: raw/sources/SRC-0058-supplementary-information-for-overlay-databank-unlocks-data-driven.pdf
original_filename: "41467_2024_45189_MOESM1_ESM.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 5e4db5ea9ff14cb6ba9a659f75919e3a6ba4ce9fe395a4324d772f43304aa34b
source_bundle: overlay-databank-nmrlipids
bundle_role: supplement
areas:
  - research
categories:
  - research/molecular-simulation/datasets
  - research/data-management
  - research/biomolecules/lipids
tags:
  - overlay-databank
  - NMRlipids
  - FAIR-data
  - membrane-simulations
  - supporting-information
related:
  - "[[wiki/sources/SRC-0057-overlay-databank-unlocks-data-driven-analyses-of-biomolecules]]"
  - "[[wiki/concepts/overlay-databanks-for-biomolecular-simulation-data]]"
cites_sources:
  - SRC-0057
sources:
  - SRC-0057
  - SRC-0058
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: standard
metadata_review_status: partial
citation_match_status: reviewed
cqt_review_status: source-local
---

# Supplementary Information for Overlay Databank Unlocks Data-driven Analyses of Biomolecules for All

Source ID: `SRC-0058`

## Raw source

- Repository path: `raw/sources/SRC-0058-supplementary-information-for-overlay-databank-unlocks-data-driven.pdf`
- Open raw source: [raw/sources/SRC-0058-supplementary-information-for-overlay-databank-unlocks-data-driven.pdf](../../raw/sources/SRC-0058-supplementary-information-for-overlay-databank-unlocks-data-driven.pdf)

## Summary

This supporting information documents the NMRlipids Databank structure, metadata keys, current force-field list, example application-layer scripts, workflow diagrams, and supporting analysis figures for SRC-0057. It functions as the implementation and provenance companion to the main article. [SRC-0058]

## Key Points

- Supplementary Fig. 1 shows the NMRlipids Databank structure, including raw simulation data, user-supplied information, experimental data, generated `README.yaml` entries, and stored analysis outputs. [SRC-0058]
- Supplementary Table 1 lists force fields represented in databank simulations, including CHARMM36, Slipids, Amber Lipid14/17, Charmm-Drude, GROMOS variants, AMOEBA, and OpenFF among others. [SRC-0058]
- Supplementary Table 2 lists example Application-layer codes for area/thickness correlations, flip-flop rates, water permeation, water lateral diffusion, and area-per-lipid prediction. [SRC-0058]
- Supplementary Table 3 defines simulation `README.yaml` keys, including DOI, software, trajectory/topology files, composition mapping, force field, warnings, trajectory size, length, temperature, atom count, and unique ID. [SRC-0058]
- Supplementary Table 4 defines keys for experimental data, and Supplementary Table 5 lists codes used to build and analyze the databank layer. [SRC-0058]
- Supplementary figures support the main-text analyses of order parameter quality, form factor quality, area per lipid, ML prediction, water permeation, water diffusion, and experimental order-parameter extraction. [SRC-0058]

## Bundle Links

- Main text: SRC-0057. [SRC-0057]
- Supporting material: SRC-0058. [SRC-0058]

## Limitations

- The supplement documents the state of the databank and associated code at publication time; live repositories may evolve. [SRC-0058]
- It provides implementation details and supporting analyses but does not replace the raw repository documentation for current usage. [SRC-0058]

## Links

- [[wiki/sources/SRC-0057-overlay-databank-unlocks-data-driven-analyses-of-biomolecules]]
- [[wiki/concepts/overlay-databanks-for-biomolecular-simulation-data]]

## Claims

- Source-local support for [[wiki/claims/CLM-0029-overlay-databanks-solve-access-and-standardization-not-simulation-quality]] through metadata-key tables, workflow diagrams, and application-layer code lists. [SRC-0058]

## Citation Links

- Citation review status: reviewed as source-local supporting information tied to [[wiki/sources/SRC-0057-overlay-databank-unlocks-data-driven-analyses-of-biomolecules]].

## Ingestion QA

### Retrieval questions checked

- What is in the supporting information?
- Which force fields are listed?
- What metadata keys are stored for simulations?
- What application-layer scripts are documented?
- Which analyses do the supporting figures back up?
- How does this source relate to the main paper?

### Coverage decision

Complete at `coverage_profile: standard`. The page captures the supplement's implementation role, key tables, workflow figures, and relationship to SRC-0057.

### Known gaps

- The wiki does not reproduce every metadata key description, supplementary figure, or reference.
