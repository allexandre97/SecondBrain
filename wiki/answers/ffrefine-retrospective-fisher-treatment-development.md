---
type: answer
status: active
created: 2026-08-28
updated: 2026-09-01
question: "What did retrospective Fisher-treatment development on two independent 100 ns reaction-field TSS archives establish about density, RDF, enthalpy, and dielectric optimisation?"
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
  - reaction-field
  - fisher-information
  - natural-gradient
  - steepest-descent
  - diagonal-preconditioning
  - spectral-damping
  - modal-uncertainty
  - kl-conditioning
  - state-mixture
  - replay-validation
  - enthalpy
  - dielectric-constant
related:
  - "[[wiki/answers/ffrefine-fisher-treatment-operators]]"
  - "[[wiki/answers/ffrefine-long-archive-target-gradient-convergence]]"
  - "[[wiki/answers/ffrefine-average-observable-trainability-validation]]"
  - "[[wiki/claims/CLM-0038-fixed-archive-gradient-validation-does-not-establish-fresh-archive-trainability]]"
  - "[[wiki/questions/QST-0006-average-observable-trainability-sampling-budget]]"
  - "[[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]"
  - "[[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]"
  - "[[wiki/claims/CLM-0039-trust-region-kl-must-match-replay-conditioning]]"
sources:
  - SRC-0018
  - SRC-0023
sensitivity: public
encryption: none
wiki_pages_used:
  - "[[wiki/index]]"
  - "[[wiki/answers/ffrefine-long-archive-target-gradient-convergence]]"
  - "[[wiki/answers/ffrefine-average-observable-trainability-validation]]"
  - "[[wiki/claims/CLM-0038-fixed-archive-gradient-validation-does-not-establish-fresh-archive-trainability]]"
  - "[[wiki/questions/QST-0006-average-observable-trainability-sampling-budget]]"
  - "[[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]"
raw_sources_consulted: []
wiki_pages_updated:
  - "[[wiki/answers/ffrefine-long-archive-target-gradient-convergence]]"
  - "[[wiki/answers/ffrefine-average-observable-trainability-validation]]"
  - "[[wiki/claims/CLM-0038-fixed-archive-gradient-validation-does-not-establish-fresh-archive-trainability]]"
  - "[[wiki/questions/QST-0006-average-observable-trainability-sampling-budget]]"
  - "[[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]"
  - "[[wiki/claims/CLM-0039-trust-region-kl-must-match-replay-conditioning]]"
project_evidence:
  - "FFRefine reaction-field TSS archive 31a6aa53-d503-4e60-84f6-042d4f811a6d"
  - "FFRefine reaction-field TSS archive fc504114-995d-4556-b1da-bdbe0042e5d0"
  - "FFRefine retrospective Fisher-treatment screen completed 2026-08-26, protocol fingerprint 533305656758db33454d19af400e39972e1ae94ad2c52ff60c5b0b788d8373f8"
  - "FFRefine retrospective Fisher-treatment replay completed 2026-08-28, replay hash f9f6161280882e4ee4ffc8bccfd02bfb9a54a0c2477cb88a4be7fcef05d45eea"
  - "FFRefine state-conditional Fisher/KL reanalysis of the source archives completed 2026-08-30"
  - "FFRefine post hoc within-state/between-state Fisher decomposition of the 100 ns treatment proposals completed 2026-08-29"
---

# FFRefine Retrospective Fisher-Treatment Development

## Historical result and current status

> [!IMPORTANT]
> This page records a completed historical campaign whose proposals were constructed with the frozen-bias joint Fisher but evaluated with state-normalized conditional empirical KL. The finite-step replay measurements remain valid for those exact proposals. The equal-KL treatment comparison and recorded ranking are not transferable to FFRefine's corrected state-conditional Fisher backend. A conditional rerun is in progress; until it finishes, no hard, damped, diagonal, identity, or SNR treatment from this page is the current prospective recommendation.

The historical retrospective campaign strengthens the case that the two archives contained transferable dielectric descent directions under the old geometry. The production hard-truncated Fisher direction transferred bidirectionally between the two archives, its paired loss intervals excluded zero, and every dielectric target temperature improved. Continuously damped Fisher treatment with $\gamma=10^{-4}$ produced an even larger cross-archive replay decrease and was the historical retrospective dielectric recommendation.

Enthalpy remains unresolved but the diagnosis changed. Identity and diagonal directions were highly reproducible across the complete archives, confirming that Fisher conditioning amplifies residual enthalpy-gradient error. Nevertheless, small-$\gamma$ damped proposals reduced enthalpy loss significantly in both cross-archive directions despite failing the exact-direction cosine gate. A low cosine therefore did not imply that the two proposals lacked a shared descent cone.

The run does **not** establish closed-loop trainability or validate the corrected conditional-Fisher proposals. Treatment selection and replay evaluation used the same two archives, delete-block intervals quantify within-archive rather than between-campaign uncertainty, temporal disjoint blocks remained unstable, and no candidate was tested by fresh simulation. The appropriate conclusion is that the old proposals demonstrated archive-pair-specific descent mechanisms that must be retested under matched conditional geometry and KL.

## Question and scope

The preceding 100 ns convergence study found:

- density and RDF raw and Fisher-conditioned directions were reproducible throughout;
- dielectric's cumulative production direction was continuously accepted from 60 through 100 ns and reached Fisher-metric cosine 0.9743 at 100 ns;
- enthalpy's raw-gradient cosine reached 0.9691 at 100 ns, while the production natural-direction cosine remained 0.6288;
- the Fisher subspaces were essentially identical, localising the enthalpy separation to target-gradient projections transformed by the common optimiser geometry. [[wiki/answers/ffrefine-long-archive-target-gradient-convergence]]

The new campaign asked a narrower retrospective-development question: using those same archived configurations and gradients, which treatment of the Fisher geometry gives directions that are stable across archive length and produce supported loss reduction when replayed on the other independent archive?

This is method development, not a held-out or prospective experiment.

## Archive and proposal protocol

The campaign reused the two independent one-replica, 100 ns reaction-field TSS archives from the convergence study. It preserved:

- the complete 14--41 degrees Celsius, 28-state thermodynamic ladder;
- the production lambda schedule, window size, and overlapping-window setup;
- the same ten-dimensional latent QEq-plus-bounded-parameter basis;
- density, RDF, enthalpy, and dielectric target definitions;
- reaction-field electrostatics and the operational dielectric estimator $\varepsilon_r=1+A$.

The direction screen evaluated 13 treatments at cumulative prefixes from 10 through 100 ns. It retained the production hard-Fisher, diagonal, and identity baselines, then selected two damping and two modal-SNR finalists per target family for replay. This produced seven replayed treatments per family, three proposal sources per treatment (archive A, archive B, and pooled), and therefore 84 proposed parameter vectors.

Each proposal was replayed on both archives, producing 168 archive/proposal evaluations and 1,680 delete-block paired-loss replicates. All 168 evaluations passed support and empirical-KL checks. Every candidate was accepted at its first proposed scale, and the maximum empirical KL was 0.005756 against the hard ceiling of 0.01.

## Fisher treatments compared

Let $F$ be the ridge-regularised latent Fisher, and let

$$
P_{ii}
=
\frac{1}{\sqrt{\max(F_{ii},\epsilon_J)}},
\qquad
PFP=V\Lambda V^\mathsf{T}.
$$

The production hard-truncated operator was

$$
A_{\mathrm{hard}}
=
PV_K\Lambda_K^{-1}V_K^\mathsf{T}P,
$$

where $K$ contains normalized eigenvalues greater than $10^{-3}$. The direction is $\Delta\phi=-A g$.

The alternatives were:

1. latent-space steepest descent, $A=I$;
2. diagonal Fisher scaling, $A=\operatorname{diag}(F)^{-1}$;
3. continuous spectral damping,

$$
A_\gamma
=
PV\operatorname{diag}
\left(
\frac{\lambda_k}{\lambda_k^2+\gamma^2}
\right)
V^\mathsf{T}P;
$$

4. modal-SNR weighting of hard-retained modes, with reliability

$$
r_k
=
\frac{\mathrm{SNR}_k^2}{1+\mathrm{SNR}_k^2},
\qquad
A_{\mathrm{SNR}}
=
PV_K\operatorname{diag}
\left(
\frac{r_k}{\lambda_k}
\right)
V_K^\mathsf{T}P.
$$

Every nonzero direction was scaled to the same quadratic estimate

$$
\widehat D_{\mathrm{KL}}
=
\frac12\Delta\phi^\mathsf{T}F\Delta\phi
=
0.005.
$$

## Direction-screen result

The screen score was the minimum independent-archive Fisher-metric cosine over 60, 70, 80, 90, and 100 ns. A treatment was direction-robust only if the minimum cosine was at least 0.8 and every metric norm ratio was between 0.5 and 2.

| Family | Hard Fisher | Diagonal | Identity | Best damping | Best SNR | Direction result |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| Density | 0.999886 | 0.999996 | 1.000000 | 0.999904 | 0.999887 | all robust |
| RDF | 0.999749 | 0.999999 | 1.000000 | 0.999948 | 0.999746 | all robust |
| Enthalpy | 0.260573 | 0.941532 | 0.997430 | 0.306157 at $\gamma=10^{-4}$ | 0.467618 at 2 ns | only diagonal and identity robust |
| Dielectric | 0.929655 | 0.975346 | 0.999336 | 0.962705 at $\gamma=10^{-4}$ | 0.912228 at 5 ns | all replayed treatments robust |

The enthalpy screen confirms the earlier geometry diagnosis: the raw/identity direction is reproducible, while the production Fisher operator rotates residual archive differences into materially different directions. The diagonal operator preserves most of that agreement. None of the tested full spectral inverses or SNR filters passes the enthalpy direction threshold.

The dielectric result is different. Once the complete archives reach the 60--100 ns interval, production, diagonal, identity, damped, and SNR treatments all give reproducible cumulative directions.

![[wiki/assets/ffrefine-retrospective-fisher-treatment-development/screen-selection-summary.png]]

*Figure 1. Minimum and median independent-archive direction cosines from 60 through 100 ns. The dotted line is the 0.8 direction gate. Shaded rows were selected for replay.*

## Temporal evidence remains stricter

Strong whole-archive agreement did not establish equilibration of disjoint time blocks. For example, between 60 and 100 ns:

- enthalpy identity had independent-archive cosine at least 0.9974, yet a cumulative chronological-half comparison reached -0.9993 and a local comparison reached -0.9988;
- dielectric identity had independent-archive cosine at least 0.9993, yet a cumulative chronological-half comparison reached -0.9896 and a local comparison reached -0.9997;
- hard-Fisher consecutive cumulative prefixes remained smooth, with minima 0.9379 for enthalpy and 0.9174 for dielectric, even though their local disjoint-block directions were unstable.

These are not contradictions. Complete-archive estimates average over far more data, while nested cumulative updates reuse nearly all earlier frames. Local blocks ask whether the recent sensitivity signal is individually resolved and remain much noisier. Whole-archive agreement and local equilibration therefore remain different validation axes.

![[wiki/assets/ffrefine-retrospective-fisher-treatment-development/screen-temporal-context.png]]

*Figure 2. Independent, cumulative-half, consecutive-prefix, and adjacent local-block Fisher-metric cosines for replayed treatments. Independent cumulative agreement is visibly stronger than disjoint temporal evidence for enthalpy and dielectric.*

## Replay validity

All candidates passed replay support, and all empirical KL values were below 0.01. The hard, damped, and SNR treatments generally realised empirical KL near 0.005. Identity and diagonal candidates realised much smaller values despite their identical nominal quadratic target.

| Family | Identity mean empirical KL | Diagonal mean empirical KL | Hard mean empirical KL | $\gamma=10^{-4}$ mean empirical KL |
| --- | ---: | ---: | ---: | ---: |
| Enthalpy | 0.000731 | 0.000887 | 0.005234 | 0.005473 |
| Dielectric | 0.000711 | 0.000253 | 0.005107 | 0.005444 |

The smaller identity and diagonal loss changes therefore cannot be interpreted as a fair equal-perturbation demonstration that those geometries are ineffective. A post hoc decomposition on Archive A identified why the nominal Fisher quadratic did not equalise the realised replay perturbation.

### Why identity and diagonal steps realise less empirical KL

The discrepancy is not a scaling failure. Every treatment, including identity and diagonal, satisfied

$$
\frac12\Delta\phi^\mathsf{T}F_{\mathrm{mix}}\Delta\phi=0.005.
$$

Recomputing the quadratic with the unregularised Fisher also gave 0.005 to the reported precision. The ridge contribution was negligible, so Fisher ridge regularisation does not explain the low replay KL.

The relevant distinction is thermodynamic-state conditioning. FFRefine's TSS candidate Fisher is the covariance of the reduced-potential score over the reported mixture of thermodynamic states. Let

$$
h_s(x)=\nabla_\phi u_s(x),
\qquad
\mu_s=\mathbb E_{p_s}[h_s(x)],
$$

where $s$ indexes temperature-ladder states and $\gamma_s$ is the reported TSS state probability. The law of total covariance gives

$$
F_{\mathrm{mix}}
=
\operatorname{Cov}_{s\sim\gamma,\,x\sim p_s}[h_s(x)]
=
\underbrace{\sum_s\gamma_s\operatorname{Cov}_{p_s}[h_s(x)]}_{F_{\mathrm{within}}}
+
\underbrace{\operatorname{Cov}_{s\sim\gamma}(\mu_s)}_{F_{\mathrm{between}}}.
$$

The empirical replay diagnostic is different. MBAR weights are normalized independently for every target state, and the campaign reports the maximum candidate-to-reference KL over states:

$$
D_{\mathrm{replay}}
=
\max_s D_{\mathrm{KL}}(q_s\Vert p_s).
$$

Its local curvature is therefore governed by the state-conditional covariances, not by the between-state covariance of score means:

$$
D_{\mathrm{KL}}(q_s\Vert p_s)
=
\frac12\Delta\phi^\mathsf{T}
\operatorname{Cov}_{p_s}[h_s(x)]
\Delta\phi
+O(\lVert\Delta\phi\rVert^3).
$$

A parameter displacement can consequently spend most of its nominal mixed-Fisher budget changing state-dependent mean reduced energies. Those changes contribute to $F_{\mathrm{between}}$ but cancel from weights normalized within each state. The proposal then reaches estimated mixed KL 0.005 while producing much less within-state configurational reweighting.

The Archive A decomposition confirmed this mechanism:

| Treatment | Within-state contribution | Between-state contribution | Within-state share | Mean local empirical KL |
| --- | ---: | ---: | ---: | ---: |
| Identity | 0.000813 | 0.004187 | 16.3% | 0.000883 |
| Diagonal | 0.000977 | 0.004023 | 19.5% | 0.001063 |
| Hard full Fisher | 0.004910 | 0.000090 | 98.2% | 0.005325 |
| Damped $\gamma=10^{-4}$ | 0.004958 | 0.000042 | 99.2% | 0.005378 |

The empirical diagnostic is a maximum over states whereas the within-state table entry is a TSS-weighted average, and the finite replay step contains higher-order effects. Exact equality is therefore not expected. The scale and ordering nevertheless agree: identity and diagonal spend about 80--84% of their nominal budget in the between-state term, while hard and mildly damped full-Fisher steps spend about 98--99% in within-state configurational curvature.

The optimiser geometry explains the treatment dependence. Identity follows the raw objective gradient, and diagonal scaling changes coordinate magnitudes without representing parameter correlations. In these archives those directions align strongly with score-mean differences across temperatures. Full-Fisher inversion or damping uses the correlated geometry and suppresses high-curvature between-state directions, allocating much more of the final fixed-KL step to within-state variation.

This changes the required follow-up. Blindly enlarging identity or diagonal steps until the current empirical KL reaches 0.005 would make a replay comparison more equal in realised perturbation, but it would not resolve which trust-region object is scientifically intended. Two internally consistent choices are:

1. if the trust region is meant to control canonical configurational reweighting at every temperature, construct and log state-conditional Fisher quadratics and scale against a conservative aggregation such as their maximum;
2. if changes in the joint extended-ensemble state distribution and relative state free energies are intended to consume budget, retain the mixture Fisher but validate it against a matching joint-state empirical KL.

Until that choice is made, both the mixed quadratic and the conditional empirical KL should be reported. [[wiki/claims/CLM-0039-trust-region-kl-must-match-replay-conditioning]]

![[wiki/assets/ffrefine-retrospective-fisher-treatment-development/replay-validity.png]]

*Figure 3. Empirical maximum KL for every replay route. Every point remains below the hard 0.01 ceiling; identity and diagonal treatments use substantially less empirical KL than the nominal 0.005 target.*

## Positive controls: density and RDF

All seven replayed density treatments and all seven replayed RDF treatments satisfied the campaign's combined eligibility rule: direction robustness, support, empirical KL, bidirectional cross-archive improvement, cross-archive paired upper bounds below zero, and bilateral pooled improvement.

The strongest worst-direction reductions were approximately 11.06% for density and 0.565% for RDF. The current hard Fisher was among the recorded recommendations for both. This result shows that the alternative-treatment machinery and paired replay analysis do not manufacture a failure specifically for every target or every Fisher treatment.

## Dielectric replay result

Five dielectric treatments were eligible: hard Fisher, both replayed small-$\gamma$ damped variants, and the 5 and 10 ns SNR variants. Continuous damping with $\gamma=10^{-4}$ ranked first.

| Treatment | A proposal replayed on B | B proposal replayed on A | Pooled proposal on A | Pooled proposal on B | Eligibility |
| --- | ---: | ---: | ---: | ---: | --- |
| Hard Fisher | -1.116% [-1.767%, -0.466%] | -1.110% [-1.773%, -0.447%] | -1.129% [-1.774%, -0.484%] | -1.140% [-1.785%, -0.496%] | eligible |
| Damped $10^{-4}$ | -1.812% [-2.616%, -1.007%] | -1.701% [-2.130%, -1.272%] | -1.723% [-2.121%, -1.325%] | -1.843% [-2.643%, -1.042%] | eligible, rank 1 |
| Damped $3\times10^{-4}$ | -1.633% [-2.352%, -0.915%] | -1.561% [-2.088%, -1.034%] | -1.571% [-2.080%, -1.062%] | -1.673% [-2.385%, -0.962%] | eligible, rank 2 |
| Diagonal | -0.193% [-0.397%, 0.011%] | -0.290% [-0.372%, -0.208%] | -0.247% [-0.374%, -0.120%] | -0.236% [-0.404%, -0.067%] | one cross interval inconclusive |
| Identity | -0.166% [-0.467%, 0.136%] | -0.213% [-0.453%, 0.027%] | -0.210% [-0.463%, 0.044%] | -0.170% [-0.462%, 0.121%] | cross intervals inconclusive |

Intervals are paired delete-block intervals on the evaluation archive. They quantify uncertainty in candidate-minus-baseline replay loss conditional on that archive, not the between-campaign distribution of directions.

The production hard-Fisher result is already important: the earlier 60--100 ns direction agreement now corresponds to supported, bidirectional, paired-resolved loss reduction. The long-archive dielectric observation is therefore not only an angular diagnostic.

Every hard, damped, and SNR dielectric proposal improved all six experimental target components on every local, cross, and pooled replay route. The stronger aggregate results were not caused by compensation between temperatures.

## Enthalpy replay result

No enthalpy treatment passed the campaign's complete combined eligibility rule. The reason, however, differed by treatment.

| Treatment | A proposal replayed on B | B proposal replayed on A | Pooled proposal on A | Pooled proposal on B | Failing gate |
| --- | ---: | ---: | ---: | ---: | --- |
| Hard Fisher | -1.257% [-2.650%, 0.135%] | -1.836% [-3.490%, -0.183%] | -2.771% [-4.508%, -1.033%] | -1.744% [-2.922%, -0.565%] | direction and one cross interval |
| Damped $10^{-4}$ | -1.779% [-3.095%, -0.464%] | -2.405% [-3.999%, -0.811%] | -3.216% [-4.881%, -1.550%] | -2.319% [-3.318%, -1.320%] | direction only |
| Damped $3\times10^{-4}$ | -1.541% [-2.852%, -0.230%] | -2.193% [-3.837%, -0.549%] | -3.082% [-4.812%, -1.351%] | -2.091% [-3.046%, -1.137%] | direction only |
| Diagonal | -0.410% [-1.347%, 0.527%] | -0.485% [-0.890%, -0.079%] | -0.514% [-0.928%, -0.101%] | -0.409% [-1.333%, 0.516%] | two intervals inconclusive |
| Identity | -0.392% [-1.276%, 0.492%] | -0.349% [-0.766%, 0.068%] | -0.359% [-0.766%, 0.048%] | -0.393% [-1.288%, 0.502%] | all intervals inconclusive |

Identity and diagonal treatment improved all 27 enthalpy temperature components in every cross and pooled route, but their small realised perturbations left the total paired effects unresolved. Damped $10^{-4}$ improved 74.1% and 88.9% of components in the two cross directions, and 100% and 81.5% for the pooled proposal on the two archives. The few worsening component contributions were individually small, but they show that the larger aggregate enthalpy decrease was not perfectly uniform across temperature.

The damped result is the main new enthalpy lead. Its cross-archive direction cosine fails the exact-direction gate, yet both archive-specific proposals reduce loss on the other archive with paired intervals below zero. Low mutual cosine is therefore not logically equivalent to absence of transferable descent.

![[wiki/assets/ffrefine-retrospective-fisher-treatment-development/primary-loss-transfer.png]]

*Figure 4. Local, cross-archive, and pooled primary-family replay-loss changes with paired delete-block intervals. Negative values are improvements.*

![[wiki/assets/ffrefine-retrospective-fisher-treatment-development/target-component-response.png]]

*Figure 5. Fraction of individual target components improved and the largest component-level loss change. This distinguishes broad temperature-wise improvement from aggregate compensation.*

## Why low cosine and cross descent can coexist

The direction gate asks whether two estimated finite steps are nearly the same vector under a common Fisher metric. Cross replay asks whether a particular step has negative directional effect on the other archive's finite loss surface. These are related but different questions.

For archive losses $L_A$ and $L_B$, two directions $d_A$ and $d_B$ may satisfy

$$
d_A^\mathsf{T}g_B<0,
\qquad
d_B^\mathsf{T}g_A<0,
$$

while their mutual metric cosine

$$
\frac{d_A^\mathsf{T}F d_B}
{\sqrt{d_A^\mathsf{T}F d_A}\sqrt{d_B^\mathsf{T}F d_B}}
$$

is well below 0.8. The directions can share a descent-producing component while differing strongly in orthogonal or weakly consequential components. The enthalpy damped result is direct finite-step evidence of this possibility on the observed archive pair.

The 0.8 gate remains useful as a conservative reproducibility criterion. The new evidence shows only that it is not a necessary mathematical condition for cross-archive replay descent. It should not be weakened retrospectively: method and threshold selection still require independent prospective data.

## Why small-gamma damping changed the result

At the pooled 100 ns endpoint, the normalized Fisher spectrum contained modes near

$$
\lambda_4\simeq8.19\times10^{-5},
\qquad
\lambda_5\simeq2.51\times10^{-4},
$$

followed by the five production-retained modes beginning near $4.34\times10^{-3}$. Hard truncation sets the gains of modes 4 and 5 to zero. Damping with $\gamma=10^{-4}$ gives them gains of approximately 4,902 and 3,438 while leaving the higher modes close to their ordinary inverse gains.

Small-$\gamma$ damping is therefore not merely a smoother version of the same five-dimensional production inverse. It reintroduces two positive low-Fisher modes that hard truncation removes. Those modes contributed to the larger dielectric and enthalpy replay responses, but their weak Fisher support also makes them an uncertainty risk.

The tested modal-SNR operator cannot make the same change because it applies reliability weights only to modes already above the $10^{-3}$ floor. This explains why the SNR finalists largely resembled the hard-Fisher replay result and did not repair the enthalpy direction gate.

![[wiki/assets/ffrefine-retrospective-fisher-treatment-development/modal-treatment-profiles.png]]

*Figure 6. Spectral gains, block-derived reliability, and modal SNR at 100 ns. The small-gamma treatments admit modes below the production hard floor, whereas the SNR treatment only reweights retained modes.*

## Collateral target-family effects

Changing optimiser geometry also changed multi-objective side effects. For pooled proposals:

- dielectric damped $10^{-4}$ improved density, RDF, and dielectric on both archives, but changed enthalpy by -0.56% on archive A and +1.00% on archive B;
- dielectric hard Fisher improved dielectric by about 1.13--1.14%, density by 1.35--1.46%, RDF by about 0.20%, and enthalpy by 2.22% on archive A but only 0.03% on archive B;
- enthalpy damped $10^{-4}$ improved enthalpy by 3.22% and 2.32%, slightly improved density and RDF, and worsened dielectric by 0.08% and 0.26%;
- enthalpy hard Fisher improved enthalpy and dielectric but worsened density by about 0.5%.

No treatment can therefore be called universally best from its primary-family score alone. The prospective multi-target optimiser must retain collateral-family guards.

![[wiki/assets/ffrefine-retrospective-fisher-treatment-development/collateral-family-response.png]]

*Figure 7. Pooled-proposal loss changes across every evaluated family and archive. Outlined cells identify the proposal's primary target family.*

## What this changes relative to the earlier results

1. **Dielectric:** the earlier cumulative direction result now has finite-step support. The production hard Fisher produces bidirectional paired-resolved replay descent at 100 ns. The most plausible explanation of the earlier 10--20 ns failures is insufficient gradient sampling under those budgets, not incorrect dielectric mathematics.
2. **Enthalpy:** the raw-versus-natural separation is confirmed. Identity and diagonal directions preserve archive agreement, while full spectral treatment amplifies target-specific residual error.
3. **Direction gate:** low exact-direction cosine does not necessarily preclude cross-archive replay descent. The enthalpy damped directions occupy a shared descent region despite poor mutual alignment.
4. **Damping:** the most promising retrospective treatment works partly by restoring two positive modes below the production hard floor. This is both a mechanism and a risk, not a generic endorsement of weaker regularisation.
5. **Steepest descent and diagonal scaling:** the campaign confirms reproducible direction orientation but does not fairly test finite-step effectiveness at matched conditional perturbation. Their low empirical KL is now explained by spending most of the mixed-Fisher budget in between-temperature score-mean covariance, not by a scaling or ridge-regularisation bug.
6. **Temporal convergence:** complete-archive agreement remains compatible with unstable disjoint blocks. The new replay evidence does not turn the observed 60 ns dielectric crossing into a universal equilibrium time.

![[wiki/assets/ffrefine-retrospective-fisher-treatment-development/treatment-ranking.png]]

*Figure 8. Campaign eligibility and worst cross-archive primary-loss change. The recorded recommendation is retrospective and conditional on all campaign gates.*

## What this establishes

- Every replayed candidate remained within support and the empirical-KL ceiling.
- Density and RDF remain matched positive controls under all replayed Fisher treatments.
- The production hard-Fisher dielectric proposal is a supported, bidirectional, paired-resolved descent direction on this independent 100 ns archive pair.
- Small-$\gamma$ damping gives the strongest retrospective dielectric replay result and improves all dielectric target temperatures.
- Enthalpy identity and diagonal directions are much more reproducible than full spectral directions.
- Small-$\gamma$ enthalpy damping gives bidirectional paired-resolved replay descent even though the exact directions are not reproducible under the 0.8 cosine gate.
- Nominal Fisher-estimated KL does not equalise realised empirical KL across optimiser geometries because the current Fisher and replay KL condition differently on thermodynamic state.

## What this does not establish

- that dielectric or enthalpy will improve after fresh candidate simulation;
- that $\gamma=10^{-4}$ generalises to a new archive pair or campaign seed;
- that the two low-Fisher modes admitted by small-$\gamma$ damping are population-stable;
- that the direction-cosine gate should be weakened or removed;
- that identity or diagonal scaling is ineffective at matched empirical KL;
- that a within-state maximum-Fisher trust region is superior to a joint-state trust region before the intended optimisation geometry is specified and prospectively tested;
- that delete-block paired intervals capture between-archive or method-selection uncertainty;
- that 60 or 100 ns is a universal archive requirement;
- that chronological blocks have equilibrated;
- that a primary-family improvement is acceptable in multi-target training without collateral guards.

These boundaries follow the broader validation principle that fixed-archive gradient and replay success do not establish fresh-archive trainability. [SRC-0018] [SRC-0023] [[wiki/claims/CLM-0038-fixed-archive-gradient-validation-does-not-establish-fresh-archive-trainability]]

## Prospective implication

The clean prospective dielectric comparison is now:

1. freeze the production hard-Fisher treatment as the baseline;
2. freeze damping at $\gamma=10^{-4}$ before generating new data;
3. use new independent long archives and identical latent bounds;
4. predeclare whether the trust region controls state-conditional configurational change or the joint extended ensemble, then use matched quadratic and empirical KL definitions;
5. require support, paired cross-archive loss reduction, individual-temperature response, temporal diagnostics, and collateral-family guards;
6. only then advance a frozen candidate to independent fresh simulation.

For enthalpy, damping $\gamma=10^{-4}$ is a promising retrospective lead but should not bypass the failed direction-reproducibility gate. A new archive pair or a genuinely held-out archive set must determine whether its observed shared descent cone repeats. Identity and diagonal arms remain scientifically useful, but any matched-KL comparison must first choose whether matching refers to conditional replay KL or a joint-state KL. Both definitions and the within/between Fisher decomposition should be logged.

## Sources used

For a self-contained derivation and motivation of the hard, diagonal, identity, continuously damped, and modal-SNR operators used by this campaign, see [[wiki/answers/ffrefine-fisher-treatment-operators]].

- SRC-0018 for the replay/frozen-reference optimisation route and the requirement that accepted replay updates survive resimulation.
- SRC-0023 for the scope and overlap limitations of MBAR-based reuse of sampled configurations.

No raw sources were consulted. The numerical results are FFRefine project evidence generated from the two recorded reaction-field archives.

## Wiki pages used

- [[wiki/answers/ffrefine-long-archive-target-gradient-convergence]]
- [[wiki/answers/ffrefine-average-observable-trainability-validation]]
- [[wiki/claims/CLM-0038-fixed-archive-gradient-validation-does-not-establish-fresh-archive-trainability]]
- [[wiki/questions/QST-0006-average-observable-trainability-sampling-budget]]
- [[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]

## Wiki updates made

- Updated the long-archive answer with the retrospective replay consequence.
- Updated the average-observable validation synthesis with the new optimiser-treatment evidence.
- Updated the sampling-budget question, signal-versus-support tension, and fixed-archive validation claim.

## Remaining gaps

- The treatment comparison is retrospective and uses only one archive pair.
- There is no independent archive pair reserved from treatment selection.
- There is no fresh-candidate simulation for any treatment.
- Empirical-KL-matched identity and diagonal steps have not been replayed.
- Per-state Fisher matrices and a matching joint-state empirical KL have not yet been compared prospectively.
- Between-campaign variability of the low-Fisher modes is unknown.
- The archive length needed for repeatable dielectric prospective success remains unknown.
