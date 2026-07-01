---
type: source
status: active
created: 2026-06-30
updated: 2026-07-01
source_id: SRC-0023
display_title: "Statistically Optimal Analysis of Samples from Multiple Equilibrium States"
short_title: "Original MBAR Paper"
aliases:
  - "SRC-0023"
  - "Original MBAR Paper"
  - "Statistically Optimal Analysis of Samples from Multiple Equilibrium States"
source_path: raw/sources/SRC-0023-statistically-optimal-analysis-multiple-equilibrium-states-mbar.pdf
imported_path: raw/sources/SRC-0023-statistically-optimal-analysis-multiple-equilibrium-states-mbar.pdf
original_filename: "124105_1_online.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 6bea1d3c790a388b5ab728175fb6914d4e1fd64a4258983cad84a26531a18214
authors:
  - "Michael R. Shirts"
  - "John D. Chodera"
author_entities:
  - "[[wiki/entities/authors/michael-r-shirts]]"
  - "[[wiki/entities/authors/john-d-chodera]]"
year: 2008
venue: "Journal of Chemical Physics"
doi: "10.1063/1.2978177"
arxiv:
metadata_review_status: reviewed
areas:
  - research
categories:
  - research/molecular-simulation/free-energy
  - research/statistics/monte-carlo
tags:
  - mbar
  - free-energy-estimation
  - bridge-sampling
  - reweighting
  - math-heavy
related:
  - "[[wiki/concepts/multistate-bennett-acceptance-ratio]]"
  - "[[wiki/concepts/free-energy-estimation]]"
  - "[[wiki/concepts/mbar-with-configuration-mapping]]"
sources:
  - SRC-0023
cites_sources: []
citation_match_status: reviewed
cqt_review_status: linked
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: math-standard
---

# Statistically Optimal Analysis of Samples from Multiple Equilibrium States

Source ID: `SRC-0023`

## Raw source

- Repository path: `raw/sources/SRC-0023-statistically-optimal-analysis-multiple-equilibrium-states-mbar.pdf`
- Open raw source: [raw/sources/SRC-0023-statistically-optimal-analysis-multiple-equilibrium-states-mbar.pdf](../../raw/sources/SRC-0023-statistically-optimal-analysis-multiple-equilibrium-states-mbar.pdf)

## Summary

This 2008 JCP paper introduces the multistate Bennett acceptance ratio estimator, MBAR, for estimating free energy differences, equilibrium expectations, and uncertainties from samples drawn from multiple equilibrium states. [SRC-0023]

MBAR generalizes BAR to more than two states, avoids WHAM's histogram discretization, and provides direct asymptotic uncertainty estimates for free energy differences and derived expectations. [SRC-0023]

## Key Points

- MBAR estimates ratios of normalization constants $c_i$ for unnormalized densities $q_i(x)$ sampled from multiple states. [SRC-0023]
- For Boltzmann samples, the estimator becomes a self-consistent set of equations for dimensionless free energies $f_i=-\log c_i$. [SRC-0023]
- Free energies are identifiable only up to an additive constant, so only differences $\Delta f_{ij}=f_j-f_i$ are meaningful. [SRC-0023]
- Unsampled target states can be added with $N_i=0$ once the sampled-state free energies are solved. [SRC-0023]
- Equilibrium expectations can be estimated by augmenting the MBAR system with additional columns corresponding to observable-weighted functions. [SRC-0023]
- The asymptotic covariance estimator propagates uncertainty to free energy differences and arbitrary functions of the estimated log-normalization constants. [SRC-0023]
- The paper demonstrates MBAR on a DNA hairpin PMF from multiple optical-tweezer constant-force experiments. [SRC-0023]

## Key equations

Unnormalized density and normalization constant:

$$
p_i(x)=c_i^{-1}q_i(x),
\qquad
c_i=\int_{\Gamma} q_i(x)\,dx.
$$

[SRC-0023]

Dimensionless free energy difference:

$$
\Delta f_{ij}=f_j-f_i=-\log\frac{c_j}{c_i}.
$$

[SRC-0023]

MBAR self-consistent equations for Boltzmann reduced potentials $u_i(x)$:

$$
\hat f_i=
-\log\sum_{j=1}^{K}\sum_{n=1}^{N_j}
\frac{\exp[-u_i(x_{jn})]}
{\sum_{k=1}^{K}N_k\exp[\hat f_k-u_k(x_{jn})]}.
$$

[SRC-0023, eq. 11]

MBAR weight matrix:

$$
W_{ni}=
\frac{\hat c_i^{-1}q_i(x_n)}
{\sum_{k=1}^{K}N_k\hat c_k^{-1}q_k(x_n)}.
$$

[SRC-0023, eq. 9]

Asymptotic covariance matrix for $\theta_i=\log c_i$:

$$
\hat\Theta=
W^{\top}(I-WNW^{\top})^{+}W.
$$

[SRC-0023, eq. 8]

Free-energy-difference uncertainty:

$$
\delta^2\Delta \hat f_{ij}
=
\hat\Theta_{ii}-2\hat\Theta_{ij}+\hat\Theta_{jj}.
$$

[SRC-0023, eq. 12]

Equilibrium expectation estimator:

$$
\hat A=\frac{\hat c_A}{\hat c_a}
=\sum_{n=1}^{N}W_{na}A(x_n).
$$

[SRC-0023, eq. 15]

## Equation inventory

| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |
| $p_i=c_i^{-1}q_i$ | SRC-0023 section II | This page; [[wiki/concepts/multistate-bennett-acceptance-ratio]] | Defines normalized states. | $p_i$, $q_i$, $c_i$ | Input model. |
| $\Delta f_{ij}$ | SRC-0023 section II | This page; [[wiki/concepts/free-energy-estimation]] | Defines dimensionless free energy differences. | $f_i$, $c_i$ | Reported quantity. |
| MBAR equations | SRC-0023 eq. 11 | This page; [[wiki/concepts/multistate-bennett-acceptance-ratio]] | Solves sampled-state free energies. | $u_i$, $N_i$, $\hat f_i$ | Core estimator. |
| Weight matrix $W$ | SRC-0023 eq. 9 | This page | Stores contribution of each sample to each state. | $W_{ni}$, $q_i$, $N_i$ | Reweighting and covariance. |
| Covariance $\hat\Theta$ | SRC-0023 eq. 8 | This page | Estimates asymptotic covariance of log normalizers. | $W$, $N$, pseudoinverse | Uncertainty propagation. |
| $\delta^2\Delta\hat f_{ij}$ | SRC-0023 eq. 12 | This page | Gives free-energy-difference uncertainty. | $\hat\Theta_{ij}$ | Error bars. |
| Expectation estimator | SRC-0023 eqs. 13-16 | This page | Estimates observables and PMFs. | $A(x)$, augmented columns | Observable reweighting. |

## Algorithmic recursions

MBAR solves the coupled nonlinear free-energy equations by self-consistent iteration or Newton-Raphson. The paper notes that self-consistent iteration is straightforward and reliable, while Newton-Raphson can be faster but less robust. [SRC-0023, Appendix C]

## Evidence

The paper demonstrates MBAR on DNA hairpin optical-tweezer data by combining constant-force measurements and estimating a PMF with smaller uncertainty than a single-trajectory histogram analysis. [SRC-0023]

## Limitations and Caveats

- MBAR requires reduced potentials $u_k(x_n)$ for every sampled configuration at every state used in the estimator. [SRC-0023]
- The covariance estimator is appropriate for uncorrelated samples; applying it to correlated time-series data can severely underestimate uncertainty. [SRC-0023, Appendix A]
- Practical reliability still depends on phase-space overlap between sampled and target states. [SRC-0023]
- MBAR removes histogram binning bias, but it does not fix poor sampling or missing support. [SRC-0023]

## Links

- [[wiki/concepts/multistate-bennett-acceptance-ratio]]
- [[wiki/concepts/free-energy-estimation]]
- [[wiki/concepts/mbar-with-configuration-mapping]]
- [[wiki/concepts/on-the-fly-estimation-versus-mbar]]

## Claims

- [[wiki/claims/CLM-0004-mbar-is-optimal-but-overlap-limited]] - MBAR is a statistically efficient fixed-sample estimator, but it remains limited by overlap, support, and reduced-potential availability. [SRC-0023]

## Questions

- [[wiki/questions/overlap-support-diagnostics-for-free-energy-estimators]] - Which overlap and support diagnostics should be mandatory before accepting MBAR estimates? [SRC-0023]
- [[wiki/questions/adaptive-estimators-vs-fixed-sample-estimators]] - How should MBAR be compared to adaptive estimators that can change future samples? [SRC-0023] [SRC-0005]

## Tensions

- [[wiki/tensions/TEN-0001-tss-variance-advantage-vs-mbar-generalization]] - TSS's variance comparison should be interpreted as an adaptive sampling-time claim, not a blanket rejection of MBAR. [SRC-0005] [SRC-0023]
- [[wiki/tensions/TEN-0004-configuration-mapping-overlap-gain-vs-support-risk]] - Mapping can extend MBAR, but support requirements remain. [SRC-0012] [SRC-0023]
- [[wiki/tensions/TEN-0005-on-the-fly-bias-adaptation-vs-postprocessing-diagnostics]] - MBAR offers fixed-sample diagnostics, while adaptive methods change the sampling process those diagnostics must evaluate. [SRC-0023]

## Open Questions

- What overlap diagnostics should be treated as mandatory before accepting MBAR estimates in high-dimensional alchemical or umbrella-sampling problems? [SRC-0023]

## Citation links

- Targeted citation review found no confirmed citations from this source to currently ingested free-energy/adaptive-sampling cluster sources; newer cluster sources cite this source instead.

## Mathematical gaps

- The wiki records the main estimator, uncertainty, and expectation equations, but not the full appendices proving BAR equivalence and deriving all generalized inverses.

## Ingestion QA

### Retrieval questions checked

- What does MBAR estimate?
- How does MBAR relate to BAR and WHAM?
- What are the self-consistent MBAR equations?
- How are uncertainty estimates computed?
- How are unsampled states and equilibrium expectations handled?
- What assumptions matter for correlated simulation data?

### Coverage decision

Complete at `coverage_profile: math-standard`. [SRC-0023]

### Known gaps

- Detailed appendix derivations are summarized rather than reproduced in full.
