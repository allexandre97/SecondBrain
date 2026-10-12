---
type: answer
status: active
created: 2026-10-11
updated: 2026-10-12
question: "What was FFRefine's optimizer step and validation-gate regime before the 2026-10-07 trust-region change, in paper-methods terms?"
answer_status: answered
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/molecular-simulation/free-energy
  - research/adaptive-sampling
  - research/scientific-computing
tags:
  - ffrefine
  - force-field-optimization
  - paper-methods
  - natural-gradient
  - fisher-information
  - kl-trust-region
  - config-aggregation
  - direction-gates
related:
  - "[[wiki/answers/ffrefine-paper-methods-knowledge-base]]"
  - "[[wiki/answers/ffrefine-current-implementation-status]]"
  - "[[wiki/answers/ffrefine-generalist-package-plan-decisions]]"
  - "[[wiki/answers/ffrefine-fisher-treatment-operators]]"
  - "[[wiki/answers/ffrefine-kl-definition-for-extended-ensemble-training]]"
  - "[[wiki/answers/ffrefine-direction-gates-and-production-policy]]"
  - "[[wiki/questions/QST-0007-checkpoint-assessment-versus-next-direction-readiness]]"
  - "[[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]"
  - "[[wiki/sources/SRC-0036-config-towards-conflict-free-training-of-physics-informed]]"
sources:
  - SRC-0018
  - SRC-0036
sensitivity: public
encryption: none
wiki_pages_used:
  - "[[wiki/answers/ffrefine-paper-methods-knowledge-base]]"
  - "[[wiki/answers/ffrefine-current-implementation-status]]"
  - "[[wiki/answers/ffrefine-fisher-treatment-operators]]"
  - "[[wiki/answers/ffrefine-kl-definition-for-extended-ensemble-training]]"
  - "[[wiki/answers/ffrefine-direction-gates-and-production-policy]]"
  - "[[wiki/questions/QST-0007-checkpoint-assessment-versus-next-direction-readiness]]"
raw_sources_consulted: []
wiki_pages_updated: []
project_evidence:
  - "FFRefine code audit on 2026-07-29 against optimiser.jl, replay.jl, gradients.jl, parameterization.jl, validity.jl, backend.jl, solvation_pipeline.jl, water_temperature.jl, and focused tests"
  - "FFRefine working-tree audit on 2026-09-02 against optimiser.jl, replay.jl, gradients.jl, parameterization.jl, validity.jl, backend.jl, epoch_pipeline.jl, optimisation_history.jl, reporting.jl, solvation.jl, water_temperature.jl, hexane_temperature.jl, and focused tests"
  - "FFRefine clean HEAD audit on 2026-09-23 at a3b6aa552faab3b91271a1e7a9cabbc97793978a: optimizer finite-step family regressions are diagnostic, not an individual acceptance veto"
  - "FFRefine test/config_optimiser_checks.jl passed 33/33 on 2026-09-23"
  - "FFRefine dielectric-only damped-Fisher reaction-field water-temperature run 20260901-171027, completed 2026-09-02"
scope: snapshot
currency: superseded
as_of: 2026-10-01
as_of_commit:
  - FFRefine@6b20031
superseded_by:
  - "[[wiki/answers/ffrefine-current-implementation-status]]"
---

# FFRefine Paper Methods: Pre-2026-10-07 Optimizer and Validation Gates

> [!currency] Superseded — describes the state as of 2026-10-01 (FFRefine@6b20031). Current information: [[wiki/answers/ffrefine-current-implementation-status]]
> Replaced by the damped Levenberg-Marquardt trust-region step introduced at 110fe64 (2026-10-07), which on 2026-10-11 became the canonical regime, superseding this natural-gradient step as the canonical step. This natural-gradient path is still in the code at 110fe64 and is decided for removal (FFR-035); whether the trust-region step replaces it in every experiment is not recorded.

This page records, as a historical snapshot, the Fisher-preconditioned natural-gradient optimizer step (hard-cut or continuously damped treatments, optional ConFIG aggregation, optional post-Fisher momentum, a KL-bounded replay line search) and the validation-gate regime (chronological half-archive and block-based direction gates, support/ESS handling, and the thresholds checked as of the 2026-10-01 audit at FFRefine commit `6b20031`) that [[wiki/answers/ffrefine-paper-methods-knowledge-base]] originally described as current. FFRefine commit `110fe64` (2026-10-07) replaced the optimizer step with a damped Levenberg-Marquardt trust-region step and made the direction gates report-only, and on 2026-10-11 that trust-region step combined with weighted-sum aggregation was declared the project's canonical regime, with the direction gates, ConFIG, momentum, and this natural-gradient path decided for removal; see [[wiki/answers/ffrefine-current-implementation-status]] and [[wiki/answers/ffrefine-generalist-package-plan-decisions]]. The sections below are moved verbatim from the source page and describe only the pre-2026-10-07 state; they are not a record of the current optimizer.

## The optimizer, step by step

### 1. Evaluate the current replay objective

At the current latent vector $\phi_t$, FFRefine:

1. builds candidate physical parameters $\theta(\phi_t)$;
2. computes replay weights and target predictions;
3. calculates physical target gradients;
4. maps them through $J$;
5. computes the family-normalized target loss;
6. adds QEq regularization;
7. retains both the total gradient and per-family gradients.

With ordinary weighted-sum aggregation,

$$
g=\nabla_\phi
\left(L_{\mathrm{target}}+L_{\mathrm{QEq}}\right).
$$

### 2. Stabilize and factorize the average conditional Fisher

First add diagonal regularization:

$$
F_r=\overline F_\phi+\lambda_FI.
$$

Next apply Jacobi scaling:

$$
P
=
\operatorname{diag}
\left[
\max\!\left((F_r)_{aa},\varepsilon_J\right)^{-1/2}
\right].
$$

Diagonalize the scaled matrix:

$$
PF_rP=V\Lambda V^T.
$$

For the hard-cut treatment, only eigenmodes with

$$
\lambda_j>\lambda_{\mathrm{floor}}
$$

are retained. If $V_r$ and $\Lambda_r$ contain those modes, define

$$
W=PV_r\Lambda_r^{-1/2}.
$$

Then

$$
WW^T
$$

is the retained, regularized Fisher pseudoinverse, while $W$ also maps between latent coordinates and the retained Fisher-whitened space. The same stabilized eigensystem is used by the continuously damped and modal-SNR treatments.

### 3. Choose a Fisher treatment and construct a descent direction

With weighted-sum aggregation and hard cutting, the raw natural-gradient direction is

$$
\boxed{
\Delta\phi_{\mathrm{raw}}
=
-WW^Tg.
}
$$

This is the implemented form of

$$
-F_r^+g.
$$

The current water default instead uses continuous Tikhonov damping. Its modal gain is

$$
a_j(\gamma)
=
\frac{\lambda_j}{\lambda_j^2+\gamma^2},
$$

and its raw step is

$$
\boxed{
\Delta\phi_{\mathrm{damp}}
=
-PV\operatorname{diag}\!\left[
\frac{\lambda_j}{\lambda_j^2+\gamma^2}
\right]V^TPg.
}
$$

Unlike a hard pseudoinverse, this retains every positive mode but smoothly suppresses near-null modes. It is not the ordinary ridge filter $1/(\lambda_j+\gamma)$. FFRefine also implements diagonal Fisher scaling, latent-coordinate identity descent, and hard-cut modal-SNR filtering for treatment comparisons and diagnostics. The exact operators and their validation boundaries are recorded in [[wiki/answers/ffrefine-fisher-treatment-operators]].

If ConFIG is enabled on the hard-cut Fisher-whitened path, FFRefine instead protects the active family components. Let

$$
h_f=W^Tg_f
$$

be family gradient $f$ in the retained Fisher-whitened space. Negligible components are dropped. A component whose non-negligible gradient lies outside retained Fisher support causes the proposal to stop.

For the remaining families, form normalized columns

$$
H=
\begin{bmatrix}
h_1/\lVert h_1\rVert & \cdots & h_K/\lVert h_K\rVert
\end{bmatrix}.
$$

FFRefine calculates

$$
c_0=(H^T)^+\mathbf 1,
\qquad
\widehat c=\frac{c_0}{\lVert c_0\rVert},
$$

then scales the common direction as

$$
c=
\left(\sum_fh_f^T\widehat c\right)\widehat c.
$$

The latent proposal is

$$
\Delta\phi_{\mathrm{raw}}=-Wc.
$$

The implementation verifies

$$
h_f^Tc>0
$$

for every protected family, which implies the first-order descent condition

$$
g_f^T\Delta\phi_{\mathrm{raw}}<0.
$$

This is FFRefine's Fisher-space adaptation of ConFIG, not a direct claim made by SRC-0036. [SRC-0036]

### 4. Apply momentum, norm control, and the KL trust region

Optional first-moment momentum reuses the previous **accepted latent displacement**, not an Adam-style raw-gradient moment. On the hard-cut path it is projected into the current retained Fisher step space and kept only if its Fisher inner-product alignment with the new direction is positive. Under ConFIG, the coefficient is reduced or reset if mixing would violate a protected family's descent condition. Momentum is disabled in the current dielectric-only water configuration.

The resulting displacement is first clipped to the configured Euclidean norm limit. FFRefine then estimates a local conditional KL for every leg and state,

$$
\widehat D_{\ell s}
=
\frac12\Delta\phi^TF_{\phi,\ell s}\Delta\phi,
\qquad
\widehat D_{\max}
=
\max_{\ell,s}\widehat D_{\ell s}.
$$

If the maximum exceeds the target $\kappa$,

$$
\Delta\phi
\leftarrow
\Delta\phi
\sqrt{
\frac{\kappa}
{\widehat D_{\max}}
}.
$$

The design-averaged quantity $\tfrac12\Delta\phi^T\overline F_\phi\Delta\phi$ is retained as a geometry diagnostic; the maximum prevents one physical state from being hidden by the average. The current dielectric-only water configuration uses $\kappa=0.005$ per proposal and an empirical archive-to-candidate KL ceiling of 0.1. The Fisher/KL interpretation is local: quadratic scaling does not replace exact finite-step replay diagnostics. [SRC-0018] [[wiki/answers/ffrefine-kl-definition-for-extended-ensemble-training]]

### 5. Replay-only backtracking line search

For trial $j=0,1,\ldots$, the scale is

$$
t_j=2^{-j},
$$

and the candidate is

$$
\phi_{t,j}=\phi_t+t_j\Delta\phi.
$$

For each candidate, FFRefine performs the complete deterministic candidate path:

$$
\phi_{t,j}
\longrightarrow
\theta(\phi_{t,j})
\longrightarrow
u_{nm}(\theta)
\longrightarrow
W_{nm}(\theta)
\longrightarrow
\mathbf y(\theta)
\longrightarrow
L(\phi_{t,j}).
$$

No MD is run inside the line search. In addition to the quadratic proposal cap, FFRefine evaluates the exact state-normalized candidate-to-reference replay KL

$$
D_{\ell s}(\theta'\Vert\theta)
=
\sum_nW_{n,\ell s}(\theta')
\log\frac{W_{n,\ell s}(\theta')}{W_{n,\ell s}(\theta)}.
$$

It checks the maximum across physical states both for the current microproposal and for the total displacement from the archive-generating parameters. The latter is evaluated directly because KL for several aligned steps is not additive.

The central acceptance checks require:

$$
L(\phi_{t,j})
\le
L(\phi_t)+\Delta L_{\max},
$$

finite loss, step, and KL estimates, and compliance with the per-proposal empirical conditional-KL limit and cumulative archive-displacement limit. For ConFIG, each protected component's direction remains first-order descending, but an individual family loss may increase at a finite replay step. The optimizer records those regressions in `failed_components`; they are not an independent acceptance veto. The aggregate-loss, support/ESS, and KL rules remain operative. The first candidate satisfying acceptance is used; if all configured scales fail, the replay proposal chain stops.

### 6. Check support after finite-step acceptance

For normalized candidate weights, FFRefine calculates the Kish effective sample size

$$
\operatorname{ESS}
=
\frac{\left(\sum_n a_n\right)^2}{\sum_na_n^2}
=
\frac{1}{\sum_nW_n^2}.
$$

It records absolute ESS, ESS retention relative to the epoch baseline, local-window support, candidate-ensemble support, and maximum frame weight.

The central line-search predicate does not itself reject an otherwise improving step solely because ESS is low. Immediately after loss acceptance, the backend applies the named support policy:

- if support passes, the candidate becomes the next replay iterate;
- if support fails, the chain stops with `:ess_collapse`, but the finite candidate is retained as the parameter set to be tested by fresh simulation.

This distinction prevents low-support replay predictions from being treated as validated improvements while still allowing resimulation to test a promising direction.

### 7. Recompute gradients or start a new macro epoch

After an accepted, supported replay step, FFRefine recalculates candidate replay summaries and gradients at the new $\phi$. It can take several local replay proposals against the same frozen archive, subject to maximum-proposal, minimum-step, Fisher-support, ESS, and stale-progress stopping rules.

When the replay chain ends, the resulting physical parameters seed the next macro epoch. New MD then determines whether the replay-predicted improvement survives resampling. A fresh archive should separately support:

1. assessment of the sampled checkpoint against its parent on the same new configurations; and
2. assessment of whether split data produce a reproducible treated direction for another update.

(Correction, 2026-10-01: the next sentence describes the pipeline at the time of the first prospective run. The current code records `evaluation_valid`, `evaluation_accepted`, `direction_ready` and `optimisation_ready` separately; `sampling_accepted` survives only as a compatibility alias of `direction_ready`.) The pipeline then still combined these statuses in `sampling_accepted`. In the first prospective dielectric run, failure of the second status prevented the paired comparison required for the first, so checkpoint 3 remained unassessed and final validation reverted to checkpoint 2. This is a control-flow limitation, not evidence that checkpoint 3 worsened the objective. [[wiki/questions/QST-0007-checkpoint-assessment-versus-next-direction-readiness]]

After the configured optimization epochs, FFRefine performs one or more final validation-only epochs or replicas.

The full loop is therefore

$$
\boxed{
\begin{aligned}
\theta^{(k)}
&\xrightarrow{\text{adaptive TSS}}
\text{ready sampler}\\
&\xrightarrow{\text{freeze + production}}
\mathcal D_k\\
&\xrightarrow{\text{MBAR replay}}
\{\mathbf y,\nabla_\theta\mathbf y,F_\theta\}\\
&\xrightarrow{\theta(\phi),\,J}
\{L,\nabla_\phi L,F_\phi\}\\
&\xrightarrow{\text{Fisher step + line search}}
\phi^{(k+1)}\\
&\xrightarrow{\theta(\phi)}
\theta^{(k+1)}
\xrightarrow{\text{fresh simulation}}
\mathcal D_{k+1}.
\end{aligned}
}
$$

## Validation gates and outputs

Before optimization is allowed, FFRefine checks:

- adaptive TSS profile uncertainty;
- local replay/TSS parity with delete-block jackknife uncertainty;
- complete window coverage;
- local or MBAR target ESS and candidate-ensemble ESS;
- split-half disagreement of selected predictions;
- Fisher eigenvalue diagnostics;
- agreement of the selected treated direction across chronological halves (legacy; replaced on 2026-09-30 by block-based direction gates, see the correction below);
- maximum state-conditional quadratic and empirical KL;
- cumulative empirical displacement from the archive-generating parameters.

**Correction (2026-10-01, FFRefine master `6b20031`).** The threshold paragraph below is the 2026-09-02 dielectric-only profile. The half-direction cosine/norm-ratio gate no longer exists: family eligibility is now decided by 8-block jackknife direction gates with Monte Carlo calibrated multipliers and a cross-fitted aggregation-promise test, followed by a generic extend-or-exclude production policy ([[wiki/answers/ffrefine-direction-gates-and-production-policy]]). Current water code defaults checked on 2026-10-01 differ from the profile below in several places: TSS standard-error threshold 0.25 $k_{\mathrm B}T$, MBAR target ESS 100 with retention 0.5, and candidate ESS 200 with retention 0.5 (all environment-configurable); the replay/TSS threshold (1.0 $k_{\mathrm B}T$), per-proposal KL target (0.005) and archive-displacement KL (0.1) are unchanged. Other values below were not re-checked.

The 2026-09-02 dielectric-only water profile used a replay/TSS threshold of 1.0 $k_{\mathrm B}T$, TSS standard-error threshold of 0.5 $k_{\mathrm B}T$, minimum local ESS ratio of 0.01, MBAR target and candidate ESS thresholds of 10 with 0.1 retention, Fisher negative-eigenvalue tolerance of $10^{-6}$, a per-proposal maximum conditional-KL target of 0.005, and a maximum empirical archive-displacement KL of 0.1. The selected damped half-directions must have Fisher-metric cosine at least 0.8 and norm ratio between 0.5 and 2. The direct dielectric family uses its own split diagnostic. Thresholds for density, RDF, enthalpy, and other experiment profiles are configuration-specific rather than universal properties of FFRefine.

History records validity diagnostics, replay uncertainty, ESS, family losses, normalized residuals, line-search trials, conditional and joint-KL diagnostics, treated-direction diagnostics, aggregation diagnostics, physical and latent parameter snapshots, QEq state, selected target curves, memory use, and checkpoints. The prospective run also persisted fresh paired comparisons and validation-replica results. These records are project evidence; their interpretation remains limited by the sampling and experimental design.

