---
type: answer
status: active
created: 2026-09-02
updated: 2026-09-02
question: "What did FFRefine's first prospective dielectric-only damped-Fisher water-temperature macro-optimization establish?"
answer_status: partially-answered
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/molecular-simulation/free-energy
  - research/statistics/monte-carlo
  - research/scientific-computing
tags:
  - ffrefine
  - water-temperature
  - dielectric-constant
  - reaction-field
  - prospective-validation
  - macro-optimization
  - fisher-damping
  - conditional-kl
  - fresh-simulation
  - gradient-convergence
related:
  - "[[wiki/answers/ffrefine-average-observable-trainability-validation]]"
  - "[[wiki/answers/ffrefine-retrospective-fisher-treatment-development]]"
  - "[[wiki/answers/ffrefine-fisher-treatment-operators]]"
  - "[[wiki/answers/ffrefine-kl-definition-for-extended-ensemble-training]]"
  - "[[wiki/answers/ffrefine-kl-divergence-definition-change]]"
  - "[[wiki/answers/ffrefine-long-archive-target-gradient-convergence]]"
  - "[[wiki/claims/CLM-0038-fixed-archive-gradient-validation-does-not-establish-fresh-archive-trainability]]"
  - "[[wiki/claims/CLM-0039-trust-region-kl-must-match-replay-conditioning]]"
  - "[[wiki/questions/QST-0006-average-observable-trainability-sampling-budget]]"
  - "[[wiki/questions/QST-0007-checkpoint-assessment-versus-next-direction-readiness]]"
  - "[[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]"
sources:
  - SRC-0018
  - SRC-0023
sensitivity: public
encryption: none
wiki_pages_used:
  - "[[wiki/index]]"
  - "[[wiki/answers/ffrefine-average-observable-trainability-validation]]"
  - "[[wiki/answers/ffrefine-retrospective-fisher-treatment-development]]"
  - "[[wiki/answers/ffrefine-fisher-treatment-operators]]"
  - "[[wiki/answers/ffrefine-kl-definition-for-extended-ensemble-training]]"
  - "[[wiki/answers/ffrefine-kl-divergence-definition-change]]"
  - "[[wiki/answers/ffrefine-long-archive-target-gradient-convergence]]"
  - "[[wiki/claims/CLM-0038-fixed-archive-gradient-validation-does-not-establish-fresh-archive-trainability]]"
  - "[[wiki/questions/QST-0006-average-observable-trainability-sampling-budget]]"
  - "[[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]"
raw_sources_consulted: []
wiki_pages_updated:
  - "[[wiki/answers/ffrefine-average-observable-trainability-validation]]"
  - "[[wiki/answers/ffrefine-retrospective-fisher-treatment-development]]"
  - "[[wiki/answers/ffrefine-long-archive-target-gradient-convergence]]"
  - "[[wiki/answers/ffrefine-fisher-treatment-operators]]"
  - "[[wiki/answers/ffrefine-kl-definition-for-extended-ensemble-training]]"
  - "[[wiki/answers/ffrefine-kl-divergence-definition-change]]"
  - "[[wiki/claims/CLM-0038-fixed-archive-gradient-validation-does-not-establish-fresh-archive-trainability]]"
  - "[[wiki/questions/QST-0006-average-observable-trainability-sampling-budget]]"
  - "[[wiki/questions/QST-0007-checkpoint-assessment-versus-next-direction-readiness]]"
  - "[[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]"
  - "[[wiki/index]]"
  - "[[wiki/log]]"
project_evidence:
  - "FFRefine state-conditional Fisher-treatment screen completed 2026-08-30, protocol fingerprint 533305656758db33454d19af400e39972e1ae94ad2c52ff60c5b0b788d8373f8"
  - "FFRefine state-conditional Fisher-treatment replay completed 2026-08-31, replay hash 01de5d364e231b464706dd0a78cf1d8ff236fa7c38c110c3a7ccfcc3d77f7c84"
  - "FFRefine dielectric-only damped-Fisher reaction-field water-temperature run 20260901-171027, completed 2026-09-02"
---

# Prospective Dielectric Training with a Damped Conditional Fisher

## Short answer

The run provides the first direct prospective evidence that FFRefine can improve the experimental water dielectric-temperature objective across fresh macro epochs. With reaction-field electrostatics, the complete 28-state temperature ladder, the corrected state-conditional KL, and continuous Fisher damping at $\gamma=0.1$, two consecutive parameter updates produced statistically resolved paired loss decreases on newly simulated archives. Two independent final-validation replicas then reproduced the best confirmed loss.

This is materially stronger than the earlier fixed-archive and cross-replay results. Those earlier results showed that supported dielectric descent directions existed on reused archives; this run showed that two such updates survived full resimulation. [SRC-0018] [[wiki/claims/CLM-0038-fixed-archive-gradient-validation-does-not-establish-fresh-archive-trainability]]

The result is nevertheless local and incomplete. A third proposed checkpoint entered a fresh fourth macro epoch, but the new archive's two chronological halves produced damped directions with Fisher-metric cosine 0.657, below the predeclared 0.8 threshold. Optimization stopped. The dielectric values themselves passed their split diagnostic. Thus damping made dielectric trainable for multiple updates without making gradient convergence automatic at every parameter state.

## Why this was a prospective test

The preceding development sequence had four distinct levels:

1. synthetic and finite-difference checks established fixed-archive value and gradient correctness;
2. two independent 100 ns archives established long-budget cumulative direction agreement;
3. a state-conditional retrospective treatment campaign compared hard cutting, diagonal scaling, identity, damping, and modal-SNR steps at matched conditional-KL geometry;
4. this run froze one treatment and generated new trajectories after every accepted parameter update.

Only the fourth level can test whether an archive-derived update improves the objective after resimulation. Frozen-reference replay is a proposal mechanism, not a substitute for fresh validation. [SRC-0018] MBAR improves use of represented configurations but does not create independent information or phase-space support. [SRC-0023]

The corrected retrospective campaign did not identify $\gamma=0.1$ as the largest fixed-archive loss reducer. The hard full-Fisher treatment ranked first by its predeclared replay score. Damping at $\gamma=0.1$ was nevertheless eligible, had a stronger 60--100 ns direction-robustness score than hard cutting (0.9853 versus 0.9599), preserved full parameter correlations, avoided a discontinuous eigenvalue cutoff, and required no block-jackknife modal-SNR machinery. It was selected prospectively as a simpler smooth full-Fisher treatment, not as a claim of retrospective numerical optimality.

## Frozen experiment configuration

The run used:

- dielectric as the only optimized target family;
- six experimental targets at 15, 20, 25, 30, 35, and 40 degrees Celsius;
- the unchanged TSS ladder of every integer temperature from 14 through 41 degrees Celsius;
- reaction-field/cutoff electrostatics with solvent dielectric 78.3;
- rigid water;
- one production replica per macro epoch;
- 20 ns adaptive sampling, 4 ns replay/TSS parity sampling, and 60 ns frozen production;
- no production extension after a failed direction gate;
- ten possible optimization epochs followed by two final-validation replicas;
- the complete QEq-plus-bounded nonbonded parameter direction;
- weighted-sum target aggregation and no momentum;
- continuously damped conditional-Fisher treatment with $\gamma=0.1$;
- the hard-truncated Fisher and raw objective gradient as reporters only;
- maximum conditional-KL target 0.005 per proposal, maximum archive displacement KL 0.1, and at most 21 proposals.

The target loss was the mean squared tolerance-normalized dielectric residual,

$$
L(\theta)
=
\frac{1}{6}
\sum_{j=1}^{6}
\left(
\frac{\varepsilon_j(\theta)-\varepsilon_j^{\mathrm{exp}}}{16}
\right)^2.
$$

The tolerance 16 sets the loss scale. It is not the estimator uncertainty and does not by itself make a gradient statistically resolvable.

## Treated-direction gate

For each production archive, the two chronological halves produced target gradients $g_1$ and $g_2$. Both were transformed with the same full-archive damped conditional-Fisher operator,

$$
d_i^{(0)}=-A_{\gamma=0.1}g_i,
$$

and capped by the same maximum state-conditional KL policy. The comparison used the full-archive conditional Fisher $F$:

$$
c_F(d_1,d_2)
=
\frac{d_1^\mathsf{T}Fd_2}
{\sqrt{d_1^\mathsf{T}Fd_1}\sqrt{d_2^\mathsf{T}Fd_2}},
$$

$$
r_F(d_1,d_2)
=
\frac{\sqrt{d_2^\mathsf{T}Fd_2}}
{\sqrt{d_1^\mathsf{T}Fd_1}}.
$$

The selected direction was optimization-ready only when $c_F\geq0.8$ and $0.5\leq r_F\leq2$. The raw-gradient and hard-cut rows used the same thresholds for reporting but could not veto optimization.

This gate tests whether the two halves imply similar finite parameter displacements under the selected geometry. It is more relevant than a raw-gradient gate when the production optimizer does not follow the raw Euclidean direction. It remains conservative: two nonparallel directions can still lie in a shared descent cone, so failure is not mathematical proof that no useful step exists.

## Macro-epoch chronology

| Macro epoch | Simulated checkpoint | Fresh evaluation | Direction gate | Result |
| --- | ---: | --- | --- | --- |
| 1 | 0, initial force field | baseline loss 7.2354 | damped pass | four replay proposals accepted; checkpoint 1 written |
| 2 | 1 | checkpoint 1 beat checkpoint 0 on the same fresh archive | damped pass | four replay proposals accepted; checkpoint 2 written |
| 3 | 2 | checkpoint 2 beat checkpoint 1 on the same fresh archive | damped pass | four replay proposals accepted; checkpoint 3 written |
| 4 | 3 | direct point loss 5.6950, but paired parent comparison was not executed | damped fail | no further optimization; campaign stopped |
| 5 | 2 | final validation replica 1, loss 5.9654 | damped pass | validation only |
| 6 | 2 | final validation replica 2, loss 5.9312 | damped pass | validation only |

Checkpoint numbers label parameter states. A proposal made at the end of epoch $e$ is first tested on genuinely fresh configurations in epoch $e+1$.

## Fresh paired evidence

The first two updates were evaluated against their parent parameters using the same newly generated archive. This paired design separates the parameter effect from much of the archive-to-archive noise.

| Evaluated checkpoint | Candidate loss | Parent loss replayed on the fresh archive | Candidate minus parent | Standard error | Recorded interval | Status |
| ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | 6.7783 | 7.3951 | -0.6168 | 0.0735 | [-0.7831, -0.4505] | accepted |
| 2 | 5.9600 | 6.4867 | -0.5267 | 0.0699 | [-0.6849, -0.3685] | accepted |

Both intervals lie below zero. The recorded relative paired improvements were 8.34% and 8.12%. These are two consecutive fresh-ensemble confirmations, not two measurements on the optimization archive.

The final-validation replicas independently reproduced checkpoint 2:

| Validation replica | Loss |
| ---: | ---: |
| 1 | 5.9654 |
| 2 | 5.9312 |
| Mean | 5.9483 |

The original fresh estimate for checkpoint 2 was 5.9600. The agreement of all three values supports the stability of the direct dielectric objective at this checkpoint.

Relative to the initial archive loss 7.2354, the validation mean is 17.79% lower. Because the physical dielectric root-mean-square error is $16\sqrt{L}$, its corresponding value decreased from 43.04 to 39.02, a 9.33% reduction.

## Dielectric-temperature curve movement

The mean of the two final-validation curves moved toward experiment at every target temperature:

| Temperature | Initial prediction | Final-validation mean | Change | Experimental value |
| ---: | ---: | ---: | ---: | ---: |
| 15 degrees Celsius | 129.69 | 129.16 | -0.53 | 81.946 |
| 20 degrees Celsius | 126.22 | 123.68 | -2.53 | 80.103 |
| 25 degrees Celsius | 122.71 | 118.33 | -4.38 | 78.304 |
| 30 degrees Celsius | 118.99 | 112.96 | -6.03 | 76.546 |
| 35 degrees Celsius | 113.82 | 108.27 | -5.56 | 74.828 |
| 40 degrees Celsius | 110.74 | 104.04 | -6.70 | 73.151 |

All residuals remain positive and substantially larger than zero. The result establishes improvement, not convergence to the experimental curve.

## Damped, hard-cut, and raw reproducibility

| Epoch | Damped cosine / norm ratio | Damped | Hard-cut reporter | Raw-gradient reporter |
| ---: | ---: | --- | --- | --- |
| 1 | 0.984 / 1.003 | pass | pass | fail |
| 2 | 0.881 / 0.990 | pass | pass | fail |
| 3 | 0.918 / 0.992 | pass | fail | pass |
| 4 | 0.657 / 0.982 | fail | fail | fail |
| 5, validation | 0.966 / 1.000 | pass | fail | pass |
| 6, validation | 0.812 / 1.002 | pass | pass | fail |

Across all six archives, the selected damped treatment passed five times, hard cutting three times, and the raw-gradient reporter twice. More importantly, the raw-gradient rule would have vetoed the run at epoch 1, before either independently confirmed improvement. The selected-direction gate therefore corrected a real false-negative failure mode.

Epoch 4 shows the other side of the result. The direct dielectric family split passed with score 0.161 against threshold 1, while the damped direction failed only its angular criterion. The hard-cut cosine was 0.671 and the raw-gradient cosine was -0.620 with norm ratio 5.92. Damping did not manufacture agreement when all representations indicated substantial sensitivity uncertainty.

## Conditional-KL behavior

The production trust region controlled the maximum state-conditional divergence,

$$
D_{\max}(\theta'\Vert\theta)
=
\max_T
D_{\mathrm{KL}}
\left(
p_{\theta'}(x\mid T)
\Vert
p_\theta(x\mid T)
\right),
$$

while the design-weighted conditional Fisher supplied the direction geometry. This matches the conditioning of state-normalized replay. [[wiki/claims/CLM-0039-trust-region-kl-must-match-replay-conditioning]]

Each accepted microproposal used empirical maximum conditional KL between approximately 0.00480 and 0.00500. Four proposals were accepted in each of the first three macro epochs. Their total displacement from the archive-generating parameters reached empirical archive KL values of 0.07699, 0.07851, and 0.07992.

The fifth proposal in each chain was rejected because it would have increased the empirical archive KL to 0.11109, 0.11216, or 0.11315, above the 0.1 ceiling. The sums of individual step KLs were only about 0.019--0.020 because KL of the total aligned displacement is not additive. The nonlinear archive-to-candidate measurement, rather than a sum of local budgets, correctly controlled the cumulative move.

All recorded proposal-support checks passed. The stopping mechanism was therefore not loss increase, MBAR support collapse, or accidental exhaustion of the proposal counter.

## Parameter movement in the best confirmed checkpoint

Checkpoint 2 was the best checkpoint with a completed paired fresh comparison. Its changes relative to the initial model were:

| Parameter | Initial | Checkpoint 2 | Relative change |
| --- | ---: | ---: | ---: |
| Oxygen charge | -0.905200 | -0.899780 | -0.599% in magnitude |
| Hydrogen charge | 0.452600 | 0.449890 | -0.599% |
| Hydrogen sigma | 0.201900 | 0.201357 | -0.269% |
| Hydrogen epsilon | 0.021000 | 0.020497 | -2.395% |
| Oxygen sigma | 0.333200 | 0.333249 | +0.015% |
| Oxygen epsilon | 0.855200 | 0.852584 | -0.306% |
| DEXP alpha | 12.159600 | 12.152049 | -0.062% |
| DEXP beta | 4.326300 | 4.325807 | -0.011% |

The parameters moved jointly. These magnitudes do not isolate a causal contribution from any one parameter. They do confirm that the prospective test used the complete direction, including the QEq charge coordinates, rather than a coordinate-wise perturbation scan.

The run metadata's `active_parameters` field listed only the bounded nonbonded parameters, whereas the parameter snapshots correctly marked the QEq charge coordinates as trainable. This is a provenance-reporting omission, not evidence that charges were excluded from optimization.

## Why optimization stopped

Epoch 4 had sufficient replay support, effective sample size, Fisher validity, and direct-observable split agreement. Its selected damped half-directions nevertheless had cosine 0.657. With no configured production extension, the campaign stopped instead of attempting another proposal.

The scientifically supported interpretation is:

- the dielectric estimator and direct objective were stable enough to evaluate at this checkpoint;
- the next parameter-sensitivity direction was not reproducible enough under the selected conservative gate;
- 60 ns from one replica was sufficient for several archives but was not a universal per-epoch guarantee;
- the run failed to continue, not because the previously accepted updates increased fresh loss, but because the next update could not be certified.

This directly preserves the distinction established by the long-archive campaign: convergence of a mean observable, its raw gradient, and its Fisher-treated direction are separate questions.

## Checkpoint assessment and next-direction readiness are currently conflated

Checkpoint 3 was generated by the accepted epoch-3 replay chain and then simulated freshly in epoch 4. Its direct point loss was 5.6950, lower than checkpoint 2's 5.9600. That cross-archive point comparison is not sufficient to declare improvement because it uses different realizations.

The appropriate paired comparison would replay checkpoint 2 on the epoch-4 archive and compare it with checkpoint 3 on exactly those configurations. The required parent parameters were available. The pipeline did not perform this comparison because `sampling_accepted` currently includes the next-direction gate; when the direction failed, fresh loss and the parent comparison were skipped. Checkpoint 3 was therefore neither accepted nor rejected on paired evidence. It was unassessed, and final validation reverted to checkpoint 2.

This reveals two logically separate statuses:

1. **checkpoint evaluation accepted:** replay, ESS, direct-target split, and paired parent comparison support a trustworthy statement about the current parameters;
2. **optimization ready:** the selected treated direction is sufficiently reproducible to propose another update.

The second should gate construction of the next proposal. It should not erase the first or prevent an already simulated candidate from becoming the best checkpoint. Final-validation replicas should likewise be judged primarily as objective evaluations, with direction diagnostics retained as reporters unless another update will follow. This design question is tracked in [[wiki/questions/QST-0007-checkpoint-assessment-versus-next-direction-readiness]].

## What this establishes

- The corrected conditional-KL backend can control multi-proposal dielectric optimization without the earlier mixed-versus-conditional KL mismatch.
- Damping at $\gamma=0.1$ generated reproducible treated directions in three consecutive optimization archives.
- Two consecutive full-parameter updates reduced dielectric loss on newly simulated archives with paired intervals entirely below zero.
- The best confirmed checkpoint reproduced across two independent final-validation simulations.
- The final-validation dielectric curve moved toward experiment at every target temperature.
- A raw-gradient gate would have incorrectly stopped this successful sequence at the first epoch.
- Damping improved practical direction reproducibility relative to both reporters in this realization, but did not force an unstable epoch to pass.
- Direct dielectric convergence can still precede convergence of its parameter-sensitivity direction.

## What this does not establish

- that dielectric optimization has converged;
- that $\gamma=0.1$ is optimal or universally preferable to hard cutting;
- that $\gamma=0.1$ would outperform hard cutting under a matched prospective arm comparison;
- that every 60 ns one-replica archive is sufficient;
- that checkpoint 3 improved or worsened the population objective;
- that the 0.8 direction-cosine threshold is necessary for descent;
- that more replicas, longer archives, or production extension would repair epoch 4;
- that the result transfers to PME, a different water model, a different parameter basis, or another campaign seed;
- that enthalpy is trainable under the same treatment;
- that the observed parameter changes preserve density, RDF, enthalpy, or other collateral properties.

## Required next evidence

Before interpreting another expensive run, the pipeline should separate checkpoint evaluation from next-direction readiness and repair the active-parameter metadata. The next prospective dielectric campaign should then:

1. retain the same conditional-KL definition, complete ladder, target family, latent map, and frozen $\gamma=0.1$ treatment;
2. compute and persist fresh paired parent comparison whenever base observable/replay validity passes, even if the next direction fails;
3. permit a valid improved checkpoint to become the best checkpoint independently of whether another proposal can be made;
4. report the direction during final validation without allowing it to invalidate an otherwise valid objective estimate;
5. predeclare whether a failed treated direction triggers longer production, an independent replica/archive, or termination;
6. repeat with a new campaign seed before estimating a success probability or universal archive length;
7. add collateral density and RDF reporting before interpreting the final parameters as an improved water model.

## Sources used

- SRC-0018 for frozen-reference replay, Fisher/KL trust regions, support checks, and the requirement that archive-derived updates survive fresh simulation.
- SRC-0023 for state-normalized multistate replay and its overlap/information limitations.

No raw sources were consulted. All numerical values are FFRefine project evidence from the recorded conditional treatment campaign and prospective run.

## Wiki pages used

- [[wiki/answers/ffrefine-average-observable-trainability-validation]]
- [[wiki/answers/ffrefine-retrospective-fisher-treatment-development]]
- [[wiki/answers/ffrefine-fisher-treatment-operators]]
- [[wiki/answers/ffrefine-kl-definition-for-extended-ensemble-training]]
- [[wiki/answers/ffrefine-kl-divergence-definition-change]]
- [[wiki/answers/ffrefine-long-archive-target-gradient-convergence]]
- [[wiki/claims/CLM-0038-fixed-archive-gradient-validation-does-not-establish-fresh-archive-trainability]]
- [[wiki/claims/CLM-0039-trust-region-kl-must-match-replay-conditioning]]
- [[wiki/questions/QST-0006-average-observable-trainability-sampling-budget]]
- [[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]

## Wiki updates made

- Added this prospective result as a dedicated answer note.
- Updated the trainability, long-archive, Fisher-treatment, and KL answers so they no longer say that no conditional-Fisher dielectric proposal has survived fresh simulation.
- Updated the fixed-versus-fresh claim, sampling-budget question, and signal-versus-support tension.
- Added a focused question separating checkpoint assessment from next-direction readiness.
- Updated the wiki index and log.

## Remaining gaps

- The campaign supplies one prospective realization and two confirmed parameter updates, not a campaign-level success rate.
- Checkpoint 3 lacks the paired parent comparison needed for acceptance or rejection.
- The minimum independent information required to recover after a failed treated direction remains unknown.
- No matched prospective hard-cut versus damped comparison has been run.
- No full experimental enthalpy optimization has passed fresh validation.
