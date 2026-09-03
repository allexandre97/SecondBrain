---
type: claim
status: active
created: 2026-08-20
updated: 2026-09-03
claim_status: supported
claim_scope: local
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/molecular-simulation/free-energy
  - research/scientific-computing
tags:
  - claim
  - ffrefine
  - gradient-validation
  - fresh-archive-validation
  - trainability
related:
  - "[[wiki/answers/ffrefine-prospective-dielectric-damped-fisher-training]]"
  - "[[wiki/questions/QST-0007-checkpoint-assessment-versus-next-direction-readiness]]"
  - "[[wiki/answers/ffrefine-retrospective-fisher-treatment-development]]"
  - "[[wiki/answers/ffrefine-long-archive-target-gradient-convergence]]"
  - "[[wiki/answers/ffrefine-average-observable-trainability-validation]]"
  - "[[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]"
  - "[[wiki/questions/QST-0006-average-observable-trainability-sampling-budget]]"
  - "[[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]"
sources:
  - SRC-0018
  - SRC-0023
sensitivity: public
encryption: none
project_evidence:
  - "FFRefine fixed-archive and fresh-archive water average-observable checks, 2026-08-15 through 2026-08-20"
  - "FFRefine cross-observable reaction-field target/Fisher reproducibility run 20260822-204246"
  - "FFRefine two-independent-100ns reaction-field target-gradient convergence comparison completed 2026-08-26"
  - "FFRefine retrospective Fisher-treatment screen and paired cross-archive replay completed 2026-08-28"
  - "FFRefine state-conditional Fisher-treatment screen and replay completed 2026-08-30 through 2026-08-31"
  - "FFRefine dielectric-only damped-Fisher reaction-field water-temperature run 20260901-171027, completed 2026-09-02"
  - "FFRefine higher-KL dielectric-only damped-Fisher reaction-field water-temperature run 20260902-115818, intentionally stopped during epoch 8 on 2026-09-03 after six paired-confirmed fresh updates"
---

# Fixed-Archive Gradient Validation Does Not Establish Fresh-Archive Trainability

## Claim

Passing value, finite-difference-gradient, loss-gradient, and synthetic recovery checks on one fixed replay archive does not establish that a fresh production archive contains a statistically resolvable, replay-supported training direction. [SRC-0018] [SRC-0023]

## Scope

This is a local FFRefine validation claim supported by the August 2026 water enthalpy and PME dielectric checks. It generalizes only to the validation distinction, not to a claim that all ensemble-average observables are hard to train.

## Evidence

- Fixed-archive enthalpy and PME dielectric checks obtained near-unit gradient cosines, relative gradient errors below $6\times10^{-4}$, large synthetic loss reduction, and accurate teacher-parameter recovery.
- Fresh 10 ns and 20 ns archives subsequently produced no candidate among 36 tested shifts that met SNR at least 5, replay support, and KL at most 0.02.
- SRC-0018 requires accepted replay updates to survive resimulation; replay support and archive-local correctness are therefore necessary but not sufficient for robust force-field improvement. [SRC-0018]
- MBAR combines information from sampled configurations but cannot create missing phase-space support or independent information. [SRC-0023]
- In the matched cross-observable reaction-field run `20260822-204246`, density and RDF directions reproduced while enthalpy and dielectric directions did not. The retained Fisher subspaces were nearly identical, and common-gradient counterfactuals were stable across Fishers, localizing the disagreement to observable-gradient estimation rather than a pipeline-wide Fisher failure.
- Independent enthalpy and dielectric proposals improved their source archive but worsened the other archive. Density and RDF proposals improved both. This directly demonstrates that archive-local descent is not sufficient evidence of a population descent direction.
- Dielectric target-value splits passed in all four individual trajectories while dielectric half-gradients failed in all four. Mean-observable stability therefore did not establish gradient stability in this realization.
- In two later independent 100 ns reaction-field archives, direct target disagreement was small for every family, yet direction convergence remained target dependent. Dielectric became continuously reproducible from 60 through 100 ns, whereas enthalpy's raw-gradient cosine reached 0.9691 but its full-Fisher natural-direction cosine remained 0.6288. Fixed-archive correctness therefore did not predict either the sampling time required for dielectric or the preconditioned enthalpy failure. [[wiki/answers/ffrefine-long-archive-target-gradient-convergence]]
- Retrospective finite-step replay on those same archives found supported bidirectional dielectric descent for the production hard Fisher and small-$\gamma$ damping, with paired intervals below zero. Small-$\gamma$ enthalpy damping also gave paired-resolved bidirectional cross-archive descent despite failing the exact-direction gate. This strengthens fixed-archive evidence without testing a prospectively frozen treatment on new archives or by fresh candidate simulation. [[wiki/answers/ffrefine-retrospective-fisher-treatment-development]]
- The later prospective dielectric run supplies the positive complement to the claim. Once $\gamma=0.1$ damping and the conditional-KL policy were frozen, two consecutive updates reduced loss on the next fresh macro archive and the best checkpoint reproduced in two final-validation simulations. This establishes trainability only because the fixed-archive proposal was followed by fresh evidence. [[wiki/answers/ffrefine-prospective-dielectric-damped-fisher-training]]
- The same prospective run's fourth archive passed direct dielectric splitting but failed treated-direction agreement. A successful earlier update and a stable current mean did not guarantee that the next fresh archive contained a reproducible direction.
- The higher-KL prospective run supplies a stronger positive complement. Checkpoints 1 through 6 all reduced paired loss on the next fresh archive, with every recorded interval below zero; fresh loss fell 50.90% from checkpoint 0 to checkpoint 6. The claim is supported precisely because six separate archive-local proposals were followed by new sampling and paired parent comparisons. [[wiki/claims/CLM-0040-damped-conditional-fisher-dielectric-training-survives-fresh-resimulation]]

## Caveats

- The fresh scans tested six bounded coordinate directions and positive shifts only.
- Failure to identify a direction at 20 ns does not prove that longer or replicated sampling will fail.
- Pooling produced a near-threshold dielectric direction and favorable cross-arm point responses, so the new result does not establish fundamental untrainability. It establishes insufficient reproducibility at the tested individual-trajectory budget and default Fisher floor.
- The cross-observable result is one campaign seed and lacks paired uncertainty for its replay-probe loss changes.
- This claim does not invalidate fixed-archive tests; those tests isolate mathematical correctness and are a necessary validation layer.
- Longer sampling can recover an independently reproducible direction for a particular target and archive pair. That observation narrows the budget question but does not retrospectively turn fixed-archive validation into evidence of fresh-archive trainability.
- Cross-replaying archive-A and archive-B proposals is stronger than source-archive replay, but treatment selection on the same pair leaves method-selection uncertainty unmeasured.
- Paired delete-block intervals below zero establish conditional replay descent, not between-campaign repeatability or recovery after resimulation.
- Fresh confirmation of two dielectric updates does not invalidate the claim; it demonstrates the additional evidence needed to move from fixed-archive plausibility to local trainability.
- Six consecutive fresh confirmations strengthen the local trainability conclusion but still do not turn a fixed-archive check into prospective evidence or establish a campaign-level success rate.

## Links

- [[wiki/answers/ffrefine-prospective-dielectric-damped-fisher-training]]
- [[wiki/answers/ffrefine-retrospective-fisher-treatment-development]]
- [[wiki/answers/ffrefine-average-observable-trainability-validation]]
- [[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]
- [[wiki/questions/QST-0006-average-observable-trainability-sampling-budget]]
- [[wiki/questions/QST-0007-checkpoint-assessment-versus-next-direction-readiness]]
- [[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]
- [[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]
- [[wiki/sources/SRC-0023-statistically-optimal-analysis-multiple-equilibrium-states-mbar]]
