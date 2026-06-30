---
type: concept
status: active
created: 2026-06-29
updated: 2026-06-29
areas:
  - research
categories:
  - research/statistics/monte-carlo
  - research/molecular-simulation/free-energy
  - research/adaptive-sampling
tags:
  - times-square-sampling
  - free-energy-estimation
  - stochastic-approximation
  - math-heavy
related:
  - "[[sources/SRC-0005-times-square-sampling-free-energy]]"
  - "[[sources/SRC-0006-times-square-sampling-supplement]]"
  - "[[concepts/free-energy-estimation]]"
  - "[[concepts/adaptive-enhanced-sampling]]"
  - "[[concepts/on-the-fly-estimation-versus-mbar]]"
  - "[[concepts/tss-implementation-patterns]]"
sources:
  - SRC-0005
  - SRC-0006
sensitivity: public
encryption: none
---

# Times Square Sampling

## Summary

Times Square Sampling is an adaptive on-the-fly algorithm for estimating free energy differences and related observables while dynamically allocating sampling effort across a discretized family of intermediate probability distributions. [SRC-0005]

## Key Points

- TSS is built on simulated tempering: a sampler moves across rungs $\lambda_k$ while also sampling configurations $x$ inside each rung. [SRC-0005, section 2.1]
- It updates free energy estimates during sampling through stochastic approximation rather than waiting until all samples are collected. [SRC-0005, eqs. 7-8]
- The algorithm maintains free energy estimates $F$, auxiliary ensemble-average estimates $\mu$, and visit-control tilts $o$. [SRC-0005, eqs. 24-26]
- Visit control biases transient sampling toward under-visited rungs, avoiding exponential slowdown when initial free energy estimates are poor. [SRC-0005, section 2.2.1]
- Windowing turns a large global parameter-space problem into overlapping local TSS problems whose local estimates are stitched into global sampling and reporting quantities. [SRC-0005, section 3.1] [SRC-0006, section 6]
- Self-adjustment is the variance-reducing feedback produced when current estimates influence future samples; the paper proves a setting where this gives lower asymptotic variance than MBAR. [SRC-0005, proposition 3] [SRC-0006, section 4.5]

## Mathematical structure

The target object is a family of Gibbs distributions $\rho_k(x)$ with unknown partition functions $Z_k^*$ and free energies $F_k^*=-\log Z_k^*$. TSS estimates the free energies only up to a common additive constant, which is enough for free-energy differences. [SRC-0005, section 2.1]

For fixed estimates $F$ and reference rung density $\gamma$, simulated tempering targets a joint density over $(x,k)$. The conditional probability $p(k \mid x)$ can be computed from Hamiltonians and current free-energy estimates, and that conditional probability drives both rung moves and Rao-Blackwellized estimator updates. [SRC-0005, eqs. 2-7]

TSS extends the basic estimator with $\theta=(F,\mu,o)$. The $\mu$ variables estimate observable averages used to choose a coordinate-aware rung density, while $o$ estimates relative visit frequencies used for visit control. [SRC-0005, section 2.2]

In the windowed version, the sampled state is $(X,K,J)$, where $J$ is the active window. Local per-window estimates are combined by solving for window probabilities, global visit-control free energies, and reported free energies. [SRC-0005, section 3.1] [SRC-0006, sections 6-7]

## Core equations

Free energy target: [SRC-0005, eq. 1]

$$
\rho_k(x)=\frac{e^{-H_k(x)}}{Z_k^*}, \qquad F_k^*=-\log Z_k^*.
$$

Simulated-tempering target: [SRC-0005, eq. 2]

$$
p_{\gamma,F}(x,k)=\frac{\gamma_k e^{F_k-F_k^*}}{\sum_{\ell}\gamma_\ell e^{F_\ell-F_\ell^*}}\rho_k(x).
$$

Basic free-energy root-finding recursion: [SRC-0005, eqs. 7-8]

$$
F_k^{t+1}=F_k^t+\frac{1}{t+1}\left(1-\frac{p_{\gamma,F^t}(k \mid X^{t+1})}{\gamma_k}\right),
$$

with mean field

$$
g_k^F(F)=1-\frac{e^{F_k-F_k^*}}{\sum_\ell \gamma_\ell e^{F_\ell-F_\ell^*}}.
$$

TSS visit-control density: [SRC-0005, eqs. 11 and 15]

$$
o_k^t=\frac{1}{t}\sum_{s=1}^t\frac{1\{K^s=k\}}{\gamma_k}, \qquad
\pi_k^{TSS}=\frac{\gamma_k o_k^{-\eta}}{\sum_\ell \gamma_\ell o_\ell^{-\eta}}.
$$

TSS update triple: [SRC-0005, eqs. 24-26]

$$
\theta^t=(F^t,\mu^t,o^t), \qquad \theta^{t+1}=\text{TSSUpdate}(X^{t+1},K^{t+1},\theta^t).
$$

Windowed invariant density: [SRC-0006, eq. 6.4]

$$
p_{\pi,F}(x,k,j)=\frac{1}{2}1_{W_j}(\lambda_k)p_{\pi,F}(x,k).
$$

## Variable glossary

- $S$: high-dimensional state space, such as atomic coordinates. [SRC-0005, section 2]
- $\Lambda$: low-dimensional parameter space, discretized into rungs $\lambda_1, \ldots, \lambda_K$. [SRC-0005, section 2]
- $H_k(x)$: Hamiltonian at rung $k$. [SRC-0005, eq. 1]
- $Z_k^*$: unknown partition function. [SRC-0005, eq. 1]
- $F_k^*$: exact dimensionless free energy, $-\log Z_k^*$. [SRC-0005, eq. 1]
- $\gamma$: reference asymptotic rung density. [SRC-0005, section 2.1]
- $\pi$: transient or adaptive rung density used for sampling. [SRC-0005, section 2.2.1]
- $F$: current free-energy estimate. [SRC-0005, eq. 7]
- $\mu$: auxiliary observable estimates used to compute adaptive $\gamma(\mu)$. [SRC-0005, section 2.2.2]
- $o$: tilts measuring empirical visits relative to target visits. [SRC-0005, eq. 11]
- $\eta$: visit-control strength. [SRC-0005, eq. 15]
- $W_j$: window in parameter space. [SRC-0005, section 3.1]
- $J$: active window index in windowed TSS. [SRC-0005, section 3.1]

## Derivation sketch

The basic estimator follows from choosing an observable whose expectation is zero exactly when the estimated free energies match the true free energies up to a constant. The conditional rung probability cancels the unknown normalization in a form that is computable from current estimates and Hamiltonian evaluations. [SRC-0005, eqs. 7-8]

Visit control starts from the observation that if $F_k^t$ is far below $F_k^*$, the bounded update can take exponentially many steps to correct. The tilt $o_k$ estimates over- or under-visitation and is used to approximate an unavailable ideal rung density that would undo the exponential tilt away from the target reference density. [SRC-0005, section 2.2.1]

The supplement derives the recursions in partition-function coordinates, identifies the optimal gain matrix, then maps them back to the logarithmic free-energy and auxiliary-average recursions used by TSS. [SRC-0006, sections 1-2]

## Implementation consequences

- TSS needs access to Hamiltonian evaluations for local rung candidates; windowing keeps this local rather than requiring all rungs each cycle. [SRC-0005, section 3.1]
- The final reported free energies should not simply be the noisy visit-control free energies, because those depend strongly on counting tilts. [SRC-0006, section 6.2]
- Practical implementations store epoch estimates so they can forget early biased history and compute jackknife error estimates. [SRC-0006, sections 7-8]
- More rung moves between estimator updates can improve variance through self-adjustment, especially when rung moves are cheap relative to global communication. [SRC-0005, section 4.3] [SRC-0006, section 10.2.3]

## Caveats

- The convergence and variance results require the paper's assumptions; they are not automatic guarantees for every molecular system. [SRC-0005, section 2.2.4] [SRC-0006, section 5]
- Visit-control strength, window sizes, and update frequencies are tuning parameters with failure modes. [SRC-0006, sections 9-10]
- TSS is promising but not universally validated; the source bundle provides a Gaussian example and one aqueous-solution MD example, not a broad benchmark suite. [SRC-0005, section 4] [SRC-0006, section 10]

## Evidence

- SRC-0005 demonstrates the algorithm on a shifted-Gaussian example and shows how visit control, windows, and self-adjustment address distinct convergence or scaling bottlenecks. [SRC-0005, section 4]
- SRC-0006 adds an aqueous-solution molecular dynamics example showing practical effects of windowing, visit control, and self-adjustment. [SRC-0006, section 10]

## Links

- [[sources/SRC-0005-times-square-sampling-free-energy]]
- [[sources/SRC-0006-times-square-sampling-supplement]]
- [[concepts/free-energy-estimation]]
- [[concepts/adaptive-enhanced-sampling]]
- [[concepts/on-the-fly-estimation-versus-mbar]]
- [[concepts/tss-implementation-patterns]]
- [[questions/tss-generalization-scope]]

## Open Questions

- Which adaptive allocation functions beyond the paper's visit-control form are useful in realistic free energy calculations? [SRC-0005]
- How should the practical tuning parameters be chosen for systems unlike the supplement's aqueous-solution example? [SRC-0006]
