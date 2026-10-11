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
  - neutron-diffraction
  - hydrogen-bonding
  - ethanol
  - radial-distribution-function
  - molecular-dynamics
related:
  - "[[wiki/sources/SRC-0093-the-structure-of-liquid-ethanol-a-neutron-diffraction]]"
  - "[[wiki/sources/SRC-0092-hydrogen-bonding-in-liquid-methanol-and-ethanol-determined]]"
  - "[[wiki/claims/CLM-0051-xray-diffraction-alcohol-oh-hydrogen-bond-geometry]]"
sources:
  - SRC-0093
sensitivity: public
encryption: none
---

# Neutron Diffraction and MD Confirm Winding Hydrogen-Bonded Chains in Liquid Ethanol

## Claim

Neutron diffraction (H/D isotopic substitution) measurements of 10 partial/composite structure factors for pure liquid ethanol at 22 °C, compared against four-site and nine-site OPLS molecular dynamics simulations, confirm that hydrogen bonding dominates the liquid's intermolecular structure, consistent with disordered, winding hydrogen-bonded chains rather than closed hexamer or tetramer clusters. [SRC-0093]

## Scope

Local to this single source. The result is specific to pure liquid ethanol at 22±1 °C and atmospheric pressure. It compares the measured nearest-neighbor hydroxyl-hydroxyl ($g_{H1H1}(r)$) peak against three specific cluster models (U-shaped open chain, tetramer closed chain, hexamer closed chain) proposed by Sarkar and Joarder, not against every possible structural model. The authors explicitly note that small quantities of closed-chain hexamer clusters could still coexist, and leave open whether/how the structure changes at higher pressure or temperature. [SRC-0093, §V.B, §VI]

## Evidence

- The measured neutron structure factors ($H_{\alpha\beta}(Q)$, including the directly measured $H_{H1H1}(Q)$ partial) agree generally well with both four-site and nine-site OPLS MD simulations, especially for $H_{H1H1}(Q)$. [SRC-0093, §V.B, Fig. 2]
- The nearest-neighbor peak in the measured $g_{H1H1}(r)$ agrees well in position and area with a U-shaped open-chain model, but not with tetramer or hexamer closed-chain models (from Sarkar and Joarder). [SRC-0093, §V.B, Fig. 7(a)]
- This U-shaped/open-chain agreement is consistent with the MD winding hydrogen-bonded chain structure, directly illustrated in MD simulation snapshots. [SRC-0093, Fig. 8]
- Two additional peaks at 3.3 Å and 4.4 Å in the measured ethanol $g_{H1H1}(r)$ (beyond the nearest-neighbor peak, absent at the same distances in methanol) are reproduced by the MD winding-chain model and correspond to the repeat H1···H1···H1 distance along the chain. [SRC-0093, §V.B, Fig. 7(b)]
- The neutron-derived intermolecular nonhydrogen ($XX$) composite structure factor agrees with Narten and Habenschuss's independently measured x-ray intermolecular structure factor for ethanol beyond $Q>5\ \text{Å}^{-1}$, where both are dominated by oxygen-oxygen correlations — an independent, different-technique cross-check of the same liquid's intermolecular structure. [SRC-0093, §V.B, Fig. 5; cf. [[wiki/sources/SRC-0092-hydrogen-bonding-in-liquid-methanol-and-ethanol-determined]]]
- Integrated coordination numbers (hydroxyl H surrounded by $2.0\pm0.2$ hydroxyl H within 3.0 Å; O surrounded by $0.95\pm0.3$ hydroxyl H within 2.1 Å and $2.0\pm0.2$ O within 3.0 Å) are consistent in magnitude with SRC-0092's x-ray-derived ethanol coordination number ($n=1.81(9)$ OH···OH neighbors at 2.808(8) Å), though the two papers measure somewhat different specific distances/site pairs by different techniques and are not identical quantities. [SRC-0093, §V.B; [[wiki/claims/CLM-0051-xray-diffraction-alcohol-oh-hydrogen-bond-geometry]]]

## Caveats

- This is an average, ensemble-averaged structural picture derived from the nearest-neighbor peak in a radial distribution function, not a direct observation of individual chain topologies; the authors compare only the nearest-neighbor interaction when ranking cluster models against the data. [SRC-0093, §V.B]
- The four-site and nine-site MD models disagree with each other (and partially with experiment) on specific peak positions by 0.07-0.16 Å, traced to differences in the dihedral potentials controlling internal C-O/C-C rotation; agreement with a winding-chain picture is therefore somewhat model-dependent, not purely experimental. [SRC-0093, §V.A-B]
- The authors explicitly state that closed-chain hexamer clusters may still survive in small quantities within the liquid at room temperature, so the winding-chain picture is a dominant-structure claim, not an exclusive one. [SRC-0093, §VI]
- Whether liquid ethanol's structure transitions from winding chains toward clusters at higher pressure/temperature (as reported for supercritical methanol by Yamaguchi et al.) is explicitly left as an open question for future experiments, not addressed in this paper. [SRC-0093, §VI]
- No SecondBrain-tracked force field or simulation project currently uses this data as a training or validation target; it is recorded here as a candidate experimental structural reference and OPLS-style baseline ethanol force field, analogous to the O-O/H-O/H-H radial-distribution-function validation data already used for water models in FFRefine. [Synthesis, not stated in the source]

## Links

- [[wiki/sources/SRC-0093-the-structure-of-liquid-ethanol-a-neutron-diffraction]]
- [[wiki/sources/SRC-0092-hydrogen-bonding-in-liquid-methanol-and-ethanol-determined]]
- [[wiki/claims/CLM-0051-xray-diffraction-alcohol-oh-hydrogen-bond-geometry]]
