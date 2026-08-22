---
type: tension
status: active
created: 2026-08-20
updated: 2026-08-22
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
  - "FFRefine cross-fitted reaction-field dielectric direction run 20260821-151000"
  - "FFRefine reaction-field dielectric replica comparison run 20260821-190105"
---

# Average-Observable Signal vs Replay Support

## Tension

Larger parameter perturbations can produce an easier-to-measure enthalpy or dielectric response, but the same perturbations can destroy overlap with the fixed archive. Smaller perturbations preserve replay support while leaving the observable displacement below sampling uncertainty. [SRC-0018] [SRC-0023]

## Evidence

In the FFRefine 20 ns scans, the best support- and KL-valid SNRs were 0.1121 for enthalpy and 0.08847 for PME dielectric. Much larger raw signals appeared for oxygen-sigma changes, including SNR 19.87 for enthalpy and 22.49 for dielectric, but those proposals had KL values above 10 and failed replay support.

The later reaction-field whole-gradient campaign found a different boundary case. A full QEq-plus-bounded proposal reduced one 10 ns archive's replay loss by 2.26% with strong ESS retention, but its paired confidence interval was inconclusive and empirical KL was 0.010535 for a nominal 0.01 step. Thus a combined direction can improve the archive-local objective without yet being statistically distinguishable or safely inside a strict empirical trust region.

The four-archive cross-fitted repetition substantially narrowed this tension. The frozen candidate reduced replay loss on all four archives by 2.36–3.12%; pooled development and held-out improvements were 2.722% and 2.718%. Both pooled confidence intervals excluded zero, development/held-out Fisher-metric direction cosine was 0.9325, and norm ratio was 0.9975. Replay support remained strong. The formal failure came from one empirical KL of 0.010215 against a 0.01 ceiling and from confidence bounds that established positive improvement but not an improvement of at least 1%.

The corrected replica comparison run `20260821-190105` did not reproduce that coherence. At matched aggregate production cost, two 5 ns replicas gave development/held-out direction cosine -0.072 and a held-out loss increase of 0.29%. Two 10 ns replicas doubled aggregate production, passed every empirical-KL check, roughly doubled local ESS, and improved chronological gradient stability to three of four archives, but direction cosine remained only 0.287 and the held-out point improvement was 0.52% with an interval crossing zero. Within-archive replica direction cosines remained poor in both variants.

This adds a second tension: conventional support and time-split diagnostics can improve while the force-field direction remains replica dependent. Every replica covered the complete thermodynamic ladder, so thermodynamic-state coverage did not guarantee equilibration of the dipole-fluctuation modes controlling dielectric response.

This is not a choice between “use a detectable step” and “use a conservative step.” A detectable but unsupported reweighting estimate is not a valid teacher signal, while a supported but unresolved estimate cannot establish a stable optimization direction.

## Interpretation

The tension should be managed by increasing genuinely independent information or changing the tested parameter basis while keeping the support criterion fixed. One run showed that pooling independent archives and Fisher projection can expose a coherent direction even when individual chronological halves are unstable; the replica comparison showed that this coherence is not yet reproducible. Replicas sharing one TSS preparation must not be counted as equivalent to independently prepared archives for direction uncertainty. Near-boundary empirical KL should cause controlled line-search shrinkage, while confidence in the sign of improvement remains distinct from confidence that a minimum effect size was exceeded. SRC-0018's frozen-reference workflow makes support and resimulation part of optimization validity, not optional diagnostics. [SRC-0018]

## Links

- [[wiki/answers/ffrefine-average-observable-trainability-validation]]
- [[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]
- [[wiki/claims/CLM-0038-fixed-archive-gradient-validation-does-not-establish-fresh-archive-trainability]]
- [[wiki/questions/QST-0006-average-observable-trainability-sampling-budget]]
- [[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]
- [[wiki/sources/SRC-0023-statistically-optimal-analysis-multiple-equilibrium-states-mbar]]
