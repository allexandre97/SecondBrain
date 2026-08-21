---
type: answer
status: active
created: 2026-08-20
updated: 2026-08-21
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
  - "[[wiki/answers/ffrefine-water-temperature-replay-fresh-loss-gap]]"
  - "[[wiki/answers/ffrefine-current-implementation-status]]"
  - "[[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]]"
  - "[[wiki/concepts/dipole-moment-fluctuation-dielectric-constant]]"
  - "[[wiki/claims/CLM-0038-fixed-archive-gradient-validation-does-not-establish-fresh-archive-trainability]]"
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
  - "FFRefine fixed-archive enthalpy mathematics run 20260815-113946"
  - "FFRefine fixed-archive PME dielectric mathematics run 20260819-092631"
  - "FFRefine fresh-archive enthalpy/cutoff trainability run 20260819-194707"
  - "FFRefine fresh-archive dielectric/PME trainability run 20260820-092232"
  - "FFRefine focused water-temperature, mathematics, and trainability tests on 2026-08-20"
  - "FFRefine reaction-field dielectric full-gradient campaign 20260821-124443"
  - "FFRefine cross-fitted reaction-field dielectric campaign revision on 2026-08-21"
graph_neighborhoods_used:
  - "tools/query_graph.py --start wiki/answers/ffrefine-water-temperature-replay-fresh-loss-gap --depth 2"
---

# FFRefine Average-Observable Trainability Validation

## Short answer

No. The August 2026 checks establish two narrower results.

First, the implemented enthalpy and conducting-boundary PME dielectric estimators, replay gradients, loss gradients, and fixed-archive recovery mathematics pass controlled synthetic checks. This substantially weakens the hypothesis that the earlier training failures were caused by an algebraic error in how ensemble-average targets were differentiated.

Second, fresh 10 ns and 20 ns TSS production archives did **not** contain any tested single-parameter perturbation that simultaneously produced a five-standard-error target signal, passed replay support, and stayed within the configured cumulative KL limit. Therefore the current workflow has not established closed-loop trainability of either property. It established a sensitivity/support limitation under the tested archive lengths, parameter basis, positive coordinate perturbations, and trust-region thresholds.

The correct conclusion is neither “the mathematics is broken” nor “enthalpy and permittivity are fundamentally untrainable.” The controlled mathematics works, while the fresh archives do not yet identify a statistically supported and independently reproducible training direction. A later reaction-field test of the whole QEq-plus-bounded-parameter gradient found an archive-local supported loss decrease, but the paired confidence test was inconclusive and the result did not reproduce as an accepted direction across independent archives.

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

## Dielectric-estimator scope

FFRefine uses $\varepsilon_r=1+A$ for conducting PME and for Molly's current atom/site-pair reaction-field convention. The configured reaction-field dielectric changes the Hamiltonian but does not automatically require a second finite-boundary inversion in post-processing. [SRC-0075] [SRC-0076] [SRC-0077] [[wiki/concepts/dipole-moment-fluctuation-dielectric-constant]]

The completed fresh-archive dielectric trainability scan used PME. It therefore does not establish trainability under the atom/site-pair reaction-field Hamiltonian. A reaction-field trainability claim would require a separate fresh-archive experiment with its Hamiltonian and provenance reported, even though the same operational $1+A$ estimator is used.

## Audit and reporting lessons

- Report the maximum SNR among support-passing, KL-valid proposals separately from the maximum over all proposals. The latter can be dominated by extreme extrapolation.
- Persist every candidate row as it completes so an interrupted long scan remains auditable.
- Distinguish `gradient_failure`, `recovery_failure`, `inconclusive_sensitivity`, and `inconclusive_independent_signal`; do not label every unsuccessful synthetic test as a mathematics failure.
- Keep the TSS ladder invariant across target families. Experimental target sparsity changes scoring, not thermodynamic sampling.
- Require an independently simulated teacher signal before macro training, then require recovery on fresh validation replicas.
- Treat target tolerances and estimator uncertainty as separate quantities.

## Required next evidence

The next scientifically useful step is not an unconstrained experimental macro run. It is to establish a supported teacher direction:

1. Generate independent baseline archives at the same checkpoint to measure between-run variation in target values, jackknife errors, and candidate SNR.
2. Run the four-archive cross-fitted whole-gradient reaction-field experiment described above without weakening its paired-confidence, support, gradient-reproducibility, or KL gates.
3. If it is inconclusive, compare more independent replicas with longer replicas at matched total cost; dielectric fluctuations may have long correlation times, so frame count alone is not an effective-sample-size guarantee.
4. Once a candidate passes the cross-fitted replay screen, simulate at least two independent teacher archives, combine within- and between-archive uncertainty, and require independent SNR of at least 5.
5. Only then run whole-parameter synthetic macro recovery with two fresh final-validation replicas.
6. Treat experimental training as a later test. A synthetic recovery failure must be resolved before experimental mismatch is interpreted as a force-field limitation.

## Remaining gaps

- The sampling length or replica count required to make either average observable identifiable is unknown.
- The full QEq-plus-bounded-parameter basis produced one supported archive-local response, but its paired confidence and independent reproducibility remain unestablished.
- The enthalpy fresh scan used cutoff/reaction-field electrostatics, while the dielectric scan used PME; the results do not isolate Hamiltonian dependence.
- Reaction-field dielectric whole-gradient trainability remains unresolved; the completed campaign stopped at the direction stage.
- No eligible direction reached the independent-teacher or macro-recovery stages.
- No full experimental enthalpy or dielectric optimization has been validated.

## Links

- [[wiki/answers/ffrefine-water-temperature-replay-fresh-loss-gap]]
- [[wiki/answers/ffrefine-current-implementation-status]]
- [[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]]
- [[wiki/concepts/dipole-moment-fluctuation-dielectric-constant]]
- [[wiki/claims/CLM-0038-fixed-archive-gradient-validation-does-not-establish-fresh-archive-trainability]]
- [[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]
- [[wiki/questions/QST-0006-average-observable-trainability-sampling-budget]]
- [[wiki/claims/CLM-0009-observable-fitting-needs-held-out-validation]]
- [[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]
- [[wiki/questions/force-field-training-validation-scope]]
- [[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]
- [[wiki/sources/SRC-0023-statistically-optimal-analysis-multiple-equilibrium-states-mbar]]
