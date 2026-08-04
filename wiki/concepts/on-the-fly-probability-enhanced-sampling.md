---
type: concept
status: active
created: 2026-06-30
updated: 2026-07-31
areas:
  - research
categories:
  - research/adaptive-sampling
  - research/molecular-simulation/free-energy
tags:
  - opes
  - metadynamics
  - probability-reconstruction
  - collective-variables
  - math-heavy
related:
  - "[[wiki/sources/SRC-0010-rethinking-metadynamics-opes]]"
  - "[[wiki/sources/SRC-0011-opes-supporting-information]]"
  - "[[wiki/concepts/adaptive-enhanced-sampling]]"
  - "[[wiki/concepts/free-energy-estimation]]"
  - "[[wiki/sources/SRC-0074-convergence-is-not-correctness-context-dependent-performance-of]]"
  - "[[wiki/concepts/enhanced-sampling-validation]]"
sources:
  - SRC-0010
  - SRC-0011
  - SRC-0074
sensitivity: public
encryption: none
---

# On-the-Fly Probability-Enhanced Sampling

## Summary

On-the-fly probability-enhanced sampling, or OPES, is an enhanced-sampling method that reconstructs a collective-variable probability distribution during a simulation and derives the bias from that estimate. It can be viewed as a metadynamics-adjacent method that shifts attention from accumulating bias hills to estimating a probability distribution with a target ensemble. [SRC-0010]

## Key Points

- OPES estimates $P(s)$ with weighted Gaussian kernels and uses the estimate to construct a bias. [SRC-0010]
- The method explicitly separates the desired target distribution $p^{tg}(s)$ from the current probability estimate. [SRC-0010, eq. 4]
- Kernel compression makes the on-the-fly KDE representation computationally feasible. [SRC-0011]
- The explored-region normalization $Z_n$ helps avoid slow exploration in multidimensional CV spaces. [SRC-0010, eq. 7]
- The regularization $\epsilon$ caps the applied bias and gives users control over how aggressively high-free-energy regions are explored. [SRC-0010, eq. 8]

## Core equations

Target-distribution bias: [SRC-0010, eq. 4]

$$
V(s)=\frac{1}{\beta}\log\frac{P(s)}{p^{tg}(s)}.
$$

Probability estimate: [SRC-0010, eq. 5]

$$
\tilde{P}_n(s)=\frac{\sum_k^n w_k G(s,s_k)}{\sum_k^n w_k}.
$$

OPES bias: [SRC-0010, eq. 8]

$$
V_n(s)=\left(1-\frac{1}{\gamma}\right)\frac{1}{\beta}
\log\left(\frac{\tilde{P}_n(s)}{Z_n}+\epsilon\right).
$$

## Variable glossary

- $s=s(R)$: collective variables. [SRC-0010]
- $P(s)$: unbiased probability density in CV space. [SRC-0010]
- $p^{tg}(s)$: target distribution sampled at convergence. [SRC-0010]
- $\tilde{P}_n(s)$: KDE probability estimate at iteration $n$. [SRC-0010]
- $G(s,s_k)$: Gaussian kernel centered at sampled CV point $s_k$. [SRC-0010]
- $Z_n$: normalization over the explored CV region. [SRC-0010]
- $\epsilon$: regularization that bounds the bias. [SRC-0010]

## Implementation consequences

- OPES requires a deposition pace, initial kernel bandwidth, and approximate barrier height. [SRC-0010]
- Kernel compression avoids grid predefinition and is better suited than grids for higher-dimensional CV spaces, though cost still scales with the number of compressed kernels. [SRC-0011]
- The barrier parameter can be interpreted as the approximate barrier height the bias should overcome. [SRC-0011]

## Caveats

- OPES still depends on the choice of collective variables. [SRC-0010]
- The source bundle focuses on well-tempered and flat targets, leaving other target designs for future work. [SRC-0010]
- In a five-system biomolecular benchmark, suitable OPES barrier settings were competitive, but some unsuitable settings produced internally stable landscapes that disagreed with other methods. Barrier sensitivity and external validation are therefore necessary for new systems. [SRC-0074, pp. 9-10]

## Links

- [[wiki/sources/SRC-0010-rethinking-metadynamics-opes]]
- [[wiki/sources/SRC-0011-opes-supporting-information]]
- [[wiki/concepts/adaptive-enhanced-sampling]]
- [[wiki/concepts/free-energy-estimation]]
- [[wiki/sources/SRC-0074-convergence-is-not-correctness-context-dependent-performance-of]]
- [[wiki/concepts/enhanced-sampling-validation]]

## Open Questions

- How should OPES target distributions be chosen for production systems where the desired exploration region is not known in advance? [SRC-0010]
