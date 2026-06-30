---
type: source
status: active
created: 2026-06-30
updated: 2026-06-30
source_id: SRC-0057
display_title: "Overlay Databank Unlocks Data-driven Analyses of Biomolecules for All"
short_title: "Overlay Databank"
aliases:
  - "SRC-0057"
  - "Overlay Databank"
  - "Overlay Databank Unlocks Data-driven Analyses of Biomolecules for All"
source_path: raw/sources/SRC-0057-overlay-databank-unlocks-data-driven-analyses-of-biomolecules.pdf
original_filename: "s41467-024-45189-z.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 1ba5d0e9bbfb4ac8af58cf63952fcfff12320a1a929160ee688989d66496c5e6
source_bundle: overlay-databank-nmrlipids
bundle_role: main
areas:
  - research
categories:
  - research/molecular-simulation/datasets
  - research/data-management
tags:
  - overlay-databank
  - NMRlipids
  - FAIR-data
  - membrane-simulations
  - machine-learning
related:
  - "[[sources/SRC-0058-supplementary-information-for-overlay-databank-unlocks-data-driven]]"
  - "[[concepts/overlay-databanks-for-biomolecular-simulation-data]]"
  - "[[concepts/machine-learning-potential-datasets]]"
sources:
  - SRC-0057
  - SRC-0058
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: standard
---

# Overlay Databank Unlocks Data-driven Analyses of Biomolecules for All

Source ID: `SRC-0057`

## Raw source

- Repository path: `raw/sources/SRC-0057-overlay-databank-unlocks-data-driven-analyses-of-biomolecules.pdf`
- Local relative link: [Open raw source](../../raw/sources/SRC-0057-overlay-databank-unlocks-data-driven-analyses-of-biomolecules.pdf)

## Summary

This Nature Communications paper proposes the overlay databank pattern: leave raw data in stable public repositories and build a lightweight metadata, naming, quality-evaluation, and analysis layer over it. The paper demonstrates the pattern with the NMRlipids Databank, a community-driven collection of atom-resolution lipid membrane MD simulations with programmatic and graphical access. [SRC-0057]

## Key Points

- The paper argues that AI and data-driven analyses are bottlenecked less by raw data existence than by programmatic accessibility, standardization, and community best practices. [SRC-0057]
- The NMRlipids Databank contained 765 simulation trajectories totaling about 0.4 ms at the time of the paper. [SRC-0057, results]
- The overlay structure has a Data layer for raw trajectories, a Databank layer for metadata, naming conventions, quality evaluation, basic computed properties, and analysis programs, and an Application layer for downstream tools. [SRC-0057]
- Basic stored/analyzed membrane properties include area per lipid, C-H bond order parameters, X-ray scattering form factors, membrane thickness, and equilibration times of principal components. [SRC-0057]
- The GUI supports searching simulations by composition, force field, temperature, membrane properties, and quality, making the data usable by nonprogrammers. [SRC-0057]
- The API enables analyses over heterogeneous simulations by mapping simulation-specific atom/molecule names to universal names. [SRC-0057]
- Demonstrations include force-field/model selection against experiments, ML prediction of membrane area/thickness from composition, cholesterol flip-flop analysis, and water permeation/diffusion analyses. [SRC-0057]

## Bundle Links

- Main text: SRC-0057. [SRC-0057]
- Supporting information: SRC-0058, containing databank structure diagrams, metadata-key tables, code lists, workflow diagrams, and supporting analysis figures. [SRC-0058]

## Limitations

- The NMRlipids Databank content is biased toward simulations that have been publicly shared and curated, not the complete universe of membrane simulation data. [SRC-0057]
- ML models trained from the databank inherit the limits of the currently available lipid compositions, force fields, temperatures, and simulation quality. [SRC-0057]
- The overlay design solves access and standardization problems but does not by itself guarantee force-field accuracy or simulation convergence. [SRC-0057]
- The paper demonstrates the approach on lipid bilayers; application to other biomolecules requires analogous metadata standards, naming conventions, and quality metrics. [SRC-0057]

## Links

- [[sources/SRC-0058-supplementary-information-for-overlay-databank-unlocks-data-driven]]
- [[concepts/overlay-databanks-for-biomolecular-simulation-data]]
- [[concepts/machine-learning-potential-datasets]]

## Ingestion QA

### Retrieval questions checked

- What is an overlay databank?
- What layers does the NMRlipids Databank use?
- What simulation properties are stored or analyzed?
- How do the GUI and API differ?
- What examples demonstrate data-driven reuse?
- What limitations remain for ML models and simulation quality?
- How does the supplement support the main article?

### Coverage decision

Complete at `coverage_profile: standard`. The page captures the bundle relationship, overlay architecture, NMRlipids implementation, demonstrations, and limitations.

### Known gaps

- The wiki does not reproduce all figures, lipid/force-field distributions, or every analysis result from the main text.
