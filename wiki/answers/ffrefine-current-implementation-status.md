---
type: answer
status: active
created: 2026-07-28
updated: 2026-07-28
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
  - "[[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]]"
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
  - "[[wiki/concepts/tolerance-normalized-multi-observable-losses]]"
  - "[[wiki/concepts/free-energy-reweighting-for-force-field-fine-tuning]]"
  - "[[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]"
  - "[[wiki/questions/force-field-training-validation-scope]]"
  - "[[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]"
sources:
  - SRC-0018
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
---

# FFRefine Current Implementation Status

## Short answer

As of 2026-07-28, FFRefine is a project-local Julia implementation for replay-based force-field fine tuning on top of Molly's `AWHGrads` branch, not a general Julia package. Its backend consumes completed user-owned TSS simulations, builds replay summaries and gradients, validates replay support, and can run replay-only natural-gradient proposal chains over named thermodynamic legs. The code now implements more than the original route plan: named-leg training, window-mixture MBAR replay, local TSS replay parity, QEq latent charge parameterization, bounded nonbonded parameter trust regions, Huber or MSE tolerance-normalized multi-target losses, split validation, ESS/Fisher gates, optimisation history, and two experiment surfaces.

The implemented experiment surfaces are ethanol solvation (`solvation.jl`) and water-temperature fitting (`water_temperature.jl`). Ethanol uses solvated and vacuum TSS legs and trains the solvation free energy target by default; the density target is present but commented out. Water-temperature fitting uses one temperature-ladder TSS leg with PME by default and trains density, RDF, and dielectric targets, while split validation currently checks density and RDF but leaves dielectric split checks commented out.

The wiki should not present FFRefine as production-validated. Focused tests and reduced smoke tests cover many numerical pieces, but the current audit did not find evidence of a complete production optimization run demonstrating improved water properties, improved ethanol solvation transfer, accepted-step quality under resimulation, or general robustness across systems. Those remain validation questions.

## Implemented architecture

FFRefine is split into a thin include surface (`ffrefine.jl`) and project-local modules:

- `replay.jl` implements TSS replay weights, local replay free energies, stitched TSS observable estimates, window-mixture MBAR references, MBAR target weights, replay archive validation, and logger extraction.
- `gradients.jl` builds Molly parameter-gradient contexts, injects candidate parameters into copied systems, checks archived reduced-potential parity, computes replay gradients for free energies and observables, forms candidate Fisher estimates, and provides replay caches and threaded replay controls.
- `parameterization.jl` maps unconstrained latent optimizer coordinates to physical Molly parameters. It supports QEq electronegativity and hardness latents, per-epoch relative bounds for non-QEq parameters, molecular charge constraints, topology-aware shared charge keys, multi-leg latent unions, Jacobian transforms, and QEq regularization.
- `optimiser.jl` defines tolerance-normalized targets, Huber and MSE objectives, family-weighted target aggregation, Fisher regularization, Jacobi preconditioning, eigenmode truncation, KL-scaled natural-gradient steps, and line-search acceptance.
- `validity.jl` implements replay/TSS parity diagnostics, TSS readiness diagnostics, ESS policies for local replay and MBAR replay, Fisher validity checks, split summaries, production recovery decisions, and TSS simulation extension helpers.
- `backend.jl` is the sampler-agnostic FFRefine boundary. It consumes named TSS states, completed simulations, and parameter contexts; summarizes replay frames; evaluates replay, ESS, Fisher, and split diagnostics; and only runs optimisation when those gates pass.
- `solvation_pipeline.jl` contains shared experiment machinery for alchemical TSS systems, PME/Ewald-aware alchemical interactions, target definitions, solvation-cycle helpers, and replay proposal policy.
- `optimisation_history.jl` and `reporting.jl` record parameter states, line-search trials, MBAR diagnostics, validity diagnostics, and concise terminal progress.

## Experiment surfaces

### Ethanol solvation

`solvation.jl` defines a two-leg thermodynamic cycle with `:solvated` and `:vacuum` legs. It builds ethanol-in-water and vacuum ethanol TSS systems, uses alchemical lambda states from 1 to 0, validates adaptive readiness with frozen parity probes, collects production replay archives, then calls `evaluate_optimisation_epoch`. The default active training target is ethanol solvation free energy in kJ/mol with a standard-state correction. A solvated density observable and target are defined, but the density training target is commented out in the default `TRAINING_TARGETS` list.

The ethanol parameter-training setup includes QEq charge latents for ethanol and water in the solvated leg and ethanol only in the vacuum leg. It also includes bounded sigma, epsilon, and double-exponential softcore alpha/beta parameters. Shared parameter names couple matching parameters across legs; parameters absent from one leg contribute only through the legs where they exist.

### Water-temperature fitting

`water_temperature.jl` defines a one-leg `:water` temperature ladder from 14 to 41 degrees Celsius. It builds a PME water system by default, uses a TSS grid over temperatures, and trains against experimental density values, Soper RDF tables at 25 degrees Celsius for HH/HO/OO pairs, and dielectric constants at selected ladder temperatures. Density, RDF, and dielectric are separate target families with configurable family weights; the current constants give RDF a larger family coefficient than density or dielectric. RDF bin weights are distributed over first shell, second shell, and tail regions within each pair type.

Water split validation currently includes density and RDF checks. Dielectric split checks are present in the source but commented out, so dielectric contributes to the training loss without an enabled split-half validation gate. The script logs ladder coverage, writes density/RDF/dielectric curves, writes active parameter CSVs, and supports checkpoint/resume.

## Replay and estimator status

FFRefine has two TSS replay modes with different roles:

- Local window replay followed by TSS stitching is used for replay/TSS parity against the TSS-reported free-energy surface. This preserves the window-local structure of frozen TSS and remains the right readiness diagnostic.
- Window-mixture MBAR uses frozen TSS windows as sampled MBAR states, solves a sampled-window reference denominator, and treats physical rungs or candidate force-field states as unsampled targets. This is used consistently for optimization free energies, optimized observables, gradients, candidate ESS, and Fisher estimates when MBAR summaries are used.

This distinction is important: MBAR connectivity allows every archived frame to contribute to every target in principle, but it does not create new phase-space support. Per-target ESS, candidate ESS, source-window weight mass, overlap connectivity, replay/TSS parity, split disagreement, and resimulation remain acceptance diagnostics. [SRC-0018]

## Validation status

The codebase contains focused tests for parameterization, ESS policy, validity diagnostics, backend alignment, reporting, PME gradient/threading behavior, and water-temperature target assembly. These support implementation correctness of specific components, including finite-difference gradient checks and MBAR/source-window behavior.

The current status is still implementation-validation, not scientific validation. Do not claim that FFRefine has demonstrated production improvement of ethanol solvation, water density/RDF/dielectric balance, transferability, or robust convergence. The durable claim remains narrower: FFRefine now implements a replay-optimization framework capable of testing the SRC-0018 idea with TSS and MBAR-style replay, provided the resulting updates pass support and resimulation checks.

## Links

- [[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]]
- [[wiki/concepts/awh-replay-force-field-optimization]]
- [[wiki/concepts/tolerance-normalized-multi-observable-losses]]
- [[wiki/concepts/free-energy-reweighting-for-force-field-fine-tuning]]
- [[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]
- [[wiki/questions/force-field-training-validation-scope]]
- [[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]
