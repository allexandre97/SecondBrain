---
type: claim
status: active
created: 2026-08-29
updated: 2026-08-29
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
---

# Trust-Region KL Must Match Replay Conditioning

## Claim

When an empirical Fisher matrix defines a KL trust region, it must marginalize or condition on thermodynamic state in the same way as the empirical KL diagnostic used to validate the step. Otherwise equal nominal Fisher-quadratic KL does not imply equal realised replay perturbation across optimiser directions. [SRC-0018] [SRC-0023]

## Scope

The mathematical conditioning requirement is general, but the quantitative evidence here is local to FFRefine's two archived 100 ns reaction-field water simulations and its August 2026 retrospective treatment campaign. It does not establish that a conditional or joint-state trust region is universally preferable.

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

## Limitations

- The numerical decomposition has been performed for one archive endpoint and should be repeated for Archive B and future prospective archives.
- The reported empirical KL is a maximum over states, whereas the within-state decomposition above is weighted by the TSS state probabilities.
- Finite-step KL also contains higher-order terms beyond the local Fisher quadratic.
- No prospective run has yet compared conditional-Fisher and joint-state-Fisher trust regions.

## FFRefine design recommendation

For FFRefine's usual goal, the state density is prescribed by the enhanced-sampling design and can readapt after a force-field update. The weighted state-conditional Fisher should therefore orient proposals, while the maximum state-conditional KL should limit finite replay steps. The current mixture Fisher remains meaningful as a frozen-bias portability diagnostic because its between-state component predicts state-occupancy changes before the bias readapts.

This is a project design recommendation rather than a prospective result. See [[wiki/answers/ffrefine-kl-definition-for-extended-ensemble-training]].

## Links

- [[wiki/answers/ffrefine-retrospective-fisher-treatment-development]]
- [[wiki/answers/ffrefine-kl-definition-for-extended-ensemble-training]]
- [[wiki/questions/QST-0006-average-observable-trainability-sampling-budget]]
- [[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]
- [[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]
- [[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]
- [[wiki/sources/SRC-0023-statistically-optimal-analysis-multiple-equilibrium-states-mbar]]
