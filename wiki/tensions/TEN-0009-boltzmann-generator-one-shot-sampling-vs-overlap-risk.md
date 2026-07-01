---
type: tension
status: active
created: 2026-07-01
updated: 2026-07-01
tension_status: active
areas:
  - research
categories:
  - research/molecular-simulation/free-energy
  - research/machine-learning/molecular-modeling
tags:
  - tension
  - Boltzmann-generators
  - reweighting
  - sampling
related_claims:
  - "[[wiki/claims/CLM-0016-boltzmann-generators-need-overlap-and-reweighting-support]]"
related_questions:
  - "[[wiki/questions/overlap-support-diagnostics-for-free-energy-estimators]]"
sources:
  - SRC-0037
  - SRC-0039
  - SRC-0041
sensitivity: public
encryption: none
---

# Boltzmann Generator One-Shot Sampling vs Overlap Risk

## Tension

Boltzmann generators promise fast independent proposal samples, but their statistically corrected estimates remain vulnerable to target-overlap failure, low effective sample size, and missed metastable states. [SRC-0041] [SRC-0037] [SRC-0039]

## Evidence

- The original Boltzmann generator method relies on exact-density reweighting and warns that ergodicity is not guaranteed by training alone. [SRC-0041]
- Transferable Boltzmann generators improve zero-shot dipeptide sampling but still require validity checks, state coverage, and effective-sample-size diagnostics. [SRC-0037]
- Scalable materials Boltzmann generators improve system-size transfer through locality while still assessing ESS and free-energy-estimation quality. [SRC-0039]

## Current Status

Active. The cluster supports Boltzmann generators as reweightable proposal methods, not as replacements for overlap diagnostics.

## Links

- [[wiki/sources/SRC-0037-transferable-boltzmann-generators]]
- [[wiki/sources/SRC-0039-scalable-boltzmann-generators-for-equilibrium-sampling-of-large]]
- [[wiki/sources/SRC-0041-boltzmann-generators-sampling-equilibrium-states-of-many-body]]
- [[wiki/concepts/boltzmann-generators-equilibrium-sampling]]
- [[wiki/questions/overlap-support-diagnostics-for-free-energy-estimators]]
