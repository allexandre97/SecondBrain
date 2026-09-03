---
type: claim
status: active
created: 2026-09-03
updated: 2026-09-03
claim_status: supported
claim_scope: local
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/molecular-simulation/free-energy
  - research/statistics/monte-carlo
  - research/scientific-computing
tags:
  - claim
  - ffrefine
  - dielectric-constant
  - prospective-validation
  - fresh-resimulation
  - conditional-fisher
  - fisher-damping
  - reaction-field
related:
  - "[[wiki/answers/ffrefine-prospective-dielectric-damped-fisher-training]]"
  - "[[wiki/answers/ffrefine-average-observable-trainability-validation]]"
  - "[[wiki/claims/CLM-0038-fixed-archive-gradient-validation-does-not-establish-fresh-archive-trainability]]"
  - "[[wiki/claims/CLM-0039-trust-region-kl-must-match-replay-conditioning]]"
  - "[[wiki/questions/QST-0006-average-observable-trainability-sampling-budget]]"
  - "[[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]"
sources:
  - SRC-0018
  - SRC-0023
sensitivity: public
encryption: none
project_evidence:
  - "FFRefine dielectric-only damped-Fisher reaction-field water-temperature run 20260901-171027, completed 2026-09-02"
  - "FFRefine higher-KL dielectric-only damped-Fisher reaction-field water-temperature run 20260902-115818, intentionally stopped during epoch 8 on 2026-09-03 after six paired-confirmed fresh updates"
---

# Damped Conditional-Fisher Dielectric Training Survives Fresh Resimulation

## Claim

In the tested FFRefine reaction-field water setup, a frozen continuously damped state-conditional Fisher treatment with $\gamma=0.1$ can generate repeated full-parameter dielectric-loss improvements that survive fresh resimulation, rather than only reducing loss on the archive that generated each proposal. [SRC-0018] [SRC-0023]

## Scope

This is a local project-evidence claim. It applies to dielectric-only training of the current rigid-water QEq-plus-bounded parameterization on the 14 through 41 degrees Celsius TSS ladder with 20 ns adaptive sampling, 4 ns parity sampling, 60 ns one-replica frozen production, reaction-field/cutoff electrostatics, state-conditional Fisher geometry, and maximum state-normalized empirical KL control.

It is not a claim that $\gamma=0.1$ is universally optimal, that 60 ns is a universal gradient-convergence budget, or that the resulting parameters improve a transferable water model.

## Evidence

The first prospective run `20260901-171027` produced two consecutive updates whose candidate-minus-parent paired intervals on the next fresh archives were entirely below zero. Two independent final-validation simulations reproduced the best confirmed checkpoint's loss.

The higher-KL run `20260902-115818` then supplied a longer prospective sequence:

- checkpoints 1 through 6 all beat their parents on the next newly simulated archive;
- paired candidate-minus-parent loss changes were -0.5770, -0.6923, -0.7102, -0.7225, -0.7635, and -0.3981;
- all six recorded 95% intervals lay below zero;
- fresh dielectric loss decreased from 7.3431 at checkpoint 0 to 3.6057 at checkpoint 6, a 50.90% reduction;
- dielectric RMSE decreased from 43.36 to 30.38, a 29.93% reduction;
- predictions moved toward experiment at all six target temperatures;
- replay-predicted reductions for checkpoints 1 through 6 were 9.31%, 9.87%, 12.25%, 12.56%, 18.19%, and 15.36%, while paired fresh reductions were 9.06%, 10.97%, 11.33%, 13.91%, 15.82%, and 9.94%.

The agreement in sign and approximate magnitude between replay and paired fresh effects is the critical evidence. Frozen-archive descent alone would not establish the claim. [SRC-0018] [[wiki/claims/CLM-0038-fixed-archive-gradient-validation-does-not-establish-fresh-archive-trainability]]

All 21 accepted microproposals passed the configured replay-support gates. Minimum target-state ESS was 1182.7, minimum target-state ESS retention was 0.5098 against a 0.5 threshold, minimum candidate ESS was 8670.0, and minimum candidate retention was 0.7587. The selected damped direction passed its chronological-half gate in all seven completed optimization epochs, with Fisher-metric cosine 0.8112--0.9789 and norm ratio 0.9903--1.0035.

The raw-gradient reporter failed in three of seven completed optimization epochs. The hard-cut Fisher reporter failed in epoch 7 with cosine 0.5999 while the damped direction passed with cosine 0.9355. This shows that the selected treatment avoided vetoes that would have stopped successful or still-supported updates in this realization; it does not establish a matched-arm advantage in objective reduction.

## Trust-region behavior

The higher-KL run used maximum conditional-KL target 0.02 per proposal and maximum empirical archive-to-candidate KL 0.2. Each completed epoch accepted three microproposals. The accepted archive displacement reached empirical KL 0.1202--0.1755, while a fourth proposal remained at 0.2142--0.2515 after the configured line-search trials and was rejected.

The sum of local quadratic step estimates was only 0.0432--0.0585. The larger empirical archive displacement is expected for repeatedly aligned moves because KL of the total displacement is not additive. The explicit state-normalized empirical archive audit, rather than the sum of local budgets, enforced the actual cumulative ceiling. [[wiki/claims/CLM-0039-trust-region-kl-must-match-replay-conditioning]]

## Remaining limitations

- The fresh loss at checkpoint 6 remains 3.6057, equivalent to normalized RMSE 1.899; the experimental curve is not fitted.
- The predicted 15-to-40 degrees Celsius decrease remains 20.25 dielectric units, versus 8.80 experimentally. Training primarily lowered the curve and only modestly corrected its slope.
- Checkpoint 7 has an archive-local predicted reduction of 11.03% but no completed fresh comparison because the operator stopped the live run during epoch 8 after deciding the trainability evidence was sufficient.
- The higher-KL campaign did not reach its configured two final-validation replicas.
- The campaign used one production replica per macro epoch and one campaign seed.
- Density, RDF, enthalpy, phase behavior, dynamical properties, and transferability were not evaluated as acceptance targets.
- The full direction moved QEq charges and bounded nonbonded parameters jointly, so the run does not identify a single causal parameter.

## Links

- [[wiki/answers/ffrefine-prospective-dielectric-damped-fisher-training]]
- [[wiki/answers/ffrefine-average-observable-trainability-validation]]
- [[wiki/claims/CLM-0038-fixed-archive-gradient-validation-does-not-establish-fresh-archive-trainability]]
- [[wiki/claims/CLM-0039-trust-region-kl-must-match-replay-conditioning]]
- [[wiki/questions/QST-0006-average-observable-trainability-sampling-budget]]
- [[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]
- [[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]
- [[wiki/sources/SRC-0023-statistically-optimal-analysis-multiple-equilibrium-states-mbar]]
