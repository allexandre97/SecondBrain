---
type: claim
status: active
created: 2026-07-01
updated: 2026-07-01
claim_status: limited
claim_scope: cross-source
areas:
  - research
categories:
  - research/molecular-simulation/free-energy
  - research/machine-learning/molecular-modeling
tags:
  - claim
  - Boltzmann-generators
  - reweighting
  - effective-sample-size
related:
  - "[[wiki/concepts/boltzmann-generators-equilibrium-sampling]]"
  - "[[wiki/concepts/transferable-and-scalable-boltzmann-generators]]"
  - "[[wiki/tensions/TEN-0009-boltzmann-generator-one-shot-sampling-vs-overlap-risk]]"
sources:
  - SRC-0037
  - SRC-0039
  - SRC-0041
sensitivity: public
encryption: none
---

# Boltzmann Generators Need Overlap and Reweighting Support

## Claim

Boltzmann generators are useful for equilibrium estimates when their generated distribution overlaps the target enough for reweighting; one-shot generation alone does not remove support, ESS, or missed-state risk. [SRC-0041] [SRC-0037] [SRC-0039]

## Scope

This claim covers the original, transferable, and scalable Boltzmann-generator pages in the current cluster. It does not judge all flow-based samplers or diffusion samplers. [SRC-0037] [SRC-0039] [SRC-0041]

## Evidence

- The original Boltzmann generator paper enables unbiased estimates through exact generated densities and reweighting, while warning that overlap and ergodicity can fail. [SRC-0041]
- Transferable Boltzmann generators distinguish reweightable generators from approximate emulators and report effective sample size and state coverage as central diagnostics. [SRC-0037]
- Scalable materials Boltzmann generators use locality to improve large-system feasibility but still report ESS and free-energy-estimation diagnostics. [SRC-0039]

## Caveats

- ESS is a necessary diagnostic but not a proof that all metastable states were generated. [SRC-0037] [SRC-0041]

## Links

- [[wiki/sources/SRC-0037-transferable-boltzmann-generators]]
- [[wiki/sources/SRC-0039-scalable-boltzmann-generators-for-equilibrium-sampling-of-large]]
- [[wiki/sources/SRC-0041-boltzmann-generators-sampling-equilibrium-states-of-many-body]]
- [[wiki/concepts/boltzmann-generators-equilibrium-sampling]]
- [[wiki/concepts/transferable-and-scalable-boltzmann-generators]]
