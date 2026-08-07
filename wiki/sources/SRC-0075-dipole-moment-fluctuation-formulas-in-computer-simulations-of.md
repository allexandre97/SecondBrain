---
type: source
status: active
created: 2026-08-05
updated: 2026-08-05
source_id: SRC-0075
display_title: "Dipole Moment Fluctuation Formulas in Computer Simulations of Polar Systems"
short_title: "Dipole Moment Fluctuation Formulas"
aliases:
  - "SRC-0075"
  - "Dipole Moment Fluctuation Formulas"
  - "Neumann 1983 dielectric fluctuation formulas"
source_path: raw/sources/SRC-0075-dipole-moment-fluctuation-formulas-in-computer-simulations-of.pdf
imported_path: raw/sources/SRC-0075-dipole-moment-fluctuation-formulas-in-computer-simulations-of.pdf
original_filename: "Dipole moment fluctuation formulas in computer simulations of polar systems.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 64c0c250db31d09469641f8fde3a26acbcb81c54e4b0c16206b54377f54d3aec
authors:
  - "Martin Neumann"
author_entities: []
year: 1983
venue: "Molecular Physics, 50(4), 841–858"
doi: "10.1080/00268978300102721"
arxiv:
metadata_review_status: reviewed
areas:
  - research
categories:
  - research/molecular-simulation/molecular-dynamics
tags:
  - scientific-paper
  - math-heavy
  - dipole-moment
  - dielectric-constant
  - reaction-field
  - toroidal-boundary-conditions
  - Ewald-summation
  - Stockmayer-system
related:
  - "[[wiki/concepts/dipole-moment-fluctuation-dielectric-constant]]"
  - "[[wiki/concepts/particle-mesh-ewald-and-long-range-electrostatics]]"
sources:
  - SRC-0075
cites_sources: []
citation_match_status: partial
cqt_review_status: linked
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: math-standard
peer_review_status: peer-reviewed
---

# Dipole Moment Fluctuation Formulas in Computer Simulations of Polar Systems

Source ID: `SRC-0075`

## Raw source

- Repository path: `raw/sources/SRC-0075-dipole-moment-fluctuation-formulas-in-computer-simulations-of.pdf`
- Open raw source: [raw/sources/SRC-0075-dipole-moment-fluctuation-formulas-in-computer-simulations-of.pdf](../../raw/sources/SRC-0075-dipole-moment-fluctuation-formulas-in-computer-simulations-of.pdf)

## Summary

Neumann derives dielectric-constant fluctuation and polarization formulas for two- and three-dimensional polar systems with toroidal boundary conditions, minimum-image interactions, spherical cutoffs, and reaction fields. The Fourier-space treatment makes the boundary conditions explicit and shows that the reaction-field formulas match those for periodic Ewald geometry with a reaction field. [SRC-0075, abstract and §§2–4]

The main practical result is that the correct dipole-fluctuation formula depends on the interaction geometry and reaction-field dielectric, and that the area/volume is that of the full simulated sample. A highly polar Stockmayer simulation supports reaction-field estimates near $\varepsilon=65$–$66$ but leaves an unresolved discrepancy with published Ewald estimates. [SRC-0075, §§4–6]

## Key points

- For a homogeneous applied field, linear response gives $\langle M\rangle_{E_0}=\langle M^2\rangle E_0/(3k_BT)$ in 3D. [SRC-0075, eq. 4.3D]
- Minimum-image and spherical-cutoff geometries have a zero $k=0$ dipole-tensor contribution and therefore yield the Clausius–Mossotti-like fluctuation relation. [SRC-0075, §§2–4]
- Reaction-field geometry has a nonzero zero-wavevector contribution and yields a formula parameterized by $\varepsilon_{\mathrm{RF}}$. [SRC-0075, eqs. 21.3D–26.1.3D]
- Setting $\varepsilon_{\mathrm{RF}}=\varepsilon$ gives Kirkwood–Fröhlich; taking $\varepsilon_{\mathrm{RF}}\to\infty$ gives conducting-boundary conditions. [SRC-0075, eqs. 26.3.3D–26.4.3D]
- The full sample volume, not the cutoff sphere, belongs in the fluctuation formulas. [SRC-0075, pp. 848–849]
- Smoothing the cutoff requires a corresponding reaction-field correction; otherwise the effective continuum dielectric differs from the requested $\varepsilon_{\mathrm{RF}}$. [SRC-0075, eq. 30]

## Methods and evidence

The paper combines statistical-mechanical linear response with an electrostatic polarization integral equation. It solves the convolution using Fourier transformation, where a homogeneous external field occupies only the zero-wavevector mode. The simulation test uses 256-particle 3D Stockmayer systems with $\mu^{*2}=3.0$, $\rho^*=0.822$, $T^*=1.15$, a spherical cutoff at half the box length, and reaction-field values $\varepsilon_{\mathrm{RF}}=50$ and $\infty$. [SRC-0075, §§2–5]

The reaction-field runs produced $\varepsilon\approx66$ for $\varepsilon_{\mathrm{RF}}=50$ and $\varepsilon\approx65$ for $\varepsilon_{\mathrm{RF}}=\infty$. Minimum-image and spherical-cutoff fluctuations were bounded and did not yield reliable dielectric constants for the 256-particle system. Published Ewald results for related system sizes were lower and had a weaker, non-monotonic size dependence. [SRC-0075, table and §§5–6]

## Mathematical structure

The proof map is: (1) derive the fluctuation/response relation; (2) write the polarization field as an external field plus a dipole-tensor convolution; (3) impose the local constitutive relation; (4) solve the toroidal convolution in Fourier space; (5) evaluate the zero-wavevector tensor for each geometry; and (6) eliminate the applied field. The paper also gives an appendix proof that toroidal convolution becomes multiplication in Fourier space. [SRC-0075, §§2–4 and Appendix]

## Key equations

The 3D geometry-dependent fluctuation relation is recorded on [[wiki/concepts/dipole-moment-fluctuation-dielectric-constant]]. In compact form: [SRC-0075, eqs. 26.1.3D–26.4.3D]

$$
\frac{4\pi}{3}\frac{\langle M^2\rangle}{3Vk_BT}
=
\begin{cases}
\displaystyle
\frac{\varepsilon-1}{\varepsilon+2}
\left[1-\frac{\varepsilon-1}{\varepsilon+2}\frac{2(\varepsilon_{\mathrm{RF}}-1)}{2\varepsilon_{\mathrm{RF}}+1}\right]^{-1}, & \mathrm{RF},\\[1em]
\displaystyle\frac{\varepsilon-1}{\varepsilon+2}, & \mathrm{MI/SC},\\[0.5em]
\displaystyle\frac{(2\varepsilon+1)(\varepsilon-1)}{9\varepsilon}, & \varepsilon_{\mathrm{RF}}=\varepsilon,\\[0.5em]
\displaystyle\frac{\varepsilon-1}{3}, & \varepsilon_{\mathrm{RF}}\to\infty.
\end{cases}
$$

The source also provides the 2D analogues, which use area $A$ and replace the 3D depolarization factors with their 2D forms. They are summarized on the concept page but not reproduced in full here. [SRC-0075, eqs. 26.1.2D–26.4.2D]

## Variable glossary

- $M$: total dipole moment; $V$: full sample volume; $P$: polarization.
- $\varepsilon$: material dielectric constant; $\varepsilon_{\mathrm{RF}}$: reaction-field continuum dielectric.
- $T_{\alpha\beta}$: dipole–dipole tensor; $E_0$: externally applied field.
- $G_K$: finite-system Kirkwood factor; $g_K$: infinite-system geometry-corrected factor. [SRC-0075, eqs. 31–32]

## Equation inventory

| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |
| Linear-response fluctuation relation | SRC-0075, eq. 4.3D, p. 843 | This page; [[wiki/concepts/dipole-moment-fluctuation-dielectric-constant]] | Connects applied-field response to equilibrium fluctuations. | $M$, $E_0$, $T$ | Defines observable-to-response conversion. |
| Polarization integral equation | SRC-0075, eq. 9, p. 844 | This page, derivation sketch | Incorporates singular dipole kernel and boundary geometry. | $P$, $E_0$, $T_{\alpha\beta}$ | Determines the zero-wavevector term. |
| Fourier-space solution | SRC-0075, eq. 12, p. 845 | This page, proof map | Solves the toroidal convolution. | $P(k)$, $\chi$, $\mathcal{T}(k)$ | Natural route for periodic/toroidal boundaries. |
| Reaction-field fluctuation formula | SRC-0075, eq. 26.1.3D, p. 848 | This page; concept page | Extracts $\varepsilon$ from full-sample fluctuations. | $M$, $V$, $\varepsilon$, $\varepsilon_{\mathrm{RF}}$ | Must match configured reaction field. |
| MI/SC fluctuation formula | SRC-0075, eq. 26.2.3D, p. 848 | This page; concept page | Gives Clausius–Mossotti-like extraction. | $M$, $V$, $\varepsilon$ | Applies when the zero-mode tensor vanishes. |
| Smoothed reaction-field correction | SRC-0075, eq. 30, p. 850 | This page, implementation notes | Defines effective dielectric after smoothing. | $f(r)$, $\varepsilon'_{\mathrm{RF}}$ | Prevents requested/effective mismatch. |

## Proof map

The appendix proves the Fourier convolution identity for toroidal boundary conditions. The main text then uses the homogeneous-field $k=0$ mode; symmetry makes that mode vanish for minimum-image and spherical-cutoff geometries, while the reaction-field term supplies a nonzero isotropic contribution. [SRC-0075, Appendix and §§2–4]

## Implementation notes

- Choose the fluctuation formula from the actual boundary/cutoff/reaction-field configuration.
- Use the full sample volume in $\langle M^2\rangle/V$, not the cutoff-sphere volume.
- Preserve finite-size and long-range-method diagnostics; reaction-field parameter consistency alone does not settle the Ewald discrepancy.
- Apply the smoothing correction when using a differentiable cutoff.

## Mathematical gaps

- Full reproduction of every intermediate equation, numerical table, figure, and cited-reference derivation is omitted.
- The 2D formula family is represented on the concept page but not duplicated in full here.
- The local constitutive relation may be inadequate for small systems; the nonlocal alternative is stated but not developed into an estimator. [SRC-0075, §6]
- The source does not resolve why its reaction-field Stockmayer estimates exceed the cited Ewald values in the thermodynamic-limit extrapolation.

## Claims

- [[wiki/claims/CLM-0035-dielectric-fluctuation-formulas-are-geometry-dependent]]

## Questions

- [[wiki/questions/QST-0003-reaction-field-versus-ewald-dielectric-limit]]

## Tensions

- [[wiki/tensions/TEN-0017-reaction-field-consistency-versus-ewald-finite-size-behavior]]

## Links

- [[wiki/concepts/dipole-moment-fluctuation-dielectric-constant]]
- [[wiki/concepts/particle-mesh-ewald-and-long-range-electrostatics]]

## Metadata notes

- The PDF identifies Martin Neumann, Molecular Physics 50(4), 841–858 (1983), DOI `10.1080/00268978300102721`. Its PDF metadata lists a 2006 generation date; the bibliographic year is taken from the article citation on the first page.
- References were skimmed for context, but no exact citation match to an already-ingested source was accepted; `citation_match_status` remains `partial`.

## Ingestion QA

### Retrieval questions checked

- What is the central contribution? A Fourier-space derivation of geometry-specific dipole-fluctuation and polarization formulas. [SRC-0075]
- Which volume belongs in the formula? The full simulated sample volume, not the cutoff sphere. [SRC-0075]
- How do MI/SC and reaction-field formulas differ? MI/SC yield the Clausius–Mossotti-like relation; RF adds an $\varepsilon_{\mathrm{RF}}$ factor. [SRC-0075]
- What are the limiting cases? $\varepsilon_{\mathrm{RF}}=\varepsilon$ gives Kirkwood–Fröhlich; $\varepsilon_{\mathrm{RF}}\to\infty$ gives conducting boundaries. [SRC-0075]
- What smoothing caveat matters? The reaction-field correction must use the smoothing-function integral. [SRC-0075]
- What evidence supports the formulas? The Stockmayer test gives consistent RF estimates near 65–66, while MI/SC are unreliable at that size. [SRC-0075]
- What remains unresolved? The difference between RF and published Ewald estimates and its particle-number dependence. [SRC-0075]
- What should not be overgeneralized? The one-state, highly polar Stockmayer benchmark and local-response assumption. [SRC-0075]

### Coverage decision

Complete at `coverage_profile: math-standard`. The wiki captures the central derivation, formula structure, limiting cases, variables, implementation implications, simulation evidence, limitations, proof map, equation inventory, and retrieval QA.

### Known gaps

- Full reproduction of every intermediate equation, numerical table, figure, and cited-reference derivation is omitted.
- The 2D formula family is summarized but not duplicated in full on this source page.
