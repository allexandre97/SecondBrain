---
type: tension
status: active
created: 2026-08-20
updated: 2026-08-21
tension_status: active
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/molecular-simulation/free-energy
  - research/statistics/monte-carlo
tags:
  - tension
  - ffrefine
  - observable-sensitivity
  - replay-support
  - trust-region
related:
  - "[[wiki/answers/ffrefine-average-observable-trainability-validation]]"
  - "[[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]"
  - "[[wiki/claims/CLM-0038-fixed-archive-gradient-validation-does-not-establish-fresh-archive-trainability]]"
  - "[[wiki/questions/QST-0006-average-observable-trainability-sampling-budget]]"
related_claims:
  - "[[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]"
  - "[[wiki/claims/CLM-0038-fixed-archive-gradient-validation-does-not-establish-fresh-archive-trainability]]"
related_questions:
  - "[[wiki/questions/QST-0006-average-observable-trainability-sampling-budget]]"
sources:
  - SRC-0018
  - SRC-0023
sensitivity: public
encryption: none
project_evidence:
  - "FFRefine fresh-archive enthalpy/cutoff and dielectric/PME parameter-shift scans completed 2026-08-20"
  - "FFRefine reaction-field dielectric full-gradient campaign 20260821-124443"
---

# Average-Observable Signal vs Replay Support

## Tension

Larger parameter perturbations can produce an easier-to-measure enthalpy or dielectric response, but the same perturbations can destroy overlap with the fixed archive. Smaller perturbations preserve replay support while leaving the observable displacement below sampling uncertainty. [SRC-0018] [SRC-0023]

## Evidence

In the FFRefine 20 ns scans, the best support- and KL-valid SNRs were 0.1121 for enthalpy and 0.08847 for PME dielectric. Much larger raw signals appeared for oxygen-sigma changes, including SNR 19.87 for enthalpy and 22.49 for dielectric, but those proposals had KL values above 10 and failed replay support.

The later reaction-field whole-gradient campaign found a different boundary case. A full QEq-plus-bounded proposal reduced one 10 ns archive's replay loss by 2.26% with strong ESS retention, but its paired confidence interval was inconclusive and empirical KL was 0.010535 for a nominal 0.01 step. Thus a combined direction can improve the archive-local objective without yet being statistically distinguishable or safely inside a strict empirical trust region.

This is not a choice between “use a detectable step” and “use a conservative step.” A detectable but unsupported reweighting estimate is not a valid teacher signal, while a supported but unresolved estimate cannot establish a stable optimization direction.

## Interpretation

The tension should be managed by increasing independent information or changing the tested parameter basis while keeping the support criterion fixed. The next protocol pools two development replicas to estimate one direction and tests that frozen proposal on two held-out replicas, while retaining archive-specific support and KL gates. It should not be resolved by accepting an extrapolative candidate or by lowering the uncertainty threshold after observing failure. SRC-0018's frozen-reference workflow makes support and resimulation part of optimization validity, not optional diagnostics. [SRC-0018]

## Links

- [[wiki/answers/ffrefine-average-observable-trainability-validation]]
- [[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]
- [[wiki/claims/CLM-0038-fixed-archive-gradient-validation-does-not-establish-fresh-archive-trainability]]
- [[wiki/questions/QST-0006-average-observable-trainability-sampling-budget]]
- [[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]
- [[wiki/sources/SRC-0023-statistically-optimal-analysis-multiple-equilibrium-states-mbar]]
