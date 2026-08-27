---
type: answer
status: active
created: 2026-07-28
updated: 2026-08-20
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
  - "[[wiki/claims/CLM-0038-fixed-archive-gradient-validation-does-not-establish-fresh-archive-trainability]]"
  - "[[wiki/questions/QST-0006-average-observable-trainability-sampling-budget]]"
  - "[[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]"
sources:
  - SRC-0018
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
---

# FFRefine Current Implementation Status

## Short answer

As of 2026-08-20, FFRefine is a project-local Julia implementation for replay-based force-field fine tuning on top of Molly's `AWHGrads` branch, not a general Julia package. Its backend consumes completed user-owned TSS simulations, builds replay summaries and gradients, validates replay support, and can run replay-only natural-gradient proposal chains over named thermodynamic legs. The code now implements more than the original route plan: named-leg training, window-mixture MBAR replay, local TSS replay parity, QEq latent charge parameterization, bounded nonbonded parameter trust regions, Huber or MSE tolerance-normalized multi-target losses, split validation, ESS/Fisher gates, opt-in Fisher-whitened ConFIG aggregation, post-Fisher first-moment momentum, optimisation history, and two experiment surfaces.

The implemented experiment surfaces are ethanol solvation (`solvation.jl`) and water-temperature fitting (`water_temperature.jl`). Ethanol uses solvated and vacuum TSS legs and trains the solvation free-energy target by default; the density target is present but commented out. Water-temperature fitting supports density, RDF, relative enthalpy, and dielectric targets selected through target-family configuration. Its current default is an enthalpy-only diagnostic configuration using cutoff/reaction-field electrostatics and rigid water; PME remains selectable. Every target family uses the same exact 14 through 41 degrees Celsius TSS ladder, 28 states, original lambda schedule, window size 4, and 15 overlapping windows. Sparse experimental target temperatures affect scoring only, never the TSS ladder.

The wiki should not present FFRefine as production-validated. Focused tests and reduced smoke tests cover many numerical pieces, but the current audit did not find evidence of a complete production optimization run demonstrating improved water properties, improved ethanol solvation transfer, accepted-step quality under resimulation, or general robustness across systems. Those remain validation questions.

## Implemented architecture

FFRefine is split into a thin include surface (`ffrefine.jl`) and project-local modules:

- `replay.jl` implements TSS replay weights, local replay free energies, stitched TSS observable estimates, window-mixture MBAR references, MBAR target weights, replay archive validation, and logger extraction.
- `gradients.jl` builds Molly parameter-gradient contexts, injects candidate parameters into copied systems, checks archived reduced-potential parity, computes replay gradients for free energies and observables, forms candidate Fisher estimates, and provides replay caches and threaded replay controls.
- `parameterization.jl` maps unconstrained latent optimizer coordinates to physical Molly parameters. It supports QEq electronegativity and hardness latents, per-epoch relative bounds for non-QEq parameters, molecular charge constraints, topology-aware shared charge keys, multi-leg latent unions, Jacobian transforms, and QEq regularization.
- `optimiser.jl` defines tolerance-normalized targets, Huber and MSE objectives, family-weighted target aggregation, Fisher regularization, Jacobi preconditioning, eigenmode truncation, KL-scaled natural-gradient steps, opt-in family-level Fisher-whitened ConFIG aggregation, post-Fisher first-moment momentum, protected-family line-search guards, and line-search acceptance.
- `validity.jl` implements replay/TSS parity diagnostics, TSS readiness diagnostics, ESS policies for local replay and MBAR replay, Fisher validity checks, split summaries, production recovery decisions, and TSS simulation extension helpers.
- `backend.jl` is the sampler-agnostic FFRefine boundary. It consumes named TSS states, completed simulations, and parameter contexts; summarizes replay frames; evaluates replay, ESS, Fisher, and split diagnostics; and only runs optimisation when those gates pass.
- `solvation_pipeline.jl` contains shared experiment machinery for alchemical TSS systems, PME/Ewald-aware alchemical interactions, target definitions, solvation-cycle helpers, and replay proposal policy.
- `optimisation_history.jl` and `reporting.jl` record parameter states, line-search trials, MBAR diagnostics, validity diagnostics, optimizer aggregation diagnostics, component losses, gradient cosines, and concise terminal progress.

## Experiment surfaces

### Ethanol solvation

`solvation.jl` defines a two-leg thermodynamic cycle with `:solvated` and `:vacuum` legs. It builds ethanol-in-water and vacuum ethanol TSS systems, uses alchemical lambda states from 1 to 0, validates adaptive readiness with frozen parity probes, collects production replay archives, then calls `evaluate_optimisation_epoch`. The default active training target is ethanol solvation free energy in kJ/mol with a standard-state correction. A solvated density observable and target are defined, but the density training target is commented out in the default `TRAINING_TARGETS` list.

The ethanol parameter-training setup includes QEq charge latents for ethanol and water in the solvated leg and ethanol only in the vacuum leg. It also includes bounded sigma, epsilon, and double-exponential softcore alpha/beta parameters. Shared parameter names couple matching parameters across legs; parameters absent from one leg contribute only through the legs where they exist.

### Water-temperature fitting

`water_temperature.jl` defines one `:water` leg on the exact integer ladder from 14 through 41 degrees Celsius. Its target family and nonbonded method are configurable. The current default is enthalpy-only, cutoff/reaction-field electrostatics, and rigid water; PME is available for dielectric checks. Density targets span the full ladder, relative enthalpy uses the lowest-temperature state as reference, dielectric has experimental targets at 15, 20, 25, 30, 35, and 40 degrees Celsius, and Soper HH, HO, and OO RDF targets are evaluated at 25 degrees Celsius. In every case TSS retains all 28 states, the original lambda schedule, window size 4, and 15 overlapping windows.

The script assembles training, split-validation, monitored-prediction, and curve-writing surfaces from the selected family so a diagnostic run cannot silently optimize one family while reporting another. It logs ladder coverage, target-specific curves, active parameter CSVs, memory/history diagnostics, and supports checkpoint/resume.

After a 2026-07-29 memory update, water macro epochs can run in isolated Julia worker processes. This is an operational safeguard for long replay/resimulation loops: worker-local memory telemetry can remain high until exit, so the relevant reclamation diagnostic is the supervisor's RSS after the worker has exited, recorded in `epoch_workers.csv`. The implementation lesson is that explicit garbage collection and workspace reuse can reduce peak allocation but may not force Julia/native allocator RSS back down after PME, threaded replay, FFT, and automatic-differentiation-heavy optimization; process exit is the reliable memory boundary.

## Optimizer aggregation status

The shared optimizer now supports two gradient aggregation policies. `:weighted_sum` remains the default scalar objective path. `:config` enables exact family-level Fisher-whitened ConFIG, using the same regularized, Jacobi-scaled, eigen-truncated Fisher factorization as the natural-gradient step. This is important because ConFIG's local conflict-free condition must be checked in the geometry of the step FFRefine actually takes, not in Euclidean gradient space before Fisher preconditioning.

ConFIG protects loss families rather than individual RDF bins. QEq regularization is included as a protected component only when active, and candidate callbacks must expose candidate values/support/parameterization so the central line search can reject finite steps that improve the scalar objective while worsening a protected family. This implementation remains an adaptation of SRC-0036 to the SRC-0018 replay/Fisher setting, not a source-validated scientific result.

The shared optimizer also supports chain-local first-moment momentum after the Fisher solve for both `:weighted_sum` and `:config` aggregation. The momentum state is stored in latent parameter coordinates as accepted line-search displacements, projected into the current retained Fisher eigenspace, KL-bounded with the current Fisher metric, and reset after complete rejection or new frozen-reference ensembles. For ConFIG, reuse is limited component-wise so an aggregate-aligned previous step cannot become uphill for a protected family. This is an FFRefine implementation lesson rather than an Adam or M-ConFIG claim from SRC-0036.

## Replay and estimator status

FFRefine has two TSS replay modes with different roles:

- Local window replay followed by TSS stitching is used for replay/TSS parity against the TSS-reported free-energy surface. This preserves the window-local structure of frozen TSS and remains the right readiness diagnostic.
- Window-mixture MBAR uses frozen TSS windows as sampled MBAR states, solves a sampled-window reference denominator, and treats physical rungs or candidate force-field states as unsampled targets. This is used consistently for optimization free energies, optimized observables, gradients, candidate ESS, and Fisher estimates when MBAR summaries are used.

This distinction is important: MBAR connectivity allows every archived frame to contribute to every target in principle, but it does not create new phase-space support. Per-target ESS, candidate ESS, source-window weight mass, overlap connectivity, replay/TSS parity, split disagreement, and resimulation remain acceptance diagnostics. [SRC-0018]

## Validation status

For paper-methods details on the exact loss, target definitions, replay estimators, latent parameterization, optimizer, and validation gates, see [[wiki/answers/ffrefine-paper-methods-knowledge-base]].

The codebase contains focused tests for parameterization, ESS policy, validity diagnostics, backend alignment, reporting, PME gradient/threading behavior, water-temperature target assembly, ConFIG aggregation, and post-Fisher momentum guards. These support implementation correctness of specific components, including finite-difference gradient checks, MBAR/source-window behavior, KL rebounding, line-search momentum storage, and a component-wise ConFIG momentum counterexample.

Controlled fixed-archive checks now support the value/gradient/recovery mathematics for relative enthalpy and conducting-boundary PME dielectric permittivity. Both obtained prediction-gradient relative errors near $3\times10^{-5}$, loss-gradient relative errors below $6\times10^{-4}$, near-unit gradient cosines, large loss reduction, and accurate recovery of a 0.1% teacher shift. The old enthalpy artifact's `math_failure` label came from an overly strict normalized-RMSE cutoff, not failed gradient agreement; the harness now distinguishes gradient failure from recovery failure. [[wiki/answers/ffrefine-average-observable-trainability-validation]]

Fresh-archive trainability remains unresolved. Across 72 candidate perturbations per property over 10 ns and sequentially extended 20 ns archives, neither cutoff/reaction-field enthalpy nor PME dielectric produced an eligible direction under SNR at least 5, replay support, and empirical KL at most 0.02. The best valid 20 ns SNRs were 0.1121 and 0.08847 respectively. Large raw SNRs occurred only far outside support. The workflow therefore stopped with `inconclusive_sensitivity` before independent teacher generation or macro optimization. This is evidence of insufficient local identifiability under the tested archive, basis, and trust region, not evidence that the formulas are wrong or the properties fundamentally untrainable. [[wiki/claims/CLM-0038-fixed-archive-gradient-validation-does-not-establish-fresh-archive-trainability]]

The current status is still implementation-validation, not scientific validation. Do not claim that FFRefine has demonstrated production improvement of ethanol solvation, water density/RDF/dielectric balance, transferability, or robust convergence. The durable claim remains narrower: FFRefine now implements a replay-optimization framework capable of testing the SRC-0018 idea with TSS and MBAR-style replay, provided the resulting updates pass support and resimulation checks.

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
- [[wiki/questions/QST-0006-average-observable-trainability-sampling-budget]]
- [[wiki/questions/force-field-training-validation-scope]]
- [[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]
- [[wiki/sources/SRC-0036-config-towards-conflict-free-training-of-physics-informed]]
