---
type: concept
status: active
created: 2026-06-30
updated: 2026-07-29
areas:
  - research
categories:
  - research/machine-learning/scientific-modeling
tags:
  - PINNs
  - gradient-conflict
  - multi-objective-optimization
sources:
  - SRC-0036
related:
  - "[[wiki/answers/adding-config-optimiser-to-ffrefine]]"
  - "[[wiki/answers/ffrefine-config-fisher-second-momentum]]"
  - "[[wiki/answers/ffrefine-current-implementation-status]]"
  - "[[wiki/concepts/tolerance-normalized-multi-observable-losses]]"
sensitivity: public
encryption: none
---

# Conflict-Free PINN Training

## Summary

Conflict-free PINN training addresses cases where separate PINN loss terms, such as PDE residuals and boundary or initial conditions, produce gradients that interfere with each other. ConFIG constructs a final update direction with positive dot product against each loss-specific gradient and balanced projection lengths. [SRC-0036]

## Key Points

- A multi-loss update conflicts with loss $L_i$ when $g_i^\top g_c < 0$, because stepping along $g_c$ locally increases or fails to decrease that loss. [SRC-0036]
- ConFIG uses a pseudoinverse construction on normalized gradients to find an update direction that is conflict-free for all losses under its assumptions. [SRC-0036]
- Equal projection lengths are used to keep loss terms decreasing at comparable effective rates. [SRC-0036]
- M-ConFIG trades exact per-step gradient aggregation for momentum-based alternating updates, improving cost but adding memory and possible degradation with many losses. [SRC-0036]

## Natural-gradient adaptation

When the optimizer applies a non-Euclidean preconditioner, Euclidean conflict-free aggregation alone does not guarantee that the final parameter step decreases every protected loss. For a regularized Fisher matrix $F_r$, one can instead apply ConFIG to whitened gradients $h_i=F_r^{-1/2}g_i$ and map the aggregate $c$ back with $\Delta\theta=-F_r^{-1/2}c$. Then $g_i^\top\Delta\theta=-h_i^\top c<0$ wherever the ConFIG condition holds in the retained Fisher subspace.

This is a reusable mathematical adaptation inferred from ConFIG's projection condition; it was not evaluated in SRC-0036. Its proposed use in FFRefine is documented in [[wiki/answers/adding-config-optimiser-to-ffrefine]].

## Momentum with protected components

Adding first-moment momentum after a Fisher or natural-gradient solve must keep the same local geometry as the accepted step. Reusing a previous displacement because it aligns with the aggregate Fisher direction is not enough when individual losses are protected: the previous displacement can still have an uphill projection for one component. A safer rule is to project the previous displacement into the current retained Fisher eigenspace, then limit or reset the momentum coefficient so every protected current gradient remains descending before finite-step line search.

For FFRefine, this means the Adam-like layer is chain-local post-Fisher displacement smoothing, not M-ConFIG's alternating per-loss gradient momentum. The lesson is project-specific and test-supported, but not evaluated in SRC-0036.

A full Adam-style second moment is less direct in this setting. The first moment can average accepted post-Fisher latent displacements, but a second moment must choose whether to square raw family gradients, Fisher-whitened family gradients, aggregate ConFIG directions, or accepted displacements. Each choice changes the meaning of the accumulator, and a coordinate-wise denominator can interfere with ConFIG's component-wise projection guarantee or duplicate the Fisher matrix's role as the local metric. The FFRefine-specific implications are summarized in [[wiki/answers/ffrefine-config-fisher-second-momentum]].

## Links

- [[wiki/sources/SRC-0036-config-towards-conflict-free-training-of-physics-informed]]
- [[wiki/answers/adding-config-optimiser-to-ffrefine]]

## Open Questions

- How should conflict-free gradient aggregation be combined with better PINN architectures, causal training, or sampling strategies for chaotic or stiff PDEs?
