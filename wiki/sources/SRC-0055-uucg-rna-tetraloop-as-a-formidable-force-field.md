---
type: source
status: active
created: 2026-06-30
updated: 2026-06-30
source_id: SRC-0055
display_title: "UUCG RNA Tetraloop as a Formidable Force-Field Challenge for MD Simulations"
short_title: "UUCG RNA Tetraloop Force-Field Challenge"
authors:
  - Klaudia Mrazikova
  - Vojtech Mlynsky
  - Petra Kuhrova
  - Pavlina Pokorna
  - Holger Kruse
  - Miroslav Krepl
  - Michal Otyepka
  - Pavel Banas
  - Jiri Sponer
year: 2020
venue: "Journal of Chemical Theory and Computation"
doi: "10.1021/acs.jctc.0c00801"
aliases:
  - "SRC-0055"
  - "UUCG RNA Tetraloop Force-Field Challenge"
  - "UUCG RNA Tetraloop as a Formidable Force-Field Challenge for MD Simulations"
source_path: raw/sources/SRC-0055-uucg-rna-tetraloop-as-a-formidable-force-field.pdf
original_filename: "10.1021@acs.jctc.0c00801.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 98f72c3b8069fac5d54fb8dc5c612686052724cb65886c3f93fff007fbfce764
areas:
  - research
categories:
  - research/molecular-simulation/molecular-dynamics
  - research/biomolecules/rna
  - research/molecular-simulation/force-fields
tags:
  - RNA
  - force-fields
  - UUCG-tetraloop
  - AMBER
  - QM-MM
related:
  - "[[wiki/concepts/rna-molecular-dynamics-simulations]]"
  - "[[wiki/concepts/rna-force-field-limitations]]"
cites_sources:
  - SRC-0056
sources:
  - SRC-0055
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: standard
metadata_review_status: reviewed
citation_match_status: reviewed
cqt_review_status: linked
references_text: "Sponer, J. et al. RNA structural dynamics as captured by molecular simulations: A comprehensive overview. Chem. Rev. 2018, 118, 4177-4338."
---

# UUCG RNA Tetraloop as a Formidable Force-Field Challenge for MD Simulations

Source ID: `SRC-0055`

## Raw source

- Repository path: `raw/sources/SRC-0055-uucg-rna-tetraloop-as-a-formidable-force-field.pdf`
- Open raw source: [raw/sources/SRC-0055-uucg-rna-tetraloop-as-a-formidable-force-field.pdf](../../raw/sources/SRC-0055-uucg-rna-tetraloop-as-a-formidable-force-field.pdf)

## Summary

This JCTC paper analyzes why the UUCG RNA tetraloop is difficult for explicit-solvent atomistic MD force fields. The authors analyze nearly 1.3 ms of simulation data and use QM/MM and QM calculations to identify coupled force-field deficiencies rather than a single dominant error. [SRC-0055]

## Key Points

- UUCG tetraloops are small but unusually challenging RNA motifs for MD simulations, despite their thermodynamic stability and well-defined native topology. [SRC-0055]
- The paper traces pathways by which simulations lose the native UUCG state, including changes in backbone substates and loss or rearrangement of signature interactions. [SRC-0055]
- The analysis compares MM force-field behavior with QM/MM and QM calculations for specific interactions and conformational scans. [SRC-0055]
- Identified discrepancies include the 5'-flanking phosphate moiety and signature sugar-base interactions. [SRC-0055]
- The authors conclude that the poor UUCG behavior reflects multiple coupled force-field inaccuracies that amplify each other. [SRC-0055]
- Tailored interventions improved some features but did not yield a fully satisfactory generally applicable RNA force-field fix. [SRC-0055]

## Method Coverage

- Large-scale explicit-solvent MD simulation analysis of UUCG-containing 8-mers. [SRC-0055]
- REST2 and other enhanced-sampling/modified-force-field attempts. [SRC-0055]
- QM/MM and QM scans of local structural motifs and interaction energies. [SRC-0055]
- Comparison against AMBER-family RNA force-field variants and discussion of DESRES force-field behavior. [SRC-0055]

## Limitations

- The paper is intentionally motif-focused; conclusions about UUCG do not automatically quantify every RNA motif. [SRC-0055]
- The authors' attempted fixes may have side effects on other RNA systems and were not presented as a general RNA force-field solution. [SRC-0055]
- QM/MM calculations diagnose local force-field errors but do not replace Boltzmann sampling of full RNA conformational ensembles. [SRC-0055]

## Links

- [[wiki/concepts/rna-molecular-dynamics-simulations]]
- [[wiki/concepts/rna-force-field-limitations]]

## Claims

- [[wiki/claims/CLM-0028-rna-force-field-validation-needs-motif-level-and-coupled-error-checks]]

## Questions

- [[wiki/questions/rna-force-field-motif-validation-scope]]

## Tensions

- [[wiki/tensions/TEN-0014-rna-motif-specific-fixes-vs-general-force-field-transfer]]

## Citation Links

- Confirmed local citation match to [[wiki/sources/SRC-0056-rna-structural-dynamics-as-captured-by-molecular-simulations]] via the reference-list entry for Sponer et al., "RNA structural dynamics as captured by molecular simulations: A comprehensive overview." [SRC-0055]
- Citation review status: reviewed for strong local RNA-cluster links.

## Ingestion QA

### Retrieval questions checked

- Why is the UUCG tetraloop a hard MD benchmark?
- What amount of simulation data was analyzed?
- What interactions and substates were implicated in native-state loss?
- What did QM/MM and QM comparisons reveal?
- Did tailored force-field interventions solve the problem?
- What should not be overgeneralized from this source?

### Coverage decision

Complete at `coverage_profile: standard`. The page captures the source's central claim, methods, identified force-field issues, and limitations.

### Known gaps

- The wiki does not reproduce all QM scans, all force-field variants, or all trajectory-state pathways.
