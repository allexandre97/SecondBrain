---
type: answer
status: active
created: 2026-07-28
updated: 2026-07-28
question: "How can ConFIG be added to the FFRefine pipeline to alleviate gradient conflicts between losses?"
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
  - gradient-conflict
  - multi-objective-optimization
  - natural-gradient
  - replay-reweighting
related:
  - "[[wiki/concepts/conflict-free-pinn-training]]"
  - "[[wiki/concepts/tolerance-normalized-multi-observable-losses]]"
  - "[[wiki/answers/ffrefine-current-implementation-status]]"
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
  - "[[wiki/sources/SRC-0036-config-towards-conflict-free-training-of-physics-informed]]"
  - "[[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]"
sources:
  - SRC-0036
  - SRC-0018
sensitivity: public
encryption: none
wiki_pages_used:
  - "[[wiki/concepts/conflict-free-pinn-training]]"
  - "[[wiki/concepts/tolerance-normalized-multi-observable-losses]]"
  - "[[wiki/answers/ffrefine-current-implementation-status]]"
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
  - "[[wiki/sources/SRC-0036-config-towards-conflict-free-training-of-physics-informed]]"
  - "[[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]"
raw_sources_consulted: []
wiki_pages_updated:
  - "[[wiki/concepts/conflict-free-pinn-training]]"
  - "[[wiki/answers/ffrefine-current-implementation-status]]"
  - "[[wiki/index]]"
  - "[[wiki/log]]"
project_evidence:
  - "FFRefine optimiser and backend code audit on 2026-07-28"
  - "FFRefine ConFIG optimizer implementation and focused tests on 2026-07-28"
  - "FFRefine post-Fisher momentum implementation and focused tests on 2026-07-28"
---

# Adding ConFIG to FFRefine

## Short answer

Add ConFIG as an optional **loss-gradient aggregation policy inside the existing natural-gradient proposal loop**. Do not replace FFRefine's replay estimators, Fisher metric, KL trust region, line search, or effective-sample-size (ESS) gates.

The important adaptation is to apply ConFIG in the geometry of the step that FFRefine actually takes. A plain Euclidean ConFIG aggregate followed by the current Fisher inverse is not generally conflict-free: Fisher preconditioning can rotate the direction and make a protected loss increase. Instead:

1. retain a separate latent-coordinate gradient for each loss family;
2. whiten those gradients with the regularized latent Fisher matrix;
3. run ConFIG on the whitened family gradients;
4. map the result back to a natural-gradient parameter step;
5. scale it to the existing KL target; and
6. keep the current replay-loss, ESS, parameter-bound, and resimulation checks.

For FFRefine's water experiment, the default ConFIG tasks should be the existing `:density`, `:rdf`, and `:dielectric` families, not every RDF bin. Family-level aggregation preserves the existing tolerance and within-family weighting while avoiding a large, poorly conditioned pseudoinverse.

## Why the present aggregation can collide

FFRefine currently converts every target to a tolerance-normalized residual, applies its Huber or mean-squared-error slope, normalizes target weights within each family, weights the families, and sums all contributions into one gradient. That scalar objective is useful for ranking candidates, but a decrease in the weighted sum can conceal an increase in one family.

ConFIG defines conflict using the loss-specific gradients: an update direction is conflict-free when it has a positive projection on every gradient before the optimizer applies the negative step. It constructs such a direction with balanced projections using normalized gradients and a pseudoinverse. [SRC-0036, section 3.1]

In FFRefine, however, the proposed step is a natural-gradient step based on the replay Fisher matrix. The ConFIG guarantee therefore needs to be expressed in Fisher geometry rather than attached to the already-summed Euclidean gradient.

## Fisher-compatible ConFIG update

Let $\phi$ be FFRefine's global latent parameter vector and let $L_f$ be the current tolerance-normalized objective for target family $f$. Preserve the current target weights inside each family and define

$$
g_f = \nabla_\phi L_f.
$$

Let $F_r$ be the same regularized latent Fisher matrix, retained eigenspace, and numerical floor used by the current optimizer. In that retained subspace, form

$$
h_f = F_r^{-1/2} g_f.
$$

Apply the ConFIG construction to the nonzero $h_f$ vectors:

$$
u =
U\left(
[U(h_1),\ldots,U(h_m)]^{-\top}\mathbf{1}_m
\right),
$$

$$
c =
\left(\sum_f h_f^\top u\right)u,
$$

where $U(v)=v/(\lVert v\rVert+\epsilon)$. [SRC-0036, equations 2-3]

Map the aggregate back to latent parameter space:

$$
\Delta\phi_{\mathrm{raw}} = -F_r^{-1/2}c.
$$

This construction matches the actual natural-gradient geometry because

$$
g_f^\top\Delta\phi_{\mathrm{raw}}
=
-h_f^\top c < 0
$$

for every represented family gradient when the ConFIG conditions hold. The step can then be shortened to FFRefine's existing KL target,

$$
\frac{1}{2}\Delta\phi^\top F_r\Delta\phi
\leq
\mathrm{KL}_{\mathrm{target}}.
$$

Positive scalar shortening preserves the local descent signs. By contrast, constructing a Euclidean ConFIG vector from the $g_f$ values and then applying $-F_r^{-1}$ does not preserve those signs in general.

This Fisher-whitened construction is a project-specific synthesis of ConFIG and FFRefine, not a method evaluated in SRC-0036.

## Minimal code integration

### 1. Expose component objectives

Refactor `objective` in `optimiser.jl` so its current behavior remains the default, but the same calculation can also return one `ObjectiveEvaluation` per family. Each component must use:

- the existing tolerance normalization;
- the configured Huber or MSE slope;
- target weights normalized within that family; and
- the family's gradient rows after physical-to-latent transformation.

Do not feed unnormalized density, RDF, dielectric, or free-energy gradients directly to ConFIG. Their units and target counts differ, and FFRefine already has the normalization needed to make the family objectives comparable through [[wiki/concepts/tolerance-normalized-multi-observable-losses]].

A small API is sufficient:

```julia
family_objectives(targets, phi; target_loss, huber_delta, huber_scale)
config_natural_step(objectives, fisher, settings)
```

Keep `objective(...)` as the weighted-sum path so existing callers and tests remain unchanged.

### 2. Add an aggregation setting

Extend `OptimiserSettings` with an explicit policy such as:

```julia
gradient_aggregation = :weighted_sum  # or :config
config_scope = :family
```

The default should remain `:weighted_sum` until the new route passes focused numerical and production validation. `:target` can be supported later, but it is a poor default for hundreds of correlated RDF-bin losses.

### 3. Replace only direction construction

Inside `optimise_replay_chain`, keep `build_training_targets`, latent-coordinate transformation, candidate replay, and Fisher construction as they are. Replace only this conceptual block:

```julia
evaluation = objective(...)
delta = natural_gradient_step(evaluation.gradient, latent_fisher, settings)
```

with a dispatch:

```julia
evaluation = objective(...)
delta = settings.gradient_aggregation == :config ?
    config_natural_step(family_objectives(...), latent_fisher, settings) :
    natural_gradient_step(evaluation.gradient, latent_fisher, settings)
```

The scalar `evaluation.loss` should remain available for progress reporting and the existing minimum-improvement rules.

### 4. Treat regularization deliberately

Hard charge constraints and parameter bounds already live in FFRefine's latent map and should remain there.

The QEq regularization gradient must not simply be added after ConFIG if strict conflict-free behavior is claimed, because that addition can rotate the step back into conflict. Either:

- include nonzero QEq regularization as another protected ConFIG component; or
- describe ConFIG as protecting only the experimental target families and enforce an explicit maximum regularization increase during line search.

The first option gives the clearest semantics, but it may legitimately return no common descent direction near a trade-off.

### 5. Strengthen finite-step acceptance

ConFIG is a local first-order construction. Candidate replay is nonlinear, and a KL-scaled finite step can still worsen an individual family. The line search should therefore record candidate losses by family and require, for protected families,

$$
L_f(\phi+\Delta\phi)
\leq
L_f(\phi) + \eta_f,
$$

where $\eta_f$ is zero for strict monotonicity or a small configured allowance for replay noise. Retain the existing total-loss improvement, ESS retention, maximum-weight, Fisher, split-half, and parameter-bound gates. Replay support remains a separate validity condition; a conflict-free gradient does not make an unsupported candidate trustworthy. [SRC-0018]

## Degenerate and Pareto-stationary cases

The implementation needs explicit outcomes rather than silently falling back:

- Drop a family from the pseudoinverse only when its gradient norm is below a configured tolerance, and report it as locally stationary.
- If a family gradient has material norm but negligible projection into the retained Fisher eigenspace, stop with a diagnostic such as `:family_outside_fisher_support`.
- Use a stable singular-value cutoff for the normalized-gradient pseudoinverse and record its rank and condition estimate.
- If no positive common direction exists numerically, report `:config_stationary` or `:config_degenerate`. Falling back to the weighted sum would remove the promised per-family protection.
- If strict family-wise line search rejects every scale, end the replay proposal chain and resimulate or reconsider family weights/tolerances; do not bypass ESS or support gates.

M-ConFIG is not the first implementation to add. FFRefine already has all family gradients after one replay-gradient construction, so exact family-level ConFIG involves only a small dense solve. M-ConFIG's alternating momentum mainly helps when separate backpropagations are expensive, and SRC-0036 notes added memory and degradation as the number of losses grows. [SRC-0036, sections 3.2 and 5]

## Post-Fisher momentum adaptation

The useful Adam-like extension for FFRefine is not SRC-0036's M-ConFIG. M-ConFIG maintains per-loss momenta and alternates which loss gradient is refreshed, which solves a backpropagation-cost problem that FFRefine does not currently have. FFRefine already computes the protected family gradients in one replay-gradient pass, so the lower-risk momentum layer is a first-moment average over accepted latent-space parameter displacements after the Fisher solve.

The implemented rule stores only chain-local latent displacement history. On a new proposal, the previous accepted displacement is projected into the current retained Fisher eigenspace, mixed with the current natural-gradient or Fisher-whitened ConFIG direction, then bounded again by the current regularized Fisher metric and KL target before the existing replay line search. The stored history is the accepted line-search displacement, not the rejected raw proposal. Complete rejection or replay-support collapse resets the history, and new frozen-reference ensembles start with no transported momentum.

For weighted-sum aggregation, a Fisher-alignment restart is enough to avoid reusing a previous displacement that opposes the current natural-gradient direction. For ConFIG, aggregate Fisher alignment is not sufficient: a previous displacement can agree with the aggregate direction while still being uphill for one protected family. The reusable guard is component-wise. Limit the effective momentum coefficient, or restart, so every protected current component still has a negative first-order projection after mixing. This preserves the local ConFIG protection before finite-step line-search checks.

This is a project-specific optimizer adaptation supported by FFRefine synthetic tests, not a claim evaluated in SRC-0036 or SRC-0018. It should be interpreted as controlled first-moment smoothing inside the existing replay/Fisher trust-region machinery, not as Adam's second-moment normalization.

## Diagnostics to record

For every proposal, write:

- the norm and normalized loss of each family gradient;
- pairwise cosine similarities before aggregation;
- $h_f^\top c$ and $g_f^\top\Delta\phi$ for every protected family;
- pseudoinverse rank, singular-value cutoff, and condition estimate;
- Fisher modes retained or truncated;
- current and proposed family losses;
- the scalar weighted loss used for reporting;
- KL scale, ESS and maximum-weight diagnostics; and
- the reason for any rejected or terminated proposal.

These values distinguish genuine loss conflict from noisy gradients, Fisher truncation, inadequate replay support, or a finite-step line-search failure.

## Focused validation plan

1. **Linear algebra tests:** use two- and three-objective synthetic gradients and verify $g_f^\top\Delta\phi<0$ after Fisher mapping, including a non-diagonal Fisher matrix. Add a regression test showing that Euclidean ConFIG followed by an arbitrary Fisher inverse can fail this property.
2. **Objective decomposition tests:** verify that summing the family objective values and gradients with the configured family weights reproduces the current weighted objective.
3. **Degeneracy tests:** cover zero gradients, collinear gradients, rank deficiency, truncated Fisher modes, and incompatible regularization.
4. **Line-search tests:** ensure a candidate with lower total loss but a worsened protected family is rejected, while ESS and support rejection behavior remains unchanged.
5. **Water smoke test:** run a reduced replay-only proposal with density, RDF, and dielectric as the three tasks; compare per-family projections, accepted steps, ESS, and scalar loss against `:weighted_sum`.
6. **Scientific validation:** only after the smoke test, compare repeated optimization/resimulation runs. The relevant outcome is not merely fewer negative gradient cosines, but improved cross-family behavior without worse replay support, stability, or transferability.

## Recommendation

FFRefine now implements exact **family-level, Fisher-whitened ConFIG** behind an opt-in setting. The implementation keeps the weighted objective for reporting and candidate ranking, and adds family-wise finite-step guards. This is the smallest change that respects both ConFIG's conflict-free condition and FFRefine's natural-gradient/replay architecture.

The implemented route deliberately avoids per-bin ConFIG, M-ConFIG, and a standalone optimizer that bypasses FFRefine's Fisher and replay checks. The useful implementation lesson is that ConFIG should reuse the exact regularized, Jacobi-scaled, eigen-truncated Fisher factorization used by the natural-gradient path, so the protected descent tests are in the same geometry as the proposed KL-controlled step.

FFRefine now also implements chain-local post-Fisher first-moment momentum for both `:weighted_sum` and `:config` aggregation. The default is deliberately moderate. The momentum proposal is always projected into the current retained Fisher eigenspace, checked against the current weighted or protected-component gradients, KL-bounded with the current Fisher metric, and then passed through the same ESS, drift, objective, and family-guard line search. The important implementation lesson is that ConFIG momentum must be guarded component-wise; Fisher agreement with the aggregate step alone does not protect every loss family.

## Sources used

- [[wiki/sources/SRC-0036-config-towards-conflict-free-training-of-physics-informed]]: ConFIG condition, pseudoinverse construction, M-ConFIG, and limitations.
- [[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]: frozen-reference replay, natural-gradient motivation, and support-sensitive optimization.

## Wiki pages used

- [[wiki/concepts/conflict-free-pinn-training]]
- [[wiki/concepts/tolerance-normalized-multi-observable-losses]]
- [[wiki/answers/ffrefine-current-implementation-status]]
- [[wiki/concepts/awh-replay-force-field-optimization]]

## Wiki updates made

- Expanded [[wiki/concepts/conflict-free-pinn-training]] with the reusable Fisher-geometry adaptation.
- Linked this design from [[wiki/answers/ffrefine-current-implementation-status]].
- Updated [[wiki/index]] and [[wiki/log]], then regenerated category indexes and the knowledge graph.

## Implementation status after 2026-07-28

FFRefine implements this design as an opt-in optimizer aggregation policy, with `:weighted_sum` retained as the default and `:config` selecting family-level Fisher-whitened ConFIG. The replay backend dispatches through the shared optimizer path, so water-temperature and solvation experiments use the same aggregation machinery. Water-temperature can opt in through its configuration, while existing runs remain on weighted-sum aggregation unless changed explicitly.

The implementation treats QEq regularization as a ConFIG component only when QEq regularization is active. This preserves the intended conflict-free semantics without creating artificial protected components in non-QEq optimizations. Candidate callbacks must return values, support diagnostics, and the candidate parameterization so the central optimizer can compute per-family finite-step losses and enforce protected-family guards.

The optimizer also has post-Fisher first-moment momentum enabled by default with a moderate coefficient. It is deliberately chain-local and stores accepted latent displacements, so it does not attempt to transport velocity across rebuilt frozen-reference ensembles. Focused tests include a ConFIG counterexample where an aggregate-aligned previous step is uphill for one protected component; the implemented component-wise beta limiter keeps all protected first-order projections descending.

Focused tests cover ConFIG linear algebra, objective decomposition, degeneracy diagnostics, backend dispatch, validity/reporting behavior, parameterization checks, water-temperature target assembly, optimizer momentum guards, KL rebounding, line-search history storage, and momentum history reporting. The old specialized solvation replay optimizer path was removed in favor of the common optimizer aggregation path.

## Remaining gaps

- SRC-0036 evaluates ordinary ConFIG primarily for PINNs and one multi-task benchmark; it does not validate this replay-force-field adaptation.
- The correct family-wise line-search allowance under correlated replay uncertainty remains an empirical policy choice.
- Production evidence is still needed to show that reduced gradient conflict improves force-field quality rather than merely changing the local optimization trajectory.
