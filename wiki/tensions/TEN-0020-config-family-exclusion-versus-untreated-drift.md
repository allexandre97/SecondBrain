---
type: tension
status: active
created: 2026-09-24
updated: 2026-10-05
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
  - "[[wiki/answers/ffrefine-direction-gates-and-production-policy]]"
  - "[[wiki/questions/QST-0011-config-versus-weighted-sum-under-calibrated-direction-gates]]"
  - "[[wiki/answers/ffrefine-config-vs-weighted-sum-water-campaign-results]]"
  - "[[wiki/questions/QST-0015-rdf-density-dielectric-pareto-front-for-this-water-parameterisation]]"
related_claims:
  - "[[wiki/claims/CLM-0044-config-must-exclude-directionally-unreliable-families]]"
  - "[[wiki/claims/CLM-0050-retesting-a-failed-gate-after-extension-needs-alpha-spending]]"
related_questions:
  - "[[wiki/questions/QST-0011-config-versus-weighted-sum-under-calibrated-direction-gates]]"
  - "[[wiki/questions/QST-0015-rdf-density-dielectric-pareto-front-for-this-water-parameterisation]]"
sources:
  - SRC-0036
sensitivity: public
encryption: none
project_evidence:
  - "FFRefine run water_rdf-dens-diel_aggressive, epoch 5, observed 2026-09-24: density family excluded scenario reconstructed from its :uncertain/:negligible reliability classification and collapsing raw gradient norm"
  - "FFRefine water run 20260924-204914, epochs 13 and 20, observed through the `improved-gates` design analysis: density excluded from ConFIG, then pushed uphill quadratically by the remaining families' steps across the epoch's proposals (+0.02, +0.06, +0.13, +0.22, ..., +0.58 at epoch 13; comparable pattern at epoch 20), each accurately predicted by replay (+0.58 predicted vs +0.57 realised at epoch 13; +0.43 vs +0.37 at epoch 20), then recovered on return the following epoch (-0.49 and -0.35 respectively)"
  - "FFRefine water runs 20260930-132911 (weighted sum) and 20260930-132851 (ConFIG), snapshot taken 2026-10-04 (weighted sum 23 epochs, ConFIG 27 epochs; both runs ongoing): ConFIG excluded dielectric in 16 of 27 epochs (13 :descent_not_confident, 3 :uncertain), with a 4-consecutive-epoch exclusion at checkpoints 23-26 (promise t 0.55-1.1, whitened dielectric-density and dielectric-rdf gradient cosines -0.17 to -0.77); predicted versus realised chain changes over those 4 epochs: full objective +0.91 predicted vs +1.60 realised, dielectric +0.97 predicted vs +1.92 realised; persistent-exclusion warning suggested production growing 160 to 592 ns across the sequence"
  - "2026-10-05 update: weighted sum ended at checkpoint 26 (OOM crash at epoch 27) with density excluded for 5 consecutive epochs at a genuine (noise-level) constrained optimum, not a conflict; ConFIG continued to checkpoint 33 with density and dielectric seesawing (density excluded :uncertain at epochs 28, 31 with chains predicting full-objective rises of 1.4-1.6 that ran anyway; dielectric excluded at epochs 29, 30, 32, 33 with promise t reaching -3.04), all three families now pairwise conflicting (whitened rdf-density cosine -0.31 to -0.77, newly negative), fresh total loss rising from a best of 1.82 to 5.05 by checkpoint 32"
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

**Superseded description (as of 2026-10-01).** The paragraph below describes the 2026-09-24/28 state with the legacy reliability multiplier. Current mitigation is described in the 2026-10-01 section further down.

FFRefine records per-epoch exclusion streaks per family so cycling (excluded, drifting, resolved, re-included, excluded again) is visible in the optimisation history, without yet applying hysteresis to the exclusion decision itself. `required_families` and `min_eligible_families` settings exist as explicit controls: they can require a specific family to always participate, or require a minimum number of eligible families before a proposal is attempted, but neither has been campaign-calibrated. A `partial_ready` checkpoint state allows an epoch to proceed when at least one family remains eligible after exclusion, which is itself part of the tension: a partial step is a real trade-off between "some progress now" and "progress on every currently active family."

## Evidence that the predicted cycle occurs, and the project's response

A 22-epoch water run (`20260924-204914`; rdf, density, dielectric under family-level ConFIG) shows the exact cycle this tension anticipated. At epoch 13, density had been excluded as near its constrained optimum; with no signal of its own, it was pushed uphill quadratically by the other families' steps across the chain's eight proposals (+0.02, +0.06, +0.13, +0.22, ..., +0.58), then recovered by -0.49 once re-included the following epoch. A comparable pattern occurred at epoch 20 (+0.43 pushed uphill, then -0.35 recovered). In both cases the replay chain's own prediction of the uphill push was accurate against fresh resimulation (+0.58 predicted vs +0.57 realised at epoch 13; +0.43 vs +0.37 at epoch 20), so the cycle is not itself evidence of a replay-calibration failure; see [[wiki/answers/ffrefine-improved-gates-water-run-lessons]].

Given this evidence, the project's explicit decision is **not to guard against exclusion cycling**: it is treated as an accepted consequence of exclusion-based ConFIG, left "out until re-evaluated," rather than something a gate should prevent. Instead, the per-family exclusion-cycle count and its associated fresh-loss cost (the rise while excluded and the recovery after return) are recorded as a **comparison metric between aggregation methods**: weighted sum keeps a near-optimum family's small restoring gradient in the objective throughout, so it is expected to cycle less than ConFIG, which excludes the family outright whenever its direction is not confidently resolved. This reframes the tension from an unresolved risk needing a fix into a measured, monitored trade-off whose size is one of the intended outputs of a future ConFIG-versus-weighted-sum campaign.

## 2026-10-01 update: calibrated gates, rescue extensions and new evidence

FFRefine now selects families with calibrated, cross-fitted direction gates and pairs exclusion with an extend-or-exclude production policy ([[wiki/answers/ffrefine-direction-gates-and-production-policy]]). The current mitigations of this tension are: a single **rescue extension** of the current archive when its expected value is positive, with the exclusion cost set to the family's full-objective loss share (1 when nothing can be optimised without it) and the retest corrected for optional stopping ([[wiki/claims/CLM-0050-retesting-a-failed-gate-after-extension-needs-alpha-spending]]); a report-only **persistent-exclusion warning** for families excluded for noise in at least 3 of the last 5 epochs with a material loss share, suggesting a longer production time; and, under weighted sum, keeping families unless they prevent confident descent of the total.

New evidence sharpens the tension:

- **A failed gate cannot tell "no descent" from "not enough data", and fresh archives do not accumulate evidence.** Each checkpoint starts a fresh archive of the same length, so a family whose true statistic sits near its threshold keeps flipping in and out; only an extension within a checkpoint adds data at fixed parameters. In shadow run `20260928-220040` the dielectric family (40–60% of the loss) was excluded in 5 of 11 epochs, never more than two in a row.
- **Exclusion cost is mostly forgone progress.** In that shadow run, the excluded family rose only 0.03–0.18 while out, but total progress in the two epochs without it was −0.23 and −0.16 against −0.44 to −0.79 in neighbouring epochs that included it; the design analysis put the forgone progress at about 60–90% of an epoch's progress — at or above its loss share, which is why the loss share is used as a conservative exclusion cost.
- **The policy can rationally decline to rescue a heavy family.** In the ConFIG campaign `20260930-132851` (provisional, 6 epochs), dielectric held 57–65% of the loss but was excluded in 4 of 6 epochs with promise $t$ well below threshold; every rescue had negative expected value, and the persistent-exclusion warning suggested roughly 4x longer production. The weighted-sum campaign `20260930-132911` excluded nothing in the same 6 epochs. See [[wiki/questions/QST-0011-config-versus-weighted-sum-under-calibrated-direction-gates]].

## 2026-10-04 update: campaign snapshot shows a conflict-driven cycle that contradicts the "no guard" decision

Both deciding campaigns referenced in the 2026-10-01 update are still running; the evidence below is a snapshot taken 2026-10-04: weighted sum (`20260930-132911`, 23 epochs, 90.8 h) and ConFIG (`20260930-132851`, 27 epochs, 92.3 h), same ten-parameter water model and rdf/density/dielectric family weights (1/2/10). Full comparison in [[wiki/answers/ffrefine-config-vs-weighted-sum-water-campaign-results]].

**Exclusion was frequent and shown to be conflict-driven, not noise-driven.** ConFIG excluded dielectric in 16 of 27 epochs (13 `:descent_not_confident`, 3 `:uncertain`): epochs 2, 3, 5, 6, 8, 10, 11, 14, 15, 18, 19, 20, 23, 24, 25, 26. Before checkpoint 23 the longest run was three epochs in a row (18-20), not one or two; checkpoints 23-26 then excluded it for four epochs in a row. (Epoch 27's dielectric exclusion was rescued and the family was included, so it is not among the 16.) Weighted sum kept every family until density was excluded (`:degrades_total`, at density's own constrained optimum) from epoch 23 onward, including epoch 24, which was still in progress at this snapshot. Whitened inter-family gradient cosines were measured directly across both runs: density-dielectric ran -0.17 to -0.54 throughout; rdf-dielectric moved from about +0.4 early to -0.47, -0.51, -0.77 late. With all three families included, ConFIG's equal-angle step sat 75-80 degrees from dielectric's own gradient while dielectric's cross-fitted promise $t$ fell to 0.55-1.1 as its loss grew; when density was excluded for its own reasons (epochs 9 and 12), dielectric's promise passed easily ($t$ 5.3, 3.2) — the same family's gradient signal did not change, but the conflict it sat inside did. ConFIG's removal rule (drop the single least-confident family) always removed dielectric — the family carrying up to 0.8 of the loss — rather than a lower-share family that was conflicting with it. This sharpens [[wiki/claims/CLM-0044-config-must-exclude-directionally-unreliable-families]]'s mechanism with a case where the "unreliability" driving exclusion is a genuine between-family gradient conflict, not merely the excluded family's own estimation noise.

A shadow evaluation (each run's gates, replayed report-only on the other run's archives) confirmed this is not specific to one trajectory: ConFIG's gates on the weighted-sum archives also excluded dielectric about half the time, while weighted sum used dielectric's gradient productively there (loss 5.1 -> 0.04, unbiased replay predictions); weighted sum's gates on the ConFIG archives kept nearly everything, with steps at 90-143 degrees from some family — i.e. deliberately trading that family off rather than missing a conflict. Early exclusion cost (ConFIG epochs 2-14) was about 75% of an epoch's progress (-0.81 per epoch with dielectric included versus -0.19 without), at or above dielectric's 50-65% loss share there, sharpening the shadow-run's 60-90% estimate above.

**The late four-epoch exclusion reproduced the predicted drift at a scale the "no guard" decision did not anticipate.** Replay's own chain-by-chain prediction for the four excluded-dielectric chains (checkpoints 23-26) agreed in direction but not magnitude: it called a full-objective rise of 0.91 (dielectric alone +0.97); the realised rise was 1.60 (dielectric alone +1.92, about twice the predicted size). Nothing acted on this: the loss gates are diagnostic by default, and even an enforced loss gate scores only the included families, not the excluded family's drift. A separate, per-epoch paired test comparing each new checkpoint's fresh total loss against its parent checkpoint's fresh total loss (both fresh, not replay-predicted) called three of the four epochs "inconclusive" (+0.15, +0.25, +0.42); only the fourth (+0.78 +/- 0.27) was rejected — a slow, monotone multi-epoch regression escaped a sequence of individually well-calibrated per-epoch fresh-versus-fresh tests, even though replay's own chain-level prediction had already flagged the direction of the rise, if not its full size.

This **contradicts the decision recorded above not to guard against exclusion cycling**, which rested on a run where exclusions lasted at most two epochs with full recovery on return. Here the exclusion lasted four epochs, grew less confident as the family's own loss grew rather than recovering, and at this snapshot dielectric was worse than its best observed value (the run is still in progress, so this is not necessarily its final state). The persistent-exclusion warning's suggested production time grew from about 160 to 592 ns across these epochs as dielectric's $z$ fell — sound advice for a noise-limited family, but specifically wrong for a conflict-limited one: more data narrows the family's own standard error without resolving the conflict with rdf and density that is suppressing its promise statistic. The warning cannot currently distinguish the two cases.

Untested candidate remedies: gate on replay's predicted full objective including excluded families, not only the included set; cap the chain's archive KL when a heavy family is excluded; a conflict-aware removal rule (among removal choices that let every remaining family pass, keep the set with the largest total included loss share, rather than always dropping the lowest-$t$ family); or fall back to weighted-sum aggregation for the chain when ConFIG's removal would drop a high-loss-share family.

A single rescue extension occurred in roughly 50 epochs across both campaigns so far (ConFIG epoch 27: dielectric's promise $t=2.18$, having failed `:descent_not_confident`, against threshold 2.26, loss share 0.80; measured $\kappa^*=1.44$, predicted post-rescue $t=2.62$ versus realised 2.67, passing the look-1 threshold of 2.53) — the first production exercise of [[wiki/claims/CLM-0050-retesting-a-failed-gate-after-extension-needs-alpha-spending]]'s alpha-spending machinery, but a single data point.

Whether rdf, density thermal expansion, and dielectric sit on a genuine trade-off surface for this parameterisation, with each aggregation walking it in a different direction (weighted sum toward dielectric then density; ConFIG toward rdf), is inference, not established; see [[wiki/questions/QST-0015-rdf-density-dielectric-pareto-front-for-this-water-parameterisation]].

## 2026-10-05 update: a net-ascending cycle under ConFIG, and a crash ends weighted sum's comparison data

Weighted sum (`20260930-132911`) is no longer running: its epoch-27 worker was killed by an out-of-memory condition before any epoch-27 chain ran; its last completed checkpoint is 26. For weighted sum, density's five-epoch exclusion (checkpoints 23-27) looks noise/optimum-driven rather than conflict-driven: its own size statistic stayed at noise level ($z$ 1.2-1.9) and its per-family loss stayed flat, consistent with the family having genuinely reached a constrained optimum. This is the contrasting case this tension's "do not silently stop training a family" position warned about: a family can be excluded for many consecutive epochs for an entirely benign reason, and the persistent-exclusion warning's "more production time" prescription is plausibly appropriate here (unlike the conflict-driven dielectric case below).

ConFIG (`20260930-132851`), still running through checkpoint 33 (epoch 34 in progress), now shows a qualitatively different and more severe version of this tension. Density and dielectric began seesawing: density was excluded `:uncertain` at epochs 28 and 31 (its own size statistic near its optimum, $z$ 1.4 and 0.46), and both of those chains ran despite replay's own prediction of a full-objective rise of about 1.4-1.6 (density alone predicted +2.14 and +2.27, realised +1.32 and +1.70) — the loss gates are diagnostic and score only the included families, so nothing stopped either chain. Density then returned each time with an easy promise test ($t$ 37-41, reflecting how far it had been pushed), while dielectric's own promise fell, reaching $t=-3.04$ at epoch 29 (and 0.48, 0.89, -1.04 at epochs 32-34); dielectric was itself excluded at epochs 29, 30, 32 and 33, with dielectric-excluded chains raising dielectric by +1.03 and +1.34. **All three families are now pairwise conflicting** (whitened rdf-density cosine, previously mildly positive, turned to -0.31 to -0.77 over epochs 29-34; rdf-dielectric and density-dielectric remain negative as before). Fresh total loss rose from its best of 1.82 (checkpoint 22) through a seesaw to 5.05 by checkpoint 32, with three of the six checkpoint-to-checkpoint transitions in that window being statistically confident rises (not merely "inconclusive" drift as in the first regression), all report-only.

**INFERENCE, explicitly a judgement call and not a measured or established result:** under the current policy this ConFIG run is unlikely to recover. What this tension's "Current mitigation" section above described as an accepted, bounded sawtooth around a descending trend has become, once every family conflicts with every other, a cycle with net ascent. This does not prove that a full-objective guard is necessary, but it substantially strengthens the case for one, since the alternative — continuing to treat multi-family conflict cycling the same as the earlier single-family, noise-driven cycling — has now coincided with sustained regression in this run. Full numbers in [[wiki/answers/ffrefine-config-vs-weighted-sum-water-campaign-results]].

## Resolution status

Active, and sharper than before. The predicted exclude/drift/recover cycle is now confirmed in three distinct regimes: a short, noise-limited cycle (one to two epochs, full recovery on return — the 2026-09-24 run and the 2026-09-28 shadow run), which the project still treats as an accepted, tracked trade-off; a longer single-family, conflict-driven cycle (four consecutive epochs, incomplete recovery, growing less confident rather than more — ConFIG checkpoints 23-26 of the 2026-09-30 campaign), which contradicts the decision recorded above not to guard against cycling; and, as of the 2026-10-05 update, a multi-family, net-ascending cycle once every family conflicts with every other (ConFIG checkpoints 27-33), which the project has not previously characterised at all. Weighted sum's own exclusion (density, checkpoints 23-27) remains in the first, benign regime, and its run ended on an unrelated infrastructure failure (an out-of-memory crash), not on any version of this tension. Candidate remedies for the conflict-driven and net-ascending cases are recorded but untested. Whether ConFIG's higher exclusion rate is worth its protection against collapsing the aggregate step ([[wiki/claims/CLM-0044-config-must-exclude-directionally-unreliable-families]]) remains open, and the 2026-10-05 evidence leans further toward "no" for this specific campaign; see [[wiki/questions/QST-0011-config-versus-weighted-sum-under-calibrated-direction-gates]] and [[wiki/answers/ffrefine-config-vs-weighted-sum-water-campaign-results]] for the latest comparison.

## Links

- [[wiki/answers/adding-config-optimiser-to-ffrefine]]
- [[wiki/claims/CLM-0044-config-must-exclude-directionally-unreliable-families]]
- [[wiki/concepts/awh-replay-force-field-optimization]]
- [[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]
- [[wiki/sources/SRC-0036-config-towards-conflict-free-training-of-physics-informed]]
- [[wiki/answers/ffrefine-improved-gates-water-run-lessons]]
- [[wiki/answers/ffrefine-direction-gates-and-production-policy]]
- [[wiki/questions/QST-0011-config-versus-weighted-sum-under-calibrated-direction-gates]]
- [[wiki/answers/ffrefine-config-vs-weighted-sum-water-campaign-results]]
- [[wiki/questions/QST-0015-rdf-density-dielectric-pareto-front-for-this-water-parameterisation]]
