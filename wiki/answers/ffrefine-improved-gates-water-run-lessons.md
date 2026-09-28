---
type: answer
status: active
created: 2026-09-28
updated: 2026-09-28
question: "What did designing calibrated, cross-fitted replay-chain diagnostics against FFRefine water run 20260924-204914 reveal about replay-prediction calibration, the optimiser's curse, family-weight renormalisation, and the legacy half-archive stability gate?"
answer_status: answered
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/molecular-simulation/free-energy
  - research/statistics/monte-carlo
  - research/scientific-computing
tags:
  - ffrefine
  - replay-reweighting
  - config
  - trust-region
  - validation-policy
  - kl-conditioning
related:
  - "[[wiki/answers/adding-config-optimiser-to-ffrefine]]"
  - "[[wiki/answers/ffrefine-loss-gate-diagnostic-policy]]"
  - "[[wiki/tensions/TEN-0020-config-family-exclusion-versus-untreated-drift]]"
  - "[[wiki/claims/CLM-0044-config-must-exclude-directionally-unreliable-families]]"
  - "[[wiki/claims/CLM-0048-family-weight-renormalisation-changes-natural-gradient-step-length]]"
  - "[[wiki/questions/QST-0007-checkpoint-assessment-versus-next-direction-readiness]]"
  - "[[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]]"
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
sources: []
sensitivity: public
encryption: none
wiki_pages_used:
  - "[[wiki/answers/adding-config-optimiser-to-ffrefine]]"
  - "[[wiki/answers/ffrefine-loss-gate-diagnostic-policy]]"
  - "[[wiki/tensions/TEN-0020-config-family-exclusion-versus-untreated-drift]]"
  - "[[wiki/questions/QST-0007-checkpoint-assessment-versus-next-direction-readiness]]"
raw_sources_consulted: []
wiki_pages_updated:
  - "[[wiki/answers/ffrefine-improved-gates-water-run-lessons]]"
  - "[[wiki/answers/adding-config-optimiser-to-ffrefine]]"
  - "[[wiki/tensions/TEN-0020-config-family-exclusion-versus-untreated-drift]]"
  - "[[wiki/questions/QST-0007-checkpoint-assessment-versus-next-direction-readiness]]"
  - "[[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]]"
project_evidence:
  - "FFRefine water run 20260924-204914 (families rdf, density, dielectric; family weights 1, 2, 10; family-level Fisher-whitened ConFIG), epochs 1-22"
  - "FFRefine `improved-gates` worktree branch, commits 20d286f and 16ea49a, and design document `improved_gates_plan.md`"
---

# FFRefine Improved Replay-Gate Design: Lessons From Water Run 20260924-204914

## Short answer

Designing calibrated, cross-fitted diagnostics against a 22-epoch multi-family water run (`20260924-204914`; rdf, density, dielectric under family-level Fisher-whitened ConFIG) surfaced four related findings, all evidenced by this one run and by the resulting unit tests, not by literature sources:

1. **Replay predictions can be checked for calibration, and a naive cumulative-error formula understates the run's real, telescoping uncertainty.**
2. **The run shows the "optimiser's curse":** from epoch 10 on, a converged family's replay-predicted improvement was optimistic in most epochs, consistent with a chain optimising its own replay estimate.
3. **Renormalising the remaining family weights to sum to 1 after excluding a family is not scale-neutral for the optimiser:** it leaves directions unchanged but rescales the natural-gradient step length, and it happened to act as a large accidental step-size boost in exactly the epochs where the smallest family made its best progress. See [[wiki/claims/CLM-0048-family-weight-renormalisation-changes-natural-gradient-step-length]].
4. **The legacy chronological half-archive stability gate (cosine similarity ≥ 0.8) mostly reacts to ordinary sampling noise, not to real drift,** and cost about 13% of the run's wall time while never catching the run's actual failure mode. This motivates replacing it with a cross-fitted, out-of-sample "aggregation promise" test rather than an uncalibrated cosine threshold.

## Detailed answer

### Replay calibration and telescoping cumulative error

Each epoch's replay chain predicts, per family, how the full-objective loss will change by the end of the chain; the next epoch's fresh production then measures what actually happened. Comparing the two per family and per epoch gives a calibration error $e=\text{realised}-\text{predicted}$ with an approximate standard error $\sqrt{\mathrm{SE}_\text{parent}^2+\mathrm{SE}_\text{new}^2}$, since the prediction's own sampling noise comes from the parent archive.

Tracking this error *across* epochs is not a simple sum-of-variances problem, because consecutive errors share an archive and the realised fresh-loss changes telescope: $\sum_e(\text{fresh}_{e+1}-\text{fresh}_e)=\text{fresh}_\text{end}-\text{fresh}_\text{start}$. The cumulative calibration error is therefore $\text{fresh}_\text{end}-\text{fresh}_\text{start}-\sum_e\Delta^\text{pred}_e$, and its standard error is approximately

$$
\mathrm{SE}_\text{cumulative}\approx\sqrt{\mathrm{SE}_\text{start}^2+\mathrm{SE}_\text{end}^2+\sum_e\mathrm{SE}^2(\Delta^\text{pred}_e)}
$$

not $\sqrt{\sum_e\mathrm{SE}_e^2}$. Here $\mathrm{SE}(\Delta^\text{pred}_e)$ is the delete-block jackknife standard error of the *predicted change itself* (both ends of the change evaluated on the same archive frames), which is small in practice: 3.5-7% of the fresh-loss standard error on a synthetic fixture used to validate the formula. A Monte Carlo check with unbiased, correctly calibrated predicted changes found the naive $\sqrt{\sum\mathrm{SE}_e^2}$ formula gave a 0% false-alarm rate for $|z|>3$ (i.e., never triggers, because it overstates uncertainty and never allows the cumulative signal to look surprising), while the telescoping formula above gave 0.29% against a nominal 0.27% for the same $|z|>3$ threshold — correctly calibrated.

**Implementation lesson.** When constructing a delete-block jackknife of the *candidate* (reweighted) replay summary for this purpose, the block-subsetted candidate estimate must reuse the corresponding block-subsetted *parent* summary's MBAR reference weights. Re-solving the MBAR reference from the candidate's own reweighted energies on the same subset silently gives the wrong answer, because it changes what "the same frames" means between the parent and candidate estimates being differenced.

### The optimiser's curse in replay chains

Applying the calibration diagnostic to run `20260924-204914` found that density's replay prediction was optimistic in every epoch from 4 to 9 (mean error about +0.05, six of six same-sign), while RDF's predictions were accurate over the same span and dielectric's were noisy but unbiased. Density's large early moves were about 25% optimistic in magnitude (about -1.28 predicted against -1.02 realised; about -0.83 against -0.60), while its later large moves (epoch 10 onward) were accurate (about +0.58 predicted against +0.57 realised; about -0.52 against -0.49).

From epoch 10 on, once dielectric had converged, the *total* objective was worse than the replay chain had predicted in 9 of 12 epochs (mean error about +0.033 per epoch, roughly a third of the predicted per-epoch progress), driven mainly by dielectric (worse than predicted in 8 of 12 epochs, mean error about +0.027). This is the pattern expected when a multi-step replay chain is effectively optimising its own replay estimate rather than the true fresh objective: later, uncertified proposals in a chain can keep "improving" an estimate that is itself drifting away from what fresh resimulation will show, an instance of the general optimiser's-curse phenomenon. Per-checkpoint gates cannot see this by construction, because the bias accumulates across the several proposals *within* one replay chain, after the checkpoint that a gate evaluates. This motivates cross-fitted, out-of-sample checks at the level of an individual proposal step — a planned "survival ratio" $\rho$, the fraction of a step's in-sample first-order promised decrease that survives when the step is recomputed leaving out each data block in turn — as a complementary, earlier-acting diagnostic to the calibration check above; the calibration check catches drift across an entire chain and into deep reweighting extrapolation, while the per-step ratio only covers a proposal's own first step.

### Renormalising family weights is an implicit step-size change

FFRefine drops excluded families from the objective and renormalises the remaining family weights to sum to 1 (for example, rdf's effective weight rises from 1/13, when density and dielectric are also included at weights 2 and 10, to 1 in an rdf-only epoch). This renormalisation does not change the step's *direction* among the included families: it is a common rescaling for weighted sum, and ConFIG unit-normalises each included component's gradient regardless. It does change the objective's magnitude, and because the optimiser's natural-gradient step uses a fixed learning rate of 1 that is only ever capped (never lengthened) at a KL target, it changes the *uncapped* step length before that cap is applied.

Reconstructing the uncapped ConFIG step KL as $\tfrac12|c|^2$ from the logged `h_dot_c` diagnostic matched the logged KL in uncapped epochs, confirming the reconstruction is faithful. In two rdf-only epochs (10 and 18, KL target 0.095), today's renormalised uncapped KL was 0.77 and 0.30 (both capped down to 0.095); without renormalisation it would have been only 0.0045 and 0.0018 — three orders of magnitude smaller and no longer capped at all. These were the same two epochs in which rdf made its largest per-epoch loss decreases in the run (about -0.128 and -0.083), so renormalisation acted as an accidental step-size boost in exactly the epochs where it happened to help. See [[wiki/claims/CLM-0048-family-weight-renormalisation-changes-natural-gradient-step-length]] for the full evidence and caveats.

**Lesson.** Step length in a KL-capped natural-gradient optimiser depends on the objective's arbitrary scale, so any policy for renormalising an objective after excluding components must be decided together with the step-length policy, not as an independent bookkeeping choice. Reporting and threshold diagnostics (logged loss, stale-progress rules, `max_loss_increase`) should be evaluated on a scale that is consistent across epochs regardless of which families are currently included, independently of whatever scale the step itself uses.

### The legacy half-archive stability gate reacts to noise

Separately from family-size (reliability) screening, FFRefine's existing direction-readiness check splits the frozen archive into two chronological halves and requires the treated (Fisher-whitened) direction's cosine similarity between halves to be at least 0.8, with a companion norm-ratio check in [0.5, 2]. Over the first 22 epochs of run `20260924-204914`, this test blocked 5 checkpoints (epochs 5, 8, 13, 15, and 19), each time because a family with a signal-to-standard-error ratio of only about 2-4 had chronological half-cosines of 0.39-0.78 (dielectric) or, once, density — cosines that low are exactly what sampling noise alone produces at that signal/SE ratio, not evidence of a real change in direction over time. The blocked checkpoints forced 13 production extensions, costing roughly 11 hours of the run's wall time (about 13%), including at least one case where the block "passed" only because a later, noisy retry happened to land above the threshold, not because new information had arrived. The companion norm-ratio check was inert whenever both chronological halves were still capped at the same KL target (both then have the same Fisher-metric length by construction, giving a ratio near 1), and only became informative once a family's signal fell below the cap — at which point it was still being compared against a threshold with no noise model behind it.

**Lesson and planned response.** A fixed cosine/norm-ratio threshold conflates "noisy" with "genuinely drifting," is not tied to any noise model, and does not account for the number of included families or the aggregation method. The planned replacement is a cross-fitted "aggregation promise" test evaluated at the level of the step the optimiser is about to take, rather than at the level of a family's raw direction: for ConFIG, whether the step still promises descent for every included family; for weighted sum, whether it still promises descent for the weighted total. Both are evaluated out of sample (the step is recomputed leaving out each jackknife block in turn and scored on that block's own data), which is designed to reject a step that is fitting noise while still passing an in-sample check, and to be comparable across different numbers of included families and different aggregation methods without a hand-set angle threshold. This test is a design proposal at the time of writing, not yet implemented or campaign-validated; see [[wiki/questions/QST-0007-checkpoint-assessment-versus-next-direction-readiness]] for the related distinction between evaluation validity and next-direction readiness that this test is intended to refine.

## Key equations

Telescoping cumulative calibration-error standard error:

$$
\mathrm{SE}_\text{cumulative}\approx\sqrt{\mathrm{SE}_\text{start}^2+\mathrm{SE}_\text{end}^2+\sum_e\mathrm{SE}^2(\Delta^\text{pred}_e)}
$$

as against the naive (and, in this run's Monte Carlo check, uncalibrated) $\sqrt{\sum_e\mathrm{SE}_e^2}$.

## Sources used

None. All findings in this note are FFRefine project evidence from run `20260924-204914` and its accompanying unit tests and design analysis (`improved_gates_plan.md`, worktree branch `improved-gates`, commits `20d286f` and `16ea49a`); no literature source is asserted for any claim above.

## Wiki pages used

- [[wiki/answers/adding-config-optimiser-to-ffrefine]]
- [[wiki/answers/ffrefine-loss-gate-diagnostic-policy]]
- [[wiki/tensions/TEN-0020-config-family-exclusion-versus-untreated-drift]]
- [[wiki/questions/QST-0007-checkpoint-assessment-versus-next-direction-readiness]]

## Wiki updates made

- Added this answer note.
- Added [[wiki/claims/CLM-0048-family-weight-renormalisation-changes-natural-gradient-step-length]].
- Updated [[wiki/answers/adding-config-optimiser-to-ffrefine]] with the family-weight-renormalisation step-length finding.
- Updated [[wiki/tensions/TEN-0020-config-family-exclusion-versus-untreated-drift]] with the observed excluded-family cycling evidence and the project's decision not to guard against it.
- Updated [[wiki/questions/QST-0007-checkpoint-assessment-versus-next-direction-readiness]] with a pointer to the planned cross-fitted aggregation-promise test as a candidate replacement for the chronological half-archive stability check.
- Updated [[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]]'s implementation snapshot with a pointer to this note.

## Remaining gaps

- All findings are evidenced by one water run (`20260924-204914`, 22 epochs) and its accompanying unit tests; no campaign compares the legacy half-archive gate against the planned cross-fitted aggregation-promise test under matched conditions.
- The cross-fitted survival ratio $\rho$ and the aggregation-promise test are design proposals, not yet implemented or validated against fresh resimulation.
- Whether to keep renormalising the optimiser's *step* (as opposed to only its reported loss) after family exclusion remains an open, undecided design question tied to the general step-length policy.
- Whether a weighted-sum run cycles excluded families less often than a ConFIG run, as the project's own reasoning predicts, has not yet been measured; it is proposed as a comparison metric between the two aggregation methods.
