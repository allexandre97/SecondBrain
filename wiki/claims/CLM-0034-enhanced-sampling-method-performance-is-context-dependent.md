---
type: claim
status: active
created: 2026-07-31
updated: 2026-07-31
claim_status: limited
claim_scope: source-specific
areas:
  - research
categories:
  - research/adaptive-sampling
  - research/molecular-simulation/free-energy
  - research/experimental-benchmarking
tags:
  - claim
  - method-selection
  - biological-complexity
related:
  - "[[wiki/concepts/enhanced-sampling-validation]]"
  - "[[wiki/concepts/adaptive-enhanced-sampling]]"
sources:
  - SRC-0074
sensitivity: public
encryption: none
---

# Enhanced-Sampling Method Performance Is Context-Dependent

## Claim

No one of REUS, WT-MtD, WTM-eABF, or OPES dominated all five SRC-0074 assays; performance changed with landscape dimensionality, topology, initialization, and parameter knowledge. [SRC-0074, pp. 8-10]

## Evidence

- REUS was fastest under the paper's sampling-time accounting for the three well-defined one-dimensional processes. [SRC-0074, table 1 and p. 8]
- WTM-eABF was most consistent for the two coupled two-dimensional systems, while WT-MtD did not converge on the BCR-Abl1 DFG flip within its allocation. [SRC-0074, p. 9]
- REUS retained initialization bias in the two-dimensional RBP and kinase landscapes. [SRC-0074, p. 9]
- OPES was competitive with a suitable barrier estimate but could converge to a wrong landscape when the estimate was unsuitable. [SRC-0074, pp. 9-10]

## Scope and caveats

This is a limited empirical claim over five systems, the selected collective variables, the tested implementations, and the authors' parameter choices. The benchmark supports context-dependent selection, not a universal dimensionality-only decision rule. [SRC-0074]

## Links

- [[wiki/sources/SRC-0074-convergence-is-not-correctness-context-dependent-performance-of]]
- [[wiki/concepts/enhanced-sampling-validation]]
- [[wiki/concepts/adaptive-enhanced-sampling]]

