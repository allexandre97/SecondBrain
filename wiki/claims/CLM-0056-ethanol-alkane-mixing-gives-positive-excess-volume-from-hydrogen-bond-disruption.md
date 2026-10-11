---
type: claim
status: active
created: 2026-10-01
updated: 2026-10-01
claim_status: supported
claim_scope: local
areas:
  - research
categories:
  - research/experimental-benchmarking
  - research/molecular-simulation/force-fields
tags:
  - claim
  - density
  - excess-molar-volume
  - ethanol
  - n-heptane
  - n-octane
  - hydrogen-bonding
  - binary-mixtures
  - high-pressure
related:
  - "[[wiki/sources/SRC-0097-densities-and-derived-thermodynamic-properties-for-the-n]]"
  - "[[wiki/claims/CLM-0051-xray-diffraction-alcohol-oh-hydrogen-bond-geometry]]"
  - "[[wiki/claims/CLM-0052-neutron-md-liquid-ethanol-winding-hydrogen-bonded-chains]]"
sources:
  - SRC-0097
sensitivity: public
encryption: none
---

# Mixing Ethanol with n-Heptane or n-Octane Gives Positive Excess Volume, Attributed to Hydrogen-Bond Disruption

## Claim

High-pressure density measurements of n-heptane + ethanol and n-octane + ethanol binary mixtures at (293.15-373.15) K and (0.1-40) MPa show positive excess molar volume ($V^E>0$) at every measured composition, temperature and pressure, increasing in magnitude with temperature (most noticeably at 353.15-373.15 K) and decreasing toward a near-constant value as pressure increases above roughly 20 MPa; by contrast, the non-polar n-heptane + n-octane mixture shows only small (and, per the cited literature, slightly negative) deviations from ideal mixing. The authors attribute the alcohol-containing mixtures' positive excess volume to rupture and stretching of ethanol's self-associated hydrogen-bonded network on dilution by the alkane, with pressure increase favoring stronger/more associated hydrogen bonding (hence smaller excess volume) and temperature increase favoring hydrogen-bond breaking (hence larger excess volume). [SRC-0097, §3.1, §3.3]

## Scope

Local to this source's two alcohol + alkane systems (n-heptane + ethanol, n-octane + ethanol) at the three measured mole fractions (~0.25, 0.50, 0.75) and the stated $T,p$ range. The excess-volume values themselves are given in the source only as a defining equation (Eq. 7) and comparison figures (Fig. 4, Fig. S3), not as a numeric table; this claim reproduces the qualitative trend and its stated physical interpretation, not exact $V^E$ values. The hydrogen-bond-disruption mechanism is the authors' own interpretation (supported by a cited infrared/heat-of-mixing study of ethanol + n-heptane, ref. 37, reporting three possible hydrogen-bond types: monomeric units, double-bonded dimers, and linear polymer chains), not a new structural measurement made in this paper itself. [SRC-0097, §3.1, §3.3]

## Evidence

- Both n-heptane + ethanol and n-octane + ethanol mixtures show positive deviation from ideal mixing behavior (positive $V^E$) across all three measured mole fractions, in contrast to the near-ideal n-heptane + n-octane system. [SRC-0097, §3.3]
- $V^E$ vs. pressure for the equimolar mixtures (Fig. 4) shows a pronounced increase in $V^E$ with temperature, most noticeable at 353.15 K and 373.15 K, and a roughly monotonic decrease in $V^E$ with pressure up to about 20 MPa, after which $V^E$ approaches a roughly constant value at each temperature. [SRC-0097, §3.3, Fig. 4]
- The authors interpret the temperature dependence as increased thermal energy weakening hydrogen bonds between like (ethanol) molecules, and the pressure dependence as compression increasing the alcohol's association constant and decreasing free volume, both of which act to reduce the accessible excess volume at higher pressure. [SRC-0097, §3.3, citing refs. 9-10]
- This interpretation is corroborated by a cited independent infrared-spectroscopy/heat-of-mixing study of ethanol + n-heptane solutions at (293.15-323.15) K (ref. 37), which identifies three possible hydrogen-bond types for ethanol in n-heptane solution (monomeric alcohol units, double-bonded dimers, linear polymer chains), consistent with partial disruption of ethanol self-association on dilution rather than complete breakup. [SRC-0097, §3.1, citing ref. 37]
- The n-heptane + n-octane system's near-ideal behavior (small deviations, slightly negative excess volume increasing in magnitude with temperature per the cited Abdulagatov and Azizov reference) is explained by the similar shape, structure, and low polarity of the two linear alkanes, i.e. the absence of any hydrogen-bond-disruption mechanism. [SRC-0097, §3.3, citing ref. 11]

## Caveats

- No exact $V^E$ numeric values are available from the main paper; this claim is based on the qualitative trend read from Fig. 4 and the authors' discussion, not a transcribed data table (see Known gaps on [[wiki/sources/SRC-0097-densities-and-derived-thermodynamic-properties-for-the-n]]).
- The hydrogen-bond-disruption mechanism is argued by analogy to other literature (ref. 37, infrared spectra of ethanol + n-heptane at lower pressure and a narrower temperature range) rather than directly verified by a structural probe within this paper itself.
- This paper does not measure liquid structure (no diffraction, spectroscopy, or simulation), so it cannot independently confirm the winding-hydrogen-bonded-chain picture of pure liquid ethanol reported in [[wiki/claims/CLM-0052-neutron-md-liquid-ethanol-winding-hydrogen-bonded-chains]] or the OH···OH coordination geometry in [[wiki/claims/CLM-0051-xray-diffraction-alcohol-oh-hydrogen-bond-geometry]]; the connection drawn here is a physically plausible macroscopic/microscopic correspondence (positive excess volume consistent with partial disruption of a hydrogen-bonded network), not a citation link between the papers, and not independently re-derived from SRC-0097's own data by SecondBrain.
- No SecondBrain-tracked force field or simulation project currently uses this high-pressure density/excess-volume dataset as a training or validation target. [Synthesis, not stated in the source]

## Links

- [[wiki/sources/SRC-0097-densities-and-derived-thermodynamic-properties-for-the-n]]
- [[wiki/claims/CLM-0051-xray-diffraction-alcohol-oh-hydrogen-bond-geometry]]
- [[wiki/claims/CLM-0052-neutron-md-liquid-ethanol-winding-hydrogen-bonded-chains]]
