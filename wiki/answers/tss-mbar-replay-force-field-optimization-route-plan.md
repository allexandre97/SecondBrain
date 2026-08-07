---
type: answer
status: active
created: 2026-07-02
updated: 2026-07-29
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
graph_neighborhoods_used:
  - "tools/query_graph.py --start wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients.md --depth 1"
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

### FFRefine window-mixture MBAR implementation status

A 2026-07-24 FFRefine implementation uses the frozen TSS windows themselves as the sampled MBAR states. For window $j$ with local rung set $W_j$, frozen local free-energy estimates $f_{jk}$, and frozen local log densities $\log \gamma_{jk}$, its unnormalized conditional configuration density is represented by the reduced potential

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

The implementation reuses Molly's lower-level MBAR machinery for the sampled-window solve and target weights, and Molly's partitioned cross-state energy assembly for reduced potentials. Focused synthetic tests verify normalization, observable and free-energy finite-difference gradients, overlap rejection, and source-window contributions. Molecular smoke tests and a reduced water-temperature test verify that the 25 degrees Celsius RDF target receives weight from frames belonging to every TSS window in the test archive. This has **not yet been validated in a complete production optimization run**. In particular, no empirical claim should yet be made that it improves RDF convergence, density/RDF balance, accepted-step quality, or resimulation agreement. Those remain production validation questions.

## Current FFRefine implementation snapshot

A 2026-07-28 code audit found that FFRefine has moved from a route-plan prototype toward a project-local implementation on Molly's `AWHGrads` branch. The backend now consumes named TSS legs and completed simulations, constructs replay summaries, checks replay/TSS parity, ESS, Fisher, and split diagnostics, and only then runs replay-only proposal chains. It also implements a global latent coordinate map across arbitrary named legs, QEq charge latents with molecular charge constraints, relative per-epoch bounds for non-QEq parameters, optimisation history, and concise terminal reporting. See [[wiki/answers/ffrefine-current-implementation-status]] and [[wiki/answers/ffrefine-paper-methods-knowledge-base]].

The implemented experiment surfaces are narrower than the general route plan. `solvation.jl` is a two-leg ethanol solvation workflow whose default training set currently enables the solvation free-energy target; the solvated density target is defined but commented out. `water_temperature.jl` is a one-leg water temperature-ladder workflow using PME by default; it currently trains density and RDF targets. Dielectric prediction and target code exists, but dielectric is commented out of the active target set and split validation. These are implementation facts from the FFRefine repository audit, not literature claims.

The route plan should therefore be read as a design envelope plus accumulated implementation lessons. It should not be read as evidence that full production optimization has already improved ethanol solvation, water density/RDF/dielectric agreement, or transferability. Focused tests and reduced smoke checks exist, but production validation remains open.

## Implementation route plan

### Phase 1: Define the sampler-agnostic interfaces

Implement or refactor around four interfaces:

| Interface | Responsibility | Method-specific? |
| --- | --- | --- |
| `ReferenceArchive` | Store frames, visited states/windows, volumes, reference energies, and metadata. | Mostly common. |
| `ReferenceAdapter` | Provide `log_reference_mixture(frame)` and readiness diagnostics. | Yes. |
| `ReplayEstimator` | Compute target free energies, observables, gradients, ESS, and split diagnostics. | Mostly common. |
| `TrustRegionOptimizer` | Build loss, Fisher metric, KL-scaled step, and acceptance decisions. | Common. |

The hard boundary is that `TrustRegionOptimizer` should not know whether the archive came from AWH, TSS, or MBAR. It should only consume predictions, gradients, Fisher estimates, and diagnostics.

### Phase 2: Lock down the AWH control path

Keep the existing SRC-0018 AWH path as the reference implementation. Add regression tests around:

- frozen reference mixture denominator,
- endpoint replay free energies,
- endpoint gradients,
- observable replay estimate and gradient,
- candidate-ensemble ESS,
- Fisher score covariance,
- line-search rejection on low ESS,
- replay/AWH parity gate. [SRC-0018]

This phase prevents the TSS and MBAR experiments from moving the target.

### Phase 3: Implement the MBAR baseline first

The MBAR baseline is the cleanest first alternative because it does not require adaptive sampler implementation.

1. Choose a small thermodynamic cycle, such as the ethanol hydration example already used by SRC-0018. [SRC-0018]
2. Run fixed equilibrium or biased simulations at a discrete lambda schedule.
3. Decorrelate or stride frames and build a cross-state reduced-potential matrix $u_k(x_n)$.
4. Solve MBAR for the reference sampled states or import the reference $\hat f_k$ values. [SRC-0023]
5. Implement `MBARReferenceAdapter.log_reference_mixture`.
6. Evaluate endpoint targets as unsampled candidate states against the fixed reference mixture.
7. Reuse the common replay gradient, observable, ESS, Fisher, and line-search logic.
8. After each accepted parameter update, run a short independent resimulation check before allowing additional trust-region steps.

Success criteria:

- free energies match standard MBAR at the reference parameterization,
- replay gradients pass finite-difference checks,
- ESS and overlap decline predictably as parameter perturbations grow,
- accepted updates improve the tolerance-normalized objective and survive resimulation.

### Phase 4: Implement a minimal TSS-as-reference prototype

Start with the smallest TSS feature set that can generate a fixed reference archive:

1. Implement a nonwindowed TSS sampler over the same lambda schedule, or choose a small enough schedule that windows are unnecessary.
2. Run adaptive TSS until free-energy estimates, rung occupancy, and visit-control diagnostics stabilize.
3. Freeze the TSS sampling distribution: no stochastic-approximation updates, no history forgetting, and no changing visit-control tilts during production.
4. Collect frozen production frames with visited rung metadata.
5. Export the exact frozen denominator used by the production kernel.
6. Plug the archive into the common replay estimator.

Only after this nonwindowed path works should the implementation add windowed TSS:

1. Store active window labels and local rung sets.
2. Export local window denominators for every retained frame.
3. Compute replay free energies and observable averages locally inside each active window.
4. Stitch local replay free-energy surfaces with the same reported TSS equations used for ordinary local estimates.
5. Stitch local observable averages with the reported window probabilities and global rung density.
6. Add window stitching diagnostics from SRC-0006 as readiness checks, but keep replay weights tied to the actual frozen production density. [SRC-0006]

Success criteria:

- TSS reported profile and replayed profile agree within configured tolerance on supported states,
- split-epoch and split-half estimates are stable,
- window offsets are connected and not dominated by one weak overlap,
- the same optimizer can consume TSS archives without sampler-specific branches.

### Phase 5: Compare AWH, TSS, and MBAR under one benchmark

Use one benchmark before expanding:

- same molecule or system,
- same lambda schedule where possible,
- same trainable parameter subset,
- same experimental or reference targets,
- same optimizer settings,
- same validation resimulations.

Report:

- wall-clock and force-evaluation cost,
- target loss improvement per macro epoch,
- ESS after each accepted step,
- split-half disagreement,
- parity or profile disagreement,
- number of rejected line-search proposals,
- number of forced resimulations,
- held-out observable or held-out lambda validation.

Do not rank methods by final training loss alone. The relevant question is which method produces reference archives that support reliable parameter updates under the same validation standard. [SRC-0018] [[wiki/questions/force-field-training-validation-scope]]

## Recommended first prototype

Build the MBAR baseline first, then the minimal nonwindowed TSS adapter.

MBAR first is useful because it tests the sampler-agnostic optimizer with the least new sampling code. It will also expose whether the current replay and Fisher implementation truly depends on AWH-specific assumptions. [SRC-0023] [SRC-0018]

TSS second is the real test of the user's idea. If TSS frozen archives give higher support or lower split uncertainty than AWH or MBAR for the same system, then TSS is not just another estimator; it becomes a better adaptive reference generator for replay-based force-field optimization. [SRC-0005] [SRC-0006]

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

## Remaining gaps

- The TSS reference-density formula must be derived against the exact implementation kernel before coding the windowed adapter; the simple formula above is only the nonwindowed simulated-tempering case. [SRC-0005] [SRC-0006]
- The wiki does not yet contain a benchmark comparing AWH, TSS, and MBAR as reference archives for the same force-field optimization problem.
- MBAR uncertainty formulas do not remove the need for support diagnostics and resimulation after parameter updates. [SRC-0023] [[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]
