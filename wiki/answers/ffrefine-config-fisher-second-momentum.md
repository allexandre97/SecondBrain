---
type: answer
status: active
created: 2026-07-29
updated: 2026-07-29
question: "Within the FFRefine context and pipeline, when the momentum adam-like step was added to the ConFIG optimiser preconditioned by the Fisher matrix, why is the second momentum tricky, or at least not as obvious, to get as the first momentum was?"
answer_status: answered
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/machine-learning/scientific-modeling
  - research/scientific-computing
tags:
  - ffrefine
  - config
  - natural-gradient
  - fisher-information
  - momentum
  - adam
related:
  - "[[wiki/answers/adding-config-optimiser-to-ffrefine]]"
  - "[[wiki/concepts/conflict-free-pinn-training]]"
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
  - "[[wiki/sources/SRC-0036-config-towards-conflict-free-training-of-physics-informed]]"
  - "[[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]"
sources:
  - SRC-0036
  - SRC-0018
sensitivity: public
encryption: none
wiki_pages_used:
  - "[[wiki/index]]"
  - "[[wiki/answers/adding-config-optimiser-to-ffrefine]]"
  - "[[wiki/concepts/conflict-free-pinn-training]]"
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
  - "[[wiki/sources/SRC-0036-config-towards-conflict-free-training-of-physics-informed]]"
  - "[[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]"
raw_sources_consulted: []
wiki_pages_updated:
  - "[[wiki/concepts/conflict-free-pinn-training]]"
  - "[[wiki/index]]"
  - "[[wiki/log]]"
project_evidence:
  - "FFRefine post-Fisher momentum implementation and focused tests on 2026-07-28"
---

# FFRefine ConFIG Fisher Second Momentum

## Short answer

The first momentum was comparatively natural because it averages objects in the same space as the actual accepted FFRefine update: latent-parameter displacements after Fisher preconditioning, KL bounding, replay line search, and support checks. It can be guarded by projecting the previous accepted displacement into the current retained Fisher eigenspace and limiting or resetting the momentum coefficient so every protected ConFIG component still has a descending first-order projection.

The Adam-style second momentum is trickier because there is no equally obvious object to average. In ordinary Adam, the second moment is an elementwise running average of squared Euclidean gradients. In FFRefine's ConFIG route, the meaningful update has already passed through three structures that are not simple elementwise gradient coordinates: family-level ConFIG aggregation, Fisher whitening and unwhitening, and KL/replay acceptance. ConFIG's guarantee is about signed projections against each protected family gradient, while the Fisher matrix already supplies a covariance-like local metric for trust-region scaling. A naive Adam denominator can therefore change the geometry, rotate or rescale the protected step, and blur whether the scaling is coming from gradient noise, parameter units, replay Fisher curvature, or target-family conflict.

## Why the first momentum was available

FFRefine's replay optimizer builds a latent-space empirical Fisher matrix and uses it as the local KL metric for natural-gradient-like steps. [SRC-0018] The ConFIG adaptation has to respect that geometry: the family gradients are whitened with the regularized Fisher matrix, ConFIG is applied in the whitened space, and the result is mapped back to a latent displacement. [SRC-0036] [[wiki/answers/adding-config-optimiser-to-ffrefine]]

Once that displacement exists, first momentum can be attached after the Fisher solve. The stored state is simply the last accepted latent displacement, not a raw gradient. This makes it compatible with FFRefine's replay pipeline: rejected proposals do not pollute the history, complete rejection or support collapse resets it, and a new frozen-reference ensemble starts without transported momentum.

The hard part for first momentum was the ConFIG guard, not the state itself. Aggregate Fisher alignment is not enough, because a previous displacement can agree with the aggregate direction while still being uphill for one protected family. The implemented guard is component-wise: mix in only as much previous displacement as keeps every protected current gradient locally descending. [[wiki/answers/adding-config-optimiser-to-ffrefine]]

## Why the second momentum is not symmetric

A second moment would need to answer what is being squared and averaged:

- Raw family gradients $g_f$ are in Euclidean latent coordinates, but the accepted ConFIG step is judged after Fisher whitening and mapping.
- Whitened family gradients $h_f=F_r^{-1/2}g_f$ match the ConFIG construction, but their coordinates depend on the current regularized, truncated Fisher factorization.
- The aggregate ConFIG direction $c$ loses component identity, so its square cannot tell which family was noisy or dominating.
- The accepted displacement already includes KL scaling, line-search shortening, parameter bounds, and replay-support effects, so its square mixes optimizer curvature with acceptance-policy artifacts.

That ambiguity matters because Adam's second moment is not just "more memory"; it is a coordinate-wise preconditioner. FFRefine already has a preconditioner, the Fisher matrix, and ConFIG's local protection is projection-based rather than coordinate-wise. Adding another diagonal denominator after ConFIG could silently alter the descent projections that made the Fisher-whitened ConFIG step meaningful.

It is also unclear what timescale the second moment should live on. FFRefine rebuilds frozen-reference ensembles across macro epochs, and the retained Fisher eigenspace can change. A first-moment displacement can be projected into the new current subspace or reset. A second-moment accumulator over squared coordinates is harder to transport, because the coordinate variances are tied to the old Fisher factorization and accepted-step history.

## Practical conclusion

The second momentum should not be copied from Adam mechanically. A defensible version would need a precisely chosen space, probably the current retained Fisher-whitened subspace; explicit reset or transport rules across Fisher rebuilds; and a proof or synthetic regression tests showing that the resulting rescaled direction still satisfies every protected component projection before finite-step line search.

Until then, FFRefine's implemented "Adam-like" part should be read as controlled first-moment smoothing of accepted post-Fisher displacements, not as full Adam with a second-moment denominator. This is a project-specific optimizer conclusion from the FFRefine implementation work; SRC-0036 supports ConFIG and M-ConFIG, and SRC-0018 supports Fisher/KL replay geometry, but neither source validates this exact second-moment extension.

## Evidence used

- [[wiki/sources/SRC-0036-config-towards-conflict-free-training-of-physics-informed]]: ConFIG's conflict-free condition, pseudoinverse construction, and M-ConFIG limitations.
- [[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]: frozen-reference replay, empirical Fisher metric, KL trust-region scaling, and replay-support caveats.
- [[wiki/answers/adding-config-optimiser-to-ffrefine]]: FFRefine-specific Fisher-whitened ConFIG construction and implemented post-Fisher first-moment guard.

## Gaps and uncertainty

- The wiki does not yet contain a validated second-moment algorithm for FFRefine ConFIG.
- A second-moment variant could still be useful, but it needs focused linear-algebra and replay acceptance tests before being treated as part of the optimizer design.
