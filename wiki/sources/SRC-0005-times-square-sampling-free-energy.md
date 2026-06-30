---
type: source
status: active
created: 2026-06-29
updated: 2026-06-29
source_id: SRC-0005
source_path: raw/sources/SRC-0005-times-square-sampling-free-energy.pdf
imported_path: raw/sources/SRC-0005-times-square-sampling-free-energy.pdf
original_path: /home/xnadre/Documentos/Times Square Sampling An Adaptive Algorithm for Free Energy Estimation.pdf
sha256: c833172f2f852948c578d6209e881babb7023fa7893c1835fdccb64743e60dd5
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
related:
  - "[[sources/SRC-0006-times-square-sampling-supplement]]"
  - "[[concepts/times-square-sampling]]"
  - "[[concepts/free-energy-estimation]]"
  - "[[concepts/adaptive-enhanced-sampling]]"
  - "[[concepts/on-the-fly-estimation-versus-mbar]]"
  - "[[concepts/tss-implementation-patterns]]"
  - "[[questions/tss-generalization-scope]]"
sources:
  - SRC-0005
  - SRC-0006
sensitivity: public
encryption: none
source_bundle: times-square-sampling-2024
bundle_role: main
ingestion_status: complete
coverage_profile: math-deep
---

# SRC-0005: Times Square Sampling: An Adaptive Algorithm for Free Energy Estimation

## Source bundle

This source is the main paper in the `times-square-sampling-2024` bundle. The supplementary material is [[sources/SRC-0006-times-square-sampling-supplement]]. Completion for the bundle is judged across both source pages and the linked concept pages. [SRC-0005] [SRC-0006]

## Summary

This 2024 paper introduces Times Square Sampling, an adaptive on-the-fly algorithm for estimating free energy differences and related observables while allocating sampling effort across a family of intermediate probability distributions. The method is built from simulated tempering, stochastic approximation, visit control, windowed local estimators, and self-adjustment through repeated sampler moves between estimator updates. [SRC-0005]

The paper's central mathematical move is to treat free energy estimation as a root-finding problem whose target, gain, and sampling distribution interact during the simulation. The supplement supplies the derivations, convergence proof structure, window-stitching equations, programming recursions, jackknife error estimates, and a molecular-dynamics numerical example. [SRC-0005] [SRC-0006]

## Key Points

- Free energy differences are negative log ratios of partition functions for parameterized Gibbs distributions, and the paper discretizes the parameter space into rungs for simulated tempering. [SRC-0005, section 2.1]
- The basic stochastic approximation recursion estimates free energies from conditional rung probabilities, but a poor initial estimate can require exponentially many steps to correct because the update observable is bounded. [SRC-0005, section 2.2.1]
- Visit control estimates rung over- or under-visitation through tilts and uses them to transiently modify the rung distribution toward under-visited rungs; the bias is designed to vanish asymptotically. [SRC-0005, eqs. 11-18]
- TSS also estimates auxiliary observable averages so that the reference rung density can be chosen from on-the-fly information such as a Fisher-information-style metric. [SRC-0005, section 2.2.2]
- The algorithm's reported recursions update free energies, observable averages, and tilts as a stochastic approximation triple. [SRC-0005, eqs. 24-26]
- The windowing system decomposes a large parameter space into overlapping local windows and then solves global stitching problems for visit-control free energies and reported free energies. [SRC-0005, section 3.1] [SRC-0006, sections 6-7]
- Self-adjustment means that current estimates influence future samples; the paper and supplement prove settings where this can have lower asymptotic variance than MBAR. [SRC-0005, proposition 3] [SRC-0006, section 4.5]
- The numerical evidence includes a shifted-Gaussian example in the main text and an aqueous-solution molecular dynamics example in the supplement. [SRC-0005, section 4] [SRC-0006, section 10]

## Mathematical structure

The source starts with a family of distributions $\rho_\lambda(x)$ over a high-dimensional state space $S$, parameterized by a lower-dimensional space $\Lambda$. A finite set of rungs $\lambda_1, \ldots, \lambda_K$ turns the problem into estimating free energies $F_k^* = -\log Z_k^*$ up to a common additive constant. [SRC-0005, section 2.1]

TSS samples an extended state $(X,K)$ or, with windows, $(X,K,J)$. For fixed estimates, simulated tempering alternates a rung move conditional on $X$ with an $X$ move conditional on $K$. Free energy estimates are then updated by stochastic approximation, using conditional probabilities over rungs rather than only the sampled rung. [SRC-0005, eqs. 2-8]

The algorithm evolves a parameter vector $\theta=(F,\mu,o)$: $F$ are free energy estimates, $\mu$ are auxiliary observable averages, and $o$ are visit-control tilts. The supplement derives these recursions through stochastic approximation and iterative importance sampling, explaining why the logarithmic partition-function coordinates are numerically useful. [SRC-0005, eqs. 24-26] [SRC-0006, sections 1-2]

For large $\Lambda$, the global problem is replaced by per-window local recursions. The supplement then reconstructs global quantities by solving an eigenvector problem for window probabilities, a convex or fixed-point problem for visit-control free-energy offsets, and a separate lower-noise reporting problem in the $\eta \to \infty$ limit. [SRC-0006, sections 6.2 and 7.2]

## Key equations

Gibbs distribution and free energy definition: [SRC-0005, eq. 1]

$$
\rho_\lambda(x) = \frac{e^{-H_\lambda(x)}}{Z_\lambda^*}, \qquad
Z_\lambda^* = \int_S e^{-H_\lambda(x)} dx, \qquad
F_\lambda^* = -\log Z_\lambda^*.
$$

Simulated-tempering target over configurations and rungs: [SRC-0005, eq. 2]

$$
p_{\gamma,F}(x,k)
= \frac{\gamma_k e^{F_k-F_k^*}}{\sum_{\ell \in [K]} \gamma_\ell e^{F_\ell-F_\ell^*}}\rho_k(x).
$$

Conditional rung probability used by the rung move and the estimator: [SRC-0005, eqs. 4 and 7]

$$
p_{\gamma,F}(k \mid x)
= \frac{\gamma_k e^{F_k-H_k(x)}}{\sum_{\ell \in [K]} \gamma_\ell e^{F_\ell-H_\ell(x)}}.
$$

Basic free energy stochastic approximation and mean field: [SRC-0005, eqs. 7-8]

$$
F_k^{t+1}=F_k^t + \frac{1}{t+1}\left(1 - \frac{p_{\gamma,F^t}(k \mid X^{t+1})}{\gamma_k}\right),
$$

$$
g_k^F(F)=1-\frac{e^{F_k-F_k^*}}{\sum_{\ell \in [K]}\gamma_\ell e^{F_\ell-F_\ell^*}}.
$$

Visit-control tilts and rung distribution: [SRC-0005, eqs. 11 and 15-17]

$$
o_k^t = \frac{1}{t}\sum_{s=1}^t \frac{1\{K^s=k\}}{\gamma_k}, \qquad
\pi_k^{TSS}(F,\gamma,o)=\frac{\gamma_k o_k^{-\eta}}{\sum_{\ell \in [K]}\gamma_\ell o_\ell^{-\eta}}.
$$

$$
\pi_k^{TSS} := (1-\epsilon_\pi)\pi_k^{TSS} + \epsilon_\pi \gamma_k.
$$

Coordinate-invariant reference density based on an observable covariance metric: [SRC-0005, eq. 19]

$$
\gamma_k \propto \det\left(E_k\left[\frac{\partial H}{\partial \lambda_i}\frac{\partial H}{\partial \lambda_j}\right]
- E_k\left[\frac{\partial H}{\partial \lambda_i}\right]E_k\left[\frac{\partial H}{\partial \lambda_j}\right]\right)^{1/2}.
$$

Lyapunov function used for convergence and visit-control comparison: [SRC-0005, eq. 27]

$$
V_\gamma(F)=D_{KL}(\gamma\Vert r(F))=-\sum_k \gamma_k \log\frac{r_k(F)}{\gamma_k}.
$$

Windowed invariant distribution and global visit-control condition: [SRC-0005, eqs. 32-33] [SRC-0006, eqs. 6.4 and 6.11]

$$
p_{\pi,F}(x,k,j)=\frac{1}{2}1_{W_j}(\lambda_k)p_{\pi,F}(x,k),
$$

$$
\sum_j p_j \frac{\gamma_{j;k}(\mu)o_{j;k}}{\sum_{\ell \in W_j}\gamma_{j;\ell}(\mu)o_{j;\ell}}
=
\sum_j p_j \frac{\pi_{j;k}e^{F_{j;k}-F_k^\circ}}{\sum_{\ell \in W_j}\pi_{j;\ell}e^{F_{j;\ell}-F_\ell^\circ}}.
$$

## Equation inventory

| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |
| Gibbs density and partition function, eq. (1) | SRC-0005 section 2.1 | This page, Key equations; [[concepts/free-energy-estimation]] | Defines the free energy target. | $H_\lambda$, $Z_\lambda^*$, $F_\lambda^*$, $S$ | Required for any implementation or interpretation of estimated free energy differences. |
| Simulated-tempering target, eq. (2) | SRC-0005 section 2.1 | This page; [[concepts/times-square-sampling]] | Defines the joint target over configurations and rungs. | $\gamma$, $F$, $F^*$, $\rho_k$ | Drives rung probabilities and conditional sampling. |
| Rung and state transition kernels, eqs. (4)-(5) | SRC-0005 section 2.1 | [[concepts/times-square-sampling]]; [[concepts/tss-implementation-patterns]] | Splits the Markov transition into rung and configuration moves. | $P^k$, $P^x$, $T_k$, $X$, $K$ | Maps directly to sampler cycle design. |
| Basic free-energy recursion and mean field, eqs. (7)-(8) | SRC-0005 section 2.1 | This page; [[concepts/free-energy-estimation]] | Frames free energy estimation as stochastic root finding. | $F_k^t$, $p(k \mid x)$, $\gamma_k$ | Core estimator before TSS-specific modifications. |
| Tilt estimator and tilt mean field, eqs. (11), (13)-(14) | SRC-0005 section 2.2.1 | This page; [[concepts/adaptive-enhanced-sampling]] | Measures empirical rung visitation relative to target. | $o_k$, $K^s$, $\gamma_k$ | Basis for visit control and diagnostics. |
| Visit-control density and regularization, eqs. (15)-(18) | SRC-0005 section 2.2.1 | This page; [[concepts/adaptive-enhanced-sampling]] | Biases sampling toward under-visited rungs while preserving positive probabilities. | $\pi^{TSS}$, $\eta$, $\epsilon_\pi$, $o$ | Main convergence-acceleration mechanism. |
| Fisher-information-style rung density, eq. (19) | SRC-0005 section 2.2.2 | This page; [[concepts/times-square-sampling]] | Makes the reference rung density coordinate-aware. | $\gamma_k$, $\mu$, $\partial H / \partial \lambda$ | Requires auxiliary observable estimation. |
| Auxiliary observable recursion, eqs. (20)-(21), (25) | SRC-0005 sections 2.2.2 and 2.2.4 | This page; [[concepts/times-square-sampling]] | Estimates ensemble averages needed for adaptive rung allocation. | $\mu_{km}$, $\psi_m$, $\pi_k$ | Used to compute $\gamma(\mu)$ and metrics. |
| TSS stochastic approximation triple, eqs. (24)-(26) | SRC-0005 section 2.2.4 | This page, Algorithmic recursions; [[concepts/times-square-sampling]] | Defines the single-window estimator updates. | $F$, $\mu$, $o$, $\theta$ | Direct algorithmic recurrence. |
| Relative-entropy Lyapunov function, eq. (27) | SRC-0005 section 2.2.4 | This page; [[concepts/adaptive-enhanced-sampling]] | Proves convergence and compares visit-control strength. | $V_\gamma$, $r(F)$, $\gamma$ | Theoretical validation boundary, not an implementation formula. |
| Window transition and invariant distribution, eqs. (30)-(32) | SRC-0005 section 3.1 | This page; [[concepts/tss-implementation-patterns]] | Introduces $(X,K,J)$ and local window dynamics. | $W_j$, $J$, $win(k)$ | Enables scalable local energy evaluations. |
| Global visit-control relation, eq. (33) | SRC-0005 section 3.1 | This page; [[concepts/tss-implementation-patterns]] | Stitches local tilts into global visit-control free energies. | $p_j$, $F_k^\circ$, $\gamma_{j;k}$, $o_{j;k}$ | Used for sampling but too noisy for final reporting. |
| Epoch and global programming recursions | SRC-0006 sections 7-8 | [[sources/SRC-0006-times-square-sampling-supplement]]; [[concepts/tss-implementation-patterns]] | Converts the mathematical estimator into stored epochs, global weights, offsets, and error bars. | $N_j$, $R_{j;k}$, $Q$, $q_k$, $f_j$, jackknife replicates | Necessary for close implementation use. |
| Variance comparison with MBAR | SRC-0005 proposition 3; SRC-0006 section 4.5 | [[concepts/on-the-fly-estimation-versus-mbar]] | Formalizes the self-adjustment advantage under stated assumptions. | $\Sigma_{TSS}$, $\Sigma_{MBAR}$, overlap matrix $O$, $\pi$ | Supports the lower-variance claim but only under the paper's assumptions. |

## Algorithmic recursions

For the single-window algorithm, each cycle samples a rung using the current parameter vector $\theta^t$, samples a configuration conditional on that rung, and updates $\theta=(F,\mu,o)$ with equations (24)-(26). [SRC-0005, algorithm 1]

The logarithmic free-energy update used by TSS can be read as an iterative-importance-sampling form of the stochastic approximation update: [SRC-0005, eq. 24] [SRC-0006, sections 1.2 and 2.1]

$$
F_k^{t+1}=F_k^t-\log\left(1+\frac{1}{t+1}\left(w_k^t(X^{t+1})-1\right)\right),
$$

where

$$
w_k^t(x)=\frac{e^{F_k^t-H_k(x)}}{\sum_{\ell \in [K]}\pi_\ell(\theta^t)e^{F_\ell^t-H_\ell(x)}}.
$$

The auxiliary observable update uses the same Rao-Blackwellized weight and a rescaling by the free-energy change: [SRC-0005, eq. 25]

$$
\mu_{km}^{t+1}=e^{F_k^{t+1}-F_k^t}\left(\mu_{km}^t+\frac{1}{t+1}w_k^t(X^{t+1})(\psi_m(X^{t+1})-\mu_{km}^t)\right).
$$

The tilt recursion is a running visit-frequency estimator relative to the current reference density: [SRC-0005, eq. 26]

$$
o_k^{t+1}=o_k^t+\frac{1}{t+1}\left(\frac{1\{K^{t+1}=k\}}{\gamma_k(\mu^t)}-o_k^t\right).
$$

For the windowed implementation, the supplement converts these recursions into epoch-based stored estimates, then combines them through global window weights and offset solves. The essential sequence is: update per-window epoch counts, update per-window free energies and observables with importance ratios, update tilts, solve window marginal probabilities, compute global rung probabilities, solve visit-control offsets, and compute lower-noise reported free energies. [SRC-0006, sections 7.1-7.2]

## Proof map

- Proposition 1, optimal gain: the supplement changes variables from $(F,\mu)$ to $(Z,\xi)$, computes the Jacobian of the mean field, and shows that the free-energy and observable recursions use the asymptotically optimal gain; if $\pi=\pi^\circ$, adding the tilt recursion is also optimal. [SRC-0005, proposition 1] [SRC-0006, section 2.2]
- Proposition 2, visit-control acceleration: the proof analyzes the derivative of the relative-entropy Lyapunov function and shows stronger visit control decreases it faster, with equality only at the free-energy solution up to a constant shift. [SRC-0005, proposition 2] [SRC-0006, section 3.2]
- Proposition 3 and Theorem 4.1, self-adjustment versus MBAR: the supplement derives TSS and MBAR covariance matrices using an overlap matrix and proves positive semidefiniteness of the MBAR-minus-TSS covariance form under irreducibility and independent-sample assumptions. [SRC-0005, proposition 3] [SRC-0006, section 4.5]
- Convergence theorem: the supplement proves convergence by establishing stability, a global Lyapunov function, gain-sequence assumptions, and drift conditions for the adaptive Markov process. [SRC-0006, section 5]
- Windowing derivations: the supplement derives the windowed invariant distribution, global visit-control optimization, reported-free-energy offsets, and programming recursions used to implement the method. [SRC-0006, sections 6-7]

## Implementation notes

- The source code for TSS is reported as available from D. E. Shaw Research at `https://github.com/DEShawResearch/tss`. [SRC-0005, data availability statement]
- Windowing is not just an optimization: the supplement's aqueous-solution example reports that one 400-rung window failed after a few rung moves because poor early free-energy estimates allowed physically infeasible rung selections. [SRC-0006, section 10.2.1]
- In the supplement's parameter guidance, visit control should generally be turned on; $\eta=2$ worked well across the authors' tested systems, while very small or very large values can slow convergence or introduce noisy random bias. [SRC-0006, sections 9 and 10.2.2]
- History forgetting stores recent epochs only; the supplement recommends $\alpha=0.19$, at least 32 epochs, and $\phi=\alpha^{-1/n_{epochs}}$ so jackknife pseudo-values can be treated as approximately independent. [SRC-0006, sections 8-9]
- The supplement recommends small regularizers such as $\epsilon_\gamma=0.01$ and $\epsilon_\pi=0.001$ in its practical guidance, while noting that these are safeguards for visitation and not universal tuning laws. [SRC-0006, section 9]

## Evidence

- The main text uses a shifted-Gaussian example to show exponential slowdown without visit control, improvement with visit control, scaling benefits from windows, and variance reduction from additional sampler moves per estimator update. [SRC-0005, section 4]
- The supplement's aqueous-solution example uses eight amino acid structures connected to a common substructure by alchemical free-energy paths, 400 rungs, 32 replicas, jackknife error estimates, and parameter sweeps for windowing, visit control, and self-adjustment. [SRC-0006, section 10]
- In that supplement example, a single large 400-rung window failed, size-2 windows were stable but diffusive with larger/noisier error bars, the default window system mixed more effectively, visit control removed early exponential slowdown, and higher-frequency rung or estimator updates reduced error. [SRC-0006, sections 10.2.1-10.2.3]

## Limitations and Caveats

- The convergence arguments rely on stated assumptions, including compactness, regularity, ergodicity, stability, gain-sequence, and drift conditions; practical MD implementations still need mixing diagnostics. [SRC-0005, section 2.2.4] [SRC-0006, section 5]
- The variance advantage over MBAR is proven for specific on-the-fly settings where TSS samples from the adaptive target and can use estimate information during sampling; it should not be read as a blanket claim that MBAR is inferior. [SRC-0005, proposition 3] [SRC-0006, section 4.5]
- Visit-control free energies depend on noisy counting tilts and are recommended for sampling, not final reporting. The supplement defines separate reported free energies to reduce this noise near convergence. [SRC-0006, sections 6.2.1-6.2.2]
- Window size is a tradeoff: too large can permit unstable, physically infeasible rung jumps early in a simulation, while too small can make rung dynamics diffusive and increase error bars. [SRC-0006, sections 9 and 10.2.1]
- The paper is promising but not universally validated. The main paper uses a Gaussian model, and the supplement adds one aqueous-solution molecular dynamics study; the wiki should not treat this as broad benchmarking across chemical systems. [SRC-0005, section 4] [SRC-0006, section 10]

## Future Directions

- The paper raises the possibility that on-the-fly estimation could reduce variance in other statistical applications beyond free energy estimation. [SRC-0005, introduction]
- It suggests that more useful adaptive rung-allocation functions may exist beyond the visit-control form studied in the paper. [SRC-0005, section 2.2.1]
- The implementation discussion points toward distributed sampler-estimator architectures, communication hiding, multiple replicas, and further chemical physics applications. [SRC-0005, section 3] [SRC-0006, section 9]
- The supplement notes that alchemical parameterizations with low-variance free energy estimates remain an active area of research. [SRC-0006, section 10.1]

## Links

- [[sources/SRC-0006-times-square-sampling-supplement]]
- [[concepts/times-square-sampling]]
- [[concepts/free-energy-estimation]]
- [[concepts/adaptive-enhanced-sampling]]
- [[concepts/on-the-fly-estimation-versus-mbar]]
- [[concepts/tss-implementation-patterns]]
- [[questions/tss-generalization-scope]]

## Open Questions

- [[questions/tss-generalization-scope]] - How broadly should the lower-variance and resource-allocation claims be expected to transfer beyond the paper's analyzed settings? [SRC-0005] [SRC-0006]

## Metadata notes

- The main paper was already imported as `SRC-0005`; its SHA256 matches the user-provided file for this bundle pass, so it was not duplicated.
- The bundle metadata, source type, areas, categories, sensitivity, encryption, and `math-deep` coverage profile were inferred from the title and content. No ambiguity blocked safe ingestion.
- The supplement is represented separately as `SRC-0006` because each physical file receives its own source ID under the source-bundle workflow.

## Mathematical gaps

- The wiki records the central equations, dependencies, recursions, and proof map, but does not reproduce the full proofs from the supplement.
- Some displayed formulas in PDF text extraction are fragile; the raw PDFs remain authoritative for exact typography and all lower-level implementation details.
- The wiki does not reproduce source-code-level C++ implementation details beyond the supplement's named formula-to-function mappings.

## Ingestion QA

### Retrieval questions checked

- What mathematical problem is Times Square Sampling solving?
- How are free energies, partition functions, rungs, and simulated-tempering targets defined?
- What are the core free-energy, auxiliary-observable, and tilt recursions?
- Why is visit control introduced, and what equations define it?
- How does the windowed version stitch local estimates into global sampling and reporting quantities?
- What does self-adjustment mean mathematically, and why can it beat MBAR under the paper's assumptions?
- What proof structure supports optimality, visit-control acceleration, variance reduction, and convergence?
- What implementation formulas matter for epochs, history forgetting, multiple replicas, global weights, and error bars?
- What numerical evidence supports the method in both the main paper and supplement?
- What claims should not be overgeneralized?

### Coverage decision

Complete at `coverage_profile: math-deep` for the `times-square-sampling-2024` bundle. The main source page, supplement source page, and linked concept pages represent the central mathematical definitions, key equations, algorithmic recursions, equation dependencies, proof map, implementation formulas, numerical evidence, limitations, and open questions needed for future retrieval about the method's underlying math. [SRC-0005] [SRC-0006]

### Known gaps

- Full proof reproduction is intentionally omitted; the wiki provides proof maps and key dependencies instead.
- Full source-code behavior must still be checked against the reported D. E. Shaw Research implementation for close reimplementation.
- Broader empirical validation beyond the paper's Gaussian and aqueous-solution examples remains an open validation boundary.
