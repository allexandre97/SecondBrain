---
type: concept
status: active
created: 2026-06-29
updated: 2026-07-31
areas:
  - research
categories:
  - research/adaptive-sampling
  - research/molecular-simulation/free-energy
  - research/statistics/monte-carlo
tags:
  - adaptive-sampling
  - simulated-tempering
  - resource-allocation
  - math-heavy
related:
  - "[[wiki/sources/SRC-0010-rethinking-metadynamics-opes]]"
  - "[[wiki/sources/SRC-0011-opes-supporting-information]]"
  - "[[wiki/sources/SRC-0013-ladybugs-lambda-dynamics]]"
  - "[[wiki/concepts/on-the-fly-probability-enhanced-sampling]]"
  - "[[wiki/concepts/lambda-dynamics-with-bias-updated-gibbs-sampling]]"
  - "[[wiki/sources/SRC-0007-improving-efficiency-extended-ensemble-awh]]"
  - "[[wiki/sources/SRC-0008-awh-free-energy-landscapes]]"
  - "[[wiki/sources/SRC-0009-awh-alchemical-free-energy]]"
  - "[[wiki/concepts/accelerated-weight-histogram-method]]"
  - "[[wiki/sources/SRC-0005-times-square-sampling-free-energy]]"
  - "[[wiki/sources/SRC-0006-times-square-sampling-supplement]]"
  - "[[wiki/concepts/times-square-sampling]]"
  - "[[wiki/concepts/free-energy-estimation]]"
  - "[[wiki/concepts/tss-implementation-patterns]]"
  - "[[wiki/sources/SRC-0074-convergence-is-not-correctness-context-dependent-performance-of]]"
  - "[[wiki/concepts/enhanced-sampling-validation]]"
sources:
  - SRC-0010
  - SRC-0011
  - SRC-0013
  - SRC-0007
  - SRC-0008
  - SRC-0009
  - SRC-0005
  - SRC-0006
  - SRC-0074
sensitivity: public
encryption: none
---

# Adaptive Enhanced Sampling

## Summary

Adaptive enhanced sampling uses information learned during a simulation to steer future sampling, with the goal of improving exploration or reducing estimator variance. [SRC-0005]

## Key Points

- Enhanced sampling methods such as replica exchange and simulated tempering help sample multimodal distributions by introducing a family of overlapping intermediate distributions. [SRC-0005, introduction]
- Their efficiency depends on the free energy landscape and on how computational resources are distributed among rungs, but that landscape is usually unknown before sampling. [SRC-0005, introduction]
- AWH is an adaptive extended-ensemble method that learns free-energy weights from conditional transition-probability histograms while sampling. [SRC-0007, section II] [SRC-0008, section II.A]
- OPES adapts a bias by reconstructing the probability distribution in collective-variable space and then targeting a chosen distribution. [SRC-0010]
- LaDyBUGS adapts scalar biases during discrete Gibbs-sampler lambda-dynamics so multiple alchemical ligand states are sampled smoothly in one simulation. [SRC-0013]
- TSS adapts the rung-sampling distribution using current estimates, enabling resource allocation to change during the run. [SRC-0005, section 2.2]
- Visit control is a transient adaptive mechanism that pushes sampling toward under-visited rungs and mitigates slow convergence caused by poor initial free energy guesses. [SRC-0005, section 2.2.1]
- Windowing is a locality mechanism: it restricts updates to overlapping parameter-space neighborhoods where distributions are expected to have useful overlap. [SRC-0005, section 3.1]
- Adaptive sampling must preserve convergence guarantees; SRC-0005 and SRC-0006 state assumptions and proof structure for convergence despite adaptation. [SRC-0005, section 2.2.4] [SRC-0006, section 5]
- In realistic free-energy landscapes, internal stability can fail to detect parameter- or initialization-dependent bias. A five-system comparison therefore recommends separating self-convergence from cross-method or extended-reference validation. [SRC-0074]

## TSS, AWH, and OPES comparison

TSS, AWH, and OPES all adapt a simulation from information learned on the fly, but they adapt different objects. TSS treats free-energy estimation as stochastic approximation over a discrete family of rungs and adds explicit resource allocation through visit-control tilts and adaptive target densities. [SRC-0005, sections 2.1-2.2] AWH is also an extended-ensemble method over a parameter $\lambda$, but its central state is a conditional weight histogram that updates a free-energy bias toward a target $\lambda$ distribution. [SRC-0007, section II] [SRC-0008, section II.A] OPES instead reconstructs a collective-variable probability density and derives a bias from the ratio between the estimated density and a target density. [SRC-0010, eqs. 4-8]

The practical distinction is that TSS emphasizes adaptive allocation and estimator variance, AWH emphasizes robust extended-ensemble bias learning from fractional conditional weights, and OPES emphasizes probability reconstruction in collective-variable space. TSS's windowing mechanism addresses large discrete rung sets by combining overlapping local estimates; AWH can use Gibbs parameter moves and nonuniform targets; OPES uses kernel compression and bias regularization to keep the KDE-based bias practical and bounded. [SRC-0005, section 3.1] [SRC-0008, section II.C] [SRC-0009, section I.A.1] [SRC-0010, eq. 8] [SRC-0011]

The evidence base also differs. TSS has theory and focused demonstrations, including a Gaussian example and an aqueous-solution MD example, but not a broad molecular benchmark suite. [SRC-0005, section 4] [SRC-0006, section 10] AWH has a longer chain of demonstrations across model systems, atomistic PMFs, and alchemical hydration free energies, while still not being universally superior to BAR/MBAR when equilibrium sampling is already efficient. [SRC-0007] [SRC-0008] [SRC-0009, conclusion] OPES is best read as a metadynamics-adjacent CV enhanced-sampling framework whose reliability still depends on the chosen collective variables and target distribution. [SRC-0010]

## Core equations

Tilt estimator for relative visitation: [SRC-0005, eq. 11]

$$
o_k^t=\frac{1}{t}\sum_{s=1}^t\frac{1\{K^s=k\}}{\gamma_k}.
$$

Visit-control density: [SRC-0005, eqs. 15-17]

$$
\pi_k^{TSS}=\frac{\gamma_k o_k^{-\eta}}{\sum_\ell \gamma_\ell o_\ell^{-\eta}}, \qquad
\pi_k^{TSS}:=(1-\epsilon_\pi)\pi_k^{TSS}+\epsilon_\pi\gamma_k.
$$

Lyapunov comparison: [SRC-0005, proposition 2]

$$
\frac{d}{dt}V_\gamma(F)\bigg|_{\eta'} \le \frac{d}{dt}V_\gamma(F)\bigg|_{\eta} \le 0, \qquad \eta'>\eta\ge 0.
$$

Windowed global rung probability: [SRC-0006, eq. 7.25]

$$
q_k^t=\sum_{j \in win(k)}p_j^t\frac{\gamma_{j;k}^t o_{j;k}^t}{\sum_{\ell \in W_j}\gamma_{j;\ell}^t o_{j;\ell}^t}.
$$

AWH conditional weight update: [SRC-0009, eqs. 3 and 5]

$$
w_\lambda(x)=
\frac{\pi_\lambda e^{f_\lambda-\beta E_\lambda(x)}}{\sum_{\lambda'}\pi_{\lambda'}e^{f_{\lambda'}-\beta E_{\lambda'}(x)}}.
$$

## Variable glossary

- $\gamma$: target asymptotic allocation across rungs. [SRC-0005, section 2.2.1]
- $\pi$: adaptive sampling allocation used transiently. [SRC-0005, section 2.2.1]
- $o_k$: empirical visit ratio for rung $k$; values above or below 1 indicate over- or under-visitation relative to target. [SRC-0005, eq. 11]
- $\eta$: visit-control strength. [SRC-0005, eq. 15]
- $\epsilon_\pi$, $\epsilon_\gamma$: regularization parameters that keep probabilities positive. [SRC-0005, eq. 17] [SRC-0006, eq. 7.18]
- $W_j$: local window. [SRC-0005, section 3.1]
- $q_k$: global probability of visiting rung $k$ across windows. [SRC-0006, eq. 7.25]
- $W_\lambda$: AWH weight histogram accumulated from conditional probabilities. [SRC-0007, eq. 5]

## Derivation sketch

Visit control is derived by freezing a poor free-energy estimate and observing that the resulting rung occupancies can be exponentially tilted away from the desired reference distribution. The tilts estimate that occupancy distortion, and the adaptive density attempts to counteract it without changing the asymptotic target. [SRC-0005, section 2.2.1]

In AWH, adaptation is driven by a persistent histogram of fractional conditional weights rather than only integer visits. The update compares the accumulated histogram to the target distribution and shrinks update size as the effective sample count grows. [SRC-0007, section II] [SRC-0008, section II.D]

Windowing is derived by introducing the active-window variable `J`, enforcing a double cover of parameter space, and using local transitions that remain ergodic over windows. The supplement then derives global probabilities and free-energy offsets from local estimates. [SRC-0005, section 3.1] [SRC-0006, sections 6-7]

## Implementation consequences

- Turning visit control on is more important than precisely optimizing $\eta$, according to the supplement's parameter guidance and numerical example. [SRC-0006, sections 9 and 10.2.2]
- Too small a window can make rung motion diffusive; too large a window can create unstable early rung jumps into physically infeasible states. [SRC-0006, sections 9 and 10.2.1]
- Regularization prevents some windows or rungs from receiving too little probability in degenerate cases. [SRC-0006, section 9]

## Caveats

- Stronger adaptation is not unconditionally better: large $\eta$ can amplify noisy tilt estimates, and window choices affect both stability and error bars. [SRC-0006, sections 9-10]
- The convergence proof depends on the adaptation satisfying the source's assumptions. [SRC-0006, section 5]

## Links

- [[wiki/sources/SRC-0005-times-square-sampling-free-energy]]
- [[wiki/sources/SRC-0007-improving-efficiency-extended-ensemble-awh]]
- [[wiki/sources/SRC-0008-awh-free-energy-landscapes]]
- [[wiki/sources/SRC-0009-awh-alchemical-free-energy]]
- [[wiki/sources/SRC-0010-rethinking-metadynamics-opes]]
- [[wiki/sources/SRC-0013-ladybugs-lambda-dynamics]]
- [[wiki/concepts/accelerated-weight-histogram-method]]
- [[wiki/concepts/on-the-fly-probability-enhanced-sampling]]
- [[wiki/concepts/lambda-dynamics-with-bias-updated-gibbs-sampling]]
- [[wiki/sources/SRC-0006-times-square-sampling-supplement]]
- [[wiki/concepts/times-square-sampling]]
- [[wiki/concepts/free-energy-estimation]]
- [[wiki/concepts/tss-implementation-patterns]]
- [[wiki/questions/tss-generalization-scope]]
- [[wiki/sources/SRC-0074-convergence-is-not-correctness-context-dependent-performance-of]]
- [[wiki/concepts/enhanced-sampling-validation]]

## Open Questions

- What adaptive policies best allocate sampling effort for realistic molecular systems where slow state-space motion and rung motion interact? [SRC-0005] [SRC-0006]
