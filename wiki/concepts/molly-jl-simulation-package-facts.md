---
type: concept
status: active
created: 2026-10-11
updated: 2026-10-11
areas:
  - research
categories:
  - research/molecular-simulation/molecular-dynamics
  - research/molecular-simulation/free-energy
  - research/scientific-computing
tags:
  - molly
  - julia
  - molecular-dynamics
  - free-energy
  - automatic-differentiation
related:
  - "[[wiki/answers/molly-master-migration-constraints-for-ffrefine]]"
  - "[[wiki/answers/ffrefine-generalist-package-plan-decisions]]"
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
sources: []
sensitivity: public
encryption: none
scope: snapshot
currency: current
as_of: 2026-10-02
as_of_commit:
  - Molly@587d3644
---

# Molly.jl Simulation Package: Facts Relevant to FFRefine

## Summary

Molly.jl is the Julia molecular-simulation package FFRefine builds on. This page records implementation facts about Molly's `master` branch (commit `587d3644`, 2026-10-02) that are reusable beyond FFRefine's own codebase: its logger contract, its handling of loggers under generalized-ensemble sampling, its alchemical free-energy types, and its parameter-naming convention. These are software-architecture facts about a specific, dated Molly commit, observed as FFRefine project evidence (reading Molly's source and probing it), not literature claims about a published Molly paper.

## Key Points

- **No thermodynamic-cycle abstraction.** Molly `master` has no `ThermodynamicCycle` type or equivalent; free-energy cycles (e.g. a solvation or binding cycle built from legs with coefficients) appear only as prose and diagrams in Molly's documentation, not as code. See [[wiki/answers/ffrefine-generalist-package-plan-decisions]] for a proposed Molly addition that would close this gap.
- **Every built-in scalar logger is a `GeneralObservableLogger`.** Its contract is a function with signature `observable(sys, neighbors, step_n, buffers; n_threads)::T`. Built-in loggers such as `DensityLogger`, `PotentialEnergyLogger`, `VolumeLogger`, `TemperatureLogger`, and the virial loggers are all thin wrappers around a function of this shape, so any custom scalar or vector observable can be declared the same way, with `GeneralObservableLogger(f, T, n_steps)`.
- **Loggers on a `ThermoState`'s own system are ignored by generalized-ensemble methods.** In TSS, AWH, and replica-exchange (REMD) runs, Molly runs loggers per replica: a logger follows the replica as it moves across physical states, rather than being tied to, and recording, one particular state. A logger attached to an individual `ThermoState`'s `System` is therefore silently not invoked in these generalized-ensemble sampling modes; loggers must instead be attached to the ensemble/simulation object itself (e.g. `TSSSimulation(...; loggers)`).
- **`AbsoluteFESystem` and `RelativeFESystem` exist, with `set_lambda!`,** and eight built-in λ schedulers, giving native alchemical free-energy support on `master` that did not exist in the same form on the earlier `AWHGrads` branch.
  - **Convention:** λ = 0 is the coupled (physical) end and λ = 1 is the decoupled (ghost) end; atoms being alchemically removed are given the `DeleteRole`; dual topology (`dual=true`) is required.
  - **`AbsoluteFESystem` cannot currently convert a double-exponential (DEXP) soft-core potential.** Building the λ-dependent interaction calls `to_lambda_function` on every pairwise interaction type; methods exist for Lennard-Jones, Coulomb, reaction-field Coulomb (CRF), and Ewald Coulomb, but no `to_lambda_function` method exists for `DoubleExponential`, even though a `DoubleExponentialSoftCore` alchemical type exists on the receiving end. A system using a DEXP-based force field therefore cannot be built through `AbsoluteFESystem` as-is; a conversion method would need to be added.
- **Interactions of the same family share one parameter-name prefix.** For example, every Coulomb-type interaction (plain Coulomb, reaction-field Coulomb, Ewald Coulomb) shares the prefix `inter_CO_`, and both the plain and soft-core double-exponential interactions share `inter_DEXP_`. Molly's `extract_parameters` keeps only the first value seen per shared prefix, so two distinct Coulomb-family interactions present in the same system would be silently tied together under one shared parameter unless the caller checks for and rejects the collision.

## Evidence

All points above were established by project-level source reading and small Julia probes against Molly `master` commit `587d3644` (2026-10-02), run as part of FFRefine's migration investigation and 2026-10-11 package-planning session; see [[wiki/answers/molly-master-migration-constraints-for-ffrefine]] and [[wiki/answers/ffrefine-generalist-package-plan-decisions]] for the fuller context and for FFRefine-specific consequences (e.g. why FFRefine attaches target loggers to its own ensemble object rather than to individual `ThermoState` systems).

## Links

- [[wiki/answers/molly-master-migration-constraints-for-ffrefine]]
- [[wiki/answers/ffrefine-generalist-package-plan-decisions]]
- [[wiki/concepts/awh-replay-force-field-optimization]]

## Open Questions

- Whether Molly upstream would accept a `to_lambda_function(::DoubleExponential, ::SoftCore)` method, a generic `ThermodynamicCycle` abstraction, parameter-prefix collision detection, or a generic per-sample TSS hook is a question for Molly's own maintainers, not resolved on this page; FFRefine's planning intends to propose these as separate Molly pull requests (see [[wiki/answers/ffrefine-generalist-package-plan-decisions]]).
