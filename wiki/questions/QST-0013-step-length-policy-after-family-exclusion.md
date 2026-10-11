---
type: question
status: active
created: 2026-10-01
updated: 2026-10-05
question_status: open
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/machine-learning/scientific-modeling
  - research/scientific-computing
tags:
  - question
  - ffrefine
  - natural-gradient
  - trust-region
  - step-length
related:
  - "[[wiki/claims/CLM-0048-family-weight-renormalisation-changes-natural-gradient-step-length]]"
  - "[[wiki/answers/ffrefine-direction-gates-and-production-policy]]"
  - "[[wiki/answers/ffrefine-improved-gates-water-run-lessons]]"
  - "[[wiki/answers/adding-config-optimiser-to-ffrefine]]"
  - "[[wiki/answers/ffrefine-config-vs-weighted-sum-water-campaign-results]]"
sources: []
sensitivity: public
encryption: none
project_evidence:
  - "FFRefine water run 20260924-204914: renormalisation boosted rdf-only and rdf+density steps (uncapped KL 0.77 vs 0.0045 without renormalisation at epoch 10); five crawl chains hit the proposal limit at mean step KL 0.001-0.009, about 1.5 h each"
  - "FFRefine master 6b20031: losses and loss thresholds reported on the full-objective scale; the optimiser step still uses weights renormalised over the included families"
  - "FFRefine weighted-sum water run 20260930-132911 (still running; snapshot through epoch 23 taken 2026-10-04), from about epoch 11: a distinct pathology on the same KL-capped step (consecutive proposals alternating sign, step KL steady at about 0.095, 8 of 10 chains hitting the 21-proposal limit from epoch 14), implicating density (the stiffest included family) rather than renormalisation alone; see [[wiki/answers/ffrefine-config-vs-weighted-sum-water-campaign-results]]"
  - "Same weighted-sum run, checkpoints 23-27 (density excluded for 5 consecutive epochs, ended by an unrelated out-of-memory crash at epoch 27): the two-cycle vanished (step cosine back to +1.0, path/displacement 1.0) and was replaced by a crawl -- all 21 proposals used every chain, median step KL falling 0.0020 to 0.0008, predicted gain only 0.03-0.06 per chain, epochs still about 285 min because cost is per proposal, not per net displacement"
---

# What Step-Length Policy Should FFRefine's KL-Capped Natural-Gradient Step Use After Family Exclusion?

## Question

FFRefine's replay step is the natural gradient with learning rate 1, capped at a KL target but never lengthened, so its length follows the objective's arbitrary scale. Should the step keep renormalising family weights over the included families after an exclusion, and should it instead always step to the KL target or use some other explicit scale convention?

## Context

Renormalisation leaves the direction among included families unchanged but rescales the uncapped step; in run `20260924-204914` it acted as an accidental step-size boost in exactly the epochs where the lowest-weight family made its best progress ([[wiki/claims/CLM-0048-family-weight-renormalisation-changes-natural-gradient-step-length]]). Near the optimum, small gradients give "crawl chains" of many tiny proposals. Always stepping to the KL target would remove crawl chains, but with loss gates diagnostic by default nothing would catch an overshoot of a stiff family. Under weighted sum, renormalisation also weakens the prior relative to the data whenever families are excluded.

## Current Position

Undecided as of 2026-10-04. Reporting has been moved to the full-objective scale; the step itself is unchanged. The project treats renormalisation, step length and the weighted-sum prior balance as one design question that would need its own campaign.

The weighted-sum campaign (`20260930-132911`, ended 2026-10-05 on an unrelated out-of-memory crash; see below) adds a related but distinct failure mode to this question: from about epoch 11, once the easier directions were mostly resolved, consecutive accepted steps began alternating sign at the KL cap (a bounded two-cycle), with 8 of 10 chains hitting the 21-proposal limit from epoch 14. The step KL itself stayed at about 0.095 throughout; what grew, from about +/-0.005 to +/-0.05, was the replay loss change between alternating proposals. Chains run without density active were straight in both runs, implicating density (the tightest-tolerance, stiffest included family) as the oscillating direction. This did not corrupt the chain's own replay calibration, but wasted wall time. It is inference, not established, that this reflects loss curvature exceeding the Fisher-metric scale the KL cap is set against, independent of the renormalisation effect already described by [[wiki/claims/CLM-0048-family-weight-renormalisation-changes-natural-gradient-step-length]]. See [[wiki/answers/ffrefine-config-vs-weighted-sum-water-campaign-results]] for details; candidate remedies (in-chain line-search descent, momentum/averaging, curvature-aware step length) are untested.

## Update (2026-10-05): the same run showed both step-length failure modes

Once density was excluded for five consecutive epochs (23-27, with a noise-level own gradient consistent with a constrained optimum), the two-cycle vanished: the step-to-step cosine returned to +1.0 and the path/displacement ratio to 1.0. In its place, the chains began to **crawl**: every chain used its full 21-proposal budget, median step KL fell from about 0.0020 to 0.0008 across these epochs, and the predicted gain per chain was only 0.03-0.06. Epochs still took about 285 minutes, because FFRefine's per-epoch replay cost is dominated by the number of proposals attempted, not by how far they collectively move. **A single run has therefore now exhibited two distinct step-length failure modes**: a bounded two-cycle at the KL cap while the stiff, conflicting family is included, and a crawl of many tiny, individually well-calibrated but barely-progressing proposals once it is excluded. This sharpens the "always step to the KL target" option considered above: doing so would remove the crawl but, as already noted, nothing would catch an overshoot of the stiff family if it later returned — the two failure modes may require different remedies rather than one shared fix. The run ended before this could be observed further: its epoch-27 worker was killed by an out-of-memory condition unrelated to the step-length question itself. See [[wiki/answers/ffrefine-config-vs-weighted-sum-water-campaign-results]] for full numbers.

## Links

- [[wiki/claims/CLM-0048-family-weight-renormalisation-changes-natural-gradient-step-length]]
- [[wiki/answers/ffrefine-direction-gates-and-production-policy]]
- [[wiki/answers/ffrefine-improved-gates-water-run-lessons]]
- [[wiki/answers/adding-config-optimiser-to-ffrefine]]
- [[wiki/answers/ffrefine-config-vs-weighted-sum-water-campaign-results]]
