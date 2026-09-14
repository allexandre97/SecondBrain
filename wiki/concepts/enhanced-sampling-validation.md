---
type: concept
status: active
created: 2026-07-31
updated: 2026-09-14
areas:
  - research
categories:
  - research/adaptive-sampling
  - research/molecular-simulation/free-energy
  - research/experimental-benchmarking
tags:
  - enhanced-sampling
  - convergence-diagnostics
  - cross-method-validation
  - free-energy-landscapes
related:
  - "[[wiki/sources/SRC-0074-convergence-is-not-correctness-context-dependent-performance-of]]"
  - "[[wiki/concepts/adaptive-enhanced-sampling]]"
  - "[[wiki/concepts/free-energy-estimation]]"
  - "[[wiki/concepts/on-the-fly-probability-enhanced-sampling]]"
  - "[[wiki/questions/QST-0002-independent-validation-for-enhanced-sampling-landscapes]]"
  - "[[wiki/tensions/TEN-0016-internal-convergence-vs-external-free-energy-correctness]]"
  - "[[wiki/sources/SRC-0086-breaking-timescales-generative-sampling-conformational-transitions]]"
  - "[[wiki/sources/SRC-0087-breaking-timescales-generative-sampling-conformational-transitions-supplement]]"
  - "[[wiki/concepts/generative-committor-guided-path-sampling]]"
  - "[[wiki/questions/QST-0009-scalable-independent-validation-of-learned-committors]]"
sources:
  - SRC-0074
  - SRC-0086
  - SRC-0087
sensitivity: public
encryption: none
---

# Enhanced-Sampling Validation

## Summary

Enhanced-sampling validation separates internal stability from external correctness. A free-energy landscape that no longer changes relative to its own final estimate may still reflect parameter misspecification, initialization bias, incomplete orthogonal sampling, or a poor collective-variable model. [SRC-0074]

## Diagnostic hierarchy

1. **Internal stability:** test whether the estimated landscape is stable over time after removing its arbitrary additive offset. This is necessary for a stopping decision but tests only consistency with the same trajectory. [SRC-0074, eqs. 19-20]
2. **Parameter and initialization sensitivity:** vary consequential settings and starting structures. SRC-0074 shows false internal convergence for some OPES barrier settings and persistent seeded corridors in multidimensional REUS. [SRC-0074, pp. 9-10]
3. **Cross-method agreement:** compare independently produced landscapes on a common coordinate grid, using normalized probabilities or aligned free energies. [SRC-0074, eqs. 14-21]
4. **Extended or independent reference:** when possible, compare with longer simulations or a reference that changes the main algorithmic assumptions. A method-marginalized average alone cannot exclude shared errors. [SRC-0074, p. 2 and Methods]
5. **Physical validation:** check basin order, barrier locations, and free-energy differences against experimental or established mechanistic constraints where available. [SRC-0074, pp. 4-9]

## Generative transition-path diagnostics

Gen-COMPAS adds diagnostics specific to learned transition proposals. Consecutive transition-state ensembles are compared through nearest-neighbour RMSD distributions and Wasserstein distance; reweighted FELs receive trajectory-level bootstrap and partial-data degradation checks; bidirectional TMD endpoints are compared by predicted committor; and direct unbiased shooting is used where computationally feasible. These diagnostics answer different questions and should not be collapsed into one convergence label. [SRC-0087, pp. S16–S35]

Eight-network committor ensembles provide a cheaper epistemic-disagreement signal for large systems, but cannot exclude a bias shared by all models. The paper correspondingly limits its FELs to exploratory local and pathway-level interpretation when global equilibrium convergence is not independently established. [SRC-0086, pp. 3, 6] [SRC-0087, p. S31]

## Context-dependent selection

In the five SRC-0074 assays, REUS was the recommended default for well-defined one-dimensional reaction coordinates, while WTM-eABF was most robust for the two coupled two-dimensional landscapes. WT-MtD was better framed as an exploratory mapper for unknown topology, and OPES required barrier-sensitivity tests plus external validation. These are scoped benchmark findings, not a universal ranking. [SRC-0074, table 2]

## Core equations

Self-convergence compares the aligned landscape at time $t$ with its own final estimate: [SRC-0074, eq. 20]

$$
\operatorname{RMSD}_{\mathrm{self}}(t)=
\left[
\frac{1}{N}\sum_i
\left(\widetilde A(\xi_i,t)-A(\xi_i,t_\infty)\right)^2
\right]^{1/2}.
$$

Cross-method consistency compares it with an independently constructed reference landscape: [SRC-0074, eq. 21]

$$
\operatorname{RMSD}_{\mathrm{ref}}(t)=
\left[
\frac{1}{N}\sum_i
\left(\widetilde A(\xi_i,t)-A_{\mathrm{ref}}(\xi_i)\right)^2
\right]^{1/2}.
$$

The two values answer different questions and should not be collapsed into one convergence label. [SRC-0074]

## Implementation consequences

- Record internal stability, parameter sensitivity, initialization sensitivity, and external agreement as separate diagnostics. [SRC-0074]
- Predefine comparison coordinates and alignment rules so methods are not tuned toward each other's final answers. [SRC-0074, p. 2]
- Treat a multi-method consensus as an agreement measure, not truth, and prefer references that differ in both duration and algorithmic assumptions. [SRC-0074, Methods]
- Report compute accounting, setup cost, replica count, and synchronization constraints alongside cumulative simulation time. [SRC-0074, table 1 and pp. 8-10]

## Caveats

- Cross-method agreement can be wrong when methods share a collective variable, force field, or initialization artifact. [SRC-0074]
- A long reference using one of the compared algorithms is not fully method-independent. [SRC-0074, p. 2]
- The method-selection boundaries in SRC-0074 come from five systems and should be expanded before becoming general rules. [SRC-0074]

## Links

- [[wiki/sources/SRC-0074-convergence-is-not-correctness-context-dependent-performance-of]]
- [[wiki/concepts/adaptive-enhanced-sampling]]
- [[wiki/concepts/free-energy-estimation]]
- [[wiki/concepts/on-the-fly-probability-enhanced-sampling]]
- [[wiki/claims/CLM-0033-self-convergence-does-not-establish-free-energy-correctness]]
- [[wiki/claims/CLM-0034-enhanced-sampling-method-performance-is-context-dependent]]
- [[wiki/questions/QST-0002-independent-validation-for-enhanced-sampling-landscapes]]
- [[wiki/tensions/TEN-0016-internal-convergence-vs-external-free-energy-correctness]]
- [[wiki/sources/SRC-0086-breaking-timescales-generative-sampling-conformational-transitions]]
- [[wiki/sources/SRC-0087-breaking-timescales-generative-sampling-conformational-transitions-supplement]]
- [[wiki/concepts/generative-committor-guided-path-sampling]]
- [[wiki/questions/QST-0009-scalable-independent-validation-of-learned-committors]]

## Open questions

- What reference design best reduces shared collective-variable, force-field, and method-family bias without multiplying cost beyond practical use? [SRC-0074]

