---
type: tension
status: active
created: 2026-07-31
updated: 2026-09-14
tension_status: active
areas:
  - research
categories:
  - research/adaptive-sampling
  - research/molecular-simulation/free-energy
  - research/experimental-benchmarking
tags:
  - tension
  - convergence
  - correctness
  - validation-cost
related:
  - "[[wiki/concepts/enhanced-sampling-validation]]"
  - "[[wiki/claims/CLM-0033-self-convergence-does-not-establish-free-energy-correctness]]"
  - "[[wiki/questions/QST-0002-independent-validation-for-enhanced-sampling-landscapes]]"
sources:
  - SRC-0074
  - SRC-0086
  - SRC-0087
sensitivity: public
encryption: none
---

# Internal Convergence vs External Free-Energy Correctness

## Tension

Internal convergence is cheap and available during one production run, but it can certify a stable wrong landscape. Stronger evidence from parameter sweeps, independent methods, or extended references is more informative but substantially increases computational and workflow cost. [SRC-0074]

## Evidence

OPES produced internally stable but cross-method-inconsistent landscapes under some barrier settings, demonstrating the risk of relying on the cheap diagnostic alone. The authors' recommended remedy requires multiple barrier settings or a second method and therefore makes validation part of the production cost. [SRC-0074, pp. 9-10]

Gen-COMPAS reports structural-coverage, bootstrap, FEL-degradation, TMD-consistency, and model-ensemble diagnostics, but still limits complex-system FELs to exploratory interpretation when global convergence is not independently established. Direct committor shooting strengthens the NANMA and Trp-cage cases but is described as prohibitively expensive for larger systems. [SRC-0086, pp. 3, 6] [SRC-0087, pp. S16–S31]

## Interpretation

The tension is not resolved by replacing self-convergence with consensus. Self-convergence remains useful as a necessary stability check, while consensus can retain shared bias. A practical protocol needs layered evidence whose independence and cost are reported explicitly. [SRC-0074]

## Links

- [[wiki/sources/SRC-0074-convergence-is-not-correctness-context-dependent-performance-of]]
- [[wiki/concepts/enhanced-sampling-validation]]
- [[wiki/claims/CLM-0033-self-convergence-does-not-establish-free-energy-correctness]]
- [[wiki/questions/QST-0002-independent-validation-for-enhanced-sampling-landscapes]]
- [[wiki/questions/QST-0009-scalable-independent-validation-of-learned-committors]]
- [[wiki/sources/SRC-0086-breaking-timescales-generative-sampling-conformational-transitions]]
- [[wiki/sources/SRC-0087-breaking-timescales-generative-sampling-conformational-transitions-supplement]]

