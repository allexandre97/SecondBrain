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
  - x-ray-diffraction
  - hydrogen-bonding
  - alcohols
  - radial-distribution-function
related:
  - "[[wiki/sources/SRC-0092-hydrogen-bonding-in-liquid-methanol-and-ethanol-determined]]"
  - "[[wiki/claims/CLM-0009-observable-fitting-needs-held-out-validation]]"
  - "[[wiki/concepts/tolerance-normalized-multi-observable-losses]]"
  - "[[wiki/claims/CLM-0052-neutron-md-liquid-ethanol-winding-hydrogen-bonded-chains]]"
sources:
  - SRC-0092
sensitivity: public
encryption: none
---

# X-Ray Diffraction Alcohol OH Hydrogen-Bond Geometry

## Claim

X-ray diffraction of liquid methanol and ethanol at 20 °C shows each hydroxyl group has, on average, about 1.8 hydrogen-bonded OH···OH neighbors at a well-defined intermolecular distance of approximately 2.8 Å, a pattern the authors interpret as chain-like molecular association rather than rings or a fully disordered liquid. [SRC-0092]

## Scope

Local to this single source. The result is specific to pure liquid methanol and pure liquid ethanol at 20 °C and atmospheric pressure; it does not cover other temperatures, pressures, mixtures, or other alcohols. The coordination number and bond distance are outputs of a least-squares fit to the large-$k$ part of the measured distinct structure function (with coordination number as a free parameter), not a direct real-space count. [SRC-0092, §III, Table IV]

## Evidence

- Methanol: coordination number $n=1.77(7)$, OH···OH distance $r=2.798(6)$ Å, rms deviation $l=0.142(6)$ Å. [SRC-0092, Table IV]
- Ethanol: coordination number $n=1.81(9)$, OH···OH distance $r=2.808(8)$ Å, rms deviation $l=0.113(7)$ Å. [SRC-0092, Table IV]
- The intermolecular radial distribution function $G_d(r)$ shows a peak near 2.8 Å for both liquids that is absent in the radial distribution functions of alkanes, supporting attribution of the peak specifically to hydrogen-bonded hydroxyl groups rather than to generic packing. [SRC-0092, §IV, Fig. 4]
- Small-angle x-ray scattering data cited by the authors show $S(k\to0)$ for several alcohols matches the value predicted from isothermal compressibility, which the authors use to argue against large persistent clusters and in favor of ordinary liquid-density fluctuations superimposed on local chain association. [SRC-0092, §IV, ref. 26]

## Caveats

- This is an average, ensemble/time-averaged structural picture; the authors explicitly note large local and instantaneous deviations from the mean configuration, and expect correlations to extend only a few molecular diameters from any given molecule. [SRC-0092, §IV]
- The chain-association interpretation is the authors' structural reading of the data, not a uniquely determined topology; they state that further experimental work or statistical-mechanical modeling would be needed to fully define the intermolecular structure. [SRC-0092, §IV]
- The fitted intramolecular bond geometry (C-O, C-C, C···O; see the source page) was obtained sequentially, with the methanol C-O fit feeding into the ethanol C-C/C···O fits, so the ethanol intramolecular parameters are conditional on the methanol result rather than independently measured. [SRC-0092, Table II]
- No SecondBrain-tracked force field or simulation project currently uses this data as a training or validation target; it is recorded here as a candidate experimental structural reference, analogous to the O-O/H-O/H-H radial-distribution-function validation data already used for water models in FFRefine. [Synthesis, not stated in the source]

## Links

- [[wiki/sources/SRC-0092-hydrogen-bonding-in-liquid-methanol-and-ethanol-determined]]
- [[wiki/claims/CLM-0009-observable-fitting-needs-held-out-validation]]
- [[wiki/concepts/tolerance-normalized-multi-observable-losses]]
- [[wiki/claims/CLM-0052-neutron-md-liquid-ethanol-winding-hydrogen-bonded-chains]] - A later, independent neutron-diffraction/MD study of liquid ethanol [SRC-0093] directly compares its own data against this source's x-ray intermolecular structure factor (good agreement for $Q>5\ \text{Å}^{-1}$) and reports a broadly consistent hydroxyl coordination picture, though it measures different specific site pairs by a different technique; see that claim for details rather than treating it as additional evidence for this claim's specific x-ray-derived numbers.
