---
type: source
status: active
created: 2026-09-25
updated: 2026-09-25
source_id: SRC-0091
display_title: "Use of the Weighted Histogram Analysis Method for the Analysis of Simulated and Parallel Tempering Simulations"
short_title: "WHAM for Simulated and Parallel Tempering (STWHAM/PTWHAM)"
aliases:
  - "SRC-0091"
  - "STWHAM"
  - "PTWHAM"
  - "WHAM for Simulated and Parallel Tempering"
  - "Use of the Weighted Histogram Analysis Method for the Analysis of Simulated and Parallel Tempering Simulations"
source_path: raw/sources/SRC-0091-use-of-the-weighted-histogram-analysis-method-for.pdf
imported_path: raw/sources/SRC-0091-use-of-the-weighted-histogram-analysis-method-for.pdf
original_filename: "ct0502864.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 6096d46001873f16e242d8dd24a37a3a2a6f75ec4a4740053955e330a67991e0
authors:
  - "John D. Chodera"
  - "William C. Swope"
  - "Jed W. Pitera"
  - "Chaok Seok"
  - "Ken A. Dill"
author_entities:
  - "[[wiki/entities/authors/john-d-chodera]]"
year: 2007
venue: "Journal of Chemical Theory and Computation"
doi: "10.1021/ct0502864"
arxiv:
metadata_review_status: reviewed
areas:
  - research
categories:
  - research/molecular-simulation/free-energy
  - research/molecular-simulation/molecular-dynamics
  - research/statistics/monte-carlo
tags:
  - wham
  - simulated-tempering
  - parallel-tempering
  - replica-exchange
  - statistical-inefficiency
  - autocorrelation
  - potential-of-mean-force
  - histogram-analysis
  - math-heavy
related:
  - "[[wiki/sources/SRC-0090-a-simple-method-for-automated-equilibration-detection-in]]"
  - "[[wiki/concepts/statistical-inefficiency-and-automated-equilibration-detection]]"
  - "[[wiki/entities/authors/john-d-chodera]]"
sources:
  - SRC-0091
cites_sources: []
citation_match_status: reviewed
cqt_review_status: linked
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: math-deep
---

# Use of the Weighted Histogram Analysis Method for the Analysis of Simulated and Parallel Tempering Simulations

Source ID: `SRC-0091`

## Raw source

- Repository path: `raw/sources/SRC-0091-use-of-the-weighted-histogram-analysis-method-for.pdf`
- Open raw source: [raw/sources/SRC-0091-use-of-the-weighted-histogram-analysis-method-for.pdf](../../raw/sources/SRC-0091-use-of-the-weighted-histogram-analysis-method-for.pdf)

## Summary

This JCTC paper (received 21 Nov 2005, published 3, 26-41, 2007) re-derives the weighted histogram analysis method (WHAM) of Kumar et al. with careful treatment of statistical uncertainty, and then extends it to two generalized-ensemble simulation protocols whose data cannot be correctly analyzed by directly applying the original (independent-canonical-simulation) WHAM: simulated tempering (STWHAM) and parallel tempering / replica-exchange among temperatures (PTWHAM). [SRC-0091]

The central methodological problem addressed is that prior attempts to apply WHAM to simulated or parallel tempering data either ignored temporal correlation entirely or destroyed it by regrouping configurations into pseudo-trajectories sorted by temperature, which obscures the true (per-replica) correlation time and introduces spurious correlation between the resulting pseudo-trajectories. [SRC-0091] The paper's STWHAM and PTWHAM instead operate directly on the unpermuted simulated-tempering trajectory or the parallel-tempering replica trajectories, and explicitly propagate the effect of temporal correlation (via the statistical inefficiency $g$) into both the WHAM density-of-states/free-energy equations and the uncertainty of any resulting canonical expectation. [SRC-0091]

Section 5 ("Practical Considerations") of the paper addresses implementation details omitted or under-specified in prior WHAM literature, most importantly Section 5.2, which describes the "fast multiscale" method for computing the integrated autocorrelation time / statistical inefficiency $g$ from a finite, noisy trajectory. This is the estimator cited by [[wiki/sources/SRC-0090-a-simple-method-for-automated-equilibration-detection-in]] (ref. 10, "section 5.2") as the one used to produce that paper's numerical results and distributed in `pymbar.timeseries`. [SRC-0090; SRC-0091]

The method is validated on a 1D asymmetric double-well Metropolis Monte Carlo model system and then applied to compute the potential of mean force (PMF) in the $\psi$ backbone torsion of alanine dipeptide from parallel tempering simulations in implicit and explicit solvent. [SRC-0091]

## Key Points

- WHAM combines histogram-based density-of-states estimates $\hat\Omega_{mk}$ from $K$ independent canonical simulations at different inverse temperatures $\beta_k$ into a single optimal density-of-states estimate $\hat\Omega_m$, using inverse-variance weighting; canonical expectations $A_\beta$ at any temperature of interest are then obtained by reweighting all stored configurations. [SRC-0091, section 2]
- The paper's key methodological contribution relative to earlier WHAM presentations (including its own application to generalized-ensemble data) is to properly account for the statistical inefficiency $g$ of each simulation/energy bin when estimating histogram-count uncertainties, rather than assuming (as had been implicitly done in the literature, including refs 1 and 4) that all $g_{mk}=1$. [SRC-0091, section 2.5, section 5.3]
- Both new expectation estimators are recast as **weighted sums over all stored configurations** (not just the discretized histogram), avoiding the need for many-dimensional histograms when multiple observables are of interest. [SRC-0091, eqs. 37-38, 58-59, 67-68]
- **Simulated tempering (STWHAM)**: a single trajectory performs a random walk among a discrete set of temperatures $\beta_1,\dots,\beta_L$ using tunable weights $a_l$ and a Metropolis-like acceptance rule (eq. 49); WHAM is applied directly to this trajectory without reordering, using a single statistical inefficiency $g_m$ per energy bin (not per temperature) because the trajectory itself is treated as one mixed-canonical time series. [SRC-0091, section 3.1]
- **Parallel tempering (PTWHAM)**: $K$ replicas are simulated at fixed inverse temperatures $\beta_1,\dots,\beta_K$ (here $L=K$), with configuration/temperature swaps accepted via a Metropolis-like criterion (eq. 61); each replica trajectory is treated as one of $K$ independent "simulated-tempering-like" time series, each capable of visiting all $L$ temperatures, and their per-replica density-of-states estimates are optimally combined exactly as in the independent-canonical-simulation case. [SRC-0091, section 3.2]
- The dominant source of statistical uncertainty in parallel/simulated tempering WHAM estimates is usually the small effective number of independent samples of the *observable* (due to time correlation within a replica), not uncertainty in the WHAM free energies $\{f_k\}$ themselves — provided the observable's correlation time is not itself comparable to that of the potential energy; the paper explicitly neglects $\{f_k\}$ uncertainty throughout and flags this as an open issue for future work (mentioning Gallicchio et al.'s T-WHAM, ref 24, as a possible route to a more complete treatment). [SRC-0091, sections 2.7, 3.1, 6]
- **Practical Considerations (section 5)** covers four issues largely unaddressed in prior WHAM literature: (5.1) bias-variance tradeoff in energy-histogram bin width; (5.2) how to efficiently and robustly compute the integrated autocorrelation time / statistical inefficiency $g$ from a finite noisy trajectory (the estimator SRC-0090 needed); (5.3) whether it is safe to neglect the dependence of $g_{mk}$ on energy bin, temperature, and replica (empirically, no — differences of up to two orders of magnitude were observed); (5.4) how to bound/regularize the statistical inefficiency of a cross-correlation term so that error-propagation formulas cannot return a negative squared uncertainty. [SRC-0091, section 5]
- Validated against ground truth on a 1D asymmetric double-well Monte Carlo potential (eq. 69) for MMC, independent multi-temperature MMC, ST, and PT protocols: computed uncertainty estimates track the true block-to-block deviation closely (confidence curves, Figure 1), and bias is small (<10% of the reported uncertainty). [SRC-0091, section 4.1]
- Applied to alanine dipeptide (implicit Generalized-Born solvent, 10 replicas, 273-600 K; and explicit TIP3P solvent, 40 replicas, 273-600 K) to compute the $\psi$-torsion PMF and per-bin uncertainty from parallel tempering; block-based confidence curves again show good agreement between predicted and true uncertainty. [SRC-0091, section 4.2, Figures 3-4]

## Key equations

### 2. WHAM for independent canonical simulations (baseline re-derivation)

Canonical expectation and its density-of-states form:

$$
A_\beta \equiv \frac{\int d\mathbf q\, e^{-\beta U(\mathbf q)} A(\mathbf q)}{\int d\mathbf q\, e^{-\beta U(\mathbf q)}},
\qquad
A_\beta = \frac{\int dU\, \Omega(U)\, e^{-\beta U} A(U)}{\int dU\, \Omega(U)\, e^{-\beta U}} .
$$

[SRC-0091, eqs. 1, 3]

Per-simulation density-of-states estimate, from the discretized histogram $H_{mk}$ (count of configurations from simulation $k$ in energy bin $m$) and dimensionless free energy $f_k\equiv-\ln Z(\beta_k)$:

$$
\hat\Omega_{mk} = \frac{H_{mk}}{N_k\,\Delta U\,\exp[f_k-\beta_k U_m]} .
$$

[SRC-0091, eq. 11]

Combined (WHAM) density-of-states estimate and self-consistency equation for the free energies, obtained by inverse-variance-weighting the per-simulation estimates (eqs. 22-30) under the sparse-histogram approximation $\delta^2 H_{mk}\approx g_{mk}H_{mk}$ (eq. 27):

$$
\hat\Omega_m = \frac{\displaystyle\sum_{k=1}^{K} g_{mk}^{-1} H_{mk}}
{\displaystyle\sum_{k=1}^{K} g_{mk}^{-1} N_k \Delta U \exp[f_k-\beta_k U_m]},
\qquad
f_k = -\ln\sum_{m=1}^{M}\hat\Omega_m\,\Delta U\, e^{-\beta_k U_m} .
$$

[SRC-0091, eqs. 30-31]

Uncertainty of the combined density-of-states estimate and its relative form:

$$
\delta^2\hat\Omega_m = \frac{\hat\Omega_m}{\displaystyle\sum_{k=1}^{K} g_{mk}^{-1} N_k \Delta U \exp[f_k-\beta_k U_m]},
\qquad
\frac{\delta^2\hat\Omega_m}{\hat\Omega_m^2} = \Big[\sum_{k=1}^{K} g_{mk}^{-1} H_{mk}\Big]^{-1} .
$$

[SRC-0091, eqs. 32-33]

Expectation of an observable $A$ recast as a weighted sum over **all stored configurations** (not just histogram bins), with per-configuration weight $w_{kn}(\beta)$:

$$
\hat A(\beta) = \frac{\displaystyle\sum_{k=1}^{K}\sum_{n=1}^{N_k} w_{kn}(\beta) A_{kn}}
{\displaystyle\sum_{k=1}^{K}\sum_{n=1}^{N_k} w_{kn}(\beta)},
\qquad
w_{kn}(\beta) = \sum_{m=1}^{M}\psi_{mkn}\, H_m^{-1}\,\hat\Omega_m\, e^{-\beta U_{kn}} .
$$

[SRC-0091, eqs. 37-38]

### 2.7 / Appendix A. Uncertainty of an expectation, and the general statistical-inefficiency / autocorrelation-time system

Writing the expectation estimator as a ratio of weighted sums, $\hat A_\beta=\hat X/\hat Y$, with $X\equiv\sum_k N_k X_k$, $Y\equiv\sum_k N_k Y_k$ (per-simulation block averages $X_k,Y_k$ of $w_{kn}A_{kn}$ and $w_{kn}$), first-order error propagation gives:

$$
\delta^2\hat A = \Big[\frac{\hat X}{\hat Y}\Big]^2\Big[\frac{\delta^2\hat X}{\hat X^2}+\frac{\delta^2\hat Y}{\hat Y^2}-\frac{2\,\delta\hat X\delta\hat Y}{\hat X\hat Y}\Big],
\qquad
\delta^2 X = \sum_{k=1}^K N_k^2\,\delta^2 X_k,\ \ \delta^2 Y=\sum_k N_k^2\,\delta^2 Y_k,\ \ \delta X\delta Y=\sum_k N_k^2\,\delta X_k\delta Y_k .
$$

[SRC-0091, eqs. 41, 43]

This is the general definition of statistical inefficiency and integrated autocorrelation time used throughout the paper (identical in form to Eqs. 10-13 already recorded on [[wiki/sources/SRC-0090-a-simple-method-for-automated-equilibration-detection-in]] and [[wiki/concepts/statistical-inefficiency-and-automated-equilibration-detection]]):

$$
\delta^2\hat X = \frac{\sigma_x^2}{N/g},
\qquad
\sigma_x^2 \equiv \overline{x_n^2}-\overline{x_n}^2,
\qquad
g \equiv 1+2\tau,
$$

$$
\tau \equiv \sum_{t=1}^{N-1}\Big(1-\frac{t}{N}\Big)C_t,
\qquad
C_t \equiv \frac{\overline{x_n x_{n+t}}-\overline{x_n}^2}{\overline{x_n^2}-\overline{x_n}^2} .
$$

[SRC-0091, eqs. 15, 17-21]

### Cross-correlation between two observables (needed for the ratio estimator's uncertainty)

Because $\hat A_\beta$ is a ratio $\hat X/\hat Y$ of two generally correlated weighted averages, the per-simulation uncertainty terms in eq. 41 require both the statistical inefficiencies of $X$ and $Y$ individually and a **cross statistical inefficiency**. Defining, for simulation $k$, the paired series $x_{kn}\equiv w_{kn}A_{kn}$ and $y_{kn}\equiv w_{kn}$:

$$
\delta^2 X_k = \frac{\sigma_{k,x,x}^2}{N_k/g_{k,x,x}},
\qquad
\delta^2 Y_k = \frac{\sigma_{k,y,y}^2}{N_k/g_{k,y,y}},
\qquad
\delta X_k\delta Y_k = \frac{\sigma_{k,x,y}^2}{N_k/g_{k,x,y}} .
$$

[SRC-0091, eq. 44]

Sample cross-covariance, cross statistical inefficiency, cross integrated correlation time, and the cross-correlation-function estimator (using stationarity and time-reversibility exactly as in the single-observable case):

$$
\hat\sigma_{k,x,y}^2 = \frac{1}{N_k-1}\sum_{n=1}^{N_k}(x_{kn}-\hat X_k)(y_{kn}-\hat Y_k),
\qquad
g_{k,x,y} \equiv 1+2\tau_{k,x,y},
$$

$$
\tau_{k,x,y} \equiv \sum_{t=1}^{N_k-1}\Big(1-\frac{t}{N_k}\Big) C_{kt,x,y},
$$

$$
C_{kt,x,y} \approx \frac{1}{2\hat\sigma_{k,x,y}^2}\,\frac{1}{N_k-t}\sum_{n=1}^{N_k-t}\Big[(x_{kn}-\hat X_k)(y_{k,n+t}-\hat Y_k) + (y_{kn}-\hat Y_k)(x_{k,n+t}-\hat X_k)\Big] .
$$

[SRC-0091, eqs. 45-48]

The paper explicitly notes: *"See section 5.2 for a discussion on efficiently computing the integrated correlation time $\tau$ from $\hat C_{kt,x,y}$."* [SRC-0091, p. 33, following eq. 48] — i.e., the section 5.2 multiscale/truncation procedure (below) is applied identically to the cross-correlation function $C_{kt,x,y}$, not only to the single-observable autocorrelation function $C_t$.

### 3.1 STWHAM (simulated tempering)

Metropolis-like acceptance rule for a proposed temperature change $\beta_l\to\beta_{l'}$ (tunable weights $a_l$):

$$
P(\beta_l\to\beta_{l'}) = \min\{1,\ \exp[-(\beta_{l'}-\beta_l)U + (a_{l'}-a_l)]\} .
$$

[SRC-0091, eq. 49]

Mixed-canonical probability density for energy bin $m$, and the resulting WHAM-style density-of-states and free-energy equations for the single simulated-tempering trajectory (only one statistical inefficiency $g_m$ per bin, not per temperature, because there is one trajectory):

$$
p_m = \Omega_m\sum_{l=1}^{L}\frac{N_l}{N}\exp[f_l-\beta_l U_m],
\qquad
\hat\Omega_m = \frac{H_m}{\displaystyle\sum_{l=1}^{L} N_l\,\Delta U\,\exp[f_l-\beta_l U_m]},
\qquad
f_l = -\ln\sum_{m=1}^{M}\hat\Omega_m\,\Delta U\,e^{-\beta_l U_m} .
$$

[SRC-0091, eqs. 51, 53-54]

Uncertainty, using a single per-bin statistical inefficiency $g_m$:

$$
\delta^2\hat\Omega_m = \frac{\hat\Omega_m}{g_m^{-1}\displaystyle\sum_{l=1}^{L} N_l\,\Delta U\,\exp[f_l-\beta_l U_m]} .
$$

[SRC-0091, eq. 57]

### 3.2 PTWHAM (parallel tempering / replica exchange among temperatures)

Metropolis-like replica-swap acceptance rule between replicas $i,j$ at inverse temperatures $\beta_i,\beta_j$:

$$
P_\text{exch} = \min\{1,\exp[-(\beta_j-\beta_i)(U_i-U_j)]\} .
$$

[SRC-0091, eq. 61]

Per-replica density-of-states estimates (each replica treated as an independent trajectory visiting all $L$ temperatures) are combined by the same optimal-combination rule as eq. 13/eq. 30, giving the PTWHAM density-of-states equation, and an equivalent form in terms of *effective* histogram counts and *effective* sample sizes $H_m^\text{eff}\equiv\sum_k g_{mk}^{-1}H_{mk}$, $N_{ml}^\text{eff}\equiv\sum_k g_{mk}^{-1}N_{kl}$:

$$
\hat\Omega_m = \frac{\displaystyle\sum_{k=1}^{K} g_{mk}^{-1} H_{mk}}
{\displaystyle\sum_{k=1}^{K} g_{mk}^{-1}\sum_{l=1}^{L} N_{kl}\,\Delta U\,\exp[f_l-\beta_l U_m]}
= \frac{H_m^\text{eff}}{\displaystyle\sum_{l=1}^{L} N_{ml}^\text{eff}\,\Delta U\,\exp[f_l-\beta_l U_m]} .
$$

[SRC-0091, eqs. 64, 66]

## Section 5.2: computing integrated correlation times — the "fast multiscale" statistical-inefficiency estimator

This is the section cited by [[wiki/sources/SRC-0090-a-simple-method-for-automated-equilibration-detection-in]] (as "ref 10, section 5.2") for the statistical-inefficiency estimator used to produce that paper's results. Its content, reproduced in full below, resolves that paper's previously recorded "Mathematical gap." [SRC-0090; SRC-0091, section 5.2]

**Problem.** Estimating the integrated correlation time $\tau$ (eqs. 19, 21, or the cross-correlation analogue eqs. 47-48) from a finite trajectory is difficult because a naive plug-in estimate of the normalized fluctuation autocorrelation function $C_t$ has statistical error that grows approximately linearly with lag $t$. Even for trajectories many times longer than the true correlation length, summing $C_t$ over its *entire* range (as eq. 19 literally specifies) is dominated by this growing noise in the tail, and can produce large errors or even unphysical negative estimates of $\tau$. [SRC-0091, section 5.2]

**Two rejected prior approaches (cited, not adopted).** Janke proposed a self-consistent scheme that truncates the sum at lag $6\tau$ (ref. 23 in SRC-0091), after which $C_t$ is assumed negligible; Evertz argued this produces incorrect results and instead proposed fitting an exponential to the noisy tail and using the fit to evaluate the summand there (ref. 43 in SRC-0091). The paper states neither approach is "both stable and straightforward to apply." [SRC-0091, section 5.2]

**Adopted truncation rule (stopping rule).** The sum defining $\tau$ (eq. 19, or its cross-correlation analogue) is truncated at the first lag $t$ where the normalized fluctuation correlation function $C_t$ crosses zero, on the reasoning that a negative correlation is "likely unphysical ... for most observables" and its appearance signals that statistical noise, not signal, dominates the remainder of the correlation function — so the remaining terms are treated as indistinguishable from zero and dropped. The paper notes velocity autocorrelation functions (which have a genuine negative peak at short times) as an explicit exception where this heuristic would be inappropriate. [SRC-0091, section 5.2]

**Adopted multiscale lag-time (subsampling) scheme.** Rather than evaluating $C_t$ at every integer lag $t=1,2,\dots$ up to the truncation point — expensive because real correlation functions typically decay quickly at first and then slowly, roughly exponentially, for large $t$ — the paper evaluates $C_t$ only at a geometrically/quadratically sparsified set of lag times

$$
t_i = 1 + \frac{i(i-1)}{2}, \qquad i = 1, 2, 3, \dots
$$

and approximates the sum in eq. 19 (or eqs. 47-48 for the cross-correlation case) using only these $t_i$ terms, each weighted by the gap to the next sampled lag, $t_{i+1}-t_i$, with $t_1=1$. This preserves fine time resolution at small $t$ (where $C_t$ can change rapidly) while avoiding the cost of evaluating $C_t$ at every lag in the slowly decaying tail. [SRC-0091, section 5.2]

**Reported accuracy.** The paper states this adaptive-integration approximation to the full sum is accurate to "at most" about 10% difference from the full (unsparsified) computation, without further quantifying how this error was assessed. [SRC-0091, section 5.2]

**Relationship to Geyer's methods (stated, not derived here).** SRC-0090 independently describes this same "fast multiscale method... described in section 5.2 of ref 10" as "related to a multiscale variant of the initial positive sequence (IPS) method of Geyer, where contributions are accumulated at increasingly longer lag times and the sum ... is truncated when the terms become negative," and reports it performed "equivalently well" to Geyer's initial-sequence estimators in the tested case, while cautioning it "may not perform well for all problems." This paper (SRC-0091) itself does not name or compare against Geyer's estimators in section 5.2; that comparison and characterization is SRC-0090's, not SRC-0091's own text. [SRC-0090; SRC-0091, section 5.2]

**Algorithm summary (as the two facts above combine into one procedure), for either $C_t$ (single observable) or $C_{kt,x,y}$ (cross-correlation):**

1. Evaluate the (cross-)correlation function only at lags $t_i=1+i(i-1)/2$ for $i=1,2,3,\dots$, up to the trajectory length.
2. Stop generating further $t_i$ as soon as the (cross-)correlation function value at a $t_i$ is negative (zero-crossing).
3. Approximate $\tau$ (eq. 19) or $\tau_{k,x,y}$ (eq. 47) as a weighted sum over only the surviving $t_i$, each term weighted by the gap $t_{i+1}-t_i$ to the next sampled lag (with $t_1=1$), rather than by unit weight per integer lag as the literal eq. 19/47 formula would imply.
4. Form $g=1+2\tau$ (eq. 20) or $g_{k,x,y}=1+2\tau_{k,x,y}$ (eq. 46) from the truncated, sparsified sum.

### 5.4 Bounding the cross-correlation statistical inefficiency

Because $g_{k,x,y}$ (or $g_{x,y}$) is estimated from a noisy correlation function via the same truncated procedure, the estimate can violate the constraint required for a physically consistent squared-uncertainty propagation. The paper derives (Appendix A) and imposes the bound

$$
g_{x,y} \le (g_x g_y)^{1/2}\,\frac{\sigma_x\sigma_y}{|\sigma_{xy}^2|} ,
$$

capping any estimated $g_{x,y}$ at this value whenever the raw estimate would otherwise exceed it (which, per Appendix A, can occur under noise and would otherwise risk making eq. 41's $\delta^2\hat A$ negative). [SRC-0091, eq. 73, Appendix A]

## Equation inventory

| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |
| $A_\beta$, density-of-states form | SRC-0091 eqs. 1, 3 | This page | Defines canonical expectation and its density-of-states rewriting. | $A_\beta$, $U(\mathbf q)$, $\Omega(U)$ | Foundational definition. |
| $\hat\Omega_{mk}$ | SRC-0091 eq. 11 | This page | Per-simulation density-of-states estimate from one histogram. | $H_{mk}$, $N_k$, $f_k$, $U_m$ | Building block combined by WHAM. |
| Optimal combination rule | SRC-0091 eqs. 13-14, 22 | This page | General inverse-variance-weighted combination of independent estimates; reused for eqs. 30, 64. | $x_k$, $\delta^2x_k$ | Underlies every WHAM combination step. |
| $\sigma_x^2$, $g$, $\tau$, $C_t$ | SRC-0091 eqs. 15, 17-21 | This page; [[wiki/concepts/statistical-inefficiency-and-automated-equilibration-detection]] | General statistical-inefficiency/autocorrelation-time system (identical in form to SRC-0090 eqs. 10-13). | $\sigma_x^2$, $g$, $\tau$, $C_t$ | Core uncertainty-scaling quantity throughout the paper. |
| WHAM density-of-states + self-consistency | SRC-0091 eqs. 30-31 | This page | Core independent-canonical-simulation WHAM equations, weighted by $g_{mk}^{-1}$. | $\hat\Omega_m$, $f_k$, $g_{mk}$ | The corrected WHAM estimator (vs. omitting $g_{mk}$). |
| $\delta^2\hat\Omega_m$, relative uncertainty | SRC-0091 eqs. 32-33 | This page | Uncertainty of the combined density-of-states estimate. | $\hat\Omega_m$, $g_{mk}$, $H_{mk}$ | Error bars on $\Omega_m$. |
| Weighted-sum expectation estimator | SRC-0091 eqs. 37-38 | This page | Rewrites the expectation as a sum over all stored configurations with per-configuration weights. | $w_{kn}(\beta)$, $A_{kn}$ | Avoids many-dimensional histograms for multiple observables. |
| Ratio uncertainty propagation | SRC-0091 eqs. 39, 41, 43 | This page | Propagates uncertainty through $\hat A_\beta=\hat X/\hat Y$. | $\hat X$, $\hat Y$, cross term | Governs final reported uncertainty on any expectation. |
| Cross statistical inefficiency system | SRC-0091 eqs. 44-48 | This page | Defines $g_{k,x,y}$, $\tau_{k,x,y}$, $C_{kt,x,y}$ for the correlated numerator/denominator of the ratio estimator. | $\sigma_{k,x,y}^2$, $g_{k,x,y}$, $C_{kt,x,y}$ | Needed whenever $\hat A_\beta$ is computed as a ratio of correlated sums; explicitly requires section 5.2's estimator. |
| Section 5.2 multiscale/truncation scheme | SRC-0091 section 5.2 (no single equation number; lag scheme $t_i=1+i(i-1)/2$) | This page; [[wiki/concepts/statistical-inefficiency-and-automated-equilibration-detection]] | Practical, efficient, noise-robust estimator for $\tau$ (or $\tau_{k,x,y}$) from a finite trajectory. | $t_i$, $C_{t_i}$, truncation lag | The estimator SRC-0090 (ref 10, section 5.2) uses in `pymbar`; resolves SRC-0090's prior mathematical gap. |
| $g_{x,y}$ bound | SRC-0091 eq. 73 (derived Appendix A, eqs. 74-81) | This page | Caps a noisy cross-statistical-inefficiency estimate to avoid a negative squared uncertainty. | $g_x$, $g_y$, $\sigma_x$, $\sigma_y$, $\sigma_{xy}$ | Numerical safeguard for eq. 41 when $X,Y$ are correlated. |
| STWHAM equations | SRC-0091 eqs. 49, 51, 53-54, 57 | This page | WHAM for a single simulated-tempering trajectory, one $g_m$ per bin. | $\hat\Omega_m$, $f_l$, $g_m$ | Analysis path for simulated tempering. |
| PTWHAM equations | SRC-0091 eqs. 61-64, 66 | This page | WHAM for $K$ parallel-tempering replicas, using per-replica statistical inefficiencies $g_{mk}$. | $\hat\Omega_m$, $H_m^\text{eff}$, $N_{ml}^\text{eff}$ | Analysis path used for the paper's alanine-dipeptide PMF application. |

## Algorithmic recursions

- **Self-consistent free-energy iteration**: eqs. 30-31 (independent canonical), eqs. 53-54 (STWHAM), and eqs. 64/66 with eq. 54's analogue (PTWHAM) form coupled nonlinear systems for $\{f_k\}$ or $\{f_l\}$, solved by iterating the density-of-states estimate and the free-energy update to self-consistency, starting from an arbitrary initial guess (e.g., $f_k=0$), exactly as in the original Kumar et al. WHAM. [SRC-0091, following eq. 31]
- **Section 5.2 multiscale statistical-inefficiency estimator**: see the dedicated section above; this is the algorithmic core requested by the ingestion brief and is reproduced there in full (lag schedule, weighting, and zero-crossing truncation rule).

## Evidence

- **1D model system** (asymmetric double-well Metropolis Monte Carlo potential, eq. 69): four protocols (single MMC at $\beta^*=4$; four independent canonical MMC simulations spanning $\beta\in\{1,\,2.52,\,1.59\ (\text{sic, as listed}),\,4\}$ — i.e. four exponentially spaced inverse temperatures in $[1,4]$; simulated tempering; parallel tempering with four replicas) were run for $5\times10^7$ steps and divided into 500 blocks of $10^4$ configurations each to empirically validate the uncertainty formulas via confidence curves (fraction of blocks whose true deviation from the whole-run estimate falls within $\sigma$ multiples of the predicted uncertainty). [SRC-0091, section 4.1, Figure 1]
- Confidence curves for all four protocols closely track the theoretical normal-distribution expectation, and bias was found to be "small — less than 10% of the magnitude of the statistical uncertainty in the cases studied (data not shown)." [SRC-0091, section 4.1]
- **Alanine dipeptide** PMF in the $\psi$ torsion at 300 K was computed from parallel tempering in implicit solvent (10 replicas, 273-600 K, 100 ns/replica) and explicit TIP3P solvent (40 replicas, 273-600 K, 20 ns/replica); block-based (2 ns/replica) uncertainty estimates were validated against confidence curves computed the same way as for the 1D system. [SRC-0091, section 4.2, Figures 2-4]
- The paper separately confirmed, for the $\alpha_R$-conformation population of alanine dipeptide, that neglecting the uncertainty in the dimensionless free energies $\{f_l\}$ is justified for these systems: the neglected contribution was found to be about 10x smaller (explicit solvent) or 100x smaller (implicit solvent) than the uncertainty from time correlation in the observable itself. [SRC-0091, p. 37-38]
- Section 5.3 empirically tested, for the alanine-dipeptide systems, whether it is safe to assume all $g_{mk}$ are equal to unity or otherwise identical (an assumption implicit in prior WHAM-for-generalized-ensembles literature, refs 1, 4). It found large differences in statistical inefficiency — "sometimes differing up to two orders of magnitude" — both across energy bins for a fixed replica and across replicas for a fixed energy bin. [SRC-0091, section 5.3]

## Limitations and Caveats

- The uncertainty framework throughout (eqs. 39-48) neglects the uncertainty contributed by the estimated dimensionless free energies $\{f_k\}$/$\{f_l\}$ themselves; this is stated to be justified only when the observable's correlation time is much longer than that of the potential energy (so that observable-sample scarcity dominates), and the paper explicitly flags this as an unresolved limitation, suggesting combination with Gallicchio et al.'s T-WHAM (ref 24) as a possible future direction when the two correlation times are comparable. [SRC-0091, sections 2.7, 5.4 intro, 6]
- STWHAM's derivation assumes the statistical inefficiency $g_m$ depends only on the energy bin $m$ and is identical for every temperature/replica the mixed-canonical trajectory visits; the paper notes this assumption specifically fails for simulated tempering replica-exchange (STREM) simulations, where replicas are not equivalent, and that the simple treatment "will only be recovered if the time between samples is so long that all $g_{mk}$ are unity." [SRC-0091, section 3.1]
- The "fast multiscale" section 5.2 estimator is described and its adaptive lag scheme is given exactly, but its reported ~10% accuracy figure versus the full (unsparsified) sum is stated without quantitative detail on how that comparison was performed (no error metric, dataset, or sample size given in the main text for this specific claim). [SRC-0091, section 5.2]
- The zero-crossing truncation heuristic is explicitly noted to be inappropriate for correlation functions with a genuine negative dip at short lag (the paper's own example: velocity autocorrelation functions). [SRC-0091, section 5.2]
- The $g_{x,y}$ bound (eq. 73) is a cap, not a bias correction: when invoked, it prevents a physically inconsistent (negative-squared-uncertainty) result, but the paper does not claim the capped value is itself an unbiased estimate of the true cross statistical inefficiency. [SRC-0091, eq. 73, Appendix A]
- Both PTWHAM and STWHAM require the two Metropolis-like acceptance rules (eqs. 49, 61) to have been the *actual* protocol used to generate the data; the derivations are specific to this replica/temperature-exchange or temperature-random-walk structure and are not claimed to generalize to arbitrary generalized-ensemble algorithms without re-derivation (though the conclusion suggests, without deriving, that the multicanonical algorithm (MUCA) could likely be treated analogously). [SRC-0091, section 6]

## Links

- [[wiki/sources/SRC-0090-a-simple-method-for-automated-equilibration-detection-in]] — SRC-0090 cites this paper (ref 10) specifically for the section 5.2 "fast multiscale" statistical-inefficiency estimator used in its `pymbar.timeseries` reference implementation; this page resolves that prior mathematical gap.
- [[wiki/concepts/statistical-inefficiency-and-automated-equilibration-detection]] — shares the identical general statistical-inefficiency/autocorrelation-time definitions (this paper's eqs. 15/17-21 versus SRC-0090's eqs. 10-13) and now also documents the section 5.2 multiscale estimator on that concept page.
- [[wiki/entities/authors/john-d-chodera]]

Note on MBAR: this 2007 paper predates the multistate Bennett acceptance ratio (MBAR) paper, [[wiki/sources/SRC-0023-statistically-optimal-analysis-multiple-equilibrium-states-mbar]] (Shirts & Chodera, 2008), and does not discuss or cite it — MBAR came later and was developed in part as a histogram-free alternative to WHAM. No wikilink or `cites_sources` relationship is recorded between SRC-0091 and SRC-0023/the MBAR concept page, since the source text does not support one; this is a chronological/topical observation, not a documented citation. [SRC-0091; SRC-0023]

## Claims

- [[wiki/claims/CLM-0046-multiscale-truncated-autocorrelation-estimator-controls-tail-noise]] - Truncating the WHAM/timeseries integrated-autocorrelation-time sum at the correlation function's first zero-crossing, while sparsifying the sampled lag times on a quadratic ($t_i=1+i(i-1)/2$) schedule, gives a statistical-inefficiency estimate that is fast to compute and accurate to within about 10% of the full sum, avoiding the noise-dominated tail that would otherwise corrupt a naive plug-in estimator. [SRC-0091]

## Questions

- (none added as separate first-class pages; open questions kept source-local below)

## Tensions

- (none identified; no contradiction with other ingested sources was found — this paper predates and does not address MBAR)

## Open Questions

- How exactly was the "at most 10%" accuracy figure for the section 5.2 multiscale estimator (versus the full, unsparsified autocorrelation sum) quantified? The paper states the result without describing the comparison protocol. [SRC-0091, section 5.2]
- The paper explicitly leaves open how to properly combine the free-energy ($\{f_k\}$) uncertainty with the observable's temporal-correlation uncertainty when the two relevant correlation times (of the potential energy and of the observable) are comparable, suggesting T-WHAM (Gallicchio et al.) as a possible direction. [SRC-0091, sections 5.4 intro, 6]
- How sensitive are STWHAM/PTWHAM results to violations of the "single $g_m$ per bin, independent of temperature/replica" simplifying assumption, given that section 5.3 found up to two-orders-of-magnitude variation in $g_{mk}$ across bins and replicas for the alanine-dipeptide systems studied? [SRC-0091, section 5.3]

## Citation links

- The full 44-entry reference list (pp. 40-41) was reviewed. No confirmed match to any other source currently ingested in SecondBrain was found: this 2007 paper predates both [[wiki/sources/SRC-0023-statistically-optimal-analysis-multiple-equilibrium-states-mbar]] (2008) and [[wiki/sources/SRC-0090-a-simple-method-for-automated-equilibration-detection-in]] (2016), so it cannot and does not cite either. `cites_sources` is therefore empty and `citation_match_status` is `reviewed` (the bibliography was checked in full, not merely sampled). [SRC-0091]
- The reverse relationship is a strong, bibliographically confirmed match: [[wiki/sources/SRC-0090-a-simple-method-for-automated-equilibration-detection-in]]'s reference (10) reads "Chodera, J. D.; Swope, W. C.; Pitera, J. W.; Seok, C.; Dill, K. A. J. Chem. Theory Comput. 2007, 3, 26-41," an exact author-list + journal + year + volume + page match to this source, and SRC-0090's in-text citation explicitly names "section 5.2 of ref 10." [SRC-0090]

## Mathematical gaps

- The full derivation of eq. 9 (i.e., the intermediate double-sum expansion splitting variance and cross-correlation terms, this paper's eq. 16, analogous across the whole family of $\delta^2\hat X$ derivations) is summarized via its final result rather than reproduced algebraically step-by-step, though the final relations (eqs. 15-21) are reproduced exactly.
- Appendix A's derivation of the $g_{x,y}$ bound (eq. 73) is summarized by its key steps (Schwartz inequality on $\sigma_{X,Y}^2\le\sigma_X\sigma_Y$, correlation-analysis estimators eqs. 78, combination into eq. 81) rather than reproduced in full line-by-line algebra.
- Appendix B (Bayesian confidence-interval estimation for the confidence curves of Figures 1 and 4, eqs. 82-84, using a Beta-Binomial conjugate model) is not reproduced in equation form here; it is a validation/plotting detail rather than part of the core WHAM/statistical-inefficiency machinery and was judged lower priority for this ingestion.
- The paper's precise numerical protocol for its "at most 10%" accuracy claim for the section 5.2 estimator (recorded above under Open Questions) is not given in the source text itself, so it cannot be reproduced.

## Ingestion QA

### Retrieval questions checked

- What problem does this paper solve, and how does it differ from the original Kumar et al. WHAM? Answered (Summary, Key Points).
- What are the STWHAM and PTWHAM equations, and how do they differ from independent-canonical WHAM? Answered (Key equations, sections 3.1-3.2).
- How exactly does the paper compute the integrated autocorrelation time / statistical inefficiency from a finite, noisy trajectory (section 5.2)? Answered in full: truncation rule, multiscale lag schedule, and reported accuracy (Section 5.2 dedicated section above).
- How does the paper handle cross-correlation between two observables (needed for the ratio-form expectation estimator)? Answered (eqs. 44-48, and the $g_{x,y}$ bound of eq. 73/section 5.4).
- What evidence supports the correctness of the uncertainty estimates? Answered (Evidence: 1D model system confidence curves; alanine dipeptide PMF confidence curves).
- What are the method's stated limitations? Answered (Limitations and Caveats: neglected $\{f_k\}$ uncertainty, STWHAM's single-$g_m$ assumption, unclear precise validation protocol for the 10% figure).
- Does this paper resolve SRC-0090's previously recorded gap about the "fast multiscale" estimator? Yes — confirmed via bibliographic cross-check of SRC-0090's reference (10) and its in-text citation to "section 5.2 of ref 10," and the section 5.2 content matches SRC-0090's own description of the cited method (multiscale lag accumulation, truncation when terms go negative).
- Does this paper discuss or relate to MBAR? Checked: no, it predates MBAR (2008) and does not mention it; no relationship recorded beyond a chronological/topical note.

### Coverage decision

`coverage_profile: math-deep`. The core WHAM re-derivation, the STWHAM and PTWHAM extensions, the full uncertainty-propagation and cross-correlation framework, and the complete section 5.2 statistical-inefficiency estimator (the paper's specific requested target) are reproduced with equation-level fidelity, including the algorithmic lag-schedule and truncation rule needed for reimplementation. Appendices A and B are summarized rather than reproduced line-by-line. [SRC-0091]

### Known gaps

- Appendix A's Schwartz-inequality derivation of eq. 73 and Appendix B's Bayesian confidence-interval construction are recorded as summaries, not full derivations (see Mathematical gaps).
- The exact empirical protocol behind the "at most 10%" accuracy claim for the section 5.2 multiscale estimator is not stated in the source and is recorded as an open question rather than reconstructed.
- Only the SRC-0091 to already-ingested-source citation direction was exhaustively checked (44/44 references, none matched); no new citation targets outside the current SecondBrain source list were investigated further.
