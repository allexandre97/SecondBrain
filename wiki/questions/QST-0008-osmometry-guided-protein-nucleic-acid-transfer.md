---
type: question
status: active
created: 2026-09-03
updated: 2026-09-03
question_status: open
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/biomolecules/proteins
  - research/biomolecules/rna
  - research/experimental-benchmarking
tags:
  - question
  - osmotic-pressure
  - protein-RNA
  - protein-DNA
  - charge-interactions
  - transferability
related:
  - "[[wiki/concepts/osmometry-guided-force-field-optimization]]"
  - "[[wiki/concepts/rna-force-field-limitations]]"
  - "[[wiki/claims/CLM-0041-osmometry-calibrated-charge-interactions-transfer-to-complex-protein-systems]]"
sources:
  - SRC-0078
sensitivity: public
encryption: none
---

# Osmometry-Guided Protein–Nucleic-Acid Transfer

## Question

Can osmotic-pressure calibration on amino acid–nucleotide and nucleotide–ion solutions correct amine–phosphate and ion interactions well enough to transfer to protein–DNA, protein–RNA, and nucleic-acid-containing condensates?

## Context

SRC-0078 shows transfer from amino-acid/ion osmometry to charged protein systems and proposes phosphate–basic-side-chain interactions as the next target. Conventional additive models can over-stabilize amine–phosphate association, but the paper does not test nucleic acids. [SRC-0078, p. 19]

## Evidence needed

- Concentration-dependent osmometry for chemically relevant amino acid–nucleotide and nucleotide–ion pairs.
- Joint checks of nucleotide–ion, residue–ion, and ion–ion coordination.
- Held-out validation against protein–DNA and protein–RNA complexes before condensate use.
- Structural and dynamical observables, with explicit convergence and salt-condition matching.
- Cross-model tests to distinguish corrections specific to one force-field/water combination from reusable trends.

## Links

- [[wiki/sources/SRC-0078-predictive-all-atom-simulations-of-disordered-proteins-and]]
- [[wiki/concepts/osmometry-guided-force-field-optimization]]
- [[wiki/concepts/rna-force-field-limitations]]

