---
type: answer
status: active
created: 2026-07-29
updated: 2026-10-12
question: "What exactly is FFRefine doing, in paper-methods terms?"
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
  - replay-reweighting
  - times-square-sampling
  - mbar
  - water-models
related:
  - "[[wiki/answers/ffrefine-paper-methods-pre-2026-10-07-optimizer-and-gates]]"
  - "[[wiki/answers/ffrefine-generalist-package-plan-decisions]]"
  - "[[wiki/answers/ffrefine-direction-gates-and-production-policy]]"
  - "[[wiki/answers/ffrefine-prospective-dielectric-damped-fisher-training]]"
  - "[[wiki/answers/ffrefine-kl-divergence-definition-change]]"
  - "[[wiki/answers/ffrefine-kl-definition-for-extended-ensemble-training]]"
  - "[[wiki/answers/ffrefine-fisher-treatment-operators]]"
  - "[[wiki/answers/ffrefine-long-archive-target-gradient-convergence]]"
  - "[[wiki/answers/ffrefine-retrospective-fisher-treatment-development]]"
  - "[[wiki/answers/ffrefine-average-observable-trainability-validation]]"
  - "[[wiki/answers/ffrefine-current-implementation-status]]"
  - "[[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]]"
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
  - "[[wiki/concepts/tolerance-normalized-multi-observable-losses]]"
  - "[[wiki/concepts/free-energy-reweighting-for-force-field-fine-tuning]]"
  - "[[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]"
  - "[[wiki/claims/CLM-0039-trust-region-kl-must-match-replay-conditioning]]"
  - "[[wiki/questions/QST-0007-checkpoint-assessment-versus-next-direction-readiness]]"
  - "[[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]"
  - "[[wiki/questions/force-field-training-validation-scope]]"
  - "[[wiki/sources/SRC-0016-fine-tuning-mm-force-fields-to-experimental-free-energies]]"
  - "[[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]"
  - "[[wiki/sources/SRC-0023-statistically-optimal-analysis-multiple-equilibrium-states-mbar]]"
  - "[[wiki/sources/SRC-0036-config-towards-conflict-free-training-of-physics-informed]]"
  - "[[wiki/sources/SRC-0098-graph-nets-partial-charge-prediction]]"
  - "[[wiki/answers/qeq-per-type-electronegativity-hardness-redundancy]]"
sources:
  - SRC-0016
  - SRC-0018
  - SRC-0023
  - SRC-0036
  - SRC-0098
sensitivity: public
encryption: none
wiki_pages_used:
  - "[[wiki/answers/ffrefine-paper-methods-pre-2026-10-07-optimizer-and-gates]]"
  - "[[wiki/answers/ffrefine-generalist-package-plan-decisions]]"
  - "[[wiki/answers/ffrefine-prospective-dielectric-damped-fisher-training]]"
  - "[[wiki/answers/ffrefine-kl-divergence-definition-change]]"
  - "[[wiki/answers/ffrefine-kl-definition-for-extended-ensemble-training]]"
  - "[[wiki/answers/ffrefine-fisher-treatment-operators]]"
  - "[[wiki/answers/ffrefine-long-archive-target-gradient-convergence]]"
  - "[[wiki/answers/ffrefine-retrospective-fisher-treatment-development]]"
  - "[[wiki/answers/ffrefine-average-observable-trainability-validation]]"
  - "[[wiki/answers/ffrefine-current-implementation-status]]"
  - "[[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]]"
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
  - "[[wiki/concepts/tolerance-normalized-multi-observable-losses]]"
  - "[[wiki/claims/CLM-0039-trust-region-kl-must-match-replay-conditioning]]"
  - "[[wiki/questions/QST-0007-checkpoint-assessment-versus-next-direction-readiness]]"
  - "[[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]"
  - "[[wiki/sources/SRC-0016-fine-tuning-mm-force-fields-to-experimental-free-energies]]"
  - "[[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]"
  - "[[wiki/sources/SRC-0023-statistically-optimal-analysis-multiple-equilibrium-states-mbar]]"
  - "[[wiki/sources/SRC-0036-config-towards-conflict-free-training-of-physics-informed]]"
raw_sources_consulted: []
wiki_pages_updated:
  - "[[wiki/index]]"
  - "[[wiki/log]]"
project_evidence:
  - "FFRefine code audit on 2026-07-29 against optimiser.jl, replay.jl, gradients.jl, parameterization.jl, validity.jl, backend.jl, solvation_pipeline.jl, water_temperature.jl, and focused tests"
  - "FFRefine working-tree audit on 2026-09-02 against optimiser.jl, replay.jl, gradients.jl, parameterization.jl, validity.jl, backend.jl, epoch_pipeline.jl, optimisation_history.jl, reporting.jl, solvation.jl, water_temperature.jl, hexane_temperature.jl, and focused tests"
  - "FFRefine clean HEAD audit on 2026-09-23 at a3b6aa552faab3b91271a1e7a9cabbc97793978a: optimizer finite-step family regressions are diagnostic, not an individual acceptance veto"
  - "FFRefine test/config_optimiser_checks.jl passed 33/33 on 2026-09-23"
  - "FFRefine dielectric-only damped-Fisher reaction-field water-temperature run 20260901-171027, completed 2026-09-02"
scope: snapshot
currency: current
as_of: 2026-10-11
as_of_commit:
  - FFRefine@110fe64
---

# FFRefine Paper Methods Knowledge Base

## Short answer

FFRefine alternates between simulation and local, replay-only force-field optimization. A simulation macro epoch produces a frozen reference archive at parameters $\theta^{(k)}$. Within that archive, MBAR supplies normalized candidate-state frame weights; those weights produce free energies, ordinary observable means, relative enthalpies, and fluctuation-derived quantities such as the dielectric constant. Their derivatives are assembled into a tolerance-normalized multi-family loss. The physical-parameter gradients and a design-averaged, state-conditional Fisher metric are then projected through a bounded latent parameterization, including a constrained charge-equilibration (QEq) map. Before FFRefine commit `110fe64` (2026-10-07), a hard-cut or continuously damped Fisher-preconditioned optimizer proposed a small latent displacement, and replay line search tested the displacement against loss, support, per-step empirical KL, and archive-displacement KL without running new molecular dynamics (MD); this pre-2026-10-07 regime is kept as a historical record in [[wiki/answers/ffrefine-paper-methods-pre-2026-10-07-optimizer-and-gates]]. Since that commit, FFRefine instead takes a damped Levenberg-Marquardt trust-region step, declared the project's canonical regime on 2026-10-11; its mathematical account is not yet recorded in SecondBrain (see [[wiki/answers/ffrefine-current-implementation-status]]). Under the pre-2026-10-07 regime, replay proposals that passed the active acceptance checks seeded the next simulation macro epoch, where new configurations could test whether the predicted improvement survived resampling; whether the trust-region step uses the same acceptance-and-reseed flow is not recorded. [SRC-0018] [SRC-0023]

Checkpoint assessment and readiness to construct another direction are conceptually separate. In the first prospective dielectric run the macro pipeline did not yet keep them fully separate: a failed next-direction gate suppressed the paired parent comparison for checkpoint 3, leaving that checkpoint unassessed rather than disproved. The separation was implemented by 2026-09-02; see [[wiki/questions/QST-0007-checkpoint-assessment-versus-next-direction-readiness]]. From 2026-09-30, next-direction readiness was decided by block-based direction gates rather than the half-archive cosine ([[wiki/answers/ffrefine-direction-gates-and-production-policy]]), until FFRefine commit `110fe64` (2026-10-07) made those gates report-only, so they no longer decide eligibility; see [[wiki/answers/ffrefine-current-implementation-status]] and [[wiki/answers/ffrefine-decision-register]].

The framework now has direct prospective evidence for one narrow result: in run `20260901-171027`, two consecutive dielectric-only reaction-field water updates reduced the paired fresh-archive loss, and two final-validation replicas reproduced the best confirmed checkpoint. This does not establish convergence to experiment, improvement of density, radial distribution functions (RDFs), enthalpy, ethanol solvation, hexane properties, or transferability.

## Scope and notation

The three experiment surfaces are:

- ethanol solvation, represented as solvated and vacuum alchemical legs;
- water-temperature fitting, represented as one temperature ladder;
- hexane-temperature fitting, represented as one temperature ladder.

As of the 2026-09-02 audit, water target construction supports density, RDF, relative enthalpy, and dielectric families selected through `WATER_TARGET_FAMILIES`. Training, split validation, required logging, and curve writing are assembled from the same selection. The default is dielectric-only fitting on the complete 28-state ladder from 14 through 41 degrees Celsius, with rigid water, atom/site-pair reaction-field electrostatics, mean-squared loss, a continuously damped Fisher with $\gamma=0.1$, and no momentum. Hexane currently trains relative enthalpy by default; density is implemented but disabled. Ethanol currently trains solvation free energy by default; solvated density is implemented but disabled.

The main symbols below are:

| Symbol | Meaning |
| --- | --- |
| $x_n,V_n$ | coordinates and volume of archived frame $n$ |
| $\theta$ | active physical Molly force-field parameters |
| $\phi$ | unconstrained optimizer coordinates |
| $\theta(\phi)$ | bounded physical parameter map, including QEq charges |
| $u_{nm}(\theta)$ | reduced potential of frame $n$ at target state $m$ |
| $W_{nm}(\theta)$ | normalized replay weight of frame $n$ for state $m$ |
| $y_i(\phi)$ | prediction for scalar training target $i$ |
| $J=\partial\theta/\partial\phi$ | physical-to-latent Jacobian |
| $F_\theta,F_\phi$ | physical- and latent-coordinate empirical Fisher matrices |

## One complete macro epoch

At macro epoch $k$, FFRefine has current parameters $\theta^{(k)}$. It performs the following sequence.

### 1. Build and adapt the TSS simulation

FFRefine constructs the system and its thermodynamic-state ladder. Water and hexane use temperature states; ethanol solvation uses alchemical states in each thermodynamic leg. Times Square Sampling (TSS) is run adaptively until its free-energy uncertainty criterion passes or the allowed adaptive extension is exhausted.

The adaptive stage is used to construct a broad reference distribution. The optimizer does **not** differentiate through the adaptive TSS recursion. This separation is inherited from the frozen-bias replay logic of SRC-0018. [SRC-0018]

### 2. Freeze the sampler and establish replay parity

The converged TSS estimators are frozen. A parity probe logs replay frames from every active TSS window. For each window, FFRefine:

1. reweights only the frames collected from that window to its local thermodynamic states;
2. computes local free energies or observables;
3. combines the local estimates with the same TSS reporting/stitching equations used by Molly;
4. compares the replayed profile with the frozen TSS profile.

Delete-block jackknife intervals are included in this comparison. The purpose is to verify that frame storage, reduced-potential evaluation, local normalization, and TSS stitching agree before the archive is used for optimization.

### 3. Collect frozen production data

With the TSS state fixed, FFRefine runs production MD and stores:

- coordinates, boundaries, active window, and local-state information;
- the information needed to reconstruct physical reduced potentials;
- logged observables required by the active targets;
- special sufficient statistics and direct derivatives for derived observables such as dielectric response.

All replay proposals in this macro epoch use this same frozen archive.

### 4. Construct the MBAR reference mixture

Suppose TSS window $k$ contains local thermodynamic states $\Lambda_k$. Its effective mixture reduced potential for archived frame $n$ is

$$
u^{\mathrm{mix}}_{nk}
=
-\log\sum_{i\in\Lambda_k}
\exp\!\left[f_{ki}+\log\rho_{ki}-u_{ni}\right],
$$

where $f_{ki}$ and $\rho_{ki}$ are the frozen local TSS estimator terms. FFRefine treats these windows as the sampled MBAR states, solves their normalization constants, and constructs a per-frame MBAR log denominator $d_n$. Every window must contain frames, the MBAR normalization residual must be below tolerance, and the window-overlap graph must be connected.

For a target state $m$, the unnormalized log weight is

$$
\ell_{nm}
=
-\left(u_{nm}-s_n\right)-d_n,
$$

where $s_n$ is a stored numerical shift. The normalized replay weight is

$$
W_{nm}
=
\frac{\exp(\ell_{nm})}
{\sum_j\exp(\ell_{jm})},
\qquad
\sum_n W_{nm}=1.
$$

The dimensionless replay free energy is

$$
f_m=-\log\sum_n\exp(\ell_{nm}),
$$

and reported free energies are differences $f_m-f_{m_0}$ relative to a reference state $m_0$. This is the optimizer estimator; local TSS replay remains the parity estimator.

### 5. Turn replay weights into predictions and gradients

For a scalar or vector frame quantity $A_n(\theta)$,

$$
\overline A_m(\theta)
=
\sum_n W_{nm}(\theta)A_n(\theta).
$$

Define the reduced-potential score

$$
g_{nm}
=
\nabla_\theta u_{nm}.
$$

Because the frozen MBAR denominator does not change during candidate evaluation,

$$
\nabla_\theta\log W_{nm}
=
-g_{nm}+\overline g_m,
\qquad
\overline g_m=\sum_nW_{nm}g_{nm}.
$$

The general observable derivative is therefore

$$
\boxed{
\nabla_\theta\overline A_m
=
\underbrace{\sum_nW_{nm}\nabla_\theta A_n}_{\text{direct observable term}}
-
\underbrace{\sum_nW_{nm}
\left(A_n-\overline A_m\right)g_{nm}}_{\text{weight-response covariance term}}
}
$$

or, more compactly,

$$
\nabla_\theta\overline A_m
=
\left\langle\nabla_\theta A\right\rangle_m
-
\operatorname{Cov}_m(A,g_m).
$$

This equation explains how FFRefine differentiates both direct frame observables and predictions built from ensemble averages. For a parameter-independent logged quantity, the direct term is zero. For an observable depending explicitly on charges, both terms are required.

The free-energy derivative is the corresponding weighted score mean,

$$
\nabla_\theta f_m=\sum_nW_{nm}g_{nm},
\qquad
\nabla_\theta(f_m-f_{m_0})
=
\overline g_m-\overline g_{m_0}.
$$

This frozen-reference reweighting layer follows the method in SRC-0018. [SRC-0018]

## How a fluctuation target such as dielectric is calculated

### Per-frame sufficient statistics

The dielectric constant is not available as one meaningful instantaneous scalar per frame. FFRefine instead logs a vector of sufficient statistics. For frame $n$,

$$
\mathbf M_n=\sum_a q_a\mathbf r_{an}
$$

is the total dipole of unwrapped molecules, and the stored vector is

$$
z_n=
\begin{bmatrix}
M_{x,n}\\
M_{y,n}\\
M_{z,n}\\
\lVert\mathbf M_n\rVert^2\\
V_n
\end{bmatrix}.
$$

At temperature state $m$, replay produces the five weighted moments

$$
\overline z_m
=
\sum_nW_{nm}z_n
=
\begin{bmatrix}
\overline{\mathbf M}_m\\
\overline{M^2}_m\\
\overline V_m
\end{bmatrix}.
$$

The dipole fluctuation is then

$$
S_m
=
\overline{M^2}_m
-
\left\lVert\overline{\mathbf M}_m\right\rVert^2.
$$

FFRefine maps these ensemble moments to the dielectric prediction

$$
\boxed{
\epsilon_m
=
1+
\frac{4\pi k_e}{3RT_m}
\frac{S_m}{\overline V_m}
}
$$

where $k_e$ is Molly's Coulomb constant in the code's unit convention, $R$ is the molar gas constant, and $T_m$ is the target temperature.

The implementation applies this estimator to conducting-boundary PME and to Molly's atom/site-pair reaction field. It does not claim that the same expression applies unchanged to arbitrary molecular or global reaction-field formulations.

This distinction matters: the code computes a nonlinear function of reweighted ensemble moments,

$$
\epsilon_m
=
f\!\left(
\overline{\mathbf M}_m,
\overline{M^2}_m,
\overline V_m
\right),
$$

not a weighted mean of per-frame dielectric constants.

### Gradient of the dielectric prediction

Let

$$
C_m=\frac{4\pi k_e}{3RT_m}.
$$

First differentiate the fluctuation:

$$
\nabla_\theta S_m
=
\nabla_\theta\overline{M^2}_m
-
2\overline{\mathbf M}_m^{\,T}
\nabla_\theta\overline{\mathbf M}_m.
$$

Then apply the quotient rule:

$$
\boxed{
\nabla_\theta\epsilon_m
=
\frac{C_m}{\overline V_m}
\left[
\nabla_\theta\overline{M^2}_m
-
2\overline{\mathbf M}_m^{\,T}
\nabla_\theta\overline{\mathbf M}_m
-
\frac{S_m}{\overline V_m}
\nabla_\theta\overline V_m
\right].
}
$$

Each moment derivative inside this expression is calculated with the replay covariance equation above. The dipole also has an explicit charge derivative. For a shared charge parameter $q_j$ applied to atom set $\mathcal A_j$,

$$
\frac{\partial\mathbf M_n}{\partial q_j}
=
\sum_{a\in\mathcal A_j}\mathbf r_{an},
$$

so

$$
\frac{\partial\lVert\mathbf M_n\rVert^2}{\partial q_j}
=
2\mathbf M_n^T
\frac{\partial\mathbf M_n}{\partial q_j},
\qquad
\frac{\partial V_n}{\partial q_j}=0.
$$

FFRefine stores these direct derivatives and adds their replay-weighted mean to the covariance term. When QEq latents control the charges, the physical charge derivative is subsequently multiplied by $\partial q/\partial\phi$.

### How this becomes a dielectric loss

Once $\epsilon_m$ and $\nabla_\phi\epsilon_m$ have been calculated, dielectric is treated like any other scalar target:

$$
r_m^{(\epsilon)}
=
\frac{\epsilon_m-\epsilon_m^{\mathrm{ref}}}
{\tau_m^{(\epsilon)}}.
$$

The Huber or mean-squared target loss is applied to this residual, and the chain rule uses $\nabla_\phi\epsilon_m$. Thus the objective never requires a direct per-frame dielectric label. It requires differentiable sufficient statistics whose ensemble means determine the dielectric constant.

The same pattern applies generally. If

$$
y=f(\mu_1,\ldots,\mu_K),
\qquad
\mu_k=\sum_nW_nA_{kn},
$$

then

$$
\nabla_\theta y
=
\sum_{k=1}^K
\frac{\partial f}{\partial\mu_k}
\left[
\left\langle\nabla_\theta A_k\right\rangle
-
\operatorname{Cov}(A_k,g)
\right].
$$

## How relative enthalpy is calculated

For water or hexane, FFRefine defines the configurational molar enthalpy of frame $n$ as

$$
A_n(\theta)
=
\frac{U_n(\theta)+pV_n}{N_{\mathrm{mol}}},
$$

where $U_n$ is the potential energy, $p$ is the configured pressure, and $N_{\mathrm{mol}}$ is the number of molecules. The temperature-series target is relative to the lowest ladder temperature $m_0$:

$$
\Delta H_m
=
\overline A_m-\overline A_{m_0}
+K_m-K_{m_0},
$$

where $K_m$ is the analytic kinetic contribution calculated from the system degrees of freedom. The reference state is omitted from the target list because its relative value is identically zero.

The gradient of each configurational mean contains both the direct energy derivative and the reweighting response:

$$
\nabla_\theta\overline A_m
=
\left\langle\frac{\nabla_\theta U}{N_{\mathrm{mol}}}\right\rangle_m
-
\operatorname{Cov}_m(A,g_m).
$$

The kinetic correction is independent of the fitted parameters, so

$$
\nabla_\theta\Delta H_m
=
\nabla_\theta\overline A_m
-
\nabla_\theta\overline A_{m_0}.
$$

Water and hexane both implement this relative-enthalpy path. The current water default does not activate it; the current hexane default does.

## Scalar targets, tolerances, and the meaning of alpha

Each scalar target $i$ has:

- prediction $y_i$ and reference $y_i^{\mathrm{ref}}$;
- positive tolerance $\tau_i$;
- nonnegative within-family weight $w_i$;
- family label $f_i$;
- positive family coefficient $\alpha_{f_i}$.

The dimensionless residual is

$$
r_i=\frac{y_i-y_i^{\mathrm{ref}}}{\tau_i}.
$$

For each family $f$, define $W_f=\sum_{j:f_j=f}w_j$ and let
$A=\sum_{g\in\mathcal F}\alpha_g$, where $\mathcal F$ contains only enabled
families. FFRefine's effective scalar weight is

$$
\boxed{
\omega_i
=
\frac{\alpha_{f_i}}{A}
\frac{w_i}{W_{f_i}}.
}
$$

### What $\alpha_f$ is

$\alpha_f$ is a dimensionless, user-configured **between-family importance coefficient**. It answers questions such as “how much of the scalar objective should be assigned to density versus the complete RDF?” It is:

- not a force-field parameter;
- not optimized by FFRefine;
- not an uncertainty or standard deviation;
- not the weight of one individual target;
- normalized over the enabled families, so multiplying every $\alpha_f$ by the same constant changes nothing.

For example, if density and RDF are the only enabled families and

$$
\alpha_{\mathrm{density}}
=
\alpha_{\mathrm{RDF}}=1,
$$

then

$$
\sum_{i\in\mathrm{density}}\omega_i
=
\sum_{i\in\mathrm{RDF}}\omega_i
=
\frac12.
$$

The entire density curve receives half of the target objective and the entire RDF collection receives half, regardless of how many temperatures or RDF bins each family contains. Within each half, $w_i/W_f$ distributes influence among that family's targets.

The three weighting controls have different meanings:

| Quantity | Role |
| --- | --- |
| $\tau_i$ | defines the physical error corresponding to one dimensionless residual unit |
| $w_i$ | distributes importance within one family |
| $\alpha_f$ | distributes importance between complete families |

Every implemented water family currently has $\alpha_f=1$ when enabled. Density, relative-enthalpy, and dielectric targets use unit $w_i$. RDF weights distribute within-family mass by structural region: 0.6 to first-shell bins, 0.3 to second-shell bins, and 0.1 to tail bins for each pair type, divided across the bins in each region. Because the default water run enables dielectric alone, its six scalar targets each receive weight $1/6$.

### Target loss and gradient

For mean-squared error (MSE),

$$
L_{\mathrm{target}}
=
\sum_i\omega_i r_i^2,
$$

with

$$
\nabla_\phi L_{\mathrm{target}}
=
\sum_i
\frac{2\omega_i r_i}{\tau_i}
\nabla_\phi y_i.
$$

For Huber loss,

$$
L_{\mathrm{target}}
=
\sum_i\omega_i c\,h_\delta(r_i),
$$

where

$$
h_\delta(r)=
\begin{cases}
\frac12r^2, & |r|\le\delta,\\
\delta\left(|r|-\frac12\delta\right), & |r|>\delta,
\end{cases}
$$

and

$$
h_\delta'(r)=
\begin{cases}
r, & |r|\le\delta,\\
\delta\,\operatorname{sign}(r), & |r|>\delta.
\end{cases}
$$

Therefore,

$$
\nabla_\phi L_{\mathrm{target}}
=
\sum_i
\frac{\omega_i c\,h_\delta'(r_i)}{\tau_i}
\nabla_\phi y_i.
$$

The current water and hexane experiment surfaces select MSE. The ethanol surface uses the optimizer's default Huber loss with $\delta=1$ and $c=1$. These are experiment settings, not fixed properties of the shared backend.

These are engineering-tolerance-normalized losses, not automatically chi-squared likelihoods. A chi-squared interpretation would require $\tau_i$ to be a justified observation standard deviation. [SRC-0018]

## QEq: from latent coefficients to charge-conserving partial charges

### Why QEq is inside the parameter map

Independent optimization of atomic charges would make charge conservation an external constraint and would not naturally share statistical strength between equivalent atom types. FFRefine instead optimizes electronegativity- and hardness-like coefficients and deterministically solves for charges satisfying every configured molecular charge constraint. Charge equilibration as constrained minimization is also used in the force-field fine-tuning approach of SRC-0016. [SRC-0016]

This functional form originates with the electronegativity/hardness trick in [[wiki/sources/SRC-0098-graph-nets-partial-charge-prediction]] (Wang et al. 2019, Eqs. 12-15), itself adapted from Gilson, Gilson & Potter (2003), and is the same construction used by Espaloma's charge model. [SRC-0098] A 2026-10-07 review established that FFRefine's per-type (shared, looked-up) parameterization of $\mathbf e,\mathbf h$ -- as opposed to Wang/Espaloma's per-atom, graph-net-predicted $\mathbf e,\mathbf h$ -- makes hardness redundant with electronegativity for any single fixed fit: the $(\mathbf e,\mathbf h)\to\mathbf q$ Jacobian has rank $p-r$ with every hardness column a scalar multiple of the corresponding electronegativity column, so a per-type QEq Fisher/Gauss-Newton block is structurally singular along the hardness directions and a uniform electronegativity shift, not merely ill-conditioned. Hardness only becomes identifiable when shared coefficients are expected to transfer to molecules with a different net-charge constraint structure than the one used to fit them. See the full derivation in [[wiki/answers/qeq-per-type-electronegativity-hardness-redundancy]].

### Atom-type features and bounded coefficients

Let $p$ be the number of selected shared charge parameters and $d$ the number of selected atom types. FFRefine builds a one-hot feature matrix

$$
X\in\{0,1\}^{p\times d}.
$$

The electronegativity and hardness vectors are

$$
\mathbf e
=
\mathbf e^0+X\mathbf c_e,
$$

$$
\mathbf h
=
\mathbf h^0\odot
\exp(X\mathbf c_h),
$$

where $\mathbf h^0>0$. The exponential ensures $h_j>0$.

The optimizer does not manipulate $\mathbf c_e$ and $\mathbf c_h$ directly. Each coefficient is obtained from an unconstrained latent through an epoch-local logistic interval:

$$
c(\phi)
=
c_{\min}
+(c_{\max}-c_{\min})\sigma(\phi),
\qquad
\sigma(\phi)=\frac{1}{1+e^{-\phi}}.
$$

Hence

$$
\frac{dc}{d\phi}
=
(c_{\max}-c_{\min})
\sigma(\phi)\left[1-\sigma(\phi)\right].
$$

The intervals are rebuilt around the accepted epoch-start values. This makes the bounds a local trust region rather than permanent global limits.

### Multiplicity-aware constrained energy

One physical parameter may be shared by several equivalent atoms. Let $q_j$ be the charge value of shared parameter $j$, and let

$$
A_{gj}
=
\text{number of occurrences of charge parameter }j
\text{ in constraint group }g.
$$

Then the molecular charge constraints are

$$
A\mathbf q=\mathbf Q.
$$

Define the total multiplicity

$$
m_j=\sum_gA_{gj},
\qquad
D=\operatorname{diag}(m_1,\ldots,m_p),
$$

and the normalized constraint matrix

$$
\overline A=AD^{-1}.
$$

The implemented solve is equivalent to minimizing the multiplicity-weighted QEq energy

$$
\boxed{
E(\mathbf q)
=
\sum_{j=1}^p
m_j\left(e_jq_j+\frac12h_jq_j^2\right)
}
$$

subject to $A\mathbf q=\mathbf Q$. Multiplicity is essential: if one shared parameter represents two equivalent hydrogen atoms, both atoms contribute to the molecular charge and to the quadratic QEq energy.

Using the Lagrangian

$$
\mathcal L(\mathbf q,\boldsymbol\lambda)
=
E(\mathbf q)
-
\boldsymbol\lambda^T(A\mathbf q-\mathbf Q),
$$

stationarity gives

$$
D(\mathbf e+H\mathbf q)-A^T\boldsymbol\lambda=0,
\qquad
H=\operatorname{diag}(\mathbf h).
$$

Because $D^{-1}A^T=\overline A^T$,

$$
\mathbf q
=
H^{-1}\left(\overline A^T\boldsymbol\lambda-\mathbf e\right).
$$

Substitution into the constraints produces the small linear system

$$
\boxed{
\left(AH^{-1}\overline A^T\right)\boldsymbol\lambda
=
\mathbf Q+AH^{-1}\mathbf e.
}
$$

FFRefine solves this system and then recovers $\mathbf q$ from the previous equation. By construction,

$$
A\mathbf q=\mathbf Q.
$$

At the first epoch, FFRefine sets

$$
\mathbf h^0=\mathbf 1,
\qquad
\mathbf e^0=-\mathbf q^{\,0},
\qquad
\mathbf c_e=\mathbf c_h=\mathbf 0,
$$

so the QEq map reproduces the force field's starting charges, subject to the configured charge constraints.

### Analytic QEq Jacobian

The optimizer needs charge derivatives, not only charge values. Write

$$
R=H^{-1},
\qquad
G=AR\overline A^T,
\qquad
\mathbf b=\mathbf Q+AR\mathbf e,
$$

so that

$$
\boldsymbol\lambda=G^{-1}\mathbf b,
\qquad
\mathbf q=R(\overline A^T\boldsymbol\lambda-\mathbf e).
$$

For any latent coordinate $\phi_a$,

$$
dR=-R(dH)R,
$$

$$
dG=A(dR)\overline A^T,
$$

$$
d\mathbf b
=
A\left[(dR)\mathbf e+R(d\mathbf e)\right],
$$

$$
d\boldsymbol\lambda
=
G^{-1}
\left(d\mathbf b-(dG)\boldsymbol\lambda\right),
$$

and finally

$$
\boxed{
d\mathbf q
=
(dR)(\overline A^T\boldsymbol\lambda-\mathbf e)
+
R\left(\overline A^Td\boldsymbol\lambda-d\mathbf e\right).
}
$$

These derivatives obey

$$
A\,d\mathbf q=0,
$$

so infinitesimal optimizer steps preserve each molecular net charge. FFRefine assembles these columns into the QEq part of

$$
J(\phi)=\frac{\partial\theta}{\partial\phi}.
$$

The other trainable physical parameters use independent logistic maps. Double-exponential $\alpha$ and $\beta$ bounds are clipped so that the physical interaction parameter $\alpha$ remains greater than $\beta$. That interaction parameter named `alpha` is unrelated to the loss-family coefficient $\alpha_f$ discussed above.

### QEq regularization

FFRefine adds

$$
L_{\mathrm{QEq}}
=
\frac{\lambda_e}{2}\lVert\mathbf c_e\rVert^2
+
\frac{\lambda_h}{2}\lVert\mathbf c_h\rVert^2.
$$

Its latent gradient includes the logistic derivatives:

$$
\nabla_\phi L_{\mathrm{QEq}}
=
\lambda_e
\left(\mathbf c_e\odot
\frac{\partial\mathbf c_e}{\partial\phi}\right)
+
\lambda_h
\left(\mathbf c_h\odot
\frac{\partial\mathbf c_h}{\partial\phi}\right),
$$

with the two terms placed in their respective latent blocks. This regularizer penalizes the absolute QEq feature coefficients relative to their zero-coefficient reference; it does not penalize only the change made in the current epoch.

Because the per-type hardness directions are structurally null for any loss built only from the resulting charges (see above), this $L_2$ regularizer is also what keeps the hardness latents numerically bounded; it does not by itself make those directions informative, and the stabilized Fisher eigensystem used by the optimizer step below should still be expected to carry a near-zero eigenvalue block attributable to hardness and the uniform-electronegativity-shift gauge. [[wiki/answers/qeq-per-type-electronegativity-hardness-redundancy]]

## How every gradient and metric is put into one coordinate system

Suppose replay produces an $N_t\times N_\theta$ matrix of target gradients

$$
G_\theta=
\begin{bmatrix}
(\nabla_\theta y_1)^T\\
\vdots\\
(\nabla_\theta y_{N_t})^T
\end{bmatrix}.
$$

The latent target gradients are

$$
\boxed{
G_\phi=G_\theta J.
}
$$

Consequently,

$$
\nabla_\phi L
=
G_\phi^T
\frac{\partial L}{\partial\mathbf y}
+
\nabla_\phi L_{\mathrm{QEq}}.
$$

For multiple thermodynamic legs, FFRefine makes a stable union of physical and latent parameter names. A leg contributes only to names that it contains. Shared names identify the same global latent and couple the legs.

For leg $\ell$ and physical thermodynamic state $s$, the physical empirical Fisher is the state-normalized score covariance

$$
F_{\theta,\ell s}
=
\sum_nW_{n,\ell s}
\left(g_{n,\ell s}-\overline g_{\ell s}\right)
\left(g_{n,\ell s}-\overline g_{\ell s}\right)^T,
$$

where

$$
\overline g_{\ell s}
=
\sum_nW_{n,\ell s}g_{n,\ell s}.
$$

With normalized leg weights $\omega_\ell$ and predeclared state weights $\gamma_{\ell s}$, FFRefine constructs the design-averaged conditional metric

$$
\boxed{
\overline F_\theta
=
\sum_\ell\omega_\ell
\sum_s\gamma_{\ell s}F_{\theta,\ell s}.
}
$$

It aligns all objects by physical parameter name and projects both the average and the individual state metrics through the same Jacobian:

$$
\overline F_\phi=J^T\overline F_\theta J,
\qquad
F_{\phi,\ell s}=J^TF_{\theta,\ell s}J.
$$

Thus predictions, loss gradients, proposal geometry, and state-wise KL limits all refer to the same bounded latent coordinates. This conditional metric replaced the earlier frozen-bias joint Fisher, which also included covariance between thermodynamic-state mean scores. That between-state term remains useful as a bias-portability diagnostic but is no longer the primary replay trust-region geometry because state-normalized replay KL does not measure it. [[wiki/answers/ffrefine-kl-divergence-definition-change]] [[wiki/claims/CLM-0039-trust-region-kl-must-match-replay-conditioning]]

## Current optimizer step and validation gates

Since FFRefine commit `110fe64` (2026-10-07, "Damped Levenberg-Marquardt trust-region step; report-only direction gates"), the parameter-proposal step is a damped Levenberg-Marquardt trust-region step, and the direction gates are report-only (`gate_mode=report`) rather than decisive. On 2026-10-11, this trust-region step combined with weighted-sum gradient aggregation was declared the project's canonical regime, superseding the natural-gradient step as the canonical step; the direction gates, ConFIG aggregation, post-Fisher momentum, the natural-gradient step and its proposal path, loss gates, and the archive KL budget are all decided for removal (not yet implemented in code as of 2026-10-11). The natural-gradient path is still in the code at `110fe64` and is decided for removal (FFR-035 in [[wiki/answers/ffrefine-decision-register]]); whether the trust-region step replaces it in every experiment is not recorded. See [[wiki/answers/ffrefine-current-implementation-status]] and [[wiki/answers/ffrefine-generalist-package-plan-decisions]] for the current status and the planning decisions.

**The mathematical account of the damped Levenberg-Marquardt trust-region step is not yet recorded in SecondBrain.** This is a documentation gap in the wiki, not a claim that no such account exists in the FFRefine codebase, and no trust-region mathematics is asserted here beyond what is stated in this paragraph.

The Fisher-preconditioned natural-gradient step (hard-cut and continuously damped treatments, optional ConFIG aggregation, optional post-Fisher momentum, the KL-bounded replay line search) and the validation-gate regime that this page previously described as current -- "The optimizer, step by step" and "Validation gates and outputs" -- describe only the pre-2026-10-07 state and are kept as a historical record in [[wiki/answers/ffrefine-paper-methods-pre-2026-10-07-optimizer-and-gates]]. The QEq, MBAR, and replay-estimator sections above were last audited at the 2026-09-02, `a3b6aa5`, and `6b20031` audits; no change to them is recorded at `110fe64`.

## Current validation boundary

The defensible implementation claim is that FFRefine is a local replay optimizer capable of testing force-field fine tuning with TSS/MBAR archives. Replay accuracy is conditional on reference-ensemble support; importance reweighting cannot recover missing phase-space regions. [SRC-0018] [SRC-0023]

The scientific claim is narrower but no longer zero. Two prospective reaction-field dielectric-only campaigns demonstrate local accepted-step quality under resimulation. In the first, run `20260901-171027`, two consecutive full-parameter dielectric-only updates reduced paired loss on the next fresh archive, and two final-validation replicas reproduced the best confirmed checkpoint; the final dielectric curve moved toward experiment at all six target temperatures but remained substantially above experiment, and a later archive passed direct dielectric splitting yet failed the predeclared damped-direction cosine gate, so the campaign stopped before convergence. [[wiki/answers/ffrefine-prospective-dielectric-damped-fisher-training]] The higher-KL run `20260902-115818` produced six consecutive paired-confirmed updates (checkpoints 1 through 6), reducing fresh dielectric loss by 50.90% through checkpoint 6, before the operator intentionally stopped the run during epoch 8. [[wiki/claims/CLM-0040-damped-conditional-fisher-dielectric-training-survives-fresh-resimulation]]

This establishes two local multi-update dielectric results under two campaign seeds. It does not establish a generally improved water model, density/RDF/enthalpy preservation, enthalpy trainability, ethanol or hexane improvement, transferability, robust convergence across systems, an optimal damping value, or superiority over AWH, ordinary MBAR workflows, or other Fisher treatments.

## Evidence and provenance

- Frozen-reference replay, observable differentiation, Fisher/KL geometry, and the macro-epoch separation are grounded in [[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]. [SRC-0018]
- State-normalized multistate weighting and its overlap limitations are grounded in [[wiki/sources/SRC-0023-statistically-optimal-analysis-multiple-equilibrium-states-mbar]]. [SRC-0023]
- The constrained QEq fine-tuning context is supported by [[wiki/sources/SRC-0016-fine-tuning-mm-force-fields-to-experimental-free-energies]]. [SRC-0016]
- The QEq functional form's literature origin and the per-type hardness-redundancy result are from [[wiki/sources/SRC-0098-graph-nets-partial-charge-prediction]] and [[wiki/answers/qeq-per-type-electronegativity-hardness-redundancy]] (added 2026-10-07). [SRC-0098]
- Conflict-free gradient aggregation is grounded in [[wiki/sources/SRC-0036-config-towards-conflict-free-training-of-physics-informed]], while the Fisher-whitened adaptation is FFRefine-specific. [SRC-0036]
- Exact target construction, multiplicity-aware QEq algebra, relative-enthalpy and dielectric estimators, and latent Jacobian come from the FFRefine audits recorded in this page's frontmatter. The pre-2026-10-07 state-conditional Fisher implementation, treatment operators, line search, support handling, and experiment defaults from those same audits are kept as a historical record in [[wiki/answers/ffrefine-paper-methods-pre-2026-10-07-optimizer-and-gates]]. The pre-2026-10-07 finite-step ConFIG acceptance behavior, also recorded there, was checked against clean repository HEAD `a3b6aa552faab3b91271a1e7a9cabbc97793978a` (`optimiser.jl`, `backend.jl`, and `test/config_optimiser_checks.jl`).
- The KL correction and treatment interpretation are synthesized from [[wiki/answers/ffrefine-kl-divergence-definition-change]], [[wiki/answers/ffrefine-kl-definition-for-extended-ensemble-training]], and [[wiki/answers/ffrefine-fisher-treatment-operators]].
- The validation boundary is synthesized from [[wiki/answers/ffrefine-average-observable-trainability-validation]], [[wiki/answers/ffrefine-long-archive-target-gradient-convergence]], [[wiki/answers/ffrefine-retrospective-fisher-treatment-development]], and [[wiki/answers/ffrefine-prospective-dielectric-damped-fisher-training]]. No raw sources were consulted for this refresh.
- [[wiki/answers/ffrefine-current-implementation-status]] contains the implementation snapshot (pinned at FFRefine commit `110fe64`, recorded 2026-10-11), [[wiki/answers/ffrefine-decision-register]] records decided and open project decisions, and [[wiki/answers/ffrefine-direction-gates-and-production-policy]] records the direction gates and production policy as they stood at master `6b20031` (superseded). Earlier descriptions in this note remain historical where explicitly tied to the 2026-09-02 audit or dated campaigns; the finite-step ConFIG acceptance description, now in [[wiki/answers/ffrefine-paper-methods-pre-2026-10-07-optimizer-and-gates]], reflects the 2026-09-23 repository HEAD.

## Gaps and open questions

- The prospective dielectric results span two campaign seeds, with two and six confirmed updates respectively; campaign-level success probability and convergence behavior remain unknown.
- Checkpoint 3 is unassessed because the failed next-direction gate suppressed its paired parent comparison.
- It is unknown whether longer continuation, additional independent replicas, or a newly prepared archive is the most efficient response to a failed treated direction.
- No matched prospective hard-cut versus damped comparison has been performed, and $\gamma=0.1$ is not established as optimal.
- Collateral density, RDF, and enthalpy preservation was not established for the final dielectric checkpoint; full experimental enthalpy optimization has not passed fresh validation.
- Tolerance and family-weight choices are engineering decisions and require sensitivity analysis.
- Fisher/KL and ESS thresholds are configured safeguards, not universal guarantees of safe extrapolation.
- Future replay-predicted improvements still require confirmation with new simulation and held-out or collateral observables. [SRC-0018]

## Links

- [[wiki/answers/ffrefine-paper-methods-pre-2026-10-07-optimizer-and-gates]]
- [[wiki/answers/ffrefine-generalist-package-plan-decisions]]
- [[wiki/answers/ffrefine-prospective-dielectric-damped-fisher-training]]
- [[wiki/answers/ffrefine-kl-divergence-definition-change]]
- [[wiki/answers/ffrefine-kl-definition-for-extended-ensemble-training]]
- [[wiki/answers/ffrefine-fisher-treatment-operators]]
- [[wiki/answers/ffrefine-long-archive-target-gradient-convergence]]
- [[wiki/answers/ffrefine-retrospective-fisher-treatment-development]]
- [[wiki/answers/ffrefine-average-observable-trainability-validation]]
- [[wiki/answers/ffrefine-current-implementation-status|FFRefine implementation status (August 20 snapshot)]]
- [[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]]
- [[wiki/concepts/awh-replay-force-field-optimization]]
- [[wiki/concepts/tolerance-normalized-multi-observable-losses]]
- [[wiki/concepts/free-energy-reweighting-for-force-field-fine-tuning]]
- [[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]
- [[wiki/claims/CLM-0039-trust-region-kl-must-match-replay-conditioning]]
- [[wiki/questions/QST-0007-checkpoint-assessment-versus-next-direction-readiness]]
- [[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]
- [[wiki/questions/force-field-training-validation-scope]]
- [[wiki/sources/SRC-0016-fine-tuning-mm-force-fields-to-experimental-free-energies]]
- [[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]
- [[wiki/sources/SRC-0023-statistically-optimal-analysis-multiple-equilibrium-states-mbar]]
- [[wiki/sources/SRC-0036-config-towards-conflict-free-training-of-physics-informed]]
- [[wiki/sources/SRC-0098-graph-nets-partial-charge-prediction]]
- [[wiki/answers/qeq-per-type-electronegativity-hardness-redundancy]]
