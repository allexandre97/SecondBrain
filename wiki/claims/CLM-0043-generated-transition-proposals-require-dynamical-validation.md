---
type: claim
status: active
created: 2026-09-14
updated: 2026-09-14
claim_status: supported
claim_scope: source-specific
areas:
  - research
categories:
  - research/adaptive-sampling
  - research/molecular-simulation/molecular-dynamics
  - research/machine-learning/molecular-modeling
tags:
  - claim
  - generative-sampling
  - dynamical-validation
  - transition-paths
related:
  - "[[wiki/concepts/generative-committor-guided-path-sampling]]"
  - "[[wiki/concepts/boltzmann-generators-equilibrium-sampling]]"
  - "[[wiki/questions/QST-0009-scalable-independent-validation-of-learned-committors]]"
  - "[[wiki/tensions/TEN-0016-internal-convergence-vs-external-free-energy-correctness]]"
sources:
  - SRC-0086
  - SRC-0087
sensitivity: public
encryption: none
---

# Generated Transition Proposals Require Dynamical Validation

## Claim

In Gen-COMPAS, diffusion-generated molecular structures are proposal targets rather than equilibrium samples or final transition states; kinetic and thermodynamic conclusions are based on explicit-Hamiltonian refinement followed by unbiased trajectories and appropriate reweighting. [SRC-0086, pp. 2–3, 7–8] [SRC-0087, pp. S10–S16]

## Scope

This claim describes the estimator and validation boundary of Gen-COMPAS. It distinguishes structural proposal generation from Boltzmann sampling and does not establish that every TMD-refined target is physically representative or that the resulting trajectory ensemble has global equilibrium coverage. [SRC-0086, pp. 3, 6–8]

## Evidence

- The main paper states that generated coordinates are proposal targets and excludes TMD trajectories from kinetic and thermodynamic estimators. [SRC-0086, p. 7]
- Bidirectional TMD is used to approach a target from both endpoint basins, after which the bias is removed and unbiased shooting begins. [SRC-0086, pp. 2, 8]
- RiteWeight reconstructs stationary weights because those unbiased trajectories start from deliberately non-equilibrium ensembles. [SRC-0087, pp. S15–S16]
- Trp-cage endpoint consistency and independent aimless shooting provide source-specific evidence that the refinement/committor loop can produce dynamically meaningful transition-region structures. [SRC-0087, pp. S26–S30]

## Caveats

- Direct shooting was not performed at the same depth for the largest biomolecular systems. [SRC-0087, p. S31]
- TMD accessibility, committor-model agreement, and internal FEL stability cannot alone exclude missed pathways or shared systematic error. [SRC-0086, pp. 3, 6] [SRC-0087, pp. S16–S21, S31]
- This claim should not be generalized to all molecular generative models; exact-density generative samplers can have a different relationship between generated samples and equilibrium estimation. [SRC-0041]

## Links

- [[wiki/sources/SRC-0086-breaking-timescales-generative-sampling-conformational-transitions]]
- [[wiki/sources/SRC-0087-breaking-timescales-generative-sampling-conformational-transitions-supplement]]
- [[wiki/concepts/generative-committor-guided-path-sampling]]
- [[wiki/concepts/boltzmann-generators-equilibrium-sampling]]
- [[wiki/questions/QST-0009-scalable-independent-validation-of-learned-committors]]
- [[wiki/tensions/TEN-0016-internal-convergence-vs-external-free-energy-correctness]]
