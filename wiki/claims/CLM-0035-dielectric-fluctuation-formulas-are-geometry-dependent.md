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
  - dielectric-constant
  - dipole-fluctuations
  - reaction-field
  - electrostatics
related:
  - "[[wiki/concepts/dipole-moment-fluctuation-dielectric-constant]]"
sources:
  - SRC-0075
sensitivity: public
encryption: none
---

# Dielectric Fluctuation Formulas Are Geometry-Dependent

## Claim

The relation used to infer a dielectric constant from total dipole fluctuations depends on the boundary and interaction treatment. Minimum-image and spherical-cutoff toroidal simulations use a Clausius–Mossotti-like expression, while reaction-field simulations require the reaction-field-dependent formula; the simulation volume is the full sample volume in both cases. [SRC-0075, eqs. 26.1.3D–26.3.3D]

## Evidence

Neumann derives the formulas by solving the polarization integral equation in Fourier space and showing that the zero-wavevector dipole tensor vanishes for minimum-image/spherical-cutoff geometry but not for reaction-field geometry. [SRC-0075, §§2–4]

In the 256-particle Stockmayer test, reaction-field runs with $\varepsilon_{\mathrm{RF}}=50$ and $\infty$ gave dielectric constants near 66 and 65, while minimum-image and spherical-cutoff runs could not provide reliable values for that system size. [SRC-0075, pp. 852–855]

## Scope and caveats

This is a geometry-specific theoretical result tested on one highly polar Stockmayer state. It should not be generalized to small systems without checking the local-response assumption or to SI-unit implementations without converting the Gaussian-unit factors. [SRC-0075]

## Links

- [[wiki/concepts/dipole-moment-fluctuation-dielectric-constant]]
- [[wiki/sources/SRC-0075-dipole-moment-fluctuation-formulas-in-computer-simulations-of]]
