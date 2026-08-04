---
type: answer
status: active
created: 2026-07-29
updated: 2026-07-29
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
  - "[[wiki/answers/ffrefine-current-implementation-status]]"
  - "[[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]]"
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
  - "[[wiki/concepts/tolerance-normalized-multi-observable-losses]]"
  - "[[wiki/concepts/free-energy-reweighting-for-force-field-fine-tuning]]"
  - "[[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]"
  - "[[wiki/questions/force-field-training-validation-scope]]"
  - "[[wiki/sources/SRC-0016-fine-tuning-mm-force-fields-to-experimental-free-energies]]"
  - "[[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]"
  - "[[wiki/sources/SRC-0036-config-towards-conflict-free-training-of-physics-informed]]"
sources:
  - SRC-0016
  - SRC-0018
  - SRC-0036
sensitivity: public
encryption: none
wiki_pages_used:
  - "[[wiki/answers/ffrefine-current-implementation-status]]"
  - "[[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]]"
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
  - "[[wiki/concepts/tolerance-normalized-multi-observable-losses]]"
  - "[[wiki/sources/SRC-0016-fine-tuning-mm-force-fields-to-experimental-free-energies]]"
  - "[[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]"
  - "[[wiki/sources/SRC-0036-config-towards-conflict-free-training-of-physics-informed]]"
raw_sources_consulted: []
wiki_pages_updated:
  - "[[wiki/index]]"
  - "[[wiki/log]]"
project_evidence:
  - "FFRefine code audit on 2026-07-29 against optimiser.jl, replay.jl, gradients.jl, parameterization.jl, validity.jl, backend.jl, solvation_pipeline.jl, water_temperature.jl, and focused tests"
---

# FFRefine Paper Methods Knowledge Base

## Short answer

FFRefine alternates between simulation and local, replay-only force-field optimization. A simulation macro epoch produces a frozen reference archive at parameters $\theta^{(k)}$. Within that archive, MBAR supplies normalized candidate-state frame weights; those weights produce free energies, ordinary observable means, and fluctuation-derived quantities such as the dielectric constant. Their derivatives are assembled into a tolerance-normalized multi-family loss. The physical-parameter gradients and Fisher matrix are then projected through a bounded latent parameterization, including a constrained charge-equilibration (QEq) map. A Fisher-preconditioned optimizer proposes a small latent displacement, and replay line search tests that displacement without running new molecular dynamics (MD). An accepted, supported proposal becomes the starting point for the next simulation macro epoch. [SRC-0018]

This is an implemented method-development framework, not yet evidence that water density, radial distribution functions (RDFs), dielectric constants, or transferability have improved in production.

## Scope and notation

The two experiment surfaces are:

- ethanol solvation, represented as solvated and vacuum alchemical legs;
- water-temperature fitting, represented as one temperature ladder.

As of the 2026-07-29 audit, water training actively includes density and RDF targets. Dielectric prediction and differentiation are implemented, but dielectric targets are commented out of `TRAINING_TARGETS`, split validation, monitored predictions, and curve writing.

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

FFRefine constructs the system and its thermodynamic-state ladder. Water uses temperature states; ethanol solvation uses alchemical states in each thermodynamic leg. Times Square Sampling (TSS) is run adaptively until its free-energy uncertainty criterion passes or the allowed adaptive extension is exhausted.

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

For the current water configuration, density and RDF both have $\alpha_f=1$. Density targets use unit $w_i$. RDF weights distribute within-family mass by structural region: 0.6 to first-shell bins, 0.3 to second-shell bins, and 0.1 to tail bins for each pair type, divided across the bins in each region.

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

The water optimizer currently uses $\delta=3$ and $c=2$. Inside the quadratic region, $c=2$ makes $c\,h_\delta(r)=r^2$, so the Huber loss matches MSE near the target and becomes linear only for $|r|>3$.

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

For each leg, the physical empirical Fisher is a weighted score covariance,

$$
F_\theta^{(\ell)}
=
\sum_nW_n^{(\ell)}
\left(g_n^{(\ell)}-\overline g^{(\ell)}\right)
\left(g_n^{(\ell)}-\overline g^{(\ell)}\right)^T.
$$

FFRefine aligns these matrices by physical parameter name and adds them:

$$
F_\theta=\sum_\ell F_\theta^{(\ell)}.
$$

It then projects the metric through the same Jacobian:

$$
\boxed{
F_\phi=J^TF_\theta J.
}
$$

Thus predictions, loss gradients, and the KL metric all refer to the same bounded latent coordinates.

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

### 2. Stabilize and factorize the Fisher matrix

First add diagonal regularization:

$$
F_r=F_\phi+\lambda_FI.
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

Only eigenmodes with

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

is the retained, regularized Fisher pseudoinverse, while $W$ also maps between latent coordinates and the retained Fisher-whitened space.

### 3. Construct a descent direction

For weighted-sum aggregation, the raw natural-gradient direction is

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

If ConFIG is enabled, FFRefine instead protects the active family components. Let

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

Optional first-moment momentum reuses the previous **accepted latent displacement**, not an Adam-style raw-gradient moment. It is projected into the current retained Fisher step space and kept only if its Fisher inner-product alignment with the new direction is positive. Under ConFIG, the coefficient is reduced or reset if mixing would violate a protected family's descent condition.

The resulting displacement is first clipped to the configured Euclidean norm limit. FFRefine then estimates the local KL change as

$$
\widehat D_{\mathrm{KL}}
=
\frac12\Delta\phi^TF_r\Delta\phi.
$$

If this exceeds the target $\kappa$,

$$
\Delta\phi
\leftarrow
\Delta\phi
\sqrt{
\frac{\kappa}
{\widehat D_{\mathrm{KL}}}
}.
$$

The water configuration currently uses $\kappa=0.02$. The Fisher/KL interpretation is local: it controls the quadratic approximation, not the exact finite-step distribution shift. [SRC-0018]

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

No MD is run inside the line search. The central acceptance checks require:

$$
L(\phi_{t,j})
\le
L(\phi_t)+\Delta L_{\max},
$$

finite loss, step, and KL estimate, and, for ConFIG-protected components,

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

When the replay chain ends, the resulting physical parameters seed the next macro epoch. New MD then determines whether the replay-predicted improvement survives resampling. After the configured optimization epochs, FFRefine performs a final validation-only epoch.

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
- Fisher eigenvalue diagnostics.

The water configuration currently uses a replay/TSS threshold of 1.0 $k_{\mathrm B}T$, TSS standard-error threshold of 0.5 $k_{\mathrm B}T$, minimum local ESS ratio of 0.01, MBAR target and candidate ESS thresholds of 10 with 0.1 retention, split-density tolerance of 0.005 kg/L, split-RDF tolerance of 0.10, Fisher negative-eigenvalue tolerance of $10^{-6}$, and KL target of 0.02.

History records validity diagnostics, replay uncertainty, ESS, family losses, normalized residuals, line-search trials, aggregation diagnostics, physical and latent parameter snapshots, QEq state, density/RDF curves, memory use, and checkpoints. These records are implementation evidence, not scientific validation.

## Current validation boundary

The defensible claim is that FFRefine implements a local replay optimizer capable of testing force-field fine tuning with TSS/MBAR archives. Replay accuracy is conditional on reference-ensemble support; importance reweighting cannot recover missing phase-space regions. [SRC-0018] [SRC-0016]

The following remain unvalidated: production improvement of the density/RDF balance, dielectric improvement, transferability, robust convergence across systems, and superiority over AWH or ordinary MBAR sampling. In particular, the dielectric mathematics above describes implemented but currently disabled target support, not a completed dielectric-training result.

## Evidence and provenance

- Frozen-reference replay, observable differentiation, Fisher/KL geometry, and the macro-epoch separation are grounded in [[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]. [SRC-0018]
- The constrained QEq fine-tuning context is supported by [[wiki/sources/SRC-0016-fine-tuning-mm-force-fields-to-experimental-free-energies]]. [SRC-0016]
- Conflict-free gradient aggregation is grounded in [[wiki/sources/SRC-0036-config-towards-conflict-free-training-of-physics-informed]], while the Fisher-whitened adaptation is FFRefine-specific. [SRC-0036]
- Exact target construction, multiplicity-aware QEq algebra, dielectric sufficient statistics, latent Jacobian, Fisher factorization, line search, support handling, and current configuration status come from the 2026-07-29 FFRefine code audit recorded in this page's frontmatter.

## Gaps and open questions

- Dielectric targets are implemented but disabled, so the full fluctuation-gradient path still needs production validation.
- Tolerance and family-weight choices are engineering decisions and require sensitivity analysis.
- Fisher/KL and ESS thresholds are configured safeguards, not universal guarantees of safe extrapolation.
- Replay-predicted improvements require confirmation with new simulation and held-out observables.

## Links

- [[wiki/answers/ffrefine-current-implementation-status]]
- [[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]]
- [[wiki/concepts/awh-replay-force-field-optimization]]
- [[wiki/concepts/tolerance-normalized-multi-observable-losses]]
- [[wiki/concepts/free-energy-reweighting-for-force-field-fine-tuning]]
- [[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]
- [[wiki/questions/force-field-training-validation-scope]]
- [[wiki/sources/SRC-0016-fine-tuning-mm-force-fields-to-experimental-free-energies]]
- [[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]
- [[wiki/sources/SRC-0036-config-towards-conflict-free-training-of-physics-informed]]
