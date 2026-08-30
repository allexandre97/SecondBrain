---
type: answer
status: active
created: 2026-08-30
updated: 2026-08-30
question: "In FFRefine, how did the definition of the KL divergence change? Why was that change needed? What implications does that change have downstream for other calculated quantities?"
answer_status: answered
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/molecular-simulation/free-energy
  - research/adaptive-sampling
  - research/statistics/monte-carlo
tags:
  - ffrefine
  - kl-divergence
  - fisher-information
  - trust-region
  - natural-gradient
  - state-conditioning
  - replay-support
related:
  - "[[wiki/answers/ffrefine-kl-definition-for-extended-ensemble-training]]"
  - "[[wiki/answers/ffrefine-long-archive-target-gradient-convergence]]"
  - "[[wiki/answers/ffrefine-retrospective-fisher-treatment-development]]"
  - "[[wiki/claims/CLM-0039-trust-region-kl-must-match-replay-conditioning]]"
  - "[[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]"
  - "[[wiki/answers/ffrefine-paper-methods-knowledge-base]]"
sources:
  - SRC-0018
  - SRC-0023
sensitivity: public
encryption: none
wiki_pages_used:
  - "[[wiki/answers/ffrefine-kl-definition-for-extended-ensemble-training]]"
  - "[[wiki/answers/ffrefine-long-archive-target-gradient-convergence]]"
  - "[[wiki/answers/ffrefine-retrospective-fisher-treatment-development]]"
  - "[[wiki/claims/CLM-0039-trust-region-kl-must-match-replay-conditioning]]"
  - "[[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]"
  - "[[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]"
raw_sources_consulted: []
wiki_pages_updated: []
---

# FFRefine KL Divergence Definition Change

## Short answer

FFRefine's KL trust region changed from the **frozen-bias joint (mixture) KL**, whose local Fisher is the covariance of the extended-ensemble score across all thermodynamic states, to a **state-conditional KL**, defined per thermodynamic state and combined as a design-weighted average for step geometry and a maximum for step control. The change was needed because the mixture Fisher and the replay acceptance metric (state-normalized conditional empirical KL) conditioned on thermodynamic state inconsistently, so equal nominal KL budgets did not correspond to equal realised replay perturbations. Downstream, the corrected geometry changed the retained Fisher rank, the condition estimate, and the reproducible natural-gradient directions for enthalpy and dielectric, while leaving the raw gradients and density/RDF controls unchanged.

## The change in definition

The original definition, drawn from SRC-0018's information-geometry section, treats the KL locally through an empirical Fisher that is the score covariance over the frozen extended-ensemble mixture:

$$
I(\phi)=\operatorname{Cov}_{p_\phi}[\nabla_\phi u(x,V,i;\phi)],
\qquad
D_{\mathrm{KL}}(p_\phi\Vert p_{\phi+\Delta\phi})
\approx
\frac12\Delta\phi^\top I(\phi)\Delta\phi.
$$

[SRC-0018]

For a thermodynamic-state ladder this mixture Fisher decomposes by the law of total covariance into a within-state term and a between-state term:

$$
F_{\mathrm{mix}}
=
\underbrace{\sum_s\gamma_s\operatorname{Cov}_{p_s}[h_s(x)]}_{F_{\mathrm{within}}}
+
\underbrace{\operatorname{Cov}_{s\sim\gamma}(\mu_s)}_{F_{\mathrm{between}}},
\qquad
\mu_s=\mathbb E_{p_s}[h_s(x)].
$$

[[wiki/claims/CLM-0039-trust-region-kl-must-match-replay-conditioning]]

The corrected definition instead conditions on the thermodynamic state first, then aggregates. The fundamental object is the per-state candidate-to-reference KL

$$
D_s(\theta'\Vert\theta)
=
D_{\mathrm{KL}}\left(p_{\theta'}(x\mid s)\Vert p_\theta(x\mid s)\right),
$$

with the predeclared weighted average $\sum_s\gamma_s D_s$ defining the natural-gradient geometry and $\max_s D_s$ limiting finite replay steps. Its local Fisher is

$$
F_{\mathrm{cond}}
=
\sum_s\gamma_s\operatorname{Cov}_{p_\theta(x\mid s)}[h_s(x)].
$$

[[wiki/answers/ffrefine-kl-definition-for-extended-ensemble-training]]

The two definitions coincide at the within-state term only; the old one additionally carries the between-state covariance of score means, which the new one drops.

## Why the change was needed

The motivation is a conditioning mismatch between the geometry used to scale a proposal and the diagnostic used to accept it. FFRefine scaled every proposal to a fixed mixture-Fisher quadratic KL budget, but its replay acceptance computed state-normalized MBAR weights and reported a maximum state-conditional empirical KL. State-normalized weights are insensitive to configuration-independent energy shifts within a state, so the between-state score-mean term contributes to the nominal budget but cancels from the acceptance metric. Equal nominal KL therefore did not imply equal realised replay perturbation across optimiser directions. [SRC-0018] [SRC-0023] [[wiki/claims/CLM-0039-trust-region-kl-must-match-replay-conditioning]]

The mechanism was quantified on Archive A of the two 100 ns reaction-field archives: identity and diagonal steps spent about 80--84% of their nominal 0.005 budget in the between-state term, whereas hard full-Fisher and damped steps spent 98--99% in within-state curvature. This explained why identity and diagonal steps realised empirical KL around 0.0007--0.0011 despite the shared nominal target. [[wiki/answers/ffrefine-retrospective-fisher-treatment-development]]

The correction does not change what is sampled or estimated — archived targets and raw gradients were unchanged — only the geometry and KL scaling applied to those quantities. [[wiki/answers/ffrefine-long-archive-target-gradient-convergence]]

## Downstream implications

### Fisher geometry and conditioning

- Retained normalized modes rose from five to six at the $10^{-3}$ eigenvalue floor, with the newly retained boundary mode only just above the threshold.
- The physical-coordinate Fisher condition estimate fell from about $6.7\times10^7$ under the joint Fisher to about $1.46\times10^7$ under the conditional Fisher.
- The two archives' corrected Jacobi-normalized spectra are nearly identical, so archive-dependent Fisher subspaces remain unsupported as an explanation for target-family differences.

[[wiki/answers/ffrefine-long-archive-target-gradient-convergence]]

### Direction reproducibility

For the 100 ns independent-archive comparison, the conditional geometry changed the difficult-family natural-direction cosines while leaving the reproducible controls alone:

| Family | Old joint-Fisher cosine | Corrected conditional cosine |
| --- | ---: | ---: |
| Density | unchanged (control) | unchanged (control) |
| RDF | unchanged (control) | unchanged (control) |
| Enthalpy | 0.6288 | 0.8143 |
| Dielectric | 0.9743 | 0.9955 |

Dielectric now passes continuously from 40 through 100 ns; enthalpy crosses only at the 100 ns endpoint and still fails chronological-half checks. Raw-gradient cosines are identical because the estimators did not change. [[wiki/answers/ffrefine-long-archive-target-gradient-convergence]]

### Magnitude mismatch between the two KLs

For corrected steps with maximum conditional KL 0.01, the historical frozen-bias joint quadratic KL was approximately 0.156 for density, 0.010--0.011 for RDF, 0.207--0.314 for enthalpy, and 0.353--0.359 for dielectric. The between-state term contributed about 94% of the joint value for density, 10--14% for RDF, 96--97% for enthalpy, and 97% for dielectric. The removal of the term is therefore target-direction dependent: it changes enthalpy and dielectric directions far more than RDF. [[wiki/answers/ffrefine-kl-definition-for-extended-ensemble-training]]

### Invalidation of prior finite-step rankings

The historical Fisher-treatment replay campaign constructed proposals with the mixture Fisher but validated them with state-conditional empirical KL. Its finite-step observations remain valid for those exact historical proposals, but its equal-KL treatment comparison and ranking (e.g. the hard-Fisher and $\gamma=10^{-4}$ damping recommendations) do not validate the corrected conditional-Fisher proposals and must be re-run under matched conditioning. The Euclidean angle between old and corrected proposals is large and even negative for RDF and dielectric, so the proposal vectors themselves changed. [[wiki/answers/ffrefine-long-archive-target-gradient-convergence]] [[wiki/answers/ffrefine-retrospective-fisher-treatment-development]]

### What did not change

The change does not repair the underlying archive-local gradient irreproducibility for enthalpy, does not establish fresh-simulation trainability, and leaves both conditional KL and ESS unable to detect candidate regions absent from the reference archive. The frozen-bias joint KL remains a legitimate bias-portability diagnostic, just not the primary trust-region geometry. [[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]] [[wiki/answers/ffrefine-kl-definition-for-extended-ensemble-training]]

## Key equations

Frozen-bias mixture Fisher decomposition:

$$
F_{\mathrm{mix}}
=
\sum_s\gamma_s\operatorname{Cov}_{p_s}[h_s(x)]
+
\operatorname{Cov}_{s\sim\gamma}\left(\mathbb E_{p_s}[h_s(x)]\right).
$$

Corrected state-conditional Fisher:

$$
F_{\mathrm{cond}}
=
\sum_s\gamma_s\operatorname{Cov}_{p_\theta(x\mid s)}[h_s(x)],
\qquad
D_s(\theta'\Vert\theta)
=
D_{\mathrm{KL}}\left(p_{\theta'}(x\mid s)\Vert p_\theta(x\mid s)\right).
$$

## Sources used

- SRC-0018 for the original frozen-bias Fisher/KL trust region and replay acceptance workflow.
- SRC-0023 for state-normalized MBAR replay weights and the support/overlap limits they impose.

No raw sources were consulted; the answer is synthesized from existing wiki pages and the recorded FFRefine project evidence.

## Wiki pages used

- [[wiki/answers/ffrefine-kl-definition-for-extended-ensemble-training]]
- [[wiki/answers/ffrefine-long-archive-target-gradient-convergence]]
- [[wiki/answers/ffrefine-retrospective-fisher-treatment-development]]
- [[wiki/claims/CLM-0039-trust-region-kl-must-match-replay-conditioning]]
- [[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]
- [[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]

## Wiki updates made

None; the required reusable knowledge was already represented in the existing KL-definition answer, the long-archive convergence answer, and the conditioning-mismatch claim.

## Remaining gaps

- No prospective campaign has yet compared conditional-Fisher and joint-state-Fisher trust regions or established that the corrected proposals improve enthalpy or dielectric training.
- The corrected enthalpy endpoint crossing (0.8143) is only 0.014 above the 0.8 gate and has not been reproduced on a new archive pair.
- Per-state Fisher matrices have only been reported for one archive endpoint; Archive B and future prospective archives remain to be decomposed.
- The best aggregation of per-state ceilings (strict maximum versus robust quantile) for large or continuous ladders is unresolved.
