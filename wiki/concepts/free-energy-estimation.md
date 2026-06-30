---
type: concept
status: active
created: 2026-06-29
updated: 2026-06-29
areas:
  - research
categories:
  - research/molecular-simulation/free-energy
  - research/statistics/monte-carlo
tags:
  - free-energy-estimation
  - partition-functions
  - molecular-simulation
  - math-heavy
related:
  - "[[sources/SRC-0005-times-square-sampling-free-energy]]"
  - "[[sources/SRC-0006-times-square-sampling-supplement]]"
  - "[[concepts/times-square-sampling]]"
  - "[[concepts/adaptive-enhanced-sampling]]"
  - "[[concepts/on-the-fly-estimation-versus-mbar]]"
sources:
  - SRC-0005
  - SRC-0006
sensitivity: public
encryption: none
---

# Free Energy Estimation

## Summary

Free energy estimation computes differences between free energies, often by estimating ratios of partition functions or normalizing constants for probability distributions such as Gibbs distributions. [SRC-0005]

## Key Points

- In SRC-0005, each probability distribution is defined by a Hamiltonian and an unknown partition function; the dimensionless free energy is the negative logarithm of that partition function. [SRC-0005, eq. 1]
- Free energy differences are all that matter because the estimates are identifiable only up to a common additive constant. [SRC-0005, section 2.1]
- Enhanced sampling introduces intermediate distributions to improve exploration, but how sampling effort is allocated across those distributions strongly affects estimator variance. [SRC-0005, introduction]
- TSS treats free energy estimation as both a stochastic root-finding problem and a resource-allocation problem. [SRC-0005, sections 2.1-2.2]
- The supplement translates the estimator into per-window, epoch-based formulas for implementation and error estimation. [SRC-0006, sections 7-8]

## Core equations

Distribution, partition function, and free energy: [SRC-0005, eq. 1]

$$
\rho_\lambda(x)=\frac{e^{-H_\lambda(x)}}{Z_\lambda^*}, \qquad
Z_\lambda^*=\int_S e^{-H_\lambda(x)}dx, \qquad
F_\lambda^*=-\log Z_\lambda^*.
$$

Free energy difference between two rungs: [SRC-0005, section 2.1]

$$
F_a^*-F_b^*=-\log\frac{Z_a^*}{Z_b^*}.
$$

TSS's basic root-finding observable: [SRC-0005, eqs. 7-8]

$$
G_k^F(X;F)=1-\frac{p_{\gamma,F}(k \mid X)}{\gamma_k}, \qquad E_{\gamma,F^*}[G_k^F]=0.
$$

Auxiliary observable estimator: [SRC-0005, eq. 20]

$$
G_{km}^{\mu}(x;F,\mu,o)=\frac{p_{\pi,F}(k \mid x)}{\pi_k}(\psi_m(x)-\mu_{km}).
$$

Coordinate-invariant rung density from a metric: [SRC-0005, eq. 19] [SRC-0006, eqs. 7.10-7.18]

$$
\gamma_k \propto \sqrt{\det g(\lambda_k)}, \qquad
g_{ij}(\lambda)=E\left[\frac{\partial H}{\partial \lambda_i}\frac{\partial H}{\partial \lambda_j}\right]
-E\left[\frac{\partial H}{\partial \lambda_i}\right]E\left[\frac{\partial H}{\partial \lambda_j}\right].
$$

## Variable glossary

- $\rho_\lambda$: probability density at parameter $\lambda$. [SRC-0005, eq. 1]
- $H_\lambda$: dimensionless Hamiltonian. [SRC-0005, eq. 1]
- $Z_\lambda^*$: partition function, generally unknown. [SRC-0005, eq. 1]
- $F_\lambda^*$: exact free energy, $-\log Z_\lambda^*$. [SRC-0005, eq. 1]
- $\lambda_k$: discretized parameter value or rung. [SRC-0005, section 2.1]
- $\psi_m$: auxiliary observable whose ensemble average may inform the target rung density. [SRC-0005, section 2.2.2]
- $\mu_{km}$: estimated average of $\psi_m$ under rung $k$. [SRC-0005, eq. 20]

## Derivation sketch

The estimator uses simulated tempering to sample an extended distribution where the unknown free energies enter only through current estimates. Conditional rung probabilities can be computed from Hamiltonian values and current estimates, so the stochastic approximation update does not need the true partition functions. [SRC-0005, section 2.1]

The supplement's iterative-importance-sampling derivation rewrites free-energy estimation in partition-function coordinates, then converts back to logarithmic free-energy coordinates. This explains both the logarithmic update and the history-forgetting implementation. [SRC-0006, sections 1.2 and 6.3]

## Implementation consequences

- Free energy estimates should be interpreted as differences or profiles, not absolute values. [SRC-0005, section 2.1]
- Estimator quality depends on overlap between neighboring distributions and on how often informative rungs are visited. [SRC-0005, introduction]
- Windowed implementations must combine local estimates into global reported free energies rather than directly report noisy visit-control free energies. [SRC-0006, section 6.2]
- Error bars in the supplement are jackknife estimates over stored epochs and require decorrelated epoch pseudo-values. [SRC-0006, section 8]

## Caveats

- A theoretically optimal estimator still depends on practical sampling quality; poor mixing in `S` or `Lambda` can make estimates unreliable. [SRC-0005, section 2.1] [SRC-0006, section 10]
- The source bundle gives examples and theory, but not universal validation across all alchemical schedules or molecular systems. [SRC-0006, section 10.1]

## Evidence

- SRC-0005 motivates TSS by arguing that the allocation of computational resources across rungs changes the variance of the desired free energy estimate. [SRC-0005, introduction]
- SRC-0006's aqueous-solution example reports free energy differences for eight alchemical edges and compares estimated errors under different TSS settings. [SRC-0006, section 10]

## Links

- [[sources/SRC-0005-times-square-sampling-free-energy]]
- [[sources/SRC-0006-times-square-sampling-supplement]]
- [[concepts/times-square-sampling]]
- [[concepts/adaptive-enhanced-sampling]]
- [[concepts/on-the-fly-estimation-versus-mbar]]

## Open Questions

- When should free energy estimation prioritize broad exploration of intermediate distributions versus targeted sampling of high-variance regions? [SRC-0005]
