---
type: claim
status: active
created: 2026-09-25
updated: 2026-09-28
claim_status: supported
claim_scope: local
areas:
  - research
categories:
  - research/molecular-simulation/molecular-dynamics
  - research/statistics/monte-carlo
tags:
  - claim
  - statistical-inefficiency
  - autocorrelation
  - wham
related:
  - "[[wiki/sources/SRC-0091-use-of-the-weighted-histogram-analysis-method-for]]"
  - "[[wiki/sources/SRC-0090-a-simple-method-for-automated-equilibration-detection-in]]"
  - "[[wiki/concepts/statistical-inefficiency-and-automated-equilibration-detection]]"
  - "[[wiki/claims/CLM-0047-calibrated-materiality-threshold-prevents-multi-series-equilibration-over-cutting]]"
  - "[[wiki/answers/ffrefine-multi-series-equilibration-cut-calibration]]"
sources:
  - SRC-0091
sensitivity: public
encryption: none
---

# Multiscale Truncated Autocorrelation Estimator Controls Tail Noise

## Claim

Estimating the integrated autocorrelation time $\tau$ (and hence the statistical inefficiency $g=1+2\tau$) by naively summing the normalized fluctuation autocorrelation function $C_t$ over its full lag range is a poor estimator, because the statistical error in the sample estimate of $C_t$ grows approximately linearly with lag $t$ and comes to dominate the sum. Instead, sampling the correlation function only at a quadratically sparsified schedule of lag times $t_i=1+i(i-1)/2$ ($i=1,2,3,\dots$), weighting each retained term by the gap to the next sampled lag, and truncating the sum at the first lag where $C_t$ crosses zero gives an estimator that is both fast to compute and, per the source, accurate to within about 10% of the full (unsparsified) sum. [SRC-0091, section 5.2]

## Scope

This is a local, source-specific claim about a specific practical estimator ("fast multiscale method") for the integrated autocorrelation time used throughout SRC-0091's WHAM/STWHAM/PTWHAM uncertainty formulas, and identically for the cross-correlation function $C_{kt,x,y}$ needed by the ratio-form expectation estimator. [SRC-0091] The same estimator is independently reported, without derivation, to be the one used by [[wiki/sources/SRC-0090-a-simple-method-for-automated-equilibration-detection-in]] and distributed in its `pymbar.timeseries` reference implementation. [SRC-0090]

## Evidence

- The paper states that summing $C_t$ over the full lag range "is almost always a poor choice, as the uncertainty in the computed correlation function grows approximately linearly with the lag time," and that this "will be dominated by contributions from the noisy tail, likely resulting in large errors or even negative values for the computed correlation time." [SRC-0091, section 5.2]
- Two competing prior approaches (Janke's $6\tau$ self-consistent truncation; Evertz's exponential-tail-fit approach) are cited and rejected as neither "stable" nor "straightforward." [SRC-0091, section 5.2]
- The paper's own zero-crossing truncation plus $t_i=1+i(i-1)/2$ lag-sparsification scheme is reported to be accurate to "at most" about 10% difference from the full sum, though the precise empirical protocol behind this figure is not given in the source text (recorded as an open question on [[wiki/sources/SRC-0091-use-of-the-weighted-histogram-analysis-method-for]]). [SRC-0091, section 5.2]
- SRC-0090 independently describes what it calls the same "fast multiscale method... described in section 5.2 of ref 10" as performing "equivalently well" to Geyer's initial-sequence estimators in its own tested case (a Lennard-Jones liquid-argon benchmark), which is consistent with, but does not itself validate, the ~10% accuracy figure claimed in SRC-0091. [SRC-0090]

## Caveats

- The "at most 10%" accuracy claim is stated without a described comparison protocol (dataset, sample size, or error metric), so it should be treated as the source's own summary claim rather than an independently reproducible benchmark. [SRC-0091, section 5.2]
- The zero-crossing truncation heuristic is explicitly stated to be inappropriate for correlation functions with a genuine negative dip at short lag, such as velocity autocorrelation functions. [SRC-0091, section 5.2]
- SRC-0090 reports this estimator "may not perform well for all problems," based on a single benchmark system (liquid argon), not a general guarantee. [SRC-0090]
- FFRefine project unit tests (branch `improved-gates`, commits `20d286f` and `16ea49a`) quantify this estimator's own bias on synthetic AR(1) series, compared against the estimator's own expected value under its lag-sparsification-and-truncation rule rather than the closed-form $(1+\phi)/(1-\phi)$: it reads about 15% high at $\phi=0.5$ and about 20% high at $\phi=0.9$, because the retained, quadratically-sparsified lags weight the near-lag (still strongly correlated) part of the autocorrelation function before the zero-crossing truncation removes the noise-dominated tail. This is project evidence, not a finding of SRC-0091 itself, but it is consistent with, and gives a concrete number to, the general concern about noisy tail contributions this estimator is designed to control. See [[wiki/answers/ffrefine-multi-series-equilibration-cut-calibration]].

## Links

- [[wiki/sources/SRC-0091-use-of-the-weighted-histogram-analysis-method-for]]
- [[wiki/sources/SRC-0090-a-simple-method-for-automated-equilibration-detection-in]]
- [[wiki/concepts/statistical-inefficiency-and-automated-equilibration-detection]]
- [[wiki/claims/CLM-0047-calibrated-materiality-threshold-prevents-multi-series-equilibration-over-cutting]]
- [[wiki/answers/ffrefine-multi-series-equilibration-cut-calibration]]
