---
type: answer
status: active
created: 2026-08-29
updated: 2026-09-02
question: "Which KL divergence should FFRefine use when extended-ensemble simulations train force-field parameters across temperature or alchemical ladders?"
answer_status: answered
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/molecular-simulation/free-energy
  - research/adaptive-sampling
  - research/statistics/monte-carlo
tags:
  - ffrefine
  - extended-ensemble
  - force-field-optimization
  - fisher-information
  - natural-gradient
  - kl-divergence
  - trust-region
  - state-conditioning
  - temperature-ladder
  - alchemical-transformation
  - replay-support
related:
  - "[[wiki/answers/ffrefine-prospective-dielectric-damped-fisher-training]]"
  - "[[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]]"
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
  - "[[wiki/answers/ffrefine-retrospective-fisher-treatment-development]]"
  - "[[wiki/claims/CLM-0039-trust-region-kl-must-match-replay-conditioning]]"
  - "[[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]"
  - "[[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]"
sources:
  - SRC-0005
  - SRC-0006
  - SRC-0007
  - SRC-0009
  - SRC-0018
  - SRC-0023
sensitivity: public
encryption: none
wiki_pages_used:
  - "[[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]]"
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
  - "[[wiki/concepts/times-square-sampling]]"
  - "[[wiki/concepts/tss-implementation-patterns]]"
  - "[[wiki/concepts/multistate-bennett-acceptance-ratio]]"
  - "[[wiki/answers/ffrefine-retrospective-fisher-treatment-development]]"
  - "[[wiki/claims/CLM-0039-trust-region-kl-must-match-replay-conditioning]]"
raw_sources_consulted: []
project_evidence:
  - "FFRefine retrospective Fisher-treatment campaign completed 2026-08-28"
  - "FFRefine within-state/between-state Fisher decomposition completed 2026-08-29"
  - "FFRefine dielectric-only damped-Fisher reaction-field water-temperature run 20260901-171027, completed 2026-09-02"
---

# KL Definition for Extended-Ensemble Force-Field Training

## Decision

For FFRefine's usual scientific objective, the fundamental trust-region objects should be the state-conditional candidate-to-reference divergences

$$
D_s(\theta'\Vert\theta)
=
D_{\mathrm{KL}}
\left(
p_{\theta'}(x\mid s)
\Vert
p_\theta(x\mid s)
\right),
$$

where $s$ is a physical thermodynamic state such as temperature or alchemical lambda, $x$ is the molecular configuration, and $\theta$ denotes force-field parameters.

These state-conditional divergences should be used in two related but distinct ways:

1. their predeclared weighted average should define the natural-gradient geometry;
2. their maximum, together with state-wise ESS, should limit and validate finite replay steps.

The KL of the joint extended ensemble under a frozen old bias is also meaningful, but it answers a different question. It should normally be reported as a bias-portability or transient-sampling diagnostic rather than used as FFRefine's primary optimisation geometry.

This is a design conclusion obtained by combining the sampler/optimizer separation in SRC-0018 with the prescribed-state-marginal structure of AWH and TSS [SRC-0005] [SRC-0006] [SRC-0007] [SRC-0009], the state-normalized replay estimators supplied by MBAR [SRC-0023], and FFRefine's 2026-08-29 Fisher-conditioning evidence. It has not yet been prospectively compared against the current mixture-Fisher optimiser.

## Probability model

Let $\gamma_s$ be the desired probability of thermodynamic state $s$. In an enhanced-sampling calculation this state density is chosen by the algorithm or investigator; it is not an observable predicted by the force field. The physical conditional distribution is

$$
p_\theta(x\mid s)
=
\frac{\exp[-u_{\theta,s}(x)]}{Z_{\theta,s}},
$$

where $u_{\theta,s}$ is the dimensionless reduced potential. The designed joint ensemble is therefore

$$
\pi_\theta(s,x)
=
\gamma_s p_\theta(x\mid s).
$$

For two general joint distributions, the KL chain rule gives

$$
D_{\mathrm{KL}}(\pi_{\theta'}\Vert\pi_\theta)
=
D_{\mathrm{KL}}(\gamma'\Vert\gamma)
+
\sum_s\gamma'_s
D_{\mathrm{KL}}
\left(
p_{\theta'}(x\mid s)
\Vert
p_\theta(x\mid s)
\right).
$$

Under the FFRefine design, the enhanced-sampling state density is held fixed, so $\gamma'=\gamma$ and the marginal term vanishes. The resulting designed-ensemble divergence is

$$
D_{\mathrm{design}}(\theta'\Vert\theta)
=
\sum_s\gamma_s D_s(\theta'\Vert\theta).
$$

Thus the appropriate joint probability model contains the same prescribed state marginal before and after the force-field update. AWH or TSS may need to update its free-energy estimates or bias to realise that marginal after resimulation, but this adaptation does not change the scientific ensemble being compared. [SRC-0005] [SRC-0006] [SRC-0007] [SRC-0009]

## Direction of the finite KL

For replay support, use candidate-to-reference KL:

$$
D_s(\theta'\Vert\theta)
=
\mathbb E_{p_{\theta'}(x\mid s)}
\left[
\log\frac{p_{\theta'}(x\mid s)}{p_\theta(x\mid s)}
\right].
$$

This direction penalizes candidate probability mass in regions that have little reference probability and is therefore aligned with asking whether a frozen reference archive can represent the candidate. The two KL directions have the same Fisher curvature to second order, but they differ at finite step size. Empirical KL cannot reveal completely unsampled candidate regions, so it must remain paired with ESS, coverage diagnostics, and fresh simulation. [SRC-0018] [[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]

## Conditional Fisher geometry

Let the latent parameter coordinate be $\phi$ and define the reduced-potential derivative

$$
h_s(x)=\nabla_\phi u_{\theta,s}(x).
$$

The score of the normalized conditional distribution is

$$
\nabla_\phi\log p_\theta(x\mid s)
=
-\left(h_s(x)-\mu_s\right),
\qquad
\mu_s=\mathbb E_{p_\theta(x\mid s)}[h_s(x)].
$$

The state-conditional Fisher matrix is consequently

$$
F_s
=
\operatorname{Cov}_{p_\theta(x\mid s)}[h_s(x)].
$$

For a small displacement $\Delta\phi$,

$$
D_s
=
\frac12\Delta\phi^\mathsf{T}F_s\Delta\phi
+O(\lVert\Delta\phi\rVert^3),
$$

and the designed-ensemble Fisher is

$$
F_{\mathrm{cond}}
=
\sum_s\gamma_sF_s.
$$

This matrix should define the orientation of FFRefine's natural-gradient proposal. State-wise centering is essential: it makes the local metric invariant to a configuration-independent reduced-energy offset within a thermodynamic state, as every normalized conditional distribution must be.

## Why the frozen-bias joint KL is different

Suppose the bias learned at $\theta$ is frozen while the force field changes to $\theta'$. The resulting candidate joint ensemble generally has a new state marginal $\widetilde\gamma_{\theta'}$, even if the old marginal was $\gamma$. Its KL decomposes as

$$
D_{\mathrm{KL}}
\left(
\widetilde\pi^{b_\theta}_{\theta'}
\Vert
\widetilde\pi^{b_\theta}_{\theta}
\right)
=
D_{\mathrm{KL}}(\widetilde\gamma_{\theta'}\Vert\gamma)
+
\sum_s\widetilde\gamma_{\theta',s}
D_s(\theta'\Vert\theta).
$$

Its local Fisher is the covariance of the uncentered state-labelled score over the extended-ensemble mixture. The law of total covariance gives

$$
F_{\mathrm{mix}}
=
\underbrace{
\sum_s\gamma_s
\operatorname{Cov}_{p_\theta(x\mid s)}[h_s(x)]
}_{F_{\mathrm{within}}}
+
\underbrace{
\operatorname{Cov}_{s\sim\gamma}(\mu_s)
}_{F_{\mathrm{between}}}.
$$

The between-state term measures how a parameter update changes relative mean reduced energies and therefore state occupancy under the old frozen bias. It is not a within-state configurational-overlap cost.

The frozen-bias joint KL is useful for:

- predicting how portable the old TSS or AWH bias is after a parameter update;
- anticipating transient state-occupancy distortion before adaptation catches up;
- diagnosing parity or mixing problems during resimulation;
- studying joint force-field and bias optimisation, if that becomes an explicit objective.

It should become the primary trust-region definition only when preserving the stationary distribution under a frozen bias is itself the scientific or algorithmic goal.

## Optimisation and acceptance policy

A weighted average alone can hide a poorly supported state. FFRefine should retain the full vector of $D_s$ values rather than reducing it immediately to one scalar.

For proposal orientation, use

$$
F_{\mathrm{cond}}
=
\sum_s\gamma_sF_s.
$$

For local step control, evaluate

$$
\widehat D_s(\Delta\phi)
=
\frac12\Delta\phi^\mathsf{T}F_s\Delta\phi,
\qquad
\widehat D_{\max}
=
\max_s\widehat D_s.
$$

A proposed direction can be scaled to a worst-state local budget $\epsilon$ using

$$
\alpha
=
\min\left(
1,
\sqrt{
\frac{\epsilon}{\max_s\widehat D_s(\Delta\phi)}
}
\right).
$$

The replay line search should then compute state-normalized empirical candidate-to-reference KL and ESS for every state and accept only if all mandatory state-wise gates pass. This creates a coherent division of labour:

- the weighted conditional KL defines the global natural-gradient geometry;
- the maximum conditional KL prevents one state from being sacrificed;
- ESS and coverage test whether the empirical KL estimate is trustworthy;
- fresh simulation tests whether replay improvement transfers to newly sampled data;
- the frozen-bias joint KL predicts bias portability but does not replace conditional support checks.

## Temperature-ladder application

For water-temperature fitting, the definition is

$$
D_{\mathrm{water}}
=
\sum_{T\in\mathcal T}\gamma_T
D_{\mathrm{KL}}
\left(
p_{\theta'}(x\mid T)
\Vert
p_\theta(x\mid T)
\right).
$$

The set $\mathcal T$ must be the complete physical TSS ladder, not only temperatures with experimental targets. Sparse experimental observations affect the objective, whereas the KL trust region protects replay support across every sampled temperature.

For an equally important discrete ladder, normalized uniform $\gamma_T$ is natural. If an irregular ladder approximates an integral over a continuous temperature interval, predeclared quadrature weights may be more appropriate. The weights should be normalized so that adding rungs does not silently change the learning-rate scale.

Experimental target weights and $\gamma_T$ have different meanings. Target weights state which discrepancies matter scientifically; $\gamma_T$ states which physical ensembles the trust region covers. They should not be conflated.

## Alchemical and multi-leg application

For alchemical transformations, lambda is an auxiliary thermodynamic state used to connect endpoint ensembles. For independent legs $\ell$, define

$$
D_{\mathrm{alchemical}}
=
\sum_\ell\omega_\ell
\sum_{s\in\mathcal S_\ell}\gamma_{\ell,s}
D_{\mathrm{KL}}
\left(
p_{\theta'}(x\mid\ell,s)
\Vert
p_\theta(x\mid\ell,s)
\right),
$$

with explicit normalized leg weights $\omega_\ell$. State-wise ceilings should cover all intermediate lambda states because overlap bottlenecks need not occur at the endpoints.

A configuration-independent energy shift at one lambda state changes its normalization and may change a free-energy difference while leaving its conditional distribution unchanged. Its conditional Fisher cost is correctly zero: it creates no configurational reweighting problem. Such directions still require physical parameter bounds, regularisation, objective line search, and fresh validation. The frozen-bias joint Fisher can quantify their immediate occupancy effect, but that effect should not be mislabelled as within-state replay loss.

For windowed TSS, $s$ in these equations is the physical thermodynamic rung. The active window is part of the sampling and replay implementation, not an additional physical target state. Window-local reconstruction and stitching remain necessary to estimate each rung distribution correctly. [SRC-0006]

## Consequences for FFRefine

The recommended implementation should:

1. compute a centered score covariance separately for each physical thermodynamic state;
2. aggregate those matrices using a predeclared normalized state density;
3. retain the per-state matrices or their quadratic forms for worst-state scaling;
4. continue calculating exact state-normalized empirical KL and ESS during line search;
5. log average conditional KL, maximum conditional KL, frozen-bias joint KL, and the within/between Fisher allocation separately;
6. compare the conditional and current mixture geometries retrospectively on existing archives before changing production defaults;
7. validate the selected policy prospectively through replay-controlled updates followed by fresh simulation.

This does not imply that FFRefine's extended-ensemble strategy or earlier results are invalid. The present mixture Fisher measures a legitimate frozen-bias joint perturbation. The problem is that this quantity was used to scale proposals that were then judged by a state-conditional empirical KL, making equal nominal budgets unequal in the validation metric. [[wiki/claims/CLM-0039-trust-region-kl-must-match-replay-conditioning]]

## Retrospective evidence from the corrected backend

The two independent 100 ns reaction-field water archives were reanalysed without regenerating configurations. Observable estimates, target values, and raw gradients were identical to the historical analysis, isolating the change to Fisher geometry and KL scaling.

At 100 ns, the maximum state-conditional quadratic KL was 0.01 for every family and the design-weighted average was 0.0091--0.0096. For those same corrected steps, the frozen-bias joint quadratic was approximately 0.156 for density, 0.010--0.011 for RDF, 0.207--0.314 for enthalpy, and 0.353--0.359 for dielectric. The between-state score-mean term contributed about 94% of the joint value for density, 10--14% for RDF, 96--97% for enthalpy, and 97% for dielectric.

This confirms that the conditioning mismatch was scientifically consequential and target-direction dependent. The corrected Fisher retained six modes instead of five, lowered the physical-coordinate condition estimate from about $6.7\times10^7$ to $1.46\times10^7$, moved enthalpy's 100 ns independent-archive natural-direction cosine from 0.6288 to 0.8143, and moved dielectric from 0.9743 to 0.9955. Density and RDF remained essentially unchanged as reproducibility controls.

The corrected result does not show that the gradients acquired more equilibrium information: the raw gradients are exactly the same. It shows that the conditional geometry maps those gradients into directions that better match the probability distribution controlled by replay. Historical finite-step treatment results remain properties of the old proposals and must not be used as validation of the corrected proposal vectors.

## Prospective evidence from the corrected backend

Dielectric-only reaction-field run `20260901-171027` used the recommended design-weighted conditional Fisher for direction geometry, maximum state-conditional quadratic and empirical KL for step safety, and exact state-normalized replay diagnostics. With damped treatment $\gamma=0.1$, two consecutive full-parameter updates reduced loss on the next fresh macro archives with paired intervals below zero. Two independent final-validation replicas reproduced the best confirmed loss. [[wiki/answers/ffrefine-prospective-dielectric-damped-fisher-training]]

The proposal chain also exercised the cumulative constraint correctly. Individual accepted steps used maximum empirical conditional KL near 0.005. Four aligned steps produced archive-to-candidate KL near 0.077--0.080, while a fifth would have produced 0.111--0.113 and was rejected against the 0.1 ceiling. This is direct evidence that the corrected KL can function as an operational trust region during closed-loop temperature-ladder training.

## What remains unresolved

- Conditional-Fisher damping has now produced two fresh-confirmed dielectric improvements in one prospective campaign; enthalpy and campaign-to-campaign reproducibility remain unresolved.
- The enthalpy conditional-Fisher direction passes only at the 100 ns endpoint and fails both 100 ns chronological-half comparisons; the probability that this endpoint crossing repeats is unknown.
- The best aggregation of state-wise ceilings may depend on whether strict maximum control is too sensitive to noisy low-support states.
- A practical policy may need both a hard maximum and a robust high-quantile diagnostic when the ladder is very large or continuous.
- Conditional KL and ESS diagnose represented support; neither can detect candidate regions absent from the reference archive.
- The relative value of frozen-bias portability for reducing the cost of the next adaptive epoch remains an empirical question.

## Links

- [[wiki/answers/ffrefine-prospective-dielectric-damped-fisher-training]]
- [[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]]
- [[wiki/concepts/awh-replay-force-field-optimization]]
- [[wiki/answers/ffrefine-retrospective-fisher-treatment-development]]
- [[wiki/claims/CLM-0039-trust-region-kl-must-match-replay-conditioning]]
- [[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]
- [[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]
- [[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]
- [[wiki/sources/SRC-0023-statistically-optimal-analysis-multiple-equilibrium-states-mbar]]
