---
type: question
status: active
created: 2026-10-01
updated: 2026-10-05
question_status: partially-answered
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/machine-learning/scientific-modeling
  - research/scientific-computing
tags:
  - question
  - ffrefine
  - config
  - multi-objective-optimization
  - direction-gate
  - production-extension
related:
  - "[[wiki/answers/ffrefine-direction-gates-and-production-policy]]"
  - "[[wiki/tensions/TEN-0020-config-family-exclusion-versus-untreated-drift]]"
  - "[[wiki/answers/adding-config-optimiser-to-ffrefine]]"
  - "[[wiki/claims/CLM-0044-config-must-exclude-directionally-unreliable-families]]"
  - "[[wiki/questions/QST-0012-persistent-replay-prediction-optimism-for-one-family]]"
  - "[[wiki/questions/QST-0013-step-length-policy-after-family-exclusion]]"
  - "[[wiki/answers/ffrefine-config-vs-weighted-sum-water-campaign-results]]"
  - "[[wiki/questions/QST-0015-rdf-density-dielectric-pareto-front-for-this-water-parameterisation]]"
sources:
  - SRC-0036
sensitivity: public
encryption: none
project_evidence:
  - "FFRefine shadow water run 20260928-220040 (11 epochs), as summarised in the project's improved-gates design document"
  - "FFRefine water runs 20260930-132851 (ConFIG) and 20260930-132911 (weighted sum), snapshot taken 2026-10-04 (ConFIG 27 epochs/92.3 h, weighted sum 23 epochs/90.8 h); both runs ongoing"
  - "2026-10-05 update: weighted sum ended at checkpoint 26 (107.9 h) when its epoch-27 worker was killed by an out-of-memory condition; ConFIG continued to checkpoint 33 (112.7 h, epoch 34 in progress), with fresh total loss rising from a best of 1.82 to 5.05 by checkpoint 32 as density and dielectric began seesawing and all three families turned pairwise conflicting"
---

# ConFIG or Weighted Sum Under Calibrated Direction Gates?

## Question

Under FFRefine's calibrated, cross-fitted direction gates, which gradient aggregation makes more fresh-archive progress per unit wall time for a multi-family objective: family-level Fisher-whitened ConFIG, which keeps only families it can confidently descend on, or weighted sum, which keeps every family unless it degrades the confident descent of the total? And when ConFIG repeatedly excludes a heavy, under-powered family, is the right response a longer production time for every checkpoint? [SRC-0036]

## Context

The gates evaluate both aggregations at every checkpoint, so the comparison is like-for-like at the level of decisions; the configured aggregation decides. ConFIG gives every included family equal angular weight, which makes noisy families dangerous to include ([[wiki/claims/CLM-0044-config-must-exclude-directionally-unreliable-families]]) but costly to exclude ([[wiki/tensions/TEN-0020-config-family-exclusion-versus-untreated-drift]]). Weighted sum can keep a noisy family whose contribution is small relative to the total, but its step may point uphill for one family.

Evidence so far (provisional):

- Shadow run `20260928-220040`: shadow ConFIG would have excluded the dielectric family in 5 of 11 epochs, never more than two in a row; weighted sum would have kept every family, with steps at 90–118° to one family in several epochs. Excluding dielectric cost about 60–90% of an epoch's progress in the epochs without it.
- ConFIG run `20260930-132851`, epochs 1–6: dielectric (57–65% of the loss) excluded in 4 of 6 epochs with promise $t$ 1.27–1.63 against thresholds of about 2.1–2.3; every rescue had negative expected value; persistent-exclusion warnings suggested about 186–198 ns of production instead of 50 ns. Fresh loss 10.59 to 5.77.
- Weighted-sum run `20260930-132911`, epochs 1–6: no exclusions; fresh loss 9.76 to 4.35.

## Current Position

**Partially answered as of 2026-10-04, from a snapshot of both still-running campaigns** (weighted sum epoch 23, ConFIG epoch 27). On the weighted objective, weighted sum leads clearly at this snapshot and throughout the comparable wall-time range: it reached fresh total loss 1.48, still improving at about -0.08/epoch at its last checkpoint, and excluded only one family (density, from epoch 23, at its own constrained optimum). ConFIG reached a best of 1.82 at checkpoint 22 (about 73 h) before regressing to 3.41 by checkpoint 26 after excluding dielectric for four consecutive epochs (16 of 27 epochs overall: 13 `:descent_not_confident`, 3 `:uncertain`; one rescue, at epoch 27, succeeded). ConFIG's 1.82 at 73 h is not actually ahead of weighted sum at equal wall time: weighted sum had already reached about 1.76 at checkpoint 19 (about 73 h) and 1.65 by about 77 h. So this is not a case of two aggregations in a close race; weighted sum is ahead on the weighted objective. The two runs' identical initial parameters (checkpoint 0) gave fresh losses 9.76 and 10.59 — a roughly 2-sigma difference on dielectric comparable in size to several early epochs' progress, so a single-seed comparison cannot fully separate aggregation effects from run-to-run noise.

The more informative result is that the two aggregations reached different physical compromises: weighted sum converged dielectric closely (residual +50..+34 -> +3.5..-1.8) at the cost of density's thermal-expansion residual (-16.7 -> -21.6 g/L, worse); ConFIG roughly halved RDF RMS and improved density's thermal slope (-16.7 -> -14.6 g/L) but left dielectric essentially unimproved (+50..+34 -> +35..+25) once excluded. Whether this reflects a genuine trade-off among the three families for this parameterisation, walked in different directions by the two aggregations, or is confounded by ConFIG's exclusion and by a weighted-sum step-oscillation pathology on the stiff density direction, is unresolved; see [[wiki/questions/QST-0015-rdf-density-dielectric-pareto-front-for-this-water-parameterisation]].

On the narrower question of raising `production_time` for an under-powered heavy family: ConFIG's exclusion of dielectric was shown to be conflict-driven (whitened gradient cosines between dielectric and the other two families ran -0.17 to -0.77) rather than purely noise-driven, and the persistent-exclusion warning's suggested production time grew from about 160 to 592 ns across the four-epoch exclusion without the exclusion resolving — more data narrows a family's own standard error but does not resolve a genuine gradient conflict with other included families. The "raise production time" response is therefore not a reliable fix once exclusion is conflict-driven; see [[wiki/tensions/TEN-0020-config-family-exclusion-versus-untreated-drift]]. Full comparison, including replay calibration and a weighted-sum KL-capped step-oscillation pathology discovered in this campaign, is in [[wiki/answers/ffrefine-config-vs-weighted-sum-water-campaign-results]].

## Update (2026-10-05)

The comparison ended asymmetrically. Weighted sum's run stopped at checkpoint 26 (last fresh loss measurement 1.376, at checkpoint 25) when its epoch-27 worker was killed by an out-of-memory condition — an infrastructure failure, not a scientific one; the run's own trend at the time was still (slowly) improving. ConFIG kept running and, over checkpoints 27-33, its fresh total loss rose from its best of 1.82 to 5.05 (checkpoint 32) as density and dielectric began seesawing — each excluded in turn, each returning to find the objective had moved uphill — and all three families turned pairwise conflicting (the rdf-density cosine, previously mildly positive, turned negative). Three of six checkpoint-to-checkpoint transitions in that window were statistically confident rises, not merely inconclusive drift, yet none stopped the campaign because the loss gates remain diagnostic.

Taken together, weighted sum's last measured state (fresh loss 1.376, improving) is substantially better than ConFIG's trajectory since checkpoint 27 (fresh loss worsening to 5.05), but this comparison is no longer a clean aggregation-versus-aggregation race: weighted sum's data stops at an externally caused crash, not at a comparable point in its own optimisation trajectory, and ConFIG's regression reflects a qualitatively different exclusion regime (multi-family net-ascending cycling) than the single-family conflict recorded at the first snapshot. The question is left **partially answered**: weighted sum's step-length pathologies (two-cycle, then crawl) and ConFIG's conflict-driven exclusion are both now well documented as reusable lessons (see [[wiki/answers/ffrefine-config-vs-weighted-sum-water-campaign-results]]), but neither campaign reached a clean, comparable terminus from which to declare a winner on this water model. See [[wiki/tensions/TEN-0020-config-family-exclusion-versus-untreated-drift]] for the sharpened tension and [[wiki/questions/QST-0013-step-length-policy-after-family-exclusion]] for the step-length side of weighted sum's behaviour.

## Links

- [[wiki/answers/ffrefine-direction-gates-and-production-policy]]
- [[wiki/tensions/TEN-0020-config-family-exclusion-versus-untreated-drift]]
- [[wiki/answers/adding-config-optimiser-to-ffrefine]]
- [[wiki/claims/CLM-0044-config-must-exclude-directionally-unreliable-families]]
- [[wiki/questions/QST-0012-persistent-replay-prediction-optimism-for-one-family]]
- [[wiki/answers/ffrefine-config-vs-weighted-sum-water-campaign-results]]
- [[wiki/questions/QST-0015-rdf-density-dielectric-pareto-front-for-this-water-parameterisation]]
- [[wiki/sources/SRC-0036-config-towards-conflict-free-training-of-physics-informed]]
