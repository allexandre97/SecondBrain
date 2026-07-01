---
type: source
status: active
created: 2026-06-30
updated: 2026-06-30
source_id: SRC-0028
display_title: "Supporting Information for Building Water Models"
short_title: "OPC Supporting Information"
aliases:
  - "SRC-0028"
  - "OPC Supporting Information"
  - "Supporting Information for Building Water Models"
source_path: raw/sources/SRC-0028-building-water-models-different-approach-supporting-information.pdf
imported_path: raw/sources/SRC-0028-building-water-models-different-approach-supporting-information.pdf
original_filename: "jz501780a_si_001.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: b6cd991886641131d6584aeff92f8fced09b922c39aad1a7a6d58e298975ceb0
authors:
  - "Saeed Izadi"
  - "Ramu Anandakrishnan"
  - "Alexey V. Onufriev"
author_entities: []
year: 2014
venue: "Journal of Physical Chemistry Letters"
doi: "10.1021/jz501780a"
arxiv:
metadata_review_status: reviewed
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
tags:
  - supporting-information
  - water-models
  - opc
  - multipoles
  - math-heavy
related:
  - "[[wiki/sources/SRC-0027-building-water-models-different-approach-opc]]"
  - "[[wiki/concepts/opc-water-model]]"
sources:
  - SRC-0028
cites_sources: []
citation_match_status: reviewed
cqt_review_status: source-local
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: math-standard
---

# Supporting Information for Building Water Models

Source ID: `SRC-0028`

## Raw source

- Repository path: `raw/sources/SRC-0028-building-water-models-different-approach-supporting-information.pdf`
- Open raw source: [raw/sources/SRC-0028-building-water-models-different-approach-supporting-information.pdf](../../raw/sources/SRC-0028-building-water-models-different-approach-supporting-information.pdf)
## Source bundle

Supporting information for SRC-0027. [SRC-0027] [SRC-0028]

## Summary

This supporting information provides the analytical solution for optimal point charges, bulk-property calculation details, solvation-free-energy details, and additional comparisons for the OPC water-model paper. [SRC-0028]

## Key Points

- The SI writes the dipole, quadrupole, and octupole tensors used in the OPC analytic construction. [SRC-0028]
- It derives equations for point-charge positions and values that sequentially reproduce low-order water multipoles. [SRC-0028]
- It records additional procedures for calculating bulk water properties and solvation free energies. [SRC-0028]

## Key equations

Traceless dipole vector:

$$
p_i=(0,0,\mu).
$$

[SRC-0028]

Quadrupole tensor:

$$
Q_{ij}=
\begin{pmatrix}
-Q_T-Q_0/2 & 0 & 0\\
0 & Q_T-Q_0/2 & 0\\
0 & 0 & Q_0
\end{pmatrix}.
$$

[SRC-0028]

## Equation inventory

| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |
| Dipole tensor, eq. (1) | SRC-0028 analytical solution | This page; [[wiki/concepts/opc-water-model]] | Defines the target water dipole component. | $p_i$, $\mu$ | Multipole target. |
| Quadrupole tensor, eq. (2) | SRC-0028 analytical solution | This page; [[wiki/concepts/opc-water-model]] | Defines linear and square quadrupole components. | $Q_{ij}$, $Q_0$, $Q_T$ | Multipole target. |
| Octupole tensor, eq. (3) | SRC-0028 analytical solution | This page | Defines linear and square octupole components. | $O_{ijk}$, $\Omega_0$, $\Omega_T$ | Higher-moment fitting. |
| Charge constraints, eqs. (4+) | SRC-0028 analytical solution | [[wiki/sources/SRC-0027-building-water-models-different-approach-opc]] | Relates charge positions to multipoles. | $q$, $y$, $z_1$, $z_2$ | OPC charge geometry construction. |

## Links

- [[wiki/sources/SRC-0027-building-water-models-different-approach-opc]]
- [[wiki/concepts/opc-water-model]]

## Citation links

- Source-local review only; no separate first-class citation links were added beyond the main-paper bundle relationship. [SRC-0028]

## Open Questions

- Can the same analytic multipole-first construction be generalized cleanly to flexible or polarizable water models? [SRC-0028]

## Ingestion QA

### Retrieval questions checked

- What tensor definitions support the OPC construction?
- What analytical charge-position solution is included?
- What simulation and solvation details are supplemented?

### Coverage decision

Complete at `coverage_profile: math-standard` as a math-bearing supporting source. [SRC-0028]

### Known gaps

- Long supplementary derivations are summarized to the equations needed for retrieval.
