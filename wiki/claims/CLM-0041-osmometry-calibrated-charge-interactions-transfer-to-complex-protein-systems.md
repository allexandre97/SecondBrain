---
type: claim
status: active
created: 2026-09-03
updated: 2026-09-03
claim_status: supported
claim_scope: source-specific
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/experimental-benchmarking
  - research/biomolecules/proteins
tags:
  - claim
  - osmotic-pressure
  - transferability
  - intrinsically-disordered-proteins
  - biomolecular-condensates
related:
  - "[[wiki/concepts/osmometry-guided-force-field-optimization]]"
  - "[[wiki/claims/CLM-0042-lennard-jones-refinement-outperforms-charge-scaling-after-shared-osmometry-fit]]"
  - "[[wiki/tensions/TEN-0006-observable-fitting-gain-vs-transferability-tradeoff]]"
sources:
  - SRC-0078
sensitivity: public
encryption: none
---

# Osmometry-Calibrated Charge Interactions Transfer to Complex Protein Systems

## Claim

Within the tested Amber ff99SBws/TIP4P-2005 framework, Lennard-Jones corrections calibrated against charged-amino-acid and ion osmometry transfer without further adjustment to improved structural and dynamical agreement for monomeric IDRs, a folded–disordered complex, and charged-protein condensates. [SRC-0078]

## Scope

This is a source-specific transfer claim for the paper's 16-IDR FRET set, ProTα–H1 NMR/contact benchmark, and four ProTα–H1/protamine condensates. It does not establish universal transfer to other force-field/water combinations, nucleic acids, or condensate chemistries. [SRC-0078, pp. 12–19]

## Evidence

- The LJ-refined model increased the 16-IDR FRET concordance correlation from 0.84 to 0.91. [SRC-0078, pp. 12–14 and Fig. 3]
- It improved ProTα $R_1$/$R_2$ relaxation and reduced mean ProTα–H1 contact lifetime from $12.0 \pm 1.0$ ns to $6.3 \pm 0.4$ ns. [SRC-0078, pp. 14–16 and Fig. 4]
- It preserved or improved condensate mean-FRET agreement and brought the especially slow arginine-rich condensate dynamics much closer to experiment. [SRC-0078, pp. 16–18 and Fig. 5]

## Caveats

- The source is a non-peer-reviewed preprint. [SRC-0078, PDF header]
- Several condensate reconfiguration estimates failed the CK convergence test and some original-force-field trajectories were shorter. [SRC-0078, pp. 34–36]
- One low-salt simulation/experiment comparison uses nearby rather than identical salt conditions. [SRC-0078, Fig. 5]

## Links

- [[wiki/sources/SRC-0078-predictive-all-atom-simulations-of-disordered-proteins-and]]
- [[wiki/concepts/osmometry-guided-force-field-optimization]]
- [[wiki/claims/CLM-0042-lennard-jones-refinement-outperforms-charge-scaling-after-shared-osmometry-fit]]

