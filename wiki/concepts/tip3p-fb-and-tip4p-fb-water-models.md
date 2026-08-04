---
type: concept
status: active
created: 2026-07-30
updated: 2026-07-30
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/experimental-benchmarking
tags:
  - water-models
  - tip3p-fb
  - tip4p-fb
  - forcebalance
related:
  - "[[wiki/concepts/forcebalance]]"
  - "[[wiki/concepts/opc-water-model]]"
  - "[[wiki/concepts/automated-force-field-training]]"
  - "[[wiki/questions/force-field-training-validation-scope]]"
sources:
  - SRC-0025
  - SRC-0026
sensitivity: public
encryption: none
---

# TIP3P-FB and TIP4P-FB Water Models

## Summary

TIP3P-FB and TIP4P-FB are rigid, fixed-charge three-site and four-site water models fitted with ForceBalance to combined experimental thermodynamic properties and ab initio cluster energies and forces. TIP4P-FB also uses ice-density targets. [SRC-0025] [SRC-0026]

## Model definitions

| Parameter | TIP4P-FB | TIP3P-FB | Units |
| --- | ---: | ---: | --- |
| O-H bond length | 0.9572 | 1.0118 | angstrom |
| H-O-H angle | 104.52 | 108.15 | degree |
| Oxygen vdW $\sigma$ | 3.1655 | 3.1780 | angstrom |
| Oxygen vdW $\epsilon$ | 0.74928 | 0.65214 | kJ/mol |
| Hydrogen charge | 0.52587 | 0.42422 | $e$ |
| Oxygen-virtual-site displacement | 0.10527 | not applicable | angstrom |

TIP4P-FB keeps the starting TIP4P geometry fixed and optimizes its nonbonded parameters and virtual-site displacement. TIP3P-FB also optimizes the rigid molecular geometry because retaining the TIP3P or SPC/E geometry gave poorer fits. [SRC-0025, p. 1888] [SRC-0026, Supporting Table 1]

## Training data

- Six experimental liquid properties: density, enthalpy of vaporization, thermal expansion coefficient, isothermal compressibility, isobaric heat capacity, and dielectric constant. [SRC-0025] [SRC-0026]
- Temperatures from 249.15 to 450 K and pressures from 1 to 9 kbar at 298.15 K. [SRC-0025] [SRC-0026]
- More than 100,000 dual-basis RI-MP2/heavy-aug-cc-pVTZ water-cluster energy and force calculations. [SRC-0025]
- Ice Ih, II, III, V, and VI densities for TIP4P-FB only. [SRC-0025] [SRC-0026]

## Evidence

- TIP4P-FB optimizations starting from TIP4P, TIP4P-Ew, and TIP4P/2005 converge to the same explored parameter region. [SRC-0025, Figure 2]
- At 298.15 K and 1 atm, the reported dielectric constants are $81.3\pm0.9$ for TIP3P-FB and $77.3\pm0.4$ for TIP4P-FB, compared with 78.5 experimentally. [SRC-0025, Table 1]
- The reported self-diffusion coefficients are $2.28\pm0.02$ and $2.21\pm0.02\times10^{-5}$ cm$^2$/s for TIP3P-FB and TIP4P-FB, compared with $2.29\times10^{-5}$ cm$^2$/s experimentally. [SRC-0025, Table 1]
- O-O radial distribution, self-diffusion, and shear viscosity were not fitted, making them held-out checks on structure and kinetics. [SRC-0025] [SRC-0026]

## Limitations

- TIP3P-FB deviates from experimental low-temperature density by up to about 1%; TIP4P-FB captures this behavior more accurately. [SRC-0025, p. 1888]
- Increasing the TIP3P-FB density weight improves density but introduces serious errors in enthalpy of vaporization, radial structure, and self-diffusion, showing a target tradeoff within the three-site functional form. [SRC-0025, p. 1888]
- Both models are rigid and nonpolarizable, and the reported study validates pure water rather than biomolecular solvation. [SRC-0025] [SRC-0026]
- Convergence from several initial TIP4P parameter sets supports local robustness in the explored region, not a general proof of global uniqueness. [SRC-0025, Figure 2]

## Links

- [[wiki/sources/SRC-0025-building-force-fields-automatic-systematic-reproducible-approach]]
- [[wiki/sources/SRC-0026-building-force-fields-forcebalance-supporting-information]]
- [[wiki/concepts/forcebalance]]
- [[wiki/concepts/opc-water-model]]
- [[wiki/concepts/automated-force-field-training]]
- [[wiki/claims/CLM-0009-observable-fitting-needs-held-out-validation]]
- [[wiki/claims/CLM-0012-forcebalance-reduces-manual-fitting-noise]]
- [[wiki/tensions/TEN-0006-observable-fitting-gain-vs-transferability-tradeoff]]
- [[wiki/tensions/TEN-0007-physical-water-construction-vs-empirical-fitting]]
- [[wiki/questions/force-field-training-validation-scope]]

## Open questions

- How well do TIP3P-FB and TIP4P-FB transfer to biomolecular solvation, phase equilibria, and conditions outside the fitted pure-water state points? [SRC-0025] [SRC-0026]
- How sensitive are their parameters to the prior widths, residual scales, and ab initio cluster selection? [SRC-0025] [SRC-0026]
