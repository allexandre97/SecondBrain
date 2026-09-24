---
type: claim
status: active
created: 2026-09-24
updated: 2026-09-24
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
  - "[[wiki/answers/adding-config-optimiser-to-ffrefine]]"
  - "[[wiki/tensions/TEN-0020-config-family-exclusion-versus-untreated-drift]]"
  - "[[wiki/concepts/conflict-free-pinn-training]]"
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
  - "[[wiki/sources/SRC-0036-config-towards-conflict-free-training-of-physics-informed]]"
sources:
  - SRC-0036
sensitivity: public
encryption: none
project_evidence:
  - "FFRefine run water_rdf-dens-diel_aggressive, epoch 5, observed 2026-09-24: density family raw gradient norm collapsed 228 to ~2 over five epochs with sign-flipping chronological halves and delete-block reliability moving from :uncertain (signal 0.012, SE 0.044) to :negligible, while remaining active in ConFIG; aggregate step collapsed to estimated KL 0.0017"
  - "FFRefine synthetic unit test, 2026-09-24: two resolved families plus one near-zero, sign-flipping family under an identity Fisher gives a three-family ConFIG step more than 100x smaller than the two-family step with the unreliable family removed"
---

# ConFIG Must Exclude Directionally Unreliable Families, Not Just Gate Readiness on Them

## Claim

In FFRefine's family-level, Fisher-whitened ConFIG aggregation, keeping a target family active whose treated latent direction is classified `:uncertain` or `:negligible` by the delete-block archive-direction reliability screen can collapse the aggregate parameter step by orders of magnitude, because ConFIG normalizes every included family's whitened gradient to unit norm and gives it equal angular weight in the common-direction construction regardless of the reliability of that direction. [SRC-0036, equations 2-3]

A small *raw* gradient norm or a low pairwise cosine alone is not an adequate exclusion criterion; the failure mode is specifically tied to directional unreliability as estimated from delete-block replicates of the treated (post-Fisher-whitening) direction, which the archive-direction reliability screen already computes for readiness purposes. See [[wiki/answers/adding-config-optimiser-to-ffrefine]].

## Scope

This is a local project-evidence claim about the specific family-level Fisher-whitened ConFIG construction implemented in FFRefine (`optimiser.jl`, `backend.jl`), applied to water density, RDF, and dielectric target families under reaction-field/cutoff electrostatics and QEq-plus-bounded latent parameters.

It is not a claim about ConFIG in general, about physics-informed neural network training (SRC-0036's original setting), or about every possible aggregation scope (`config_scope`) FFRefine could use. It does not establish a calibrated numerical exclusion threshold; it establishes only that inclusion of a directionally unreliable but formally active family caused a large collapse in one observed run and in one synthetic reproduction.

## Evidence

In run `water_rdf-dens-diel_aggressive`, the density family's raw replay gradient norm fell 228, 117, 37, 20, and approximately 2 across macro epochs 1 through 5. Its chronological archive-half directions flipped sign, and its delete-block reliability classification was `:uncertain` (signal 0.012, standard error 0.044) on one attempt and `:negligible` on the next. Density remained an active ConFIG family throughout. At epoch 5 the estimated aggregate-step KL was 0.0017 at nominal scale 1.0, with the RDF and dielectric step projections roughly 10 to 30 times smaller than in earlier, better-conditioned epochs.

A synthetic unit test isolates the mechanism from any archive-specific confound: with two resolved families and one near-zero, sign-flipping family under an identity Fisher, the three-family ConFIG step is more than 100x smaller than the two-family step obtained by removing the unreliable family.

## Why this matters

ConFIG's common-descent construction is designed to give every protected family a guaranteed, balanced positive projection. [SRC-0036, section 3.1] That guarantee is only useful when every included family's gradient is itself a trustworthy estimate of a descent direction. When one included family's direction is dominated by sampling noise, ConFIG does not down-weight it in proportion to its unreliability; it treats it as an equally weighted constraint, which can force the shared direction into a small, poorly conditioned compromise rather than making genuine progress on the resolved families.

## Adopted response

FFRefine now excludes families classified `:uncertain` or `:negligible` by the delete-block reliability screen from the ConFIG family set used to construct the aggregate direction, renormalizing the remaining family weights while preserving within-family target weighting. Excluded families remain in monitoring, ESS/support accounting, and KL coverage. This creates a distinct risk, discussed in [[wiki/tensions/TEN-0020-config-family-exclusion-versus-untreated-drift]]: excluding a family removes its only training signal for that epoch.

## Links

- [[wiki/answers/adding-config-optimiser-to-ffrefine]]
- [[wiki/tensions/TEN-0020-config-family-exclusion-versus-untreated-drift]]
- [[wiki/concepts/conflict-free-pinn-training]]
- [[wiki/concepts/awh-replay-force-field-optimization]]
- [[wiki/sources/SRC-0036-config-towards-conflict-free-training-of-physics-informed]]
