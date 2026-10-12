---
type: answer
status: active
created: 2026-07-02
updated: 2026-10-12
question: "Can the AWH frozen-bias replay force-field optimization idea be tested with Times Square Sampling and MBAR, and what machinery is common versus method-specific?"
answer_status: answered
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/molecular-simulation/free-energy
  - research/adaptive-sampling
  - research/statistics/monte-carlo
  - research/scientific-computing
tags:
  - force-field-optimization
  - replay-reweighting
  - times-square-sampling
  - mbar
  - awh
  - implementation-route
related:
  - "[[wiki/answers/ffrefine-direction-gates-and-production-policy]]"
  - "[[wiki/answers/ffrefine-config-vs-weighted-sum-water-campaign-results]]"
  - "[[wiki/answers/ffrefine-average-observable-trainability-validation]]"
  - "[[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]"
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
  - "[[wiki/concepts/times-square-sampling]]"
  - "[[wiki/concepts/tss-implementation-patterns]]"
  - "[[wiki/concepts/multistate-bennett-acceptance-ratio]]"
  - "[[wiki/concepts/free-energy-reweighting-for-force-field-fine-tuning]]"
  - "[[wiki/concepts/tolerance-normalized-multi-observable-losses]]"
  - "[[wiki/answers/ffrefine-current-implementation-status]]"
  - "[[wiki/answers/ffrefine-paper-methods-knowledge-base]]"
  - "[[wiki/answers/ffrefine-water-temperature-replay-fresh-loss-gap]]"
  - "[[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]"
  - "[[wiki/questions/force-field-training-validation-scope]]"
  - "[[wiki/claims/CLM-0038-fixed-archive-gradient-validation-does-not-establish-fresh-archive-trainability]]"
  - "[[wiki/claims/CLM-0039-trust-region-kl-must-match-replay-conditioning]]"
  - "[[wiki/claims/CLM-0040-damped-conditional-fisher-dielectric-training-survives-fresh-resimulation]]"
  - "[[wiki/questions/QST-0006-average-observable-trainability-sampling-budget]]"
  - "[[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]"
  - "[[wiki/answers/ffrefine-kl-definition-for-extended-ensemble-training]]"
  - "[[wiki/answers/adding-config-optimiser-to-ffrefine]]"
  - "[[wiki/answers/ffrefine-loss-gate-diagnostic-policy]]"
  - "[[wiki/claims/CLM-0044-config-must-exclude-directionally-unreliable-families]]"
  - "[[wiki/tensions/TEN-0020-config-family-exclusion-versus-untreated-drift]]"
  - "[[wiki/answers/ffrefine-improved-gates-water-run-lessons]]"
  - "[[wiki/answers/ffrefine-multi-series-equilibration-cut-calibration]]"
  - "[[wiki/claims/CLM-0047-calibrated-materiality-threshold-prevents-multi-series-equilibration-over-cutting]]"
  - "[[wiki/claims/CLM-0048-family-weight-renormalisation-changes-natural-gradient-step-length]]"
  - "[[wiki/answers/ffrefine-generalist-package-plan-decisions]]"
  - "[[wiki/answers/ffrefine-decision-register]]"
  - "[[wiki/answers/tss-mbar-replay-phased-implementation-plan]]"
sources:
  - SRC-0005
  - SRC-0006
  - SRC-0007
  - SRC-0009
  - SRC-0018
  - SRC-0023
sensitivity: public
encryption: none
wiki_pages_used:
  - "[[wiki/index]]"
  - "[[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]"
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
  - "[[wiki/concepts/accelerated-weight-histogram-method]]"
  - "[[wiki/concepts/times-square-sampling]]"
  - "[[wiki/concepts/tss-implementation-patterns]]"
  - "[[wiki/concepts/multistate-bennett-acceptance-ratio]]"
  - "[[wiki/concepts/on-the-fly-estimation-versus-mbar]]"
  - "[[wiki/concepts/free-energy-reweighting-for-force-field-fine-tuning]]"
  - "[[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]"
  - "[[wiki/questions/force-field-training-validation-scope]]"
  - "[[wiki/answers/sample-bias-reweighting-method-comparison]]"
  - "[[wiki/answers/ffrefine-current-implementation-status]]"
raw_sources_consulted:
  - raw/sources/SRC-0018-force-field-optimization-via-awh-gradients.pdf
wiki_pages_updated:
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
  - "[[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]]"
  - "[[wiki/answers/ffrefine-improved-gates-water-run-lessons]]"
  - "[[wiki/answers/ffrefine-multi-series-equilibration-cut-calibration]]"
graph_neighborhoods_used:
  - "tools/query_graph.py --start wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients.md --depth 1"
scope: timeless
---

# Testing Replay Force-Field Optimization With TSS and MBAR

## Short answer

Yes, it is feasible as an implementation experiment, but the clean way to do it is to preserve the core idea of SRC-0018 as a sampler-agnostic replay optimizer rather than to treat AWH, TSS, and MBAR as interchangeable algorithms. The reusable core is: generate or define a supported reference ensemble, freeze or otherwise fix the reference distribution, replay stored frames under candidate force-field parameters, assemble free-energy and observable losses with gradients, enforce support diagnostics, and take Fisher/KL-controlled parameter steps. [SRC-0018]

In that decomposition, AWH is one reference-ensemble generator. TSS can be another adaptive extended-ensemble generator if its adaptation is frozen before production and if the implementation exports the exact fixed reference density or local window denominator used for replay. [SRC-0005] [SRC-0006] MBAR is different: it is primarily a fixed-sample estimator, not an adaptive sampler. It can provide a strong baseline or a reference-mixture estimator when samples have already been collected from known states, but a separate sampling schedule must generate those samples. [SRC-0023]

The first test should therefore compare three adapters behind one common optimizer:

| Variant | Main role in the route plan | Practical interpretation |
| --- | --- | --- |
| AWH replay | Existing adaptive reference generator and frozen-bias replay baseline | Keep as the control implementation from SRC-0018. |
| TSS replay | Alternative adaptive reference generator | Test whether TSS windows, visit control, and self-adjustment produce a better replay archive for the same optimizer. |
| MBAR replay | Fixed-sample estimator/reference-mixture baseline | Test how far a nonadaptive MBAR-style archive can carry the same parameter updates before overlap or ESS fails. |

## Feasibility judgement

The AWH-to-TSS extension is conceptually feasible because both methods create extended ensembles over configurations and discrete rungs, use conditional probabilities or local rung weights, and maintain free-energy estimates during sampling. AWH learns a bias from conditional weight histograms, whereas TSS uses stochastic approximation, visit control, and possibly windowed local estimates stitched into a global profile. [SRC-0007] [SRC-0009] [SRC-0005] [SRC-0006]

The important implementation constraint is stationarity. SRC-0018 deliberately avoids optimizing from actively adapting AWH data; it freezes the bias, collects production frames, and then replays those frames offline. [SRC-0018] The same rule should be applied to TSS: use adaptive TSS to reach a useful broad reference, then freeze the estimates and collect a production archive under a known fixed kernel before using the frames for optimization. This is an inference from SRC-0018's frozen-reference separation and from TSS's adaptive estimator structure. [SRC-0018] [SRC-0005] [SRC-0006]

The MBAR route is feasible but answers a different question. MBAR can analyze samples from multiple known equilibrium or biased states using all cross-evaluated reduced potentials. [SRC-0023] It does not by itself decide where to sample next. For force-field optimization, the safest MBAR interpretation is to keep the actual sampling distributions fixed as the reference mixture, solve or store their reference normalization constants, and evaluate candidate force-field states as reweighted target states. This keeps the statistical meaning aligned with the samples that were actually drawn. [SRC-0023] [SRC-0018]

The main risk for all three variants is not deriving a weight formula; it is trusting a parameter update outside the support of the reference archive. The wiki already records this as a cross-source claim for reweighting-based force-field fine-tuning. [SRC-0016] [SRC-0018] [SRC-0019] [SRC-0020] [[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]

## Common inner machinery

All three routes should share the following internal layers.

### 1. Target and loss layer

Represent each training objective as a target object with a prediction, reference value, tolerance, and priority weight. SRC-0018 already supports thermodynamic-cycle targets and state-observable targets, then combines them through tolerance-normalized Huber losses rather than raw-unit residuals. [SRC-0018]

When one objective contains target families with very different counts, such as a temperature-dependent density curve and hundreds of RDF bins, normalize within each family before applying configurable between-family coefficients. This preserves unit invariance and prevents the family with more bins from dominating by cardinality alone. Within-family weights can still emphasize scientifically important regions such as RDF peaks. See [[wiki/concepts/tolerance-normalized-multi-observable-losses]].

This layer should not know whether the samples came from AWH, TSS, or MBAR. It should ask for:

- a target free energy or observable estimate,
- its latent-parameter gradient,
- support diagnostics for the estimate,
- split or uncertainty diagnostics for acceptance.

### 2. Parameterization and energy-gradient layer

Keep the bounded or constrained parameter maps from latent optimizer coordinates $\phi$ into physical force-field parameters $\theta$, and apply the chain rule to energy gradients. SRC-0018 uses this to keep parameter families inside valid ranges and to assemble latent-space loss gradients and Fisher matrices. [SRC-0018]

This layer is common to all sampler choices. The sampler only changes which frames and reference weights are used.

### 3. Reference archive layer

Store a method-neutral production archive:

- coordinates, volumes when needed, and possibly velocities if restart logic uses them,
- visited state index and, for TSS, visited window index,
- reference reduced potentials under the actual fixed sampling distribution,
- all candidate-state reduced potentials needed for replay,
- per-frame parameter-energy gradients at target states and visited states,
- enough metadata to reconstruct the log reference mixture for every retained frame.

The critical interface is a method-specific function:

$$
\log q_{\mathrm{ref}}^*(x_n,V_n)
$$

where $q_{\mathrm{ref}}^*$ is the unnormalized marginal density of the fixed reference archive over configuration and volume. In SRC-0018 this is the frozen AWH mixture normalizer. [SRC-0018]

### 4. Replay estimator layer

Given a target state $m$, candidate parameters $\theta$, and a retained frame $n$, compute the unnormalized target replay weight

$$
a_{n,m}(\theta)
=
\exp[-u_m(x_n,V_n;\theta)-\log q_{\mathrm{ref}}^*(x_n,V_n)].
$$

The additive-constant-free free energy is

$$
\tilde F_m(\theta)=-\log\sum_n a_{n,m}(\theta),
$$

and the normalized replay weight is

$$
W_{n,m}(\theta)=\frac{a_{n,m}(\theta)}{\sum_j a_{j,m}(\theta)}.
$$

The endpoint-gradient formula then remains the SRC-0018 replay formula:

$$
\nabla_\theta \tilde F_m(\theta)
=
\sum_n W_{n,m}(\theta)\nabla_\theta u_m(x_n,V_n;\theta).
$$

[SRC-0018]

For an observable $O_m$, the replay estimate is

$$
\hat O_m(\theta)=\sum_n W_{n,m}(\theta)O_m(x_n,V_n;\theta),
$$

with a covariance-like gradient correction when the observable itself is not the only parameter-dependent term. SRC-0018 derives this for arbitrary replayed observables. [SRC-0018]

### 5. Candidate-ensemble support and Fisher layer

Separate target-state replay weights from candidate-ensemble weights. SRC-0018 uses target-state weights for endpoint free energies and observables, but candidate-ensemble weights for ESS and empirical Fisher estimation. [SRC-0018]

For every retained frame, compute an importance ratio from the fixed reference archive into the current candidate ensemble. Then compute:

- Kish ESS or ESS ratio,
- weighted score covariance as an empirical Fisher matrix,
- split-half disagreement in predictions and gradients,
- per-state or per-window support coverage.

The Fisher matrix remains the local KL metric because SRC-0018 derives it as the covariance of reduced-potential gradients under the candidate ensemble. [SRC-0018]

### 6. Optimizer and resimulation policy

A 2026-08-29 FFRefine design analysis distinguishes two KL geometries that should no longer be conflated. When the thermodynamic-state density $\gamma_s$ is prescribed by the enhanced-sampling design and is expected to be restored after a force-field update, the scientific ensemble is $\pi_\theta(s,x)=\gamma_s p_\theta(x\mid s)$. Its Fisher is the weighted state-conditional covariance

$$
F_{\mathrm{cond}}
=
\sum_s\gamma_s\operatorname{Cov}_{p_\theta(x\mid s)}
[\nabla_\phi u_{\theta,s}(x)].
$$

This should define proposal orientation, while the maximum state-conditional candidate-to-reference KL and state-wise ESS should control finite replay steps. By contrast, the covariance over the state-labelled frozen-bias mixture also contains the between-state covariance of mean scores. It measures the change in joint state occupancy if the old bias remains frozen. That remains a useful bias-portability diagnostic, but it should not be treated as equivalent to state-normalized replay KL. This is a project design recommendation supported by the 2026-08-29 conditioning analysis; its prospective evidence is limited to the dielectric-only reaction-field training recorded in [[wiki/claims/CLM-0040-damped-conditional-fisher-dielectric-training-survives-fresh-resimulation]]. See [[wiki/answers/ffrefine-kl-definition-for-extended-ensemble-training]] and [[wiki/claims/CLM-0039-trust-region-kl-must-match-replay-conditioning]].

Keep the SRC-0018 update logic as the common optimizer:

- assemble tolerance-normalized loss and latent gradient,
- build the empirical Fisher metric,
- apply diagonal regularization when configured,
- apply Jacobi preconditioning,
- eigentruncate weakly informed directions,
- scale to a KL target,
- line-search with ESS, drift, and objective gates,
- resimulate when support or readiness fails. [SRC-0018]

The route plan should treat resimulation as normal, not exceptional. A reweighting-based update is only intended to move within a local trust region supported by the current archive. [SRC-0018] [[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]

## What differs among AWH, TSS, and MBAR

### AWH adapter

AWH samples a joint distribution over configurations and a parameter $\lambda$, learning free-energy weights so the sampled $\lambda$ marginal approaches a target distribution. [SRC-0007] [SRC-0009] In the SRC-0018 route, AWH is run adaptively only until readiness criteria pass, then a frozen-bias production archive is collected. [SRC-0018]

For a frozen AWH reference, the unnormalized configuration-space denominator is

$$
q_{\mathrm{AWH}}^*(x,V)
=
\sum_i \exp[g_{\mathrm{ref}}(i)-u_{\mathrm{ref}}(x,V,i)],
$$

where $g_{\mathrm{ref}}(i)$ is the frozen AWH free-energy estimate plus target-state log weight. [SRC-0018] The replay layer then targets any state $m$ by replacing the numerator with $\exp[-u_m(x,V;\theta)]$. [SRC-0018]

AWH-specific readiness should keep the SRC-0018 gates:

- adaptive-stage bias-change and lambda-mixing checks,
- frozen probe split-half convergence,
- replay/AWH parity over the full lambda profile,
- endpoint parity,
- support coverage over states,
- ESS checks at proposed parameter values. [SRC-0018]

### TSS adapter

TSS also lives naturally in a runged extended ensemble, but its adaptive state is richer. It maintains free-energy estimates, auxiliary averages, visit-control tilts, and, in the windowed version, local window estimates that must be stitched into a global profile. [SRC-0005] [SRC-0006]

The TSS adapter should start with a nonwindowed or minimally windowed implementation before attempting the full windowed machinery. In the simplest nonwindowed case, a frozen TSS reference has the same simulated-tempering denominator shape:

$$
q_{\mathrm{TSS}}^*(x)
\propto
\sum_k \exp[\log \pi_{\mathrm{ref},k}+F_{\mathrm{ref},k}-H_{\mathrm{ref},k}(x)],
$$

where the exact $\pi_{\mathrm{ref}}$ and $F_{\mathrm{ref}}$ must be whatever fixed sampling distribution the frozen production kernel actually uses. This formula is an implementation inference from the TSS simulated-tempering target. [SRC-0005]

For windowed TSS, the adapter must not hand-wave the denominator. It needs to store the active window $J$, the local rung set $W_J$, local free-energy estimates, window weights or selection probabilities, and the exact fixed window/rung sampling rule used during production. The global reporting free energies are stitched from local estimates, but replay weights for parameter optimization should be based on the exact frozen production density, not only on a displayed stitched profile. [SRC-0006]

A 2026-07-07 FFRefine ethanol-solvation implementation test sharpened this requirement. The nonwindowed replay formula should not be generalized to windowed TSS by summing over all frames and adding an active-window offset. In a frozen windowed TSS archive, replay should first be local to the active window: for frames with $J_n=j$ and target rungs $k \in W_j$, compute local weights from the local reduced potential and the archived local log denominator, then estimate local replay surfaces $F^{rep}_{j;k}$. Those local replay surfaces must then be passed through the same reported-window stitching equations as ordinary TSS local estimates. General observables follow the same order: estimate local $\hat O_{j;k}$ with local replay weights, then mix them with $p_j\gamma_{j;k}/\gamma_k^{TSS}$ over windows containing $k$. This is project evidence aligned with SRC-0006's reported-surface construction: the global-offset implementation gave about $6\,k_BT$ replay/TSS disagreement in the windowed scaffold, while local replay plus reported stitching reduced the maximum discrepancy to about $0.37\,k_BT$, within the largest jackknife endpoint uncertainty. [SRC-0006]

TSS-specific readiness should include:

- epoch-based stability after history forgetting,
- jackknife or split-epoch error estimates,
- window coverage and window-overlap connectivity,
- rung round trips or local rung-mixing diagnostics,
- agreement between replayed full profiles and TSS reported profiles,
- stitching residuals or offset instability,
- per-window and per-state ESS under candidate parameters. [SRC-0006]

A 2026-07-13 FFRefine production failure refined this readiness policy. The procedure should not treat every threshold miss as a terminal reason to stop the whole epoch. When replay/TSS parity is close to the tolerance, the diagnostic should carry an uncertainty interval, for example from contiguous delete-block jackknife or split-half replicates over the frozen archive. Accept only when the upper interval bound is within the replay/TSS tolerance, reject only when the lower interval bound exceeds it, and otherwise classify the result as inconclusive. An inconclusive leg-local parity result should extend only the affected frozen-production leg while retaining any other leg that already passed; a clear leg-local parity failure, or an inconclusive result after exhausting frozen extensions, should retry adaptive TSS for that leg rather than discarding unrelated production data. Joint diagnostics such as chronological split-half disagreement can still require extending both legs when both have remaining capacity. This is a project validation lesson grounded in the SRC-0018 frozen-reference separation and in TSS's need for method-specific readiness checks. [SRC-0018] [SRC-0005] [SRC-0006]

The expected benefit to test is not that TSS gives a new optimizer. The optimizer is the same. The test is whether TSS's self-adjustment, visit control, and windowing create a better supported replay archive per unit simulation cost than AWH or fixed MBAR sampling for the same parameter update. [SRC-0005] [SRC-0006]

### MBAR adapter

MBAR estimates free energies from samples collected at multiple known states using all cross-evaluated reduced potentials, and it also gives expectation weights and asymptotic covariance information. [SRC-0023] It is a natural fixed-sample comparator because SRC-0018's replay denominator is already close to MBAR-style mixture reweighting. [SRC-0018]

The safest MBAR force-field-optimization adapter should distinguish sampled reference states from candidate target states:

- sampled reference states have known sampling distributions and counts $N_k$,
- candidate force-field states are evaluated as target or unsampled states,
- the denominator remains tied to the actual reference sampling distributions,
- parameter updates are accepted only while target-state ESS and overlap diagnostics remain adequate.

In MBAR notation, the reference-mixture denominator has the structure

$$
q_{\mathrm{MBAR}}^*(x_n)
=
\sum_k N_k\exp[\hat f_k^{\mathrm{ref}}-u_k^{\mathrm{ref}}(x_n)],
$$

up to a common constant, while a candidate target state uses $\exp[-u_m(x_n;\theta)]$ in the numerator. This is the fixed-reference analogue of the SRC-0018 replay formula and follows the MBAR requirement that all retained samples be evaluated under the relevant reduced potentials. [SRC-0023] [SRC-0018]

MBAR-specific diagnostics should include:

- trajectory decorrelation or subsampling before trusting asymptotic covariance,
- overlap matrix or pairwise overlap diagnostics,
- per-target ESS and influence concentration,
- bootstrap or block uncertainty,
- leave-one-state-out sensitivity,
- comparison against resimulation after accepted parameter moves. [SRC-0023]

The MBAR route will likely be the easiest baseline to implement, because it avoids adaptive-bias readiness. It will also be the least forgiving: if the initial state grid or windows do not cover the candidate force-field distributions, MBAR cannot adaptively repair that support problem. [SRC-0023] [[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]

### Window-mixture MBAR reference for frozen windowed TSS

A window-mixture MBAR reference uses the frozen TSS windows themselves as the sampled MBAR states; FFRefine implemented this on 2026-07-24 (implementation and test details in [[wiki/answers/ffrefine-current-implementation-status]]). For window $j$ with local rung set $W_j$, frozen local free-energy estimates $f_{jk}$, and frozen local log densities $\log \gamma_{jk}$, its unnormalized conditional configuration density is represented by the reduced potential

$$
u_j^{\mathrm{mix}}(x)
=
-\log\sum_{k\in W_j}
\exp[f_{jk}+\log\gamma_{jk}-u_k(x)].
$$

The archive's active-window labels provide the sampled-state assignments and counts $N_j$. Cross-evaluating every retained frame under every frozen window mixture allows MBAR to solve the window normalization constants and form one fixed reference denominator

$$
D_n
=
\sum_j N_j
\exp[\hat f_j-u_j^{\mathrm{mix}}(x_n)].
$$

Any physical rung or candidate force-field state $m$ is then treated as an unsampled target with weights

$$
W_{nm}
\propto
\frac{\exp[-u_m(x_n)]}{D_n}.
$$

Consequently, every archived frame is considered for every thermodynamic target and every optimized observable, rather than restricting a target to frames whose active windows contain that rung. A frame's actual contribution can still be negligible when phase-space overlap is poor; MBAR changes estimator connectivity, not the underlying sampling support. Per-target ESS, influence concentration, source-window weight mass, and sampled-window overlap therefore remain acceptance diagnostics. This is an implementation inference combining the frozen conditional TSS window density from SRC-0006 with the sampled-state mixture estimator from SRC-0023. [SRC-0006] [SRC-0023]

This global MBAR estimator does not replace local-window replay as a TSS readiness check. Local replay followed by the ordinary TSS stitching equations remains the appropriate parity diagnostic against the TSS-reported free-energy surface. The MBAR denominator is instead used consistently for optimization free energies, all optimized observables, their gradients, candidate ESS, and empirical Fisher estimates. During candidate replay, the sampled-window normalization constants and reference denominator are held fixed while candidate target reduced potentials change, preserving the frozen-reference separation required by SRC-0018. [SRC-0018]

## Validation staging

Mathematical correctness, local identifiability on fresh production, and prospective resimulation are separate validation stages. Passing fixed-archive differentiation (values, finite-difference gradients, loss gradients, and small teacher-parameter recovery) proves that the implemented estimator is internally consistent; it does not prove that a production archive resolves a supported parameter direction. The route must therefore require local-identifiability screening on fresh production before commissioning teacher simulations. A failed sensitivity screen should be reported as `inconclusive_sensitivity`, not as mathematics failure or proof of fundamental untrainability. [[wiki/claims/CLM-0038-fixed-archive-gradient-validation-does-not-establish-fresh-archive-trainability]] [[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]

Only fresh resimulation validates the central replay/resimulation loop. So far this has been shown for one local scientific objective: in FFRefine's dielectric-only reaction-field water training, supported archive-derived proposals survived fresh simulation repeatedly. This does not establish ethanol solvation improvement, water density/RDF/dielectric balance, transferability, or robust convergence. [[wiki/claims/CLM-0040-damped-conditional-fisher-dielectric-training-survives-fresh-resimulation]] The underlying evidence for both stages is listed in the Evidence timeline below.

## Phased implementation plan

A phased plan built on this analysis (sampler-agnostic interfaces, an AWH control path, an MBAR baseline first, then a minimal nonwindowed TSS prototype, then a three-way benchmark) was proposed on 2026-07-02; its windowed-TSS steps were revised on 2026-07-07 (commit `eb401bb`). It is kept as a historical snapshot in [[wiki/answers/tss-mbar-replay-phased-implementation-plan]].

## FFRefine project state

This page is a sampler-agnostic design analysis; read it as a design envelope, not as a description of any codebase. FFRefine's implementation of the route is described in [[wiki/answers/ffrefine-current-implementation-status]] (a snapshot pinned to a commit), its decisions and their status in [[wiki/answers/ffrefine-decision-register]], and the project evidence that refined this design in the Evidence timeline below and in [[wiki/answers/ffrefine-paper-methods-knowledge-base]].

## Key equations

Common replay target:

$$
a_{n,m}(\theta)=\exp[-u_m(x_n;\theta)-\log q_{\mathrm{ref}}^*(x_n)].
$$

Common free-energy gradient:

$$
\nabla_\theta \tilde F_m(\theta)
=
\sum_n
\frac{a_{n,m}(\theta)}{\sum_j a_{j,m}(\theta)}
\nabla_\theta u_m(x_n;\theta).
$$

Common Fisher/KL trust region:

$$
D_{\mathrm{KL}}(p_\phi\Vert p_{\phi+\Delta\phi})
\approx
\frac{1}{2}\Delta\phi^\top I(\phi)\Delta\phi,
\qquad
I(\phi)=\mathrm{Cov}_{p_\phi}[\nabla_\phi u].
$$

[SRC-0018]

Method-specific reference denominators:

| Adapter | Reference denominator |
| --- | --- |
| AWH | $\sum_i\exp[g_{\mathrm{ref}}(i)-u_{\mathrm{ref}}(x,i)]$ [SRC-0018] |
| TSS | Exact frozen simulated-tempering or windowed TSS denominator used by production; in the simplest nonwindowed case, $\sum_k\exp[\log\pi_{\mathrm{ref},k}+F_{\mathrm{ref},k}-H_{\mathrm{ref},k}(x)]$. [SRC-0005] [SRC-0006] |
| MBAR | $\sum_k N_k\exp[\hat f_k^{\mathrm{ref}}-u_k^{\mathrm{ref}}(x)]$ for the sampled reference states. [SRC-0023] |

## Evidence timeline

- 2026-07-07: an FFRefine ethanol-solvation scaffold test found that windowed TSS replay must be local to the active window and then stitched; the global-offset alternative gave about $6\,k_BT$ replay/TSS disagreement (see the TSS adapter section).
- 2026-07-13: an FFRefine production failure refined the TSS replay/TSS parity policy toward interval-based, leg-local decisions (see the TSS adapter section).
- 2026-07-24: FFRefine implemented the window-mixture MBAR reference described above. At that date it had **not yet been validated in a complete production optimization run**; in particular, no empirical claim was made that it improves RDF convergence, density/RDF balance, accepted-step quality, or resimulation agreement, which remained production validation questions. [[wiki/answers/ffrefine-current-implementation-status]]
- 2026-07-28: a code audit found that FFRefine had moved from a route-plan prototype toward a project-local implementation on Molly's `AWHGrads` branch. The backend consumed named TSS legs and completed simulations, constructed replay summaries, checked replay/TSS parity, ESS, Fisher, and split diagnostics, and only then ran replay-only proposal chains. It also implemented a global latent coordinate map across arbitrary named legs, QEq charge latents with molecular charge constraints, relative per-epoch bounds for non-QEq parameters, optimisation history, and concise terminal reporting. The implemented experiment surfaces were narrower than this route. [[wiki/answers/ffrefine-current-implementation-status]] [[wiki/answers/ffrefine-paper-methods-knowledge-base]]
- 2026-08-15 to 2026-08-20: FFRefine enthalpy and PME dielectric checks added a validation stage between mathematical correctness and macro optimization. Fixed-archive values, finite-difference gradients, loss gradients, and 0.1% one-parameter recovery passed. Fresh 10 ns and 20 ns scans then found no tested direction meeting SNR 5, replay support, and empirical KL at most 0.02. At 20 ns the best valid SNR was 0.1121 for cutoff/reaction-field enthalpy and 0.08847 for PME dielectric, whereas much larger raw responses were outside replay support. [[wiki/answers/ffrefine-average-observable-trainability-validation]]
- 2026-08-29: an FFRefine conditioning analysis separated the state-conditional Fisher (proposal orientation) from the frozen-bias joint Fisher (bias-portability diagnostic), as described in the optimizer section; at that date the recommendation had not been prospectively validated. [[wiki/answers/ffrefine-kl-definition-for-extended-ensemble-training]] [[wiki/claims/CLM-0039-trust-region-kl-must-match-replay-conditioning]]
- 2026-09-02 to 2026-09-03: the state-conditional Fisher implementation, continuous damping at $\gamma=0.1$, exact empirical cumulative-KL control, and fresh paired checkpoint assessment crossed the production-validation boundary for the dielectric-only reaction-field surface. The first campaign produced two paired-confirmed updates and reproducible final-validation loss. Higher-KL campaign `20260902-115818` produced six consecutive paired-confirmed updates and reduced fresh loss from 7.3431 to 3.6057 through checkpoint 6. The dielectric curve did not converge, checkpoint 7 was not fresh assessed before the user intentionally stopped the run, and no collateral or transferability targets were evaluated. [[wiki/answers/ffrefine-prospective-dielectric-damped-fisher-training]] [[wiki/claims/CLM-0040-damped-conditional-fisher-dielectric-training-survives-fresh-resimulation]]
- 2026-09-24: a multi-family water run (density, RDF, dielectric under family-level Fisher-whitened ConFIG) found that a near-stationary but formally active family with an unreliable treated direction can collapse the shared ConFIG step by orders of magnitude, and that a paired loss-confidence acceptance gate cost work on well-supported steps while missing the run's actual failure (a chain that over-predicted its fresh-archive improvement). FFRefine's response excluded directionally unreliable families from ConFIG aggregation with weight renormalization, and treated loss-based acceptance gates as diagnostic by default under the existing KL/ESS trust region. [[wiki/answers/adding-config-optimiser-to-ffrefine]] [[wiki/answers/ffrefine-loss-gate-diagnostic-policy]] [[wiki/claims/CLM-0044-config-must-exclude-directionally-unreliable-families]] [[wiki/tensions/TEN-0020-config-family-exclusion-versus-untreated-drift]]
- 2026-09-28: designing calibrated, cross-fitted replay-chain diagnostics against a 22-epoch multi-family water run (`20260924-204914`) produced four findings. First, replay-prediction calibration can be checked per family across epochs, but the cumulative-error uncertainty must account for telescoping realised changes and shared archives, not a naive sum of per-epoch variances. Second, the run shows the "optimiser's curse": from epoch 10 on, a converged family's replay-predicted improvement was optimistic in most epochs, consistent with a multi-step replay chain optimising its own replay estimate. Third, renormalising the remaining family weights to sum to 1 after excluding a family changes the natural-gradient step's uncapped length, and acted as a large accidental step-size boost in exactly the epochs where the smallest-weighted family made its best progress. Fourth, the chronological half-archive stability gate (cosine ≥ 0.8) mostly reacted to ordinary sampling noise rather than real drift, costing about 13% of the run's wall time while missing the run's actual failure mode, motivating a cross-fitted "aggregation promise" test in place of a fixed angle threshold. [[wiki/answers/ffrefine-improved-gates-water-run-lessons]] [[wiki/claims/CLM-0048-family-weight-renormalisation-changes-natural-gradient-step-length]] [[wiki/tensions/TEN-0020-config-family-exclusion-versus-untreated-drift]] [[wiki/questions/QST-0007-checkpoint-assessment-versus-next-direction-readiness]]
- 2026-09-28: adapting SRC-0090's per-trajectory $N_\text{eff}$-maximizing equilibration cut and SRC-0091's fast multiscale statistical-inefficiency estimator to a frozen-bias production archive with several observable series and a single replica walking a temperature ladder — a combination neither source addresses — found that the fast estimator itself reads about 15-20% high on AR(1) series, and that naively taking the latest of several per-series argmax cuts over-cuts a stationary archive by an amount that grows sharply as $N/g$ falls; a materiality threshold calibrated conditionally on a cut-independent statistic controls this. [[wiki/answers/ffrefine-multi-series-equilibration-cut-calibration]] [[wiki/claims/CLM-0047-calibrated-materiality-threshold-prevents-multi-series-equilibration-over-cutting]]
- 2026-10-01: since 2026-09-30, FFRefine decided family eligibility with block-based, cross-fitted direction gates (replacing the chronological half-archive cosine gate) and decided, before any replay chain, whether to optimise, buy one rescue extension of the current archive, or stop, using a generic expected-value policy with α-spending for the retest. The first deciding ConFIG and weighted-sum water campaigns were still running on 2026-10-01. [[wiki/answers/ffrefine-direction-gates-and-production-policy]] [[wiki/questions/QST-0011-config-versus-weighted-sum-under-calibrated-direction-gates]]
- 2026-10-07 to 2026-10-11: commit `110fe64` introduced a damped Levenberg-Marquardt trust-region step and made the direction gates report-only (rationale not recorded); on 2026-10-11 this step, with weighted-sum aggregation, became the canonical regime, superseding the natural-gradient step as the canonical step. The natural-gradient path is still in the code at `110fe64` and is decided for removal (FFR-035); whether the trust-region step replaces it in every experiment is not recorded. The 2026-10-11 planning session also decided (not yet implemented) to remove the direction gates, ConFIG, momentum, rescue/extension sizing, loss gates in every mode, the archive KL budget, and Huber loss, and planned a generalist Julia package mirroring Molly's API, a Molly `master` migration after the package shell, and Molly-side changes gated on their usefulness to Molly users. [[wiki/answers/ffrefine-decision-register]] [[wiki/answers/ffrefine-generalist-package-plan-decisions]]

## Sources used

- SRC-0018 for frozen-bias replay, endpoint and observable gradients, candidate-ensemble ESS, empirical Fisher/KL geometry, readiness gates, and line-search acceptance.
- SRC-0005 and SRC-0006 for TSS adaptive rung sampling, visit control, windowing, history forgetting, self-adjustment, global stitching, and implementation tradeoffs.
- SRC-0007 and SRC-0009 for AWH extended ensembles, conditional weight histograms, and alchemical AWH reference context.
- SRC-0023 for MBAR fixed-sample multistate estimation, cross-state reduced potentials, expectation weights, and covariance/overlap limitations.

## Wiki pages used

- [[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]
- [[wiki/concepts/awh-replay-force-field-optimization]]
- [[wiki/concepts/accelerated-weight-histogram-method]]
- [[wiki/concepts/times-square-sampling]]
- [[wiki/concepts/tss-implementation-patterns]]
- [[wiki/concepts/multistate-bennett-acceptance-ratio]]
- [[wiki/concepts/on-the-fly-estimation-versus-mbar]]
- [[wiki/concepts/free-energy-reweighting-for-force-field-fine-tuning]]
- [[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]
- [[wiki/questions/force-field-training-validation-scope]]
- [[wiki/answers/sample-bias-reweighting-method-comparison]]

## Wiki updates made

- Added this answer note.
- Updated [[wiki/concepts/awh-replay-force-field-optimization]] with a sampler-agnostic extension note covering TSS and MBAR adapters.
- Updated on 2026-09-24 with a pointer to the multi-family ConFIG aggregation and loss-gate diagnostic-policy findings recorded in [[wiki/answers/adding-config-optimiser-to-ffrefine]], [[wiki/answers/ffrefine-loss-gate-diagnostic-policy]], [[wiki/claims/CLM-0044-config-must-exclude-directionally-unreliable-families]], and [[wiki/tensions/TEN-0020-config-family-exclusion-versus-untreated-drift]].
- Updated on 2026-09-28 with pointers to [[wiki/answers/ffrefine-improved-gates-water-run-lessons]] (replay calibration, the optimiser's curse, family-weight renormalisation, and the legacy stability gate) and [[wiki/answers/ffrefine-multi-series-equilibration-cut-calibration]] (fast-estimator bias and multi-series over-cutting calibration), and the new claims [[wiki/claims/CLM-0047-calibrated-materiality-threshold-prevents-multi-series-equilibration-over-cutting]] and [[wiki/claims/CLM-0048-family-weight-renormalisation-changes-natural-gradient-step-length]].
- Updated on 2026-10-11 with a subsection recording the canonical trust-region/weighted-sum regime and the 2026-10-11 generalist-package planning session, pointing to [[wiki/answers/ffrefine-generalist-package-plan-decisions]].
- Split on 2026-10-11 so that this page holds only the sampler-agnostic design: the FFRefine implementation-snapshot subsections and the window-mixture MBAR implementation status moved to the Evidence timeline, [[wiki/answers/ffrefine-current-implementation-status]] and [[wiki/answers/ffrefine-decision-register]]; the phased implementation plan and recommended first prototype moved to [[wiki/answers/tss-mbar-replay-phased-implementation-plan]].

## Remaining gaps

- The TSS reference-density formula must be derived against the exact implementation kernel before coding the windowed adapter; the simple formula above is only the nonwindowed simulated-tempering case. [SRC-0005] [SRC-0006]
- The wiki does not yet contain a benchmark comparing AWH, TSS, and MBAR as reference archives for the same force-field optimization problem.
- MBAR uncertainty formulas do not remove the need for support diagnostics and resimulation after parameter updates. [SRC-0023] [[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]
