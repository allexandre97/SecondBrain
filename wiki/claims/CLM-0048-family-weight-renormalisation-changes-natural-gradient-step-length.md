---
type: claim
status: active
created: 2026-09-28
updated: 2026-10-12
claim_status: supported
claim_scope: local
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/machine-learning/scientific-modeling
  - research/scientific-computing
tags:
  - claim
  - ffrefine
  - config
  - natural-gradient
  - trust-region
  - multi-objective-optimization
related:
  - "[[wiki/questions/QST-0013-step-length-policy-after-family-exclusion]]"
  - "[[wiki/answers/adding-config-optimiser-to-ffrefine]]"
  - "[[wiki/tensions/TEN-0020-config-family-exclusion-versus-untreated-drift]]"
  - "[[wiki/claims/CLM-0044-config-must-exclude-directionally-unreliable-families]]"
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
  - "[[wiki/answers/ffrefine-improved-gates-water-run-lessons]]"
sources: []
sensitivity: public
encryption: none
project_evidence:
  - "FFRefine water run 20260924-204914 (families rdf, density, dielectric; family weights 1, 2, 10), epochs 1-22, observed through the `improved-gates` design analysis: rdf's effective weight after renormalisation rises from 1/13 (all three families included) to 1 (rdf-only epochs); reconstructed uncapped ConFIG step KL (1/2 |c|^2 from logged h_dot_c) matches logged KL in uncapped epochs (0.032/0.029, 0.088/0.086, 0.0078/0.0083)"
  - "FFRefine epochs 10 and 18 (rdf-only, KL target 0.095): uncapped ConFIG step KL under today's renormalisation was 0.77 and 0.30 (both capped to 0.095); reconstructed without renormalisation it would have been 0.0045 and 0.0018, in the same two epochs that produced rdf's largest per-epoch rdf-loss decreases (about -0.128 and -0.083)"
scope: timeless
---

# Family-Weight Renormalisation After Exclusion Changes the Natural-Gradient Step Length

## Claim

In a multi-family natural-gradient trust-region optimiser whose step length is capped by a KL target but otherwise uses a fixed learning rate, renormalising the remaining family weights to sum to 1 after one or more families are excluded from a proposal leaves the step *direction* among the still-included families unchanged (a common rescaling factor for weighted sum; ConFIG unit-normalizes each component regardless), but rescales the objective's magnitude and therefore the *uncapped* step length before the KL cap is applied. Because the step is never lengthened past the cap but can be shortened by it, this renormalisation acts as an implicit, family-count-dependent step-size change: renormalising after excluding low-weight families from a high-weight family set effectively boosts the step, and the reverse effectively shrinks it, independently of whether the direction itself is trustworthy.

## Scope

This is a local, project-evidence claim about FFRefine's specific optimiser design: a natural-gradient step with learning rate 1, capped (never lengthened) at a KL target, under both `:weighted_sum` and family-level Fisher-whitened ConFIG aggregation, applied to water density/RDF/dielectric target families (weights 1, 2, 10) whose remaining weights are renormalised to sum to 1 whenever one or more families are excluded from a proposal (for example, by the ConFIG directional-reliability screen; see [[wiki/claims/CLM-0044-config-must-exclude-directionally-unreliable-families]]). It is not a claim about multi-objective optimisers in general, and it does not establish what the "correct" step-length policy should be after exclusion; that remains an open project design question.

## Evidence

- With family weights rdf 1, density 2, dielectric 10, rdf's effective (renormalised) weight is 1/13 when all three families are included but 1 in an rdf-only epoch — a 13x change in effective weight from exclusion alone, with no change in which physical direction rdf's gradient points.
- The optimiser's uncapped ConFIG step KL, reconstructed as $\tfrac12|c|^2$ from the logged `h_dot_c` diagnostic, matches the logged KL in epochs where the cap did not bind (0.032 reconstructed vs 0.029 logged; 0.088 vs 0.086; 0.0078 vs 0.0083), confirming the reconstruction is a faithful measure of what the step would have been without the cap.
- In two rdf-only epochs (10 and 18) with a KL target of 0.095, today's renormalised uncapped step KL was 0.77 and 0.30 respectively (both capped down to 0.095). Reconstructing the same epochs *without* renormalisation gives an uncapped KL of only 0.0045 and 0.0018 — three orders of magnitude smaller, and no longer capped at all. These are the same two epochs in which rdf achieved its largest per-epoch loss decreases in the run (about -0.128 and -0.083), i.e. renormalisation acted as an accidental step-size boost in exactly the epochs where it happened to help.

## Why this matters

Reporting and acceptance diagnostics (logged loss, stale-progress thresholds, `max_loss_increase`) that read the renormalised objective directly conflate "the objective's arbitrary scale changed because a family left or rejoined the active set" with "the optimiser made more or less progress." The same coupling determines the step's actual physical length: whether renormalisation should continue to set the step scale, be decoupled from a separately chosen step-length policy, or be replaced by an explicit scale convention are all the same open design question, because the objective's arbitrary scale is what produces both the renormalisation effect and epochs where many tiny, well-supported steps are taken in a row ("crawl chains") once a family converges and the remaining objective shrinks.

## Caveats

- Demonstrated only for FFRefine's specific KL-capped, learning-rate-1 natural-gradient step construction with family-level weighted-sum or ConFIG aggregation; a differently normalized trust-region step (for example, one that always rescales to exactly hit the KL target rather than only capping) would not exhibit the same asymmetric boost/shrink behavior.
- At the time of this analysis, FFRefine's adopted response was limited to reporting the optimised loss on a full-objective scale (data terms divided back by the renormalisation factor, prior terms untouched) without changing the step itself; the step's scale remains renormalised pending a combined step-length-policy decision.
- The regularisation/data balance under `:weighted_sum` is separately affected: an unrenormalised regularisation term becomes relatively weaker whenever excluded families shrink the renormalisation factor (for example, about 13x weaker in an rdf-only epoch); this is a related but distinct effect from the step-length change described here.
- This is a project design finding from a single water run (`20260924-204914`, 22 epochs); it has not been tested against an alternative step-length or normalisation convention.

## Evidence timeline

- 2026-10-04: still undecided. At FFRefine master `6b20031`, losses and loss thresholds are reported on the full-objective scale while the step keeps renormalised weights. The open design question is tracked in [[wiki/questions/QST-0013-step-length-policy-after-family-exclusion]], which also records a distinct KL-cap oscillation pathology observed in the weighted-sum campaign `20260930-132911` (still running as of this 2026-10-04 snapshot; it later ended on 2026-10-05 when its epoch-27 worker was killed by an out-of-memory condition, not by a planned completion); see [[wiki/answers/ffrefine-config-vs-weighted-sum-water-campaign-results]].

## Links

- [[wiki/answers/adding-config-optimiser-to-ffrefine]]
- [[wiki/tensions/TEN-0020-config-family-exclusion-versus-untreated-drift]]
- [[wiki/claims/CLM-0044-config-must-exclude-directionally-unreliable-families]]
- [[wiki/concepts/awh-replay-force-field-optimization]]
- [[wiki/answers/ffrefine-improved-gates-water-run-lessons]]
- [[wiki/answers/ffrefine-config-vs-weighted-sum-water-campaign-results]]
