---
type: concept
status: active
created: 2026-06-29
updated: 2026-06-29
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
  - "[[sources/SRC-0005-times-square-sampling-free-energy]]"
  - "[[sources/SRC-0006-times-square-sampling-supplement]]"
  - "[[concepts/times-square-sampling]]"
  - "[[concepts/free-energy-estimation]]"
  - "[[concepts/tss-implementation-patterns]]"
sources:
  - SRC-0005
  - SRC-0006
sensitivity: public
encryption: none
---

# Adaptive Enhanced Sampling

## Summary

Adaptive enhanced sampling uses information learned during a simulation to steer future sampling, with the goal of improving exploration or reducing estimator variance. [SRC-0005]

## Key Points

- Enhanced sampling methods such as replica exchange and simulated tempering help sample multimodal distributions by introducing a family of overlapping intermediate distributions. [SRC-0005, introduction]
- Their efficiency depends on the free energy landscape and on how computational resources are distributed among rungs, but that landscape is usually unknown before sampling. [SRC-0005, introduction]
- TSS adapts the rung-sampling distribution using current estimates, enabling resource allocation to change during the run. [SRC-0005, section 2.2]
- Visit control is a transient adaptive mechanism that pushes sampling toward under-visited rungs and mitigates slow convergence caused by poor initial free energy guesses. [SRC-0005, section 2.2.1]
- Windowing is a locality mechanism: it restricts updates to overlapping parameter-space neighborhoods where distributions are expected to have useful overlap. [SRC-0005, section 3.1]
- Adaptive sampling must preserve convergence guarantees; SRC-0005 and SRC-0006 state assumptions and proof structure for convergence despite adaptation. [SRC-0005, section 2.2.4] [SRC-0006, section 5]

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

## Variable glossary

- $\gamma$: target asymptotic allocation across rungs. [SRC-0005, section 2.2.1]
- $\pi$: adaptive sampling allocation used transiently. [SRC-0005, section 2.2.1]
- $o_k$: empirical visit ratio for rung $k$; values above or below 1 indicate over- or under-visitation relative to target. [SRC-0005, eq. 11]
- $\eta$: visit-control strength. [SRC-0005, eq. 15]
- $\epsilon_\pi$, $\epsilon_\gamma$: regularization parameters that keep probabilities positive. [SRC-0005, eq. 17] [SRC-0006, eq. 7.18]
- $W_j$: local window. [SRC-0005, section 3.1]
- $q_k$: global probability of visiting rung $k$ across windows. [SRC-0006, eq. 7.25]

## Derivation sketch

Visit control is derived by freezing a poor free-energy estimate and observing that the resulting rung occupancies can be exponentially tilted away from the desired reference distribution. The tilts estimate that occupancy distortion, and the adaptive density attempts to counteract it without changing the asymptotic target. [SRC-0005, section 2.2.1]

Windowing is derived by introducing the active-window variable `J`, enforcing a double cover of parameter space, and using local transitions that remain ergodic over windows. The supplement then derives global probabilities and free-energy offsets from local estimates. [SRC-0005, section 3.1] [SRC-0006, sections 6-7]

## Implementation consequences

- Turning visit control on is more important than precisely optimizing $\eta$, according to the supplement's parameter guidance and numerical example. [SRC-0006, sections 9 and 10.2.2]
- Too small a window can make rung motion diffusive; too large a window can create unstable early rung jumps into physically infeasible states. [SRC-0006, sections 9 and 10.2.1]
- Regularization prevents some windows or rungs from receiving too little probability in degenerate cases. [SRC-0006, section 9]

## Caveats

- Stronger adaptation is not unconditionally better: large $\eta$ can amplify noisy tilt estimates, and window choices affect both stability and error bars. [SRC-0006, sections 9-10]
- The convergence proof depends on the adaptation satisfying the source's assumptions. [SRC-0006, section 5]

## Links

- [[sources/SRC-0005-times-square-sampling-free-energy]]
- [[sources/SRC-0006-times-square-sampling-supplement]]
- [[concepts/times-square-sampling]]
- [[concepts/free-energy-estimation]]
- [[concepts/tss-implementation-patterns]]
- [[questions/tss-generalization-scope]]

## Open Questions

- What adaptive policies best allocate sampling effort for realistic molecular systems where slow state-space motion and rung motion interact? [SRC-0005] [SRC-0006]
