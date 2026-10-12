---
type: claim
status: active
created: 2026-09-24
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
  - gradient-conflict
  - multi-objective-optimization
  - fisher-information
  - trust-region
related:
  - "[[wiki/answers/ffrefine-direction-gates-and-production-policy]]"
  - "[[wiki/answers/adding-config-optimiser-to-ffrefine]]"
  - "[[wiki/tensions/TEN-0020-config-family-exclusion-versus-untreated-drift]]"
  - "[[wiki/concepts/conflict-free-pinn-training]]"
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
  - "[[wiki/sources/SRC-0036-config-towards-conflict-free-training-of-physics-informed]]"
  - "[[wiki/answers/ffrefine-config-vs-weighted-sum-water-campaign-results]]"
  - "[[wiki/questions/QST-0015-rdf-density-dielectric-pareto-front-for-this-water-parameterisation]]"
sources:
  - SRC-0036
sensitivity: public
encryption: none
project_evidence:
  - "FFRefine run water_rdf-dens-diel_aggressive, epoch 5, observed 2026-09-24: density family raw gradient norm collapsed 228 to ~2 over five epochs with sign-flipping chronological halves and delete-block reliability moving from :uncertain (signal 0.012, SE 0.044) to :negligible, while remaining active in ConFIG; aggregate step collapsed to estimated KL 0.0017"
  - "FFRefine synthetic unit test, 2026-09-24: two resolved families plus one near-zero, sign-flipping family under an identity Fisher gives a three-family ConFIG step more than 100x smaller than the two-family step with the unreliable family removed"
scope: timeless
---

# ConFIG Must Exclude Directionally Unreliable Families, Not Just Gate Readiness on Them

## Claim

In FFRefine's family-level, Fisher-whitened ConFIG aggregation, keeping a target family active whose treated latent direction is classified `:uncertain` or `:negligible` by the delete-block archive-direction reliability screen can collapse the aggregate parameter step by orders of magnitude, because ConFIG normalizes every included family's whitened gradient to unit norm and gives it equal angular weight in the common-direction construction regardless of the reliability of that direction. [SRC-0036, equations 2-3]

A small *raw* gradient norm or a low pairwise cosine alone is not an adequate exclusion criterion; the failure mode is specifically tied to directional unreliability as estimated from delete-block replicates of the treated (post-Fisher-whitening) direction, which the archive-direction reliability screen already computes for readiness purposes. See [[wiki/answers/adding-config-optimiser-to-ffrefine]].

This directional unreliability is not only a family's own sampling noise: campaign evidence (see Evidence timeline) shows it can also arise from a genuine gradient conflict between an included family and the others, and in one campaign eventually generalised to pairwise conflict among every included family.

## Scope

This is a local project-evidence claim about the specific family-level Fisher-whitened ConFIG construction implemented in FFRefine (`optimiser.jl`, `backend.jl`), applied to water density, RDF, and dielectric target families under reaction-field/cutoff electrostatics and QEq-plus-bounded latent parameters.

It is not a claim about ConFIG in general, about physics-informed neural network training (SRC-0036's original setting), or about every possible aggregation scope (`config_scope`) FFRefine could use. It does not establish a calibrated numerical exclusion threshold; it establishes only that inclusion of a directionally unreliable but formally active family caused a large collapse in one observed run and in one synthetic reproduction.

## Evidence

In run `water_rdf-dens-diel_aggressive`, the density family's raw replay gradient norm fell 228, 117, 37, 20, and approximately 2 across macro epochs 1 through 5. Its chronological archive-half directions flipped sign, and its delete-block reliability classification was `:uncertain` (signal 0.012, standard error 0.044) on one attempt and `:negligible` on the next. Density remained an active ConFIG family throughout. At epoch 5 the estimated aggregate-step KL was 0.0017 at nominal scale 1.0, with the RDF and dielectric step projections roughly 10 to 30 times smaller than in earlier, better-conditioned epochs.

A synthetic unit test isolates the mechanism from any archive-specific confound: with two resolved families and one near-zero, sign-flipping family under an identity Fisher, the three-family ConFIG step is more than 100x smaller than the two-family step obtained by removing the unreliable family.

## Why this matters

ConFIG's common-descent construction is designed to give every protected family a guaranteed, balanced positive projection. [SRC-0036, section 3.1] That guarantee is only useful when every included family's gradient is itself a trustworthy estimate of a descent direction. When one included family's direction is dominated by sampling noise, ConFIG does not down-weight it in proportion to its unreliability; it treats it as an equally weighted constraint, which can force the shared direction into a small, poorly conditioned compromise rather than making genuine progress on the resolved families.

## Exclusion mechanism at FFRefine `6b20031` (2026-09-30 to 2026-10-07)

FFRefine excluded families from the ConFIG family set used to construct the aggregate direction, renormalizing the remaining family weights while preserving within-family target weighting. Excluded families remained in monitoring, ESS/support accounting, and KL coverage. This created a distinct risk, discussed in [[wiki/tensions/TEN-0020-config-family-exclusion-versus-untreated-drift]]: excluding a family removes its only training signal for that epoch.

Under ConFIG, a family entered aggregation only if its size statistic (signal over jackknife standard error of the unscaled treated direction) exceeded a Monte Carlo calibrated multiplier; entering families then had to pass a cross-fitted aggregation-promise test, and the least confident failing family was removed until all passed. Under weighted sum, families were not excluded for being uncertain or negligible; one was removed only if it prevented confident descent of the weighted total. Remaining family weights were still renormalised for the step. At FFRefine `110fe64` (2026-10-07) the direction gates became report-only and no longer decide family eligibility (FFR-020); removal of the gates, rescue sizing, and ConFIG itself is decided but not implemented (FFR-031, FFR-032, FFR-033). See [[wiki/answers/ffrefine-decision-register]] and [[wiki/answers/ffrefine-direction-gates-and-production-policy]].

## Evidence timeline

- 2026-09-24: FFRefine's original adopted response excluded families classified `:uncertain` or `:negligible` by the delete-block reliability screen from the ConFIG family set, using a legacy reliability multiplier of 2.
- 2026-10-01: the legacy reliability-multiplier exclusion mechanism described above (2026-09-24) was replaced (commit `26affa0`, 2026-09-30) by the size-statistic/cross-fitted-promise-test mechanism described under "Exclusion mechanism at FFRefine `6b20031` (2026-09-30 to 2026-10-07)." See [[wiki/answers/ffrefine-direction-gates-and-production-policy]].
- 2026-10-04: a still-running ConFIG water campaign (`20260930-132851`), snapshot at 27 epochs, sharpened this claim's mechanism with family weights spanning rdf 1, density 2, dielectric 10. Dielectric was excluded by the current cross-fitted promise test in 16 of 27 epochs (13 `:descent_not_confident`, 3 `:uncertain`), including a 4-consecutive-epoch exclusion. Directly measured whitened inter-family gradient cosines showed dielectric was genuinely in conflict with rdf and density (-0.17 to -0.77 across the run), not merely noisy on its own: when density was separately excluded for its own reasons, dielectric's promise test passed easily, with no change to dielectric's own gradient estimate. The removal rule (drop the single least-confident family) always dropped dielectric, the highest-loss-share family, rather than a lower-share family that was conflicting with it. So the directional unreliability this claim describes can arise specifically from a between-family conflict, not only from a family's own sampling noise. See [[wiki/tensions/TEN-0020-config-family-exclusion-versus-untreated-drift]] and [[wiki/answers/ffrefine-config-vs-weighted-sum-water-campaign-results]] for the campaign-snapshot comparison, including a prior project decision this evidence contradicts.
- 2026-10-05: by checkpoint 33 of the same still-running campaign, the mechanism generalised: whitened gradient cosines show rdf, density, and dielectric now conflicting **pairwise**, not only dielectric against the other two as in the 2026-10-04 observation. The rdf-density cosine, previously mildly positive (+0.05 to +0.17), turned negative (-0.31 to -0.77) over checkpoints 29-34. With the conflict mutual, exclusion stopped behaving like a single-family, bounded sawtooth and became a seesaw between density and dielectric with a net rise in the full objective (fresh total loss 1.82 best, rising to 5.05 by checkpoint 32): each family's return from exclusion was accompanied by an easy promise test (reflecting how far it had drifted), while the other family's promise fell, including two density-excluded chains that ran despite replay's own prediction of a full-objective rise of about 1.4-1.6. This is consistent with, but does not by itself establish, every included family eventually conflicting with every other once the parameter trajectory moves far enough from the shared early-epoch region; see [[wiki/questions/QST-0015-rdf-density-dielectric-pareto-front-for-this-water-parameterisation]] for the open question of whether this reflects the model's achievable parameter space or an artifact of the aggregation's own trajectory. Full numbers in [[wiki/answers/ffrefine-config-vs-weighted-sum-water-campaign-results]].

## Links

- [[wiki/answers/adding-config-optimiser-to-ffrefine]]
- [[wiki/tensions/TEN-0020-config-family-exclusion-versus-untreated-drift]]
- [[wiki/concepts/conflict-free-pinn-training]]
- [[wiki/concepts/awh-replay-force-field-optimization]]
- [[wiki/sources/SRC-0036-config-towards-conflict-free-training-of-physics-informed]]
- [[wiki/answers/ffrefine-config-vs-weighted-sum-water-campaign-results]]
- [[wiki/questions/QST-0015-rdf-density-dielectric-pareto-front-for-this-water-parameterisation]]
