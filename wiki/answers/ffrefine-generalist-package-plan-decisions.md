---
type: answer
status: active
created: 2026-10-11
updated: 2026-10-12
question: "How did the 2026-10-11 FFRefine planning session decide to sequence turning FFRefine into a generalist package, migrate it to Molly `master`, and divide work between FFRefine and Molly, and why?"
answer_status: answered
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/molecular-simulation/free-energy
  - research/molecular-simulation/molecular-dynamics
  - research/scientific-computing
tags:
  - ffrefine
  - molly
  - software-architecture
  - migration
  - project-decision
related:
  - "[[wiki/answers/ffrefine-current-implementation-status]]"
  - "[[wiki/answers/molly-master-migration-constraints-for-ffrefine]]"
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
  - "[[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]]"
  - "[[wiki/answers/ffrefine-direction-gates-and-production-policy]]"
  - "[[wiki/answers/ffrefine-loss-gate-diagnostic-policy]]"
  - "[[wiki/questions/QST-0011-config-versus-weighted-sum-under-calibrated-direction-gates]]"
  - "[[wiki/concepts/molly-jl-simulation-package-facts]]"
sources: []
sensitivity: public
encryption: none
wiki_pages_used:
  - "[[wiki/answers/ffrefine-current-implementation-status]]"
  - "[[wiki/answers/molly-master-migration-constraints-for-ffrefine]]"
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
raw_sources_consulted: []
wiki_pages_updated:
  - "[[wiki/answers/ffrefine-current-implementation-status]]"
  - "[[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]]"
  - "[[wiki/answers/molly-master-migration-constraints-for-ffrefine]]"
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
  - "[[wiki/answers/ffrefine-direction-gates-and-production-policy]]"
  - "[[wiki/answers/ffrefine-loss-gate-diagnostic-policy]]"
  - "[[wiki/questions/QST-0011-config-versus-weighted-sum-under-calibrated-direction-gates]]"
  - "[[wiki/concepts/molly-jl-simulation-package-facts]]"
project_evidence:
  - "FFRefine repository planning document `ffrefine_package_plan.md`, dated 2026-10-11 (an audit-and-plan document, not a literature source), covering sequencing (its section 2), the Molly-master audit (3.2), target design (4), the Molly work list (6), code streamlining (7), and the decisions table (10)"
  - "FFRefine repository document `molly_master_migration.md`, the earlier (2026-10-02) frozen catalogue of AWHGrads-to-master breakages with probe evidence, referenced by the planning document as MIG"
  - "Molly.jl `master` at commit `587d3644` (2026-10-02)"
  - "FFRefine commit `d48d2f1` (2026-07-16, \"Group charges by atom type\")"
  - "FFRefine commit `110fe64` (2026-10-07, \"Damped Levenberg-Marquardt trust-region step; report-only direction gates\")"
scope: snapshot
currency: current
as_of: 2026-10-11
as_of_commit:
  - FFRefine@110fe64
  - Molly@587d3644
---

# FFRefine Generalist-Package Plan: 2026-10-11 Decisions

## Question

How did the 2026-10-11 FFRefine planning session decide to sequence (a) turning FFRefine into a package, (b) migrating its Molly.jl backend from `AWHGrads` to `master`, and (c) generalising its API, and what did it decide about the user-facing API, fit targets, thermodynamic cycles, the Molly-versus-FFRefine work split, and the long-standing per-epoch subprocess design?

## Short answer

On 2026-10-11, FFRefine's planning document decided a four-phase sequence: **Phase 0** builds a package shell on Molly `AWHGrads` with no behaviour change, after recording baselines and pruning unused code; **Phase 1** migrates the package to Molly `master`; **Phase 2** builds a generic, Molly-mirroring user API; **Phase 3** proves generality on an unseen system and prepares publication. The rationale is that the migration changes numerics (validated against `AWHGrads` baselines with the code structure fixed) while the generalisation changes structure (validated by old code and new code agreeing on the same Molly), so doing both at once would leave differences unattributable; a generic API built on `AWHGrads` would also be thrown away once the migration replaces its underlying types.

The session also decided: the user-facing API should mirror Molly's own conventions (users build `System`s, `ThermoState`s and TSS-style ensemble settings themselves, keyword-constructed, with one verb `refine!` analogous to `simulate!`, and no `ENV` reads in the library); that a Molly logger declares what to measure rather than supplying data, so FFRefine re-evaluates the logger's observable function on archived frames at proposed parameters; that Molly currently has no thermodynamic-cycle abstraction and FFRefine should add one to Molly as a reusable, estimator-agnostic type; and a list of Molly-side changes (U1-U7) gated by whether a change is useful to Molly users on its own. All decisions are FFRefine project evidence and project design, dated 2026-10-11, not literature claims.

## Detailed answer

### A. Sequencing: package, then migrate, then generalise, then publish

**Decided (A).** The planning document rejects doing the Molly `master` migration and the generalisation to a public API as one combined change. Two reasons are given:

- **Each change needs a fixed reference.** The migration changes numerics: the reaction-field electrostatic λ path, intra-solute steric annihilation-versus-decoupling, small PME energy drift (about $2\times10^{-6}$ relative), and the `float_type_high` accumulation default. It should be validated against `AWHGrads` baselines with the code structure held fixed. The generalisation changes structure (a new public API replacing the three experiment drivers), and should be validated by old code and new code agreeing on the same Molly version. Doing both at once would leave any observed difference unattributable to either cause.
- **A generic API built on `AWHGrads` would be throwaway.** It would be built around types that disappear in the migration (FFRefine's own `ParameterSet`-like container and its `AWHGrads`-only `TSSReplayLogger`). Only a mechanical package shell is worth building before the migration.

The four phases, with Molly backend and exit gate:

| Phase | Molly backend | Goal | Exit gate |
|---|---|---|---|
| 0 Shell | `AWHGrads`, pinned | Package skeleton, no behaviour change; baselines recorded; unused code pruned | Tests give the same pass/fail set as the pre-package scripts; baselines stored |
| 1 Migrate | `master` commits including Molly PRs U1-U3 | The same three experiments (ethanol solvation, water-temperature, hexane-temperature) run on `master` | Energy/gradient parity against Phase-0 baselines within migration tolerances; replay parity from fresh runs; one short GPU TSS run |
| 2 Generalise | `master` | Public API; the three drivers become examples | Examples reproduce Phase-1 results (deterministic parts to round-off, stochastic parts within noise) |
| 3 Prove and publish | released Molly | A new, previously unused system runs; `ThermodynamicCycle` (U6) replaces FFRefine's λ builder | A new system runs with no edits to the package source; docs build |

Some infrastructure needed by both the migration and the eventual generic package (the parameter container, charge injection, the system converter, a replay-capture format) is designed in its final public form during Phase 1, so it is written once rather than migrated and then rewritten.

### B. User-API principles mirroring Molly

The target design adopts Molly's own conventions rather than a custom configuration surface:

- **The user owns the physics.** Users construct `System`s, force fields, integrators, couplers, and the thermodynamic-state ladder themselves (e.g. a list of `ThermoState`s), exactly as they would for a plain Molly simulation; FFRefine never builds a force field or chooses an integrator.
- **One verb, `refine!`,** analogous to Molly's `simulate!`, runs a fitting problem (ensembles, targets, parameters, and a trust-region algorithm) for a number of epochs, writing checkpoints and history, with resume support.
- **Keyword-constructed structs,** composition over configuration files, extension through multiple dispatch — again mirroring Molly's own style.
- **No `ENV` reads in the library.** GPU selection follows Molly's own convention (the system's `array_type`); a `settings_from_env` helper for batch scripts is kept outside the core library.

This is FFRefine project design (planning document section 4.1), not yet implemented as of 2026-10-11.

### C. Fit targets, Molly loggers, and gradients of averages

**A logger is a declaration, not a data source.** Target observables are declared with ordinary Molly loggers (any `GeneralObservableLogger`, whose contract is a function `f(sys, neighbors, step_n, buffers; n_threads)`), and the logger also runs during production as an ordinary monitoring logger. But FFRefine does not read fitting values from the logger's own recorded output. Instead it takes the logger's underlying observable function and re-evaluates it on archived replay frames, using a CPU, unitless, Float64 copy of the *target state's* system with candidate parameters θ injected. This recomputation is required both to evaluate the observable at a proposed θ (which the original production run never sampled at) and to differentiate it with Enzyme.

**Gradient of an average.** For an ensemble average $\langle A\rangle_s$ at state $s$ under parameters $\theta$ (reduced units):

$$
\partial_\theta\langle A\rangle_s=\langle\partial_\theta A\rangle_s-\mathrm{Cov}_s\!\left(A,\ \partial_\theta u_s\right).
$$

The direct term $\langle\partial_\theta A\rangle_s$ comes from Enzyme differentiating through the observable function itself (skipped when the observable is declared parameter-independent, e.g. density, volume, coordinate, or box wrappers); the covariance term accounts for how a parameter change reweights which configurations are sampled.

**Where loggers live (decided, L).** Target loggers attach to the FFRefine ensemble object (planned as `TSSEnsemble(...; loggers)`), mirroring how `TSSSimulation(...; loggers)` takes them on Molly `master`. This is necessary because Molly `master` ignores loggers placed on a `ThermoState`'s own `System` in generalized-ensemble runs (TSS, AWH, and REMD alike): Molly's loggers are run per replica and follow the replica across physical states, rather than being attached per state, so a logger declared on one `ThermoState`'s system would not reliably record that state's observable.

### D. `ThermodynamicCycle`: a planned, estimator-agnostic Molly addition

Molly `master` (`587d3644`) has no thermodynamic-cycle abstraction; cycles currently appear only as prose and diagrams in its free-energy documentation, not as code. The planning document proposes adding `ThermodynamicCycle` and `Leg` to Molly itself (work item U5, Phase 2), with each leg specifying a source, a pair of states (by index or name), a coefficient (usually ±1), and an overall cycle holding legs plus an explicit correction term (standard-state, restraint-release, or long-range corrections). The abstraction is estimator-agnostic: a leg's `source` is anything implementing `free_energy_difference` (and an uncertainty counterpart) between two of its states. Molly would implement this interface for `TSSState` and for an MBAR result; FFRefine adds its own replay-estimator implementation at a candidate θ, plus a `free_energy_gradient` method (the existing annihilation free-energy gradient, generalised to any pair of states rather than only the TSS ladder's endpoints).

This generalises FFRefine's current cycle prediction, which is restricted to the ladder's first and last states (`[1, n_states]`) and which bakes in `solvated`/`vacuum` leg labels and module-level `T0`/`P0` globals for its standard-state correction. The new design allows any pair of states per leg, an explicit (not global) correction, and per-leg temperature/unit conversion, raising an error if legs disagree on temperature when that matters. Binding-cycle restraint-release corrections are left as a hook only, with no implementation planned yet.

### E. The Molly-side work list and its criterion

**Decided (B, K).** A change belongs in Molly if it is useful to Molly users on its own; FFRefine-specific logic (the replay archive format, replay estimators, charge models, and target gradients) stays in FFRefine. Because the user is a Molly developer, Molly changes are explicitly in scope when justified, landing as ordinary Molly PRs with Molly's own tests, with FFRefine then moving its pinned Molly commit.

| ID | Change | Phase | Status |
|---|---|---|---|
| U1 | A generic per-sample TSS hook (`TSSSimulation(...; sample_loggers)`, called once per collected sample with the replica, active system, active state/window, the window's reduced potentials, `log_den`, and weights) | 1 (blocking) | Decided (B): a generic hook in Molly; FFRefine owns the archive format built from it. Replaces porting the `AWHGrads`-only `TSSReplayLogger`/`tss_replay_archive` upstream as-is. |
| U2 | System-level unit stripping, float-type conversion, and device transfer | 1 | Not yet decided whether this lands in Molly or stays a local FFRefine converter; master may have dropped these deliberately. |
| U3 | Unit-aware `extract_parameters`/`ParameterPlan`/`inject_gradients` | 1 | Planned; replaces an FFRefine-side unitless-only workaround. |
| U4 | Parameter-prefix namespacing, or an explicit error on collision | 2 | FFRefine checks for collisions itself until this lands. |
| U5 | `ThermodynamicCycle` plus `free_energy_difference` for `TSSState` and MBAR | 2 | See section D above. |
| U6 | A `to_lambda_function` conversion from FFRefine's double-exponential (DEXP) soft-core alchemical potential to Molly's `DoubleExponentialSoftCore`, plus whatever else is needed so Molly's `AbsoluteFESystem` can reproduce FFRefine's own λ ladder (λ convention, soft-core α = 0.85, vacuum leg) | 3 | Prerequisite for retiring FFRefine's own λ-ladder builder (decision E, below). |
| U7 | Charge parameters keyed by atom type (`atom_<type>_charge`), the same keying Molly already uses for σ/ϵ | 1 (not blocking) | **Decided (K): a separate Molly PR**, starting with an investigation of how a charge slot fits Molly's parameter-injection machinery and how it interacts with Ewald/PME exclusions and alchemical charge scaling. Once merged, it replaces FFRefine's own charge-injection layer; `ChargeModel`/QEq logic stays in FFRefine, mapping onto Molly's own charge parameters. |

(U8, MBAR accepting `+Inf` reduced potentials as zero support, and M6, `AlchemicalPartition` input validation, are optional, non-blocking items not elaborated here.)

### F. All decisions, dated 2026-10-11

| Decision | Topic | What was decided |
|---|---|---|
| A | Sequencing | Package (Phase 0) -> migrate (Phase 1) -> generalise (Phase 2) -> prove and publish (Phase 3); see section A. |
| B | Shape of U1 | A generic TSS per-sample hook in Molly; FFRefine owns the archive it builds from that hook. |
| L | Where target loggers live | On the FFRefine ensemble, mirroring `TSSSimulation(...; loggers)`, because Molly ignores loggers on a `ThermoState`'s own system in generalized-ensemble runs; see section C. |
| F | Electrostatic λ path (reaction-field/plain-Coulomb pair scaling) | Accept Molly `master`'s pair-scaling convention (pair energy ∝ λ) rather than reproducing `AWHGrads`' per-charge scaling (pair energy ∝ λ²). |
| E | Ethanol λ ladder | Keep FFRefine's own alchemical-ladder builder until Molly's alchemical setup (via U6) can reproduce it; only then retire the local builder. |
| P | Process isolation | Keep one subprocess per macro epoch as the production default; see section G. |
| C | Checkpoints | A breaking change: checkpoint/run formats from before the package cannot be resumed after the migration. |
| S | Inputs | Not tracked in version control until the paper's experiments are fixed; package tests use synthetic fixtures and Molly's own bundled example data instead. |
| R | Canonical regime | A damped Levenberg-Marquardt trust-region step with weighted-sum gradient aggregation (see [[wiki/answers/ffrefine-current-implementation-status]] for the implementation-status consequences). |
| D | Report-only diagnostics | Keep only diagnostics that are necessary (decide something) or genuinely informative; remove the rest (see [[wiki/answers/ffrefine-current-implementation-status]]). |
| K | Per-type charges in Molly (U7) | A separate Molly PR, starting with an investigation; FFRefine keeps local charge injection until it merges. |
| H | Repository hygiene | Deferred until the architecture is stable; cleanup may happen in this repository or in a new one. |
| Q | QEq hardness default | **Open.** Keep today's behaviour for now: no gauge fixing; hardness is a bounded latent inside per-epoch QEq bounds, and regularisation is set per experiment (off for water and hexane, default for solvation). Garnet 2.0 may need charge equilibration with a different parameterisation, so the per-type electronegativity/hardness redundancy result (see [[wiki/answers/qeq-per-type-electronegativity-hardness-redundancy]]) may not carry over, and `ChargeModel` is kept as an extension point so Garnet 2.0 could plug in a different default. To be decided before the Phase 2 parameter-layer work. |
| N | Package name | **Open.** `FFRefine` is the current working name; it may be too close to the unrelated `MDRefine` project. A rename before registration is considered mechanical (module name, `Project.toml` name, examples; the package UUID can stay). To be decided before Phase 3 documentation. |

Decisions R and D (the canonical regime and report-only diagnostic policy) are tracked in [[wiki/answers/ffrefine-decision-register]] (FFR-029 to FFR-040), with their effect on the code described in [[wiki/answers/ffrefine-current-implementation-status]], since they concern what the running code currently does and is planned to stop doing, rather than the package/migration architecture covered here.

### G. Process-isolation rationale (P), not previously recorded

FFRefine has long run one disposable worker subprocess per macro epoch in production, but the reason was not previously written down anywhere in SecondBrain. The 2026-10-11 planning document records it for the first time: **the per-epoch subprocess was introduced to contain inter-epoch memory leaks and unpredictable segmentation faults.** The user's own investigation pointed at an interaction between PME, multithreading, and Enzyme automatic differentiation as the likely cause, though the planning document does not describe that investigation's method or evidence in more detail; it is recorded here as the stated rationale, not as a separately validated root-cause analysis.

The subprocess-per-epoch design is confirmed as still the reliable production default (decision P): the supervisor starts a worker that re-runs the same user script with an environment flag set, under which `refine!` executes exactly one epoch before the worker exits; an in-process mode is kept only for tests and debugging. Whether running one continuous process is now safe is explicitly left open as a secondary check (planned as a later work package), not resolved by this planning session.

## Sources used

None (no literature source). All content is FFRefine project evidence and project design from the 2026-10-11 planning document and the earlier 2026-10-02 migration catalogue, both listed in this page's frontmatter.

## Wiki pages used

- [[wiki/answers/ffrefine-current-implementation-status]]
- [[wiki/answers/molly-master-migration-constraints-for-ffrefine]]
- [[wiki/concepts/awh-replay-force-field-optimization]]

## Wiki updates made

- Added this answer note.
- Updated [[wiki/answers/ffrefine-current-implementation-status]] with the canonical-regime status and planned-but-not-yet-implemented removals.
- Added a 2026-10-11 lessons entry to [[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]] (since moved to [[wiki/answers/ffrefine-decision-register]] / the route plan's Evidence timeline).
- Corrected the charge-key description and added the AbsoluteFESystem/DEXP/logger facts in [[wiki/answers/molly-master-migration-constraints-for-ffrefine]].
- Corrected the fourth implementation lesson in [[wiki/concepts/awh-replay-force-field-optimization]] to mark molecular-template charge keys as superseded by atom-type charge keys (production since 2026-07-16, commit `d48d2f1`).
- Added 2026-10-11 status notes to [[wiki/answers/ffrefine-direction-gates-and-production-policy]] and [[wiki/answers/ffrefine-loss-gate-diagnostic-policy]], and to [[wiki/questions/QST-0011-config-versus-weighted-sum-under-calibrated-direction-gates]] (since moved to [[wiki/answers/ffrefine-decision-register]] / the route plan's Evidence timeline).
- Added a new Molly-facts concept page, [[wiki/concepts/molly-jl-simulation-package-facts]].

## Remaining gaps

- As of 2026-10-11, none of Phase 0 through Phase 3 has started in code; this page records planning decisions only. The canonical-regime removals (direction gates, ConFIG, momentum, the natural-gradient path, the archive KL budget, Huber loss) are decided but not yet implemented.
- Decisions Q (QEq hardness default) and N (package name) are open.
- The process-isolation rationale (P) is recorded as the planning document's stated reason; the underlying PME/multithreading/Enzyme investigation itself is not described in enough detail here to be independently checked.
- Whether U2 (system conversion) lands in Molly or stays a local FFRefine converter is undecided.
