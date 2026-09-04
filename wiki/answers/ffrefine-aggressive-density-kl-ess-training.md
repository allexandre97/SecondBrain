---
type: answer
status: active
created: 2026-09-04
updated: 2026-09-04
question: "What did FFRefine's aggressive density-only KL and ESS campaign establish?"
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
  - density
  - trust-region
  - empirical-kl
  - effective-sample-size
  - fresh-validation
  - direction-readiness
related:
  - "[[wiki/answers/ffrefine-average-observable-trainability-validation]]"
  - "[[wiki/answers/ffrefine-prospective-dielectric-damped-fisher-training]]"
  - "[[wiki/claims/CLM-0039-trust-region-kl-must-match-replay-conditioning]]"
  - "[[wiki/questions/QST-0007-checkpoint-assessment-versus-next-direction-readiness]]"
  - "[[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]"
  - "[[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]"
sources:
  - SRC-0018
  - SRC-0023
sensitivity: public
encryption: none
wiki_pages_used:
  - "[[wiki/index]]"
  - "[[wiki/answers/ffrefine-average-observable-trainability-validation]]"
  - "[[wiki/answers/ffrefine-prospective-dielectric-damped-fisher-training]]"
  - "[[wiki/claims/CLM-0039-trust-region-kl-must-match-replay-conditioning]]"
  - "[[wiki/questions/QST-0007-checkpoint-assessment-versus-next-direction-readiness]]"
  - "[[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]"
raw_sources_consulted: []
wiki_pages_updated:
  - "[[wiki/answers/ffrefine-average-observable-trainability-validation]]"
  - "[[wiki/claims/CLM-0039-trust-region-kl-must-match-replay-conditioning]]"
  - "[[wiki/questions/QST-0007-checkpoint-assessment-versus-next-direction-readiness]]"
  - "[[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]"
project_evidence:
  - "FFRefine density-only KL 0.1/archive 1.0/ESS 0.45 water-temperature run 20260903-220645, completed 2026-09-03"
  - "FFRefine density-only aggressive conditional-KL/ESS water-temperature run 20260904-102939, completed 2026-09-04"
---

# Aggressive Density-Only KL and ESS Training

## Short answer

Run `20260904-102939` showed that FFRefine can move the water density-temperature curve rapidly under a substantially more aggressive replay policy while retaining support and fresh-simulation confirmation. Two macro-updates reduced the fresh density loss from 143.6331 to 21.5935. Two independent terminal validations at the selected checkpoint gave losses 20.0060 and 20.2560, a mean reduction of about 86.0% from the initial archive.

The result is a positive control, not a universal calibration. It establishes that empirical archive KL above 0.2 is not automatically unsafe for this density target and run realization. It does not establish that the same KL or ESS thresholds are safe for RDF, enthalpy, dielectric, another seed, or a different thermodynamic setup. Replay support and fresh resimulation remain independent requirements. [SRC-0018] [SRC-0023]

## Frozen configuration

The campaign used:

- density as the only target family, with all 28 experimental targets;
- the unchanged 14--41 degrees Celsius TSS ladder;
- reaction-field/cutoff electrostatics with dielectric 78.3;
- 10 ns adaptive sampling and an initial 10 ns production archive;
- at most two 10 ns production extensions;
- one production replica and two final-validation replicas;
- continuously damped state-conditional Fisher geometry with $\gamma=0.1$;
- maximum state-conditional KL target 0.1 per proposal;
- empirical archive-to-candidate KL ceiling 1.0;
- target-state and candidate ESS retention thresholds of 0.25;
- absolute target-state and candidate ESS minima of 100;
- no raw-gradient veto.

For tolerance $\tau_\rho=0.001\ \mathrm{kg\,L^{-1}}$, the density loss is

$$
L_\rho(\theta)
=
\frac{1}{28}
\sum_{j=1}^{28}
\left(
\frac{\rho_j(\theta)-\rho_j^{\mathrm{exp}}}{\tau_\rho}
\right)^2,
$$

so the physical root-mean-square residual is

$$
\operatorname{RMS}_\rho
=
\tau_\rho\sqrt{L_\rho}.
$$

## Macro-epoch chronology

| Epoch | Simulated checkpoint | Fresh assessment | Selected direction | Consequence |
| ---: | ---: | --- | --- | --- |
| 1 | 0 | valid baseline | ready | three replay proposals applied; checkpoint 1 written |
| 2 | 1 | paired accepted | ready | two replay proposals applied; checkpoint 2 written |
| 3 | 2 | paired accepted | sampling-limited | checkpoint 2 retained; no checkpoint 3 update |
| 4 | 2 | final validation accepted | reporter ready | validation only |
| 5 | 2 | final validation accepted | reporter ready | validation only |

Checkpoint 2 was therefore not rejected. Its loss and paired response were accepted, but the archive did not certify the next damped-Fisher direction. This run exercised the intended separation between checkpoint evaluation and readiness for another update. [[wiki/questions/QST-0007-checkpoint-assessment-versus-next-direction-readiness]]

## Fresh paired evidence

Each accepted macro-update was assessed against its parent on the same newly simulated archive:

| Checkpoint | Candidate loss | Parent loss on candidate archive | Candidate minus parent | Standard error | Recorded interval |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 56.0352 | 151.0997 | -95.0645 | 10.3598 | [-118.4985, -71.6306] |
| 2 | 21.5935 | 66.0780 | -44.4844 | 3.4417 | [-52.2696, -36.6993] |

Both intervals are wholly below zero. The corresponding paired relative improvements were 62.92% and 67.32%. Replay descent therefore survived fresh resimulation twice rather than merely fitting the proposal archives. [SRC-0018]

The density RMS residual changed as follows:

| Assessment | Loss | RMS residual, kg/L | Maximum absolute residual, kg/L |
| --- | ---: | ---: | ---: |
| Initial checkpoint | 143.6331 | 0.011985 | 0.019253 |
| Checkpoint 1 | 56.0352 | 0.007486 | 0.013277 |
| Checkpoint 2 | 21.5935 | 0.004647 | 0.008427 |
| Validation 1 | 20.0060 | 0.004473 | 0.007838 |
| Validation 2 | 20.2560 | 0.004501 | 0.007996 |

The two validation losses differ by only 0.250, and their mean is 20.1310. Relative to the initial archive, the validation mean represents about an 86.0% loss reduction and a 62.6% RMS-residual reduction.

The validation-mean absolute residual improved at 24 of 28 temperatures. The exceptions were 14--17 degrees Celsius, where the optimized curve overshot the experimental density. The campaign therefore achieved a large global improvement but had already begun to trade low-temperature accuracy against the remainder of the curve.

## What the KL and support records establish

The accepted proposal chains reached empirical archive-to-candidate maximum state KL values of 0.3006 in epoch 1 and 0.3803 in epoch 2. Both resulting checkpoint updates were then accepted by paired fresh comparisons. This directly rules out treating archive KL 0.2 as a universal safety boundary.

It does not make archive KL irrelevant. The reliable interpretation is:

1. local quadratic KL scales the proposed displacement;
2. exact empirical step and archive KL audit the finite replay perturbation;
3. state-wise ESS and candidate ESS test represented support;
4. paired fresh simulation decides whether replay predicted a transferable improvement.

The first proposal of each epoch used nearly the full empirical step budget, at 0.09865 and 0.09626. Line search automatically reduced later steps when support or loss required it. In epoch 1, accepted step KL values fell to 0.02412 and 0.00597 before the chain stopped.

The final attempted epoch-1 proposal illustrates why absolute and relative ESS constraints should remain separate. Its target-state retention was 0.2726, above the 0.25 threshold, but its minimum target-state ESS was 98.70, below the absolute minimum of 100. The proposal was correctly rejected at the support boundary. MBAR cannot manufacture support absent from the archive. [SRC-0023] [[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]

Epoch 2 supplied another independent veto: a third proposal passed line search and support at scale 0.5, but its loss improvement was statistically inconclusive, so it was not applied.

## Direction-readiness result

At checkpoint 2, the first 10 ns production attempt needed extension for replay/TSS parity. After 20 ns total, the direct checkpoint assessment passed but the selected damped direction had chronological-half cosine 0.188. After 30 ns total, the comparison was:

| Representation | Cosine | Norm ratio | Gate result |
| --- | ---: | ---: | --- |
| Damped conditional-Fisher direction | 0.7280 | 1.0220 | fail |
| Raw gradient reporter | 0.9358 | 0.7928 | pass |
| Hard-cut conditional-Fisher reporter | 0.8056 | 1.0103 | pass |

The failure was therefore treatment-sensitive rather than a generic failure of the raw density gradient at 30 ns. It is consistent with the continuously damped operator retaining weak-curvature modes that the five-mode hard cutoff removes, but this single archive does not prove that mechanism.

The same checkpoint then produced damped cosines 0.9457 and 0.8209 in the two independent 10 ns final-validation archives. Direct density losses remained reproducible while readiness of a further direction varied across archives. Consequently, a single chronological-half direction gate is a conservative stochastic decision rule: failure can justify withholding the next update without invalidating the checkpoint already assessed.

## Relation to the preceding density screen

The preceding density run `20260903-220645` used the same nominal KL target 0.1 and archive ceiling 1.0, but stricter target-state retention 0.45, candidate retention 0.5, a 0.995 KL interior fraction, and only one production extension. Its first checkpoint passed paired fresh validation. Its next proposal chain reached empirical archive KL 0.3030, but checkpoint 2 could not obtain supported paired evaluation on its fresh archive even after the allowed extension. The recorded point losses favored the candidate, 29.7581 versus 92.7883 for the parent, but zero valid uncertainty blocks made the comparison `insufficient_support`, not accepted evidence.

The two runs are not matched arms and do not isolate ESS thresholds or extension count causally. Together they nevertheless demonstrate why archive KL cannot be interpreted as a deterministic overlap percentage or universal safety boundary: one density update at archive KL 0.3030 lacked a valid fresh comparison, while later updates at 0.3006 and 0.3803 passed support and paired fresh validation.

## What is established

- Aggressive density-only replay can produce large, fresh-confirmed progress in two macro-updates.
- Archive KL values of 0.3006 and 0.3803 were compatible with support and fresh improvement in this run.
- A fixed archive-KL value alone is not a sufficient accept/reject rule.
- Absolute and relative ESS thresholds provide complementary protection.
- The separated checkpoint state model preserved and validated checkpoint 2 even though its next damped direction failed.
- Near an improved checkpoint, direction readiness can become treatment- and archive-dependent even while the direct density curve is stable.

## What is not established

- The run does not causally identify which threshold change produced the acceleration because it is not a matched multi-arm comparison.
- One seed does not estimate the probability that KL target 0.1, archive ceiling 1.0, and ESS retention 0.25 will succeed again.
- The result does not justify transferring those values directly to RDF, enthalpy, dielectric, alchemical transformations, or other systems.
- It does not establish that damping or hard truncation is universally preferable near convergence.
- It does not establish a converged water model; four low-temperature points worsened, and collateral observables were not validated.

## Next evidence

The cleanest follow-ups are a new-seed repetition of the same density arm and a matched RDF positive-control arm. These would distinguish a reproducible operating region from a favorable density realization before the aggressive thresholds are used to infer behavior for more difficult targets.

## Sources and provenance

The numerical results come from FFRefine project run `20260904-102939`. The interpretation of frozen-reference replay, support, and fresh resimulation follows SRC-0018; the overlap limitation of state-normalized MBAR replay follows SRC-0023. No raw sources were consulted for this write-back.

## Links

- [[wiki/answers/ffrefine-average-observable-trainability-validation]]
- [[wiki/answers/ffrefine-prospective-dielectric-damped-fisher-training]]
- [[wiki/claims/CLM-0039-trust-region-kl-must-match-replay-conditioning]]
- [[wiki/questions/QST-0007-checkpoint-assessment-versus-next-direction-readiness]]
- [[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]
- [[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]
- [[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]
- [[wiki/sources/SRC-0023-statistically-optimal-analysis-multiple-equilibrium-states-mbar]]
