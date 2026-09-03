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
tags:
  - claim
  - Lennard-Jones
  - charge-scaling
  - transfer-validation
  - parameter-non-identifiability
related:
  - "[[wiki/concepts/osmometry-guided-force-field-optimization]]"
  - "[[wiki/claims/CLM-0041-osmometry-calibrated-charge-interactions-transfer-to-complex-protein-systems]]"
  - "[[wiki/tensions/TEN-0006-observable-fitting-gain-vs-transferability-tradeoff]]"
sources:
  - SRC-0078
sensitivity: public
encryption: none
---

# Lennard-Jones Refinement Outperforms Charge Scaling After a Shared Osmometry Fit

## Claim

For the two ff99SBws variants tested in SRC-0078, comparable success on the osmotic-pressure calibration set did not imply comparable transfer: integral-charge Lennard-Jones refinement outperformed charge scaling on the held-out 16-IDR FRET benchmark and was therefore selected for complex and condensate validation. [SRC-0078, pp. 9–14]

## Scope

This comparison applies to ff99SBws-CS and ff99SBws-LJ as parameterized in the paper. It supports the need for transfer validation; it does not prove that Lennard-Jones refinement generally dominates charge scaling in other models or target domains. [SRC-0078, pp. 9–19]

## Evidence

- Both routes reproduce the osmometry calibration data through distinct combinations of charge and Lennard-Jones changes. [SRC-0078, pp. 9–12]
- The 16-IDR FRET concordance correlation was 0.83 for CS versus 0.91 for LJ, compared with 0.84 for the original model. [SRC-0078, pp. 12–14 and Fig. 3]
- The authors advanced only the LJ model to the folded–disordered and condensate benchmarks. [SRC-0078, p. 14]

## Caveats

- The later validation is not a head-to-head CS/LJ comparison because the CS route was dropped after the IDR screen. [SRC-0078, pp. 13–14]
- Calibration quality does not by itself reveal which microscopic interaction changes are most physical or transferable. [SRC-0078, pp. 9–14]

## Links

- [[wiki/sources/SRC-0078-predictive-all-atom-simulations-of-disordered-proteins-and]]
- [[wiki/concepts/osmometry-guided-force-field-optimization]]
- [[wiki/tensions/TEN-0006-observable-fitting-gain-vs-transferability-tradeoff]]

