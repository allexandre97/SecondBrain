---
type: question
status: active
created: 2026-09-14
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
  - committor
  - direct-shooting
  - independent-validation
  - uncertainty-quantification
related:
  - "[[wiki/concepts/generative-committor-guided-path-sampling]]"
  - "[[wiki/concepts/enhanced-sampling-validation]]"
  - "[[wiki/questions/QST-0002-independent-validation-for-enhanced-sampling-landscapes]]"
  - "[[wiki/claims/CLM-0043-generated-transition-proposals-require-dynamical-validation]]"
  - "[[wiki/tensions/TEN-0016-internal-convergence-vs-external-free-energy-correctness]]"
sources:
  - SRC-0086
  - SRC-0087
sensitivity: public
encryption: none
---

# Scalable Independent Validation of Learned Committors

## Question

How can learned committors and TMD-refined transition-state ensembles be validated independently for large heterogeneous biomolecular systems without making validation as expensive as the rare-event sampling problem itself? [SRC-0087, p. S31]

## Context

Gen-COMPAS validates NANMA and Trp-cage committors using direct unbiased shooting and adds a check against one independent DESRES trajectory for Trp-cage. The Trp-cage aimless-shooting comparison retained 91 structures and obtained $r=0.898$ and $R^2=0.806$. The DESRES check uses forward continuations from 2,028 frames rather than newly launched independent shots, so temporal correlation and overlapping continuations limit a literal binomial interpretation. Direct shooting is described as computationally prohibitive for more complex systems, where eight independently trained VCNs, internal structural convergence, TMD consistency, and comparisons with earlier work carry more of the validation burden. [SRC-0087, pp. S22–S31]

## Current position

A scalable validation design should distinguish at least four questions:

1. Does the learned $q(x)$ predict first-arrival probabilities on held-out configurations?
2. Do structures reached from opposite endpoints toward the same proposal have consistent committors under unbiased shooting?
3. Does the trajectory ensemble cover distinct pathways rather than only one internally stable channel?
4. Does the resulting free-energy reconstruction agree with a reference that changes the principal modelling or sampling assumptions? [SRC-0086, pp. 3, 6] [SRC-0087, pp. S16–S31]

Model-ensemble variance is useful for locating poorly constrained regions, but agreement among models trained on shared data and architecture cannot exclude common bias. [SRC-0087, p. S31]

## Validation boundaries

- Finite-horizon shooting must report unresolved trajectories and censoring rules. [SRC-0087, p. S26]
- A long trajectory generated under a different force-field parameterization is a stringent transfer test but does not isolate every source of disagreement. [SRC-0087, pp. S28–S30]
- Internal TSE/FEL stability and trajectory-level bootstrap uncertainty test consistency with available data, not exhaustive global correctness. [SRC-0086, pp. 3, 6] [SRC-0087, pp. S16–S21]
- Validation cost should be reported alongside production sampling cost rather than omitted from efficiency claims. [SRC-0086, p. 4] [SRC-0087, Table S6]

## Links

- [[wiki/sources/SRC-0086-breaking-timescales-generative-sampling-conformational-transitions]]
- [[wiki/sources/SRC-0087-breaking-timescales-generative-sampling-conformational-transitions-supplement]]
- [[wiki/concepts/generative-committor-guided-path-sampling]]
- [[wiki/concepts/enhanced-sampling-validation]]
- [[wiki/questions/QST-0002-independent-validation-for-enhanced-sampling-landscapes]]
- [[wiki/claims/CLM-0043-generated-transition-proposals-require-dynamical-validation]]
- [[wiki/tensions/TEN-0016-internal-convergence-vs-external-free-energy-correctness]]
