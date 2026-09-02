---
type: answer
status: active
created: 2026-09-01
updated: 2026-09-02
question: "How does FFRefine construct the unscaled hard-cut, diagonal, identity, continuously damped, and modal-SNR parameter steps, and what motivates each treatment?"
answer_status: answered
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/molecular-simulation/free-energy
  - research/statistics/monte-carlo
  - research/scientific-computing
tags:
  - ffrefine
  - fisher-information
  - natural-gradient
  - jacobi-preconditioning
  - eigenvalue-truncation
  - steepest-descent
  - diagonal-preconditioning
  - tikhonov-damping
  - modal-snr
  - block-jackknife
  - kl-trust-region
related:
  - "[[wiki/answers/ffrefine-prospective-dielectric-damped-fisher-training]]"
  - "[[wiki/answers/ffrefine-paper-methods-knowledge-base]]"
  - "[[wiki/answers/ffrefine-retrospective-fisher-treatment-development]]"
  - "[[wiki/answers/ffrefine-kl-definition-for-extended-ensemble-training]]"
  - "[[wiki/answers/ffrefine-kl-divergence-definition-change]]"
  - "[[wiki/answers/ffrefine-long-archive-target-gradient-convergence]]"
  - "[[wiki/claims/CLM-0039-trust-region-kl-must-match-replay-conditioning]]"
sources:
  - SRC-0018
  - SRC-0023
sensitivity: public
encryption: none
wiki_pages_used:
  - "[[wiki/index]]"
  - "[[wiki/answers/ffrefine-paper-methods-knowledge-base]]"
  - "[[wiki/answers/ffrefine-retrospective-fisher-treatment-development]]"
  - "[[wiki/answers/ffrefine-kl-definition-for-extended-ensemble-training]]"
  - "[[wiki/answers/ffrefine-kl-divergence-definition-change]]"
  - "[[wiki/answers/ffrefine-long-archive-target-gradient-convergence]]"
  - "[[wiki/claims/CLM-0039-trust-region-kl-must-match-replay-conditioning]]"
  - "[[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]"
  - "[[wiki/sources/SRC-0023-statistically-optimal-analysis-multiple-equilibrium-states-mbar]]"
raw_sources_consulted: []
wiki_pages_updated:
  - "[[wiki/answers/ffrefine-retrospective-fisher-treatment-development]]"
  - "[[wiki/index]]"
  - "[[wiki/log]]"
project_evidence:
  - "FFRefine optimiser.jl, backend.jl, gradients.jl, and parameterization.jl, implementation inspected 2026-09-01"
  - "FFRefine water_target_fisher_treatment_development.jl, state-conditional campaign schema version 2, implementation inspected 2026-09-01"
  - "State-conditional treatment protocol fingerprint 533305656758db33454d19af400e39972e1ae94ad2c52ff60c5b0b788d8373f8"
  - "FFRefine state-conditional Fisher-treatment replay completed 2026-08-31"
  - "FFRefine dielectric-only damped-Fisher reaction-field water-temperature run 20260901-171027, completed 2026-09-02"
---

# FFRefine Fisher-Treatment Operators

## Short answer

Every treatment begins with the same latent objective gradient $g$, the same state-conditional Fisher geometry, and the same stabilized Jacobi-scaled eigensystem. A treatment chooses a linear operator $A$ and forms an **unscaled** descent proposal

$$
\Delta\phi^{(0)}=-Ag.
$$

The five treatments differ only in how $A$ converts gradient components into parameter displacement:

- **hard cutting** uses the regularized Fisher pseudoinverse but discards eigenmodes below a fixed normalized-eigenvalue floor;
- **diagonal scaling** divides each latent-gradient component by that parameter's Fisher diagonal and ignores parameter correlations;
- **identity** uses ordinary steepest descent in the chosen latent coordinates;
- **continuous damping** replaces the discontinuous hard pseudoinverse with a Tikhonov spectral filter;
- **modal SNR** starts from hard cutting and shrinks retained modes whose projected target gradient is poorly resolved by a delete-block jackknife.

The retrospective campaign then rescales every nonzero direction to the same maximum state-conditional quadratic KL. That common rescaling makes the comparison primarily about **direction**, not about an arbitrary treatment-specific learning rate. Fisher/KL geometry and frozen-reference replay are grounded in SRC-0018; MBAR supplies the state-normalized replay weights used to estimate expectations and score moments. [SRC-0018] [SRC-0023]

The exact diagonal, damping, and modal-SNR filters described here are FFRefine project methods. They are not attributed to SRC-0018 or SRC-0023.

## Why construct an unscaled step first?

At a current latent parameter vector $\phi$, linearize the objective:

$$
L(\phi+\Delta\phi)
\approx
L(\phi)+g^\mathsf T\Delta\phi,
\qquad
g=\nabla_\phi L.
$$

For a small parameter change, the state-conditional distributional displacement is locally quadratic:

$$
D_{\ell s}(\phi+\Delta\phi\Vert\phi)
\approx
\frac12\Delta\phi^\mathsf T
F_{\ell s}\Delta\phi,
$$

where $\ell$ labels a thermodynamic leg, $s$ labels a physical thermodynamic state, and $F_{\ell s}$ is the corresponding Fisher matrix. [SRC-0018] [[wiki/answers/ffrefine-kl-definition-for-extended-ensemble-training]]

With one Fisher matrix $F$, minimizing the linearized loss subject to a fixed quadratic KL gives a direction proportional to

$$
-F^{-1}g.
$$

The proportionality constant is determined by the trust-region radius. It is therefore useful to separate:

1. the **orientation rule**, $\Delta\phi^{(0)}=-Ag$;
2. the **magnitude rule**, which rescales $\Delta\phi^{(0)}$ to the KL budget;
3. finite-step replay, support, and loss checks.

This separation lets FFRefine ask whether a failure comes from the target gradient, the inverse-Fisher treatment, or the chosen step size.

## Common input: the latent objective gradient

Suppose the fitted target vector is $y(\theta)$, the target loss is $L$, the physical force-field parameters are $\theta$, and the optimizer coordinates are latent parameters $\phi$ with deterministic map $\theta(\phi)$. If

$$
J=\frac{\partial\theta}{\partial\phi},
$$

then replay first produces physical target gradients and maps them into latent coordinates:

$$
G_\phi=G_\theta J,
$$

$$
g
=
\nabla_\phi L
=
G_\phi^\mathsf T\frac{\partial L}{\partial y}
+\nabla_\phi L_{\mathrm{reg}}.
$$

Here $L_{\mathrm{reg}}$ includes parameter-map regularization such as the QEq terms when active. Thus $g$ is the derivative of the complete replay objective in the same latent coordinates in which the step is taken. [[wiki/answers/ffrefine-paper-methods-knowledge-base]]

The identity treatment is therefore not a gradient in raw heterogeneous force-field units. It is a gradient in FFRefine's bounded and constrained latent parameterization.

## Common input: the conditional Fisher metric

### Per-state score covariance

For frame $x_n$ at leg $\ell$ and state $s$, define the physical reduced-potential derivative

$$
h_{n,\ell s}
=
\nabla_\theta u_{\ell s}(x_n;\theta).
$$

Let $w_{n,\ell s}$ be the normalized replay weight of frame $n$ in that state. FFRefine calculates

$$
\mu_{\ell s}
=
\sum_n w_{n,\ell s}h_{n,\ell s},
$$

$$
F_{\theta,\ell s}
=
\sum_n w_{n,\ell s}
\left(h_{n,\ell s}-\mu_{\ell s}\right)
\left(h_{n,\ell s}-\mu_{\ell s}\right)^\mathsf T.
$$

This is the empirical Fisher of the normalized conditional configurational distribution. MBAR supplies normalized multistate weights for such state expectations, but finite-sample reliability still depends on overlap and time-series sampling. [SRC-0023]

### Design-weighted geometry

Let $\omega_\ell$ be the configured normalized leg weight and $\gamma_{\ell s}$ the predeclared state weight. When no explicit state weights are supplied, FFRefine uses the reported TSS design probabilities and renormalizes them over the analyzed target states. It constructs

$$
\bar F_\theta
=
\sum_\ell\omega_\ell
\sum_s\gamma_{\ell s}F_{\theta,\ell s}.
$$

The same parameter-map Jacobian used for target gradients maps every Fisher object to latent coordinates:

$$
F_{\ell s}=J^\mathsf T F_{\theta,\ell s}J,
\qquad
\bar F=J^\mathsf T\bar F_\theta J.
$$

This makes gradients, parameter displacements, and KL geometry refer to the same coordinate system. [[wiki/claims/CLM-0039-trust-region-kl-must-match-replay-conditioning]]

## Common stabilization and eigensystem

All five treatments receive the same regularized average conditional Fisher. FFRefine first adds a numerical ridge:

$$
F_r=\bar F+\lambda_F I.
$$

The water campaign used $\lambda_F=10^{-8}$. This ridge prevents exact singularity and absorbs small numerical negative or zero directions; it is not intended to dominate well-resolved Fisher curvature.

Next, define the Jacobi factors

$$
p_a
=
\left[
\max\left((F_r)_{aa},\varepsilon_J\right)
\right]^{-1/2},
\qquad
P=\operatorname{diag}(p_a).
$$

The water campaign used $\varepsilon_J=10^{-12}$. The eigendecomposition is performed on

$$
C=PF_rP=V\Lambda V^\mathsf T,
$$

with normalized eigenvalues $\lambda_k$ and orthonormal eigenvectors $v_k$. Jacobi scaling makes the spectrum closer to a correlation spectrum, so the eigenvalue floor and damping values do not primarily reflect the arbitrary numerical units of individual latent coordinates.

Define the projected gradient coefficient

$$
z_k
=
v_k^\mathsf T P g.
$$

Every full spectral treatment can then be written as

$$
\Delta\phi^{(0)}
=
-PV\operatorname{diag}(a_k)V^\mathsf T P g
=
-P\sum_k a_k z_k v_k,
$$

where the treatment is completely specified by its modal gain $a_k$.

The Fisher eigenvalues and eigenvectors are properties of the archive, force-field parameterization, and KL definition. They are the same for density, RDF, enthalpy, and dielectric at a fixed endpoint. The resulting steps differ because each target family has a different $g$; modal SNR additionally has family-dependent uncertainty weights.

## Treatment 1: hard-cut full Fisher

### Formula

For the hard treatment,

$$
a_k^{\mathrm{hard}}
=
\begin{cases}
1/\lambda_k, & \lambda_k>\lambda_{\min},\\
0, & \lambda_k\le\lambda_{\min}.
\end{cases}
$$

Therefore

$$
\boxed{
\Delta\phi_{\mathrm{hard}}^{(0)}
=
-PV_K\Lambda_K^{-1}V_K^\mathsf T P g
}
$$

where $K$ is the set of retained modes. Equivalently, with

$$
W=PV_K\Lambda_K^{-1/2},
$$

the step is

$$
\Delta\phi_{\mathrm{hard}}^{(0)}=-WW^\mathsf T g.
$$

The water treatment campaign used $\lambda_{\min}=10^{-3}$ after Jacobi normalization.

### Motivation

The full natural gradient accounts for correlations between parameters. If changing two parameters together produces little distributional change, or if they compensate one another, the off-diagonal Fisher structure should affect the proposed step. This is the main advantage over identity or diagonal scaling. The Fisher/KL relation gives the operator a direct information-geometric motivation. [SRC-0018]

The inverse is dangerous in a weakly identified direction: $1/\lambda_k$ becomes very large as $\lambda_k\rightarrow0$. In finite archives, the smallest modes can represent exact redundancies, constrained combinations, insufficient excitation, or sampling noise. Hard cutting treats those modes as unsupported and removes them.

### Why it is reasonable

- It is the closest tested operator to the ideal natural gradient on the statistically supported subspace.
- It incorporates all retained parameter correlations.
- It makes the retained rank and discarded subspace explicit.
- It prevents uncontrolled amplification of near-null modes.

### Main limitation

The cutoff is discontinuous. A small sampling change that moves $\lambda_k$ across $\lambda_{\min}$ changes its gain abruptly from zero to approximately $1/\lambda_{min}$. The floor is therefore both a regularization choice and a model-selection decision about which parameter combinations are trusted.

## Treatment 2: diagonal Fisher scaling

### Formula

Let

$$
d_a=\max\left((F_r)_{aa},\varepsilon_J\right).
$$

The diagonal treatment uses

$$
A_{\mathrm{diag}}=\operatorname{diag}(d_a^{-1})=P^2,
$$

and hence

$$
\boxed{
(\Delta\phi_{\mathrm{diag}}^{(0)})_a
=
-\frac{g_a}{d_a}.
}
$$

It uses the same regularized Fisher diagonal as the full treatment, but it never diagonalizes or inverts the off-diagonal correlation structure.

### Motivation

Different latent parameters can have very different distributional sensitivities. Dividing by the Fisher diagonal suppresses movement in individually sensitive parameters and permits more movement in individually insensitive parameters. This is an axis-aligned approximation to natural-gradient scaling.

### Why it is reasonable

- It retains local parameter-wise sensitivity information.
- It avoids noisy Fisher eigenvectors and inverse cross-parameter rotations.
- It is simple, deterministic, inexpensive, and numerically stable.
- It is a useful compromise when the diagonal is reproducible but the correlated inverse is not.

### Main limitation

It assumes that the chosen latent axes are the important directions. It cannot recognize compensating parameter combinations or strong correlations. It is not invariant to a general rotation of latent coordinates, and it can be inefficient when the true well-conditioned directions are oblique to the parameter axes.

Diagonal scaling is also not simply a hard-Fisher treatment with different eigenvalue gains: $\operatorname{diag}(F_r)^{-1}$ generally does not commute with the full Fisher eigensystem.

## Treatment 3: identity or latent steepest descent

### Formula

The identity treatment sets

$$
A_{\mathrm{id}}=I,
$$

so

$$
\boxed{
\Delta\phi_{\mathrm{id}}^{(0)}=-g.
}
$$

The Fisher is not used to orient this unscaled step. It is still used later to impose the same state-conditional KL budget as the other treatments.

### Motivation

$-g$ is the direction of steepest first-order loss decrease under an ordinary Euclidean norm in the selected latent coordinates. It is the cleanest control for asking what Fisher preconditioning changes: if two archives agree on $-g$ but disagree after applying a full Fisher inverse, the additional disagreement was introduced by the inverse geometry rather than by a sign disagreement in the raw objective gradient.

### Why it is reasonable

- It preserves the raw target-gradient orientation.
- It introduces no estimated correlation matrix or spectral cutoff.
- It is an essential diagnostic baseline for Fisher-induced rotation or amplification.
- FFRefine's latent map already applies bounds, transformations, and charge constraints, making this baseline more meaningful than steepest descent in raw heterogeneous force-field units.

### Main limitation

Euclidean steepest descent is coordinate dependent. A rescaling or nonlinear reparameterization changes the direction. It also ignores that the same numerical displacement can produce very different distributional changes in different parameter combinations. KL rescaling controls the final overall displacement but does not make the identity direction a natural gradient.

## Treatment 4: continuously damped full Fisher

### Formula

For damping value $\gamma>0$, FFRefine uses

$$
\boxed{
a_k^{\mathrm{damp}}(\gamma)
=
\frac{\lambda_k}{\lambda_k^2+\gamma^2}
}
$$

for $\lambda_k>0$, with zero gain for non-positive modes. Thus

$$
\Delta\phi_\gamma^{(0)}
=
-PV\operatorname{diag}
\left(
\frac{\lambda_k}{\lambda_k^2+\gamma^2}
\right)
V^\mathsf T P g.
$$

This is a Tikhonov-filtered inverse of the Jacobi-scaled Fisher. If $b=Pg$ and $\Delta\phi=Pq$, then $q$ solves

$$
\min_q
\left\|Cq+b\right\|_2^2
+\gamma^2\left\|q\right\|_2^2.
$$

Because $C$ is symmetric, the solution is

$$
q
=
-(C^2+\gamma^2I)^{-1}Cb.
$$

This distinction matters: the implemented filter is $\lambda/(\lambda^2+\gamma^2)$, not the ordinary ridge-inverse filter $1/(\lambda+\gamma)$.

The campaign screened

$$
\gamma\in
\{10^{-4},3\times10^{-4},10^{-3},3\times10^{-3},10^{-2},3\times10^{-2},10^{-1}\}.
$$

Because $C$ is Jacobi normalized, these $\gamma$ values live in the normalized spectral scale.

### Modal behavior

The gain has three useful regimes:

$$
\lambda_k\gg\gamma
\quad\Longrightarrow\quad
a_k\approx\frac{1}{\lambda_k},
$$

$$
\lambda_k=\gamma
\quad\Longrightarrow\quad
a_k=\frac{1}{2\gamma},
$$

$$
\lambda_k\ll\gamma
\quad\Longrightarrow\quad
a_k\approx\frac{\lambda_k}{\gamma^2}\rightarrow0.
$$

Large, well-supported modes therefore behave like an ordinary Fisher inverse, while near-null modes are smoothly suppressed.

### Motivation

Hard truncation forces a binary decision: a mode is either fully inverted or completely removed. Damping replaces that discontinuity with a continuous bias-variance tradeoff. It also permits positive modes below the production hard floor to contribute, while preventing the divergence of $1/\lambda_k$ at zero.

### Why it is reasonable

- It is less sensitive than hard cutting to an eigenvalue lying just above or below a threshold.
- It retains correlated Fisher geometry.
- It exposes a continuous regularization path through $\gamma$.
- It can test whether discarded low-Fisher modes contain reproducible target signal.

### Main limitation

A low-Fisher mode can have a large damped gain when $\lambda_k$ is near $\gamma$. Damping is therefore not automatically conservative. It can reintroduce precisely the weakly identified modes that hard cutting was designed to exclude. The choice of $\gamma$ must be validated against independent archives, temporal blocks, replay support, and fresh simulation rather than selected solely for a larger retrospective loss decrease.

## Treatment 5: modal signal-to-noise filtering

### Formula

The modal-SNR treatment retains the hard eigenvalue floor but multiplies each retained inverse gain by a target-family-specific reliability:

$$
a_{fk}^{\mathrm{SNR}}
=
\begin{cases}
\rho_{fk}/\lambda_k,
& \lambda_k>\lambda_{\min},\\
0,
& \lambda_k\le\lambda_{\min}.
\end{cases}
$$

The reliability is

$$
\rho_{fk}
=
\frac{\mathrm{SNR}_{fk}^2}
{1+\mathrm{SNR}_{fk}^2},
$$

so $0\le\rho_{fk}\le1$. An SNR of zero gives zero gain, an SNR of one gives half the hard-inverse gain, and very large SNR approaches the hard treatment.

The unscaled step is

$$
\Delta\phi_{f,\mathrm{SNR}}^{(0)}
=
-PV\operatorname{diag}
\left(
\frac{\rho_{fk}\mathbf 1[\lambda_k>\lambda_{\min}]}
{\lambda_k}
\right)
V^\mathsf T P g_f.
$$

### How the modal signal is computed

For target family $f$, the full-archive projected gradient coefficient is

$$
z_{fk}=v_k^\mathsf T P g_f.
$$

The family dependence enters through $g_f$. The Fisher eigensystem remains common to all target families at that endpoint.

### How the modal uncertainty is computed

For a chosen chronological block length, FFRefine deletes one block at a time and recomputes the objective gradient. Let $g_f^{(-r)}$ be delete-block replicate $r$, and let there be $B$ replicates. Each replicate is projected through the **same endpoint Fisher factorization**:

$$
z_{fk}^{(-r)}
=
v_k^\mathsf T P g_f^{(-r)}.
$$

The delete-block jackknife standard error is

$$
\widehat\sigma_{fk}
=
\sqrt{
\frac{B-1}{B}
\sum_{r=1}^{B}
\left(
z_{fk}^{(-r)}-\overline z_{fk}^{(-\cdot)}
\right)^2
}.
$$

The modal signal-to-noise ratio is

$$
\mathrm{SNR}_{fk}
=
\frac{|z_{fk}|}{\widehat\sigma_{fk}}.
$$

The implementation requires at least five delete-block replicates for every contributing archive. It screened 2, 5, and 10 ns block lengths.

If two independent archives are pooled with equal weight, FFRefine first computes the modal jackknife standard errors separately and combines them as

$$
\widehat\sigma_{fk,\mathrm{pool}}
=
\frac{
\sqrt{
\widehat\sigma_{fk,A}^2+
\widehat\sigma_{fk,B}^2
}
}{2}.
$$

This is the propagated standard error for the equally weighted mean when the two archive estimates are treated as independent.

For implementation edge cases, zero projected signal and zero standard error gives SNR zero; nonzero signal with zero standard error gives infinite SNR and reliability one.

### Motivation

Hard cutting asks only whether the **distributional curvature** of a mode exceeds the Fisher floor. It does not ask whether the **target-gradient coefficient** in that mode is statistically resolved. Modal SNR adds this second question. A mode can have adequate Fisher support yet have a projected enthalpy or dielectric gradient dominated by time-block variability.

### Why it is reasonable

- It shrinks noisy target-specific modal coefficients without discarding every use of the mode.
- It distinguishes Fisher support from target-gradient resolution.
- The reliability changes smoothly rather than through another binary SNR cutoff.
- Testing several block lengths exposes sensitivity to the assumed correlation timescale.

### Main limitations

- The reliability function is a pragmatic shrinkage rule, not a proof of an optimal Bayesian estimator.
- Delete-block replicates are correlated, and the result depends on block length.
- The calculation estimates uncertainty in $z_{fk}$ while treating $P$, $V$, and $\lambda_k$ as fixed. It does **not** propagate uncertainty in the Fisher matrix, eigenvalues, or eigenvectors.
- It cannot restore modes below the hard Fisher floor, regardless of their apparent target signal.
- A mode can have high within-archive SNR but still fail to reproduce in a new independent archive.

## Common KL rescaling after the unscaled step

The treatments above define direction before the retrospective comparison equalizes magnitude. For every leg and physical state, FFRefine evaluates the unregularized conditional quadratic

$$
K_{\ell s}^{(0)}
=
\frac12
(\Delta\phi^{(0)})^\mathsf T
F_{\ell s}
\Delta\phi^{(0)}.
$$

The raw campaign KL is

$$
K_{\max}^{(0)}
=
\max_{\ell,s}K_{\ell s}^{(0)}.
$$

Provided it is finite and positive, the retrospective treatment campaign uses

$$
\alpha
=
\sqrt{
\frac{\kappa}{K_{\max}^{(0)}}
},
\qquad
\Delta\phi=\alpha\Delta\phi^{(0)}.
$$

The state-conditional campaign used $\kappa=0.005$. It deliberately scales both downward and upward so that every treatment reaches the same quadratic maximum. This is stricter experimental equalization than the production optimizer's ordinary KL cap, which leaves a direction unchanged when it is already below budget.

After scaling,

$$
\max_{\ell,s}
\frac12\Delta\phi^\mathsf T F_{\ell s}\Delta\phi
=
\kappa
$$

to numerical precision. Consequently, a larger replay loss change should be interpreted as a more effective direction at the matched **local conditional-KL** budget, not as a treatment having been assigned a larger learning rate.

## KL diagnostics retained for every direction

The campaign stores more than the limiting maximum:

### Design-weighted average conditional KL

$$
K_{\mathrm{avg}}
=
\sum_{\ell,s}
\omega_\ell\gamma_{\ell s}
\frac12\Delta\phi^\mathsf T F_{\ell s}\Delta\phi
=
\frac12\Delta\phi^\mathsf T\bar F\Delta\phi.
$$

This is the geometry used to orient the natural-gradient operators.

### Limiting condition

The campaign records the leg and state attaining

$$
K_{\max}=\max_{\ell,s}K_{\ell s}.
$$

### Frozen-bias joint and between-state diagnostics

The frozen-bias joint Fisher decomposes as

$$
F_{\mathrm{joint}}
=
\bar F+F_{\mathrm{between}},
$$

where $F_{\mathrm{between}}$ is the covariance of state-dependent mean scores. FFRefine reports

$$
K_{\mathrm{joint}}
=
\frac12\Delta\phi^\mathsf T
F_{\mathrm{joint}}\Delta\phi,
$$

$$
K_{\mathrm{between}}
=
\frac12\Delta\phi^\mathsf T
F_{\mathrm{between}}\Delta\phi.
$$

These do not constrain the treatment-campaign step. They diagnose how strongly the old frozen TSS bias may cease to represent the desired state occupancy before the bias readapts. [[wiki/answers/ffrefine-kl-divergence-definition-change]]

## Compact comparison

| Treatment | Unscaled operator | Uses full correlations? | Uses hard floor? | Uses gradient uncertainty? | Primary purpose |
| --- | --- | ---: | ---: | ---: | --- |
| Hard full | $PV_K\Lambda_K^{-1}V_K^\mathsf TP$ | yes | yes | no | production natural-gradient pseudoinverse on retained support |
| Diagonal | $\operatorname{diag}(F_r)^{-1}$ | no | no | no | stable axis-aligned Fisher approximation |
| Identity | $I$ | no | no | no | latent steepest-descent control |
| Damped | $PV\operatorname{diag}[\lambda/(\lambda^2+\gamma^2)]V^\mathsf TP$ | yes | no; positive modes are smoothly filtered | no | continuous spectral regularization and floor-sensitivity test |
| Modal SNR | $PV_K\operatorname{diag}(\rho_{fk}/\lambda_k)V_K^\mathsf TP$ | yes | yes | projected gradient only | suppress unresolved retained target modes |

## What each treatment can and cannot diagnose

### Hard versus identity

This comparison isolates the total effect of Fisher rotation, correlated scaling, and truncation. Better identity agreement does not by itself prove the Fisher is wrong; it can mean that the Fisher inverse amplifies small archive differences in weak but retained directions.

### Diagonal versus identity

This isolates parameter-wise Fisher scaling without full correlation rotation. If diagonal and identity agree but hard does not, off-diagonal geometry or spectral treatment is the leading suspect.

### Damping versus hard cutting

This tests whether a hard boundary is responsible for instability or lost signal. Improved results at a particular $\gamma$ show that a different spectral bias helps on the analyzed archives; they do not establish that low-Fisher modes will reproduce prospectively.

### Modal SNR versus hard cutting

This asks whether noisy target-gradient projections inside the retained Fisher subspace are driving the step. If SNR and hard treatments are nearly identical, the reliability factors are near one on influential modes or the downweighted modes contribute little. It does not test uncertainty in the Fisher eigensystem itself.

## Why all five treatments make scientific sense

There is no universally best finite-sample inverse:

- hard cutting prioritizes an interpretable supported subspace;
- diagonal scaling prioritizes stability and parameter-wise sensitivity;
- identity prioritizes direct fidelity to the estimated objective gradient;
- damping prioritizes continuity across the Fisher spectrum;
- modal SNR prioritizes target-gradient resolution inside the retained subspace.

They represent different finite-sample bias-variance choices. Comparing them on identical archives and identical conditional-KL budgets is useful precisely because density/RDF controls and enthalpy/dielectric targets can project very differently onto the same Fisher eigensystem.

## Prospective status of continuous damping

The completed state-conditional retrospective campaign found both $\gamma=0.03$ and $\gamma=0.1$ eligible for dielectric. Hard full Fisher produced the strongest fixed-archive cross-replay score, while $\gamma=0.1$ produced the stronger minimum direction-robustness score. The prospective choice of $\gamma=0.1$ therefore prioritized a smooth full-correlation operator and implementation simplicity rather than the largest retrospective effect size.

Run `20260901-171027` supplied the first fresh test. The $\gamma=0.1$ direction passed three consecutive optimization archives; the first two generated updates were then confirmed by paired loss reductions on the next fresh archives. The best checkpoint reproduced in two final-validation simulations. A fourth archive failed the damped half-direction cosine gate, so the result establishes local multi-update utility rather than universal stability. [[wiki/answers/ffrefine-prospective-dielectric-damped-fisher-training]]

The reporters demonstrate why treatment-specific gating matters. Across the six run archives, damping passed five times, hard cutting three times, and the raw gradient twice. A raw-gradient gate would have stopped the run before either fresh-confirmed update. Damping also failed when the fourth archive's sensitivity signal was broadly inconsistent, showing that the operator did not simply force every archive through the gate.

## Validation boundary

An operator can produce a mathematically valid and replay-supported step while still failing in a new simulation. The treatment campaign reuses fixed archives to compare directions and finite replay responses. It does not by itself establish that:

- the direction has converged in the population;
- delete-block uncertainty captures between-archive variability;
- the Fisher eigenvectors are stable;
- the candidate retains support outside the sampled reference;
- the old TSS bias remains immediately portable;
- the loss decrease survives a fresh macro epoch.

These boundaries follow the general requirement that replay-based force-field updates must pass overlap/support diagnostics and ultimately survive fresh simulation. [SRC-0018] [SRC-0023] [[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]] [[wiki/claims/CLM-0038-fixed-archive-gradient-validation-does-not-establish-fresh-archive-trainability]]

## Sources used

- SRC-0018 for frozen-reference replay, empirical Fisher/KL geometry, natural-gradient trust regions, and the requirement for finite-step support and resimulation.
- SRC-0023 for normalized multistate replay weights, state expectations, and overlap limitations.

No raw sources were consulted. Exact operator filters, thresholds, jackknife formulas, edge-case handling, and retrospective equal-KL scaling were checked directly against the FFRefine implementation.

## Wiki pages used

- [[wiki/answers/ffrefine-paper-methods-knowledge-base]]
- [[wiki/answers/ffrefine-retrospective-fisher-treatment-development]]
- [[wiki/answers/ffrefine-kl-definition-for-extended-ensemble-training]]
- [[wiki/answers/ffrefine-kl-divergence-definition-change]]
- [[wiki/answers/ffrefine-long-archive-target-gradient-convergence]]
- [[wiki/claims/CLM-0039-trust-region-kl-must-match-replay-conditioning]]
- [[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]
- [[wiki/sources/SRC-0023-statistically-optimal-analysis-multiple-equilibrium-states-mbar]]

## Wiki updates made

- Added this self-contained mathematical and implementation explanation.
- Linked it from the retrospective Fisher-treatment answer and the main wiki index.
- Recorded the write-back in the wiki log.

## Remaining gaps

- The modal-SNR shrinkage function is pragmatic; no claim of statistical optimality has been established.
- The tested SNR treatment does not quantify Fisher-eigenvector uncertainty.
- Continuous damping at $\gamma=0.1$ has now produced two fresh-confirmed dielectric updates, but no prospective campaign has isolated it against hard cutting, diagonal scaling, or identity under matched independently regenerated trajectories.
