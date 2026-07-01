---
type: tension
status: active
created: 2026-07-01
updated: 2026-07-01
tension_status: active
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/biomolecules/rna
tags:
  - tension
  - RNA
  - force-fields
  - transferability
related_claims:
  - "[[wiki/claims/CLM-0028-rna-force-field-validation-needs-motif-level-and-coupled-error-checks]]"
related_questions:
  - "[[wiki/questions/rna-force-field-motif-validation-scope]]"
sources:
  - SRC-0055
  - SRC-0056
sensitivity: public
encryption: none
---

# RNA Motif-Specific Fixes vs General Force-Field Transfer

## Tension

Fixing a specific RNA motif can improve the failure that exposed a force-field defect, but the same intervention may not transfer cleanly across RNA motifs, ions, sampling regimes, or RNA-protein contexts. [SRC-0055] [SRC-0056]

## Evidence

- SRC-0055 reports tailored interventions for the UUCG tetraloop but states that results remained far from a generally satisfactory RNA force-field fix. [SRC-0055]
- SRC-0056 presents RNA MD reliability as system-dependent, with force fields, enhanced sampling, coarse graining, and ion treatment all affecting different RNA systems. [SRC-0056]

## Current Status

Active. The cluster supports motif failures as high-value diagnostics, not as sufficient evidence that a local parameter adjustment is transferable. [SRC-0055] [SRC-0056]

## Links

- [[wiki/sources/SRC-0055-uucg-rna-tetraloop-as-a-formidable-force-field]]
- [[wiki/sources/SRC-0056-rna-structural-dynamics-as-captured-by-molecular-simulations]]
- [[wiki/questions/rna-force-field-motif-validation-scope]]
