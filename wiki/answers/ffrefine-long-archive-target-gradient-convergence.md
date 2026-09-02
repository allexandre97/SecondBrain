---
type: answer
status: active
created: 2026-08-26
updated: 2026-09-02
question: "What did two independent 100 ns reaction-field TSS archives establish about convergence of FFRefine water target values, gradients, and natural-gradient directions?"
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
  - gradient-convergence
  - fisher-information
  - optimizer-geometry
  - steepest-descent
  - enthalpy
  - dielectric-constant
  - independent-archives
related:
  - "[[wiki/answers/ffrefine-prospective-dielectric-damped-fisher-training]]"
  - "[[wiki/answers/ffrefine-retrospective-fisher-treatment-development]]"
  - "[[wiki/answers/ffrefine-average-observable-trainability-validation]]"
  - "[[wiki/claims/CLM-0038-fixed-archive-gradient-validation-does-not-establish-fresh-archive-trainability]]"
  - "[[wiki/questions/QST-0006-average-observable-trainability-sampling-budget]]"
  - "[[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]"
  - "[[wiki/concepts/dipole-moment-fluctuation-dielectric-constant]]"
sources:
  - SRC-0018
  - SRC-0023
sensitivity: public
encryption: none
raw_sources_consulted: []
project_evidence:
  - "FFRefine reaction-field TSS archive 31a6aa53-d503-4e60-84f6-042d4f811a6d, analysed 2026-08-25"
  - "FFRefine reaction-field TSS archive fc504114-995d-4556-b1da-bdbe0042e5d0, analysed 2026-08-26"
  - "FFRefine two-archive target-gradient convergence comparison completed 2026-08-26"
  - "FFRefine cumulative/local half and consecutive-prefix reanalysis completed 2026-08-26"
  - "FFRefine raw-versus-Fisher-conditioned optimizer interpretation completed 2026-08-26"
  - "FFRefine Jacobi-scaled truncated-Fisher implementation audit completed 2026-08-26"
  - "FFRefine retrospective Fisher-treatment screen and paired cross-archive replay completed 2026-08-28"
  - "FFRefine state-conditional Fisher/KL reanalysis of the same two 100 ns archives completed 2026-08-30"
---

# FFRefine Long-Archive Target-Gradient Convergence

## Short answer

Two independently prepared 100 ns reaction-field TSS archives substantially changed the diagnosis, but did not establish closed-loop trainability.

The same archived configurations, target estimates, and raw gradients were reanalysed after FFRefine's trust-region geometry was corrected on 2026-08-30. The old analysis used a frozen-bias joint Fisher that included covariance between thermodynamic-state score means, while replay acceptance used state-normalized conditional KL. The corrected analysis uses the design-weighted state-conditional Fisher for direction geometry and the maximum state-conditional KL for step scaling. This is the current interpretation; the earlier joint-Fisher numbers remain historical diagnostics only.

Density and RDF remain positive controls: their raw gradients and conditional-Fisher directions agree across independent archives at every cumulative prefix from 10 through 100 ns. Dielectric is stronger under the corrected geometry: its direction passes continuously from 40 through 100 ns and reaches cosine 0.9955 with norm ratio 0.9812 at 100 ns.

Enthalpy changes materially. Its raw-gradient cosine remains 0.9691 because the raw estimators are unchanged, but its conditional-Fisher direction reaches cosine 0.8143 with norm ratio 1.0079 at 100 ns and therefore crosses the predeclared gate. It does not pass at 90 ns, and both 100 ns chronological-half comparisons remain below threshold, so “sustained from 100 ns” is only an endpoint crossing rather than evidence of stable equilibration or trainability.

The corrected result narrows the old diagnosis. Fisher conditioning still reduces enthalpy agreement relative to the raw gradient, but the inappropriate between-state term was a material contributor to the previous 0.6288 failure. Residual gradient variability remains, while the corrected geometry maps the same two gradients into a barely reproducible endpoint direction.

The direct target values looked converged much earlier than this distinction became visible. At 100 ns, the root-mean-square independent-archive target differences were only 0.159, 0.171, 0.305, and 0.082 target-tolerance units for density, RDF, enthalpy, and dielectric respectively. Stable observable means were therefore neither sufficient to establish a stable natural direction nor diagnostic of which target family would pass.

A finer temporal decomposition strengthens that warning. In archive 2, extending the cumulative enthalpy estimate from 70 to 80 ns left its raw-gradient cosine apparently high at 0.8876, but reduced the raw-gradient norm from 239.3 to 85.7, a ratio of 0.3582. The corresponding KL-scaled natural-step norm ratio remained 0.9975. Thus a nearly fixed optimizer step length can conceal a large change in the underlying estimated gradient.

The earlier retrospective Fisher-treatment campaign replayed proposals constructed with the old joint-Fisher geometry and a mismatched conditional empirical-KL check. Its finite-step observations remain evidence about those historical proposals, but its treatment ranking and effect sizes do not validate the corrected conditional-Fisher proposals. A conditional rerun is required before carrying any hard-Fisher or damping recommendation forward. [[wiki/answers/ffrefine-retrospective-fisher-treatment-development]]

## Experiment and provenance

The experiment used:

- reaction-field electrostatics and the operational dielectric estimator $\varepsilon_r=1+A$;
- the exact `water_temperature.jl` thermodynamic ladder from 14 through 41 degrees Celsius, with 28 states, the unchanged lambda schedule, window size 4, and 15 overlapping windows;
- the same complete ten-dimensional latent parameter basis for density, RDF, enthalpy, and dielectric, comprising QEq and bounded water parameters;
- two independently prepared TSS archives, one replica per archive;
- 100 ns of production per archive, saved every 5 ps, giving 20,001 frames per archive;
- cumulative analyses at 10 ns intervals and chronological-half analyses at every prefix;
- delete-block jackknife calculations with 2, 5, and 10 ns blocks;
- the prospective direction gate used elsewhere in FFRefine: Fisher-metric cosine at least 0.8 and norm ratio between 0.5 and 2.

The comparison is deliberately cost- and protocol-matched across target families. Experimental target sparsity changes scoring only; it does not change the TSS ladder.

## Sampling and replay validity

Every cumulative prefix in both archives passed the recorded sampling and Fisher-validity gates. Every thermodynamic state and TSS window was represented. Candidate ESS increased from about 1,920–1,997 frames at 10 ns to 18,744–19,910 frames at 100 ns. Minimum local ESS ratios remained about 0.135–0.206 across the series, and maximum frame weights decreased with archive length.

Under the corrected conditional geometry, the physical-coordinate Fisher condition estimate remains large but falls to approximately $1.45\times10^7$ to $1.48\times10^7$, and both 100 ns endpoints retain the same six normalized modes. This experiment therefore does not support incomplete ladder coverage, rejected replay support, or archive-dependent retained Fisher rank as explanations for the remaining target-family separation.

![[wiki/assets/ffrefine-long-archive-target-gradient-convergence/sampling-diagnostics.png]]

*Figure 1. Sampling, replay, coverage, and Fisher diagnostics versus cumulative archive length for the two independent archives.*

## Direct targets converge before all optimisation directions

At 100 ns, the RMS independent-archive target disagreement divided by the fitting tolerance was:

| Family | RMS target difference / tolerance |
| --- | ---: |
| Density | 0.1589 |
| RDF | 0.1707 |
| Enthalpy | 0.3047 |
| Dielectric | 0.0823 |

All four values are small compared with one tolerance unit. Dielectric has the smallest direct-target disagreement even though it was the slowest family to acquire a reproducible natural direction. Enthalpy target disagreement also decreases substantially, yet its production direction never passes. Direct-value convergence and optimiser-direction convergence are therefore distinct empirical questions.

![[wiki/assets/ffrefine-long-archive-target-gradient-convergence/target-loss-and-disagreement.png]]

*Figure 2. Family losses and independent-archive target disagreement. The direct quantities become mutually consistent without guaranteeing natural-gradient agreement.*

## Independent-archive direction convergence

The 100 ns comparison was:

| Family | Raw-gradient cosine | Raw norm ratio | Natural-direction cosine | Natural norm ratio | Natural direction accepted |
| --- | ---: | ---: | ---: | ---: | --- |
| Density | 0.999997 | 1.0258 | 0.999970 | 1.0106 | yes |
| RDF | 0.999998 | 0.9839 | 0.999795 | 1.0104 | yes |
| Enthalpy | 0.969050 | 0.9655 | 0.814334 | 1.0079 | yes |
| Dielectric | 0.977708 | 0.8204 | 0.995525 | 0.9812 | yes |

The cumulative time series adds important context:

- density and RDF passed at every prefix from 10 through 100 ns;
- dielectric passed at every prefix from 40 through 100 ns;
- enthalpy passed only at the 100 ns endpoint; its 90 ns cosine was 0.7368;
- norm ratios remained close to one, so the difficult-family failures were predominantly angular rather than step-length failures.

![[wiki/assets/ffrefine-long-archive-target-gradient-convergence/independent-archive-direction-convergence.png]]

*Figure 3. Independent-archive cosine and norm ratio before and after corrected state-conditional Fisher conditioning. The raw-gradient norm uses the Euclidean latent-space metric; the natural-step norm uses the averaged conditional Fisher metric.*

![[wiki/assets/ffrefine-long-archive-target-gradient-convergence/direction-acceptance-heatmap.png]]

*Figure 4. Prospective natural-direction gate over cumulative archive length. Dielectric's 40 ns crossing and enthalpy's isolated 100 ns crossing describe this one archive pair; neither is a universal sampling threshold.*

## Nested endpoint self-convergence is descriptive, not independent evidence

For each archive, the nested endpoint diagnostic compares the cumulative prefix $[0,t]$ with that same archive's full $[0,100\,\mathrm{ns}]$ estimate. The pooled curve makes the corresponding comparison after combining both archives at each prefix. Therefore its points share most frames with their reference, and the pooled curve also averages archive-specific fluctuations. Its smoothness is expected and must not be interpreted as independent evidence of equilibrium.

![[wiki/assets/ffrefine-long-archive-target-gradient-convergence/nested-endpoint-convergence.png]]

*Figure 5. Per-archive and pooled cumulative-prefix natural directions compared with their own 100 ns endpoint. These are nested self-convergence diagnostics; pooling reduces noise but does not create an independent replicate.*

## Cumulative and local disjoint halves remain a warning

Two complementary disjoint-half diagnostics were calculated. At cumulative time $t$, the cumulative-half comparison is

$$
[0,t/2]\quad\text{versus}\quad(t/2,t],
$$

whereas the local 5 ns comparison is

$$
(t-10\,\mathrm{ns},t-5\,\mathrm{ns}]\quad\text{versus}\quad(t-5\,\mathrm{ns},t].
$$

For example, at 60 ns the cumulative diagnostic compares 0–30 with 30–60 ns, while the local diagnostic compares 50–55 with 55–60 ns. The former asks whether the two long chronological halves agree; the latter asks whether the most recent adjacent short blocks agree.

Independent cumulative agreement did not imply that each archive had internally stable halves. At 100 ns, cumulative-half natural-direction cosines were:

| Family | Archive 1 halves | Archive 2 halves |
| --- | ---: | ---: |
| Density | approximately 1.000 | 0.999 |
| RDF | approximately 1.000 | approximately 1.000 |
| Enthalpy | 0.752 | 0.548 |
| Dielectric | 0.802 | 0.794 |

The corrected geometry brings both dielectric half comparisons close to the 0.8 threshold but leaves one just below it. Both enthalpy half comparisons fail. This does not invalidate cumulative independent-archive agreement, but it prevents treating it as proof of equilibration. Both chronological and independent axes must remain visible.

Archive 2 enthalpy illustrates why both orientation and magnitude are required:

| Prefix | Raw-gradient cosine | Raw norm ratio | Natural-direction cosine | Natural norm ratio |
| --- | ---: | ---: | ---: | ---: |
| 70 ns halves | 0.8964 | 0.2524 | 0.8449 | 0.9855 |
| 80 ns halves | -0.9654 | 0.8868 | 0.2114 | 0.9977 |

At 70 ns, the high raw-gradient cosine alone is misleading because the two half-gradient norms differ by almost a factor of four. At 80 ns, the two cumulative halves point in nearly opposite raw-gradient directions. The near-unit natural-step norm ratios do not rescue these comparisons because KL scaling deliberately normalizes the final step magnitude.

The local diagnostic is stricter and noisier. All local enthalpy pairs failed the target-family split-validity check, so their plotted crosses are diagnostic values rather than accepted estimates. At 100 ns, dielectric local natural-direction cosines improve to 0.242 and 0.448 in archives 1 and 2 but remain far below the gate. The corresponding enthalpy values are 0.327 and 0.678 and are split-invalid. Similar final step lengths therefore continue to coexist with different recent-block directions.

![[wiki/assets/ffrefine-long-archive-target-gradient-convergence/cumulative-and-local-half-agreement.png]]

*Figure 6. Cosine and norm-ratio agreement before and after Fisher conditioning for cumulative chronological halves and local adjacent 5 ns blocks. Crosses identify local comparisons that failed sampling or family split validity; they remain visible only as diagnostics and are not connected as accepted trends.*

## Consecutive cumulative updates expose magnitude instability

The cumulative-update diagnostic compares

$$
[0,t-10\,\mathrm{ns}]\quad\text{with}\quad[0,t]
$$

and therefore asks how much the latest 10 ns changes the complete estimate available at time $t$. Because the samples are nested, strong agreement is expected; a large change is especially informative.

At the 80 ns mark, the enthalpy comparison was:

| Archive | Raw-gradient cosine | Raw norm ratio | Earlier raw norm | Updated raw norm | Natural-direction cosine | Natural norm ratio |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 0.9841 | 1.2000 | 163.2 | 195.8 | 0.9939 | 1.0007 |
| 2 | 0.8876 | 0.3582 | 239.3 | 85.7 | 0.9379 | 0.9975 |

This is not a cumulative-gradient sign flip: archive 2 retains a positive cosine. It is nevertheless a severe norm collapse accompanied by meaningful rotation after adding only the 70–80 ns segment. The effect is possible because replay analysis does not append an independently averaged gradient. MBAR free energies and normalized weights are re-estimated, so old-frame weights change; target residuals and observable Jacobians are also recomputed. Schematically, for target family $f$,

$$
\mathbf g_f(t)
=
2\sum_i \omega_i
\frac{r_{f,i}(t)}{\tau_{f,i}}
\nabla_{\phi} y_{f,i}(t),
$$

and every factor can change when the prefix is extended. For cancellation-sensitive observables such as enthalpy, the net vector can therefore change much more than the direct mean.

![[wiki/assets/ffrefine-long-archive-target-gradient-convergence/cumulative-update-gradient-and-natural-direction.png]]

*Figure 7. Consecutive cumulative-prefix updates. Raw-gradient cosine, absolute norm, and norm ratio are shown separately from Fisher-metric natural-direction cosine and natural-step norm ratio. The latter can remain near one because the optimizer scales accepted proposals to its KL budget.*

## Fisher preconditioning is an amplifier, not an archive-dependent root cause

### What the production Fisher operator actually is

FFRefine first centers score derivatives independently within every thermodynamic state and forms

$$
F_{\theta,\mathrm{cond}}=\sum_s\gamma_s\operatorname{Cov}_{p_\theta(x\mid s)}[h_s(x)].
$$

It does not invert this physical-coordinate matrix directly. The implementation applies the parameterization chain rule,

$$
g_\phi=J^\mathsf{T}g_\theta,
\qquad
F_\phi=J^\mathsf{T}F_\theta J,
$$

where $J$ includes the derivatives of bounded latent parameters and constrained QEq parameters. It then adds a small numerical ridge,

$$
F_r=F_\phi+10^{-8}I,
$$

and constructs the Jacobi scale and dimensionless correlation-like matrix

$$
P_{ii}=\frac{1}{\sqrt{\max((F_r)_{ii},\epsilon_J)}},
\qquad
C=PF_rP.
$$

After diagonalizing $C=V\Lambda V^\mathsf{T}$, the production setting retains only modes with normalized eigenvalue greater than $10^{-3}$. With $K$ denoting those modes,

$$
W=PV_K\Lambda_K^{-1/2},
$$

and the one-family unscaled direction is

$$
\Delta\phi_0
=-WW^\mathsf{T}g_\phi
=-PV_K\Lambda_K^{-1}V_K^\mathsf{T}Pg_\phi.
$$

A final scalar enforces the maximum state-conditional Fisher-estimated KL budget. It changes step length but cannot change the direction cosine. With one active target family and disabled parameter regularization, the ConFIG path reduces algebraically to this same truncated natural step. Momentum was disabled in the reproducibility campaigns. ConFIG and momentum therefore did not cause the observed single-family archive disagreement, although both can matter later in multi-target or multi-epoch production.

An implementation audit found this sequence algebraically consistent: the physical-to-latent chain rule, Jacobi transformation, retained-mode inverse, and KL rescaling match their intended definitions. The result should therefore be described as a **Jacobi-scaled, hard-truncated, ridge-regularized natural metric**, not as an unqualified inverse of the raw Fisher matrix.

### What the corrected geometry removes and what it leaves

The former frozen-bias joint Fisher decomposes as

$$
F_{\mathrm{joint}}=F_{\mathrm{cond}}+\operatorname{Cov}_{\gamma}(\mu_s).
$$

The second term measures changes in thermodynamic-state score means and therefore predicts immediate state-occupancy or bias-portability changes under a frozen old bias. It is not the curvature of the normalized canonical distribution within each state. Using it to orient and scale proposals while validating replay with state-normalized empirical KL made the quadratic and empirical trust regions refer to different probability distributions.

At 100 ns the corrected Jacobi-normalized spectra are nearly identical between archives. Representative eigenvalues are

$$
(2.2\times10^{-11},5.6\times10^{-11},8.9\times10^{-11},
3.0\times10^{-4},1.0\times10^{-3},1.5\times10^{-2},
5.0\times10^{-2},2.5\times10^{-1},5.5\times10^{-1},9.1).
$$

The $10^{-3}$ floor retains six modes in both archives; the newly retained boundary mode is only just above the threshold. The minimum principal cosine is 0.999941 and normalized projector overlap is 0.999980, so archive-dependent Fisher subspaces remain unsupported as the explanation. The physical-coordinate condition estimate falls from about $6.7\times10^7$ under the joint Fisher to about $1.46\times10^7$ under the conditional Fisher.

The enthalpy improvement is not solely a threshold-crossing artifact. Its 100 ns independent-archive cosine is 0.811, 0.814, and 0.804 at floors $10^{-4}$, $10^{-3}$, and $10^{-2}$ respectively. The conditional geometry changes the complete retained operator, not merely its rank.

The 100 ns counterfactuals are now:

| Enthalpy variant at 100 ns | Metric cosine |
| --- | ---: |
| Raw objective gradient | 0.9691 |
| Each gradient with its own conditional Fisher | 0.8143 |
| Each gradient with the common conditional Fisher | 0.8118 |
| Common averaged gradient with each archive Fisher | 0.9999 |
| Own diagonal Fisher | 0.9995 |
| Identity geometry | 0.9991 |

Using a common Fisher still leaves the enthalpy result close to its own-Fisher result, whereas using a common gradient gives essentially unit agreement. Residual target-gradient variation therefore remains the source signal. The corrected result adds that the between-state covariance in the old joint Fisher materially amplified that signal enough to turn the 100 ns endpoint from a pass into a fail.

The conditional proposals spend their intended budget coherently. At 100 ns the design-weighted conditional KL is about 0.0091--0.0096 and the maximum conditional KL is 0.01 for every family. Evaluating those same steps with the historical frozen-bias joint metric gives approximately 0.156 for density, 0.010--0.011 for RDF, 0.207--0.314 for enthalpy, and 0.353--0.359 for dielectric. The between-state term contributes about 94% for density, 10--14% for RDF, 96--97% for enthalpy, and 97% for dielectric. This target-direction dependence explains why removing the term changes some directions much more than others.

![[wiki/assets/ffrefine-long-archive-target-gradient-convergence/state-conditional-kl-diagnostics.png]]

*Figure 8. Design-weighted average and maximum state-conditional quadratic KL for each archive, family, and cumulative prefix. The maximum is fixed at the 0.01 safety ceiling; the apparent zero-centered offset in the lower panels is a plotting presentation effect around 0.01.*

The correction is not cosmetic. At 100 ns the Euclidean angle between the old and corrected proposals is large and is even negative for RDF and dielectric, although both proposals remain descent constructions in their respective metrics. Historical finite-step replay results therefore do not validate the new proposal vectors.

![[wiki/assets/ffrefine-long-archive-target-gradient-convergence/fisher-counterfactuals.png]]

*Figure 9. Conditional-Fisher and counterfactual direction agreement for enthalpy and dielectric.*

![[wiki/assets/ffrefine-long-archive-target-gradient-convergence/retained-mode-disagreement.png]]

*Figure 10. Difference between archives in signed Fisher-whitened mode fractions. Persistent enthalpy redistribution across retained modes explains why a nearly aligned raw gradient can yield a less aligned natural direction.*

## Optimizer implication: steepest descent is plausible, not validated

The production natural-gradient direction is schematically

$$
\boldsymbol\Delta_{\mathrm{full}}
=
-\alpha F^{+}\mathbf g.
$$

Inverting retained low-information modes can magnify small archive-specific components of $\mathbf g$. A latent-space steepest-descent direction would instead use

$$
\boldsymbol\Delta_{\mathrm{SD}}
=
-\eta\mathbf g.
$$

This removes Fisher-induced rotation. The Fisher can still define a scalar trust limit without being inverted:

$$
\frac12
\boldsymbol\Delta_{\mathrm{SD}}^\mathsf T
F
\boldsymbol\Delta_{\mathrm{SD}}
\leq
D_{\mathrm{KL}}^{\mathrm{target}}.
$$

This distinction matters because ordinary steepest descent depends on coordinates. Any test must operate in FFRefine's dimensionless latent parameterization, retain the existing physical bounds and regularization, and use the Fisher only for matched KL control. A diagonal-Fisher direction is a useful intermediate arm because it preserves parameter-wise scale information without full cross-parameter mode mixing.

For enthalpy, the corrected 100 ns conditional-Fisher direction now passes, but only 0.014 above the cosine threshold after failing at every earlier prefix. The common-Fisher and common-gradient counterfactuals still show that conditioning amplifies residual gradient differences. Enthalpy's cumulative halves, local blocks, and the archive-2 70–80 ns update show that neither the raw estimator nor the conditional direction is stationary enough to declare trainability.

For dielectric, both raw and conditional-Fisher directions pass at 100 ns, and the conditional direction passes continuously from 40 ns. Its cumulative chronological halves improve markedly but local adjacent blocks remain unstable. The corrected result strengthens the case for a long-budget direction without replacing prospective replay and fresh simulation.

A more reproducible direction is necessary but not sufficient. The current counterfactuals are retrospective fixed-archive diagnostics; they do not show that a finite steepest-descent or diagonal step reduces held-out replay loss, survives empirical-KL backtracking, or improves a fresh candidate simulation.

## Within-archive uncertainty versus between-archive variation

At 100 ns the relative independent-archive vector differences were:

| Family | Objective-gradient relative difference | Natural-direction relative difference |
| --- | ---: | ---: |
| Density | 0.0256 | 0.0288 |
| RDF | 0.0164 | 0.0123 |
| Enthalpy | 0.2512 | 0.3526 |
| Dielectric | 0.2883 | 0.0336 |

Conditional-Fisher preconditioning strongly reduces the dielectric discrepancy and still increases the enthalpy discrepancy, but no longer by more than fourfold. Ten-nanosecond-block jackknife estimates remain substantial for difficult-observable vector components, especially archive-2 enthalpy. These componentwise diagonal uncertainty summaries are diagnostic; they are not a full multivariate covariance estimate and do not turn two archives into a population-level uncertainty estimate.

![[wiki/assets/ffrefine-long-archive-target-gradient-convergence/within-vs-between-uncertainty.png]]

*Figure 11. Within-archive delete-block uncertainty versus independent-archive difference for targets, objective gradients, and natural directions.*

## Updated interpretation

The earlier working model

$$
\widehat{\nabla L}_i
=
\nabla L_{\mathrm{equilibrium}}
+
\eta_i
$$

remains useful, but the 100 ns result shows that the optimizer transforms this error in a target-dependent way. A more operational expression is

$$
\widehat{\Delta\phi}_i
=
-\alpha_i\widehat{F}_i^{+}
\left(\nabla L_{\mathrm{equilibrium}}+\eta_i\right),
$$

where $\widehat{F}_i^{+}$ is the regularized pseudoinverse in the retained Fisher subspace. The two Fisher estimates can span almost exactly the same subspace while that transformation still magnifies a small component of $\eta_i$ for one target family and suppresses it for another.

This resolves the apparent contradiction that a “bad Fisher” should affect density and RDF too. The Fisher is common geometry, not common signal. Density and RDF gradients occupy that geometry reproducibly. Dielectric does so at the longer tested budget. Enthalpy retains enough archive-specific projection in sensitive modes that even the corrected geometry reduces its agreement, although not enough to fail the final endpoint.

The results also reject a categorical explanation based only on “frame observables” versus “average observables.” Density and RDF are themselves estimated from ensembles and were subjected to the same split diagnostics. What separates the families empirically is the convergence of their complete parameter-sensitivity vectors. Slow collective dipole fluctuations provide a plausible mechanism for dielectric, and cancellation-sensitive energetic covariance terms provide a plausible mechanism for enthalpy, but the completed experiment does not isolate individual covariance or autocorrelation contributions well enough to claim either mechanism as uniquely proven.

The main hypothesis is therefore no longer simply “the direct quantities equilibrate before all gradients.” It is:

1. direct target means can converge before covariance-derived parameter sensitivities;
2. raw-gradient orientation and magnitude are separate convergence requirements, and a cosine alone can hide severe norm instability;
3. nested consecutive prefixes, disjoint chronological halves, local adjacent blocks, and independent archives test different questions and are not interchangeable;
4. KL normalization can keep natural-step norm ratios near one while the unscaled gradient norm remains unstable;
5. the same stable Fisher geometry can selectively amplify residual target-gradient error because each target family projects differently into its retained modes;
6. including between-state score-mean covariance in a trust region intended to control state-conditional replay can materially rotate and overconstrain target-dependent proposals;
7. a conditional-Fisher endpoint pass remains an optimizer hypothesis until it transfers through held-out replay and fresh simulation;
8. cumulative agreement between two archives can coexist with poor chronological-half and local-block agreement and therefore requires prospective repetition.

## Historical retrospective Fisher-treatment follow-up

The same two archives were previously reused for a development-only comparison of the production hard inverse, identity, diagonal scaling, continuous damping, and block-derived modal-SNR filtering. That campaign used the old joint-Fisher quadratic while applying state-conditional empirical replay KL. Its observations remain valid for those exact historical proposals, but comparisons advertised as equal-KL treatment comparisons were not conditioning-consistent.

For dielectric, the production hard-Fisher direction passed every recorded retrospective gate: the minimum independent-archive cosine from 60 through 100 ns was 0.9297, both cross-archive paired loss intervals were below zero, pooled proposals improved both archives, and all six target temperatures improved. Damping with $\gamma=10^{-4}$ ranked first, with cross reductions of 1.812% and 1.701%.

For enthalpy, identity and diagonal directions had minimum 60--100 ns cosines of 0.9974 and 0.9415, confirming that avoiding full spectral inversion preserves complete-archive direction agreement. Their realised empirical KL values were only about 0.0007--0.0009, however, and their paired loss intervals were mostly inconclusive. They were not tested at a comparable empirical perturbation.

Small-$\gamma$ enthalpy damping produced a more surprising result. Its exact direction cosine remained poor, but both cross-archive replay reductions were paired-resolved: 1.779% and 2.405% for $\gamma=10^{-4}$. This means the two archive directions can occupy a shared descent cone without being mutually aligned enough to pass the conservative cosine gate. It does not justify weakening the gate after observing the data because the damping strength was selected on this same archive pair.

Mechanistically, $\gamma=10^{-4}$ damping restored two positive normalized Fisher modes near $8.2\times10^{-5}$ and $2.5\times10^{-4}$ that the production $10^{-3}$ hard floor removes. Their gains were approximately 4,902 and 3,438. The improvement is therefore associated with a changed effective subspace, not merely gentler inversion of the existing five retained modes. The modal-SNR filter only reweighted modes above the hard floor and consequently could not test this mechanism.

Nominal quadratic KL also failed to equalise treatments. Although every proposal was scaled to estimated KL 0.005, identity and diagonal proposals realised much smaller empirical KL than hard, damped, and SNR proposals. Future comparisons must match empirical replay KL before interpreting loss-effect size.

The detailed historical screen, paired intervals, component responses, spectral gains, collateral-family effects, and limitations are recorded in [[wiki/answers/ffrefine-retrospective-fisher-treatment-development]]. Its old-geometry ranking was subsequently replaced by a state-conditional rerun before prospective selection.

## Prospective dielectric follow-up

The completed state-conditional treatment campaign found hard full Fisher, damped $\gamma=0.03$ and $0.1$, diagonal, and selected modal-SNR dielectric proposals eligible on the reused archive pair. Hard full Fisher ranked first by fixed-archive replay loss, whereas $\gamma=0.1$ gave stronger direction robustness and was selected prospectively as a smooth full-correlation treatment with lower implementation complexity than modal SNR.

Reaction-field run `20260901-171027` then tested $\gamma=0.1$ in the complete macro pipeline. Two consecutive updates reduced dielectric loss on the next fresh archive with paired intervals below zero, and two final-validation replicas reproduced the best confirmed checkpoint. This validates the long-archive study's central prospective lead: the corrected long-budget dielectric direction can produce real fresh-simulation descent. [[wiki/answers/ffrefine-prospective-dielectric-damped-fisher-training]]

The run also confirmed the temporal warning. A fourth macro archive passed direct dielectric splitting but failed damped half-direction agreement with cosine 0.657. The long-archive cumulative result therefore predicted a viable treatment without establishing a universal per-epoch sampling time.

## What this establishes

- The corrected reaction-field pipeline produces a reproducible dielectric conditional-Fisher direction from 40–100 ns in this realization.
- The 10 ns budget was genuinely insufficient for dielectric under this matched setup; its failure was not evidence of a formula error.
- At the 100 ns independent-archive endpoint, enthalpy passes both the raw and corrected conditional-Fisher gates, but the conditional cosine is only 0.814 and every earlier endpoint fails.
- The historical 0.629 enthalpy failure was materially worsened by the mismatched between-state covariance term; residual target-gradient variation remains the source signal.
- Archive-2 enthalpy remains temporally unstable before Fisher preconditioning: adding 10 ns to the 70 ns cumulative prefix reduced the raw-gradient norm by about 64% and rotated the vector despite substantial sample overlap.
- Full Fisher coupling can amplify difficult-target instability, but it is not its sole origin; the raw-gradient estimator itself can remain unstable after direct means appear converged.
- Direct target values, raw gradients, and natural directions have different convergence times and must be monitored separately.
- Historical joint-Fisher dielectric and damped-enthalpy proposals gave supported cross-archive replay descent on this archive pair, but those effects do not validate the corrected conditional proposals.
- A corrected conditional-Fisher damped dielectric treatment has now produced two paired-confirmed fresh macro updates and reproducible final-validation loss in one prospective campaign.

## What this does not establish

- that 40 ns is a universal or unbiased dielectric budget estimate;
- that two archives characterize the population distribution of directions;
- that the observed dielectric success rate will repeat across new campaign seeds;
- that every fresh archive at the tested 60 ns budget will produce an optimization-ready direction;
- that any conditional-Fisher treatment is a validated enthalpy optimiser under held-out replay or fresh simulation;
- that enthalpy would not converge with more independent information or a prospectively specified geometry;
- that a smooth pooled nested-prefix curve, a high gradient cosine without a compatible norm, or a near-unit KL-scaled natural-step norm ratio establishes gradient equilibrium;
- that identity or diagonal conditioning trains enthalpy or dielectric; the current comparisons are retrospective direction diagnostics only.

## Required next evidence

1. Repeat the independent long-archive comparison with new seeds and the same predeclared conditional-Fisher settings. Do not select a minimum archive length retrospectively from the observed 40 ns dielectric or 100 ns enthalpy crossings.
2. Require agreement across more than one archive pair and report, for every target, independent-archive agreement, cumulative disjoint halves, local adjacent blocks, and consecutive cumulative-prefix updates.
3. For every comparison, report raw-gradient cosine, both absolute norms, and their norm ratio before reporting the KL-scaled natural direction. Do not use pooled nested self-convergence or a near-unit natural-step norm ratio as equilibrium evidence.
4. Retain the completed conditional-Fisher treatment campaign as development evidence; do not retune the prospectively selected $\gamma=0.1$ on run `20260901-171027`.
5. Separate fresh checkpoint assessment from readiness to construct the next direction, so a direction failure cannot erase an otherwise valid paired candidate evaluation. [[wiki/questions/QST-0007-checkpoint-assessment-versus-next-direction-readiness]]
6. For enthalpy, distinguish an isolated endpoint crossing from repeatable trainability using new archive pairs and predeclared conditional-Fisher treatment arms.
7. Apply identical latent-parameter bounds and an identical empirical-KL budget to all optimizer arms. In the identity arm, use the Fisher only to scale or backtrack the step, not to rotate it.
8. Evaluate every frozen arm on independent held-out long archives before fresh simulation. A raw-direction cosine and norm-ratio pass is a prerequisite, not evidence that a finite step reduces population loss.
9. Separate the raw-physical-Fisher validity tolerance from the Jacobi-normalized optimizer eigenvalue floor; report both explicitly.
10. Report the retained normalized spectrum, retained condition number, and each target gradient's signed retained-mode coefficients with block uncertainty. Rank and subspace overlap alone do not quantify inverse amplification.
11. Treat $\gamma=10^{-4}$ as a retrospective finalist, not a validated constant. Do not retune it on the prospective archive pair.

## Links

- [[wiki/answers/ffrefine-prospective-dielectric-damped-fisher-training]]
- [[wiki/answers/ffrefine-retrospective-fisher-treatment-development]]
- [[wiki/answers/ffrefine-average-observable-trainability-validation]]
- [[wiki/claims/CLM-0038-fixed-archive-gradient-validation-does-not-establish-fresh-archive-trainability]]
- [[wiki/questions/QST-0006-average-observable-trainability-sampling-budget]]
- [[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]
- [[wiki/concepts/dipole-moment-fluctuation-dielectric-constant]]
- [[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]
- [[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]
- [[wiki/sources/SRC-0023-statistically-optimal-analysis-multiple-equilibrium-states-mbar]]
