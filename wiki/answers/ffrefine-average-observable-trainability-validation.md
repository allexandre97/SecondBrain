---
type: answer
status: active
created: 2026-08-20
updated: 2026-09-04
question: "Do FFRefine's validated replay mathematics establish that water enthalpy and dielectric permittivity can be trained from fresh TSS archives?"
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
  - enthalpy
  - dielectric-constant
  - replay-reweighting
  - trainability
  - validation
related:
  - "[[wiki/answers/ffrefine-aggressive-density-kl-ess-training]]"
  - "[[wiki/answers/ffrefine-prospective-dielectric-damped-fisher-training]]"
  - "[[wiki/answers/ffrefine-retrospective-fisher-treatment-development]]"
  - "[[wiki/answers/ffrefine-long-archive-target-gradient-convergence]]"
  - "[[wiki/answers/ffrefine-water-temperature-replay-fresh-loss-gap]]"
  - "[[wiki/answers/ffrefine-current-implementation-status]]"
  - "[[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]]"
  - "[[wiki/concepts/dipole-moment-fluctuation-dielectric-constant]]"
  - "[[wiki/claims/CLM-0038-fixed-archive-gradient-validation-does-not-establish-fresh-archive-trainability]]"
  - "[[wiki/claims/CLM-0040-damped-conditional-fisher-dielectric-training-survives-fresh-resimulation]]"
  - "[[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]"
  - "[[wiki/questions/QST-0006-average-observable-trainability-sampling-budget]]"
  - "[[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]"
  - "[[wiki/questions/force-field-training-validation-scope]]"
sources:
  - SRC-0005
  - SRC-0006
  - SRC-0018
  - SRC-0023
  - SRC-0075
  - SRC-0076
  - SRC-0077
sensitivity: public
encryption: none
wiki_pages_used:
  - "[[wiki/index]]"
  - "[[wiki/answers/ffrefine-water-temperature-replay-fresh-loss-gap]]"
  - "[[wiki/answers/ffrefine-current-implementation-status]]"
  - "[[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]]"
  - "[[wiki/concepts/dipole-moment-fluctuation-dielectric-constant]]"
  - "[[wiki/claims/CLM-0009-observable-fitting-needs-held-out-validation]]"
  - "[[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]"
  - "[[wiki/questions/force-field-training-validation-scope]]"
raw_sources_consulted: []
wiki_pages_updated:
  - "[[wiki/answers/ffrefine-water-temperature-replay-fresh-loss-gap]]"
  - "[[wiki/answers/ffrefine-current-implementation-status]]"
  - "[[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]]"
  - "[[wiki/concepts/dipole-moment-fluctuation-dielectric-constant]]"
  - "[[wiki/questions/force-field-training-validation-scope]]"
project_evidence:
  - "FFRefine density-only aggressive conditional-KL/ESS water-temperature run 20260904-102939, completed 2026-09-04"
  - "FFRefine fixed-archive enthalpy mathematics run 20260815-113946"
  - "FFRefine fixed-archive PME dielectric mathematics run 20260819-092631"
  - "FFRefine fresh-archive enthalpy/cutoff trainability run 20260819-194707"
  - "FFRefine fresh-archive dielectric/PME trainability run 20260820-092232"
  - "FFRefine focused water-temperature, mathematics, and trainability tests on 2026-08-20"
  - "FFRefine reaction-field dielectric full-gradient campaign 20260821-124443"
  - "FFRefine cross-fitted reaction-field dielectric campaign revision on 2026-08-21"
  - "FFRefine cross-fitted reaction-field dielectric direction run 20260821-151000"
  - "FFRefine reaction-field dielectric replica comparison run 20260821-190105"
  - "FFRefine cross-observable reaction-field target/Fisher reproducibility run 20260822-204246"
  - "FFRefine two-independent-100ns reaction-field target-gradient convergence comparison completed 2026-08-26"
  - "FFRefine retrospective Fisher-treatment screen and paired cross-archive replay completed 2026-08-28"
  - "FFRefine state-conditional Fisher-treatment screen and replay completed 2026-08-30 through 2026-08-31"
  - "FFRefine dielectric-only damped-Fisher reaction-field water-temperature run 20260901-171027, completed 2026-09-02"
  - "FFRefine higher-KL dielectric-only damped-Fisher reaction-field water-temperature run 20260902-115818, intentionally stopped during epoch 8 on 2026-09-03 after six paired-confirmed fresh updates"
graph_neighborhoods_used:
  - "tools/query_graph.py --start wiki/answers/ffrefine-water-temperature-replay-fresh-loss-gap --depth 2"
---

# FFRefine Average-Observable Trainability Validation

## Short answer

Yes for dielectric in the tested local reaction-field setup; not yet for enthalpy. The first dielectric-only prospective run `20260901-171027` crossed the fresh-trainability boundary with two consecutive paired-confirmed updates and two reproducible final-validation replicas. The higher-KL run `20260902-115818` strengthened that result to six consecutive paired-confirmed updates and reduced fresh dielectric loss from 7.3431 to 3.6057 through checkpoint 6. [[wiki/answers/ffrefine-prospective-dielectric-damped-fisher-training]] [[wiki/claims/CLM-0040-damped-conditional-fisher-dielectric-training-survives-fresh-resimulation]]

This does not establish convergence, a universal sampling budget, or enthalpy trainability. The first run encountered a later direction failure, whereas the higher-KL run's damped direction passed all seven completed optimization archives and was intentionally stopped during epoch 8 after the user judged the six fresh confirmations sufficient. The updated conclusion is that dielectric is demonstrably trainable for sustained local macro optimization under the corrected conditional-KL and damped-Fisher setup, while campaign-level reliability and collateral water properties remain untested.

The earlier checks established two necessary precursor results.

First, the implemented enthalpy and conducting-boundary PME dielectric estimators, replay gradients, loss gradients, and fixed-archive recovery mathematics pass controlled synthetic checks. This substantially weakens the hypothesis that the earlier training failures were caused by an algebraic error in how ensemble-average targets were differentiated.

Second, fresh 10 ns and 20 ns TSS production archives did **not** contain any tested single-parameter perturbation that simultaneously produced a five-standard-error target signal, passed replay support, and stayed within the configured cumulative KL limit. Therefore the current workflow has not established closed-loop trainability of either property. It established a sensitivity/support limitation under the tested archive lengths, parameter basis, positive coordinate perturbations, and trust-region thresholds.

The correct conclusion is neither “the mathematics is broken” nor “enthalpy and permittivity are fundamentally untrainable.” The controlled mathematics works. One cross-fitted reaction-field run found the same approximately 2.7% replay-loss decrease on independent development and held-out archives, with strongly agreeing Fisher-projected directions. A subsequent replica comparison did not reproduce that directional agreement at either matched or doubled aggregate production cost.

The cross-observable run `20260822-204246` now isolates the failure more sharply. Under the same reaction-field Hamiltonian, sampling budget, thermodynamic ladder, parameter basis, and optimizer, density and RDF gradients were reproducible while enthalpy and dielectric gradients were not. The retained Fisher subspace was essentially identical across archives. Holding the gradient fixed while changing the Fisher estimate preserved the direction, whereas holding the Fisher fixed while changing the archive gradient preserved the enthalpy/dielectric disagreement. The leading problem is therefore observable-specific gradient estimation, with Fisher inversion amplifying that disagreement, rather than a generally defective Fisher information matrix.

The present evidence establishes that coherent replay directions can occur, especially after pooling independent information, but not yet that enthalpy or dielectric directions are reproducible enough for closed-loop training.

The later two-independent-100 ns reaction-field comparison refines that conclusion. Density and RDF remained reproducible at every cumulative prefix. Dielectric became continuously accepted from 60 through 100 ns and reached natural-direction cosine 0.9743 at 100 ns. Enthalpy's raw-gradient cosine reached 0.9691, but its full-Fisher natural direction remained at 0.6288. The retained Fisher subspaces were effectively identical. This makes a long-archive dielectric direction a prospective validation candidate while localizing the enthalpy failure to residual target-gradient variation amplified by full Fisher coupling. Two archives and unstable chronological halves are not sufficient to establish equilibrium convergence or fresh-simulation trainability. [[wiki/answers/ffrefine-long-archive-target-gradient-convergence]]

Retrospective finite-step replay on those same two archives adds an important layer. The production hard-Fisher dielectric proposal reduced loss bidirectionally on the opposite archive by about 1.11%, with both paired intervals below zero; damping with $\gamma=10^{-4}$ increased the reductions to about 1.70--1.81%. All six dielectric target temperatures improved. For enthalpy, identity and diagonal directions were highly reproducible but realised much smaller empirical KL and mostly inconclusive loss changes. Small-$\gamma$ damping instead reduced enthalpy loss significantly in both cross directions despite failing the exact-direction cosine gate. These are strong fixed-archive development results, not held-out method validation or fresh-simulation trainability. [[wiki/answers/ffrefine-retrospective-fisher-treatment-development]]

## Exact experiment scope

The validation preserved the production thermodynamic ladder used by `water_temperature.jl`:

- integer temperatures from 14 through 41 degrees Celsius;
- 28 thermodynamic states;
- the original lambda schedule;
- TSS window size 4;
- 15 overlapping TSS windows.

Target availability did not change sampling. Enthalpy targets use relative liquid enthalpies across the ladder, with the lowest-temperature state as the reference. Dielectric training has six experimental target temperatures, 15, 20, 25, 30, 35, and 40 degrees Celsius, but TSS still samples the complete 28-state ladder.

The fresh-archive scan tested positive fractional shifts of 0.02%, 0.05%, 0.1%, 0.2%, 0.5%, and 1% for six bounded water parameters: hydrogen sigma and epsilon, oxygen sigma and epsilon, and double-exponential alpha and beta. A direction was eligible only when all of the following held:

- replay support passed;
- empirical KL divergence was no greater than 0.02;
- the root-mean-square target displacement, normalized by jackknife standard errors, was at least 5.

For target vector $y$ and baseline vector $y_0$, the prescreen signal-to-noise ratio was

$$
\operatorname{SNR}
=
\sqrt{
\frac{1}{N_y}
\sum_i
\left(
\frac{y_i-y_{0,i}}{\operatorname{SE}_i}
\right)^2
}.
$$

This uncertainty-normalized signal is distinct from the scientific target tolerance used in the training loss. A small training tolerance cannot manufacture information that is absent from a noisy archive.

Each scan began with 10 ns of frozen production. If no eligible direction existed, the same production trajectory was extended by another 10 ns and the full scan was repeated on the 20 ns archive. The enthalpy check used Molly's atom/site-pair reaction-field cutoff path; the dielectric check used PME. Both ran with rigid water on GPU 1 using Julia 1.12, 32 Julia threads, and one garbage-collector thread.

## Fixed-archive mathematics results

### Relative enthalpy

The fixed-archive enthalpy check used a 0.1% synthetic teacher shift that stayed within replay support, with empirical KL 0.00269. Analytic and finite-difference results agreed closely:

| Diagnostic | Result |
| --- | ---: |
| Prediction-gradient relative error | $2.36\times10^{-5}$ |
| Prediction-gradient cosine | $0.9999999999$ |
| Loss-gradient relative error | $5.15\times10^{-4}$ |
| Loss-gradient cosine | $1.0$ |
| Initial loss | $100$ |
| Final loss | $0.01396$ |
| Final normalized RMSE | $0.1182$ |
| Teacher-shift recovery error | $0.01221$ |

The original artifact labeled this run `math_failure` because the first harness used an arbitrary normalized-RMSE cutoff of 0.1. That label was not consistent with the gradient agreement or parameter recovery. The harness was corrected to distinguish gradient failure from recovery failure and to accept the observed controlled recovery under a 0.2 normalized-RMSE threshold. The underlying numerical evidence, not the stale label, supports the mathematics.

### PME dielectric permittivity

The fixed-archive PME dielectric check used the operational estimator

$$
\varepsilon_r=1+
\frac{\langle M^2\rangle-|\langle M\rangle|^2}
{3\varepsilon_0\langle V\rangle k_BT},
$$

consistent with conducting-boundary PME. [SRC-0075] The 0.1% synthetic teacher check gave:

| Diagnostic | Result |
| --- | ---: |
| Prediction-gradient relative error | $2.80\times10^{-5}$ |
| Prediction-gradient cosine | $0.9999999996$ |
| Loss-gradient relative error | $4.96\times10^{-4}$ |
| Loss-gradient cosine | $1.0$ |
| Initial loss | $100$ |
| Final loss | $0.000721$ |
| Final normalized RMSE | $0.02686$ |
| Teacher-shift recovery error | $0.002574$ |

This check passed. It validates the implemented PME dielectric value/gradient/recovery path on a fixed archive. It does not validate fresh-archive trainability, finite-size convergence, or the atom/site-pair reaction-field Hamiltonian.

## Fresh-archive trainability results

The table separates the largest **valid** candidate from the largest raw SNR. “Valid” means replay support passed and KL was at most 0.02.

| Property and Hamiltonian | Archive | Best valid direction | Fraction | Valid SNR | KL | Largest raw SNR | Eligible directions |
| --- | ---: | --- | ---: | ---: | ---: | ---: | ---: |
| Relative enthalpy, cutoff/RF | 10 ns | oxygen sigma | 0.02% | 0.1394 | 0.01462 | 14.21 | 0 |
| Relative enthalpy, cutoff/RF | 20 ns | DEXP alpha | 0.05% | 0.1121 | 0.01639 | 19.87 | 0 |
| Dielectric, PME | 10 ns | DEXP alpha | 0.05% | 0.1120 | 0.01595 | 30.22 | 0 |
| Dielectric, PME | 20 ns | DEXP alpha | 0.05% | 0.08847 | 0.01577 | 22.49 | 0 |

The large raw SNRs were oxygen-sigma proposals with KL values above 10 and failed replay support. They are evidence that sufficiently large parameter changes alter the observable, but they are not evidence that the fixed archive can estimate those changes reliably. MBAR/replay cannot create phase-space support that was not sampled. [SRC-0018] [SRC-0023] [[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]

Doubling production from 10 ns to 20 ns did not increase the best valid SNR in either realized archive. This is an empirical observation from one sequentially extended archive per property, not a general scaling law. It does not prove that longer sampling or independent replicas cannot help.

Because no prescreen candidate was eligible, the workflow correctly stopped before generating independent teacher archives and before starting macro-epoch optimization. Thus these runs test local identifiability and replay support, not end-to-end recovery.

## What the result explains about earlier failures

The result separates two mechanisms that had previously been conflated.

The earlier density sawtooth analysis showed that replay loss on archive $D_e$ and fresh loss on archive $D_{e+1}$ are different estimators. Replay line search can be monotone on $D_e$ while the next resimulation jumps upward because the selected proposal was adapted to the old archive. [[wiki/answers/ffrefine-water-temperature-replay-fresh-loss-gap]] [SRC-0018]

The new average-observable checks identify an earlier bottleneck for enthalpy and dielectric: within the tested replay trust region, their parameter-induced signal is much smaller than archive uncertainty. In that regime, an optimizer can follow a mathematically correct but statistically unstable gradient. A large loss change between macro epochs would then be unsurprising, because resimulation noise and archive-specific gradient error can dominate the resolvable local signal.

This does not prove that every historical enthalpy or dielectric failure had this single cause. The historical runs were not all generated with the final diagnostics, and the new tests cover only the current parameterization and Hamiltonian choices. It does rule out treating a successful fixed-archive finite-difference test as sufficient evidence for production trainability.

## Reaction-field whole-gradient campaign

Run `20260821-124443` tested dielectric-only training with Molly's atom/site-pair reaction-field cutoff Hamiltonian, the operational $1+A$ estimator, and the complete QEq-plus-bounded-water-parameter direction produced by the production optimizer. It retained the exact 14 through 41 degrees Celsius TSS ladder and used two independent production archives, each started at 10 ns and then sequentially extended to 20 ns after an inconclusive result.

The first 10 ns archive produced a numerically valid full-gradient proposal:

- replay loss decreased from 6.051353 to 5.914360, a 2.26% archive-local reduction;
- estimated KL was 0.010000 and empirical archive KL was 0.010535;
- the minimum target-state ESS was 433.7 with minimum retention 0.9474;
- candidate ESS was 1949.3 with retention 0.9792;
- five of ten Fisher modes were retained;
- the proposal moved both QEq-derived charges and every configured bounded nonbonded parameter.

This is stronger evidence than the earlier coordinate scan that a combined, support-preserving dielectric descent direction can exist. It is not evidence of trainability: the delete-block paired loss interval was inconclusive, so the proposal was not accepted. After both archives reached 20 ns, each independently failed the pre-optimization sampling gate with the generic `sampling_limited` classification. The two final dielectric curves also differed materially; their experimental-target losses were 6.61384 and 6.97481. The old campaign did not persist the exact replay, ESS, split, Fisher, or half-gradient subgate responsible for those terminal classifications, so no more specific cause should be inferred from the saved artifact.

The result exposes two design problems in that campaign. Sequentially extending the same realization does not measure between-replica stability, and requiring each archive to independently create an accepted proposal conflates direction estimation with out-of-sample validation. It can reject a useful pooled direction merely because an individual noisy archive cannot establish paired confidence.

The revised direction experiment therefore uses four independent 10 ns archives:

1. Pool two development archives at the level of target values, target gradients, and physical Fisher matrices.
2. Construct one full QEq-plus-bounded-parameter natural-gradient proposal from that pooled development estimate.
3. Use estimated KL 0.009 for proposal scaling while retaining a hard empirical-KL ceiling of 0.01 on every archive.
4. Require replay support on both development archives and combine their paired delete-block loss changes using both within-archive and between-archive variance.
5. Freeze the selected proposal and replay it unchanged on two independent held-out archives.
6. Require held-out replay support, empirical KL at most 0.01 on each archive, a pooled paired loss improvement of at least 1%, and development/held-out full-gradient agreement with Fisher-metric cosine at least 0.8 and norm ratio between 0.5 and 2.

Every archive-level replay, ESS, Fisher, split, half-gradient, paired-loss, line-search, and empirical-KL diagnostic is now persisted. The direction stage does not sequentially extend archives; an inconclusive result points to additional independent replicas or more information per replica rather than silently reusing the same trajectory.

### Cross-fitted result

Run `20260821-151000` completed that four-archive protocol. Its formal classification was `inconclusive`, but the evidence was qualitatively different from the earlier failures.

| Diagnostic | Development archives | Held-out archives |
| --- | ---: | ---: |
| Pooled point loss decrease | 2.722% | 2.718% |
| Conservative lower bound on loss decrease | 0.815% | 0.236% |
| Empirical KL values | 0.010215, 0.009683 | 0.009879, 0.009769 |
| Paired classification under the at-least-1% confidence gate | inconclusive | inconclusive |

All four individual archive point estimates favored the fixed candidate, with loss decreases of 2.36%, 3.12%, 2.37%, and 2.99%. The development and held-out pooled point responses differed by less than 0.2% relative to each other. Both pooled candidate-minus-baseline confidence intervals lay below zero, so the sign of the replay improvement was resolved; they failed only the stronger requirement that the entire interval establish at least a 1% decrease.

The independently estimated development and held-out natural-gradient directions had Fisher-metric cosine 0.9325 and norm ratio 0.9975, passing the predefined thresholds of 0.8 and 0.5–2.0. Each retained five of ten Fisher modes. Their ordinary Euclidean step cosine was 0.9821. In contrast, chronological half-archive gradient cosines for the four individual 10 ns archives were 0.085, 0.505, 0.292, and 0.262. This combination is evidence that individual half archives are too noisy, while pooling independent archives and Fisher projection can expose a reproducible direction.

Replay support was strong on all four archives. Candidate minimum target-state ESS values were at least 391.8, minimum ESS retention was at least 0.9438, candidate ESS was at least 1918.6, and candidate ESS retention was at least 0.9811. The candidate changed charge magnitudes by about 0.075% and each bounded nonbonded parameter by less than 0.8%; it was not a large extrapolative perturbation.

The first development archive had empirical KL 0.010215 for estimated KL 0.009, exceeding the predefined 0.01 ceiling by 2.15%; the other three archives passed. The implementation applied this hard empirical check after line search, so it classified the proposal as `empirical_kl_exceeded` instead of shrinking and reevaluating it. This is a control-flow limitation exposed by the run, not evidence that overlap was poor.

The result supports the narrower claim that a reproducible, support-preserving reaction-field dielectric replay direction exists in the tested full-parameter basis. It does not establish that fresh simulations at the candidate parameters reproduce the dielectric or loss response. The held-out archives were independently simulated at baseline parameters and evaluated the frozen candidate by replay. Candidate dielectric values by temperature were not persisted, so the saved result cannot determine whether all six temperature targets moved favorably or whether the aggregate improvement was concentrated in a subset.

### Replica comparison result

Run `20260821-190105` prospectively applied the corrected empirical-KL line-search constraint, the direction-stage policy requiring a point improvement of at least 1% plus a confidence interval below zero, and temperature-resolved candidate logging. It compared two replicas in every TSS phase under two budgets while retaining two independently prepared development archives and two independently prepared held-out archives:

- cost matched: 5 ns per replica, 10 ns aggregate production per archive;
- higher power: 10 ns per replica, 20 ns aggregate production per archive.

Both variants were `inconclusive` at the replay-direction stage.

| Diagnostic | Two by 5 ns | Two by 10 ns |
| --- | ---: | ---: |
| Development point loss improvement | 1.84% | 1.21% |
| Held-out point loss improvement | -0.29% | 0.52% |
| Development/held-out Fisher direction cosine | -0.072 | 0.287 |
| Mean within-archive replica direction cosine | -0.277 | 0.090 |
| Archives passing chronological gradient stability | 1 of 4 | 3 of 4 |
| Empirical-KL outcome | One held-out value at 0.01064 failed | All values passed |

Replay, ESS, Fisher, chronological target split, and complete ladder/window coverage passed for every archive. Increasing from 5 to 10 ns per replica roughly doubled local ESS and reduced within-archive loss uncertainty by about 18% in development and 36% held out. It did not resolve the direction: similarly sized Fisher-metric steps had different orientations, individual replica directions remained inconsistent, and one held-out archive improved while the other worsened in each variant.

The difference between chronological and replica splits is scientifically important. In the higher-power variant, three archives had chronological half-gradient cosines near 0.97 or above, yet their two constituent replicas did not agree on the direction. A pooled trajectory can therefore appear temporally stable while retaining persistent replica-specific dielectric or gradient behavior. Complete TSS ladder coverage is not evidence that the slower dipole-fluctuation modes determining permittivity and its parameter gradient have equilibrated.

Temperature-resolved replay showed that the higher-power development candidate lowered permittivity at all six target temperatures. On held-out data it lowered five of six values, but the pooled loss decrease was only 0.52%, below the prospective 1% point threshold and statistically unresolved. Thus the failure was not a missing physical response; it was insufficiently reproducible magnitude and direction.

Compared with run `20260821-151000`, which obtained direction cosine 0.9325 and approximately 2.7% point improvements in both development and held out, the replica run shows that the earlier coherence was not robust to the tested replica setups. The two replica variants used the same campaign seed and are not independent repetitions, so they do not establish a frequency of success or prove that more sampling worsens the direction. They do establish that neither tested replica allocation is sufficient evidence for trainability.

### Cross-observable Fisher reproducibility result

Run `20260822-204246` directly tested whether Fisher estimation could explain why density and RDF train while enthalpy and dielectric fail. It used reaction-field electrostatics, the operational $1+A$ dielectric estimator, the complete QEq-plus-bounded-water-parameter basis, and the unchanged 14 through 41 degrees Celsius, 28-state TSS ladder. At matched aggregate production cost it compared:

- one shared TSS archive containing two 10 ns replicas;
- two independently prepared TSS archives containing one 10 ns replica each;
- the pooled shared arm, with 20 ns aggregate production, against the pooled independent arm, also with 20 ns aggregate production.

This is one campaign seed and one pair of pooled arms. It diagnoses this realization; it does not estimate a probability of success over campaign repetitions.

#### Sampling and Fisher validity

All three archive-level replay checks passed. Every requested path had complete TSS-window coverage, sufficient ESS, and an accepted Fisher estimate. Across the four individual 10 ns trajectories, minimum local ESS ranged from 242.5 to 403.3 and candidate ESS ranged from 1874.2 to 1988.4. The shared pooled path had minimum local ESS 686.9 and candidate ESS 3920.4.

Every endpoint retained modes 6 through 10 of the ten-dimensional Fisher decomposition at the default eigenvalue floor of 0.001. The Fisher subspaces were nearly identical:

| Comparison | Retained modes per endpoint | Minimum principal cosine | Normalized projector overlap |
| --- | ---: | ---: | ---: |
| Shared replicas | 5, 5 | 0.999996 | 0.999999 |
| Independent archives | 5, 5 | 0.999945 | 0.999977 |
| Pooled arms | 5, 5 | 0.999994 | 0.999997 |
| Chronological halves, range over four paths | 5, 5 | 0.999912–0.999977 | 0.999958–0.999990 |

The large physical-coordinate condition estimates, about $6.2\times10^7$ to $6.9\times10^7$, therefore did not correspond to an archive-dependent retained subspace. Jacobi scaling and eigenmode truncation selected the same effective geometry in every path.

#### Direction reproducibility separates the observable families

Using the common-Fisher metric, the default natural-gradient directions gave:

| Comparison | Density cosine | RDF cosine | Enthalpy cosine | Dielectric cosine |
| --- | ---: | ---: | ---: | ---: |
| Shared replicas | 0.999 | 0.996 | 0.170 | 0.265 |
| Independent archives | 1.000 | 0.999 | -0.545 | -0.089 |
| Pooled shared arm versus pooled independent arm | 0.999 | 0.999 | 0.589 | 0.764 |

The prospective acceptance threshold was 0.8, with a Fisher-metric norm ratio between 0.5 and 2. Density and RDF passed every comparison. Enthalpy and dielectric failed every default full-path comparison even though their norm ratios were near one after KL scaling.

Chronological halves showed the same target-family separation rather than falsely reassuring internal consistency:

- density cosines were 0.996–0.999;
- RDF cosines were 0.990–0.998;
- enthalpy cosines were -0.469 to 0.484;
- dielectric cosines were -0.254 to 0.107.

Thus this campaign does **not** show gradients that are stable inside each 10 ns trajectory but unstable only between independent archives. The difficult observables were already directionally unresolved between chronological halves.

Target-value split checks did not substitute for gradient checks. RDF passed all four individual target splits and enthalpy passed one of four, which was consistent with their direction results. Dielectric nevertheless passed all four target-value splits while failing every chronological gradient comparison. Density passed only two of four target-value splits while retaining nearly perfect direction transfer. Under these strict thresholds, target-mean convergence was therefore neither sufficient for gradient convergence nor necessary for the observed density direction reproducibility.

#### Gradient variation, not Fisher variation, is dominant

The campaign recomputed directions under two counterfactuals:

1. each endpoint kept its own gradient but both used a common averaged Fisher;
2. both endpoints used the same averaged gradient but kept their own Fisher estimates.

The first counterfactual preserved the enthalpy and dielectric failure. For independent archives, common-Fisher cosines were -0.557 for enthalpy and -0.091 for dielectric. The second counterfactual produced cosines of 0.997 and 0.998, respectively. Across all target families and comparisons, changing the Fisher while holding the gradient fixed gave cosines of 0.989–1.000.

The retained-mode projections explain how the same Fisher treatment can affect target families differently. Density placed most Fisher-whitened gradient weight consistently in modes 7 and 8, while RDF placed about three quarters in mode 9. Enthalpy and dielectric redistributed weight between retained modes across archives and often reversed projection signs. Between independent archives, enthalpy reversed signs in modes 7 through 10, including its dominant mode-9 contribution; dielectric reversed mode 8 and changed the relative mode weights substantially. Fisher inversion amplified these observable-specific gradient differences, but did not create them through archive-to-archive Fisher variation.

#### Replay transfer directly exposes archive-specific updates

Each archive's default proposal was replayed on itself and on the other archive. Percentage loss changes were:

| Target | Archive 1 proposal on archive 1 | Archive 1 proposal on archive 2 | Archive 2 proposal on archive 1 | Archive 2 proposal on archive 2 |
| --- | ---: | ---: | ---: | ---: |
| Density | -15.37% | -16.73% | -14.95% | -16.27% |
| RDF | -0.80% | -0.79% | -0.84% | -0.83% |
| Enthalpy | -7.69% | +6.54% | +5.26% | -11.81% |
| Dielectric | -2.08% | +0.47% | +0.17% | -2.23% |

Density and RDF proposals transferred almost unchanged. Enthalpy and dielectric proposals improved the archive that generated them but increased loss on the other independently prepared archive. This is direct evidence of archive-specific optimization in this realization.

Shared-preparation replicas were more mutually favorable but still failed directional reproducibility. Their enthalpy cross-replay improvements were only 0.71% and 2.15%, compared with source-replica improvements of 10.53% and 5.41%. Their dielectric cross-replay improvements were 1.02% and 0.80%, compared with local improvements of 2.67% and 3.21%. Shared TSS preparation may induce useful correlation, but these replicas cannot be counted as independent evidence for the equilibrium direction.

#### Pooling is promising for dielectric but not yet validation

Pooling raised the shared-versus-independent dielectric direction cosine to 0.764. The shared-pool proposal reduced pooled independent loss by 1.21%; at member level it reduced the two independent losses by 1.94% and 0.37%. The independent-pool proposal reduced shared-pool loss by 1.99%. Nine of twelve dielectric temperature-level residuals improved under the shared-to-independent replay, while all six improved under the independent-to-shared replay.

Enthalpy pooling was weaker. The pooled-arm cosine was 0.589. The shared-pool proposal increased loss on independent archive 1 by 0.75% and reduced loss on independent archive 2 by 7.17%, while the independent-pool proposal reduced shared-pool loss by 3.19%.

The predeclared Fisher-floor sweep showed sensitivity in pooled dielectric only. Its pooled-arm cosine was 0.835 at floor 0.0001, 0.764 at the default 0.001, and 0.842 at floor 0.01. Neither alternative floor repaired the individual shared-replica or independent-archive comparisons, and enthalpy remained below threshold at every floor. The non-monotonic pooled dielectric result is evidence that mode regularization may matter; selecting a floor from this single observed realization would be post-selection rather than validation.

#### Replay support passed, but the KL target had no safety margin

All 56 member-level replay probes passed support. Minimum local ESS retention was at least 0.9004 and candidate ESS retention was at least 0.9781. Cross-archive loss failures therefore cannot be attributed to replay-support collapse under the recorded diagnostics.

The estimated KL target and hard empirical ceiling were both 0.01. Empirical KL ranged from 0.00921 to 0.01287, so only 3 of 56 member-level probes passed the hard ceiling. The systematic near-boundary overshoot is a control-setting limitation: future proposals need an estimated-KL margin below 0.01 or empirical-KL backtracking. It is orthogonal to the target-family separation because density and RDF transferred despite the same overshoot, whereas enthalpy and dielectric did not.

#### Updated interpretation

For this matched reaction-field experiment, a generally unstable Fisher matrix is not a viable explanation for why only enthalpy and dielectric fail. The retained Fisher geometry was reproducible, and density/RDF supplied positive controls under exactly the same geometry. The evidence instead supports target-dependent error in the covariance-derived objective gradients. A schematic archive estimate remains

$$
\widehat{\nabla L}_i
=
\nabla L_{\mathrm{equilibrium}}
+
\eta_i,
$$

but this run adds two qualifications. First, $\eta_i$ was visible between chronological halves as well as between independent archives for enthalpy and dielectric. Second, natural-gradient preconditioning can magnify $\eta_i$ when noisy observable-gradient components project into retained low-information modes. Density and RDF are protected not because they use a different Fisher estimate, but because their gradients occupy the retained Fisher modes reproducibly.

The result does not establish closed-loop trainability, an adequate final sampling budget, or a fresh-simulation response. It does establish a matched-control diagnosis: under one common pipeline and at the original short budgets, the difficult average-observable gradients are unstable while density and RDF gradients are reproducible.

The later two-independent-100 ns reaction-field comparison refined this diagnosis. At 100 ns, enthalpy's independent-archive raw-gradient cosine and Euclidean norm ratio reached 0.9691 and 0.9655, but its full-Fisher natural-direction cosine was only 0.6288 despite a Fisher-metric norm ratio of 0.9989. Dielectric passed at the same endpoint both before Fisher conditioning, with cosine 0.9777 and norm ratio 0.8204, and after it, with cosine 0.9743 and norm ratio 1.0028. Therefore, it is no longer accurate to summarize both difficult targets as having equally unresolved cumulative raw gradients at the longest tested budget. [[wiki/answers/ffrefine-long-archive-target-gradient-convergence]]

The distinction is target-specific:

- dielectric increasingly looks sampling-limited; longer independent cumulative archives recovered a reproducible raw and full-Fisher direction in one archive pair, although disjoint halves and local blocks still prevent claiming equilibrium;
- enthalpy retains temporal raw-gradient instability, but the 100 ns independent endpoint indicates that full Fisher inversion is the proximate transformation that destroys otherwise strong cross-archive directional agreement;
- the Fisher estimate is common geometry rather than a universally bad estimator: density and RDF remain positive controls, and changing Fisher matrices while holding the gradient fixed produced almost identical directions.

### Main working hypothesis for dielectric training failure

The leading interpretation is now archive-specific gradient error. For archive $i$, the computed gradient can be represented schematically as

$$
\widehat{\nabla L}_i
=
\nabla L_{\mathrm{equilibrium}}
+
\eta_i,
$$

where $\eta_i$ is the error caused by the finite realization of the slowly mixing dielectric fluctuations and their covariance with parameter-energy derivatives. The mathematics can therefore produce a correct gradient for the sampled archive while two independently sampled archives produce materially different directions whenever $\eta_i$ is comparable to or larger than the equilibrium gradient.

This hypothesis directly explains a macro-epoch failure mode. A proposal selected on archive $D_e$ can decrease replay loss on $D_e$, but after resimulation the next archive $D_{e+1}$ can expose a differently oriented gradient and a higher fresh loss. The optimizer is then following an archive-specific descent direction rather than a sufficiently precise estimate of the population descent direction.

Chronological self-consistency is not sufficient evidence against this explanation. In the higher-power replica run, three of four pooled archives passed their chronological half-gradient check while the constituent replicas and the independently pooled development and held-out archives disagreed. A trajectory confined to one slowly evolving polarization regime can have consistent halves without representing equilibrium variation across regimes. Conversely, run `20260822-204246` found that all four 10 ns trajectories already had inconsistent enthalpy and dielectric half-directions. Chronological stability must therefore be measured rather than presumed; when it passes, it still does not replace independent-archive validation.

This is a working hypothesis, not a proof that every historical dielectric failure had the same cause or that no feasible sampling budget can recover the equilibrium gradient. It is the explanation most consistent with the current combination of validated fixed-archive derivatives, acceptable replay support and KL, improved within-archive uncertainty, and failed cross-archive direction reproducibility.

The 100 ns result is compatible with this hypothesis rather than contradicting it: increasing independent information eventually produced cumulative dielectric agreement. It does not show that 60 ns is a universal threshold or that recent chronological blocks have equilibrated.

### Optimizer-geometry implication

An implementation audit confirmed that the production operator is not a direct inverse of the raw physical Fisher. It applies the physical-to-latent chain rule, a $10^{-8}$ ridge, Jacobi normalization, hard truncation of normalized modes below $10^{-3}$, the retained-mode pseudoinverse, and scalar KL rescaling. This construction is algebraically consistent. At 100 ns both archives retained the same five-dimensional subspace, but its normalized condition number was still about 2,100. The regularization removed near-null modes without eliminating strong inverse reweighting within the retained space. The observed enthalpy failure is therefore an interaction between residual target-gradient error and the retained full off-diagonal metric, not evidence of an incorrectly coded or archive-dependent Fisher estimate. The detailed spectrum, mode projections, floor sweep, and configuration implications are recorded in [[wiki/answers/ffrefine-long-archive-target-gradient-convergence]].

The same setting currently serves two conceptually different roles: validating negative eigenvalues of the raw physical Fisher and truncating positive modes of the Jacobi-normalized latent Fisher. These tolerances should be separated. The hard floor is also target-independent and cannot distinguish stable density/RDF projections from noisy enthalpy projections; continuous damping or uncertainty-aware modal filtering should be tested prospectively rather than chosen after inspecting this archive pair.

The long-archive enthalpy result motivates a prospective comparison between the existing full-Fisher direction,

$$
\boldsymbol\Delta_{\mathrm{full}}
=
-\alpha F^{+}\mathbf g,
$$

and latent-space steepest descent,

$$
\boldsymbol\Delta_{\mathrm{SD}}
=
-\eta\mathbf g.
$$

The second direction avoids amplifying noisy gradient components through inverse low-information Fisher modes. The Fisher can still be used without inversion to enforce the same scalar trust region,

$$
\frac12
\boldsymbol\Delta_{\mathrm{SD}}^\mathsf T
F
\boldsymbol\Delta_{\mathrm{SD}}
\leq
D_{\mathrm{KL}}^{\mathrm{target}}.
$$

A diagonal-Fisher arm is a useful intermediate comparison. All arms must use the same complete pooled gradient, dimensionless latent coordinates, bounds, regularization, and empirical-KL budget.

The retrospective treatment campaign has now tested these operators more directly. Identity and diagonal enthalpy directions preserved independent-archive agreement, with minimum 60--100 ns cosines 0.9974 and 0.9415. Their realised empirical KL values were only about 0.00073 and 0.00089, compared with about 0.0052--0.0055 for the hard and damped directions, and their paired loss intervals were mostly inconclusive. They therefore establish orientation reproducibility, not finite-step superiority.

Continuous damping with $\gamma=10^{-4}$ produced bidirectional paired-resolved enthalpy replay descent despite a poor direction cosine. It did so partly by restoring two normalized Fisher modes below the production hard floor. This reveals a shared descent cone but also creates a low-information-mode risk. The damping value was selected on the same archive pair and must be frozen before any new comparison. [[wiki/answers/ffrefine-retrospective-fisher-treatment-development]]

This optimizer hypothesis is stronger for enthalpy than dielectric. At 100 ns full Fisher conditioning specifically reduced enthalpy reproducibility, whereas dielectric passed both raw and full-Fisher comparisons. Steepest descent cannot replace the longer or more independent sampling still required by either target.

## Prospective damped-Fisher dielectric result

The state-conditional Fisher-treatment rerun completed before the prospective experiment. Under matched maximum conditional-KL geometry, hard full Fisher, damping at $\gamma=0.03$ and $0.1$, diagonal scaling, and modal-SNR treatments all produced eligible dielectric replay proposals on the reused 100 ns archive pair. Hard full Fisher ranked first by the retrospective replay score. Damping at $\gamma=0.1$ was selected prospectively because it preserved the full correlation geometry, gave a stronger direction-robustness score than hard cutting on that pair, avoided a discontinuous eigenvalue floor, and was simpler than estimating modal SNR. This was a bias-variance and implementation choice, not a claim that damping had the largest retrospective loss effect.

Run `20260901-171027` then used the complete reaction-field macro pipeline with $\gamma=0.1$, state-conditional Fisher geometry, maximum conditional-KL control, 20 ns adaptive sampling, and 60 ns one-replica production per epoch. It generated three replay-updated checkpoints. The first two were evaluated in subsequent fresh macro epochs:

| Evaluated checkpoint | Fresh candidate loss | Parent loss on same fresh archive | Paired loss change | Recorded interval |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 6.7783 | 7.3951 | -0.6168 | [-0.7831, -0.4505] |
| 2 | 5.9600 | 6.4867 | -0.5267 | [-0.6849, -0.3685] |

Two final-validation replicas of checkpoint 2 gave losses 5.9654 and 5.9312. Their mean, 5.9483, was 17.79% below the initial archive loss 7.2354. The validation-mean dielectric prediction moved toward experiment at every one of the six target temperatures.

The selected damped half-direction passed in epochs 1--3, failed in epoch 4, and passed in both validation replicas. Across all six archives it passed five times, compared with three hard-cut reporter passes and two raw-gradient reporter passes. A raw-gradient gate would have stopped epoch 1 and prevented both confirmed improvements.

Epoch 4 preserved the central sampling lesson. Direct dielectric splitting passed, with family score 0.161 against threshold 1, while the damped direction cosine was only 0.657 against threshold 0.8. Direct target convergence therefore remained insufficient to guarantee parameter-sensitivity convergence. The run establishes local multi-epoch dielectric trainability, not a universal 60 ns direction budget.

The run also exposed a control-flow problem. The backend currently computes fresh loss and paired parent comparison only after the next-direction gate passes. Checkpoint 3 entered a fresh epoch and had direct point loss 5.6950, but its paired comparison with checkpoint 2 was skipped because the new direction failed. It was therefore unassessed rather than rejected. Checkpoint evaluation and readiness to take another step should be separated. [[wiki/questions/QST-0007-checkpoint-assessment-versus-next-direction-readiness]]

The full numerical chronology, KL behavior, parameter changes, interpretation, and limitations are recorded in [[wiki/answers/ffrefine-prospective-dielectric-damped-fisher-training]].

### Higher-KL sustained prospective result

Run `20260902-115818` retained the same reaction-field dielectric objective, complete ladder, 20 ns adaptive and 60 ns frozen-production budget, and $\gamma=0.1$ damped conditional-Fisher treatment. It raised the maximum conditional-KL target from 0.005 to 0.02 and the empirical archive-displacement ceiling from 0.1 to 0.2. This is a successful prospective configuration, not a matched causal demonstration that the larger KL values caused the improved continuation.

Seven optimization epochs completed and each accepted three supported microproposals. Checkpoints 1 through 6 were then evaluated on their next fresh archives. Their paired candidate-minus-parent intervals were all below zero, and paired reductions were 9.06%, 10.97%, 11.33%, 13.91%, 15.82%, and 9.94%. Fresh loss decreased monotonically from 7.3431 at checkpoint 0 to 3.6057 at checkpoint 6. Replay predicted the correct sign and similar magnitude for every update.

All six target temperatures moved toward experiment. Physical dielectric RMSE decreased from 43.36 to 30.38, but final residuals remained 23.81--35.27. The simulated 15-to-40 degrees Celsius decrease remained 20.25 dielectric units compared with 8.80 experimentally, showing that the run mostly corrected the curve level rather than its excessive temperature slope.

The damped chronological-half direction passed all seven completed epochs with conditional-Fisher cosine 0.8112--0.9789. Raw Euclidean gradients failed three epochs, while the hard-cut reporter failed epoch 7 at cosine 0.5999 when damping passed at 0.9355. All 21 accepted microproposals passed ESS and support gates. The lowest target-state ESS retention was 0.5098 against the 0.5 threshold, so the largest accepted move had little retention margin even though its absolute ESS remained 1182.7.

The exact empirical cumulative-KL audit was essential. Three accepted aligned proposals produced archive-to-candidate empirical KL 0.1202--0.1755, while a fourth remained above the 0.2 ceiling and was rejected. The sums of local quadratic estimates were only 0.0432--0.0585. [[wiki/claims/CLM-0039-trust-region-kl-must-match-replay-conditioning]]

Epoch 8 had passed adaptive readiness and parity when the user intentionally stopped the live run because the trainability evidence was sufficient. This is not a recorded scientific failure. Checkpoint 6 is the last fresh-validated state; checkpoint 7 has an 11.03% replay-predicted decrease but no fresh comparison.

## Aggressive density positive control

Density-only run `20260904-102939` tested whether a stable target could use a wider optimisation region: maximum conditional-KL target 0.1 per proposal, empirical archive ceiling 1.0, and target-state and candidate ESS-retention thresholds 0.25. Two macro-updates were accepted on fresh paired archives. Loss decreased from 143.6331 initially to 56.0352 and then 21.5935; the paired candidate-minus-parent intervals were [-118.4985, -71.6306] and [-52.2696, -36.6993]. Two terminal validations gave losses 20.0060 and 20.2560.

The accepted chains reached empirical archive KL 0.3006 and 0.3803. This shows that the earlier 0.2 ceiling is not a universal physical boundary: substantially larger displacements can remain useful when exact empirical KL, state-wise support, uncertainty, and fresh validation all agree. It does not show that the new thresholds are universally safe. In preceding run `20260903-220645`, a density update at archive KL 0.3030 could not establish a supported paired comparison on its fresh archive. The campaigns were not matched and do not identify which configuration or sampling difference caused the divergent outcomes.

The run also exercised the corrected checkpoint state model. Checkpoint 2 passed direct evaluation and paired comparison but failed readiness for another damped step after 30 ns, with cosine 0.728. It was retained as the best checkpoint and validated rather than discarded. Raw and hard-cut reporters passed on that extended archive, and the two later validation archives gave damped cosines 0.946 and 0.821. Direct-target reproducibility and next-direction readiness are therefore distinct even for density. [[wiki/questions/QST-0007-checkpoint-assessment-versus-next-direction-readiness]]

The full configuration, loss trajectory, KL/ESS evidence, direction diagnostics, and limitations are recorded in [[wiki/answers/ffrefine-aggressive-density-kl-ess-training]].

## Dielectric-estimator scope

FFRefine uses $\varepsilon_r=1+A$ for conducting PME and for Molly's current atom/site-pair reaction-field convention. The configured reaction-field dielectric changes the Hamiltonian but does not automatically require a second finite-boundary inversion in post-processing. [SRC-0075] [SRC-0076] [SRC-0077] [[wiki/concepts/dipole-moment-fluctuation-dielectric-constant]]

The completed 10 and 20 ns fresh-archive dielectric trainability scan used PME. The later matched two-independent-100 ns convergence experiment used the atom/site-pair reaction-field Hamiltonian and found a reproducible cumulative dielectric direction in that archive pair. It stopped at direction diagnosis and therefore still does not establish reaction-field replay improvement, fresh-simulation response, or closed-loop trainability, even though both electrostatics paths use the same operational $1+A$ estimator. [[wiki/answers/ffrefine-long-archive-target-gradient-convergence]]

## Audit and reporting lessons

- Report the maximum SNR among support-passing, KL-valid proposals separately from the maximum over all proposals. The latter can be dominated by extreme extrapolation.
- Persist every candidate row as it completes so an interrupted long scan remains auditable.
- Distinguish `gradient_failure`, `recovery_failure`, `inconclusive_sensitivity`, and `inconclusive_independent_signal`; do not label every unsuccessful synthetic test as a mathematics failure.
- Keep the TSS ladder invariant across target families. Experimental target sparsity changes scoring, not thermodynamic sampling.
- Require an independently simulated teacher signal before macro training, then require recovery on fresh validation replicas.
- Treat target tolerances and estimator uncertainty as separate quantities.

## Required next evidence

The next dielectric evidence should extend the successful prospective sequence without changing the selected geometry after observing the run:

1. Separate fresh checkpoint evaluation from readiness to construct the next direction. Compute the paired parent comparison whenever base observable/replay validity passes. [[wiki/questions/QST-0007-checkpoint-assessment-versus-next-direction-readiness]]
2. Allow an improved checkpoint to become the best checkpoint even when its archive cannot certify another update.
3. During final validation, retain direction diagnostics as reporters rather than objective-validity gates.
4. Freeze $\gamma=0.1$, the corrected conditional-KL policy, complete ladder, target definition, and parameter basis for the next repetition; do not retune them on run `20260901-171027`.
5. Predeclare whether a failed treated direction triggers longer continuation, another independent replica/archive, or termination.
6. Repeat the campaign with a new seed before estimating a success probability or claiming that 60 ns is sufficient.
7. Retain raw-gradient and hard-cut reporters so damping can be compared without allowing those reporters to veto the selected production treatment.
8. Add collateral density and RDF evaluation before interpreting the optimized parameters as an improved water model.
9. Continue treating enthalpy as unresolved; the dielectric result does not validate the same sampling budget or treatment for an energy-covariance target.

## Remaining gaps

- One independent archive pair produced a continuously accepted dielectric direction from 60 through 100 ns, but the minimum reproducible budget and campaign-to-campaign success rate remain unknown. Enthalpy did not converge under the production full-Fisher geometry by 100 ns, although its 100 ns raw independent-archive cosine and norm ratio passed.
- The full QEq-plus-bounded-parameter direction and replay-loss response reproduced across independent pooled archives, but the predefined empirical-KL and at-least-1% confidence gates did not both pass.
- The original fresh scans used different electrostatics, but the matched 100 ns reaction-field comparison removes that Hamiltonian difference from the density/RDF/enthalpy/dielectric direction diagnosis.
- Reaction-field dielectric has now shown two consecutive paired-confirmed fresh macro updates, but reliable continuation beyond them and convergence of the experimental curve remain unresolved.
- The higher-KL reaction-field run extended this to six consecutive paired-confirmed fresh updates. It establishes sustained local continuation in one additional trajectory, not a campaign-level success probability or a universal 60 ns budget.
- Candidate dielectric changes by temperature were not persisted in run `20260821-151000`; run `20260821-190105` corrected this reporting gap.
- The number and length of independently prepared archives needed to validate the full dielectric direction remain unknown. Two replicas sharing one TSS preparation did not substitute for independent directional evidence, and one 100 ns archive pair does not characterize between-campaign variability.
- The cross-observable run used one campaign seed and the long-archive run used one independent pair. Their dielectric directions require prospective repetition before a sampling allocation is selected.
- The retrospective treatment campaign added paired candidate-minus-baseline intervals. The production hard-Fisher and small-$\gamma$ dielectric proposals passed bidirectional cross-archive replay on the observed pair, but treatment selection and evaluation reused the same archives.
- The prospectively selected $\gamma=0.1$ treatment has passed fresh simulation, but it has not been compared against hard cutting in matched prospective arms.
- Checkpoint 3 from run `20260901-171027` lacks a paired parent comparison because the pipeline conflated checkpoint assessment with next-direction readiness.
- Checkpoint 7 from run `20260902-115818` lacks a fresh comparison because the user intentionally stopped the live run during epoch 8 after sufficient evidence had accumulated.
- The aggressive density thresholds have succeeded for one seed only; their repeatability and transfer to RDF or difficult average-observable targets remain unknown.
- No converged experimental dielectric optimization and no fresh-validated experimental enthalpy optimization have been established.
- No prospective hard-, damped-, identity-, or diagonal-conditioned enthalpy optimisation has passed held-out replay and fresh-simulation validation.

## Links

- [[wiki/answers/ffrefine-aggressive-density-kl-ess-training]]
- [[wiki/answers/ffrefine-prospective-dielectric-damped-fisher-training]]
- [[wiki/answers/ffrefine-retrospective-fisher-treatment-development]]
- [[wiki/answers/ffrefine-long-archive-target-gradient-convergence]]
- [[wiki/answers/ffrefine-water-temperature-replay-fresh-loss-gap]]
- [[wiki/answers/ffrefine-current-implementation-status]]
- [[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]]
- [[wiki/concepts/dipole-moment-fluctuation-dielectric-constant]]
- [[wiki/claims/CLM-0038-fixed-archive-gradient-validation-does-not-establish-fresh-archive-trainability]]
- [[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]
- [[wiki/questions/QST-0006-average-observable-trainability-sampling-budget]]
- [[wiki/questions/QST-0007-checkpoint-assessment-versus-next-direction-readiness]]
- [[wiki/claims/CLM-0009-observable-fitting-needs-held-out-validation]]
- [[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]
- [[wiki/questions/force-field-training-validation-scope]]
- [[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]
- [[wiki/sources/SRC-0023-statistically-optimal-analysis-multiple-equilibrium-states-mbar]]
