---
type: concept
status: active
created: 2026-08-05
updated: 2026-08-05
areas:
  - research
categories:
  - research/molecular-simulation/molecular-dynamics
  - research/molecular-simulation/force-fields
tags:
  - concept
  - reaction-field
  - atomic-cutoff
  - energy-conservation
  - force-smoothing
  - molecular-dynamics
related:
  - "[[wiki/concepts/dipole-moment-fluctuation-dielectric-constant]]"
  - "[[wiki/concepts/particle-mesh-ewald-and-long-range-electrostatics]]"
sources:
  - SRC-0077
sensitivity: public
encryption: none
---

# Conservative Reaction-Field Cutoff Schemes

## Summary

Reaction-field electrostatics can be combined with atomic truncation in high-permittivity liquids if the force is modified to vanish smoothly at the cutoff. Additive polynomial shifting (SH) or spline switching (SW) functions alter the short-range interaction only near the cutoff, retain a constant long-range energy term, and permit conservative MD with corrected energies. [SRC-0077]

## Key points

- Charge-group (CG) truncation suppresses straight-cutoff noise for low-permittivity solvents, but atomic (AT) truncation can better preserve local structure and dielectric behavior when the reaction-field correction is large. [SRC-0077, §§1–2]
- The modified scheme requires zero first and second derivatives at $R_c$, while preserving the original interaction at zero separation. [SRC-0077, eqs. 12–13]
- The long-range constant energy contribution has no force or virial; corrected energies remove that bookkeeping term and recover the unmodified RF energy. [SRC-0077, §§2.3 and 2.6]
- In the 57-liquid validation, 4–6 SH and 0.75 SW electrostatic modifications improved agreement with lattice-sum references for thermodynamic and transport properties without requiring force-field reparameterization. [SRC-0077, §§4–5]

## Core equations

The standard pairwise Coulomb-plus-reaction-field influence function is: [SRC-0077, eqs. 1 and 4]

$$
v_{\mathrm{RF},ij}(r)=\frac{q_iq_j}{4\pi\epsilon_0}
\left[
\frac{1}{r}+\frac{\epsilon_{\mathrm{RF}}-1}{1+2\epsilon_{\mathrm{RF}}}\frac{r^2}{R_c^3}
-\frac{3\epsilon_{\mathrm{RF}}}{1+2\epsilon_{\mathrm{RF}}}\frac{1}{R_c}
\right].
$$

The additive shifting function uses two powers: [SRC-0077, eq. 14]

$$
u_o^{\mathrm{SH}}(r)=a_{o,m}r^{m_o}+a_{o,n}r^{n_o},
\qquad 0<m_o<n_o,
$$

with coefficients chosen so the modified influence function and its first two derivatives satisfy: [SRC-0077, eqs. 12–13]

$$
\frac{d\widetilde u_o^{\mathrm O}}{dr}(R_c)=0,
\qquad
\frac{d^2\widetilde u_o^{\mathrm O}}{dr^2}(R_c)=0,
\qquad
u_o^{\mathrm O}(0)=0.
$$

## Implementation consequences

- Keep standard, modified, and corrected energies conceptually separate. The modified force path is conservative for the modified potential; corrected energy is a reporting or free-energy-comparison operation.
- Include the reaction-field self and offset terms when changing partial charges or comparing media, even though they contribute neither forces nor virials. [SRC-0077, eqs. 5–6]
- Use AT truncation cautiously in low-permittivity liquids; use a force-regularizing SH/SW modification when AT is needed for high-permittivity liquids.
- If applying analogous modifications to Lennard-Jones terms, account for their virial effects; the paper finds that a virial correction can improve density and vaporization-enthalpy agreement. [SRC-0077, §4.2]

## Caveats

- The validation is based on GROMOS-compatible 2016H66 force fields, 57 organic liquids, and comparisons to a lattice-sum reference; it is not a universal proof for biomolecular or interfacial systems.
- Mean-field reaction fields assume a homogeneous, isotropic outside medium and can fail near surfaces, macromolecules, or slabs. [SRC-0077, §1]
- The modified interaction changes the force model near the cutoff; even when small, this can interact with force-field parameterization.

## Links

- [[wiki/sources/SRC-0077-reaction-field-electrostatics-in-molecular-dynamics-simulations-development]]
- [[wiki/claims/CLM-0037-conservative-atomic-reaction-field-cutoffs-improve-high-permittivity-md]]
- [[wiki/questions/QST-0005-corrected-energy-and-virial-policy-for-modified-cutoffs]]
- [[wiki/concepts/dipole-moment-fluctuation-dielectric-constant]]
