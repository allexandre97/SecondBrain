---
type: answer
status: active
created: 2026-07-29
updated: 2026-09-02
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
sources:
  - SRC-0016
  - SRC-0018
  - SRC-0023
  - SRC-0036
sensitivity: public
encryption: none
wiki_pages_used:
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
  - "FFRefine dielectric-only damped-Fisher reaction-field water-temperature run 20260901-171027, completed 2026-09-02"
---

# FFRefine Paper Methods Knowledge Base

## Short answer

FFRefine alternates between simulation and local, replay-only force-field optimization. A simulation macro epoch produces a frozen reference archive at parameters $\theta^{(k)}$. Within that archive, MBAR supplies normalized candidate-state frame weights; those weights produce free energies, ordinary observable means, relative enthalpies, and fluctuation-derived quantities such as the dielectric constant. Their derivatives are assembled into a tolerance-normalized multi-family loss. The physical-parameter gradients and a design-averaged, state-conditional Fisher metric are then projected through a bounded latent parameterization, including a constrained charge-equilibration (QEq) map. A hard-cut or continuously damped Fisher-preconditioned optimizer proposes a small latent displacement, and replay line search tests the displacement against loss, support, per-step empirical KL, and archive-displacement KL without running new molecular dynamics (MD). Supported replay proposals seed the next simulation macro epoch, where new configurations can test whether the predicted improvement survives resampling. [SRC-0018] [SRC-0023]

Checkpoint assessment and readiness to construct another direction are conceptually separate, but the current macro pipeline does not yet keep them fully separate: a failed next-direction gate can suppress the paired parent comparison for an already simulated checkpoint. This occurred for checkpoint 3 in the first prospective dielectric run, leaving that checkpoint unassessed rather than disproved.

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

finite loss, step, and KL estimates; compliance with the per-proposal empirical conditional-KL limit and cumulative archive-displacement limit; and, for ConFIG-protected components,

$$
L_f(\phi_{t,j})\le L_f(\phi_t)
\quad\text{for every protected }f.
$$

The first accepted scale is used. If all configured scales fail, the replay proposal chain stops.

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

The current pipeline still combines these statuses in `sampling_accepted`. In the first prospective dielectric run, failure of the second status prevented the paired comparison required for the first, so checkpoint 3 remained unassessed and final validation reverted to checkpoint 2. This is a control-flow limitation, not evidence that checkpoint 3 worsened the objective. [[wiki/questions/QST-0007-checkpoint-assessment-versus-next-direction-readiness]]

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
- agreement of the selected treated direction across chronological halves;
- maximum state-conditional quadratic and empirical KL;
- cumulative empirical displacement from the archive-generating parameters.

The current dielectric-only water profile uses a replay/TSS threshold of 1.0 $k_{\mathrm B}T$, TSS standard-error threshold of 0.5 $k_{\mathrm B}T$, minimum local ESS ratio of 0.01, MBAR target and candidate ESS thresholds of 10 with 0.1 retention, Fisher negative-eigenvalue tolerance of $10^{-6}$, a per-proposal maximum conditional-KL target of 0.005, and a maximum empirical archive-displacement KL of 0.1. The selected damped half-directions must have Fisher-metric cosine at least 0.8 and norm ratio between 0.5 and 2. The direct dielectric family uses its own split diagnostic. Thresholds for density, RDF, enthalpy, and other experiment profiles are configuration-specific rather than universal properties of FFRefine.

History records validity diagnostics, replay uncertainty, ESS, family losses, normalized residuals, line-search trials, conditional and joint-KL diagnostics, treated-direction diagnostics, aggregation diagnostics, physical and latent parameter snapshots, QEq state, selected target curves, memory use, and checkpoints. The prospective run also persisted fresh paired comparisons and validation-replica results. These records are project evidence; their interpretation remains limited by the sampling and experimental design.

## Current validation boundary

The defensible implementation claim is that FFRefine is a local replay optimizer capable of testing force-field fine tuning with TSS/MBAR archives. Replay accuracy is conditional on reference-ensemble support; importance reweighting cannot recover missing phase-space regions. [SRC-0018] [SRC-0023]

The scientific claim is narrower but no longer zero. In reaction-field run `20260901-171027`, two consecutive full-parameter dielectric-only updates reduced paired loss on the next fresh archive, and two final-validation replicas reproduced the best confirmed checkpoint. The final dielectric curve moved toward experiment at all six target temperatures, but remained substantially above experiment. A later archive passed direct dielectric splitting yet failed the predeclared damped-direction cosine gate, so the campaign stopped before convergence. [[wiki/answers/ffrefine-prospective-dielectric-damped-fisher-training]]

This establishes one local multi-update dielectric result under one campaign seed. It does not establish a generally improved water model, density/RDF/enthalpy preservation, enthalpy trainability, ethanol or hexane improvement, transferability, robust convergence across systems, an optimal damping value, or superiority over AWH, ordinary MBAR workflows, or other Fisher treatments.

## Evidence and provenance

- Frozen-reference replay, observable differentiation, Fisher/KL geometry, and the macro-epoch separation are grounded in [[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]. [SRC-0018]
- State-normalized multistate weighting and its overlap limitations are grounded in [[wiki/sources/SRC-0023-statistically-optimal-analysis-multiple-equilibrium-states-mbar]]. [SRC-0023]
- The constrained QEq fine-tuning context is supported by [[wiki/sources/SRC-0016-fine-tuning-mm-force-fields-to-experimental-free-energies]]. [SRC-0016]
- Conflict-free gradient aggregation is grounded in [[wiki/sources/SRC-0036-config-towards-conflict-free-training-of-physics-informed]], while the Fisher-whitened adaptation is FFRefine-specific. [SRC-0036]
- Exact target construction, multiplicity-aware QEq algebra, relative-enthalpy and dielectric estimators, latent Jacobian, current state-conditional Fisher implementation, treatment operators, line search, support handling, and experiment defaults come from the FFRefine audits recorded in this page's frontmatter.
- The KL correction and treatment interpretation are synthesized from [[wiki/answers/ffrefine-kl-divergence-definition-change]], [[wiki/answers/ffrefine-kl-definition-for-extended-ensemble-training]], and [[wiki/answers/ffrefine-fisher-treatment-operators]].
- The validation boundary is synthesized from [[wiki/answers/ffrefine-average-observable-trainability-validation]], [[wiki/answers/ffrefine-long-archive-target-gradient-convergence]], [[wiki/answers/ffrefine-retrospective-fisher-treatment-development]], and [[wiki/answers/ffrefine-prospective-dielectric-damped-fisher-training]]. No raw sources were consulted for this refresh.
- [[wiki/answers/ffrefine-current-implementation-status]] is an August 20 snapshot. Its then-current defaults and statement that fresh trainability was unresolved are superseded here by the September audit and prospective-result pages.

## Gaps and open questions

- The prospective dielectric result has one campaign seed and two confirmed updates; its campaign-level success probability and convergence behavior are unknown.
- Checkpoint 3 is unassessed because the failed next-direction gate suppressed its paired parent comparison.
- It is unknown whether longer continuation, additional independent replicas, or a newly prepared archive is the most efficient response to a failed treated direction.
- No matched prospective hard-cut versus damped comparison has been performed, and $\gamma=0.1$ is not established as optimal.
- Collateral density, RDF, and enthalpy preservation was not established for the final dielectric checkpoint; full experimental enthalpy optimization has not passed fresh validation.
- Tolerance and family-weight choices are engineering decisions and require sensitivity analysis.
- Fisher/KL and ESS thresholds are configured safeguards, not universal guarantees of safe extrapolation.
- Future replay-predicted improvements still require confirmation with new simulation and held-out or collateral observables. [SRC-0018]

## Links

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
