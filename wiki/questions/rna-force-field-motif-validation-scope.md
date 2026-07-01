---
type: question
status: active
created: 2026-07-01
updated: 2026-07-01
question_status: open
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/biomolecules/rna
tags:
  - question
  - RNA
  - force-fields
  - validation
  - motifs
related:
  - "[[wiki/concepts/rna-molecular-dynamics-simulations]]"
  - "[[wiki/concepts/rna-force-field-limitations]]"
  - "[[wiki/claims/CLM-0028-rna-force-field-validation-needs-motif-level-and-coupled-error-checks]]"
  - "[[wiki/tensions/TEN-0014-rna-motif-specific-fixes-vs-general-force-field-transfer]]"
sources:
  - SRC-0055
  - SRC-0056
sensitivity: public
encryption: none
---

# RNA Force-Field Motif Validation Scope

## Question

What RNA motif and observable suite is sufficient before treating an RNA force-field change as transferable beyond the local system that motivated it? [SRC-0055] [SRC-0056]

## Context

SRC-0055 shows that the UUCG tetraloop is a small but demanding RNA force-field challenge where local interventions did not produce a generally satisfactory fix. SRC-0056 reviews a broad RNA simulation landscape in which tetraloops, internal loops, helices, ions, riboswitches, ribozymes, ribosomes, and RNA-protein complexes stress different parts of the model. [SRC-0055] [SRC-0056]

## Current Position

Keep the question open. A useful validation suite should include motif-specific stability, transition pathways, ion/solvent behavior, enhanced-sampling convergence, and experimental or QM/QM-MM cross-checks where available. [SRC-0055] [SRC-0056]

## Links

- [[wiki/sources/SRC-0055-uucg-rna-tetraloop-as-a-formidable-force-field]]
- [[wiki/sources/SRC-0056-rna-structural-dynamics-as-captured-by-molecular-simulations]]
- [[wiki/claims/CLM-0028-rna-force-field-validation-needs-motif-level-and-coupled-error-checks]]
