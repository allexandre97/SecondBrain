---
type: claim
status: active
created: 2026-07-31
updated: 2026-07-31
claim_status: supported
claim_scope: source-specific
areas:
  - research
categories:
  - research/adaptive-sampling
  - research/molecular-simulation/free-energy
  - research/experimental-benchmarking
tags:
  - claim
  - convergence-diagnostics
  - cross-method-validation
related:
  - "[[wiki/concepts/enhanced-sampling-validation]]"
  - "[[wiki/questions/QST-0002-independent-validation-for-enhanced-sampling-landscapes]]"
  - "[[wiki/tensions/TEN-0016-internal-convergence-vs-external-free-energy-correctness]]"
sources:
  - SRC-0074
sensitivity: public
encryption: none
---

# Self-Convergence Does Not Establish Free-Energy Correctness

## Claim

Stability of a free-energy landscape relative to its own final estimate is necessary but does not establish that the landscape is thermodynamically correct. [SRC-0074, eq. 20 and pp. 9-10]

## Evidence

- OPES runs for Abl-SH3:p41 at barrier settings of 18 and 25 kcal/mol satisfied the paper's self-convergence threshold but disagreed with the other methods and the consensus landscape. [SRC-0074, p. 9]
- OPES membrane-permeation runs at 10 and 15 kcal/mol produced qualitatively incorrect central hysteresis while appearing internally stable. [SRC-0074, p. 9]
- The paper's separate self and reference RMSDs formalize the distinction between within-run stability and agreement with an external landscape. [SRC-0074, eqs. 20-21]

## Scope and caveats

This claim applies directly to the five enhanced-sampling assays and convergence definition tested by SRC-0074. It does not imply that every stable estimate is wrong or that cross-method consensus is ground truth; it establishes that an internal plateau alone cannot rule out a stable bias. [SRC-0074]

## Links

- [[wiki/sources/SRC-0074-convergence-is-not-correctness-context-dependent-performance-of]]
- [[wiki/concepts/enhanced-sampling-validation]]
- [[wiki/questions/QST-0002-independent-validation-for-enhanced-sampling-landscapes]]
- [[wiki/tensions/TEN-0016-internal-convergence-vs-external-free-energy-correctness]]

