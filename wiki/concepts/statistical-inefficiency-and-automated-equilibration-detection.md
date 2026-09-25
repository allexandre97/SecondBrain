---
type: concept
status: active
created: 2026-09-25
updated: 2026-09-25
areas:
  - research
categories:
  - research/molecular-simulation/molecular-dynamics
  - research/statistics/monte-carlo
tags:
  - equilibration
  - statistical-inefficiency
  - effective-sample-size
  - autocorrelation
  - burn-in
  - wham
  - math-heavy
related:
  - "[[wiki/sources/SRC-0090-a-simple-method-for-automated-equilibration-detection-in]]"
  - "[[wiki/sources/SRC-0023-statistically-optimal-analysis-multiple-equilibrium-states-mbar]]"
  - "[[wiki/concepts/multistate-bennett-acceptance-ratio]]"
  - "[[wiki/sources/SRC-0091-use-of-the-weighted-histogram-analysis-method-for]]"
sources:
  - SRC-0090
  - SRC-0091
sensitivity: public
encryption: none
---

# Statistical Inefficiency and Automated Equilibration Detection

## Summary

Molecular simulations are usually started from atypical configurations, so an initial portion of the trajectory ("equilibration" or "burn-in") must be discarded before computing equilibrium averages, or the estimate will be biased. Discarding more data reduces bias but also reduces the number of samples available, increasing variance. The statistical inefficiency $g$ quantifies how many correlated timeseries samples are needed to produce one effectively independent sample; the effective number of uncorrelated samples $N_\text{eff}(t_0)=(T-t_0+1)/g_{t_0}$ can be estimated from a single trajectory and used to automatically choose the equilibration time $t_0$ that best balances this bias-variance trade-off, without assuming any particular distribution for the observable. [SRC-0090]

## Key Points

- For a fixed equilibration time $t_0$, the mean squared error of the production-region average decomposes exactly into a variance term and a squared-bias term. [SRC-0090]
- Once $t_0$ is large enough to eliminate bias, the timeseries is stationary and time-reversible, and the remaining error is $\sigma_{t_0}^2/N_\text{eff}(t_0)$, i.e., variance divided by the effective number of uncorrelated samples. [SRC-0090, eq. 9]
- The statistical inefficiency is $g \equiv 1+2\tau_{ac}$, where $\tau_{ac}$ is the integrated autocorrelation time computed from the normalized fluctuation autocorrelation function $C_t$ of the observable timeseries. [SRC-0090, eqs. 11-13]
- The automated equilibration-detection rule chooses $t_0^\text{opt}=\arg\max_{t_0} N_\text{eff}(t_0)$: as $t_0$ increases past the true equilibration point, $g_{t_0}$ drops and $N_\text{eff}(t_0)$ peaks, and this peak closely tracks where bias is essentially eliminated. [SRC-0090, eq. 14, Figure 2]
- On a liquid-argon benchmark (density and reduced potential energy), per-trajectory $N_\text{eff}$-maximization achieved RMS error only ~11% worse than the best possible fixed $t_0$ (which requires knowledge from many replicates), versus ~290% worse if no equilibration time is discarded at all. [SRC-0090]
- The method needs only the saved scalar observable timeseries, not full configurations, and makes no assumption about the observable's marginal distribution (unlike normality-test-based schemes such as reverse cumulative averaging). [SRC-0090]
- Robustly estimating $g$ from a finite, noisy sample autocorrelation function is itself a nontrivial sub-problem; naive plug-in estimates of $C_t$ let noise grow with lag and dominate the sum defining $\tau_{ac}$, motivating estimators such as Geyer's initial sequence methods or the "fast multiscale" estimator used in the source paper's reference implementation (`pymbar.timeseries.detectEquilibration()`). [SRC-0090]
- The "fast multiscale" estimator is fully specified in [[wiki/sources/SRC-0091-use-of-the-weighted-histogram-analysis-method-for]], section 5.2: it computes the normalized fluctuation autocorrelation function only at a quadratically sparsified set of lag times $t_i=1+i(i-1)/2$ ($i=1,2,3,\dots$), weights each retained term by the gap to the next sampled lag, and truncates the sum at the first lag where the correlation function crosses zero (treating the remainder as noise-dominated); the source reports this is accurate to within about 10% of the full, unsparsified sum. [SRC-0091, section 5.2]
- The same lag-sparsification and zero-crossing truncation scheme also applies to the cross-correlation function between two different observables, which is needed when an estimator is expressed as a ratio of two correlated weighted sums (as in WHAM); the resulting cross statistical inefficiency $g_{x,y}$ is additionally capped by a derived upper bound, $g_{x,y}\le(g_xg_y)^{1/2}\sigma_x\sigma_y/|\sigma_{xy}^2|$, to prevent noise from producing an unphysical negative squared uncertainty. [SRC-0091, eq. 73, section 5.4]
- This is directly relevant to any downstream estimator (e.g., MBAR) whose uncertainty formulas assume effectively uncorrelated samples: correlated, non-decorrelated trajectory data can severely underestimate the reported uncertainty if used directly. [SRC-0023]

## Core equations

**Bias-variance decomposition of a fixed-$t_0$ estimator, source Eqs. (4)-(7) [SRC-0090]:**

$$
\delta^2 \hat A_{[t_0,T]}
= \operatorname{var}_{x_0}\!\big(\hat A_{[t_0,T]}\big)
+ \operatorname{bias}_{x_0}^2\!\big(\hat A_{[t_0,T]}\big).
$$

**Error once bias is eliminated, source Eq. (9) [SRC-0090]:**

$$
\delta^2 \hat A_{[t_0,T]}^{\text{equil}} = \frac{\sigma_{t_0}^2}{T_{t_0}/g_{t_0}},
\qquad T_{t_0}\equiv T-t_0+1.
$$

**Statistical inefficiency and integrated autocorrelation time, source Eqs. (10)-(13) [SRC-0090]:**

$$
\sigma^2 \equiv \langle a_t^2\rangle - \langle a_t\rangle^2,
\qquad
g \equiv 1+2\tau_{ac},
\qquad
\tau_{ac} \equiv \sum_{t=1}^{T-1}\Big(1-\frac{t}{T}\Big)C_t,
$$

$$
C_t \equiv \frac{\langle a_n a_{n+t}\rangle - \langle a_n\rangle^2}{\langle a_n^2\rangle - \langle a_n\rangle^2}.
$$

**Automated equilibration-time selection rule, source Eq. (14) [SRC-0090]:**

$$
t_0^{\text{opt}} = \operatorname*{arg\,max}_{t_0} N_\text{eff}(t_0)
= \operatorname*{arg\,max}_{t_0} \frac{T-t_0+1}{g_{t_0}}.
$$

**The "fast multiscale" estimator for $\tau$ (or $g$), source section 5.2, algorithm [SRC-0091]:**

The literal sum $\tau=\sum_{t=1}^{N-1}(1-t/N)C_t$ is not evaluated at every integer lag. Instead:

1. Evaluate $C_t$ only at lags $t_i = 1 + i(i-1)/2$ for $i=1,2,3,\dots$ (quadratically increasing spacing).
2. Stop as soon as $C_{t_i}<0$ (first zero-crossing); treat the remaining, untested lags as noise-dominated and drop them from the sum.
3. Approximate $\tau$ as the sum over the surviving $t_i$ terms, each weighted by the gap $t_{i+1}-t_i$ to the next sampled lag (with $t_1=1$), rather than by unit weight per integer lag.
4. Form $g=1+2\tau$ from this truncated, sparsified sum.

This is reported to be accurate to within about 10% of the full (unsparsified) sum over all integer lags, though the source does not describe the exact empirical protocol behind that figure. [SRC-0091, section 5.2] The same procedure is applied to the cross-correlation function $C_{kt,x,y}$ between two observables, with the resulting cross statistical inefficiency additionally capped at $g_{x,y}\le (g_xg_y)^{1/2}\sigma_x\sigma_y/|\sigma_{xy}^2|$ to avoid an unphysical negative squared uncertainty when noise dominates. [SRC-0091, eq. 73]

## Variable glossary

- $a_t$: scalar observable sampled at simulation "time" $t$ (in sampling-interval units). [SRC-0090]
- $t_0$: candidate equilibration time; samples with index $<t_0$ are discarded. [SRC-0090]
- $T$: total number of samples in the trajectory. [SRC-0090]
- $g_{t_0}$: statistical inefficiency estimated over the production region $[t_0,T]$. [SRC-0090]
- $N_\text{eff}(t_0)$: estimated effective number of uncorrelated samples in $[t_0,T]$. [SRC-0090]
- $\tau_{ac}$: integrated autocorrelation time. [SRC-0090]
- $C_t$: normalized fluctuation autocorrelation function at lag $t$. [SRC-0090]
- $\sigma^2$: sample variance of the observable. [SRC-0090]

## Implementation consequences

- Requires only the saved scalar timeseries of the observable(s) of interest, not full simulation configurations, and can be computed as a cheap postprocessing step. [SRC-0090]
- Distributed as a practical reference implementation, `pymbar.timeseries.detectEquilibration()`, returning `(t0, g, Neff_max)`. [SRC-0090]
- Provides a principled, distribution-free alternative to fixed or manually chosen burn-in periods, and to normality-test-based schemes (e.g., reverse cumulative averaging) that are less appropriate for the often strongly non-Gaussian observables seen in molecular simulation. [SRC-0090]
- Should be applied before feeding trajectory data into estimators (such as MBAR) whose asymptotic uncertainty formulas assume effectively uncorrelated samples. [SRC-0023]

## Caveats

- Cannot rescue a simulation that never reached equilibrium: if no portion of the trajectory is representative, no choice of $t_0$ removes the bias. [SRC-0090]
- Degrades if there is too little data to estimate $g$ reliably; the author frames this as a symptom of insufficient sampling rather than a flaw specific to this method. [SRC-0090]
- The reported strong empirical performance (11% worse than an oracle fixed $t_0$) was demonstrated on a single simple Lennard-Jones liquid-argon system for two smooth, roughly unimodal observables; behavior on strongly non-Gaussian, multimodal, or slowly interconverting biomolecular observables is not separately benchmarked in the source. [SRC-0090]
- The choice among competing statistical-inefficiency estimators (fast multiscale vs. Geyer's initial sequence methods) is not shown to be immaterial in general; the source paper reports they "performed equivalently well" only for the tested case. [SRC-0090]
- The zero-crossing truncation rule used by the fast multiscale estimator is explicitly noted to be inappropriate for correlation functions with a genuine negative dip at short lag, such as velocity autocorrelation functions. [SRC-0091, section 5.2]
- The reported "at most 10%" accuracy of the fast multiscale estimator relative to the full sum is stated without a described comparison protocol. [SRC-0091, section 5.2]

## Links

- [[wiki/sources/SRC-0090-a-simple-method-for-automated-equilibration-detection-in]]
- [[wiki/sources/SRC-0023-statistically-optimal-analysis-multiple-equilibrium-states-mbar]]
- [[wiki/concepts/multistate-bennett-acceptance-ratio]]
- [[wiki/sources/SRC-0091-use-of-the-weighted-histogram-analysis-method-for]]

## Open Questions

- How does $N_\text{eff}$-maximization behave for strongly non-Gaussian, multimodal, or metastable biomolecular observables where a single trajectory may not sample all relevant states? [SRC-0090]
- How sensitive is the resulting $t_0^\text{opt}$ to the choice of underlying statistical-inefficiency estimator on realistic, finite molecular-dynamics timeseries? [SRC-0090]
