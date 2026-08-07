---
type: claim
status: active
created: 2026-08-05
updated: 2026-08-05
claim_status: supported
claim_scope: source-specific
areas:
  - research
categories:
  - research/molecular-simulation/molecular-dynamics
tags:
  - claim
  - reaction-field
  - interaction-site-models
  - dielectric-constant
  - water-models
related:
  - "[[wiki/concepts/dipole-moment-fluctuation-dielectric-constant]]"
  - "[[wiki/claims/CLM-0035-dielectric-fluctuation-formulas-are-geometry-dependent]]"
sources:
  - SRC-0076
sensitivity: public
encryption: none
---

# Site-Site Reaction Fields Avoid Molecular-Size Mismatch

## Claim

For rigid interaction-site polar molecules, the standard point-dipole reaction-field correction is not self-consistent with a molecular center-of-mass cutoff. Applying the reaction field at individual charge sites (ISRF) yields a site-site potential and fluctuation formula matched to the microscopic polarization operator; a molecular cutoff requires additional multipole terms. [SRC-0076, §§2–3]

## Evidence

Omelyan derives the site-site reaction-field potential with a quadratic charge-separation correction and shows that the usual molecular-cutoff point-dipole reaction field omits finite-molecule effects. [SRC-0076, eqs. 8–12]

For a molecular reaction field (MRF), the leading correction contains quadrupole–quadrupole and quadrupole–dipole terms. The omitted terms in the usual potential introduce errors of order $d/R$, while the modified MRF reduces the truncation error to order $(d/R)^2$. [SRC-0076, eq. 16 and §3]

In the MCY-water test, standard PDRF produced nonphysical oscillations in wavevector-dependent dielectric quantities, with deviations from ISRF reaching about 25% near the first Kirkwood-factor maximum. [SRC-0076, §4]

## Scope and caveats

The result concerns rigid interaction-site models with permanent charges and excludes molecular/electronic polarizability. The proposed MRF potential is not accompanied by a complete molecular-cutoff fluctuation formula in this paper. [SRC-0076]

## Links

- [[wiki/sources/SRC-0076-9901032v1]]
- [[wiki/concepts/dipole-moment-fluctuation-dielectric-constant]]
- [[wiki/questions/QST-0004-molecular-cutoff-reaction-field-fluctuation-formula]]
