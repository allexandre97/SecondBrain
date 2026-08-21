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
---

# Average-Observable Trainability Sampling Budget

## Question

What archive length, number of independent replicas, uncertainty estimator, and parameter-direction basis are required before FFRefine can identify a five-standard-error enthalpy or dielectric teacher signal without leaving replay support or the KL trust region?

## Context

Controlled fixed-archive checks validate the implemented enthalpy and PME dielectric mathematics, but fresh 10 ns and 20 ns scans found no eligible direction among the tested coordinate shifts. The best support- and KL-valid SNR was 0.1121 for enthalpy and 0.08847 for PME dielectric at 20 ns, versus the required SNR of 5. [[wiki/answers/ffrefine-average-observable-trainability-validation]]

Reweighting methods require sampled support for the candidate distribution, and fresh resimulation is required before an archive-local improvement is treated as robust. [SRC-0018] [SRC-0023]

## Current position

Twenty nanoseconds in one sequentially extended archive is insufficient under the tested settings. A subsequent reaction-field campaign tested the production optimizer's complete QEq-plus-bounded-parameter gradient. Its first 10 ns archive produced a supported 2.26% replay-loss reduction, but paired confidence was inconclusive and empirical KL was 0.010535 for a nominal 0.01 step. After extension, both 20 ns archives were `sampling_limited`; the old output did not retain the exact failing subgate. This shows that a combined local response can exist, but does not establish a stable or independently reproducible direction.

The next experiment uses two independent 10 ns development archives to estimate one pooled full-gradient proposal and two separate independent 10 ns held-out archives to test that fixed proposal. It scales to estimated KL 0.009, applies a hard empirical ceiling of 0.01 to every archive, combines paired confidence with within- and between-archive variance, and requires development/held-out Fisher-metric direction agreement. If this is inconclusive, the next comparison should hold total cost fixed while contrasting more independent replicas with longer replicas.

## Validation boundaries

- Do not weaken SNR or support thresholds merely to produce an eligible candidate.
- Do not infer $1/\sqrt{t}$ error scaling from one sequential extension.
- Coordinate-wise positive shifts may miss a supported combined direction, but changing the direction basis creates a new experiment.
- Pooling development archives must not leak candidate selection into the held-out archives; the proposed parameter vector is frozen before held-out replay.
- PME dielectric and cutoff/reaction-field enthalpy results do not isolate electrostatics dependence.
- A candidate that passes the replay prescreen still requires independent teacher archives and fresh macro-recovery validation. [SRC-0018]

## Links

- [[wiki/answers/ffrefine-average-observable-trainability-validation]]
- [[wiki/claims/CLM-0038-fixed-archive-gradient-validation-does-not-establish-fresh-archive-trainability]]
- [[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]
- [[wiki/questions/force-field-training-validation-scope]]
- [[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]
