---
type: question
status: active
created: 2026-08-05
updated: 2026-08-05
question_status: open
areas:
  - research
categories:
  - research/molecular-simulation/molecular-dynamics
tags:
  - question
  - reaction-field
  - interaction-site-models
  - dielectric-constant
  - finite-size-effects
related:
  - "[[wiki/concepts/dipole-moment-fluctuation-dielectric-constant]]"
  - "[[wiki/claims/CLM-0036-site-site-reaction-fields-avoid-molecular-size-mismatch]]"
sources:
  - SRC-0076
sensitivity: public
encryption: none
---

# Molecular-Cutoff Reaction-Field Fluctuation Formula

## Question

Can a complete, finite-size-consistent fluctuation formula be derived for the molecular center-of-mass cutoff using the modified molecular reaction-field potential and its quadrupole terms?

## Evidence and current position

Omelyan derives the molecular reaction field and its corrected intermolecular potential, but states that constructing the corresponding molecular-cutoff fluctuation formula is not simple and leaves it for future work. The site-site ISRF route has the explicit wavevector-dependent formula; the molecular-cutoff PDRF route should therefore not reuse that formula without qualification. [SRC-0076, §§3 and 5]

## Links

- [[wiki/sources/SRC-0076-9901032v1]]
- [[wiki/concepts/dipole-moment-fluctuation-dielectric-constant]]
- [[wiki/claims/CLM-0036-site-site-reaction-fields-avoid-molecular-size-mismatch]]
