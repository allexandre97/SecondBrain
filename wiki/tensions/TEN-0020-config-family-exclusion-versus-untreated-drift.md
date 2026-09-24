---
type: tension
status: active
created: 2026-09-24
updated: 2026-09-24
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
related_claims:
  - "[[wiki/claims/CLM-0044-config-must-exclude-directionally-unreliable-families]]"
sources:
  - SRC-0036
sensitivity: public
encryption: none
project_evidence:
  - "FFRefine run water_rdf-dens-diel_aggressive, epoch 5, observed 2026-09-24: density family excluded scenario reconstructed from its :uncertain/:negligible reliability classification and collapsing raw gradient norm"
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

## Resolution status

Active and unresolved. The exclusion policy is evidenced by one water multi-family run and one synthetic unit test; no campaign has yet measured whether excluded high-loss families recover on their own, drift further from target, or oscillate in and out of the aggregate over many epochs.

## Links

- [[wiki/answers/adding-config-optimiser-to-ffrefine]]
- [[wiki/claims/CLM-0044-config-must-exclude-directionally-unreliable-families]]
- [[wiki/concepts/awh-replay-force-field-optimization]]
- [[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]
- [[wiki/sources/SRC-0036-config-towards-conflict-free-training-of-physics-informed]]
