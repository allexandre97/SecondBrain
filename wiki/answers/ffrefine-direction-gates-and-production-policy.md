---
type: answer
status: active
created: 2026-10-01
updated: 2026-10-11
question: "How do FFRefine's current block-based direction gates and extend-or-exclude production policy work (master 6b20031, 2026-10-01), and what did building and running them teach?"
answer_status: answered
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/statistics/monte-carlo
  - research/scientific-computing
tags:
  - ffrefine
  - direction-gate
  - config
  - jackknife
  - validation-policy
  - production-extension
  - multiple-testing
related:
  - "[[wiki/answers/ffrefine-current-implementation-status]]"
  - "[[wiki/answers/ffrefine-improved-gates-water-run-lessons]]"
  - "[[wiki/answers/adding-config-optimiser-to-ffrefine]]"
  - "[[wiki/answers/ffrefine-loss-gate-diagnostic-policy]]"
  - "[[wiki/answers/ffrefine-multi-series-equilibration-cut-calibration]]"
  - "[[wiki/questions/QST-0007-checkpoint-assessment-versus-next-direction-readiness]]"
  - "[[wiki/questions/QST-0011-config-versus-weighted-sum-under-calibrated-direction-gates]]"
  - "[[wiki/questions/QST-0012-persistent-replay-prediction-optimism-for-one-family]]"
  - "[[wiki/questions/QST-0013-step-length-policy-after-family-exclusion]]"
  - "[[wiki/answers/ffrefine-config-vs-weighted-sum-water-campaign-results]]"
  - "[[wiki/claims/CLM-0049-few-block-pseudo-value-covariance-understates-promise-null]]"
  - "[[wiki/claims/CLM-0050-retesting-a-failed-gate-after-extension-needs-alpha-spending]]"
  - "[[wiki/claims/CLM-0048-family-weight-renormalisation-changes-natural-gradient-step-length]]"
  - "[[wiki/claims/CLM-0044-config-must-exclude-directionally-unreliable-families]]"
  - "[[wiki/tensions/TEN-0020-config-family-exclusion-versus-untreated-drift]]"
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
  - "[[wiki/answers/ffrefine-generalist-package-plan-decisions]]"
sources:
  - SRC-0036
sensitivity: public
encryption: none
wiki_pages_used:
  - "[[wiki/answers/ffrefine-current-implementation-status]]"
  - "[[wiki/answers/ffrefine-improved-gates-water-run-lessons]]"
  - "[[wiki/answers/adding-config-optimiser-to-ffrefine]]"
  - "[[wiki/answers/ffrefine-loss-gate-diagnostic-policy]]"
  - "[[wiki/answers/ffrefine-multi-series-equilibration-cut-calibration]]"
  - "[[wiki/questions/QST-0007-checkpoint-assessment-versus-next-direction-readiness]]"
  - "[[wiki/tensions/TEN-0020-config-family-exclusion-versus-untreated-drift]]"
  - "[[wiki/claims/CLM-0044-config-must-exclude-directionally-unreliable-families]]"
  - "[[wiki/claims/CLM-0048-family-weight-renormalisation-changes-natural-gradient-step-length]]"
raw_sources_consulted: []
wiki_pages_updated:
  - "[[wiki/answers/ffrefine-current-implementation-status]]"
  - "[[wiki/answers/ffrefine-improved-gates-water-run-lessons]]"
  - "[[wiki/answers/adding-config-optimiser-to-ffrefine]]"
  - "[[wiki/answers/ffrefine-paper-methods-knowledge-base]]"
  - "[[wiki/answers/ffrefine-multi-series-equilibration-cut-calibration]]"
  - "[[wiki/answers/ffrefine-loss-gate-diagnostic-policy]]"
  - "[[wiki/answers/ffrefine-long-archive-target-gradient-convergence]]"
  - "[[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]]"
  - "[[wiki/questions/QST-0007-checkpoint-assessment-versus-next-direction-readiness]]"
  - "[[wiki/claims/CLM-0044-config-must-exclude-directionally-unreliable-families]]"
  - "[[wiki/claims/CLM-0048-family-weight-renormalisation-changes-natural-gradient-step-length]]"
  - "[[wiki/tensions/TEN-0020-config-family-exclusion-versus-untreated-drift]]"
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
  - "[[wiki/answers/ffrefine-generalist-package-plan-decisions]]"
project_evidence:
  - "FFRefine repository audit on 2026-10-01 at master 6b20031 (direction_gates.jl, production_decision.jl, configuration.jl, backend.jl, epoch_pipeline.jl, solvation_pipeline.jl, validity.jl, optimiser.jl, water_temperature.jl, hexane_temperature.jl, solvation.jl, optimisation_history.jl); the new gates became authoritative in commit 26affa0 and the production policy in e49cfde, both 2026-09-30"
  - "FFRefine design document for the improved gates (project-local, not a literature source), used for rationale and for its recorded analysis of runs 20260924-204914 and 20260928-220040; treated as rationale, not as a description of the code"
  - "FFRefine Monte Carlo checks in the direction-gate and production-decision test suites, with numbers as reported by the implementing session of 2026-09-28 to 2026-10-01; the test code was inspected for this write-back but the Monte Carlo numbers were not re-run"
  - "FFRefine shadow water run 20260928-220040 (legacy gates deciding, new gates in shadow), 11 epochs, as summarised in the design document"
  - "FFRefine water runs 20260930-132851 (ConFIG) and 20260930-132911 (weighted sum), rdf+density+dielectric, 50 ns production, both still running; per-epoch CSV records read on 2026-10-01 after 6 epochs each (provisional)"
  - "2026-10-05 update: weighted sum ended on an out-of-memory crash at its epoch-27 worker (last completed checkpoint 26, 107.9 h); ConFIG still running through checkpoint 33 (112.7 h); six production rescue extensions (five resolved, one cut short by the crash) read from per-epoch records, as detailed in [[wiki/answers/ffrefine-config-vs-weighted-sum-water-campaign-results]]"
  - "FFRefine commit 110fe64 (2026-10-07, \"Damped Levenberg-Marquardt trust-region step; report-only direction gates\"); FFRefine repository planning document `ffrefine_package_plan.md`, dated 2026-10-11, declaring the canonical regime (R) and the planned gate/ConFIG/momentum removal; see [[wiki/answers/ffrefine-generalist-package-plan-decisions]]"
---

# FFRefine Direction Gates and Extend-or-Exclude Production Policy

## Question

How do FFRefine's current direction gates and production-extension policy work at repository `master` commit `6b20031` (2026-10-01), and what reusable lessons and open questions did their construction and first campaigns produce?

## Short answer

Since 2026-09-30, FFRefine decides which target families the replay optimiser may use at a checkpoint with **block-based, aggregation-aware direction gates**, replacing the legacy chronological half-archive cosine/norm-ratio gate and the legacy delete-block reliability multiplier. The frozen production archive is cut into $B=8$ replica-stratified, time-contiguous jackknife blocks. From the leave-one-block-out family gradients the gates compute (i) a per-family **size** statistic (signal over jackknife standard error, against a Monte Carlo multiplier), which filters families before ConFIG (conflict-free inverse gradients) aggregation and is only reported under weighted-sum aggregation, and (ii) a **cross-fitted aggregation-promise test**: does the step the optimiser would actually take, recomputed without block $i$, still decrease block $i$'s pseudo-value of each included family (ConFIG) or of the weighted total (weighted sum), with confidence? Failing families are removed one at a time until the remaining set passes. A promise-drift test is computed but, by default, only reported.

A generic **extend-or-exclude production policy** then decides, before any replay chain is computed, whether to optimise the included families, extend the archive once ("rescue") to retest an excluded family, or stop. A rescue is bought only when its expected value in units of one epoch's progress is positive, and the retest of a rescued family is corrected for optional stopping by α-spending with a Monte Carlo threshold. Families that are excluded for noise in at least 3 of the last 5 epochs trigger a report-only suggestion of a longer production time. A checkpoint that still cannot optimise ends the campaign at its "noise floor".

All of this is FFRefine project design and project evidence, not a result evaluated in a literature source; ConFIG itself comes from SRC-0036. [SRC-0036] The first deciding campaigns (one ConFIG, one weighted sum, started 2026-09-30) were still running at the time of writing, so campaign evidence below is provisional.

## Detailed answer

### Where the gates sit in a macro epoch

For each epoch, an experiment script (water temperature ladder, hexane temperature ladder, or the two-leg ethanol solvation cycle) runs adaptive Times Square Sampling (TSS), a frozen parity probe, and a frozen-bias production archive (water default 60 ns; the 2026-09-30 water campaigns used 50 ns). The backend (`evaluate_optimisation_epoch`) builds window-mixture multistate Bennett acceptance ratio (MBAR) replay summaries, checks replay/TSS parity, effective sample size (ESS), split validation and Fisher validity, computes the full-objective fresh loss with per-family losses and delete-block standard errors (10 blocks for the fresh loss, independent of the gates' $B$), and then runs the direction gates. The gates run only when the evaluation and the Fisher metric are valid; if any leave-one-block-out subset misses a TSS window, the checkpoint is `:sampling_limited` with reason `:insufficient_gate_blocks`.

The production decision is taken immediately after the gates and **before** the replay chain (`evaluate_and_decide` passes an `optimisation_gate` callback into the evaluation). Only a checkpoint whose decision is "finish the epoch" computes the Kullback-Leibler (KL) bounded natural-gradient replay chain, restricted to the eligible families. The next epoch's fresh archive measures what the chain achieved.

### Blocks, pseudo-values and the size filter

Blocks are contiguous in time within each replica and stratified across replicas. For a family quantity $x$ with full-archive value $x$ and leave-one-block-out values $x_{(-i)}$, the pseudo-values are

$$
p_i[x]=B\,x-(B-1)\,x_{(-i)},\qquad i=1,\dots,B .
$$

The size statistic uses the family's **unscaled** treated direction $d_f$ (the damped or hard-cut natural-gradient step divided by its KL scale, so KL bounding does not equalise weak and strong families), measured in the Fisher metric $M$:

$$
\mathrm{signal}_f=\lVert d_f\rVert_M,\qquad
\mathrm{SE}_f=\sqrt{\tfrac{B-1}{B}\textstyle\sum_i\lVert d_{f,(-i)}-\bar d_f\rVert_M^2},\qquad
z_f=\mathrm{signal}_f/\mathrm{SE}_f .
$$

A family is `:resolved` if $z_f>m_{\mathrm{size}}$, `:negligible` if $\mathrm{signal}_f+m_{\mathrm{size}}\mathrm{SE}_f\le\varphi\max_g\mathrm{signal}_g$ with $\varphi=0.1$, otherwise `:uncertain`; a non-finite standard error is `:unavailable` and blocks the checkpoint. Under ConFIG only resolved families enter the promise stage; under weighted sum every family with a finite standard error enters, so small or noisy families are no longer excluded merely for being small or noisy.

### The aggregation-promise test

For an included set $S$, let $\hat u$ be the step the optimiser would take, built by the optimiser's own aggregation code (`config_natural_step` or the weighted-sum natural-gradient step) and normalised to unit Fisher length, and let $\hat u_{(-i)}$ be the same step built from the leave-one-block-out gradients. The tested gradient $g$ is each family's gradient under ConFIG, or the weighted total of $S$ under weighted sum (in both cases weighted as the optimiser weights $S$, i.e. renormalised over the included families). The cross-fitted values are

$$
q_i=-\big\langle p_i[g],\,\hat u_{(-i)}\big\rangle,\qquad
\bar q=\tfrac1B\textstyle\sum_i q_i,\qquad
t=\frac{\bar q}{s_q/\sqrt B},
$$

and the test passes when $\bar q-m_{\mathrm{promise}}\,s_q/\sqrt B>0$. Each $q_i$ scores a step that never saw block $i$ on block $i$'s own data, so a step that only fits noise should not pass. A degenerate leave-one-out step contributes $q_i=0$ and is counted; only a degenerate full-data step fails the whole set. The ratio $\rho_{\mathrm{survival}}=\bar q/\hat q$, with $\hat q=-\langle g,\hat u\rangle$ the in-sample promise, is recorded as a report-only "survival ratio" (in the code and design document this is called $\rho$, which collides with the production-cost $\rho$ below).

Removal loops:

- **ConFIG:** while any included family fails, remove the failing family with the lowest $t$ (reason `:descent_not_confident`), recompute the step for the smaller set, and retest.
- **Weighted sum:** while the total fails, remove the family whose removal gives the largest total $t$ (reason `:degrades_total`).

Regularisation components are aggregated into every step but are never tested or removed. Both aggregations are evaluated at every checkpoint; the configured one decides and the other is recorded, which makes the two methods comparable checkpoint by checkpoint.

### Multipliers

All tests use one false-alarm rate $\alpha$ (default 0.05).

- **Size multiplier:** Monte Carlo per checkpoint (20 000 draws, cached by $B$, parameter count and rounded spectrum) under a null in which gradient noise is proportional to the Fisher metric, with per-mode variances $1$ for kept modes (hard cut) or $(\lambda^2/(\lambda^2+\gamma^2))^2$ under damping. A `:worst_case` single-mode option exists. An observed-versus-expected effective-dimension mismatch larger than 3x raises a warning, not a gate.
- **Promise multiplier:** Monte Carlo per included set and aggregation (2000 draws), with null pseudo-values drawn with Fisher-proportional covariance, per-family scales and between-family correlations estimated from the whitened pseudo-values. If fewer than half the draws are non-degenerate, the analytic value is used instead. The analytic multiplier $\sqrt{2(B-1)/(B-2)}\,t_{1-\alpha,B-1}$ is still computed and reported.
- **Drift multiplier:** the one-sided Student-t quantile $t_{1-\alpha,B-2}$.

### Promise drift

With in-sample values $r_i=-\langle p_i[g],\hat u\rangle$ regressed on centred block times $t_i=i-(B+1)/2$ (slope $\beta$), the drift flag is $\beta/\mathrm{SE}(\beta)<-m_{\mathrm{drift}}$ **and** an extrapolated late value $r_{\mathrm{late}}=\bar r+\beta(B-1)/2\le0$. Under `drift_mode = :gate` (which requires $B\ge6$) a drift blocks the checkpoint; under the default `:report` it is recorded and the family stays eligible (`:promise_drift_reported`).

### Classification

Per-family decisions feed the unchanged `family_selection` rule: any blocking family gives `:sampling_limited` (`:direction_gate_blocked`); no eligible family, fewer than `min_eligible_families`, or an ineligible `required_families` member also give `:sampling_limited`; no exclusions give `:ready`; otherwise `:partial_ready`. `direction_ready` and `optimisation_ready` are true only for `:ready` or `:partial_ready` (or when no gate policy is configured), so the evaluation-validity versus direction-readiness separation of [[wiki/questions/QST-0007-checkpoint-assessment-versus-next-direction-readiness]] is preserved, with the new statistics replacing the half-archive cosine.

### The production decision

`production_decision` applies these rules in order (the first match wins):

1. under `loss_gate_mode = :enforce` only, a rejected proposal stops and an inconclusive blocked proposal extends by one `extension_time`; because the decision precedes the chain, this rule is re-applied after the chain (`decision_after_optimisation`);
2. an invalid evaluation extends by one `extension_time` while the budget lasts, otherwise stops;
3. a validation-only epoch finishes; gates that could not run (Fisher invalid, too few usable blocks) extend by one `extension_time`, otherwise stop direction-unready;
4. a blocking promise drift (only under `drift_mode = :gate`) extends by one `extension_time`, otherwise stops;
5. `:sampling_limited`: extend **once** by the largest rescue among failing families that are rescuable with exclusion cost $c_{\mathrm{ex}}=1$ (`:rescue_required`), otherwise stop **at once** without spending extensions (`:stop_unrescuable`);
6. `:partial_ready` with a rescuable excluded family: extend once by the largest such rescue (`:rescue_family`);
7. otherwise optimise the included families.

Independently, the water production loop extends production before evaluation when a TSS window is missing from the archive (coverage extension).

**Rescue sizing.** The rescue statistic is the debiased size statistic $z_{\mathrm{deb}}=\sqrt{\max(\mathrm{signal}^2-\mathrm{SE}^2,0)}/\mathrm{SE}$ for a ConFIG size exclusion, the family's promise $t$ for a ConFIG promise exclusion, and the total's promise $t$ with the family restored for a weighted-sum removal. Extending an archive of length $T$ to $\kappa T$ keeps the original frames, so the model is conditional, not independent:

$$
P(\kappa)=\Phi\!\left(\frac{\mu(\kappa)-m_1}{\sqrt{1-1/\kappa}}\right),\qquad
\mu(\kappa)=z\sqrt\kappa\ \text{(promise, total)},\quad
\mu(\kappa)=\sqrt{\kappa z_{\mathrm{deb}}^2+1}\ \text{(size)},
$$

$$
V(\kappa)=P(\kappa)\,c_{\mathrm{ex}}-(\kappa-1)\,\rho-c_0 .
$$

Here $c_{\mathrm{ex}}$ is the family's full-objective loss share (1 when nothing can be optimised without it), $\rho$ is one production period's wall time and $c_0$ one re-evaluation's wall time, both as fractions of the previous epoch's wall time (fallbacks 1.0 and 0.05 before any measurement). $\kappa^*=\arg\max V$ is searched on multiples of the sampler's smallest unit (one TSS cycle for water), capped by `max_rescue_kappa` (2) and by the remaining extension budget; a rescue happens only if $V(\kappa^*)>0$. A family with $z\le0$ or labelled negligible is never rescuable. Every production leg is extended by the same fraction of its own kept time.

**Rescue looks and α-spending.** A family is re-tested once after its rescue and that result is final for the checkpoint (a failed look keeps it excluded as `:rescue_look_failed`). When a rescue is possible, "importance-eligible" families (required, or loss share above $c_0$) are tested at look 0 with $\alpha_0=(1-s)\alpha$ (`rescue_alpha_share` $s=0.2$, so $\alpha_0=0.04$). The look-1 threshold $m_1$ is found by bisection so that, under the same null noise model, $P(\text{pass at look 0})+P(\text{fail, qualify under the actual rescue rule, pass at look 1})\le\alpha$, simulating archives at 64 time units per production period and re-blocking into $B$ blocks at each look. The included set is held at its look-0 value (an approximation). When several families share one rescue, the extension is the largest $\kappa^*$, and a family extended beyond its own $\kappa^*$ is retested at the larger of its own $m_1$ and the $m_1$ calibrated for the applied extension.

**Persistent exclusions (report only).** A warning fires when a family was excluded for noise (`:uncertain`, `:descent_not_confident`, `:degrades_total`) with $z>0$ and not negligible in at least 3 of the last 5 epochs (not necessarily consecutive) and its current loss share exceeds $c_0$. It suggests the production time $T'=T\,((\tilde m+z_\beta)/\tilde z)^2$ from median statistic and threshold over the counted exclusions, $z_\beta=\Phi^{-1}(0.8)$. This is the independent-data formula, appropriate because each checkpoint has a fresh archive; it is not applied automatically.

**Campaign end.** A direction-unready checkpoint is repeated at unchanged parameters with a fresh archive up to `max_unready_epochs` times (default 0), after which the campaign ends with reason `:noise_floor` (or `:gates_not_evaluated` when the gates never ran), listing each failing family's suggested production time. The macro loop also stops when a replay chain accepts no proposal, and then runs final-validation replicas of the latest checkpoint. Stale fresh-loss epochs are counted and recorded, but no code path in the epoch pipeline stops on them (the `early_stopping_patience` configuration key is not read).

### Configuration surface and defaults

Every field of `ArchiveGradientPolicy` (group `gate`), `ExtensionPolicy` (group `extension`) and, for water only, `EquilibrationPolicy` (group `equilibration`) is resolved with precedence: environment variable `<PREFIX>_<GROUP>_<FIELD>` (prefixes `WATER`, `HEXANE`, `SOLVATION`), then `config.<group>.<field>`, then a legacy flat key (water only: `min_eligible_families`, `required_families`, `equilibration_mode`), then the policy default. Unknown variables with a known group prefix and unknown nested fields are errors, every policy is built once at start-up, and every resolved value and its source is written to the experiment metadata. The aggregation is a separate experiment-level setting, `<PREFIX>_GRADIENT_AGGREGATION`, then `config.gradient_aggregation`, then `:weighted_sum`. The optimisation-history schema is version 34.

Gate defaults: $B=8$, $\alpha=0.05$, `multiplier_mode = :model`, `drift_mode = :report`, `negligible_fraction = 0.1`, `min_eligible_families = 1`, no required families, `promise_calibration = :monte_carlo`. Extension defaults: `exclusion_cost = :loss_share`, measured production and re-evaluation costs, `max_rescue_kappa = 2`, `rescue_alpha_share = 0.2`, persistent warning 3 of 5 at power 0.8, `max_unready_epochs = 0`. Experiment configs set: water `:config`, `momentum_beta = 0`, damped Fisher $\gamma=0.1$ (`drift_mode = :report` set explicitly); hexane `:config` with `momentum_beta = 0.25`; solvation `:weighted_sum` with `momentum_beta = 0.5`. Water's `max_production_extensions` defaults to 0 (environment-configurable), which makes every extension, including rescues, impossible; the 2026-09-30 campaigns used 5 extensions of 10 ns on a 50 ns production.

### Momentum and what the gates certify

`OptimiserSettings` defaults to `momentum_beta = 0.5` for both aggregations (guarded component-wise under ConFIG, and by descent on the total under weighted sum), but damped Fisher requires `momentum_beta = 0`. The gates build the aggregated step without momentum. Synthesis (not tested): with momentum switched on, as in the hexane and solvation defaults, the step actually taken mixes in the previous displacement and is therefore not the step the promise test certified.

### Report-only diagnostics kept alongside the gates

- **Equilibration cut (water only).** Per replica, one loss-sensitivity-weighted series per observable family (tolerance-weighted on the raw production data) plus the active-state reduced potential, each centred per sampled state; the cut maximises $N_{\mathrm{eff}}=(N-t_0)/g(t_0)$ with the fast multiscale statistical inefficiency; a series' cut counts only if material under a δ table keyed on the series count and the smallest $N/g_{\mathrm{late}}$; the latest material cut wins; a cut above half the archive is flagged. No frame is removed, `:apply` is not implemented, and failures never abort a checkpoint. See [[wiki/answers/ffrefine-multi-series-equilibration-cut-calibration]].
- **Chain-level diagnostics.** Per-family fresh losses with jackknife standard errors; replay calibration of each chain's predicted per-family change against the next fresh change, with a telescoping cumulative standard error and warnings at cumulative $|z|>3$ or a same-sign streak of at least 4; step-to-family angles with a near-orthogonal flag; exclusion-cycle bookkeeping. See [[wiki/answers/ffrefine-improved-gates-water-run-lessons]].
- **Full-objective-scale loss reporting.** Logged losses and loss thresholds are reported on the full-objective scale, while the optimiser step still uses weights renormalised over the included families (see [[wiki/claims/CLM-0048-family-weight-renormalisation-changes-natural-gradient-step-length]]).
- **Legacy-comparable half cosine.** An early-versus-late cosine of mean pseudo-values is still reported, never gated.

## Key equations

$$
p_i[x]=B\,x-(B-1)\,x_{(-i)}
$$

$$
q_i=-\big\langle p_i[g],\hat u_{(-i)}\big\rangle,\qquad \text{pass iff }\ \bar q-m_{\mathrm{promise}}\,s_q/\sqrt B>0
$$

$$
V(\kappa)=\Phi\!\left(\frac{\mu(\kappa)-m_1}{\sqrt{1-1/\kappa}}\right)c_{\mathrm{ex}}-(\kappa-1)\rho-c_0
$$

$$
T'=T\left(\frac{\tilde m+z_\beta}{\tilde z}\right)^2
$$

## Validation and implementation lessons

These lessons come from Monte Carlo checks in FFRefine's tests and from campaign records. Numbers marked as session-reported were reported by the implementing session and were not re-run for this write-back.

1. **A null drawn from few pseudo-values is too lenient.** Drawing the promise-test null from the sample covariance of only $B=8$ pseudo-values (rank $B-1$) understates the effective noise dimension and gave null false-pass rates of 0.08–0.10 at nominal 0.05. A Fisher-proportional noise model with data-estimated family scales and correlations brought weighted-sum rates to 0.049–0.053 and put the ConFIG multiplier within about 5% of the exact null quantile; the per-dataset ConFIG procedure remains slightly liberal (about 0.06–0.07) because scales and correlations come from the data being tested. See [[wiki/claims/CLM-0049-few-block-pseudo-value-covariance-understates-promise-null]].
2. **The analytic inflation fits only one tested quantity.** Cross-fitted $q_i$ share terms through the leave-one-out steps (correlation about $1/(B-1)$), so plain $t_{1-\alpha,B-1}$ is too liberal (0.10–0.13 for one family or the total). The analytic inflation $\sqrt{2(B-1)/(B-2)}$ is right for one family or the weighted total but far too strict for multi-family ConFIG (about 2.9 against an exact quantile of about 2.1; false-pass about 0.015).
3. **Re-testing a family because it failed is optional stopping.** Session-reported: uncorrected, the two-look false-pass rate is about $1.45\alpha$ (0.0727 for the size test, 0.070 for the promise test); with α-spending it was 0.051 and 0.056. See [[wiki/claims/CLM-0050-retesting-a-failed-gate-after-extension-needs-alpha-spending]].
4. **The conditional extension model is a guide, biased in a known direction.** Session-reported: it is pessimistic for short extensions because re-blocking re-estimates the standard error (at $\kappa=1.1$, $z=1.6$: realised pass rate 0.23 against predicted 0.08), agreeing once new data dominate ($\kappa\ge1.5$); and a statistic that has just failed is biased low (after selection, realised 0.565 against predicted 0.458). The independent-data formula $((m+z_\beta)/z)^2$ overstates the data an extension needs.
5. **Debias a vector-length statistic before predicting rescues.** With no true gradient, signal/SE stays near 1 however much data is collected. The debiased statistic's null distribution does not depend on the amount of data (mean about 0.27, exactly zero in about 55% of draws), and its debiased signal estimate goes to 0, so it never predicts rescues that cannot happen.
6. **A failed gate cannot tell "no descent" from "not enough data".** Because each checkpoint starts a fresh archive of the same length at new parameters, a family's standard error does not shrink between checkpoints, and a family whose true statistic sits near its threshold flips in and out; only an extension within a checkpoint accumulates data at fixed parameters. In the shadow run the cost of excluding the heavy dielectric family included its forgone progress (about 60–90% of an epoch's progress), not only its rise while excluded (0.03–0.18). See [[wiki/tensions/TEN-0020-config-family-exclusion-versus-untreated-drift]].
7. **Measure costs; do not assume them.** The design assumed one production period cost about 0.85 of an epoch and one re-evaluation about 0.05 (shadow-run timings). In the 2026-09-30 ConFIG campaign the measured values were $\rho\approx0.40$–$0.45$ and $c_0\approx0.09$–$0.11$, which changes which rescues have positive expected value.
8. **A rescue's pass-probability model must score every stage a family still has to clear, not only the stage it currently failed.** By 2026-10-05, five rescues had resolved and one had been cut short by a crash (see below): one ConFIG promise-test rescue passed and ran (epoch 27, $t=2.18\to2.67$ against $m_0=2.26$); two ConFIG size-filter rescues passed their own (size) statistic and then failed the *later* promise stage because of a genuine inter-family conflict (epoch 29: size $z$ 1.26$\to$1.97 passed, promise $t=-3.04$ failed; epoch 32: size $z$ 1.52$\to$2.67 passed, promise $t=0.48$ failed) — the extension was bought and "succeeded" by its own test, but contributed nothing; and two weighted-sum rescues used the total's $t$ with the family restored rather than the family's own debiased size statistic, so the policy's intended protection against rescuing a family that is simply at its own constrained optimum (which keys off that family's own size statistic; a family with $z\le0$ or negligible is never rescuable) never engaged — a family at a genuine optimum with a large loss share (density, holding about 54% of the loss) looked rescuable twice (epoch 26: predicted total $t$ 2.79, realised 1.40, failed; epoch 27: gate passed at 2.84 against threshold 2.73, but the worker was killed before any chain ran). See [[wiki/answers/ffrefine-config-vs-weighted-sum-water-campaign-results]] for the full six-rescue account and the all-three-family-conflict context that produced the ConFIG rescues.
9. **A measured production-cost fraction is only meaningful relative to a non-pathological epoch.** $\rho$ is defined relative to the *current* epoch's own wall time; once a run enters a slow or crawling regime, its own inflated wall time becomes the denominator, so further extensions can look artificially cheap. Weighted sum's measured $\rho$ fell to 0.18–0.28 during a crawl regime (chains using all 21 proposals for tiny, well-calibrated steps), against about 0.48 for ConFIG's faster epochs in the same window — the same cost model, applied to runs in different dynamical regimes, gives cost estimates that are not comparable across those regimes.
10. **The rescue model has no memory-cost term, and an archive extension is exactly the operation that raises a worker's peak memory.** A replay worker's resident memory grew roughly linearly with archive frame count in production (about 11 MB per frame, of which about 6 MB was live GC heap); a normal 50 ns (10,001-frame) epoch peaked at 205–260 GB, and rescue-extended archives (14,440–17,282 frames) peaked at 290–311 GB. One worker was killed by the kernel's out-of-memory killer during a rescued epoch while a second campaign's worker held a large but separate allocation on the same node; the two campaigns' ordinary peaks already summed to roughly the node's total memory, and a rescue extension was what pushed the combined total over the edge. The run's monitoring reported the killed worker as having exited with code 0, because a kernel signal kill leaves a Julia process's exit code at 0 with a failed status and records the signal separately (`termsignal`), which the message did not print — so it looked like a clean exit unless the signal itself is surfaced. Candidate remedies, untested: cap the rescue multiplier $\kappa$ by predicted frame count times measured bytes-per-frame against an explicit memory budget; bound the worker's heap; avoid co-scheduling campaigns whose ordinary peak memory can coincide on one node; and report terminating signals, not only exit codes. See [[wiki/answers/ffrefine-config-vs-weighted-sum-water-campaign-results]] and [[wiki/answers/ffrefine-current-implementation-status]].

## Provisional campaign evidence (recorded 2026-10-01)

- **Legacy run `20260924-204914`:** the half-archive gate blocked checkpoints at signal/SE 2–4 and cost about 13% of wall time; see [[wiki/answers/ffrefine-improved-gates-water-run-lessons]].
- **Shadow run `20260928-220040`** (legacy gates deciding, new gates in shadow, 11 epochs; fresh loss 10.1 to 2.97), as summarised in the design document: the dielectric family (weight 10, 40–60% of the loss) had promise $t$ between 0.7 and 5.1 against thresholds of about 2.0 and was excluded in 5 of 11 epochs, never more than two in a row; the legacy gate's extensions (about 4 h over 11 epochs) were spent where the failing families needed about 3–4 times more data, and the new rules would have avoided them; the promise-drift slope $t$ was well calibrated (variance 1.48 against 1.5 expected, 3 of 27 below $-m_{\mathrm{drift}}$ against 1.35 expected, none with $r_{\mathrm{late}}\le0$); weighted sum would have kept every family, with steps at 90–118° to one family in several epochs; the equilibration cut was never material beyond 1.6%; the gates cost about 170 s per evaluation, of which the Monte Carlo calibrations took 5–8 s.
- **ConFIG run `20260930-132851`** (gates deciding, 6 epochs so far, still running): fresh loss 10.59, 8.11, 6.77, 7.05, 5.88, 5.77. Dielectric was excluded as `:descent_not_confident` in 4 of 6 epochs (2, 3, 5, 6; promise $t$ 1.27–1.63 against thresholds 2.12–2.31) while holding 57–65% of the loss; every rescue had negative expected value, so no rescue extension ran. Persistent-exclusion warnings at epochs 5 and 6 suggested production times of about 186 and 198 ns against the 50 ns used. Density's cumulative replay-calibration $z$ exceeded 3 from epoch 4 (3.17–4.19; replay predictions optimistic).
- **Weighted-sum run `20260930-132911`** (6 epochs so far, still running): fresh loss 9.76, 8.24, 6.70, 6.26, 5.24, 4.35; no family was excluded (total promise $t$ 3.03–8.48 against thresholds 2.69–2.80). Density's cumulative calibration $z$ exceeded 3 from epoch 3 (3.36–4.48), and RDF's reached 3.17 at epoch 6.

These two runs are single seeds with different epoch-1 fresh losses; they do not yet answer which aggregation is better. See [[wiki/questions/QST-0011-config-versus-weighted-sum-under-calibrated-direction-gates]] and [[wiki/questions/QST-0012-persistent-replay-prediction-optimism-for-one-family]].

**2026-10-04 update:** both campaigns are still running; a snapshot was taken at weighted sum 23 epochs/90.8 h and ConFIG 27 epochs/92.3 h. The interim comparison, including a late conflict-driven dielectric exclusion that regressed ConFIG's loss, one rescue extension (the first observed in a deciding campaign), a weighted-sum KL-capped step-oscillation pathology, and the physical trade-offs each aggregation reached so far, is in [[wiki/answers/ffrefine-config-vs-weighted-sum-water-campaign-results]].

**2026-10-05 update:** weighted sum is no longer running — its epoch-27 worker was killed by an out-of-memory condition at the first replay proposal of epoch 27, after its direction gates had already passed a rescue for density; its last completed checkpoint is 26 (107.9 h), plateauing at about -0.03/epoch with density excluded for 5 consecutive epochs at a genuine (noise-level) constrained optimum, and its earlier two-cycle oscillation replaced by a crawl once density left the step. ConFIG is still running (checkpoint 33, 112.7 h, epoch 34 in progress); its fresh loss rose from a best of 1.82 to 5.05 over checkpoints 27–32 as density and dielectric began seesawing with a net ascent and all three families turned pairwise conflicting. Lessons 8–10 above come from this update's six rescue extensions and the out-of-memory crash; full numbers in [[wiki/answers/ffrefine-config-vs-weighted-sum-water-campaign-results]].

## Design document versus code

The project's design document mixes implemented behaviour, planned stages and superseded drafts. Where they differ, the code (master `6b20031`) is authoritative:

- The document's statistics table labels promise drift as a gate; the code default is `drift_mode = :report` (the document's open decisions agree that report-only is the first-campaign default).
- The document's rule table includes a `:not_equilibrated` rule and re-detecting the equilibration cut after drift; the code has no equilibration-based rule because the cut is report-only and `:apply` is not implemented. Gradient series and `:cut_unstable` in the equilibration report are stage-2 plans.
- The document's rule numbering omits the enforced-loss-gate and "gates could not run" rules that the code applies.
- Field names differ: the document's `gate_blocks`, `drift_gate_mode`, `max_equilibration_fraction` and `equilibration_grid_stride` are `blocks`, `drift_mode`, `max_fraction` and `grid_stride` in the code; the equilibration cut works per series (`equilibration_cut`) with a separate per-replica report, not as a function returning kept frame indices.
- The document lists `loss_gate_mode` among the water legacy aliases; in the code it is an ordinary water config key read by the optimiser and replay settings, not part of the policy surface.
- The document cites history schema 32; the code is at 34.
- The document's measured costs (0.85 and 0.05) are shadow-run values; the 2026-09-30 campaign measured about 0.45 and 0.10.

## 2026-10-07 and 2026-10-11 status update: gates retired under the canonical regime

**2026-10-07 (commit `110fe64`, "Damped Levenberg-Marquardt trust-region step; report-only direction gates").** The natural-gradient step described throughout this page was replaced by a damped Levenberg-Marquardt trust-region step, and the direction gates were made report-only (`gate_mode=report`): by this date they no longer decide family eligibility or the production decision at all. **The rationale for this specific change is not recorded anywhere in the project or in SecondBrain; this page does not speculate about it.**

**2026-10-11 (planning document).** This report-only combination, together with weighted-sum aggregation, was declared the project's canonical regime (decision R). The planning document gives two reasons to remove the direction gates entirely (not yet done in code as of 2026-10-11), rather than leave them as report-only diagnostics:

1. In report mode they never exclude a family or block a step, so they already have no operational effect.
2. They test the natural-gradient direction described throughout this page, not the trust-region step the canonical regime actually takes. A report-only diagnostic that certifies a step the optimiser never takes is not informative, independent of whether the gates' own statistics are well calibrated.

Also decided for removal under the canonical regime: ConFIG aggregation (so the ConFIG-versus-weighted-sum comparison this page and [[wiki/questions/QST-0011-config-versus-weighted-sum-under-calibrated-direction-gates]] describe is no longer pursued operationally, independent of its scientific outcome), rescue/extension sizing (the production decision reduces to "extend production once if evaluation validity fails, otherwise optimise"), momentum, the natural-gradient step and its proposal path, loss gates in every mode, the archive KL budget, and Huber loss. See [[wiki/answers/ffrefine-generalist-package-plan-decisions]] and [[wiki/answers/ffrefine-current-implementation-status]] for the full removal list and its rationale.

**What remains valid.** CLM-0049 and CLM-0050 are statistical claims about Monte Carlo calibration of a cross-fitted promise test under a fixed block count; they remain correct statistical findings about that calibration procedure, independent of whether FFRefine continues to use the gates in production. Removing the gates does not retract these claims; it only means FFRefine no longer applies the calibrated procedure they describe.

**The momentum open issue is now moot.** The "Remaining gaps" item below, "the gates certify the non-momentum step; whether momentum ... should be disabled or the momentum step certified is open", is moot once momentum itself is removed under the canonical regime: there is no momentum step left to certify or not certify.

## Sources used

- SRC-0036 for ConFIG itself; every other statement is FFRefine project evidence listed in this page's frontmatter.

## Wiki pages used

- [[wiki/answers/ffrefine-current-implementation-status]]
- [[wiki/answers/ffrefine-improved-gates-water-run-lessons]]
- [[wiki/answers/adding-config-optimiser-to-ffrefine]]
- [[wiki/answers/ffrefine-loss-gate-diagnostic-policy]]
- [[wiki/answers/ffrefine-multi-series-equilibration-cut-calibration]]
- [[wiki/questions/QST-0007-checkpoint-assessment-versus-next-direction-readiness]]
- [[wiki/tensions/TEN-0020-config-family-exclusion-versus-untreated-drift]]
- [[wiki/claims/CLM-0044-config-must-exclude-directionally-unreliable-families]]
- [[wiki/claims/CLM-0048-family-weight-renormalisation-changes-natural-gradient-step-length]]
- [[wiki/answers/ffrefine-generalist-package-plan-decisions]]

## Wiki updates made

- Added this answer note, [[wiki/claims/CLM-0049-few-block-pseudo-value-covariance-understates-promise-null]], [[wiki/claims/CLM-0050-retesting-a-failed-gate-after-extension-needs-alpha-spending]], [[wiki/questions/QST-0011-config-versus-weighted-sum-under-calibrated-direction-gates]], [[wiki/questions/QST-0012-persistent-replay-prediction-optimism-for-one-family]] and [[wiki/questions/QST-0013-step-length-policy-after-family-exclusion]].
- Marked the legacy half-archive gate and legacy reliability screen as superseded where pages described them as current, and refreshed the implementation-status snapshot.
- **2026-10-11:** added the status-update section above recording the 2026-10-07 trust-region/report-only-gates change (rationale not recorded) and the 2026-10-11 decision to remove the gates, ConFIG, and momentum entirely under the canonical regime; linked [[wiki/answers/ffrefine-generalist-package-plan-decisions]].

## Remaining gaps

- Weighted sum's campaign ended on an out-of-memory crash, not a `:noise_floor` stop or a clean completion; ConFIG is still running. No deciding campaign has yet reached `:noise_floor` through the gates' own logic.
- The rescue policy's pass-probability model, weighted-sum rescue statistic, and cost-fraction normalisation all have generic flaws exposed only once several rescues had been observed (lessons 8–9 above); none of the candidate fixes are implemented.
- The production-extension policy has no memory-budget term (lesson 10); a rescue extension can push a worker's resident memory past what the node can provide, especially when another campaign is co-scheduled on the same node.
- Whether promise drift should gate (`drift_mode = :gate`) is undecided; so far it has only been checked for calibration in the shadow run.
- Only a checkpoint's first step is certified; later proposals in a replay chain are not re-certified, and the survival ratio has not yet been compared against realised fresh changes.
- The gates certify the non-momentum step; whether momentum (hexane, solvation defaults) should be disabled or the momentum step certified is open. **Moot as of 2026-10-11:** momentum is decided for removal under the canonical regime (see the 2026-10-07/2026-10-11 status update above).
- The equilibration report is enabled only for water; hexane and solvation would first need per-frame series for their fluctuation observables.
- The step-length and renormalisation policy remains undecided; see [[wiki/questions/QST-0013-step-length-policy-after-family-exclusion]].
- The Monte Carlo numbers in lessons 3 and 4 were not re-run for this write-back.
