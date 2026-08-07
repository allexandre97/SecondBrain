---
type: concept
status: active
created: 2026-08-05
updated: 2026-08-05
areas:
  - research
categories:
  - research/molecular-simulation/molecular-dynamics
tags:
  - concept
  - dipole-moment
  - dielectric-constant
  - reaction-field
  - Ewald-summation
  - polar-systems
related:
  - "[[wiki/concepts/particle-mesh-ewald-and-long-range-electrostatics]]"
sources:
  - SRC-0075
  - SRC-0076
  - SRC-0077
sensitivity: public
encryption: none
---

# Dipole-Moment Fluctuations and Dielectric Constants in Polar MD

## Summary

The raw dipole-fluctuation expression is a dimensionless fluctuation parameter $A$, not the relative permittivity itself. For conducting-boundary PME and for the atom/site-pair reaction-field convention used by FFRefine through Molly, the operational estimator is $\varepsilon_r=1+A$. The additive one must not be omitted. [SRC-0076, eq. 7; SRC-0077, §2.7]

This is not a geometry-independent rule for every method called "reaction field." A global spherical or molecular reaction-field construction can require a boundary-dependent relation such as Neumann's finite-$\varepsilon_{\mathrm{RF}}$ formula. The estimator must be selected from the actual cutoff and polarization operator, not merely from the presence of a parameter named $\varepsilon_{\mathrm{RF}}$. [SRC-0075; SRC-0076]

## Operational formula for FFRefine

For each saved frame, form the total dipole moment $M$ of the complete neutral periodic sample. From equilibrated samples compute

$$
A=
\frac{\langle M^2\rangle-|\langle M\rangle|^2}
{3\varepsilon_0\langle V\rangle k_BT}.
$$

The relative static permittivity is then

$$
\boxed{\varepsilon_r=1+A}.
$$

Use this formula for both of the electrostatic paths currently supported by FFRefine:

| Simulation electrostatics | Permittivity estimator | Treatment of $\varepsilon_{\mathrm{RF}}$ |
| --- | --- | --- |
| PME with tin-foil/conducting boundaries | $\varepsilon_r=1+A$ | Not applicable |
| Molly atom/site-pair `CoulombReactionField` | $\varepsilon_r=1+A$ | Parameter of the simulated pair potential only; do not insert it into a second post-processing inversion |

For an NVT calculation, replace $\langle V\rangle$ by the fixed volume. For NPT, FFRefine uses the ratio of the dipole fluctuation to the mean sampled volume shown above. If the sampled mean dipole is not exactly zero, retain the subtraction $|\langle M\rangle|^2$.

The corresponding SI expression for absolute permittivity is

$$
\varepsilon=\varepsilon_0\varepsilon_r,
$$

but liquid simulations and experimental tables normally report the dimensionless relative permittivity $\varepsilon_r$.

## Key points

- Never label $A$ itself as the dielectric constant: vacuum has $A=0$ and $\varepsilon_r=1$.
- For FFRefine's current PME and atom/site-pair RF implementations, values such as $A\approx230$ imply $\varepsilon_r\approx231$; they do not indicate a pole.
- The configured RF solvent dielectric changes the Hamiltonian and therefore the sampled fluctuations. It does not, for the current site-pair implementation, select a separate algebraic conversion from $A$ to $\varepsilon_r$.
- The fluctuation observable is the total dipole moment $M$ of the full simulated sample. The area or volume in the formulas is the full sample area/volume, not the cutoff sphere. [SRC-0075, pp. 846–849]
- In three dimensions, minimum-image and spherical-cutoff geometries give $\frac{\varepsilon-1}{\varepsilon+2}=\frac{4\pi}{3}\frac{\langle M^2\rangle}{3Vk_BT}$. [SRC-0075, eq. 26.2.3D]
- Reaction-field geometry gives a formula containing $\varepsilon_{\mathrm{RF}}$; setting $\varepsilon_{\mathrm{RF}}=\varepsilon$ recovers the Kirkwood–Fröhlich relation, while $\varepsilon_{\mathrm{RF}}\to\infty$ gives conducting-boundary conditions. [SRC-0075, eqs. 26.1.3D, 26.3.3D, 26.4.3D]
- Reaction-field simulations are statistically better suited to highly polar systems because their dipole fluctuations grow with the dielectric constant; minimum-image and ordinary spherical-cutoff fluctuations remain bounded as $\varepsilon\to\infty$. [SRC-0075, §4.3]
- In Neumann's global spherical RF geometry, using the conducting-boundary formula at finite reaction-field dielectric overestimates the extracted dielectric constant by a factor approaching $3/2$ in 3D for highly polar systems. This warning does not override the site-pair rule above. [SRC-0075, pp. 848–849]
- For finite interaction-site molecules, the reaction-field correction must match the cutoff operator. Site-site ISRF is self-consistent with the fluctuation formula, whereas a molecular center-of-mass cutoff requires multipole-aware MRF corrections and its compatible fluctuation estimator remains unresolved. [SRC-0076]

## Core equations

### Conducting PME and atom/site-pair RF

In SI units, the estimator used in FFRefine is

$$
A=
\frac{\langle M^2\rangle-|\langle M\rangle|^2}
{3\varepsilon_0\langle V\rangle k_BT},
\qquad
\varepsilon_r=1+A.
$$

Omelyan's individual-site RF expression provides a useful consistency check. At $k\to0$, $j_1(kR)/(kR)\to1/3$ and isotropy gives $G_L(0)=G_K/3$; equation 7 then reduces to the same $\varepsilon_r=1+A$ relation for the site-level fluctuation convention. [SRC-0076, eq. 7]

### Different global spherical RF geometry

Neumann's geometry-dependent formulas below are retained for theory and for implementations that explicitly reproduce that global spherical reaction-field construction. They must not be applied automatically to Molly's atom/site-pair RF trajectory merely because its pair potential has finite $\varepsilon_{\mathrm{RF}}$.

For a homogeneous applied field $E_0$, linear response relates the mean dipole to equilibrium fluctuations: [SRC-0075, eq. 4.3D]

$$
\langle M\rangle_{E_0}=\frac{\langle M^2\rangle}{3k_BT}E_0.
$$

The three-dimensional fluctuation formulas are: [SRC-0075, eqs. 26.1.3D–26.4.3D]

$$
\frac{4\pi}{3}\frac{\langle M^2\rangle}{3Vk_BT}
=
\begin{cases}
\displaystyle
\frac{\varepsilon-1}{\varepsilon+2}
\left(1-\frac{\varepsilon-1}{\varepsilon+2}\frac{2(\varepsilon_{\mathrm{RF}}-1)}{2\varepsilon_{\mathrm{RF}}+1}\right)^{-1}, & \text{reaction field},\\
\displaystyle\frac{\varepsilon-1}{\varepsilon+2}, & \text{minimum image or spherical cutoff},\\
\displaystyle\frac{(2\varepsilon+1)(\varepsilon-1)}{9\varepsilon}, & \varepsilon_{\mathrm{RF}}=\varepsilon,\\
\displaystyle\frac{\varepsilon-1}{3}, & \varepsilon_{\mathrm{RF}}\to\infty.
\end{cases}
$$

## Variable glossary

- $M$: total dipole moment; $V$: full sample volume; $P=M/V$.
- $T$: temperature; $k_B$: Boltzmann constant.
- $A$: dimensionless total-dipole fluctuation parameter.
- $\varepsilon_0$: vacuum permittivity; $\varepsilon_r$: dimensionless relative static permittivity; $\varepsilon=\varepsilon_0\varepsilon_r$: absolute permittivity.
- $\varepsilon_{\mathrm{RF}}$: relative permittivity assigned to the continuum outside an RF cutoff sphere; it is not generally identical to the material response $\varepsilon_r$.
- $T_{\alpha\beta}(r)$: dipole–dipole interaction tensor.
- $G_K=\langle M^2\rangle/(N\mu^2)$: finite-system Kirkwood factor; $g_K$ is the geometry-corrected infinite-system factor. [SRC-0075, eqs. 31–32]

## Derivation sketch and proof map

1. Statistical mechanics gives the linear-response relation between $\langle M\rangle_{E_0}$ and $\langle M^2\rangle$.
2. Electrostatics writes the field as the external field plus a dipole-tensor convolution with the polarization.
3. The local constitutive relation $P=\chi E$ converts this into an integral equation.
4. Fourier transformation is natural for toroidal boundaries: a homogeneous external field has only the $k=0$ component.
5. The zero-wavevector dipole tensor vanishes for minimum-image and spherical-cutoff geometries, but is nonzero for reaction-field geometry. Eliminating $E_0$ yields the geometry-specific formulas. [SRC-0075, §§2–4]

The derivation assumes a sufficiently large system that behaves as a macroscopic dielectric and a local constitutive relation. A nonlocal response may be more appropriate for small systems. [SRC-0075, §6]

## Implementation consequences

- Implement $A$ and $\varepsilon_r=1+A$ as distinct quantities so the additive one cannot be lost.
- Use the same canonical $\varepsilon_r=1+A$ estimator for FFRefine PME and Molly atom/site-pair RF trajectories.
- Treat $\varepsilon_{\mathrm{RF}}$ as simulation provenance and a Hamiltonian parameter, not as an instruction to apply the finite-boundary Neumann inversion.
- Select a different dielectric formula only after demonstrating that the actual interaction geometry, cutoff operator, and polarization observable match its derivation.
- Accumulate $\langle M^2\rangle$ for the full sample volume. Cutoff-sphere fluctuations are not interchangeable with full-system fluctuations. [SRC-0075, pp. 848–855]
- If smoothing multiplies the dipole tensor by $f(r)$, apply the corresponding integral correction to the reaction field; otherwise the effective reaction-field dielectric differs from the requested value. [SRC-0075, eq. 30]
- Report finite-size dependence and local orientational correlations. The Stockmayer test found reaction-field estimates near 65–66 for $N=256$, but left the reaction-field/Ewald discrepancy unresolved. [SRC-0075, pp. 852–856]
- For interaction-site models, retain site-level charge geometry when applying reaction fields; finite molecular size can produce order-$d/R$ errors and nonphysical wavevector-dependent dielectric oscillations under standard PDRF. [SRC-0076]

## Caveats

- The FFRefine rule is scoped to Molly's current atom/site-pair RF implementation. A future charge-group, molecule-center, or multipole RF implementation requires a fresh derivation check.
- The simulation test used a highly polar 3D Stockmayer model at one thermodynamic state and modest system sizes.
- The analysis is in Gaussian units; SI implementations need corresponding convention changes.
- The local constitutive approximation may fail for small or strongly nonlocal systems. [SRC-0075]

## Links

- [[wiki/sources/SRC-0075-dipole-moment-fluctuation-formulas-in-computer-simulations-of]]
- [[wiki/claims/CLM-0035-dielectric-fluctuation-formulas-are-geometry-dependent]]
- [[wiki/questions/QST-0003-reaction-field-versus-ewald-dielectric-limit]]
- [[wiki/tensions/TEN-0017-reaction-field-consistency-versus-ewald-finite-size-behavior]]
- [[wiki/claims/CLM-0036-site-site-reaction-fields-avoid-molecular-size-mismatch]]
- [[wiki/questions/QST-0004-molecular-cutoff-reaction-field-fluctuation-formula]]
- [[wiki/concepts/particle-mesh-ewald-and-long-range-electrostatics]]
