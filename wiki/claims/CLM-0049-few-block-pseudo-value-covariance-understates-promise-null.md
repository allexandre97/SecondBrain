---
type: claim
status: active
created: 2026-10-01
updated: 2026-10-11
claim_status: limited
claim_scope: local
areas:
  - research
categories:
  - research/statistics/monte-carlo
  - research/molecular-simulation/force-fields
  - research/scientific-computing
tags:
  - claim
  - ffrefine
  - jackknife
  - multiple-testing
  - direction-gate
related:
  - "[[wiki/answers/ffrefine-direction-gates-and-production-policy]]"
  - "[[wiki/claims/CLM-0050-retesting-a-failed-gate-after-extension-needs-alpha-spending]]"
  - "[[wiki/answers/adding-config-optimiser-to-ffrefine]]"
sources: []
sensitivity: public
encryption: none
project_evidence:
  - "FFRefine direction-gate Monte Carlo checks (B = 8), 2026-09-28 to 2026-10-01, as recorded in the project's improved-gates design document and reported by the implementing session: null false-pass 0.08-0.10 with a pseudo-value sample-covariance null; 0.049-0.053 (weighted sum) with a Fisher-proportional null; ConFIG multiplier within about 5% of the exact null quantile (about 2.1), per-dataset ConFIG procedure about 0.06-0.07; plain Student-t 0.10-0.13 (one family or total); analytic inflation about 2.9 and false-pass about 0.015 for multi-family ConFIG"
  - "FFRefine master 6b20031, direction_gates.jl (calibrate_promise_multiplier, promise_noise_model, promise_inflation)"
scope: timeless
---

# Few-Block Pseudo-Value Covariance Understates the Null of a Cross-Fitted Promise Test

## Claim

When the null distribution of a cross-fitted descent ("promise") test is simulated by Monte Carlo, drawing the null noise from the sample covariance of only $B$ jackknife pseudo-values (rank at most $B-1$) understates the effective dimension of the gradient noise and yields a multiplier that is too small; drawing it instead from a structured noise model (covariance proportional to the Fisher metric) with only per-family scales and between-family correlations estimated from the pseudo-values restores approximately nominal error rates. No fixed analytic inflation of the Student-t quantile is correct for every aggregation.

## Scope

Local project-evidence claim about FFRefine's promise test with $B=8$ replica-stratified time blocks, cross-fitted values $q_i=-\langle p_i[g],\hat u_{(-i)}\rangle$, and Fisher-preconditioned weighted-sum or family-level ConFIG steps. The structured model is itself an assumption (gradient noise proportional to the Fisher metric) that is not exact for real archives.

## Evidence

- With a null drawn from the pseudo-values' own sample covariance, the realised null false-pass rate was 0.08–0.10 at nominal $\alpha=0.05$.
- With a Fisher-proportional null and data-estimated scales and correlations, the weighted-sum rate was 0.049–0.053, and the ConFIG multiplier was within about 5% of the exact null quantile; the per-dataset ConFIG procedure remains slightly liberal (about 0.06–0.07) because the scales and correlations come from the data being tested.
- The plain quantile $t_{1-\alpha,B-1}$ gave 0.10–0.13 for one family or the weighted total, because cross-fitted $q_i$ and $q_j$ correlate (about $1/(B-1)$) through the shared leave-one-out steps. The worst-case analytic inflation $\sqrt{2(B-1)/(B-2)}$ (1.53 at $B=8$) is right there, but for ConFIG with several families it gives a multiplier of about 2.9 against an exact quantile of about 2.1, a false-pass rate of about 0.015.

## Caveats

- Evidence is from synthetic Monte Carlo checks inside FFRefine's test suite; the numbers were reported by the implementing session and recorded in the design document, not re-run for this page.
- The structured noise model can be wrong; FFRefine reports an effective-dimension mismatch warning rather than gating on it.
- Only $B=8$ was characterised in detail.

## Links

- [[wiki/answers/ffrefine-direction-gates-and-production-policy]]
- [[wiki/claims/CLM-0050-retesting-a-failed-gate-after-extension-needs-alpha-spending]]
- [[wiki/answers/adding-config-optimiser-to-ffrefine]]
