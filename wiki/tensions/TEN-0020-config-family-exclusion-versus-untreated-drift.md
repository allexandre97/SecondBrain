---
type: tension
status: active
created: 2026-09-24
updated: 2026-09-28
tension_status: active
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/machine-learning/scientific-modeling
  - research/scientific-computing
tags:
  - tension
  - ffrefine
  - config
  - gradient-conflict
  - multi-objective-optimization
  - trust-region
related:
  - "[[wiki/answers/adding-config-optimiser-to-ffrefine]]"
  - "[[wiki/claims/CLM-0044-config-must-exclude-directionally-unreliable-families]]"
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
  - "[[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]"
  - "[[wiki/answers/ffrefine-improved-gates-water-run-lessons]]"
related_claims:
  - "[[wiki/claims/CLM-0044-config-must-exclude-directionally-unreliable-families]]"
sources:
  - SRC-0036
sensitivity: public
encryption: none
project_evidence:
  - "FFRefine run water_rdf-dens-diel_aggressive, epoch 5, observed 2026-09-24: density family excluded scenario reconstructed from its :uncertain/:negligible reliability classification and collapsing raw gradient norm"
  - "FFRefine water run 20260924-204914, epochs 13 and 20, observed through the `improved-gates` design analysis: density excluded from ConFIG, then pushed uphill quadratically by the remaining families' steps across the epoch's proposals (+0.02, +0.06, +0.13, +0.22, ..., +0.58 at epoch 13; comparable pattern at epoch 20), each accurately predicted by replay (+0.58 predicted vs +0.57 realised at epoch 13; +0.43 vs +0.37 at epoch 20), then recovered on return the following epoch (-0.49 and -0.35 respectively)"
---

# ConFIG Family Exclusion vs Untreated Drift

## Tension

Excluding a directionally unreliable family from FFRefine's ConFIG aggregate direction protects the shared step from collapsing, but it also means nothing optimizes that family for the epochs in which it is excluded. A family that is marginally resolved but carries a large loss can plausibly cycle between included and excluded across epochs, or stay excluded for an extended run, while the aggregate step improves only the remaining families. [SRC-0036]

## Positions

- **Exclude unreliable directions.** [[wiki/claims/CLM-0044-config-must-exclude-directionally-unreliable-families]] shows that keeping an `:uncertain` or `:negligible` family active in ConFIG can collapse the aggregate step by more than 100x in a synthetic reproduction and produced an estimated KL of 0.0017 in a real multi-family water run. Not excluding such families sacrifices progress on every family to protect one whose signal cannot currently be trusted.
- **Do not silently stop training a family.** In the same run, the dielectric family's signal-to-standard-error ratio was near 3 against the default reliability multiplier of 2, i.e. marginally resolved. A family in that regime is a plausible candidate to flip between `:resolved` and `:uncertain` across epochs depending on archive-specific noise, which would leave it excluded from some proposals for reasons that have nothing to do with whether it needs correction. A high-loss family that is excluded more often than it is included receives systematically less optimization attention than its loss would justify.

## Why it matters

Retrieval or reasoning about FFRefine's ConFIG policy should not treat exclusion as a free safety measure. It trades aggregate-step integrity against the risk of stalling, or slowly regressing, an excluded family, especially one whose reliability classification is itself noisy from epoch to epoch. This is structurally different from [[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]], which concerns whether a *single* family's signal is large enough to be trainable at all under replay support; this tension concerns what happens to a family's training progress once it participates in a *multi-family* ConFIG aggregate and is intermittently excluded.

## Current mitigation

FFRefine records per-epoch exclusion streaks per family so cycling (excluded, drifting, resolved, re-included, excluded again) is visible in the optimisation history, without yet applying hysteresis to the exclusion decision itself. `required_families` and `min_eligible_families` settings exist as explicit controls: they can require a specific family to always participate, or require a minimum number of eligible families before a proposal is attempted, but neither has been campaign-calibrated. A `partial_ready` checkpoint state allows an epoch to proceed when at least one family remains eligible after exclusion, which is itself part of the tension: a partial step is a real trade-off between "some progress now" and "progress on every currently active family."

## Evidence that the predicted cycle occurs, and the project's response

A 22-epoch water run (`20260924-204914`; rdf, density, dielectric under family-level ConFIG) shows the exact cycle this tension anticipated. At epoch 13, density had been excluded as near its constrained optimum; with no signal of its own, it was pushed uphill quadratically by the other families' steps across the chain's eight proposals (+0.02, +0.06, +0.13, +0.22, ..., +0.58), then recovered by -0.49 once re-included the following epoch. A comparable pattern occurred at epoch 20 (+0.43 pushed uphill, then -0.35 recovered). In both cases the replay chain's own prediction of the uphill push was accurate against fresh resimulation (+0.58 predicted vs +0.57 realised at epoch 13; +0.43 vs +0.37 at epoch 20), so the cycle is not itself evidence of a replay-calibration failure; see [[wiki/answers/ffrefine-improved-gates-water-run-lessons]].

Given this evidence, the project's explicit decision is **not to guard against exclusion cycling**: it is treated as an accepted consequence of exclusion-based ConFIG, left "out until re-evaluated," rather than something a gate should prevent. Instead, the per-family exclusion-cycle count and its associated fresh-loss cost (the rise while excluded and the recovery after return) are recorded as a **comparison metric between aggregation methods**: weighted sum keeps a near-optimum family's small restoring gradient in the objective throughout, so it is expected to cycle less than ConFIG, which excludes the family outright whenever its direction is not confidently resolved. This reframes the tension from an unresolved risk needing a fix into a measured, monitored trade-off whose size is one of the intended outputs of a future ConFIG-versus-weighted-sum campaign.

## Resolution status

Active, but no longer purely unresolved for the specific cycling behavior: one 22-epoch water run confirms the predicted exclude/drift/recover cycle occurs, that replay accurately predicts the drift and recovery when it does, and the project has decided to treat cycling as a tracked, accepted trade-off rather than to gate against it. What remains open is whether ConFIG's higher expected cycling rate, relative to weighted sum, is worth its other benefits (protection against unreliable directions collapsing the aggregate step; see [[wiki/claims/CLM-0044-config-must-exclude-directionally-unreliable-families]]) — a question reserved for a future comparison campaign between the two aggregation methods.

## Links

- [[wiki/answers/adding-config-optimiser-to-ffrefine]]
- [[wiki/claims/CLM-0044-config-must-exclude-directionally-unreliable-families]]
- [[wiki/concepts/awh-replay-force-field-optimization]]
- [[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]
- [[wiki/sources/SRC-0036-config-towards-conflict-free-training-of-physics-informed]]
- [[wiki/answers/ffrefine-improved-gates-water-run-lessons]]
