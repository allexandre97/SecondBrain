---
type: question
status: active
created: 2026-10-01
updated: 2026-10-12
question_status: open
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/molecular-simulation/free-energy
  - research/scientific-computing
tags:
  - question
  - ffrefine
  - replay-reweighting
  - calibration
  - optimiser-curse
related:
  - "[[wiki/answers/ffrefine-direction-gates-and-production-policy]]"
  - "[[wiki/answers/ffrefine-improved-gates-water-run-lessons]]"
  - "[[wiki/answers/ffrefine-loss-gate-diagnostic-policy]]"
  - "[[wiki/questions/QST-0011-config-versus-weighted-sum-under-calibrated-direction-gates]]"
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
  - "[[wiki/answers/ffrefine-config-vs-weighted-sum-water-campaign-results]]"
  - "[[wiki/tensions/TEN-0020-config-family-exclusion-versus-untreated-drift]]"
  - "[[wiki/answers/ffrefine-decision-register]]"
sources:
  - SRC-0018
sensitivity: public
encryption: none
project_evidence:
  - "FFRefine water run 20260924-204914: density replay predictions optimistic in 6 of 6 epochs 4-9 (mean error about +0.05); total optimistic in 9 of 12 epochs from epoch 10"
  - "FFRefine water runs 20260930-132851 (ConFIG) and 20260930-132911 (weighted sum), read 2026-10-01 after 6 epochs: density cumulative replay-calibration z above 3 from epoch 4 (3.17-4.19) and from epoch 3 (3.36-4.48) respectively; rdf reached 3.17 at epoch 6 in the weighted-sum run"
  - "Both campaigns still running; snapshot taken 2026-10-04 (weighted sum 23 epochs, ConFIG 27 epochs): rdf persistently optimistic by about 5% in both runs (cumulative z 4.5 weighted sum, 5.9 ConFIG); density optimistic under weighted sum (cumulative error +0.94, z 4.7) and fading under ConFIG (z 1.9); dielectric unbiased whenever included"
  - "2026-10-05 update, ConFIG checkpoints 28 and 31 (density excluded both times): replay OVER-predicted density's rise (predicted +2.14 and +2.27; realised +1.32 and +1.70) -- the opposite sign from density's own earlier optimism and from the earlier roughly 2x under-prediction of dielectric's rise in chains 23-26"
scope: timeless
---

# What Should FFRefine Do About a Family Whose Replay Predictions Stay Optimistic?

## Question

When one target family's replay-predicted improvement is repeatedly worse on the next fresh archive than the replay chain predicted (a significant, same-sign cumulative calibration error), should the optimiser change its behaviour for that family, and how? [SRC-0018]

## Context

SRC-0018-style replay optimisation trusts a frozen archive only within its support; a multi-step chain can still optimise its own replay estimate (an optimiser's-curse effect) and drift away from what fresh resimulation shows. [SRC-0018] FFRefine records per-family replay calibration with a telescoping cumulative standard error and warns at cumulative $|z|>3$, report only. The density family has now shown persistent optimism in three water runs: the legacy run `20260924-204914` (epochs 4–9), and both 2026-09-30 deciding runs, under ConFIG and under weighted sum, so the effect is not specific to one aggregation. At `6b20031` the direction gates certified only the first step of a chain on the frozen archive, so they could not see this by construction ([[wiki/answers/ffrefine-improved-gates-water-run-lessons]]); at `110fe64` the gates became report-only and no longer certify anything (FFR-020), and their removal is decided (FFR-031 in [[wiki/answers/ffrefine-decision-register]]).

## Current Position

Open and report-only; no candidate response has been implemented or tested. Candidate responses recorded in the project's design document: shorten the chain's archive-KL budget when an included family's cumulative calibration $|z|$ exceeds 3 (this archive-KL budget is itself decided for removal, FFR-037); stop protecting that family under ConFIG (ConFIG is itself decided for removal, FFR-033); or cap its predicted contribution. Two of these three candidate responses therefore act on mechanisms already decided for removal; see [[wiki/answers/ffrefine-decision-register]]. Whether the bias comes mainly from deep reweighting (large archive KL), from the multi-step chain, or from a property of the density estimator is not established.

This question's title and framing assumed a one-directional bias (replay staying optimistic for a family under active training), based on rdf and density's behaviour through the first snapshot (2026-10-04). Later evidence (2026-10-05, see Evidence timeline) showed the sign of the miscalibration is not stable: when a family is excluded from the aggregate step rather than actively trained, replay's prediction error can run in either direction depending on context. This weakens any simple one-directional correction (for example, always discounting an excluded family's predicted rise by a fixed factor) as a general fix, and suggests the bias may be state-dependent — which family, how far it has drifted, whether it is included or excluded — rather than a fixed property of replay reweighting itself.

## Evidence timeline

- 2026-10-04: both campaigns still running; at a snapshot taken 2026-10-04 (weighted sum epoch 23, ConFIG epoch 27), the pattern was unchanged: rdf stayed persistently optimistic by about 5% in both runs (significant mainly because its own standard error is tiny, not because the absolute bias is large); density's optimism continued under weighted sum but faded under ConFIG; dielectric stayed unbiased whenever it was actually included in the chain. See [[wiki/answers/ffrefine-config-vs-weighted-sum-water-campaign-results]] for the snapshot numbers. Still report-only; none of the candidate responses above had been implemented or tested.
- 2026-10-05: new evidence showed the miscalibration's sign is not stable. In ConFIG, when density was excluded at checkpoints 28 and 31, replay **over-predicted** density's rise (predicted +2.14 and +2.27; realised +1.32 and +1.70) — the opposite sign from density's own earlier persistent optimism, and from the earlier roughly 2x *under*-prediction of dielectric's rise when it was excluded at checkpoints 23-26 (see [[wiki/tensions/TEN-0020-config-family-exclusion-versus-untreated-drift]]). So the same kind of event — a family excluded from the aggregate step, then drifting until it returns — produced both an under-predicted and an over-predicted drift, for different families in the same run. See [[wiki/answers/ffrefine-config-vs-weighted-sum-water-campaign-results]] for the full numbers; this remains open and report-only.

## Links

- [[wiki/answers/ffrefine-direction-gates-and-production-policy]]
- [[wiki/answers/ffrefine-improved-gates-water-run-lessons]]
- [[wiki/answers/ffrefine-loss-gate-diagnostic-policy]]
- [[wiki/questions/QST-0011-config-versus-weighted-sum-under-calibrated-direction-gates]]
- [[wiki/concepts/awh-replay-force-field-optimization]]
- [[wiki/answers/ffrefine-config-vs-weighted-sum-water-campaign-results]]
- [[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]
- [[wiki/answers/ffrefine-decision-register]]
