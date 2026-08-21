---
type: question
status: active
created: 2026-08-20
updated: 2026-08-21
question_status: open
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/molecular-simulation/free-energy
  - research/statistics/monte-carlo
tags:
  - question
  - ffrefine
  - enthalpy
  - dielectric-constant
  - sampling-budget
  - trainability
related:
  - "[[wiki/answers/ffrefine-average-observable-trainability-validation]]"
  - "[[wiki/claims/CLM-0038-fixed-archive-gradient-validation-does-not-establish-fresh-archive-trainability]]"
  - "[[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]"
  - "[[wiki/questions/force-field-training-validation-scope]]"
sources:
  - SRC-0018
  - SRC-0023
sensitivity: public
encryption: none
project_evidence:
  - "FFRefine fresh-archive enthalpy/cutoff and dielectric/PME trainability runs completed 2026-08-20"
  - "FFRefine reaction-field dielectric full-gradient campaign 20260821-124443"
  - "FFRefine cross-fitted reaction-field dielectric direction run 20260821-151000"
---

# Average-Observable Trainability Sampling Budget

## Question

What archive length, number of independent replicas, uncertainty estimator, and parameter-direction basis are required before FFRefine can identify a five-standard-error enthalpy or dielectric teacher signal without leaving replay support or the KL trust region?

## Context

Controlled fixed-archive checks validate the implemented enthalpy and PME dielectric mathematics, but fresh 10 ns and 20 ns scans found no eligible direction among the tested coordinate shifts. The best support- and KL-valid SNR was 0.1121 for enthalpy and 0.08847 for PME dielectric at 20 ns, versus the required SNR of 5. [[wiki/answers/ffrefine-average-observable-trainability-validation]]

Reweighting methods require sampled support for the candidate distribution, and fresh resimulation is required before an archive-local improvement is treated as robust. [SRC-0018] [SRC-0023]

## Current position

Twenty nanoseconds in one sequentially extended archive was insufficient under the original settings. A subsequent reaction-field campaign tested the production optimizer's complete QEq-plus-bounded-parameter gradient. Its first 10 ns archive produced a supported 2.26% replay-loss reduction, but paired confidence was inconclusive and empirical KL was 0.010535 for a nominal 0.01 step. After extension, both 20 ns archives were `sampling_limited`; the old output did not retain the exact failing subgate.

The completed cross-fitted run `20260821-151000` then used two independent 10 ns development archives to estimate one pooled full-gradient proposal and two independent 10 ns held-out archives to test that fixed proposal. All four archive point estimates improved by 2.36–3.12%. Pooled point improvements were 2.722% in development and 2.718% held out; both confidence intervals excluded zero. The development and held-out Fisher-metric direction cosine was 0.9325 with norm ratio 0.9975. This establishes a reproducible replay direction under pooling, even though every individual archive's chronological half-gradient comparison failed.

The formal result remained `inconclusive`. One development empirical KL was 0.010215, 2.15% above the hard 0.01 ceiling, while the other three passed. The conservative lower bounds established only 0.815% and 0.236% loss improvement, below the protocol's requirement to establish at least 1%. The remaining sampling-budget question has therefore moved: the existence and sign of a pooled full-gradient replay response are supported, but the budget needed for a predefined minimum effect size and for fresh candidate simulation remains unknown.

Before repeating the experiment, empirical KL should gate line search directly, candidate target values should be persisted by temperature, and the statistical role of the 1% threshold should be declared prospectively. After that correction, compare additional replicas with longer replicas only if the cross-fitted direction remains inconclusive.

## Validation boundaries

- Do not weaken SNR or support thresholds merely to produce an eligible candidate.
- Do not infer $1/\sqrt{t}$ error scaling from one sequential extension.
- Coordinate-wise positive shifts may miss a supported combined direction, but changing the direction basis creates a new experiment.
- Pooling development archives must not leak candidate selection into the held-out archives; the proposed parameter vector is frozen before held-out replay.
- A confidence interval below zero establishes descent but does not establish that the decrease exceeds a chosen minimum effect size; those are distinct claims and need distinct gates.
- A hard empirical-KL ceiling should be enforced while selecting the line-search scale, not only after a proposal has otherwise been selected.
- PME dielectric and cutoff/reaction-field enthalpy results do not isolate electrostatics dependence.
- A candidate that passes the replay prescreen still requires independent teacher archives and fresh macro-recovery validation. [SRC-0018]

## Links

- [[wiki/answers/ffrefine-average-observable-trainability-validation]]
- [[wiki/claims/CLM-0038-fixed-archive-gradient-validation-does-not-establish-fresh-archive-trainability]]
- [[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]
- [[wiki/questions/force-field-training-validation-scope]]
- [[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]
