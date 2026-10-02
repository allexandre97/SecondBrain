---
type: answer
status: active
created: 2026-07-28
updated: 2026-10-02
question: "What does the FFRefine codebase currently implement, and what remains unvalidated?"
answer_status: answered
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/molecular-simulation/free-energy
  - research/adaptive-sampling
  - research/scientific-computing
tags:
  - ffrefine
  - force-field-optimization
  - replay-reweighting
  - times-square-sampling
  - mbar
  - water-models
  - implementation-status
related:
  - "[[wiki/answers/ffrefine-average-observable-trainability-validation]]"
  - "[[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]]"
  - "[[wiki/answers/ffrefine-paper-methods-knowledge-base]]"
  - "[[wiki/answers/ffrefine-water-temperature-replay-fresh-loss-gap]]"
  - "[[wiki/answers/adding-config-optimiser-to-ffrefine]]"
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
  - "[[wiki/concepts/tolerance-normalized-multi-observable-losses]]"
  - "[[wiki/concepts/free-energy-reweighting-for-force-field-fine-tuning]]"
  - "[[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]"
  - "[[wiki/questions/force-field-training-validation-scope]]"
  - "[[wiki/questions/QST-0010-damped-fisher-config-compatibility]]"
  - "[[wiki/claims/CLM-0038-fixed-archive-gradient-validation-does-not-establish-fresh-archive-trainability]]"
  - "[[wiki/claims/CLM-0039-trust-region-kl-must-match-replay-conditioning]]"
  - "[[wiki/claims/CLM-0040-damped-conditional-fisher-dielectric-training-survives-fresh-resimulation]]"
  - "[[wiki/questions/QST-0006-average-observable-trainability-sampling-budget]]"
  - "[[wiki/questions/QST-0007-checkpoint-assessment-versus-next-direction-readiness]]"
  - "[[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]"
  - "[[wiki/answers/ffrefine-direction-gates-and-production-policy]]"
  - "[[wiki/answers/ffrefine-improved-gates-water-run-lessons]]"
  - "[[wiki/answers/ffrefine-multi-series-equilibration-cut-calibration]]"
  - "[[wiki/questions/QST-0011-config-versus-weighted-sum-under-calibrated-direction-gates]]"
  - "[[wiki/questions/QST-0013-step-length-policy-after-family-exclusion]]"
  - "[[wiki/answers/molly-master-migration-constraints-for-ffrefine]]"
sources:
  - SRC-0018
  - SRC-0023
  - SRC-0036
sensitivity: public
encryption: none
wiki_pages_used:
  - "[[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]]"
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
  - "[[wiki/concepts/tolerance-normalized-multi-observable-losses]]"
  - "[[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]"
raw_sources_consulted: []
project_evidence:
  - "FFRefine repository audit on 2026-07-28"
  - "FFRefine ConFIG optimizer implementation and focused tests on 2026-07-28"
  - "FFRefine post-Fisher momentum implementation and focused tests on 2026-07-28"
  - "FFRefine water-temperature memory isolation implementation and focused tests on 2026-07-29"
  - "FFRefine fixed-archive enthalpy mathematics run 20260815-113946"
  - "FFRefine fixed-archive PME dielectric mathematics run 20260819-092631"
  - "FFRefine fresh-archive enthalpy/cutoff trainability run 20260819-194707"
  - "FFRefine fresh-archive dielectric/PME trainability run 20260820-092232"
  - "FFRefine dielectric-only damped-Fisher reaction-field water-temperature run 20260901-171027, completed 2026-09-02"
  - "FFRefine higher-KL dielectric-only damped-Fisher reaction-field water-temperature run 20260902-115818, intentionally stopped during epoch 8 on 2026-09-03 after six paired-confirmed fresh updates"
  - "FFRefine implementation audit on 2026-09-20: OptimiserSettings validation and water-temperature configuration correction"
  - "FFRefine damped-Fisher + ConFIG focused test rerun on 2026-09-21: 33/33 passed; focused damped-Fisher, ConFIG, and momentum tests reported passing"
  - "FFRefine clean HEAD audit on 2026-09-23 at a3b6aa552faab3b91271a1e7a9cabbc97793978a: ConFIG finite-step family regressions are reported, not individually vetoed; focused test/config_optimiser_checks.jl passed 33/33"
  - "FFRefine master audit on 2026-10-01 at 6b20031 (code read only; no tests re-run for this audit): block-based direction gates authoritative since commit 26affa0 and generic extend-or-exclude production policy since e49cfde (both 2026-09-30); generic configuration surface; history schema 34"
  - "FFRefine Molly AWHGrads-to-master migration analysis on 2026-10-02: static diffs plus small Julia probes against FFRefine's garnet force-field files, no completed port or fresh experiment run; see [[wiki/answers/molly-master-migration-constraints-for-ffrefine]]"
---

# FFRefine Current Implementation Status

## Short answer

**2026-10-01 update (master `6b20031`).** The direction-readiness and production-extension logic described in older FFRefine notes has been replaced. Since 2026-09-30, block-based, aggregation-aware direction gates decide which families the optimiser uses at each checkpoint (B = 8 jackknife blocks, a Monte Carlo calibrated size filter for ConFIG, and a cross-fitted aggregation-promise test for both ConFIG and weighted sum); the legacy chronological half-archive cosine/norm-ratio gate and the legacy delete-block reliability multiplier are gone. A generic extend-or-exclude production policy, shared by the water, hexane and solvation experiments, decides before any replay chain whether to optimise, extend once to rescue an excluded family, or stop; a checkpoint that cannot optimise ends the campaign at its "noise floor". All policies are configurable through one environment/config surface. Details are in the macro-epoch section below and in [[wiki/answers/ffrefine-direction-gates-and-production-policy]]. The rest of this short answer is the 2026-09-23 snapshot and remains accurate except where marked.

**2026-10-02 note.** The backend is still Molly's `AWHGrads` branch. A migration to Molly `master` was analysed (diffs plus small probes against FFRefine's own force-field files, not a completed port): a differently shaped parameter-gradient API with no charge support, a replay-archive logger that exists only on `AWHGrads`, missing unit/precision conversion helpers, small PME energy drift on fixed coordinates, alchemical-state semantics that change intermediate-λ energies (role renumbering, `intraLJ` default, and reaction-field/plain-Coulomb λ-scaling), and a pre-existing, branch-independent PME charge-gradient mismatch between Enzyme and finite differences. See [[wiki/answers/molly-master-migration-constraints-for-ffrefine]].

As of 2026-09-23 (FFRefine clean `master` HEAD `a3b6aa552faab3b91271a1e7a9cabbc97793978a`), FFRefine is a project-local Julia implementation for replay-based force-field fine tuning on top of Molly's `AWHGrads` branch, not a general Julia package. Its backend consumes completed user-owned TSS simulations, builds replay summaries and gradients, validates replay support, and runs replay-only parameter-proposal chains over named thermodynamic legs. The current implementation includes state-conditional Fisher geometry, continuously damped and hard-cut treatment operators, worst-state conditional-KL scaling, exact empirical cumulative-KL checks, fresh paired checkpoint assessment, distinct evaluation and next-direction readiness states, named-leg training, window-mixture MBAR replay, local TSS replay parity, QEq latent charge parameterization, bounded nonbonded trust regions, multi-target losses, split validation, ConFIG aggregation, optional post-Fisher momentum, and isolated macro-epoch workers.

The implemented experiment surfaces are ethanol solvation, water-temperature fitting, and hexane-temperature fitting (relative enthalpy and density targets; the hexane surface existed before 2026-09-23 but was omitted from that snapshot). Water-temperature fitting supports density, RDF, relative enthalpy, and dielectric targets selected through target-family configuration. Its current working-tree default is dielectric-only training with cutoff/reaction-field electrostatics and rigid water; PME remains selectable. Every target family uses the same exact 14 through 41 degrees Celsius TSS ladder, 28 states, original lambda schedule, window size 4, and 15 overlapping windows. Sparse experimental target temperatures affect scoring only, never the TSS ladder.

The validation status is no longer zero. Two prospective reaction-field dielectric-only campaigns now demonstrate local accepted-step quality under resimulation. The first produced two paired-confirmed updates and reproducible final-validation loss. The higher-KL campaign produced six consecutive paired-confirmed updates and reduced fresh dielectric loss by 50.90% through checkpoint 6. This is evidence of local dielectric trainability, not evidence of a transferable improved water model, multi-property balance, ethanol transfer, or robust convergence across systems and seeds. [[wiki/claims/CLM-0040-damped-conditional-fisher-dielectric-training-survives-fresh-resimulation]]

## Implemented architecture

FFRefine is split into a thin include surface (`ffrefine.jl`) and project-local modules:

- `replay.jl` implements TSS replay weights, local replay free energies, stitched TSS observable estimates, window-mixture MBAR references, MBAR target weights, replay archive validation, and logger extraction.
- `gradients.jl` builds Molly parameter-gradient contexts, injects candidate parameters into copied systems, checks archived reduced-potential parity, computes replay gradients for free energies and observables, forms candidate Fisher estimates, and provides replay caches and threaded replay controls.
- `parameterization.jl` maps unconstrained latent optimizer coordinates to physical Molly parameters. It supports QEq electronegativity and hardness latents, per-epoch relative bounds for non-QEq parameters, molecular charge constraints, topology-aware shared charge keys, multi-leg latent unions, Jacobian transforms, and QEq regularization.
- `optimiser.jl` defines tolerance-normalized targets, Huber and MSE objectives, family-weighted target aggregation, Fisher regularization, Jacobi preconditioning, eigenmode truncation, KL-scaled natural-gradient steps, family-level Fisher-whitened ConFIG aggregation, post-Fisher first-moment momentum, and replay line-search acceptance. Under ConFIG, family loss regressions are recorded as diagnostics, not independent line-search vetoes; aggregate loss, support, and KL constraints still apply.
- `validity.jl` implements replay/TSS parity diagnostics, TSS readiness diagnostics, ESS policies for local replay and MBAR replay, Fisher validity checks, split summaries, parity recovery actions, replica-stratified jackknife blocks, the per-series equilibration-cut estimator with its calibrated materiality table, and TSS simulation extension helpers.
- `backend.jl` is the sampler-agnostic FFRefine boundary. It consumes named TSS states, completed simulations, and parameter contexts; summarizes replay frames; evaluates replay, ESS, Fisher, and split diagnostics; computes full-objective fresh losses with per-family jackknife standard errors; runs the direction gates; and (since 2026-09-30) calls an optimisation callback so that the production decision is taken before any replay chain. The chain optimises only the families the gates made eligible.
- `direction_gates.jl` (added 2026-09-28, deciding since 2026-09-30) implements block pseudo-values, family size statistics, Monte Carlo multipliers, the cross-fitted aggregation-promise test with ConFIG and weighted-sum removal loops, and the promise-drift test.
- `production_decision.jl` (added 2026-09-30) implements the generic extend-or-exclude policy: rescue sizing by expected value, α-spending for the rescue look, measured production and re-evaluation costs, and persistent-exclusion warnings.
- `configuration.jl` (added 2026-09-30) resolves every policy field from `<PREFIX>_<GROUP>_<FIELD>` environment variables, nested config, legacy flat keys, or defaults, and writes each resolved value and its source to the run metadata.
- `epoch_pipeline.jl` and `epoch_worker.jl` run each macro epoch in a fresh Julia worker process, record fresh losses, fresh comparisons, replay calibration and exclusion cycles, repeat or end direction-unready epochs, and run final-validation replicas.
- `solvation_pipeline.jl` contains shared experiment machinery for alchemical TSS systems, PME/Ewald-aware alchemical interactions, target definitions, solvation-cycle helpers, replay proposal policy, the `ArchiveGradientPolicy` and `EquilibrationPolicy` definitions, and the per-replica equilibration report.
- `optimisation_history.jl` and `reporting.jl` record parameter states, line-search trials, MBAR diagnostics, validity diagnostics, optimizer aggregation diagnostics, component losses, gradient cosines, and concise terminal progress.

## Experiment surfaces

### Ethanol solvation

`solvation.jl` defines a two-leg thermodynamic cycle with `:solvated` and `:vacuum` legs. It builds ethanol-in-water and vacuum ethanol TSS systems, uses alchemical lambda states from 1 to 0, validates adaptive readiness with frozen parity probes, collects production replay archives, then calls `evaluate_optimisation_epoch`. The default active training target is ethanol solvation free energy in kJ/mol with a standard-state correction. A solvated density observable and target are defined, but the density training target is commented out in the default `TRAINING_TARGETS` list.

The ethanol parameter-training setup includes QEq charge latents for ethanol and water in the solvated leg and ethanol only in the vacuum leg. It also includes bounded sigma, epsilon, and double-exponential softcore alpha/beta parameters. Shared parameter names couple matching parameters across legs; parameters absent from one leg contribute only through the legs where they exist.

### Water-temperature fitting

`water_temperature.jl` defines one `:water` leg on the exact integer ladder from 14 through 41 degrees Celsius. Its target family and nonbonded method are configurable. The current working-tree default is dielectric-only, cutoff/reaction-field electrostatics, and rigid water; PME remains selectable. Density targets span the full ladder, relative enthalpy uses the lowest-temperature state as reference, dielectric has experimental targets at 15, 20, 25, 30, 35, and 40 degrees Celsius, and Soper HH, HO, and OO RDF targets are evaluated at 25 degrees Celsius. In every case TSS retains all 28 states, the original lambda schedule, window size 4, and 15 overlapping windows.

The script assembles training, split-validation, monitored-prediction, and curve-writing surfaces from the selected family so a diagnostic run cannot silently optimize one family while reporting another. It logs ladder coverage, target-specific curves, active parameter CSVs, memory/history diagnostics, and supports checkpoint/resume.

After a 2026-07-29 memory update, water macro epochs can run in isolated Julia worker processes. This is an operational safeguard for long replay/resimulation loops: worker-local memory telemetry can remain high until exit, so the relevant reclamation diagnostic is the supervisor's RSS after the worker has exited, recorded in `epoch_workers.csv`. The implementation lesson is that explicit garbage collection and workspace reuse can reduce peak allocation but may not force Julia/native allocator RSS back down after PME, threaded replay, FFT, and automatic-differentiation-heavy optimization; process exit is the reliable memory boundary.

## Macro-epoch control flow (2026-10-01, master `6b20031`)

Each macro epoch of every experiment runs adaptive TSS until its readiness criterion passes, a frozen parity probe, and a frozen-bias production archive (water default 60 ns, environment-configurable; the 2026-09-30 water campaigns used 50 ns with up to five 10 ns extensions). `evaluate_optimisation_epoch` then builds window-mixture MBAR replay summaries and evaluates, in order:

1. evaluation validity (replay/TSS parity, ESS, split validation) and Fisher validity;
2. the full-objective fresh loss, with per-family losses and delete-block standard errors;
3. the report-only equilibration cut (water only);
4. the direction gates, when evaluation and Fisher are valid, using leave-one-block-out targets from 8 replica-stratified blocks;
5. an independent fresh-loss comparison with the parent checkpoint and a backward replay comparison, both diagnostic only (`evaluation_accepted` equals `evaluation_valid`; a significant fresh regression raises a warning event);
6. the production decision (`production_decision` via `evaluate_and_decide`): optimise, extend once (invalid evaluation, gates that could not run, a gating promise drift, or a rescue chosen by expected value), or stop (`:stop_unrescuable` stops at once instead of spending extensions);
7. only for "optimise": the KL-bounded natural-gradient replay chain (ConFIG or weighted sum) on the eligible families, with the enforced loss gate, if configured, applied after the chain.

The next epoch's fresh archive measures what the chain achieved. The campaign continues only when the chain accepted at least one proposal; a direction-unready checkpoint is repeated at unchanged parameters up to `max_unready_epochs` (default 0) and otherwise ends the campaign with reason `:noise_floor` (or `:gates_not_evaluated`), listing suggested production times. Final-validation replicas then evaluate the latest checkpoint. Stale fresh-loss epochs are recorded but nothing stops on them; the `early_stopping_patience` config key is not read by the pipeline.

Notable current defaults: gate $\alpha=0.05$, `drift_mode = :report`, Monte Carlo promise calibration; water's `max_production_extensions` defaults to 0 (no extension or rescue is possible unless it is configured). Water uses ConFIG with damped Fisher ($\gamma=0.1$) and `momentum_beta = 0`; hexane uses ConFIG with `momentum_beta = 0.25`; solvation uses weighted sum with `momentum_beta = 0.5`. The aggregation is set by `<PREFIX>_GRADIENT_AGGREGATION`, then the experiment config, then `:weighted_sum`. The optimisation-history schema is version 34.

Report-only diagnostics kept alongside: chain-level replay calibration with telescoping cumulative standard errors, step-to-family angles, exclusion cycles, per-family fresh losses, full-objective-scale loss reporting (the step itself still renormalises weights over included families; see [[wiki/questions/QST-0013-step-length-policy-after-family-exclusion]]), and an early/late pseudo-value cosine for comparison with the legacy gate. See [[wiki/answers/ffrefine-direction-gates-and-production-policy]] for the gate statistics, the rescue rule, α-spending, lessons, provisional campaign evidence, and differences between the design document and the code.

## Optimizer aggregation status

The shared optimizer now supports two gradient aggregation policies. `:weighted_sum` remains the default scalar objective path. `:config` enables exact family-level Fisher-whitened ConFIG, using the same regularized, Jacobi-scaled, eigen-truncated Fisher factorization as the natural-gradient step. This is important because ConFIG's local conflict-free condition must be checked in the geometry of the step FFRefine actually takes, not in Euclidean gradient space before Fisher preconditioning.

ConFIG protects loss families rather than individual RDF bins at the direction-construction stage. QEq regularization is included as a protected component only when active. The aggregate ConFIG direction is checked for first-order descent in each protected component, but a finite replay step may worsen one or more family losses: such regressions are reported in `failed_components` and do not independently veto acceptance. Candidate loss must still meet the aggregate-loss rule, and support/ESS and KL constraints remain in force. This implementation remains an adaptation of SRC-0036 to the SRC-0018 replay/Fisher setting, not a source-validated scientific result. The latest FFRefine commit records this policy change (commit `a3b6aa5`, 2026-09-23); focused regression test `test/config_optimiser_checks.jl` passes 33/33.

The shared optimizer also supports chain-local first-moment momentum after the Fisher solve for both `:weighted_sum` and `:config` aggregation. The momentum state is stored in latent parameter coordinates as accepted line-search displacements, projected into the current retained Fisher eigenspace, KL-bounded with the current Fisher metric, and reset after complete rejection or new frozen-reference ensembles. For ConFIG, reuse is limited component-wise so an aggregate-aligned previous step cannot become uphill for a protected family. This is an FFRefine implementation lesson rather than an Adam or M-ConFIG claim from SRC-0036. The `OptimiserSettings` default is `momentum_beta = 0.5`; damped Fisher requires `momentum_beta = 0`. Since 2026-09-30 the direction gates certify the aggregated step without momentum, so with momentum enabled (hexane and solvation defaults) the step taken is not exactly the certified one.

### Damped-Fisher/ConFIG compatibility and diagnostics

`OptimiserSettings` now includes `fisher_damping_gamma` and permits `fisher_damping_gamma != nothing` with `gradient_aggregation == :config`, while still requiring `momentum_beta == 0`. `fisher_factorization` uses the damped modal gains consistently in ConFIG's whitening factor, so the family-level aggregate and natural-gradient step share the selected regularized Fisher geometry. Hard-reference diagnostics compare against hard-cut ConFIG, not a weighted-sum reference. Raw and capped KL diagnostics use the selected Fisher metric and conditional metric.

`test/fisher_damping_checks.jl` covers constructor, numerical, conditional-KL, ConFIG, hard-reference, and reporting behavior. The focused rerun `source .env && TMPDIR=/tmp julia +1.11 --startup-file=no test/fisher_damping_checks.jl` passed 33/33; focused damped-Fisher, ConFIG, and momentum tests are also reported as passing. The earlier water run exposed a stale `WATER_TEMPERATURE_CONFIG` selection of `:config` alongside damped Fisher and was corrected before this implementation. [[wiki/questions/QST-0010-damped-fisher-config-compatibility]]

## Replay and estimator status

FFRefine has two TSS replay modes with different roles:

- Local window replay followed by TSS stitching is used for replay/TSS parity against the TSS-reported free-energy surface. This preserves the window-local structure of frozen TSS and remains the right readiness diagnostic.
- Window-mixture MBAR uses frozen TSS windows as sampled MBAR states, solves a sampled-window reference denominator, and treats physical rungs or candidate force-field states as unsampled targets. This is used consistently for optimization free energies, optimized observables, gradients, candidate ESS, and Fisher estimates when MBAR summaries are used.

This distinction is important: MBAR connectivity allows every archived frame to contribute to every target in principle, but it does not create new phase-space support. Per-target ESS, candidate ESS, source-window weight mass, overlap connectivity, replay/TSS parity, split disagreement, and resimulation remain acceptance diagnostics. [SRC-0018]

## Validation status

**2026-10-01 note.** The first campaigns in which the new gates decide (one ConFIG and one weighted-sum water run with rdf, density and dielectric, started 2026-09-30) were still running at 6 epochs; their provisional evidence is recorded in [[wiki/answers/ffrefine-direction-gates-and-production-policy]] and [[wiki/questions/QST-0011-config-versus-weighted-sum-under-calibrated-direction-gates]]. No focused test suites were re-run for the 2026-10-01 audit; the statements below about test results refer to their own dates.

For paper-methods details on the exact loss, target definitions, replay estimators, latent parameterization, optimizer, and validation gates, see [[wiki/answers/ffrefine-paper-methods-knowledge-base]].

The codebase contains focused tests for parameterization, ESS policy, validity diagnostics, backend alignment, reporting, PME gradient/threading behavior, water-temperature target assembly, ConFIG aggregation, and post-Fisher momentum guards. These support implementation correctness of specific components, including finite-difference gradient checks, MBAR/source-window behavior, KL rebounding, line-search momentum storage, and a component-wise ConFIG momentum counterexample.

Controlled fixed-archive checks now support the value/gradient/recovery mathematics for relative enthalpy and conducting-boundary PME dielectric permittivity. Both obtained prediction-gradient relative errors near $3\times10^{-5}$, loss-gradient relative errors below $6\times10^{-4}$, near-unit gradient cosines, large loss reduction, and accurate recovery of a 0.1% teacher shift. The old enthalpy artifact's `math_failure` label came from an overly strict normalized-RMSE cutoff, not failed gradient agreement; the harness now distinguishes gradient failure from recovery failure. [[wiki/answers/ffrefine-average-observable-trainability-validation]]

The original 10 ns and 20 ns coordinate scans did not establish fresh-archive trainability. Later conditional-Fisher development and prospective macro optimization changed the dielectric conclusion. Run `20260901-171027` produced two paired-confirmed fresh improvements and two consistent final-validation replicas. Run `20260902-115818` produced six consecutive paired-confirmed fresh improvements; checkpoint-0 to checkpoint-6 fresh loss fell from 7.3431 to 3.6057. All six target temperatures moved toward experiment, all accepted proposals passed support, and the selected damped direction passed every completed optimization archive. The user intentionally stopped the live run during epoch 8 after sufficient evidence had accumulated; this is not a recorded scientific failure. [[wiki/answers/ffrefine-prospective-dielectric-damped-fisher-training]]

The positive result remains narrowly scoped. Checkpoint 7 has not been assessed on a completed fresh archive, the terminal validation replicas were not reached in the higher-KL campaign, the dielectric curve remains substantially above experiment and too steep with temperature, and collateral density, RDF, enthalpy, and stability properties were not evaluated. Experimental enthalpy trainability remains unresolved.

The current status is implementation validation plus a local scientific proof of concept for dielectric-only training. The 2026-09-23 optimizer change revises only finite-step family-regression acceptance: ConFIG's first-order component-direction guard remains, while finite-step family decreases are not guaranteed or required. The 33/33 damped-Fisher checks and focused ConFIG/momentum tests validate implementation behavior, not scientific or production performance of the combined damped-Fisher + ConFIG method. No multi-family replay/fresh-resimulation campaign has validated that combined method. `CLM-0040` is limited to fresh-resimulation evidence for the damped conditional-Fisher dielectric protocol and does not validate ConFIG. Do not promote this to water-model validation, multi-property balance, transferability, or robust convergence. The durable positive claim is restricted to repeated fresh-resimulation dielectric descent under the tested damped conditional-Fisher reaction-field protocol.

## Links

- [[wiki/answers/adding-config-optimiser-to-ffrefine]]
- [[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]]
- [[wiki/answers/ffrefine-paper-methods-knowledge-base]]
- [[wiki/answers/ffrefine-average-observable-trainability-validation]]
- [[wiki/concepts/awh-replay-force-field-optimization]]
- [[wiki/concepts/tolerance-normalized-multi-observable-losses]]
- [[wiki/concepts/free-energy-reweighting-for-force-field-fine-tuning]]
- [[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]
- [[wiki/claims/CLM-0038-fixed-archive-gradient-validation-does-not-establish-fresh-archive-trainability]]
- [[wiki/claims/CLM-0039-trust-region-kl-must-match-replay-conditioning]]
- [[wiki/claims/CLM-0040-damped-conditional-fisher-dielectric-training-survives-fresh-resimulation]]
- [[wiki/questions/QST-0006-average-observable-trainability-sampling-budget]]
- [[wiki/questions/QST-0007-checkpoint-assessment-versus-next-direction-readiness]]
- [[wiki/questions/force-field-training-validation-scope]]
- [[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]
- [[wiki/sources/SRC-0036-config-towards-conflict-free-training-of-physics-informed]]
- [[wiki/answers/ffrefine-direction-gates-and-production-policy]]
- [[wiki/answers/ffrefine-improved-gates-water-run-lessons]]
- [[wiki/answers/ffrefine-multi-series-equilibration-cut-calibration]]
- [[wiki/questions/QST-0011-config-versus-weighted-sum-under-calibrated-direction-gates]]
- [[wiki/questions/QST-0013-step-length-policy-after-family-exclusion]]
- [[wiki/answers/molly-master-migration-constraints-for-ffrefine]]
