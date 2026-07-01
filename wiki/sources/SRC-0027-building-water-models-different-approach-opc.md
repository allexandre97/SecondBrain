---
type: source
status: active
created: 2026-06-30
updated: 2026-06-30
source_id: SRC-0027
display_title: "Building Water Models: A Different Approach"
short_title: "OPC Water Model"
aliases:
  - "SRC-0027"
  - "OPC Water Model"
  - "Building Water Models: A Different Approach"
source_path: raw/sources/SRC-0027-building-water-models-different-approach-opc.pdf
imported_path: raw/sources/SRC-0027-building-water-models-different-approach-opc.pdf
original_filename: "building-water-models-a-different-approach.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 8ce61c6fa3337a8e8d03742f03081b257e5ce06856350d02d43dde32afc651a5
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
  - water-models
  - opc
  - multipoles
  - hydration-free-energy
  - math-heavy
related:
  - "[[wiki/sources/SRC-0028-building-water-models-different-approach-supporting-information]]"
  - "[[wiki/concepts/opc-water-model]]"
  - "[[wiki/concepts/automated-force-field-training]]"
sources:
  - SRC-0027
cites_sources:
  - SRC-0025
citation_match_status: reviewed
cqt_review_status: linked
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: math-standard
---

# Building Water Models: A Different Approach

Source ID: `SRC-0027`

## Raw source

- Repository path: `raw/sources/SRC-0027-building-water-models-different-approach-opc.pdf`
- Open raw source: [raw/sources/SRC-0027-building-water-models-different-approach-opc.pdf](../../raw/sources/SRC-0027-building-water-models-different-approach-opc.pdf)
## Source bundle

Main paper for SRC-0028, the supporting information. [SRC-0027] [SRC-0028]

## Summary

This 2014 JPCL paper introduces the OPC water model, a rigid fixed-charge water model built by optimizing point-charge positions to reproduce low-order electrostatic multipole moments rather than imposing conventional water geometry. [SRC-0027]

The approach separates the electrostatic charge-distribution design from later Lennard-Jones fitting and reports strong performance on bulk water properties and small-molecule hydration free energies. [SRC-0027]

## Key Points

- OPC relaxes conventional geometry constraints except symmetry, allowing point-charge locations to optimize electrostatic multipoles. [SRC-0027]
- The model uses three point charges in a four-site rigid model and chooses charges/positions to reproduce dipole and quadrupole moments exactly while optimally approximating octupole moments. [SRC-0027]
- The scan over dipole and square-quadrupole values identifies a high-quality OPC region. [SRC-0027]
- OPC reports an average relative error of about $0.76\%$ across a comprehensive set of bulk properties. [SRC-0027]
- Small-molecule hydration free energies are reported with RMSE below $1$ kcal/mol and improved average error relative to common rigid models. [SRC-0027]
- The paper treats missing polarization and limited point-charge expressivity as fundamental caveats for rigid fixed-charge water models. [SRC-0027]

## Key equations

Dipole constraint:

$$
\mu = 2q(z_2-z_1).
$$

[SRC-0027, eq. 1]

Linear quadrupole constraint:

$$
Q_0=-2q\left(\frac{y^2}{2}-z_2^2+z_1^2\right).
$$

[SRC-0027, eq. 2]

Square quadrupole constraint:

$$
Q_T=\frac{3qy^2}{2}.
$$

[SRC-0027, eq. 3]

Geometry implied by multipoles and charge magnitude:

$$
y=\sqrt{\frac{2Q_T}{3q}},
\qquad
z_{1,2}=\frac{2Q_T+3Q_0}{6\mu}\mp\frac{\mu}{4q}.
$$

[SRC-0027, eqs. 5-6]

Bulk-property score:

$$
M=\max\left\{
10-\left|\frac{(x-x_{\mathrm{exp}})100}{x_{\mathrm{exp}}\mathrm{tol}}\right|,
0
\right\}.
$$

[SRC-0027]

## Equation inventory

| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |
| Dipole constraint | SRC-0027 Computational Methods | This page; [[wiki/concepts/opc-water-model]] | Matches water dipole. | $\mu$, $q$, $z_1$, $z_2$ | Charge geometry design. |
| Quadrupole constraints | SRC-0027 Computational Methods | This page | Matches $Q_0$ and $Q_T$. | $Q_0$, $Q_T$, $y$ | Charge geometry design. |
| Geometry formulas | SRC-0027 Computational Methods | This page | Converts multipole targets to charge positions. | $y$, $z_1$, $z_2$, $q$ | Parameter generation. |
| Bulk score | SRC-0027 Computational Methods | This page | Ranks test water models. | $x$, $x_{\mathrm{exp}}$, tolerance | Model selection. |

## Limitations and Caveats

- A three-charge fixed model cannot exactly reproduce all multipoles of real water. [SRC-0027]
- OPC is nonpolarizable, so phase and environment transfer remain bounded by fixed-charge assumptions. [SRC-0027]
- The method is water-specific in its analytic geometry, though the idea of optimizing charge distributions to multipoles is more general. [SRC-0027]

## Links

- [[wiki/sources/SRC-0028-building-water-models-different-approach-supporting-information]]
- [[wiki/concepts/opc-water-model]]
- [[wiki/concepts/automated-force-field-training]]
- [[wiki/questions/force-field-training-validation-scope]]
- [[wiki/tensions/TEN-0007-physical-water-construction-vs-empirical-fitting]]

## Questions

- [[wiki/questions/force-field-training-validation-scope]] - How broad must water-model validation be before treating physical construction criteria as transferable? [SRC-0027]

## Tensions

- [[wiki/tensions/TEN-0007-physical-water-construction-vs-empirical-fitting]] - OPC emphasizes physically motivated charge construction while still requiring empirical validation. [SRC-0027] [SRC-0028]

## Citation links

- `SRC-0025`: The references list Wang, Martinez, and Pande, "Building Force Fields," matching the ingested ForceBalance water-model fitting source. [SRC-0027]

## Open Questions

- How much of OPC's transferability comes from multipole accuracy versus the later Lennard-Jones fit to bulk water? [SRC-0027]

## Ingestion QA

### Retrieval questions checked

- What is different about OPC's construction?
- Which multipoles are matched exactly?
- How are charge positions related to multipole targets?
- What bulk and hydration validations are reported?
- What fixed-charge limitations remain?

### Coverage decision

Complete at `coverage_profile: math-standard`. [SRC-0027]

### Known gaps

- Full property tables and simulation-protocol details are summarized rather than transcribed.
