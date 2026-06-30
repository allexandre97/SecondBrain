---
type: source
status: active
created: 2026-06-30
updated: 2026-06-30
source_id: SRC-0015
display_title: "Supporting Information for Lipid Force Field SAXS Reparameterization"
short_title: "Lipid SAXS Reparameterization Supplement"
aliases:
  - "SRC-0015"
  - "Lipid SAXS Reparameterization Supplement"
  - "Supporting Information for Lipid Force Field SAXS Reparameterization"
source_path: raw/sources/SRC-0015-lipid-force-field-saxs-reparameterization-supporting-information.pdf
imported_path: raw/sources/SRC-0015-lipid-force-field-saxs-reparameterization-supporting-information.pdf
original_filename: "jp5c08658_si_001.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 103992aa4dc24c77805c79912b6fc36402702834fcf32e6158ebdf2fe5acd821
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
tags:
  - supporting-information
  - forcebalance
  - lipid-force-field
  - saxs
related:
  - "[[sources/SRC-0014-lipid-force-field-saxs-reparameterization]]"
  - "[[concepts/force-field-training-from-experimental-observables]]"
sources:
  - SRC-0015
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: standard
---

# Supporting Information for Lipid Force Field SAXS Reparameterization

Source ID: `SRC-0015`

## Raw source

- Repository path: `raw/sources/SRC-0015-lipid-force-field-saxs-reparameterization-supporting-information.pdf`
- Local relative link: [Open raw source](../../raw/sources/SRC-0015-lipid-force-field-saxs-reparameterization-supporting-information.pdf)

## Source bundle

Supporting information for SRC-0014. [SRC-0014] [SRC-0015]

## Summary

This supporting information provides the parameter tables, SAXS comparison figures, extended-sampling checks, and additional validation plots for the ForceBalance-SAS lipid reparameterization in SRC-0014. [SRC-0015]

## Key Points

- The SI documents separate optimization trials for head-group, tail-group, combined head/tail, torsional, and water-parameter variants. [SRC-0015]
- Figures compare experimental SAXS, original CHARMM36 SAXS, and optimized-parameter SAXS across pure POPE/POPG and solvent-stressed systems. [SRC-0015]
- Table S1 records original and final CHARMM36 parameters for the final optimized model. [SRC-0015]
- Extended 200 ns simulations are used to check whether apparent transfer behavior persists beyond short validation runs. [SRC-0015]

## Evidence

The SI makes the transferability diagnosis in SRC-0014 auditable by showing which optimized variants improve the training profile and which fail on THF or butanol stress tests. [SRC-0015]

## Links

- [[sources/SRC-0014-lipid-force-field-saxs-reparameterization]]
- [[concepts/force-field-training-from-experimental-observables]]
- [[questions/force-field-training-validation-scope]]

## Open Questions

- Which parameter changes in Table S1 are most responsible for the observed improvements and failures? [SRC-0015]

## Ingestion QA

### Retrieval questions checked

- What supporting figures compare optimized and original SAXS?
- Which optimization trials are documented?
- Where are the final parameter values recorded?
- What extended-sampling checks are included?

### Coverage decision

Complete at `coverage_profile: standard` as a supporting-information source. [SRC-0015]

### Known gaps

- Numerical tables are summarized rather than transcribed.
