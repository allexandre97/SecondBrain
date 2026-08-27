---
type: answer
status: active
created: 2026-08-07
updated: 2026-08-20
question: "Why can FFRefine water-temperature replay optimization show monotone intra-epoch loss but upward loss jumps between macro epochs?"
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
  - water-temperature
  - replay-reweighting
  - mbar
  - validation
  - force-field-optimization
related:
  - "[[wiki/answers/ffrefine-average-observable-trainability-validation]]"
  - "[[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]]"
  - "[[wiki/answers/ffrefine-current-implementation-status]]"
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
  - "[[wiki/concepts/free-energy-reweighting-for-force-field-fine-tuning]]"
  - "[[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]"
  - "[[wiki/claims/CLM-0009-observable-fitting-needs-held-out-validation]]"
  - "[[wiki/questions/force-field-training-validation-scope]]"
  - "[[wiki/claims/CLM-0038-fixed-archive-gradient-validation-does-not-establish-fresh-archive-trainability]]"
  - "[[wiki/questions/QST-0006-average-observable-trainability-sampling-budget]]"
  - "[[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]"
  - "[[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]"
  - "[[wiki/sources/SRC-0023-statistically-optimal-analysis-multiple-equilibrium-states-mbar]]"
sources:
  - SRC-0016
  - SRC-0018
  - SRC-0019
  - SRC-0020
  - SRC-0023
sensitivity: public
encryption: none
wiki_pages_used:
  - "[[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]]"
  - "[[wiki/answers/ffrefine-current-implementation-status]]"
  - "[[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]"
  - "[[wiki/claims/CLM-0009-observable-fitting-needs-held-out-validation]]"
  - "[[wiki/questions/force-field-training-validation-scope]]"
raw_sources_consulted: []
project_evidence:
  - "FFRefine water_temperature.jl audit on 2026-08-07"
  - "FFRefine artifact audit: /ssd/outputs/water-temperature/20260806-210949"
  - "FFRefine fixed-archive and fresh-archive water average-observable validation through 2026-08-20"
---

# FFRefine Water-Temperature Replay Fresh Loss Gap

## Short answer

The upward jumps between water-temperature macro epochs are not failures of the intra-epoch line search. They compare two different estimators. Inside a macro epoch, FFRefine optimizes parameters by replaying candidate force fields on one fixed production archive. At the next macro epoch, the same accepted parameters are evaluated on a newly generated simulation archive. The replay chain enforces non-increasing loss on the old archive, but it does not and cannot guarantee non-increasing fresh loss on the next independently generated archive. This is the validation boundary recorded in SRC-0018: replay-based accepted updates must survive resimulation before they count as robust force-field improvement. [SRC-0018]

For the 2026-08-06 water-temperature run, the artifact evidence supports this interpretation. The active objective was density-only over 28 temperatures with a tolerance-normalized MSE. Within each completed macro epoch, accepted replay proposals were monotone because acceptance required the proposed replay loss not to exceed the current replay loss. Across macro epochs, the plotted boundary connects the final replay loss from archive $D_e$ to the initial fresh loss from a new archive $D_{e+1}$ at essentially the same checkpoint parameters. That is a replay-to-fresh validation comparison, not one continuous optimization trajectory.

## Evidence from the run

The audited run used `water_temperature.jl` in a density-only configuration: 28 density targets from 14 to 41 degrees Celsius, tolerance 0.001 kg/L, MSE objective, no active regularization, and MBAR/TSS replay with a per-epoch cumulative KL budget of 0.005. Reconstructing the loss from the target CSVs matched the logged objective, confirming that the sawtooth was not a plotting formula mismatch.

At each completed boundary, the final replay loss was lower than the next fresh loss:

| Boundary | Final replay loss | Next fresh loss | Gap |
| --- | ---: | ---: | ---: |
| 1 to 2 | 210.944 | 250.360 | 39.416 |
| 2 to 3 | 183.769 | 212.949 | 29.180 |
| 3 to 4 | 155.147 | 185.262 | 30.115 |
| 4 to 5 | 130.363 | 157.134 | 26.770 |
| 5 to 6 | 106.579 | 134.910 | 28.332 |
| 6 to 7 | 89.704 | 124.218 | 34.514 |
| 7 to 8 | 81.696 | 100.690 | 18.994 |
| 8 to 9 | 65.356 | 86.598 | 21.242 |
| 9 to 10 | 54.555 | 73.164 | 18.609 |
| 10 to 11 | 48.115 | 60.294 | 12.180 |

The epoch 11 number is provisional because the run was interrupted during that macro epoch, but its fresh initial loss had already been evaluated.

Parameter continuity was checked across boundaries. The saved checkpoint parameters matched the final accepted replay parameters, and the next initial parameters differed only by floating-point reinsertion at about 1e-8 relative scale. Therefore the boundary jumps are not explained by rollback, checkpoint mismatch, or a changed physical parameter set.

The fresh-loss sequence itself still decreased across macro epochs:

$$
282.39, 250.36, 212.95, 185.26, 157.13, 134.91, 124.22, 100.69, 86.60, 73.16, 60.29.
$$

So the replay optimizer was making real progress, but the replay archive overestimated the size of the immediately accepted improvement.

## Mechanism

The optimizer loop reuses the same fixed archive for gradient estimation, Fisher/KL geometry, candidate replay evaluation, and line-search selection. With `max_loss_increase = 0`, the candidate acceptance rule mechanically enforces monotone replay loss on that archive. The next macro epoch then constructs a new water system, equilibrates, runs fresh adaptive/parity/production stages, and evaluates the accepted checkpoint on a new sample set. That new sample set breaks the adaptive correlation between the chosen candidate and the archive used to choose it.

This creates an in-sample replay gap. The final proposal in a macro epoch is selected because it looks best, subject to support gates, on $D_e$. The next macro epoch estimates the same density curve on $D_{e+1}$. Even when ESS, retention, and parity gates pass, those diagnostics mainly rule out severe weight collapse or obvious replay/TSS inconsistency among sampled configurations. They do not prove that all important configurations were sampled, nor do they make the selected replay loss an unbiased predictor of fresh resimulation loss. [SRC-0016] [SRC-0018] [SRC-0019] [SRC-0020]

For this density run, the boundary residual evidence was directional: fresh density estimates after resimulation were usually higher than the prior final replay estimates. Across boundaries 1 to 10, 275 of 280 temperature-level fresh-minus-replay density shifts were positive, with mean shift about 0.0014 kg/L. Since most residuals were already positive, this upward density shift raised the tolerance-normalized density loss.

## Interpretation

The durable lesson is that replay monotonicity is an in-archive property. It is a useful optimizer diagnostic, but it should not be plotted or interpreted as macro-epoch monotonic validation unless each accepted checkpoint is also evaluated on a held-out archive or independent resimulation. The correct production diagnostic is the replay-to-fresh gap at fixed checkpoint parameters, tracked alongside ESS, parity, split diagnostics, and fresh macro-epoch progress. [SRC-0018] [[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]] [[wiki/claims/CLM-0009-observable-fitting-needs-held-out-validation]]

The 2026-08-06 run did not show a support-collapse failure under the configured thresholds. It showed adaptive reuse of a finite replay archive: monotone in-sample loss, systematic replay optimism, and continued but smaller fresh resimulation improvement. Disentangling finite-sample MBAR variance, adaptive selection bias, serial correlation, and residual equilibration effects would require held-out replay blocks or fixed-checkpoint replicate resimulations.

## Later average-observable validation

The August 2026 enthalpy and PME dielectric checks isolate a second, earlier failure mode. Fixed-archive finite-difference gradients, loss gradients, and one-parameter synthetic recovery passed for both properties, but fresh 10 ns and 20 ns archives contained no tested direction that simultaneously reached SNR 5, passed replay support, and stayed below empirical KL 0.02. The best valid 20 ns SNRs were 0.1121 for enthalpy and 0.08847 for dielectric. [[wiki/answers/ffrefine-average-observable-trainability-validation]]

This is distinct from the density sawtooth above. The density run had a resolvable direction and made fresh progress, but replay overestimated the improvement selected on each old archive. The average-observable prescreens did not reach macro optimization: their supported local response was already smaller than archive uncertainty. A mathematically correct replay gradient can therefore fail to give stable fresh progress either because candidate selection overfits a finite archive or because the archive does not resolve the local observable response in the first place. [[wiki/claims/CLM-0038-fixed-archive-gradient-validation-does-not-establish-fresh-archive-trainability]]

## Implementation implications

Future FFRefine diagnostics should separate these curves visually: replay proposal loss within a macro epoch, fresh initial loss at the next macro epoch, and held-out or replicate validation loss if available. Line plots should not connect proposal losses across archive boundaries without marking that the estimator changed.

Candidate-level validation should also be considered. A cheap version is to reserve chronological or block-held-out frames from the production archive for candidate scoring after the line search chooses a proposal. A stronger version is to run fixed-checkpoint replicate resimulations for selected accepted checkpoints. Either check would estimate whether replay improvements survive outside the archive that selected them.

## Links

- [[wiki/answers/ffrefine-average-observable-trainability-validation]]
- [[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]]
- [[wiki/answers/ffrefine-current-implementation-status]]
- [[wiki/concepts/awh-replay-force-field-optimization]]
- [[wiki/concepts/free-energy-reweighting-for-force-field-fine-tuning]]
- [[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]
- [[wiki/claims/CLM-0009-observable-fitting-needs-held-out-validation]]
- [[wiki/questions/force-field-training-validation-scope]]
- [[wiki/claims/CLM-0038-fixed-archive-gradient-validation-does-not-establish-fresh-archive-trainability]]
- [[wiki/questions/QST-0006-average-observable-trainability-sampling-budget]]
- [[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]
- [[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]
- [[wiki/sources/SRC-0023-statistically-optimal-analysis-multiple-equilibrium-states-mbar]]
