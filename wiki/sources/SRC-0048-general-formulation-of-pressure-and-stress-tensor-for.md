---
type: source
status: active
created: 2026-06-30
updated: 2026-06-30
source_id: SRC-0048
display_title: "General Formulation of Pressure and Stress Tensor for Arbitrary Many-body Interaction Potentials Under Periodic Boundary Conditions"
short_title: "Many-Body Pressure and Stress Tensor"
authors:
  - Aidan P. Thompson
  - Steven J. Plimpton
  - William Mattson
year: 2009
venue: "Journal of Chemical Physics"
doi: "10.1063/1.3245303"
aliases:
  - "SRC-0048"
  - "Many-Body Pressure and Stress Tensor"
  - "General Formulation of Pressure and Stress Tensor for Arbitrary Many-body Interaction Potentials Under Periodic Boundary Conditions"
source_path: raw/sources/SRC-0048-general-formulation-of-pressure-and-stress-tensor-for.pdf
original_filename: "154107_1_online.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 591c1701ef7d2e4a951b46108b04a4b15380ab2f8d9bcef915fd30cee7efa8c8
areas:
  - research
categories:
  - research/molecular-simulation/molecular-dynamics
tags:
  - pressure-tensor
  - virial
  - many-body-potentials
  - periodic-boundary-conditions
related:
  - "[[wiki/concepts/md-pressure-and-stress-tensor-calculation]]"
sources:
  - SRC-0048
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: math-standard
metadata_review_status: reviewed
citation_match_status: partial
cqt_review_status: linked
---

# General Formulation of Pressure and Stress Tensor for Arbitrary Many-body Interaction Potentials Under Periodic Boundary Conditions

Source ID: `SRC-0048`

## Raw source

- Repository path: `raw/sources/SRC-0048-general-formulation-of-pressure-and-stress-tensor-for.pdf`
- Open raw source: [raw/sources/SRC-0048-general-formulation-of-pressure-and-stress-tensor-for.pdf](../../raw/sources/SRC-0048-general-formulation-of-pressure-and-stress-tensor-for.pdf)

## Summary

Thompson, Plimpton, and Mattson derive equivalent force-virial forms for pressure and stress tensors under periodic boundary conditions that work for arbitrary many-body interatomic potentials. The point of the formulation is implementation: the expressions are written in terms of forces on atoms rather than pair-energy decompositions. [SRC-0048]

## Key Points

- The standard pressure relation separates the ideal kinetic contribution from an internal virial contribution. [SRC-0048, section II]
- Pair-potential virial formulas do not directly generalize to arbitrary many-body potentials, because many-body potentials may not decompose cleanly into pair terms. [SRC-0048]
- The paper derives atom-cell, atom, and group virial forms and shows they are mathematically equivalent. [SRC-0048]
- The atom form is suited to spatial-decomposition MD codes, while the group form supports assignment of virial contributions to atoms. [SRC-0048]
- Numerical tests show the forms agree to machine accuracy. [SRC-0048]

## Key equations

Macroscopic pressure: [SRC-0048, eq. 1]

$$
P = \frac{N k_B T}{V} + \frac{\langle W \rangle}{3V}.
$$

Thermodynamic definition of the internal virial: [SRC-0048, eq. 2]

$$
W(r^N) = -3V \frac{dU}{dV}.
$$

## Variable glossary

- $P$: scalar pressure. [SRC-0048, eq. 1]
- $N$: number of atoms. [SRC-0048, eq. 1]
- $T$: temperature. [SRC-0048, eq. 1]
- $V$: simulation volume. [SRC-0048, eq. 1]
- $W$: internal virial contribution from interatomic forces. [SRC-0048, eq. 1]
- $U$: potential energy. [SRC-0048, eq. 2]

## Equation inventory

| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |
| Pressure relation | Eq. (1) | Key equations | Splits ideal and virial pressure terms | $P$, $N$, $T$, $V$, $W$ | Baseline pressure computation |
| Thermodynamic virial | Eq. (2) | Key equations | Defines virial as volume derivative | $W$, $U$, $V$ | Connects pressure to potential response |
| Atom-cell, atom, group forms | Section III | Mathematical gaps | Equivalent force-based tensor forms | atom forces, periodic images, groups | Core implementation formulas |

## Limitations

- The wiki records the pressure and virial definitions but not every tensor-form derivation; the full atom-cell, atom, and group formulas should be read in the source before implementation. [SRC-0048]
- The paper addresses force virials for periodic atomistic systems, not all possible boundary conditions or nonequilibrium stress definitions. [SRC-0048]

## Mathematical gaps

- Full tensor derivations and periodic-image bookkeeping are summarized rather than reproduced.

## Links

- [[wiki/concepts/md-pressure-and-stress-tensor-calculation]]

## Claims

- [[wiki/claims/CLM-0024-force-based-virials-generalize-pressure-and-stress-to-many-body-md]]
- [[wiki/claims/CLM-0025-constraints-and-long-range-electrostatics-change-pressure-tensor-accounting]]

## Questions

- [[wiki/questions/md-virial-pressure-implementation-for-autodiff-and-many-body-potentials]]

## Tensions

- [[wiki/tensions/TEN-0013-analytic-constraint-virials-vs-autodiff-energy-gradients]]

## Citation links

- Citation review status: partial. Bibliographic metadata was checked from the PDF first page; no source-to-source citation link within SRC-0047 through SRC-0054 was promoted without direct bibliography evidence.

## Ingestion QA

### Retrieval questions checked

- What problem does the paper solve for many-body potentials?
- Which virial forms are derived?
- Why is force-based formulation useful for MD codes?
- What are the central pressure and virial equations?
- What remains in the raw source for implementation?

### Coverage decision

Complete at `coverage_profile: math-standard`. The source page captures scope, main formulas, implementation relevance, and derivation gaps.
