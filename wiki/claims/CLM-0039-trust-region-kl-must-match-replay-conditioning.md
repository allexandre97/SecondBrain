---
type: claim
status: active
created: 2026-08-29
updated: 2026-09-04
claim_status: limited
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
  - fisher-information
  - trust-region
  - empirical-kl
  - thermodynamic-conditioning
  - state-mixture
related:
  - "[[wiki/answers/ffrefine-aggressive-density-kl-ess-training]]"
  - "[[wiki/answers/ffrefine-retrospective-fisher-treatment-development]]"
  - "[[wiki/answers/ffrefine-kl-definition-for-extended-ensemble-training]]"
  - "[[wiki/questions/QST-0006-average-observable-trainability-sampling-budget]]"
  - "[[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]"
  - "[[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]"
sources:
  - SRC-0018
  - SRC-0023
sensitivity: public
encryption: none
project_evidence:
  - "FFRefine retrospective Fisher-treatment screen and paired cross-archive replay completed 2026-08-28"
  - "FFRefine post hoc within-state/between-state Fisher decomposition of Archive A completed 2026-08-29"
  - "FFRefine higher-KL dielectric-only damped-Fisher reaction-field water-temperature run 20260902-115818, intentionally stopped during epoch 8 on 2026-09-03 after six paired-confirmed fresh updates"
  - "FFRefine density-only KL 0.1/archive 1.0/ESS 0.45 water-temperature run 20260903-220645, completed 2026-09-03"
  - "FFRefine density-only aggressive conditional-KL/ESS water-temperature run 20260904-102939, completed 2026-09-04"
---

# Trust-Region KL Must Match Replay Conditioning

## Claim

When an empirical Fisher matrix defines a KL trust region, it must marginalize or condition on thermodynamic state in the same way as the empirical KL diagnostic used to validate the step. Otherwise equal nominal Fisher-quadratic KL does not imply equal realised replay perturbation across optimiser directions. [SRC-0018] [SRC-0023]

## Scope

The mathematical conditioning requirement is general, but the quantitative evidence here is local to FFRefine's archived reaction-field water simulations and its retrospective and prospective water-temperature campaigns. It does not establish that a conditional or joint-state trust region is universally preferable.

## Mechanism

For state-specific score $h_s(x)=\nabla_\phi u_s(x)$ and state probability $\gamma_s$, the mixture Fisher decomposes as

$$
F_{\mathrm{mix}}
=
\sum_s\gamma_s\operatorname{Cov}_{p_s}[h_s(x)]
+
\operatorname{Cov}_{s\sim\gamma}
\left(\mathbb E_{p_s}[h_s(x)]\right).
$$

The first term controls configurational reweighting within thermodynamic states. The second measures variation of mean scores between states. An empirical KL computed after separately normalizing candidate and reference weights within each state is insensitive to state-specific constant energy shifts and therefore does not include the second term in its local curvature.

The Fisher/KL relation motivates local trust-region scaling, while MBAR supplies state-specific normalized replay weights. [SRC-0018] [SRC-0023] The exact coexistence of a mixture Fisher and maximum state-conditional empirical KL described here is an FFRefine implementation fact, not a claim attributed to either source.

## Project evidence

Every screened treatment was scaled to mixed-Fisher estimated KL 0.005. On Archive A:

- identity allocated 0.000813 to within-state covariance and 0.004187 to between-state covariance; its mean local empirical KL was 0.000883;
- diagonal scaling allocated 0.000977 within state and 0.004023 between states; its mean local empirical KL was 0.001063;
- hard full-Fisher scaling allocated 0.004910 within state and 0.000090 between states; its mean local empirical KL was 0.005325;
- damping at $\gamma=10^{-4}$ allocated 0.004958 within state and 0.000042 between states; its mean local empirical KL was 0.005378.

Recomputing with the unregularised Fisher preserved the nominal 0.005 values; the ridge contribution was negligible. The discrepancy is therefore attributable to state conditioning and direction orientation rather than failed scaling or ridge regularisation.

## Consequences

- Do not interpret identity or diagonal loss effects as weaker optimiser geometry until perturbations are compared under a matched KL definition.
- Log within-state and between-state Fisher contributions for every proposed direction.
- If the intended trust region controls canonical distributions at each temperature, evaluate per-state Fisher quadratics and scale against a predeclared conservative aggregation.
- If the intended trust region controls the joint extended ensemble, retain the mixture Fisher but add a matching joint-state empirical KL diagnostic.
- Continue reporting support and fresh-simulation validation; matching KL geometry does not establish trainability. [SRC-0018]

## Prospective operational evidence

Higher-KL dielectric run `20260902-115818` prospectively exercised the matched state-conditional geometry for seven completed optimization epochs. Accepted individual-step empirical KL values were 0.00480--0.01999 under target 0.02. Three accepted aligned steps produced empirical archive-to-candidate KL 0.1202--0.1755, while a fourth remained at 0.2142--0.2515 and was rejected against the 0.2 ceiling.

The sum of local Fisher-quadratic step estimates was only 0.0432--0.0585. The exact empirical archive audit therefore prevented the local estimates from being treated as an additive cumulative divergence. All 21 accepted steps retained replay support, and the first six checkpoint updates subsequently reduced paired loss on fresh archives. This supports the conditional-KL design as an operational trust-region implementation, not merely a retrospective geometric correction. [[wiki/answers/ffrefine-prospective-dielectric-damped-fisher-training]]

Density-only positive-control run `20260904-102939` tested a more aggressive local region: maximum conditional-KL target 0.1, empirical archive ceiling 1.0, and target-state and candidate ESS-retention thresholds 0.25. Its accepted proposal chains reached empirical archive KL 0.3006 and 0.3803. Both resulting macro-updates were accepted by paired fresh comparisons; the fresh loss fell from 143.6331 to 56.0352 and then 21.5935, and two terminal validations gave losses 20.0060 and 20.2560.

This rules out treating 0.2 as a universal empirical archive-KL safety boundary. It does not identify a replacement universal boundary. In preceding density run `20260903-220645`, an update constructed at archive KL 0.3030 could not obtain a supported paired comparison on its fresh archive, whereas the new run succeeded at 0.3006 and 0.3803. The runs were not matched and cannot isolate the cause. In the new run, an attempted later proposal was also rejected when its minimum target-state ESS fell to 98.70 despite relative retention 0.2726. Exact empirical archive KL, absolute and relative support, loss uncertainty, and fresh resimulation therefore remain complementary controls. [[wiki/answers/ffrefine-aggressive-density-kl-ess-training]]

## Limitations

- The numerical decomposition has been performed for one archive endpoint and should be repeated for Archive B and future prospective archives.
- The reported empirical KL is a maximum over states, whereas the within-state decomposition above is weighted by the TSS state probabilities.
- Finite-step KL also contains higher-order terms beyond the local Fisher quadratic.
- No matched prospective run has compared conditional-Fisher and joint-state-Fisher trust regions; the successful prospective runs used only the selected conditional geometry.
- The aggressive density result is one campaign realization and does not calibrate a transferable KL or ESS boundary for other targets or systems.

## FFRefine design recommendation

For FFRefine's usual goal, the state density is prescribed by the enhanced-sampling design and can readapt after a force-field update. The weighted state-conditional Fisher should therefore orient proposals, while the maximum state-conditional KL should limit finite replay steps. The current mixture Fisher remains meaningful as a frozen-bias portability diagnostic because its between-state component predicts state-occupancy changes before the bias readapts.

This began as a project design recommendation and has now been exercised prospectively for dielectric training. The choice still lacks a matched prospective comparison against the old joint-state geometry. See [[wiki/answers/ffrefine-kl-definition-for-extended-ensemble-training]].

## Links

- [[wiki/answers/ffrefine-aggressive-density-kl-ess-training]]
- [[wiki/answers/ffrefine-retrospective-fisher-treatment-development]]
- [[wiki/answers/ffrefine-kl-definition-for-extended-ensemble-training]]
- [[wiki/questions/QST-0006-average-observable-trainability-sampling-budget]]
- [[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]
- [[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]
- [[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]
- [[wiki/sources/SRC-0023-statistically-optimal-analysis-multiple-equilibrium-states-mbar]]
