---
type: source
status: active
created: 2026-06-29
updated: 2026-07-01
source_id: SRC-0006
display_title: "Supplemental Materials for Times Square Sampling"
short_title: "Times Square Sampling Supplement"
aliases:
  - "SRC-0006"
  - "Times Square Sampling Supplement"
  - "Supplemental Materials for Times Square Sampling"
source_path: raw/sources/SRC-0006-times-square-sampling-supplement.pdf
imported_path: raw/sources/SRC-0006-times-square-sampling-supplement.pdf
original_filename: "ucgs_a_2291108_sm6913.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: a0fb7d3c50d92ff03cc4b3a92968a389113d4e9ad1826dcb5c5c37ddb364fd4c
authors:
  - "Cristian Predescu"
  - "Michael Snarski"
  - "Avi Robinson-Mosher"
  - "Duluxan Sritharan"
  - "Tamas Szalay"
  - "David E. Shaw"
author_entities: []
year: 2024
venue: "Journal of Computational and Graphical Statistics"
doi: "10.1080/10618600.2023.2291108"
arxiv:
metadata_review_status: reviewed
areas:
  - research
categories:
  - research/statistics/monte-carlo
  - research/molecular-simulation/free-energy
  - research/computational-drug-discovery
  - research/adaptive-sampling
tags:
  - free-energy-estimation
  - adaptive-sampling
  - simulated-tempering
  - stochastic-approximation
  - molecular-simulation
  - math-heavy
  - supplement
related:
  - "[[wiki/sources/SRC-0005-times-square-sampling-free-energy]]"
  - "[[wiki/concepts/times-square-sampling]]"
  - "[[wiki/concepts/free-energy-estimation]]"
  - "[[wiki/concepts/adaptive-enhanced-sampling]]"
  - "[[wiki/concepts/on-the-fly-estimation-versus-mbar]]"
  - "[[wiki/concepts/tss-implementation-patterns]]"
  - "[[wiki/questions/tss-generalization-scope]]"
sources:
  - SRC-0006
  - SRC-0005
cites_sources:
  - SRC-0023
citation_match_status: reviewed
cqt_review_status: linked
sensitivity: public
encryption: none
source_bundle: times-square-sampling-2024
bundle_role: supplement
ingestion_status: complete
coverage_profile: math-deep
---

# Supplemental Materials for Times Square Sampling

Source ID: `SRC-0006`

## Raw source

- Repository path: `raw/sources/SRC-0006-times-square-sampling-supplement.pdf`
- Open raw source: [raw/sources/SRC-0006-times-square-sampling-supplement.pdf](../../raw/sources/SRC-0006-times-square-sampling-supplement.pdf)
## Source bundle

This source is the supplement in the `times-square-sampling-2024` bundle. The main paper is [[wiki/sources/SRC-0005-times-square-sampling-free-energy]]. Completion for the bundle is judged across both source pages and the linked concept pages. [SRC-0005] [SRC-0006]

## Summary

The supplement supplies the detailed mathematical and implementation backing for Times Square Sampling. It is organized into theory, implementation, and numerics: stochastic approximation and iterative importance sampling, optimality proofs, visit-control analysis, TSS-versus-MBAR variance calculations, convergence proof, windowed/global estimate construction, history forgetting, multireplica recursions, jackknife error estimation, and an aqueous-solution molecular dynamics example. [SRC-0006]

For the wiki, this supplement is the key source for understanding the method at implementation depth. It gives the equations that translate the main paper's abstract stochastic approximation triple into epoch-based per-window estimates, global rung weights, visit-control offsets, reported free energies, and error bars. [SRC-0006, sections 6-9]

## Key Points

- The supplement derives the TSS recursions from general stochastic approximation and an iterative importance sampling viewpoint. [SRC-0006, section 1]
- It proves the optimal-gain statement for the free-energy and observable recursions by changing variables from $(F,\mu)$ to $(Z,\xi)$ and identifying the inverse Jacobian. [SRC-0006, section 2]
- It analyzes visit control through a steady-state approximation and the decay of a Lyapunov function. [SRC-0006, section 3]
- It derives variance formulas for TSS and MBAR, then proves a general variance-reduction theorem for TSS under the paper's assumptions. [SRC-0006, section 4]
- It proves convergence by checking stability, gain-sequence, and drift conditions for the adaptive Markov process. [SRC-0006, section 5]
- It gives practical formulas for windows, global visit-control free energies, reported free energies, history forgetting, multiple replicas, programming recursions, and jackknife error estimates. [SRC-0006, sections 6-8]
- The molecular-dynamics example studies windowing, visit control, and self-adjustment on aqueous free energy differences among amino-acid-like structures connected through alchemical paths. [SRC-0006, section 10]

## Mathematical structure

Part I is the proof layer. It starts from stochastic approximation with Markovian noise, derives iterative importance sampling recursions, proves optimality of the gain structure, analyzes visit control through Lyapunov descent, compares asymptotic variance with MBAR, and proves convergence under stated assumptions. [SRC-0006, sections 1-5]

Part II is the implementation layer. It defines a windowed invariant distribution for the triple $(X,K,J)$, constructs global quantities from local per-window estimates, introduces history forgetting and multiple replicas, spells out epoch-based programming recursions, defines jackknife error estimates, and explains the order of operations in a full TSS cycle. [SRC-0006, sections 6-9]

Part III is the numerical layer. It applies TSS to a molecular dynamics free energy problem in aqueous solution, with eight amino acid structures connected to a common substructure $X$, 400 rungs, 32 replicas, parameter sweeps, and jackknife error estimates. [SRC-0006, section 10]

## Key equations

General stochastic approximation with Markovian noise: [SRC-0006, eqs. 1.1-1.2]

$$
g(\theta)=E_\theta[G(Y;\theta)], \qquad
\theta^{t+1}=\theta^t+\frac{1}{t+1}\Gamma G(Y^{t+1};\theta^t).
$$

Windowed invariant distribution: [SRC-0006, eq. 6.4]

$$
p_{\pi,F}(x,k,j)=\frac{1}{2}1_{W_j}(\lambda_k)p_{\pi,F}(x,k).
$$

Window marginal eigenvector equation: [SRC-0006, eqs. 6.9 and 7.23-7.24]

$$
Qp=p, \qquad q_{ij}=\frac{1}{2}\frac{\sum_{k \in W_i \cap W_j}\gamma_{j;k}o_{j;k}}{\sum_{k \in W_j}\gamma_{j;k}o_{j;k}}.
$$

Global rung probability from window probabilities: [SRC-0006, eq. 7.25]

$$
q_k^t = \sum_{j \in win(k)}p_j^t\frac{\gamma_{j;k}^t o_{j;k}^t}{\sum_{\ell \in W_j}\gamma_{j;\ell}^t o_{j;\ell}^t}.
$$

Visit-control free-energy offset fixed point: [SRC-0006, eqs. 7.26-7.30]

$$
f_j^t=h_j(f^t), \qquad
h_j(f)=(\eta+1)\log g_j(f).
$$

Reported rung density and reported free energies: [SRC-0006, eqs. 6.22-6.25 and 7.31]

$$
\gamma_k^{TSS}=\sum_{j \in win(k)}p_j\gamma_{j;k}, \qquad
F_k^{TSS}=\frac{1}{\gamma_k^{TSS}}\sum_{j \in win(k)}p_j\gamma_{j;k}(F_{j;k}-f_j^{TSS}).
$$

Jackknife MSE estimate for a free-energy difference: [SRC-0006, eqs. 8.1-8.3]

$$
\widehat{MSE}(t;k,k')=\frac{1}{n(t)-n(\alpha t)}\sum_l \frac{(1-a_l)^2}{a_l}\left[(F_{e',k'}^{t,(l)}-F_{e,k}^{t,(l)})-(F_{e',k'}^t-F_{e,k}^t)\right]^2.
$$

## Equation inventory

| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |
| Stochastic approximation mean field, eq. (1.1) | SRC-0006 section 1.1 | This page; [[wiki/concepts/times-square-sampling]] | States root finding as $g(\theta)=0$. | $\theta$, $Y$, $G$, $P_\theta$ | General frame for TSS convergence. |
| Stochastic approximation update, eq. (1.2) | SRC-0006 section 1.1 | This page; [[wiki/concepts/times-square-sampling]] | Shows gain matrix and harmonic step size. | $\Gamma$, $\theta^t$, $Y^{t+1}$ | Explains optimal-gain discussion. |
| IIS-derived recursions, eqs. (1.15)-(1.16) | SRC-0006 section 1.2 | [[wiki/concepts/times-square-sampling]] | Gives partition-function coordinate view. | $Z$, $F$, importance weights | Explains why TSS uses logarithmic updates. |
| Variable change $(F,\mu)$ to $(Z,\xi)$ | SRC-0006 section 2.1 | [[wiki/concepts/times-square-sampling]] | Makes the Jacobian/gain calculation tractable. | $Z=e^{-F}$, $\xi=e^{-F}\mu$ | Supports stable recursions and optimal gain. |
| Optimal gain Jacobian | SRC-0006 section 2.2 | [[wiki/concepts/times-square-sampling]] | Proves Proposition 1. | $Jg(\theta^*)$, $\Gamma$ | Theoretical validation of recursions. |
| Visit-control steady-state calculations | SRC-0006 sections 3.1-3.2 | [[wiki/concepts/adaptive-enhanced-sampling]] | Shows how $\eta$ affects Lyapunov descent. | $\eta$, $o$, $\pi$, $V_\gamma$ | Guides turning visit control on and choosing strength. |
| TSS and MBAR covariance formulas | SRC-0006 sections 4.1-4.5 | [[wiki/concepts/on-the-fly-estimation-versus-mbar]] | Proves variance comparison. | $\Sigma_{TSS}$, $\Sigma_{MBAR}$, overlap matrix $O$ | Limits the lower-variance claim to the theorem's assumptions. |
| Windowed invariant density, eq. (6.4) | SRC-0006 section 6.1 | This page; [[wiki/concepts/tss-implementation-patterns]] | Defines stationary distribution for $(X,K,J)$. | $W_j$, $J$, $p_{\pi,F}$ | Basis for windowed TSS. |
| Window eigenvector, eqs. (6.9), (7.23)-(7.24) | SRC-0006 sections 6.1 and 7.2.1 | This page; [[wiki/concepts/tss-implementation-patterns]] | Computes window marginal probabilities. | $Q$, $p_j$, $\gamma$, $o$ | Needed for global estimates. |
| Regularized per-window rung density, eqs. (6.10), (7.18)-(7.19) | SRC-0006 sections 6.2 and 7.1.3 | [[wiki/concepts/tss-implementation-patterns]] | Keeps probabilities positive and local. | $\epsilon_\gamma$, $M(\mu)$, $\gamma_{j;k}$ | Prevents zero-probability failures. |
| Global visit-control objective, eqs. (6.18)-(6.19) | SRC-0006 section 6.2.1 | This page; [[wiki/concepts/tss-implementation-patterns]] | Defines convex optimization for sampling free energies. | $F^\circ$, $f_j$, $q_k$, $p_j$ | Global operation used for sampling. |
| Reported free-energy system, eqs. (6.22)-(6.25) | SRC-0006 section 6.2.2 | This page; [[wiki/concepts/tss-implementation-patterns]] | Combines local estimates into lower-noise reported values. | $\gamma_k^{TSS}$, $F_k^{TSS}$, $f_j^{TSS}$ | Output free energies for users. |
| Epoch counts, eqs. (7.2)-(7.4) | SRC-0006 section 7.1.1 | [[wiki/concepts/tss-implementation-patterns]] | Stores recent history across replicas. | $N_j^{t,l}(r)$, $R$, $\alpha$ | Supports bounded storage and history forgetting. |
| Importance ratio and epoch free energy, eqs. (7.5)-(7.9) | SRC-0006 section 7.1.2 | This page; [[wiki/concepts/tss-implementation-patterns]] | Updates per-window epoch and all-epoch free energies. | $R_{j;k}$, $d_j$, $F_{j;k}^{t,l}$ | Main implementation recursion. |
| Metric and observable estimates, eqs. (7.10)-(7.17) | SRC-0006 section 7.1.3 | [[wiki/concepts/free-energy-estimation]]; [[wiki/concepts/tss-implementation-patterns]] | Estimates coordinate-invariant rung density. | $g_{ij}(\lambda)$, $\psi$, $G_{j;k}$ | Required when using adaptive $\gamma(\mu)$. |
| Tilt recursions, eqs. (7.20)-(7.22) | SRC-0006 section 7.1.4 | This page; [[wiki/concepts/adaptive-enhanced-sampling]] | Implements per-window visit-control tilts. | $o_{j;k}$, $\gamma_{j;k}$ | Drives visit control. |
| Offset fixed point, eqs. (7.26)-(7.30) | SRC-0006 section 7.2.2 | This page; [[wiki/concepts/tss-implementation-patterns]] | Solves global visit-control free energies. | $f_j$, $h_j$, $g_j$, $\eta$ | Communication/global-estimator cost. |
| Jackknife MSE, eqs. (8.1)-(8.5) | SRC-0006 section 8 | This page; [[wiki/concepts/tss-implementation-patterns]] | Estimates error bars from stored epochs. | jackknife replicates, $a_l$, $\phi$, $n_{epochs}$ | Enables reported uncertainty. |
| High-frequency kernel, eqs. (10.1)-(10.2) | SRC-0006 section 10.2.3 | [[wiki/concepts/on-the-fly-estimation-versus-mbar]] | Describes repeated rung moves within one estimator-update interval. | $\nu$, $P^x$, $P^k$, $P^j$ | Practical self-adjustment mechanism. |

## Algorithmic recursions

The supplement's implementation recursions are epoch-based because history forgetting keeps only recent data. At time $t$, the recent history is approximately the interval from $\alpha t$ to $t$; epoch counts are stored by window and replica, then aggregated across replicas. [SRC-0006, section 7.1.1]

The per-window free-energy recursion uses an importance ratio $R_{j;k}^t(r)$ for replica $r$, accumulates epoch estimates $F_{j;k}^{t,l}$, and then combines current retained epochs into an all-epoch per-window estimate. This is the programming-level version of the free-energy estimator. [SRC-0006, section 7.1.2]

Observable recursions estimate the derivatives needed for the coordinate-invariant metric, including central or boundary finite differences for $\partial H / \partial \lambda$, covariance matrices, and the regularized local density $\gamma_{j;k}(\mu)$. [SRC-0006, section 7.1.3]

Tilt recursions store per-window epoch estimates $o_{j;k}^{t,l}$ and combine them into all-epoch tilts $o_{j;k}^t$. Those tilts feed the global window-weight and visit-control calculations. [SRC-0006, section 7.1.4]

Global estimates are assembled by solving $Qp=p$, computing global rung probabilities $q_k$, solving the visit-control offset fixed point, and computing reported free energies from the $\eta \to \infty$ reporting limit. [SRC-0006, section 7.2]

## Proof map

- Stochastic approximation setup: define the mean field $g(\theta)$, gain matrix $\Gamma$, harmonic step size, Markovian noise, and convergence conditions. [SRC-0006, section 1.1]
- Iterative importance sampling derivation: motivate the recursions in partition-function coordinates and explain history forgetting as an estimator design rather than a purely ad hoc burn-in removal. [SRC-0006, section 1.2]
- Optimality: change variables to $(Z,\xi)$, identify the inverse Jacobian, and show the main recursions have minimal asymptotic variance under the stated gain-matrix criterion. [SRC-0006, section 2]
- Visit control: compute uniform-distribution examples and prove improved decrease of the Lyapunov function as $\eta$ increases, while preserving the asymptotic target. [SRC-0006, section 3]
- Variance comparison: derive stochastic approximation and maximum-likelihood covariance formulas, then prove TSS's covariance for free-energy differences is no larger than MBAR's under the theorem assumptions. [SRC-0006, section 4]
- Convergence: verify stability, gain-sequence, drift, and uniform ergodicity-style assumptions to state the general convergence theorem. [SRC-0006, section 5]
- Implementation correctness: derive the invariant distribution and stitching equations that justify windowed local estimates and global reported free energies. [SRC-0006, sections 6-7]

## Implementation notes

- The supplement maps several equations to implementation function names, including `window_t::update_epoch_fe_estimates`, `window_t::estimate_all_epochs`, `window_t::normalized_weights`, `window_t::update_tilts`, `free_energy_estimator_t::window_weights_qr`, `free_energy_estimator_t::global_weights`, `free_energy_estimator_t::improve_fes`, and `free_energy_estimator_t::update_errors`. [SRC-0006, sections 7-8]
- A full cycle can run sampler-side operations and estimator-side operations separately. The global offset solve is more expensive than per-window epoch updates, and jackknife error-bar calculations can be run infrequently because they do not drive sampling. [SRC-0006, section 9]
- Multiple replicas contribute conditionally independent samples to shared estimates; the supplement's aqueous-solution example uses 32 replicas. [SRC-0006, sections 6.3 and 10.2]
- The supplement recommends $\eta=2$ as a practical default in its tested systems, $\alpha=0.19$ for history forgetting, at least 32 epochs for jackknife error estimates, $\epsilon_\gamma=0.01$, and $\epsilon_\pi=0.001$. [SRC-0006, sections 8-10]

## Evidence

The molecular-dynamics example simulates eight amino acid structures, `A, C, F, H, I, L, M, N`, sharing a common substructure $X$. Each edge from $X$ to an amino acid is discretized into 50 rungs, giving 400 total rungs; the free-energy difference for an edge is the terminal minus initial rung free energy. [SRC-0006, section 10.1]

The example compares one 400-rung window, very small windows, and the default window system. The single huge window failed after a few rung moves due to physically infeasible selections caused by unstable early estimates; very small windows completed but caused diffusive rung motion and larger/noisier error bars; the default window system mixed more effectively. [SRC-0006, section 10.2.1]

The visit-control experiments compare $\eta=0,1,2,4,16,64$. Turning visit control on removes much of the early exponential slowdown; values that are too small can leave residual slowdown, and values that are too large can make noisy tilt fluctuations dominate the visit-control distribution. [SRC-0006, section 10.2.2]

The self-adjustment experiments compare different rung-update and estimator-update intervals. Higher-frequency rung moves and estimator updates reduce estimated error, with the best tested setup reaching lower error than the default and illustrating that improved rung sampling contributes substantially to variance reduction. [SRC-0006, section 10.2.3]

## Limitations and Caveats

- The supplement's proofs depend on their stated assumptions; satisfying them in a practical MD simulation is a modeling and diagnostics issue, not an automatic consequence of running TSS. [SRC-0006, section 5]
- The reported defaults are practical recommendations from the authors' tested systems and supplement example, not guaranteed optimal settings for all free-energy problems. [SRC-0006, section 9]
- Counting-based visit-control free energies are noisy and are used for sampling rather than final reported free energies. [SRC-0006, section 6.2]
- Error bars from jackknife epochs require sufficiently long and decorrelated epochs and enough epochs for stable estimation. [SRC-0006, section 8]
- The aqueous-solution example is valuable but does not constitute broad validation across all molecular systems or all alchemical parameterizations. [SRC-0006, section 10]

## Future Directions

- The supplement supports further work on choosing window sizes, visit-control strength, update frequencies, and history-forgetting parameters for different systems. [SRC-0006, sections 9-10]
- It notes that choosing low-variance alchemical parameterizations remains active research. [SRC-0006, section 10.1]
- It points toward implementations that exploit separate sampler and estimator hardware, communication hiding, and multiple replicas. [SRC-0006, section 9]

## Links

- [[wiki/sources/SRC-0005-times-square-sampling-free-energy]]
- [[wiki/concepts/times-square-sampling]]
- [[wiki/concepts/free-energy-estimation]]
- [[wiki/concepts/adaptive-enhanced-sampling]]
- [[wiki/concepts/on-the-fly-estimation-versus-mbar]]
- [[wiki/concepts/tss-implementation-patterns]]
- [[wiki/questions/tss-generalization-scope]]

## Claims

- [[wiki/claims/CLM-0001-tss-self-adjustment-can-lower-variance]] - The supplement derives the covariance comparison supporting TSS self-adjustment under stated assumptions. [SRC-0006, section 4.5]

## Questions

- [[wiki/questions/tss-generalization-scope]] - How broadly should the TSS theory and aqueous-solution evidence transfer? [SRC-0006]
- [[wiki/questions/adaptive-estimators-vs-fixed-sample-estimators]] - How should adaptive estimator advantages be compared with fixed-sample estimators under matched assumptions? [SRC-0006]
- [[wiki/questions/overlap-support-diagnostics-for-free-energy-estimators]] - How should overlap-matrix and support assumptions be checked in practical adaptive simulations? [SRC-0006, section 4.5]
- [[wiki/questions/windowed-local-free-energy-global-profile-reliability]] - When do local TSS windows stitch into a reliable global profile? [SRC-0006, sections 6-10]

## Tensions

- [[wiki/tensions/TEN-0001-tss-variance-advantage-vs-mbar-generalization]] - The variance advantage is formal but assumption-bound. [SRC-0006, section 4.5]
- [[wiki/tensions/TEN-0005-on-the-fly-bias-adaptation-vs-postprocessing-diagnostics]] - Sampling-time adaptation needs diagnostics that account for adaptation history and correlated samples. [SRC-0006]

## Open Questions

- How should practitioners tune window size, $\eta$, $\nu$, history forgetting, and regularizers for systems that differ substantially from the supplement's aqueous-solution example? [SRC-0006]
- How much of the TSS variance advantage persists in practical simulations where samples are correlated rather than independent as assumed in the strongest variance theorem? [SRC-0005] [SRC-0006]

## Citation links

- `SRC-0023`: The supplement references Michael Shirts and John Chodera, "Statistically optimal analysis of samples from multiple equilibrium states," Journal of Chemical Physics 129. This is an exact title match to the ingested MBAR source. [SRC-0006]
- Citation review is complete for the currently ingested free-energy/adaptive-sampling cluster; it is not a full bibliography extraction.

## Metadata notes

- The source title, bundle role, source type, areas, categories, sensitivity, encryption, and `math-deep` coverage profile were inferred from the supplement title and contents.
- The file was imported as a supplement rather than merged into `SRC-0005` because source-bundle workflow assigns a stable source ID to each physical file.

## Mathematical gaps

- The wiki records the proof map and central formulas, not every intermediate proof equation in the supplement.
- Full source-code behavior and exact numerical schedules still require consulting the supplement and the linked implementation.
- Some PDF extraction artifacts affect exact typography; the raw PDF is authoritative.

## Ingestion QA

### Retrieval questions checked

- What does the supplement add beyond the main Times Square Sampling paper?
- What derivations support the stochastic approximation recursions?
- How is optimal gain proved?
- How does the supplement analyze visit control?
- How are TSS and MBAR variances compared?
- What assumptions support the convergence theorem?
- What equations implement windowing, history forgetting, multiple replicas, global estimates, and jackknife error bars?
- What does the aqueous-solution example test?
- What implementation defaults and caveats does the supplement identify?
- What claims remain bounded by validation limits?

### Coverage decision

Complete at `coverage_profile: math-deep` as the supplement component of the `times-square-sampling-2024` bundle. The supplement page and linked concept pages capture the central equations, recursions, proof structure, implementation formulas, parameter guidance, numerical evidence, and caveats needed to understand the mathematical underpinnings of TSS. [SRC-0006]

### Known gaps

- The full proofs and every intermediate equation are not reproduced.
- Full implementation requires checking the supplement and reported source repository.
- The molecular-dynamics example does not remove the broader validation caveat for TSS.
