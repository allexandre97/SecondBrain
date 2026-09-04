---
type: question
status: active
created: 2026-09-02
updated: 2026-09-04
question_status: answered
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/molecular-simulation/free-energy
  - research/scientific-computing
tags:
  - question
  - ffrefine
  - macro-optimization
  - fresh-validation
  - direction-gate
  - checkpoint-selection
  - early-stopping
related:
  - "[[wiki/answers/ffrefine-aggressive-density-kl-ess-training]]"
  - "[[wiki/answers/ffrefine-prospective-dielectric-damped-fisher-training]]"
  - "[[wiki/answers/ffrefine-average-observable-trainability-validation]]"
  - "[[wiki/claims/CLM-0038-fixed-archive-gradient-validation-does-not-establish-fresh-archive-trainability]]"
  - "[[wiki/questions/QST-0006-average-observable-trainability-sampling-budget]]"
  - "[[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]"
sources:
  - SRC-0018
  - SRC-0023
sensitivity: public
encryption: none
project_evidence:
  - "FFRefine dielectric-only damped-Fisher reaction-field water-temperature run 20260901-171027, completed 2026-09-02"
  - "FFRefine higher-KL dielectric-only damped-Fisher reaction-field water-temperature run 20260902-115818, intentionally stopped during epoch 8 on 2026-09-03 after six paired-confirmed fresh updates"
  - "FFRefine density-only aggressive conditional-KL/ESS water-temperature run 20260904-102939, completed 2026-09-04"
---

# Checkpoint Assessment vs Next-Direction Readiness

## Question

Should FFRefine treat trustworthy evaluation of the current checkpoint and statistical readiness to construct the next parameter update as separate pipeline states?

## Context

In prospective dielectric run `20260901-171027`, checkpoint 3 was generated from an archive whose damped direction passed. It was then simulated on a fresh fourth macro-epoch archive. Replay support, effective sample size, Fisher validity, and the direct dielectric split passed, and the direct point loss was 5.6950.

The two chronological halves of that same archive produced damped directions with Fisher-metric cosine 0.657, below the predeclared 0.8 threshold. The current backend consequently classified the full epoch as sampling-limited before computing the paired checkpoint-3-versus-checkpoint-2 comparison. Checkpoint 3 was not rejected by paired evidence; it was never assessed. [[wiki/answers/ffrefine-prospective-dielectric-damped-fisher-training]]

This behavior conflates two questions with different estimators:

1. whether the current checkpoint's observable loss and paired change from its parent are trustworthy;
2. whether the current archive supplies a reproducible sensitivity direction for another update.

SRC-0018 requires archive-derived replay updates to survive resimulation, but it does not imply that the gradient of the fresh archive must converge before the already generated candidate can be evaluated. [SRC-0018] State-normalized replay and support diagnostics can evaluate a parent/candidate pair on common configurations even when the next objective-gradient direction is uncertain. [SRC-0023]

## Current position

The statuses should be separated conceptually and in recorded artifacts:

- **evaluation accepted** should require the base replay/ESS and direct-observable diagnostics needed for a trustworthy fresh loss, plus a paired parent comparison when a parent exists;
- **optimization ready** should additionally require the selected treated-direction diagnostics needed to construct another proposal.

An optimization-ready epoch is necessarily evaluation-ready, but an evaluation-ready epoch need not be optimization-ready. When only the first passes, the current checkpoint can still become the best checkpoint if its paired fresh comparison is accepted; the pipeline should then stop, extend sampling, or acquire independent information before attempting another update.

Final-validation replicas do not normally produce another update. Their scientific purpose is to estimate the selected checkpoint's fresh objective. The treated direction can remain a useful reporter in those replicas, but should not veto an otherwise valid final objective estimate.

The separation has now been implemented in the recorded checkpoint-assessment schema. Run `20260902-115818` persisted distinct `evaluation_valid`, `evaluation_accepted`, `direction_ready`, `optimisation_ready`, and `optimisation_ran` fields. In all seven completed epochs, evaluation and direction readiness passed together, and checkpoints 1 through 6 received paired fresh comparisons.

## Proposed state model

| State | Base observable/replay validity | Paired parent comparison | Selected direction | Consequence |
| --- | --- | --- | --- | --- |
| invalid evaluation | fail | not trusted | not evaluated or irrelevant | extend or reject archive |
| valid evaluation, parent rejected | pass | worsening resolved | any | roll back candidate |
| valid evaluation, direction unresolved | pass | accepted or baseline | fail/inconclusive | update best checkpoint if warranted; do not optimize |
| optimization ready | pass | accepted or baseline | pass | construct next replay proposal |
| final validation accepted | pass | optional | reporter only | retain objective estimate |

This proposal preserves conservative direction gating without discarding valid information about an already simulated checkpoint.

## Prospective branch validation

Density-only run `20260904-102939` exercised the previously missing branch. In epoch 3, checkpoint 2 passed base evaluation and its paired comparison with checkpoint 1 was accepted: candidate loss 21.5935 versus parent replay loss 66.0780, with candidate-minus-parent interval [-52.2696, -36.6993]. The selected damped direction nevertheless failed its chronological-half gate after the allowed extensions, with final cosine 0.7280 against threshold 0.8.

The recorded state was consequently `evaluation_valid=true`, `evaluation_accepted=true`, `direction_ready=false`, `optimisation_ready=false`, and `optimisation_ran=false`. Checkpoint 2 remained the best checkpoint, no uncertain next update was generated, and two final-validation replicas successfully evaluated that checkpoint at losses 20.0060 and 20.2560. This is the intended behavior and validates the control-flow separation on its decisive path. [[wiki/answers/ffrefine-aggressive-density-kl-ess-training]]

## Remaining uncertainty

- Which base diagnostics are strictly required for objective evaluation versus gradient construction should be made explicit for every FFRefine setup.
- A paired comparison can still be inconclusive even when its point loss improves; this needs a separate extension/termination rule.
- If a direction fails after the candidate is accepted, the best policy among longer continuation, more independent replicas, or stopping remains target and cost dependent.
- The state separation is now validated on both the all-pass path and one prospective evaluation-pass/direction-fail path, but that branch should still be observed across other targets and campaign seeds.

## Links

- [[wiki/answers/ffrefine-aggressive-density-kl-ess-training]]
- [[wiki/answers/ffrefine-prospective-dielectric-damped-fisher-training]]
- [[wiki/answers/ffrefine-average-observable-trainability-validation]]
- [[wiki/claims/CLM-0038-fixed-archive-gradient-validation-does-not-establish-fresh-archive-trainability]]
- [[wiki/questions/QST-0006-average-observable-trainability-sampling-budget]]
- [[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]
- [[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]
- [[wiki/sources/SRC-0023-statistically-optimal-analysis-multiple-equilibrium-states-mbar]]
