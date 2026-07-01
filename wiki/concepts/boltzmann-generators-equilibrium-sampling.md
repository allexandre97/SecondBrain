---
type: concept
status: active
created: 2026-06-30
updated: 2026-06-30
areas:
  - research
categories:
  - research/molecular-simulation/free-energy
  - research/machine-learning/scientific-modeling
  - research/machine-learning/molecular-modeling
tags:
  - Boltzmann-generators
  - normalizing-flows
  - equilibrium-sampling
  - reweighting
related:
  - "[[wiki/concepts/free-energy-estimation]]"
  - "[[wiki/concepts/adaptive-enhanced-sampling]]"
  - "[[wiki/concepts/transferable-and-scalable-boltzmann-generators]]"
  - "[[wiki/claims/CLM-0016-boltzmann-generators-need-overlap-and-reweighting-support]]"
  - "[[wiki/tensions/TEN-0009-boltzmann-generator-one-shot-sampling-vs-overlap-risk]]"
sources:
  - SRC-0041
  - SRC-0037
  - SRC-0039
sensitivity: public
encryption: none
---

# Boltzmann Generators for Equilibrium Sampling

## Summary

Boltzmann generators use exact-likelihood generative models, often normalizing flows, to generate proposal samples close to a target Boltzmann distribution and then reweight those samples for unbiased equilibrium estimates when overlap is adequate. [SRC-0041] [SRC-0037]

## Key Points

- The key distinction from ordinary generative modeling is that the generated density is known, so samples can be assigned statistical weights relative to the target Boltzmann density. [SRC-0041]
- Training by energy pushes generated samples toward low-energy regions while a Jacobian/entropy term discourages collapse to a single minimum. [SRC-0041]
- Training by example can help focus the model on relevant configurations when energy-only training is too diffuse or unstable early in training. [SRC-0041]
- Importance reweighting supports equilibrium observables and free-energy estimates, but only if generated samples cover the target support with sufficient effective sample size. [SRC-0037] [SRC-0039]
- Later work extends the original system-specific idea toward transfer across molecules and scale across materials systems. [SRC-0037] [SRC-0039]

## Core equations

**KL-style BG training loss [SRC-0041]:**

$$
J_{\mathrm{KL}} =
E_z\left[u(F_{zx}(z))-\log R_{zx}(z)\right]
$$

**Importance-reweighted observable [SRC-0037]:**

$$
\langle O\rangle_\mu =
\frac{E_{x\sim \tilde p(x)}[w(x)O(x)]}
{E_{x\sim \tilde p(x)}[w(x)]}
$$

## Caveats

- Boltzmann-generator samples are not automatically unbiased; unbiased estimates require reweighting and adequate overlap. [SRC-0041] [SRC-0037]
- Ergodicity is not guaranteed by training alone, so missed states remain a serious risk. [SRC-0041] [SRC-0037]
- Scaling depends heavily on architecture, representation, and whether the target system has exploitable locality or transfer structure. [SRC-0039]

## Links

- [[wiki/sources/SRC-0041-boltzmann-generators-sampling-equilibrium-states-of-many-body]]
- [[wiki/sources/SRC-0037-transferable-boltzmann-generators]]
- [[wiki/sources/SRC-0039-scalable-boltzmann-generators-for-equilibrium-sampling-of-large]]
- [[wiki/concepts/free-energy-estimation]]
- [[wiki/concepts/transferable-and-scalable-boltzmann-generators]]
- [[wiki/claims/CLM-0016-boltzmann-generators-need-overlap-and-reweighting-support]]
- [[wiki/tensions/TEN-0009-boltzmann-generator-one-shot-sampling-vs-overlap-risk]]

## Open Questions

- What diagnostics can reliably detect missing metastable states when a generator has no known convergence guarantee?
