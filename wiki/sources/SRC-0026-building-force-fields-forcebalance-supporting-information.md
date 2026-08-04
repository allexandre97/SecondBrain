---
type: source
status: active
created: 2026-06-30
updated: 2026-07-30
source_id: SRC-0026
display_title: "Supporting Information for Building Force Fields"
short_title: "ForceBalance Supporting Information"
aliases:
  - "SRC-0026"
  - "ForceBalance Supporting Information"
  - "Supporting Information for Building Force Fields"
source_path: raw/sources/SRC-0026-building-force-fields-forcebalance-supporting-information.pdf
imported_path: raw/sources/SRC-0026-building-force-fields-forcebalance-supporting-information.pdf
original_filename: "jz500737m_si_001.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: ca3852db9cb4efd2a27e43ae4066cb0ea4b1d44c6dd61e108414b1656cb6df3b
authors:
  - "Lee-Ping Wang"
  - "Todd J. Martinez"
  - "Vijay S. Pande"
author_entities: []
year: 2014
venue: "Journal of Physical Chemistry Letters"
doi: "10.1021/jz500737m"
arxiv:
metadata_review_status: reviewed
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
tags:
  - supporting-information
  - forcebalance
  - water-models
related:
  - "[[wiki/sources/SRC-0025-building-force-fields-automatic-systematic-reproducible-approach]]"
  - "[[wiki/concepts/forcebalance]]"
  - "[[wiki/concepts/tip3p-fb-and-tip4p-fb-water-models]]"
sources:
  - SRC-0026
cites_sources: []
citation_match_status: reviewed
cqt_review_status: linked
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: deep
source_bundle: building-force-fields-water-models-2014
bundle_role: supplement
---

# Supporting Information for Building Force Fields

Source ID: `SRC-0026`

## Raw source

- Repository path: `raw/sources/SRC-0026-building-force-fields-forcebalance-supporting-information.pdf`
- Open raw source: [raw/sources/SRC-0026-building-force-fields-forcebalance-supporting-information.pdf](../../raw/sources/SRC-0026-building-force-fields-forcebalance-supporting-information.pdf)

## Source bundle

Supporting information in the `building-force-fields-water-models-2014` bundle; SRC-0025 is the main paper. [SRC-0025] [SRC-0026]

## Summary

This supporting information records the optimized TIP3P-FB and TIP4P-FB parameters, experimental target tables, condensed-phase and ab initio simulation protocols, optimizer behavior, and held-out structural and kinetic validation for the ForceBalance study. [SRC-0026]

## Key points

- The SI compares density, enthalpy of vaporization, thermal expansion coefficient, isothermal compressibility, heat capacity, and dielectric constant as functions of temperature. [SRC-0026, Supporting Figures 1-6]
- It also reports O-O radial distribution functions, self-diffusion, and shear viscosity; these three properties are validation observables not used for fitting. [SRC-0026, Supporting Figures 7-9]
- TIP4P-FB retains the initial TIP4P geometry, whereas TIP3P-FB optimizes its O-H bond length and H-O-H angle in addition to nonbonded parameters. [SRC-0026, Supporting Table 1]
- Condensed-phase targets use 216-water NPT simulations in OpenMM/CUDA, with 4 ns trajectories, a 2 fs step, PME electrostatics, and distributed execution through Work Queue. [SRC-0026, Computational Details]
- The theoretical target comprises energy and force calculations for water clusters of 2-22 molecules sampled from liquid-gas and liquid-ice simulations and evaluated at dual-basis RI-MP2/heavy-aug-cc-pVTZ. [SRC-0026, Computational Details]
- Levenberg-Marquardt optimization uses a 0.2 trust radius in rescaled parameter space; rejected noisy steps trigger additional sampling, and later simulations double in length. [SRC-0026, Parameter Optimization]
- Validation uses GROMACS simulations over seven system sizes from 216 to 16,000 waters and six temperatures; diffusion is extrapolated to infinite size, and viscosity is computed both from diffusion-size scaling and the Green-Kubo relation. [SRC-0026, Kinetic Properties]

## Optimized parameters

| Parameter | TIP4P-FB | TIP3P-FB | Units |
| --- | ---: | ---: | --- |
| O-H bond length | 0.9572 | 1.0118 | angstrom |
| H-O-H angle | 104.52 | 108.15 | degree |
| Oxygen vdW $\sigma$ | 3.1655 | 3.1780 | angstrom |
| Oxygen vdW $\epsilon$ | 0.74928 | 0.65214 | kJ/mol |
| Hydrogen charge | 0.52587 | 0.42422 | $e$ |
| Oxygen-virtual-site displacement | 0.10527 | not applicable | angstrom |

All listed prior widths are 0.1 in the corresponding parameter units, except the angle prior width is 0.1 rad. The TIP4P-FB geometry parameters are fixed rather than optimized. [SRC-0026, Supporting Table 1]

## Target and validation design

### Fitted targets

- Liquid density, enthalpy of vaporization, thermal expansion coefficient, isothermal compressibility, isobaric heat capacity, and dielectric constant from 249.15-450 K and at pressures up to 9 kbar. [SRC-0026, Supporting Table 2]
- Ice Ih, II, III, V, and VI densities for TIP4P-FB; these ice-density targets are omitted for TIP3P-FB because the three-site form cannot accurately describe the high-pressure ice phases. [SRC-0026, Supporting Table 3]
- Ab initio cluster energies and forces for clusters of 2-22 water molecules sampled across liquid, vapor, interface, and ice environments. [SRC-0026, Computational Details]

### Held-out validation

- O-O radial distribution function at 298.15 K and 1 atm. [SRC-0026, Supporting Figure 7]
- Self-diffusion coefficient across six temperatures, extrapolated to infinite system size. [SRC-0026, Supporting Figure 8]
- Shear viscosity across six temperatures, checked by two estimators. [SRC-0026, Supporting Figure 9]

## Implementation details

1. Each ForceBalance target pairs a reference data set with a simulation protocol and returns its objective, gradient, and Gauss-Newton Hessian contribution. [SRC-0026, Computational Details]
2. Potential-energy parameter derivatives are evaluated with central finite differences on stored configurations. [SRC-0026, Computational Details]
3. Condensed-phase trajectories are post-processed for properties and derivatives before results return to ForceBalance. [SRC-0026, Computational Details]
4. A rejected optimizer step appends new samples at the previous parameter values; subsequent simulations double in length to reduce statistical noise near convergence. [SRC-0026, Parameter Optimization]
5. Each nonlinear iteration takes approximately 2-12 hours, with convergence to an objective standard error of 1-3 after about 30 cycles. [SRC-0026, Parameter Optimization]

## Limitations and caveats

- The reference cluster geometries were reset to TIP3P geometry before ab initio calculations, constraining the intramolecular geometry represented by those targets. [SRC-0026, Computational Details]
- The full ab initio data set is hosted externally and is not contained in the supplied PDF bundle. [SRC-0026]
- The validation remains pure-water validation; it does not test biomolecular solvation or protein observables. [SRC-0026]
- The reported protocols and engine versions are specific to the 2014 implementation and may not reproduce bitwise under current software. [SRC-0026]

## Links

- [[wiki/sources/SRC-0025-building-force-fields-automatic-systematic-reproducible-approach]]
- [[wiki/concepts/forcebalance]]
- [[wiki/concepts/tip3p-fb-and-tip4p-fb-water-models]]
- [[wiki/claims/CLM-0009-observable-fitting-needs-held-out-validation]]
- [[wiki/claims/CLM-0012-forcebalance-reduces-manual-fitting-noise]]

## Citation links

- Source-local review only; no separate first-class citation links were added beyond the main-paper bundle relationship. [SRC-0026]

## Open questions

- Which supplemental property curves are most sensitive to the regularization strength used in the ForceBalance fit? [SRC-0026]
- How much do the cluster-geometry reset and selected phase points influence the fitted models? [SRC-0026]
- Do the two viscosity estimators remain consistent under independent modern reruns? [SRC-0026]

## Ingestion QA

### Retrieval questions checked

- What supporting property figures are included?
- How does the SI relate to TIP3P-FB and TIP4P-FB validation?
- Are uncertainty estimates shown?
- What are the exact optimized parameter values?
- Which observables are training targets and which are held out?
- What condensed-phase and ab initio protocols generated the target data?
- How does ForceBalance react to a noisy rejected step?
- How are diffusion and viscosity validated against finite-size effects?

### Coverage decision

Complete at `coverage_profile: deep` as supporting information in the SRC-0025/SRC-0026 bundle. The page captures the parameters, target/validation split, main simulation settings, optimizer behavior, and known limitations needed for future retrieval. [SRC-0026]

### Known gaps

- The complete temperature/pressure table and plotted numerical series are summarized rather than transcribed.
- The sample Q-Chem input and basis blocks are not reproduced; the method and basis level are recorded.
