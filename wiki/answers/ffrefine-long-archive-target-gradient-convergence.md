---
type: answer
status: active
created: 2026-08-26
updated: 2026-08-26
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
---

# FFRefine Long-Archive Target-Gradient Convergence

## Short answer

Two independently prepared 100 ns reaction-field TSS archives substantially changed the diagnosis, but did not establish closed-loop trainability.

Density and RDF remained positive controls: their objective gradients and natural-gradient directions agreed across independent archives at every cumulative prefix from 10 through 100 ns. Dielectric was initially unstable but its cumulative independent-archive natural direction passed the predeclared cosine and norm-ratio gate continuously from 60 through 100 ns. At 100 ns its Fisher-metric cosine was 0.9743 and its norm ratio was 1.0028.

Enthalpy behaved differently. Its raw objective-gradient cosine rose to 0.9691 at 100 ns, but the production natural-gradient cosine remained only 0.6288. The retained Fisher subspaces were effectively identical, and imposing a common gradient while keeping each archive's Fisher gave unit agreement. The Fisher estimate was therefore not varying materially between archives; rather, full Fisher preconditioning amplified the remaining target-specific enthalpy-gradient difference.

The accompanying norm ratios sharpen this result. At 100 ns, enthalpy's independent-archive raw cosine and norm ratio were 0.9691 and 0.9655, whereas its Fisher-conditioned cosine and norm ratio were 0.6288 and 0.9989. Dielectric passed both representations: raw 0.9777 and 0.8204; Fisher-conditioned 0.9743 and 1.0028. This makes latent-space steepest descent or diagonal conditioning a justified **prospective hypothesis for enthalpy**, but not a validated replacement optimizer. For dielectric, the same endpoint does not implicate full Fisher conditioning; longer sampling is the clearer change.

The direct target values looked converged much earlier than this distinction became visible. At 100 ns, the root-mean-square independent-archive target differences were only 0.159, 0.171, 0.305, and 0.082 target-tolerance units for density, RDF, enthalpy, and dielectric respectively. Stable observable means were therefore neither sufficient to establish a stable natural direction nor diagnostic of which target family would pass.

A finer temporal decomposition strengthens that warning. In archive 2, extending the cumulative enthalpy estimate from 70 to 80 ns left its raw-gradient cosine apparently high at 0.8876, but reduced the raw-gradient norm from 239.3 to 85.7, a ratio of 0.3582. The corresponding KL-scaled natural-step norm ratio remained 0.9975. Thus a nearly fixed optimizer step length can conceal a large change in the underlying estimated gradient.

The result supports a prospective long-archive dielectric validation campaign. It does **not** establish that 60 ns is a universal minimum, that the 100 ns dielectric direction will repeat across additional archive pairs, that chronological halves are equilibrated, or that a replay improvement will survive fresh simulation.

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

The physical-coordinate Fisher condition estimate remained large, approximately $6.6\times10^7$ to $6.9\times10^7$, but every endpoint retained the same five modes. This experiment therefore does not support incomplete ladder coverage, rejected replay support, or archive-dependent retained Fisher rank as explanations for the target-family separation.

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
| Density | 0.999997 | 1.0258 | 0.999930 | 0.9979 | yes |
| RDF | 0.999998 | 0.9839 | 0.999793 | 1.0080 | yes |
| Enthalpy | 0.969050 | 0.9655 | 0.628810 | 0.9989 | no |
| Dielectric | 0.977708 | 0.8204 | 0.974299 | 1.0028 | yes |

The cumulative time series adds important context:

- density and RDF passed at every prefix from 10 through 100 ns;
- dielectric passed at 40 ns, failed again at 50 ns, and then passed at every prefix from 60 through 100 ns;
- enthalpy did not pass the production natural-direction gate at any prefix;
- norm ratios remained close to one, so the difficult-family failures were predominantly angular rather than step-length failures.

![[wiki/assets/ffrefine-long-archive-target-gradient-convergence/independent-archive-direction-convergence.png]]

*Figure 3. Independent-archive cosine and norm ratio before and after Fisher conditioning. The raw-gradient norm uses the Euclidean latent-space metric; the natural-step norm uses the averaged Fisher metric. Fisher preconditioning separates enthalpy from the other families.*

![[wiki/assets/ffrefine-long-archive-target-gradient-convergence/direction-acceptance-heatmap.png]]

*Figure 4. Prospective natural-direction gate over cumulative archive length. “Sustained from 60 ns” describes this one dielectric archive pair; it is not a universal sampling threshold.*

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
| Enthalpy | 0.950 | 0.168 |
| Dielectric | 0.451 | 0.269 |

Thus the two cumulative dielectric directions can agree while 50 ns halves within each archive remain noisy. This does not invalidate the cumulative result, but it prevents treating two-archive agreement as proof of equilibration. Conversely, enthalpy can look stable in one archive and fail in the other. Both chronological and independent axes must remain visible.

Archive 2 enthalpy illustrates why both orientation and magnitude are required:

| Prefix | Raw-gradient cosine | Raw norm ratio | Natural-direction cosine | Natural norm ratio |
| --- | ---: | ---: | ---: | ---: |
| 70 ns halves | 0.8964 | 0.2524 | 0.8449 | 0.9855 |
| 80 ns halves | -0.9654 | 0.8868 | 0.2114 | 0.9977 |

At 70 ns, the high raw-gradient cosine alone is misleading because the two half-gradient norms differ by almost a factor of four. At 80 ns, the two cumulative halves point in nearly opposite raw-gradient directions. The near-unit natural-step norm ratios do not rescue these comparisons because KL scaling deliberately normalizes the final step magnitude.

The local diagnostic is stricter and noisier. All local enthalpy pairs failed the target-family split-validity check, so their plotted crosses are diagnostic values rather than accepted estimates. At 100 ns, even the valid dielectric local natural directions remained incompatible: their cosines were -0.459 and 0.190 in archives 1 and 2, with norm ratios 0.996 and 1.032. Similar final step lengths therefore coexisted with different recent-block directions.

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

FFRefine does not invert the physical-coordinate Fisher matrix directly. The implementation first applies the parameterization chain rule,

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

A final scalar enforces the Fisher-estimated KL budget. It changes step length but cannot change the direction cosine. With one active target family and disabled parameter regularization, the ConFIG path reduces algebraically to this same truncated natural step. Momentum was disabled in the reproducibility campaigns. ConFIG and momentum therefore did not cause the observed single-family archive disagreement, although both can matter later in multi-target or multi-epoch production.

An implementation audit found this sequence algebraically consistent: the physical-to-latent chain rule, Jacobi transformation, retained-mode inverse, and KL rescaling match their intended definitions. The result should therefore be described as a **Jacobi-scaled, hard-truncated, ridge-regularized natural metric**, not as an unqualified inverse of the raw Fisher matrix.

### What the regularization removes and what it leaves

At 100 ns the two archives had nearly identical normalized spectra. Representative eigenvalues were

$$
(10^{-12},10^{-12},10^{-12},
8\times10^{-5},2.5\times10^{-4},
0.0043,0.0195,0.075,0.61,9.29).
$$

The $10^{-3}$ floor removed the first five modes and retained modes 6 through 10 in both archives. Their retained subspaces were essentially identical, so threshold crossings, archive-dependent rank, and unstable retained eigenvectors are not supported explanations for this experiment.

The retained geometry nevertheless remained strongly anisotropic. Its condition number was about 2,100, corresponding to an inverse-weight spread of about 2,100 and a whitening-weight spread of about 46. Jacobi scaling was useful because the latent Fisher diagonal itself spanned a factor of about 2,584; without it, parameter units and marginal scale would dominate the eigendecomposition. Jacobi scaling is therefore not identified as an error. Once truncation is applied, however, it defines the normalized modes on which regularization acts and is consequently part of the optimizer design rather than a neutral numerical rearrangement.

The $10^{-8}$ ridge prevents numerical singularity but is too small to provide meaningful statistical damping of retained modes beginning near $0.0043$. The hard eigenvalue floor removes the near-null space but does not prevent appreciable amplification within the retained space.

The target-specific mode projections explain why the same operator affects families differently. Density and RDF placed reproducible proportions of their gradients into the same retained modes in both archives. For 100 ns enthalpy, mode 6 near eigenvalue 0.0043 was aligned; the disagreement instead came mainly from redistribution and a sign change in modes 7 and 8, near eigenvalues 0.0195 and 0.075. Full cross-parameter coupling made those residual differences decisive. It is therefore too crude to say that the single smallest retained mode caused the failure.

The predefined floor sweep also did not provide a simple repair. Enthalpy's independent-archive cosine was 0.711 at floor $10^{-4}$, 0.629 at the production floor $10^{-3}$, and 0.225 at floor $10^{-2}$. Raising the floor removed the well-aligned mode 6 and worsened agreement. This proves sensitivity to spectral regularization but does not justify selecting a floor retrospectively from this realization. Dielectric remained accepted at 100 ns across the tested floors.

One configuration issue should be corrected independently of the scientific conclusion: the same numerical setting, `fisher_min_eigenvalue_tolerance`, is currently used both as an absolute negative-eigenvalue tolerance for validating the raw physical Fisher and as a positive-mode truncation floor for the Jacobi-normalized latent Fisher. These are distinct decisions in different coordinate systems and should have separate names and settings.

The durable interpretation is therefore not that the Fisher implementation is mathematically broken. Residual target-gradient sampling error is the source signal, while the retained full off-diagonal Fisher geometry and its present spectral filter can amplify that error. A target-independent eigenvalue cutoff cannot distinguish stable density/RDF modal coefficients from noisy enthalpy coefficients. Prospective comparisons should therefore include continuous spectral damping or uncertainty-aware modal filtering, in addition to full, diagonal, and identity geometry, under identical latent coordinates and empirical-KL control.

At 100 ns both archives retained five Fisher modes, with minimum principal cosine and normalized projector overlap numerically indistinguishable from one at the reported precision. Counterfactual directions localize the enthalpy failure:

| Enthalpy variant at 100 ns | Metric cosine |
| --- | ---: |
| Raw objective gradient | 0.9691 |
| Each gradient with its own full Fisher | 0.6288 |
| Each gradient with the common averaged Fisher | 0.6240 |
| Common averaged gradient with each archive Fisher | approximately 1.0000 |
| Own diagonal Fisher | 0.9995 |
| Identity geometry | 0.9998 |

Using the same Fisher does not repair enthalpy, whereas using the same gradient does. The archive-specific Fisher matrices are not producing different geometries. Instead, small residual differences in the target-dependent gradient are projected differently through the same ill-conditioned retained geometry. The diagonal and identity counterfactuals show that the pathology is specific to full Fisher coupling, but they are diagnostic alternatives, not retrospectively validated replacement optimizers.

Dielectric shows the complementary outcome: by 100 ns its raw gradient and full-Fisher direction both agree, and its result is stable across the predefined eigenvalue floors. Longer sampling appears to have reduced its gradient error enough that Fisher preconditioning no longer rotates the two archive directions apart.

![[wiki/assets/ffrefine-long-archive-target-gradient-convergence/fisher-counterfactuals.png]]

*Figure 8. Full-Fisher and counterfactual direction agreement for enthalpy and dielectric.*

![[wiki/assets/ffrefine-long-archive-target-gradient-convergence/retained-mode-disagreement.png]]

*Figure 9. Difference between archives in signed Fisher-whitened mode fractions. Persistent enthalpy redistribution across retained modes explains why a nearly aligned raw gradient can yield a poorly aligned natural direction.*

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

For enthalpy, the 100 ns independent-archive endpoint supports this experiment: the raw direction passes the cosine and norm-ratio gate, while the full-Fisher direction fails. The common-Fisher and common-gradient counterfactuals further localize the loss of reproducibility to full preconditioning of residual gradient differences. However, enthalpy's cumulative halves, local blocks, and the archive-2 70–80 ns update show that the raw estimator itself is not stationary enough to declare trainability.

For dielectric, both raw and full-Fisher directions pass at 100 ns. The evidence therefore does not identify full preconditioning as its long-budget obstacle. Its earlier failures are more consistent with insufficient independent information about slowly mixing dipole fluctuations. Identity or diagonal conditioning may still be useful controls, but they cannot substitute for sampling.

A more reproducible direction is necessary but not sufficient. The current counterfactuals are retrospective fixed-archive diagnostics; they do not show that a finite steepest-descent or diagonal step reduces held-out replay loss, survives empirical-KL backtracking, or improves a fresh candidate simulation.

## Within-archive uncertainty versus between-archive variation

At 100 ns the relative independent-archive vector differences were:

| Family | Objective-gradient relative difference | Natural-direction relative difference |
| --- | ---: | ---: |
| Density | 0.0256 | 0.0212 |
| RDF | 0.0164 | 0.0158 |
| Enthalpy | 0.2512 | 1.0802 |
| Dielectric | 0.2883 | 0.0802 |

Fisher preconditioning reduces the dielectric discrepancy but amplifies the enthalpy discrepancy by more than fourfold. Ten-nanosecond-block jackknife estimates remain substantial for difficult-observable vector components, especially archive-2 enthalpy. These componentwise diagonal uncertainty summaries are diagnostic; they are not a full multivariate covariance estimate and do not turn two archives into a population-level uncertainty estimate.

![[wiki/assets/ffrefine-long-archive-target-gradient-convergence/within-vs-between-uncertainty.png]]

*Figure 10. Within-archive delete-block uncertainty versus independent-archive difference for targets, objective gradients, and natural directions.*

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

This resolves the apparent contradiction that a “bad Fisher” should affect density and RDF too. The Fisher is common geometry, not common signal. Density and RDF gradients occupy that geometry reproducibly. Dielectric eventually does so at the longer tested budget. Enthalpy retains enough archive-specific projection in sensitive modes that the same geometry amplifies rather than repairs it.

The results also reject a categorical explanation based only on “frame observables” versus “average observables.” Density and RDF are themselves estimated from ensembles and were subjected to the same split diagnostics. What separates the families empirically is the convergence of their complete parameter-sensitivity vectors. Slow collective dipole fluctuations provide a plausible mechanism for dielectric, and cancellation-sensitive energetic covariance terms provide a plausible mechanism for enthalpy, but the completed experiment does not isolate individual covariance or autocorrelation contributions well enough to claim either mechanism as uniquely proven.

The main hypothesis is therefore no longer simply “the direct quantities equilibrate before all gradients.” It is:

1. direct target means can converge before covariance-derived parameter sensitivities;
2. raw-gradient orientation and magnitude are separate convergence requirements, and a cosine alone can hide severe norm instability;
3. nested consecutive prefixes, disjoint chronological halves, local adjacent blocks, and independent archives test different questions and are not interchangeable;
4. KL normalization can keep natural-step norm ratios near one while the unscaled gradient norm remains unstable;
5. the same stable Fisher geometry can selectively amplify residual target-gradient error because each target family projects differently into its retained modes;
6. avoiding Fisher inversion may preserve a reproducible enthalpy endpoint direction, but this remains an optimizer hypothesis until it transfers to held-out archives and fresh simulation;
7. cumulative agreement between two archives can coexist with poor chronological-half and local-block agreement and therefore requires prospective repetition.

## What this establishes

- The complete reaction-field pipeline can produce a reproducible dielectric natural direction when cumulative independent archives reach 60–100 ns in this realization.
- The 10 ns budget was genuinely insufficient for dielectric under this matched setup; its failure was not evidence of a formula error.
- Enthalpy's remaining 100 ns failure is localized to the interaction between residual target-gradient variation and full Fisher preconditioning, not archive-dependent Fisher rank or subspace.
- At the 100 ns independent-archive endpoint, enthalpy passes the raw cosine and norm-ratio gate but fails after full Fisher preconditioning; dielectric passes both raw and full-Fisher comparisons.
- Archive-2 enthalpy remains temporally unstable before Fisher preconditioning: adding 10 ns to the 70 ns cumulative prefix reduced the raw-gradient norm by about 64% and rotated the vector despite substantial sample overlap.
- Full Fisher coupling can amplify difficult-target instability, but it is not its sole origin; the raw-gradient estimator itself can remain unstable after direct means appear converged.
- Direct target values, raw gradients, and natural directions have different convergence times and must be monitored separately.

## What this does not establish

- that 60 ns is a universal or unbiased dielectric budget estimate;
- that two archives characterize the population distribution of directions;
- that the dielectric direction will reduce paired replay loss under a strict empirical-KL ceiling;
- that the direction will survive fresh candidate simulation or macro-epoch resimulation;
- that diagonal or identity preconditioning is a validated enthalpy optimizer;
- that enthalpy would not converge with more independent information or a prospectively specified geometry;
- that a smooth pooled nested-prefix curve, a high gradient cosine without a compatible norm, or a near-unit KL-scaled natural-step norm ratio establishes gradient equilibrium;
- that identity or diagonal conditioning trains enthalpy or dielectric; the current comparisons are retrospective direction diagnostics only.

## Required next evidence

1. Repeat the independent long-archive comparison with new seeds and the same predeclared full-Fisher settings. Do not select the minimum archive length retrospectively from the observed 60 ns crossing.
2. Require agreement across more than one archive pair and report, for every target, independent-archive agreement, cumulative disjoint halves, local adjacent blocks, and consecutive cumulative-prefix updates.
3. For every comparison, report raw-gradient cosine, both absolute norms, and their norm ratio before reporting the KL-scaled natural direction. Do not use pooled nested self-convergence or a near-unit natural-step norm ratio as equilibrium evidence.
4. If dielectric repeats, freeze a pooled long-archive direction before validation, leave margin below the empirical-KL ceiling, and report paired replay-loss uncertainty on held-out long archives.
5. Only after replay, support, KL, and direction gates pass should the dielectric candidate advance to independent fresh simulation.
6. For enthalpy, distinguish “more sampling” from “different optimizer geometry” with a prospective comparison of full Fisher, diagonal Fisher, and identity directions computed from the same complete pooled gradient.
7. Apply identical latent-parameter bounds and an identical empirical-KL budget to all optimizer arms. In the identity arm, use the Fisher only to scale or backtrack the step, not to rotate it.
8. Evaluate every frozen arm on independent held-out long archives before fresh simulation. A raw-direction cosine and norm-ratio pass is a prerequisite, not evidence that a finite step reduces population loss.
9. Separate the raw-physical-Fisher validity tolerance from the Jacobi-normalized optimizer eigenvalue floor; report both explicitly.
10. Report the retained normalized spectrum, retained condition number, and each target gradient's signed retained-mode coefficients with block uncertainty. Rank and subspace overlap alone do not quantify inverse amplification.
11. Compare the hard truncated inverse with a prospectively specified continuously damped or uncertainty-aware spectral filter. Do not select its damping strength from the observed archive pair.

## Links

- [[wiki/answers/ffrefine-average-observable-trainability-validation]]
- [[wiki/claims/CLM-0038-fixed-archive-gradient-validation-does-not-establish-fresh-archive-trainability]]
- [[wiki/questions/QST-0006-average-observable-trainability-sampling-budget]]
- [[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]
- [[wiki/concepts/dipole-moment-fluctuation-dielectric-constant]]
- [[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]
- [[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]
- [[wiki/sources/SRC-0023-statistically-optimal-analysis-multiple-equilibrium-states-mbar]]
