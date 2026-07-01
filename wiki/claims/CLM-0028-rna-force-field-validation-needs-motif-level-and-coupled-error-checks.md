---
type: claim
status: active
created: 2026-07-01
updated: 2026-07-01
claim_status: supported
claim_scope: cross-source
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/biomolecules/rna
tags:
  - claim
  - RNA
  - force-fields
  - validation
  - motifs
related:
  - "[[wiki/concepts/rna-molecular-dynamics-simulations]]"
  - "[[wiki/concepts/rna-force-field-limitations]]"
  - "[[wiki/questions/rna-force-field-motif-validation-scope]]"
  - "[[wiki/tensions/TEN-0014-rna-motif-specific-fixes-vs-general-force-field-transfer]]"
sources:
  - SRC-0055
  - SRC-0056
sensitivity: public
encryption: none
---

# RNA Force-Field Validation Needs Motif-Level and Coupled-Error Checks

## Claim

RNA force-field validation needs motif-level tests and coupled-error analysis because apparently small motifs can fail through multiple interacting backbone, base, sugar, ion, and sampling errors rather than one isolated parameter defect. [SRC-0055] [SRC-0056]

## Evidence

- SRC-0055 shows that the UUCG tetraloop can lose its native state in long explicit-solvent simulations and traces the failure to coupled force-field inaccuracies rather than one straightforward correction. [SRC-0055]
- SRC-0055 uses QM/MM and QM checks to identify discrepancies in the 5'-flanking phosphate moiety and signature sugar-base interactions. [SRC-0055]
- SRC-0056 reviews RNA MD as bottlenecked by force-field accuracy, long-timescale sampling, ion interactions, and system-dependent validation limits. [SRC-0056]
- SRC-0056 treats tetraloops, tetranucleotides, internal loops, ions, riboswitches, ribozymes, and RNA-protein complexes as distinct validation contexts rather than one homogeneous RNA category. [SRC-0056]

## Caveats

Motif-level validation does not mean every motif failure generalizes to all RNA. It means a broadly useful RNA force field should survive targeted motif tests before being trusted for predictive RNA dynamics. [SRC-0055] [SRC-0056]

## Links

- [[wiki/sources/SRC-0055-uucg-rna-tetraloop-as-a-formidable-force-field]]
- [[wiki/sources/SRC-0056-rna-structural-dynamics-as-captured-by-molecular-simulations]]
- [[wiki/concepts/rna-force-field-limitations]]
