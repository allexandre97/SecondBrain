---
type: question
status: active
created: 2026-07-31
updated: 2026-09-14
question_status: open
areas:
  - research
categories:
  - research/adaptive-sampling
  - research/molecular-simulation/free-energy
  - research/experimental-benchmarking
tags:
  - question
  - cross-method-validation
  - convergence-diagnostics
  - reference-design
related:
  - "[[wiki/concepts/enhanced-sampling-validation]]"
  - "[[wiki/claims/CLM-0033-self-convergence-does-not-establish-free-energy-correctness]]"
  - "[[wiki/tensions/TEN-0016-internal-convergence-vs-external-free-energy-correctness]]"
sources:
  - SRC-0074
  - SRC-0086
  - SRC-0087
sensitivity: public
encryption: none
---

# Independent Validation for Enhanced-Sampling Landscapes

## Question

What practical reference design can distinguish stable method-specific bias from a correct free-energy landscape while minimizing shared collective-variable, force-field, initialization, and algorithm-family errors? [SRC-0074]

## Context

SRC-0074 combines blinded cross-method comparison, a probability-space consensus, and longer multiple-walker WTM-eABF trajectories. This detects failures missed by self-convergence, but the methods share coordinates and molecular models, while WTM-eABF is both a tested method and the long reference. [SRC-0074, p. 2 and Methods]

Gen-COMPAS adds a complementary validation case: direct committor shooting and an independent DESRES trajectory support Trp-cage, whereas larger systems rely more heavily on structural convergence, TMD consistency, trajectory bootstrap, model ensembles, and literature agreement because direct shooting is expensive. [SRC-0086, pp. 3–6] [SRC-0087, pp. S16–S31]

## Current position

A defensible validation protocol should separate internal stability, parameter sensitivity, initialization sensitivity, cross-method agreement, and physical reference checks. It should also state which assumptions remain shared across the supposedly independent comparisons. [SRC-0074]

## Validation boundaries

- Agreement among methods is evidence of consistency, not proof of correctness. [SRC-0074]
- A longer trajectory reduces finite-time error but does not automatically remove method-specific bias. [SRC-0074]
- Independent methods can still share an inadequate collective variable or force field. [SRC-0074]
- Fully independent references may be computationally impractical, so the required evidence should scale with the consequence of an incorrect profile. [SRC-0074]

## Links

- [[wiki/sources/SRC-0074-convergence-is-not-correctness-context-dependent-performance-of]]
- [[wiki/concepts/enhanced-sampling-validation]]
- [[wiki/claims/CLM-0033-self-convergence-does-not-establish-free-energy-correctness]]
- [[wiki/tensions/TEN-0016-internal-convergence-vs-external-free-energy-correctness]]
- [[wiki/questions/QST-0009-scalable-independent-validation-of-learned-committors]]
- [[wiki/sources/SRC-0086-breaking-timescales-generative-sampling-conformational-transitions]]
- [[wiki/sources/SRC-0087-breaking-timescales-generative-sampling-conformational-transitions-supplement]]

