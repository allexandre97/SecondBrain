---
type: concept
status: active
created: 2026-06-29
updated: 2026-06-29
areas:
  - research
categories:
  - research/adaptive-sampling
  - research/scientific-computing
  - research/molecular-simulation/free-energy
tags:
  - implementation
  - adaptive-sampling
  - free-energy-estimation
  - math-heavy
related:
  - "[[sources/SRC-0005-times-square-sampling-free-energy]]"
  - "[[sources/SRC-0006-times-square-sampling-supplement]]"
  - "[[concepts/times-square-sampling]]"
  - "[[concepts/adaptive-enhanced-sampling]]"
  - "[[concepts/free-energy-estimation]]"
sources:
  - SRC-0005
  - SRC-0006
sensitivity: public
encryption: none
---

# Times Square Sampling Implementation Patterns

## Summary

Times Square Sampling is designed around the practical cost difference between sampler moves, energy evaluations, estimator updates, and communication between hardware components. [SRC-0005]

## Key Points

- The paper separates sampler work from estimator work: sampler moves perform state and rung dynamics, while estimator updates process Hamiltonian evaluations and update free energy estimates. [SRC-0005, section 4.3]
- Energy evaluations across all rungs can be prohibitively expensive, so windowing limits updates to local neighborhoods in parameter space. [SRC-0005, section 3.1]
- Communication latency matters because sampling and estimation may run on separate hardware; TSS can perform multiple sampler moves between estimator updates to hide some latency. [SRC-0005, section 4.3] [SRC-0006, section 9]
- History forgetting reduces dependence on inaccurate initial estimates and makes epoch-based jackknife error estimation practical. [SRC-0006, sections 6.3 and 8]
- Multiple replicas allow parallel samplers to contribute to shared estimates. [SRC-0006, sections 6.3 and 10.2]
- A full TSS cycle alternates window movement, molecular or state dynamics, Hamiltonian evaluation, rung moves, local stochastic approximation updates, and global estimate assembly. [SRC-0006, section 9]

## Core equations

Recent-history epoch counts: [SRC-0006, eqs. 7.2-7.4]

$$
N_j^{t,l}(r)=\sum_{s=\tau_{l-1}+1}^{\tau_l \wedge t}1\{J^s(r)=j\}, \qquad
N_j^t=\sum_{r=1}^R\sum_{l=n(\alpha t)}^{n(t)}N_j^{t,l}(r).
$$

Importance ratio for per-window estimates: [SRC-0006, eqs. 7.5-7.6]

$$
R_{j;k}^t(r)=1\{J^t(r)=j\}\frac{e^{-H_k(X^t(r))}}{d_j^t(r)}.
$$

Per-window all-epoch free energy estimate: [SRC-0006, eq. 7.9]

$$
e^{-F_{j;k}^t}=\sum_{l=n(\alpha t)}^{n(t)}\frac{N_j^{t,l}}{\sum_{l'}N_j^{t,l'}}e^{-F_{j;k}^{t,l}}.
$$

Window marginal probabilities and global rung weights: [SRC-0006, eqs. 7.23-7.25]

$$
Qp=p, \qquad
q_k^t=\sum_{j \in win(k)}p_j^t\frac{\gamma_{j;k}^t o_{j;k}^t}{\sum_{\ell \in W_j}\gamma_{j;\ell}^t o_{j;\ell}^t}.
$$

Reported free energies: [SRC-0006, eq. 6.23]

$$
F_k^{TSS}=\frac{1}{\gamma_k^{TSS}}\sum_{j \in win(k)}p_j\gamma_{j;k}(F_{j;k}-f_j^{TSS}).
$$

Jackknife epoch spacing: [SRC-0006, eq. 8.5]

$$
\phi=\alpha^{-1/n_{epochs}}.
$$

## Variable glossary

- `R`: number of replicas. [SRC-0006, section 7.1.1]
- $\alpha$: history-forgetting fraction; recent history is approximately from `alpha t` to `t`. [SRC-0006, section 7.1.1]
- $\phi$: epoch growth multiplier. [SRC-0006, section 8]
- $N_j^{t,l}$: visits to window $j$ during epoch $l$. [SRC-0006, eq. 7.2]
- $R_{j;k}^t$: importance ratio for a per-window estimate. [SRC-0006, eq. 7.5]
- $Q$: left-stochastic matrix used to compute window probabilities. [SRC-0006, eq. 7.23]
- $p_j$: estimated marginal probability of window $j$. [SRC-0006, section 7.2.1]
- $q_k$: global probability of visiting rung $k$. [SRC-0006, eq. 7.25]
- $f_j$: window free-energy offset. [SRC-0006, sections 6.2 and 7.2]

## Implementation consequences

- Per-window epoch updates are relatively cheap; global offset solves and error-bar calculations are more expensive global operations. [SRC-0006, section 9]
- Visit-control free energies are used for sampling, while reported free energies are computed with a lower-noise reporting construction near convergence. [SRC-0006, section 6.2]
- Jackknife error bars can be computed infrequently because they do not drive the sampler. [SRC-0006, section 9]
- Increasing rung-update frequency can reduce variance even when estimator-update frequency is unchanged, but the benefit depends on the relative cost of rung moves, energy evaluations, and communication. [SRC-0006, section 10.2.3]

## Tradeoffs

- More sampler moves per estimator update can improve statistical behavior through self-adjustment, but only if the extra moves are cheap enough relative to communication and estimation costs. [SRC-0005, section 4.3] [SRC-0006, section 9]
- Larger windows permit broader rung movement but can be unstable early; smaller windows reduce infeasible jumps but can make rung dynamics diffusive and increase error bars. [SRC-0006, sections 9 and 10.2.1]
- History forgetting can reduce early-estimate bias, but epochs must be long and numerous enough for useful jackknife error estimates. [SRC-0006, section 8]

## Caveats

- The supplement's implementation guidance reflects tested systems and examples, not universal settings. [SRC-0006, section 9]
- Practical implementations still need diagnostics for rung mixing, epoch decorrelation, window coverage, and physical feasibility of proposed states. [SRC-0006, sections 8-10]

## Links

- [[sources/SRC-0005-times-square-sampling-free-energy]]
- [[sources/SRC-0006-times-square-sampling-supplement]]
- [[concepts/times-square-sampling]]
- [[concepts/adaptive-enhanced-sampling]]
- [[concepts/free-energy-estimation]]

## Open Questions

- How should window size, visit-control strength, sampler moves per estimator update, replica count, and epoch schedule be tuned for different molecular systems? [SRC-0005] [SRC-0006]
