---
type: claim
status: active
created: 2026-09-28
updated: 2026-10-11
claim_status: supported
claim_scope: local
areas:
  - research
categories:
  - research/molecular-simulation/molecular-dynamics
  - research/statistics/monte-carlo
  - research/molecular-simulation/force-fields
tags:
  - claim
  - ffrefine
  - equilibration
  - statistical-inefficiency
  - effective-sample-size
  - times-square-sampling
related:
  - "[[wiki/claims/CLM-0045-neff-maximization-gives-near-optimal-equilibration-time]]"
  - "[[wiki/claims/CLM-0046-multiscale-truncated-autocorrelation-estimator-controls-tail-noise]]"
  - "[[wiki/concepts/statistical-inefficiency-and-automated-equilibration-detection]]"
  - "[[wiki/sources/SRC-0090-a-simple-method-for-automated-equilibration-detection-in]]"
  - "[[wiki/sources/SRC-0091-use-of-the-weighted-histogram-analysis-method-for]]"
  - "[[wiki/answers/ffrefine-multi-series-equilibration-cut-calibration]]"
sources:
  - SRC-0090
  - SRC-0091
sensitivity: public
encryption: none
project_evidence:
  - "FFRefine `improved-gates` worktree branch, commits 20d286f and 16ea49a: Monte Carlo simulation of stationary AR(1) series checking the bias of the argmax-N_eff cut, both for one series and for the maximum cut over several series"
  - "FFRefine `improved_gates_plan.md` section 3.0, choice 4, referencing an independent reviewer's stationary AR(1) simulation with a 10-frame grid and up to 90% search depth"
scope: timeless
---

# Calibrated Materiality Threshold Prevents Over-Cutting in Multi-Series Equilibration Detection

## Claim

When several per-frame series each contribute their own $N_\text{eff}$-maximizing equilibration cut [SRC-0090] and the latest cut among them is taken as one global cut, the result is biased late (over-cuts), because each series' $\arg\max_{t_0}N_\text{eff}(t_0)$ is itself noisy and the maximum of several noisy argmaxes compounds that bias. Requiring a series' cut to be *material* — $N_\text{eff}(t_0)\ge(1+\delta)N_\text{eff}(0)$ — with $\delta$ calibrated by Monte Carlo so that a spurious material cut occurs with probability at most a target $\alpha$, controls this over-cutting. The calibration is only valid if it is conditioned on a statistic that (a) is not itself selected by the cut search and (b) is not inflated by a genuine early transient: FFRefine uses the statistical inefficiency $g$ measured on each series' second half, pooling stationary draws over a grid of true $g$ and binning by $\log_{10}$ of the minimum $N/g_\text{late}$ across series. Keying the same calibration on the *true* $g$ is over-conservative, because a real transient would legitimately inflate the true $g$ and should raise its own threshold; keying it on the $g$ *at the selected cut* is anti-conservative, because that $g$ is itself deflated by the argmax bias being corrected for.

## Scope

This is a local, project-evidence claim about FFRefine's planned equilibration-cut policy for a frozen-bias Times Square Sampling (TSS) production archive with a single replica walking a temperature ladder, where several per-family observable series (and, in a later implementation stage, per-family gradient series) are combined into one global cut in trajectory time. It builds directly on the per-trajectory $N_\text{eff}$-maximizing rule of [[wiki/claims/CLM-0045-neff-maximization-gives-near-optimal-equilibration-time]] and the fast multiscale $g$-estimator of [[wiki/claims/CLM-0046-multiscale-truncated-autocorrelation-estimator-controls-tail-noise]], neither of which addresses combining multiple series or a single-replica multi-state walk; [[wiki/concepts/statistical-inefficiency-and-automated-equilibration-detection]] lists both as open questions. [SRC-0090] [SRC-0091] The calibration itself, and its numerical false-cut rates, are demonstrated only on stationary synthetic AR(1) series, not on FFRefine's real observable or gradient series.

## Evidence

- Simulating stationary AR(1) series with the argmax-$N_\text{eff}$ cut, a 10-frame search grid, and up to 90% search depth: a single series' mean cut is biased late by at most about 1.5% of the archive when $N/g\ge200$. Taking the maximum cut over 10 such series raises this to roughly 6-12% at $N/g=200$–$1300$, and to about 35% at $N/g\approx40$, with about a 28% chance the maximum-of-10 cut exceeds 50% of the archive and the archive is wrongly flagged as not equilibrated.
- Introducing the materiality rule with $\delta$ calibrated conditionally on $\log_{10}(\min_\text{series} N/g_\text{late})$ (second-half $g$ per series) reduces the realized false-cut rate over 10 stationary series to 4.0% at $N/g=40$ and 2.5% at $N/g=200$, against a target $\alpha=5\%$.
- An earlier table calibrated on the *true* $g$ instead of the measured second-half $g$ gave realized false-cut rates of 0.5% and 0% at the same $N/g$ values — safe, but substantially over-conservative, because the fast multiscale $g$-estimator itself reads about 15-20% high [SRC-0091, section 5.2], and a table keyed on the (unavailable in practice) true value does not correct for that bias in the way actually used at run time.
- $\delta$ shows a small non-monotonicity, rising again slightly for series close to white noise (small true $g$).

## Caveats

- The calibration table is a Monte Carlo lookup indexed by the number of series and rounded $\log_{10}(N/g)$, computed once per (series-count, noise-model) configuration; it is not a closed-form correction and must be recalibrated if the number of contributing series or the assumed noise process changes materially.
- Demonstrated only for stationary, Gaussian-driven AR(1) synthetic series. FFRefine's planned per-family gradient series are products of fluctuations with heavier tails and longer correlations than the observable series tested here; the source method itself flags non-Gaussian behavior as an open question. [SRC-0090]
- This claim corrects an over-cutting effect that arises *given* whatever per-series $g$ the fast multiscale estimator reports; it does not by itself establish that estimator's own bias is acceptable for this use (see [[wiki/claims/CLM-0046-multiscale-truncated-autocorrelation-estimator-controls-tail-noise]] and its updated caveats).
- Evidenced by FFRefine's own Monte Carlo checks and by one independent reviewer's simulation reported in the project's `improved_gates_plan.md`; no third-party literature source evaluates this multi-series combination rule.

## Links

- [[wiki/claims/CLM-0045-neff-maximization-gives-near-optimal-equilibration-time]]
- [[wiki/claims/CLM-0046-multiscale-truncated-autocorrelation-estimator-controls-tail-noise]]
- [[wiki/concepts/statistical-inefficiency-and-automated-equilibration-detection]]
- [[wiki/sources/SRC-0090-a-simple-method-for-automated-equilibration-detection-in]]
- [[wiki/sources/SRC-0091-use-of-the-weighted-histogram-analysis-method-for]]
- [[wiki/answers/ffrefine-multi-series-equilibration-cut-calibration]]
