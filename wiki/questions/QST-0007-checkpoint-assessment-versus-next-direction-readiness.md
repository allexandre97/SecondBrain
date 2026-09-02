---
type: question
status: active
created: 2026-09-02
updated: 2026-09-02
question_status: partially-answered
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

## Proposed state model

| State | Base observable/replay validity | Paired parent comparison | Selected direction | Consequence |
| --- | --- | --- | --- | --- |
| invalid evaluation | fail | not trusted | not evaluated or irrelevant | extend or reject archive |
| valid evaluation, parent rejected | pass | worsening resolved | any | roll back candidate |
| valid evaluation, direction unresolved | pass | accepted or baseline | fail/inconclusive | update best checkpoint if warranted; do not optimize |
| optimization ready | pass | accepted or baseline | pass | construct next replay proposal |
| final validation accepted | pass | optional | reporter only | retain objective estimate |

This proposal preserves conservative direction gating without discarding valid information about an already simulated checkpoint.

## Remaining uncertainty

- Which base diagnostics are strictly required for objective evaluation versus gradient construction should be made explicit for every FFRefine setup.
- A paired comparison can still be inconclusive even when its point loss improves; this needs a separate extension/termination rule.
- If a direction fails after the candidate is accepted, the best policy among longer continuation, more independent replicas, or stopping remains target and cost dependent.
- The proposed separation has not yet been implemented and tested on a prospective rerun.

## Links

- [[wiki/answers/ffrefine-prospective-dielectric-damped-fisher-training]]
- [[wiki/answers/ffrefine-average-observable-trainability-validation]]
- [[wiki/claims/CLM-0038-fixed-archive-gradient-validation-does-not-establish-fresh-archive-trainability]]
- [[wiki/questions/QST-0006-average-observable-trainability-sampling-budget]]
- [[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]
- [[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]
- [[wiki/sources/SRC-0023-statistically-optimal-analysis-multiple-equilibrium-states-mbar]]
