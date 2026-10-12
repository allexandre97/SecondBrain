---
type: answer
status: active
created: 2026-09-28
updated: 2026-10-11
question: "How should automated N_eff-maximizing equilibration detection be adapted for a frozen-bias TSS production archive with several observable series and a single replica walking a temperature ladder, and how accurate is the fast multiscale statistical-inefficiency estimator in that setting?"
answer_status: answered
areas:
  - research
categories:
  - research/molecular-simulation/molecular-dynamics
  - research/molecular-simulation/force-fields
  - research/statistics/monte-carlo
  - research/scientific-computing
tags:
  - ffrefine
  - equilibration
  - statistical-inefficiency
  - times-square-sampling
  - mbar
  - replay-reweighting
related:
  - "[[wiki/answers/ffrefine-direction-gates-and-production-policy]]"
  - "[[wiki/concepts/statistical-inefficiency-and-automated-equilibration-detection]]"
  - "[[wiki/sources/SRC-0090-a-simple-method-for-automated-equilibration-detection-in]]"
  - "[[wiki/sources/SRC-0091-use-of-the-weighted-histogram-analysis-method-for]]"
  - "[[wiki/claims/CLM-0045-neff-maximization-gives-near-optimal-equilibration-time]]"
  - "[[wiki/claims/CLM-0046-multiscale-truncated-autocorrelation-estimator-controls-tail-noise]]"
  - "[[wiki/claims/CLM-0047-calibrated-materiality-threshold-prevents-multi-series-equilibration-over-cutting]]"
  - "[[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]]"
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
  - "[[wiki/answers/ffrefine-decision-register]]"
sources:
  - SRC-0090
  - SRC-0091
sensitivity: public
encryption: none
wiki_pages_used:
  - "[[wiki/concepts/statistical-inefficiency-and-automated-equilibration-detection]]"
  - "[[wiki/claims/CLM-0045-neff-maximization-gives-near-optimal-equilibration-time]]"
  - "[[wiki/claims/CLM-0046-multiscale-truncated-autocorrelation-estimator-controls-tail-noise]]"
  - "[[wiki/sources/SRC-0090-a-simple-method-for-automated-equilibration-detection-in]]"
  - "[[wiki/sources/SRC-0091-use-of-the-weighted-histogram-analysis-method-for]]"
raw_sources_consulted: []
wiki_pages_updated:
  - "[[wiki/answers/ffrefine-multi-series-equilibration-cut-calibration]]"
  - "[[wiki/concepts/statistical-inefficiency-and-automated-equilibration-detection]]"
  - "[[wiki/claims/CLM-0045-neff-maximization-gives-near-optimal-equilibration-time]]"
  - "[[wiki/claims/CLM-0046-multiscale-truncated-autocorrelation-estimator-controls-tail-noise]]"
  - "[[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]]"
project_evidence:
  - "FFRefine `improved-gates` worktree branch, commits 20d286f and 16ea49a: unit tests and Monte Carlo checks of the fast multiscale g-estimator and of the multi-series equilibration-cut calibration"
  - "FFRefine `improved_gates_plan.md` section 3.0, a design document for a frozen-bias TSS water production archive seeded from the end of an equilibrated parity run at the same force-field parameters"
  - "FFRefine repository audit on 2026-10-01 at master 6b20031 (stage-1 implementation of the cut) and the shadow water run 20260928-220040 as summarised in the project's design document; see [[wiki/answers/ffrefine-direction-gates-and-production-policy]]"
scope: snapshot
currency: current
as_of: 2026-10-01
---

# FFRefine Multi-Series Equilibration Cut Calibration

## Short answer

Neither SRC-0090's per-trajectory $N_\text{eff}$-maximizing equilibration rule nor SRC-0091's fast multiscale statistical-inefficiency estimator was validated for combining several series or for a single replica walking a temperature ladder; [[wiki/concepts/statistical-inefficiency-and-automated-equilibration-detection]] lists both as open questions. Implementing the combination for FFRefine's frozen-bias water production archives surfaced two reusable findings, both from FFRefine's own Monte Carlo checks rather than from the literature sources themselves:

1. The fast multiscale $g$-estimator itself reads about 15-20% high on AR(1) series (about 15% at $\phi=0.5$, about 20% at $\phi=0.9$), because its lag weighting emphasizes the near-lag part of a decaying autocorrelation function before the zero-crossing truncation. [SRC-0091, section 5.2]
2. Taking the latest of several per-series $N_\text{eff}$-maximizing cuts over-cuts a stationary archive, because each series' argmax is noisy and the maximum of several noisy argmaxes is biased late; the fix is a materiality threshold on $N_\text{eff}$ gain, calibrated by Monte Carlo, keyed on a statistic that is neither selected by the cut search nor inflated by a genuine transient. See [[wiki/claims/CLM-0047-calibrated-materiality-threshold-prevents-multi-series-equilibration-over-cutting]].

Because FFRefine's production archives are seeded from the end of an equilibrated parity run at the same force-field parameters, only the temperature-ladder state restarts mid-walk; the expected configurational transient is small (on the order of 100 ps of a 50 ns archive). FFRefine therefore runs the cut in report-only mode first (computed and logged, no frames removed) before deciding whether to apply it.

## Detailed answer

### The fast estimator's own bias

SRC-0091's fast multiscale estimator for the integrated autocorrelation time samples the normalized autocorrelation function $C_t$ only at quadratically sparsified lags $t_i=1+i(i-1)/2$, weights each retained term by the gap to the next sampled lag, and truncates at the first zero-crossing. [SRC-0091, section 5.2] [[wiki/concepts/statistical-inefficiency-and-automated-equilibration-detection]] already records that this is reported "accurate to within about 10%" without a described comparison protocol. FFRefine's unit tests, run against synthetic AR(1) series with a small minimum-lag floor (`mintime` 3) and compared against the estimator's own expected value rather than the closed-form $(1+\phi)/(1-\phi)$, found the estimator overestimates $g$ by about 15% at $\phi=0.5$ and about 20% at $\phi=0.9$. The cause is that the retained, sparsely-sampled lags are weighted toward the left (near-lag) end of a still-decaying correlation function, so the weighted sum systematically overcounts correlation relative to the unweighted full sum. The practical implication is that any test of this estimator against a stationary AR(1) benchmark should compare against the estimator's own expected value under the sparsification-and-truncation rule, not against the exact autocorrelation-time formula for the underlying process; the two differ by a stable, direction-known amount.

This bias runs in the "safe" direction for equilibration detection (an inflated $g$ reduces $N_\text{eff}$ and so tends to favor earlier stopping of the cut search, not more aggressive cutting), but it matters directly for the calibration described next, because that calibration must be keyed on a statistic that already reflects this same estimator, not on the (unobservable at run time) true $g$.

### Over-cutting when maximizing over several series

FFRefine's cut uses one series per enabled target family (density, dielectric dipole, RDF projected onto the family's current loss sensitivity) plus the active-state reduced potential, each reduced to a scalar and, for a single replica walking a temperature ladder, centred per active state before detection (subtracting each frame's per-state mean) so that the ladder walk itself is not mistaken for a transient. Naively taking the latest of these several per-series $N_\text{eff}$-maximizing cuts as the one global cut over-cuts a stationary archive: each series' own argmax is a noisy estimate of "no cut needed," and the maximum over several such noisy estimates is biased toward later, larger cuts purely from selection. FFRefine's Monte Carlo checks and an independent reviewer's simulation of stationary AR(1) series (10-frame grid, up to 90% search depth) found:

- a single series' mean cut is biased late by at most about 1.5% of the archive once $N/g\ge200$;
- the maximum over 10 such series raises this to roughly 6-12% at $N/g=200$-$1300$ (FFRefine's own test found about 12% at $N/g=200$), and to about 35% at $N/g\approx40$, with roughly a 28% chance the maximum-of-10 cut exceeds 50% of the archive and the archive is wrongly flagged as not equilibrated.

### The materiality fix and its calibration

FFRefine's response is to require a series' cut to be *material*: it counts only if $N_\text{eff}(t_0)\ge(1+\delta)N_\text{eff}(0)$, with $\delta$ calibrated by Monte Carlo so a spurious material cut occurs with probability at most a target $\alpha$ (default 5%). Among the series whose cuts are material, the latest wins, so every fitted family is equilibrated by the chosen $t_0$. The calibration must condition on a statistic that is (a) not itself selected by the cut search and (b) not inflated by a genuine early transient. FFRefine keys the $\delta$ lookup on $r=\min_\text{series}N/g_\text{late}$, where $g_\text{late}$ is the fast multiscale estimator applied to each series' *second half only*, and calibrates the table by pooling stationary Monte Carlo draws over a grid of true $g$ and binning them by $\log_{10}r$. Two alternative keys were rejected: keying on the *full-series* $g$ is over-conservative, because a real transient legitimately inflates the full-series $g$ and would then raise its own threshold; keying on the $g$ *at the selected cut* is anti-conservative, because that $g$ is itself deflated by the same argmax selection bias the materiality rule exists to correct. With this calibration, realized false-cut rates over 10 stationary series were 4.0% at $N/g=40$ and 2.5% at $N/g=200$ against $\alpha=5\%$; an earlier table keyed on the unavailable true $g$ gave 0.5% and 0%, safe but substantially over-conservative given that the fast multiscale estimator itself reads 15-20% high. $\delta$ shows a small non-monotonicity, rising again slightly for series close to white noise. See [[wiki/claims/CLM-0047-calibrated-materiality-threshold-prevents-multi-series-equilibration-over-cutting]] for the full claim and evidence.

The calibration table is computed once per (number-of-series, noise-model) configuration and looked up at run time by the number of contributing series and the smallest measured $N/g$ among them; a full per-checkpoint recalibration was judged too slow to repeat at every production extension.

### Per-state centring for a single replica on a state ladder

For a single replica walking a temperature ladder, an uncentred series conflates "which state the replica currently occupies" with "has the local configuration relaxed," because production restarts the ladder walk from a middle state. FFRefine's per-state centring (subtracting each frame's per-active-state mean before detection) is needed mainly for slow ladder walks. This does not need to be applied to the per-state occupation itself, since MBAR already treats each frame as a sample of its own visited state's distribution regardless of occupancy counts.

### Staging given the expected transient size

Because FFRefine's production archives are seeded from the end of an already-equilibrated parity run at the same force-field parameters, and only the ladder-state index restarts mid-walk, the expected configurational transient is small — on the order of 100 ps out of a 50 ns archive. Given that expectation, FFRefine runs the cut in report-only mode first: it is computed, logged, and can trigger a warning event, but does not remove frames or block a checkpoint, before any decision to switch to an enforcing mode. A detection failure in report-only mode is recorded and ignored rather than treated as an evaluation failure.

## Sources used

- SRC-0090 for the $N_\text{eff}$-maximizing per-trajectory equilibration rule and its liquid-argon benchmark accuracy.
- SRC-0091, section 5.2, for the fast multiscale statistical-inefficiency estimator (quadratic lag sparsification, zero-crossing truncation) whose bias is quantified here.

The multi-series combination rule, its Monte Carlo calibration, the per-state centring requirement, and the fast estimator's measured AR(1) bias are FFRefine project findings, not claims evaluated by SRC-0090 or SRC-0091.

## Wiki pages used

- [[wiki/concepts/statistical-inefficiency-and-automated-equilibration-detection]]
- [[wiki/claims/CLM-0045-neff-maximization-gives-near-optimal-equilibration-time]]
- [[wiki/claims/CLM-0046-multiscale-truncated-autocorrelation-estimator-controls-tail-noise]]

## Wiki updates made

- Added this answer note.
- Added [[wiki/claims/CLM-0047-calibrated-materiality-threshold-prevents-multi-series-equilibration-over-cutting]].
- Updated [[wiki/concepts/statistical-inefficiency-and-automated-equilibration-detection]]'s Open Questions to note that FFRefine's project evidence now partially addresses the multi-series and single-replica-multi-state gaps.
- Updated [[wiki/claims/CLM-0046-multiscale-truncated-autocorrelation-estimator-controls-tail-noise]]'s Caveats with the measured AR(1) bias.
- Updated [[wiki/claims/CLM-0045-neff-maximization-gives-near-optimal-equilibration-time]]'s Links to point to the new claim and answer note.
- Updated [[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]]'s implementation snapshot with a pointer to this note (since 2026-10-11 that pointer is in the route plan's Evidence timeline).

## Implementation at master `6b20031`

At FFRefine master `6b20031` (2026-10-01), the cut described here is implemented as stage 1 and runs in report-only mode for the water experiment only: per replica, one series per observable target family (loss-sensitivity weighted at checkpoint evaluation, tolerance weighted on raw production data; the dielectric family uses the per-frame squared box dipole) plus the active-state reduced potential, each centred per sampled state; δ is looked up from the calibrated table keyed on the number of series and the smallest $N/g_{\mathrm{late}}$, where $g_{\mathrm{late}}$ is measured on the second half of each series; a cut above half the archive is only flagged; `:apply` mode (frame removal) and the gradient series are not implemented. Hexane and solvation do not yet pass an equilibration policy. In the shadow water campaign `20260928-220040` (11 epochs), as summarised in the project's design document, the cut was never material beyond 1.6% of the archive and never flagged an archive. See [[wiki/answers/ffrefine-direction-gates-and-production-policy]].

## Remaining gaps

- The multi-series calibration and the fast estimator's measured bias are demonstrated only on stationary synthetic AR(1) series, not on FFRefine's real observable series or on the heavier-tailed gradient series planned for a later implementation stage.
- Whether FFRefine's production archives ever need the enforcing (frame-removing) mode of the cut, rather than report-only, is untested. When this note was first written (2026-09-28), no campaign with the cut in report-only mode had run to completion; the shadow-campaign result recorded by 2026-10-01 is in the implementation section above.
- The block-length-versus-correlation-time consistency check (jackknife blocks should be at least about 10 times the measured $g$) has not yet been evaluated against production dielectric-dipole series, which are expected to be the noisiest.
- No comparison exists yet between the observable-only cut and the combined observable-plus-gradient cut planned for stage 2.
