---
type: claim
status: active
created: 2026-10-01
updated: 2026-10-05
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
  - multiple-testing
  - optional-stopping
  - production-extension
related:
  - "[[wiki/answers/ffrefine-direction-gates-and-production-policy]]"
  - "[[wiki/claims/CLM-0049-few-block-pseudo-value-covariance-understates-promise-null]]"
  - "[[wiki/tensions/TEN-0020-config-family-exclusion-versus-untreated-drift]]"
  - "[[wiki/answers/ffrefine-config-vs-weighted-sum-water-campaign-results]]"
sources: []
sensitivity: public
encryption: none
project_evidence:
  - "FFRefine production-decision Monte Carlo checks (B = 8, alpha = 0.05, alpha0 = 0.04, c_ex = 1, rho = 0.85, c0 = 0.05), reported by the implementing session 2026-09-30 to 2026-10-01: uncorrected two-look false-pass 0.0727 (size) and 0.070 (promise), about 1.45 alpha; with alpha-spending 0.051 and 0.056; conditional model at kappa = 1.1, z = 1.6: realised 0.23 vs predicted 0.08; after selection on a failed look 0: realised 0.565 vs predicted 0.458"
  - "FFRefine master 6b20031, production_decision.jl (rescue_look_threshold, gate_looks, rescue_pass_probability) and test/production_decision_checks.jl"
---

# Retesting a Failed Gate After an Extension Needs α-Spending

## Claim

Extending a sampling archive *because* a family failed a noise test, and then retesting that family on the extended archive, is optional stopping: with both looks at level $\alpha$, the family's false-pass rate exceeds $\alpha$ (about $1.45\alpha$ for one look in FFRefine's setting), and an α-spending design — a reduced level $\alpha_0$ at the first look for families that could be rescued, plus a Monte Carlo look-1 threshold calibrated under the actual rescue rule — restores approximately nominal error.

## Scope

Local project-evidence claim for FFRefine's one-look rescue policy: archives extended to $\kappa T$ share their original frames, both looks re-block into $B=8$ blocks, rescues are chosen by an expected-value rule, and the included family set is held at its look-0 value in the calibration.

## Evidence

- Uncorrected (both looks at $\alpha=0.05$): 0.0727 for the size test and 0.070 for the promise test.
- With $\alpha_0=(1-0.2)\alpha=0.04$ at look 0 and a Monte Carlo $m_1$ at look 1: 0.051 and 0.056.
- The predictive model behind the rescue rule, $P(\kappa)=\Phi\big((\mu(\kappa)-m_1)/\sqrt{1-1/\kappa}\big)$, is pessimistic for short extensions because re-blocking re-estimates the standard error ($\kappa=1.1$, $z=1.6$: realised 0.23 against predicted 0.08), and a just-failed statistic is biased low (after selection: realised 0.565 against predicted 0.458). These biases make the rescue rule conservative about buying extensions but do not remove the optional-stopping inflation, which is why the threshold is calibrated on the actual rule.

## Caveats

- Numbers come from synthetic Monte Carlo checks and were reported by the implementing session; the test code was inspected but not re-run for this page.
- The calibration ignores that a rescued ConFIG look can change the included set.
- No deciding campaign had executed a rescue extension at the time of writing (2026-10-01), so realised look-1 pass rates in production are unmeasured.

## 2026-10-05 update: production rescues now observed

Six rescue extensions have now run in the two deciding water campaigns (five resolved, one cut short by an out-of-memory crash before its chain ran). They are too few to re-estimate a realised look-1 pass rate, but they do show failure modes beyond the look-level statistics this claim covers: a rescue can pass its own targeted statistic and still fail a *later* stage of the gate (a ConFIG size-filter rescue passing size and then failing the promise test), and a weighted-sum rescue's total-based statistic can make a family that is simply at its own constrained optimum look rescuable, bypassing this policy's own "not rescuable" protection, which is keyed to the family's own size statistic. These are generic design flaws, not failures of the alpha-spending correction itself, and are recorded with full numbers in [[wiki/answers/ffrefine-direction-gates-and-production-policy]] and [[wiki/answers/ffrefine-config-vs-weighted-sum-water-campaign-results]].

## Links

- [[wiki/answers/ffrefine-direction-gates-and-production-policy]]
- [[wiki/claims/CLM-0049-few-block-pseudo-value-covariance-understates-promise-null]]
- [[wiki/tensions/TEN-0020-config-family-exclusion-versus-untreated-drift]]
- [[wiki/answers/ffrefine-config-vs-weighted-sum-water-campaign-results]]
