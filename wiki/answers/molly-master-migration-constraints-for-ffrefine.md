---
type: answer
status: active
created: 2026-10-02
updated: 2026-10-15
question: "What must change for FFRefine to run on Molly's `master` branch instead of Molly's `AWHGrads` branch, and why?"
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
  - enzyme
  - autodiff
  - parameter-gradients
  - alchemical-free-energy
  - pme
  - migration
related:
  - "[[wiki/answers/ffrefine-current-implementation-status]]"
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
  - "[[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]]"
  - "[[wiki/answers/ffrefine-paper-methods-knowledge-base]]"
  - "[[wiki/questions/md-free-energy-decoupling-implementation-validation]]"
  - "[[wiki/claims/CLM-0023-decoupling-implementations-must-preserve-intramolecular-solute-terms]]"
  - "[[wiki/questions/QST-0014-pme-charge-gradient-enzyme-vs-finite-difference-mismatch]]"
  - "[[wiki/answers/ffrefine-generalist-package-plan-decisions]]"
  - "[[wiki/concepts/molly-jl-simulation-package-facts]]"
  - "[[wiki/answers/ffrefine-decision-register]]"
sources: []
sensitivity: public
encryption: none
wiki_pages_used:
  - "[[wiki/answers/ffrefine-current-implementation-status]]"
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
raw_sources_consulted: []
wiki_pages_updated:
  - "[[wiki/questions/md-free-energy-decoupling-implementation-validation]]"
  - "[[wiki/questions/QST-0014-pme-charge-gradient-enzyme-vs-finite-difference-mismatch]]"
  - "[[wiki/answers/ffrefine-current-implementation-status]]"
  - "[[wiki/answers/ffrefine-decision-register]]"
project_evidence:
  - "FFRefine project investigation, 2026-10-02: static diffs between Molly AWHGrads head `e122c88b` (2026-07-31) and Molly master head `587d3644` (2026-10-02); merge base `491668ae` (AWHGrads has 50 commits not on master, master has 184 not on AWHGrads); compared against FFRefine commit `6b20031`, which currently runs only on AWHGrads"
  - "FFRefine project probes, 2026-10-02: small Julia probe scripts (not kept; scripts were temporary) built with FFRefine's own garnet force-field XMLs and PDBs, run on CPU in Float64 against both Molly checkouts"
  - "Full project-local write-up: `molly_master_migration.md` in the FFRefine repository root"
  - "FFRefine project probes, 2026-10-15: CPU, Float64 probes against Molly master `623d314a` plus the unmerged system-conversion PR branch (U2, head `0e4b8819`), using FFRefine's garnet-force-field water (2661 atoms), hexane, and ethanol systems built as FFRefine's own drivers build them (Float32 unitful, then converted to Float64 unitless with `grad_safe=true`); covered the PME charge-gradient Enzyme-vs-finite-difference question (QST-0014), PME/Enzyme thread safety, PME energy parity against the Phase 0 baselines, and a parameter-container benchmark on garnet ethanol (6282 atoms, DEXP+RF, 223 keys)"
  - "FFRefine refactor step 13a, 2026-10-15 (working tree on top of commit `68a2aae`, not yet committed): pinned Molly to master `ac3ede15856d2ac8da18cbc7325a3fa49aaa8f0f` in `Project.toml` `[sources]`, re-seeding the Manifest from the default environment then `Pkg.resolve()`; implemented `FFParameterSet`/`ParameterSchema`/`atom_parameter_indices` in `src/molly_compat.jl`; `julia +1.12 --project=. -e 'using FFRefine'` loads; `test/parameter_container_checks.jl` passes 156/156; full write-up in `refactor/LOG.md`, \"Step 13a\", in the FFRefine repository"
scope: snapshot
currency: current
as_of: 2026-10-02
as_of_commit:
  - Molly@587d3644
---

# Molly Master Migration Constraints for FFRefine

## Question

What must change in FFRefine, and in how it uses Molly.jl, to run on Molly's `master` branch instead of Molly's `AWHGrads` branch, and why?

## Short answer

FFRefine (commit `6b20031`) currently runs only on Molly's `AWHGrads` branch. A 2026-10-02 diff-and-probe investigation compared `AWHGrads` head `e122c88b` against `master` head `587d3644` and found six areas that block a direct port: a differently shaped parameter-gradient API with no charge support (A), a replay-archive logger that exists only on `AWHGrads` (B), missing unit/precision conversion helpers plus a changed default accumulation float type (C), small PME energy drift on fixed coordinates (D), materially different alchemical-state semantics that change intermediate-$\lambda$ energies and discontinuity behaviour (E), and a PME charge-gradient mismatch between Enzyme and finite differences, originally thought branch-independent and resolved on master 2026-10-15 (F). None of these invalidate FFRefine's scientific approach, but items B and E mean that TSS replay archives, free-energy seeds, and alchemical-state semantics built under `AWHGrads` are not portable to `master` without re-establishing parity. This is all FFRefine project evidence from diffs and probes run against FFRefine's own force-field files; no literature source is involved. The full write-up is `molly_master_migration.md` in the FFRefine repository root.

## Detailed answer

### A. Master's parameter-gradient API (`src/parameters.jl`)

Master's API has a different shape from `AWHGrads`: `extract_parameters(sys, ff)` returns a `Dict{String,T}` with atom mass/σ/ϵ keyed by atom type plus each interaction's declared `parameter_prefix`/`parameter_fields` entries, but **no atomic charges**. `ParameterPlan(sys, dict)` is built once outside the loss, and `inject_gradients(sys, dict, plan, coords)` returns a new `System`. All three throw `DimensionError` on `units=true` systems, so this path is unitless-only (verified).

What worked in probes: a custom ordered, vector-backed `AbstractDict` is compatible with `ParameterPlan`/`inject_gradients` and with Enzyme reverse mode. Charges injected afterward by rebuilding `Atom`s gave Enzyme gradients matching central finite differences to about $10^{-8}$, checked for charges, σ, ϵ, DEXP α, and bond $k$, on water with reaction field.

Pitfalls found: a `ParameterPlan` caches host copies of its own system's atoms, including λ and alchemical role, so (from code reading, not yet tested end-to-end) one plan is needed per thermodynamic state. Rebuilding the System using the *injected* system as template raised `EnzymeNoTypeError` with PME; taking non-parameter fields from the reference system instead works. Master's fast Enzyme rule for dictionary lookup applies only to `Base.Dict`.

Parameter names changed: master shares prefixes across a family (all Coulomb variants use `inter_CO_`; DEXP and DEXP soft-core both use `inter_DEXP_`), and `extract_parameters` keeps only the first value seen per shared prefix. Renames relative to `AWHGrads`: `inter_DEXPSC_*` → `inter_DEXP_*`, and `inter_CRF_*`/`inter_CE_*` → `inter_CO_*`.

**Decision, corrected 2026-10-11:** this page originally recommended keeping charge parameters entirely on the FFRefine side because FFRefine supposedly needed molecular-template, not atom-type, charge keys. That premise was wrong: FFRefine production has keyed charges by atom type since commit `d48d2f1` (2026-07-16, "Group charges by atom type"), before this page was written; the molecular-template charge-key code was already dead by 2026-10-02. See the corrected fourth implementation lesson in [[wiki/concepts/awh-replay-force-field-optimization]].

With that correction, FFRefine's atom-type charge keys match how Molly's upstream `extract_parameters`/`ParameterPlan` design already keys σ and ϵ by atom type. The 2026-10-11 package-planning session therefore decided (K) to propose per-atom-type charge parameters (`atom_<type>_charge`) as a separate Molly pull request (work item U7, investigation first, not blocking the Phase 1 migration): once merged, it replaces FFRefine's local charge-injection layer, with `ChargeModel`/QEq logic mapping onto Molly's own charge parameters rather than FFRefine rebuilding `Atom`s after injection. Until U7 merges, FFRefine keeps local charge injection (an ordered container plus post-injection charge rebuilding), as originally found in this investigation. See [[wiki/answers/ffrefine-generalist-package-plan-decisions]].

**Container design decided, 2026-10-15 (recorded as FFR-049 in [[wiki/answers/ffrefine-decision-register]]).** Benchmarking master's `extract_parameters`/`ParameterPlan` path on FFRefine's garnet ethanol system (6282 atoms, DEXP+RF, 223 parameter keys, one thread) found that master reads the parameter dictionary once per distinct key (`parameter_flat`) and then works on a flat vector, so the container type itself is performance-irrelevant: a full Enzyme energy-gradient pass took 178 ms whether the container was a `Base.Dict`, a vector-backed `AbstractDict`, or a plain values vector rewrapped in a container inside the loss, and gradients were identical across all three; a custom `Molly.dict_get` method saved about 0.1 ms. Under 8 threads sharing one container (the reaction-field system), every form gave results bit-identical to serial, with about 6.5x speed-up. Type inference is concrete for parameter injection in both `Dict` and the custom container; the whole loss function infers `Any` regardless, which traces to Molly master's own `potential_energy`, not to the container choice. FFRefine's container is therefore: an immutable key schema (sorted parameter names plus a name-to-index `Dict`, shared by copy and by zero) paired with a mutable values vector; Enzyme differentiates the values vector, and per-atom parameter indices are computed from atom types rather than stored. Thread-safety rule: the schema is immutable with no lazy caches; the values vector is written only on copies or between parallel phases, never concurrently; each concurrent gradient gets its own private shadow (see section H below). This design replaces the `AWHGrads`-era `ParameterSet`, which existed only to avoid per-atom dictionary lookups in differentiated code — a problem master's `ParameterPlan` already solves.

**Implemented and verified, 2026-10-15 (FFRefine refactor step 13a; working tree, not yet committed; FFR-049 now `implemented` in [[wiki/answers/ffrefine-decision-register]]).** The design above was built as `FFParameterSet{T} <: AbstractDict{String,T}` (fields `schema::ParameterSchema`, `values::Vector{T}`) plus `atom_parameter_indices(p, sys)` (`charge`/`σ`/`ϵ`, zero when a type lacks the parameter), in `src/molly_compat.jl`, and checked with Molly's bundled ethanol/water fixtures in `test/parameter_container_checks.jl` (156/156 assertions pass). Points settled by the implementation, not just the design:

- **Construction is a union over all thermodynamic states' systems, by parameter name**, keeping the first system's value for a name seen more than once (Molly's own first-seen rule for a shared prefix). A key a given state's system does not use gets zero gradient at that state, rather than being absent.
- **Masses are excluded from the container.** Molly's `extract_parameters` includes one mass per atom type, but injecting a trained mass back would undo any hydrogen-mass repartitioning FFRefine applied when building the system; the container union therefore drops every `*_mass` key.
- **Key order is sorted by parameter name**, not by `Dict` hash order or by any one thermodynamic state's own `ParameterPlan` order; every lookup (schema, atom-index map, test fixtures) matches by name, never by position, so the sort order is an implementation detail, not part of the contract.
- **No custom `Molly.dict_get` method was needed.** The ≈0.1 ms saving measured in the benchmark above did not justify adding one; `FFParameterSet`'s `AbstractDict` interface (`getindex`/`setindex!` by name or integer, `haskey`, `get`, `copy`, `zero`) is enough for `ParameterPlan`/`inject_gradients`.
- **Gradient correctness, both Enzyme calling conventions.** Differentiating with `Duplicated(θ, dθ)` (a plain values vector; the loss rewraps `FFParameterSet(p, θ)` before injection) and with `Duplicated(p, zero(p))` (the container itself duplicated) both gave gradients matching the `Base.Dict` path to relative tolerance $10^{-12}$.
- **Thread safety, exercised not just argued.** Eight concurrent Enzyme gradient calls (`Threads.@spawn`, perturbed coordinate sets) against one shared container, system, and `ParameterPlan` gave results `==` the serial results for both calling conventions, all eight runs mutually distinct, and left the shared values vector unchanged — consistent with the thread-safety rule stated above (immutable schema, values vector untouched during concurrent reads).
- **Type stability holds**: `Base.return_types` is concrete for `FFParameterSet(p, θ)` and for `inject_gradients(sys, p, plan, coords)`.

This exercises the container in isolation; it is not yet wired into FFRefine's production gradient path (`injected_system`/`injected_system_template` in `src/gradients.jl` still raise `error("pending step 14")`), so the one-plan-per-thermodynamic-state question noted above remains unexercised end to end.

### B. TSS replay archive

`TSSReplayLogger`, `TSSReplayFrame`, `tss_replay_archive`, and the `TSSSimulation` `replay_logger` keyword exist only on `AWHGrads`. Capturing a frame needs the active window, active state, and estimator from inside Molly's private TSS cycle loop; master's public loggers see only the physical system, so the archive cannot be rebuilt robustly downstream of Molly. Recommendation: port it upstream (roughly 230 lines; its dependencies are unchanged on master), or add a generic per-step TSS hook that an external logger can use. The rest of the TSS/MBAR machinery FFRefine relies on is unchanged, with one exception: master's MBAR implementation rejects $+\infty$ reduced potentials, where `AWHGrads` treated them as zero support.

### C. Conversion helpers and precision

Absent on master: whole-system unit stripping (`ustrip(::System)`), device transfer (`from_device(::System)`), float conversion (`_float_precision_convert`), and `nonbonded_energy_type`. Master introduces `float_type_high` as the energy-accumulation type, defaulting to Float64 even on CUDA, and the System float type must now be passed explicitly (on CPU it still defaults to Float64 regardless of the force field's own type).

### D. Energy parity on fixed coordinates

Reaction-field energies for water, hexane, and ethanol are bit-identical across branches. PME energies are identical for water but differ by 0.019 and 0.107 kJ/mol for hexane and ethanol respectively (about $2\times10^{-6}$ relative). `AlchemicalPartition` energies agree with direct per-state evaluation to $\le 7\times10^{-9}$ kJ/mol on both branches.

**Clarified, 2026-10-15.** The numbers above compare direct Float64 builds on each branch. Probing the systems the way FFRefine's own drivers actually build them (Float32 unitful, then converted to Float64 unitless with `grad_safe=true`) against the Phase 0 baseline reference numbers (`test/baselines/`) gives a different, closer comparison: reaction-field energies agree to $10^{-14}$ relative for water, hexane, and ethanol, and PME energies differ by $-7.3\times10^{-7}$ (water), $-2.3\times10^{-6}$ (hexane), and $-1.2\times10^{-6}$ (ethanol) relative. Water PME built directly at Float64 on master (bypassing the Float32-then-converted path) reproduces this section's own earlier migration-probe value exactly ($-37212.5210$ kJ/mol), so the PME engine itself agrees closely between branches; the small remaining baseline difference traces to converting a Float32-built PME to Float64/unitless rather than to the PME engine, since master's converter rebuilds PME through its own constructor while `AWHGrads`' converter differed, and which internal PME quantity differs between the two converters was not identified. The $1.1\times10^{-4}$ relative ethanol PME offset implied above is therefore a probe-settings artifact of comparing against this section's own 2026-10-02 migration-probe number, not against the Phase 0 baselines; the baselines themselves agree to $1.2\times10^{-6}$.

### E. Alchemical semantics

Probed on ethanol-in-water plus a vacuum leg, with FFRefine-style states (soft-core DEXP; scaled reaction-field or plain Coulomb; solute atoms given the Insert role; `DefaultLambdaScheduler`; λ from 1 to 0; electrostatics off for λ ≤ 0.5; sterics staged over λ < 0.5):

1. **Roles were renumbered.** `AWHGrads`: Core = 0, Insert = 1, Delete = 2. Master: Env = 0, Core = 1, CoreI = 2, CoreD = 3, Insert = 4, Delete = 5. Serialized alchemical states are not portable between branches.
2. **Intra-solute sterics.** Master's `DefaultLambdaScheduler` defaults to `intraLJ=false`, scaling solute-solute steric pairs (annihilation); `AWHGrads` kept them on (decoupling). `intraLJ=true` reproduces `AWHGrads` exactly at λ > 0.
3. **Reaction-field / plain Coulomb electrostatics differ in how pairs scale with λ.** `AWHGrads` scaled each solute charge, so a solute-solute pair scales as $\lambda_e^2$, where $\lambda_e$ is the electrostatic coupling; master scales the pair energy by the pair λ, so the pair scales as $\lambda_e$. Endpoints are identical but intermediate states differ: at λ = 0.75, solvated energy is −62427.81 kJ/mol (`AWHGrads`) versus −62441.01 kJ/mol (master); vacuum is 11.909 versus 8.083 kJ/mol. The PME path is unaffected because the mesh scales charges on both branches. Both branches annihilate intramolecular solute electrostatics, which connects to the overlay-correction caveat in [[wiki/claims/CLM-0023-decoupling-implementations-must-preserve-intramolecular-solute-terms]] and [[wiki/questions/md-free-energy-decoupling-implementation-validation]].
4. **λ = 0 discontinuity on `AWHGrads`.** `AWHGrads`' `LJZeroShortcut` skips every pair involving an atom with λ = 0, so intra-solute DEXP interactions vanish exactly at λ = 0 but are present for every λ > 0 (for ethanol, about 0.05 kJ/mol: vacuum 15.786 at λ = 0 versus 15.736 at λ = 0.25 and 0.5). Master with `intraLJ=true` is continuous.
5. **Consequence.** TSS biases, initial free-energy seeds, and replay archives are tied to the exact alchemical Hamiltonian definition and are not portable across this backend change; ΔG between the physical endpoints is unchanged in principle, but replay parity must be re-established after any switch.

**Decisions made 2026-10-11, recorded here for this specific finding:**
- **(F) Accept master's pair-scaling electrostatic λ path** (point 3 above) rather than reproducing `AWHGrads`' per-charge scaling.
- **(E) Keep FFRefine's own alchemical-ladder builder** (the λ schedule, soft-core α = 0.85, and vacuum-leg construction) rather than switching to Molly's native alchemical types, until Molly's own alchemical setup can reproduce it (work item U6, below).

**Molly `master`'s native alchemical types, found during the 2026-10-11 package-planning session.** Master has `AbsoluteFESystem`, `RelativeFESystem`, and `set_lambda!`, giving native alchemical free-energy support that did not exist in this form on `AWHGrads`. Its convention is: λ = 0 is the coupled (physical) end and λ = 1 is the decoupled (ghost) end (the reverse of FFRefine's own ladder, which runs λ from 1 at the coupled end to 0); atoms being alchemically removed get the `DeleteRole`; and dual topology (`dual=true`) is required. **`AbsoluteFESystem` cannot currently convert FFRefine's double-exponential (DEXP) soft-core potential**, because building the λ-dependent interaction calls `to_lambda_function` on every pairwise interaction, and no `to_lambda_function` method exists for `DoubleExponential`, even though the receiving alchemical type `DoubleExponentialSoftCore` already exists. This is why FFRefine's own λ-ladder builder is being kept (decision E) rather than replaced immediately; work item **U6** (Phase 3) is to add the missing `to_lambda_function` conversion plus whatever else is needed so `AbsoluteFESystem` can reproduce FFRefine's own ladder, after which FFRefine's builder can be retired. See [[wiki/answers/ffrefine-generalist-package-plan-decisions]] and [[wiki/concepts/molly-jl-simulation-package-facts]] for the general Molly facts.

### F. PME charge-gradient mismatch (originally thought branch-independent; resolved on master 2026-10-15)

Using water with the garnet force field (2661 atoms), PME with `grad_safe=true`, CPU Float64, single thread, the derivative of potential energy with respect to the shared O charge ($q=-0.9052$) gave Enzyme $9.415971\times10^{4}$ versus central finite difference $9.380141\times10^{4}$ ($h=10^{-6}$), a relative error of $3.8\times10^{-3}$. Split by component: real-space pair part relative error $6.4\times10^{-9}$; Ewald exclusion-correction part $8.4\times10^{-10}$; PME reciprocal + self part Enzyme $3.308299\times10^{5}$ versus finite difference $3.304716\times10^{5}$, relative error $1.1\times10^{-3}$. Finite differences are trusted here because the energy is quadratic in the charges (no truncation error) with rounding at about $10^{-9}$ relative; σ and DEXP α gradients through the same PME system match finite differences at $10^{-10}$ and $10^{-9}$. This exists identically on both branches and matters only when charges (e.g. QEq) are trained with PME; FFRefine's water and hexane runs default to reaction field. See [[wiki/questions/QST-0014-pme-charge-gradient-enzyme-vs-finite-difference-mismatch]] for the open-question write-up.

**Resolved on master, 2026-10-15, with a probable cause; the "identically on both branches" premise above does not hold.** Probing Molly master (`623d314a`) plus the unmerged system-conversion PR branch (U2, head `0e4b8819`), master's PME has mutable `charge_grid`/`recip_grid` fields that `spread_charge!` and `grad_safe_fft!`/`grad_safe_bfft!` write in place on every call, and MollyEnzymeExt's custom Enzyme rules for these FFTs write into `charge_grid.dval`/`recip_grid.dval`. Enzyme therefore needs the PME interaction passed as `Duplicated(general_inters, Enzyme.make_zero(general_inters))`, as Molly's own tests do; passing it `Const`, which was FFRefine's pattern (PME sitting inside a `Const` general-interactions context), throws `FieldError: type Const has no field dval` rather than silently disagreeing. With PME `Duplicated`, on the same water PME system: $\partial U/\partial q(\mathrm O)$ Enzyme vs central finite difference relative error $1.0\times10^{-10}$ (finite-difference value $9.380141\times10^4$, matching the value above); $q(\mathrm H)$ relative error $1.1\times10^{-9}$; the PME part alone (total minus the energy evaluated without `general_inters`) $\le 6\times10^{-11}$; σ, ϵ, DEXP α/β, and `coulomb_const` all $\le 1.1\times10^{-8}$. FFRefine's `AWHGrads`-era Enzyme values for the same O/H charges differ from this master `Duplicated` result by $3.8\times10^{-3}$ and $5.7\times10^{-3}$ respectively — matching the mismatch recorded above, which means the `AWHGrads`-era Enzyme value was the wrong one, not master's. Hypothesis, **not verified on `AWHGrads`**: its PME path loses part of the charge gradient through its own mutable grids being differentiated without an Enzyme shadow, analogous to what `Const` does on master. Not yet checked: GPU, and PME charge gradients for hexane and ethanol (only water was probed). See the updated status in [[wiki/questions/QST-0014-pme-charge-gradient-enzyme-vs-finite-difference-mismatch]].

### G. Loggers under generalized-ensemble sampling (found 2026-10-11)

Molly `master`'s loggers belong to the generalized-ensemble simulation object, not to an individual `ThermoState`'s own `System`. In TSS, AWH, and replica-exchange (REMD) runs alike, a logger runs per replica and follows that replica as it moves across physical states; a logger attached to one `ThermoState`'s `System` is therefore silently never invoked during these runs. This is why FFRefine's planned target-logger declarations attach to the FFRefine ensemble object (planned as `TSSEnsemble(...; loggers)`), mirroring how `TSSSimulation(...; loggers)` already takes them on master, rather than to individual thermodynamic-state systems. See decision L and section C ("Fit targets, Molly loggers, and gradients of averages") in [[wiki/answers/ffrefine-generalist-package-plan-decisions]], and the general Molly facts in [[wiki/concepts/molly-jl-simulation-package-facts]].

### H. PME-Enzyme shadow requirement and thread safety (found 2026-10-15)

- **PME must be `Duplicated`, not `Const`.** See the 2026-10-15 addition to section F above: master's PME has mutable `charge_grid`/`recip_grid` fields with custom Enzyme FFT rules that write into their `.dval` shadows, so Enzyme needs `Duplicated(general_inters, Enzyme.make_zero(general_inters))`; `Const` throws `FieldError: type Const has no field dval`.
- **Concurrent Enzyme gradients cannot share one PME object.** Sixteen concurrent Enzyme gradient calls across 8 threads against one shared PME object gave results wrong by up to $1\times10^{66}$ relative; giving each task a deep copy of the PME made the results bit-identical to serial. Likely mechanism: Molly's PME `deepcopy` re-plans its FFTW plans, and FFTW planning is not thread-safe, so per-task PME copies should be made before spawning tasks rather than inside them (copying before versus inside the spawn was not itself tested). The PME Enzyme shadow costs about 0.03 ms to create (water, $25^3$ mesh) and, once created, can be reused across repeated gradient calls with identical results; `Enzyme.make_zero!` errors on a PME shadow, but `Enzyme.remake_zero!` works. Water's Enzyme gradient through PME costs about 85 ms versus about 77 ms without PME, single thread.
- **Smaller finding.** Master names `CoulombEwald` parameters `inter_CO_*` like every Coulomb-family interaction (`AWHGrads` used a separate `inter_CE_*` prefix for Ewald). Enzyme gives a gradient of exactly 0 for `inter_CO_dist_cutoff` on water PME, where central finite differences give about $-3157$ kJ/mol/nm: cutoffs are not meaningful trainable parameters through Enzyme.

This is relevant to the per-epoch subprocess rationale recorded in [[wiki/answers/ffrefine-generalist-package-plan-decisions]] (decision P), which cites a suspected PME/multithreading/Enzyme interaction behind inter-epoch memory leaks and segmentation faults without describing the investigation. The mechanism probed here (FFTW re-planning during a shared, un-copied PME shadow under concurrent Enzyme gradients) is a directly confirmed PME/Enzyme/threading hazard, but it has not been shown to be the same mechanism behind the earlier leaks and segfaults.

### I. Pinning Molly `master` in `Project.toml`: `Pkg.resolve()` cannot raise a fixed Manifest version (found 2026-10-15, FFRefine step 13a)

Moving the `[sources]` git pin from a fixed commit to a newer one can raise what that commit requires of its own dependencies. Here, Molly `master` `ac3ede15` requires KernelAbstractions $\ge 0.9.43$, while FFRefine's existing Manifest had KernelAbstractions pinned at 0.9.42 from the previous Molly pin. `Pkg.resolve()` treats every package version already in the Manifest as fixed and only resolves packages not yet present, so it fails with an unsatisfiable-requirements error in this situation; it cannot raise an existing pin. `Pkg.update()` would resolve it, but updates every package freely, which is more disruptive than needed and not how this project pins dependencies (see `refactor/prompts/CONVENTIONS.md`'s pin procedure in the FFRefine repository).

**Fix that stays consistent with the stacked environment:** CUDA is not a package dependency of FFRefine; the examples find and load it only because `--project=.` stacks the default environment (`~/.julia/environments/v1.12`) underneath. Re-seeding the project Manifest from that default environment's Manifest, then running `Pkg.resolve()` (never `Pkg.update()`), raises every shared package to the versions already resolved there — satisfying Molly's tighter KernelAbstractions bound as a side effect, because the default environment had already moved past 0.9.42 — while keeping every package FFRefine shares with the stacked environment (CUDA, GPUArrays, Enzyme, etc.) at one consistent version pair. This is the procedure an earlier FFRefine step ("step 08") had already established for the same reason. Verified after reseeding: CUDA 6.2.2, GPUArrays 11.5.16, and Enzyme 0.13.216 load together with the pinned Molly, and `CuArray` construction works. 23 packages moved versions this way (not failures, just the default environment's already-current versions); the only new dependency was Molly master's own addition, PhiloxRNG.

This is a general `Pkg.jl` mechanism, not specific to Molly: any git-pinned `[sources]` dependency whose newer commit tightens a compat bound beyond what the Manifest already fixed will hit the same `Pkg.resolve()` failure, and reseeding from the environment the project is stacked on (when the project depends on that stacking, as FFRefine does for CUDA) is the way to raise versions without drifting from it.

## Recommended strategy

- Port the TSS replay archive logger upstream to master (or add a generic per-step TSS hook), since it cannot be reconstructed robustly from master's public loggers (B). **Decided 2026-10-11:** a generic per-sample TSS hook (work item U1), not a direct port of the `AWHGrads`-only replay-archive logger; FFRefine owns the archive format built from that hook. See [[wiki/answers/ffrefine-generalist-package-plan-decisions]].
- Keep an FFRefine-side parameter container, charge layer, and system converter rather than adopting master's atom-type-keyed `extract_parameters`/`ParameterPlan` design as-is: a local ordered dict for charges, post-injection charge rebuilding, and project-local replacements for the removed `ustrip(::System)`/`from_device(::System)`/`_float_precision_convert` helpers, with the System float type passed explicitly (A, C). **Corrected 2026-10-11:** the charge layer should stay local only until Molly's own per-atom-type charge parameters (U7) merge, not indefinitely; see the corrected charge-key discussion in section A above. **Finalized 2026-10-15:** the container's concrete design (immutable key schema plus values vector) is decided; see the end of section A and FFR-049 in [[wiki/answers/ffrefine-decision-register]]. **Implemented and verified 2026-10-15 (step 13a):** built and unit-tested as `FFParameterSet`/`ParameterSchema`/`atom_parameter_indices`, not yet wired into production gradient injection; see the "Implemented and verified" paragraph in section A.
- Make an explicit alchemical decision rather than inheriting master's defaults silently: set `intraLJ=true` to preserve `AWHGrads`' decoupling semantics, and explicitly accept or replace the reaction-field/plain-Coulomb λ-scaling change (pair-λ instead of per-charge-λ) (E). **Decided 2026-10-11 (F):** accept master's pair-scaling path.
- Do not reuse `AWHGrads`-era TSS replay archives, free-energy seeds, or serialized alchemical states on master; the role numbering and intermediate-λ Hamiltonian differ even though endpoints agree (E).

## Validation checklist

- Energy parity on fixed coordinates, reaction field and PME, across the systems FFRefine uses (water, hexane, ethanol), and over the full λ grid for alchemical legs, not just the values sampled in this investigation (D, E).
- Finite-difference gradient checks per parameter family (charges, σ, ϵ, DEXP α/β, bond $k$) after porting the parameter layer, mirroring the probes in A.
- The QEq Jacobian check (per [[wiki/concepts/awh-replay-force-field-optimization]]'s existing compressed-site lesson) re-run against the master-based parameter layer.
- Replay parity, endpoint free-energy parity, and effective-sample-size diagnostics from fresh TSS runs on master, not reused `AWHGrads` archives.
- A short GPU TSS run, since conversion helpers, device transfer, and the `float_type_high` default changed (C).
- PME charge-gradient Enzyme-vs-finite-difference parity on GPU and on hexane/ethanol, since the 2026-10-15 resolution of F (section F, section H) only checked CPU Float64 water PME.

## Key equations

Reaction-field/plain-Coulomb pair scaling for a solute-solute pair with charges $e_i,e_j$ at lambda $\lambda$:

$$
U_{\mathrm{AWHGrads}} \propto (\lambda e_i)(\lambda e_j) = \lambda^2\, e_i e_j,
\qquad
U_{\mathrm{master}} \propto \lambda\, e_i e_j .
$$

Both reduce to $e_ie_j$ at $\lambda=1$ and to $0$ at $\lambda=0$; they differ at intermediate $\lambda$.

## Sources used

None (no literature source). All content is FFRefine project evidence from the 2026-10-02 diff-and-probe investigation listed in this page's frontmatter.

## Wiki pages used

- [[wiki/answers/ffrefine-current-implementation-status]]
- [[wiki/concepts/awh-replay-force-field-optimization]]
- [[wiki/answers/ffrefine-generalist-package-plan-decisions]]
- [[wiki/concepts/molly-jl-simulation-package-facts]]

## Wiki updates made

- Added this answer note.
- Added [[wiki/questions/QST-0014-pme-charge-gradient-enzyme-vs-finite-difference-mismatch]] for the F finding.
- Added section E as project evidence to [[wiki/questions/md-free-energy-decoupling-implementation-validation]], linked to [[wiki/claims/CLM-0023-decoupling-implementations-must-preserve-intramolecular-solute-terms]].
- Added a short pointer to this note in [[wiki/answers/ffrefine-current-implementation-status]].
- **2026-10-11 update:** corrected section A's charge-key decision (production has used atom-type charge keys since 2026-07-16, not molecular-template keys); added decisions F and E and work item U7 where they apply; added `AbsoluteFESystem`/`RelativeFESystem`/`set_lambda!`, the missing DEXP `to_lambda_function` conversion, and the λ=0-coupled/λ=1-decoupled/`DeleteRole`/`dual=true` convention to section E; added section G on loggers being ignored on `ThermoState` systems under generalized-ensemble sampling. Added links to the new [[wiki/answers/ffrefine-generalist-package-plan-decisions]] and [[wiki/concepts/molly-jl-simulation-package-facts]] pages.
- **2026-10-15 update:** added the resolution of the F mismatch on Molly master (PME must be passed `Duplicated`, not `Const`) and updated [[wiki/questions/QST-0014-pme-charge-gradient-enzyme-vs-finite-difference-mismatch]] accordingly; clarified section D's PME energy parity against the Phase 0 baselines and the ethanol offset artifact; finalized the parameter-container design at the end of section A and recorded it as FFR-049 in [[wiki/answers/ffrefine-decision-register]]; added section H on PME/Enzyme thread safety (shared-PME hazard, FFTW re-planning, shadow reuse) and the `inter_CO_dist_cutoff`/`inter_CE_*` naming note.
- **2026-10-15 update (FFRefine refactor step 13a write-back):** added the "Implemented and verified" paragraph to section A, recording that the parameter container was built (`FFParameterSet`/`ParameterSchema`/`atom_parameter_indices`) and unit-tested, and updated FFR-049 to `implemented` in [[wiki/answers/ffrefine-decision-register]] (also updated FFR-021 and the register's short-answer phase summary, since Phase 1 migration now has code); added section I on the `Pkg.resolve()`-cannot-raise-a-fixed-version Manifest mechanism found while pinning Molly to `master`, and its fix (reseed the Manifest from the stacked default environment, never `Pkg.update()`).

## Remaining gaps

- The 2026-10-02 and 2026-10-15 probe scripts were not kept, so these numbers cannot be independently re-run from this write-back; they should be treated as one-time measurements, not a regression-tested result.
- The F mismatch is resolved for CPU, Float64, water PME on master (section F, 2026-10-15): passing PME as `Const` instead of `Duplicated` was the cause. The analogous hypothesis for `AWHGrads` (an un-shadowed mutable grid) was not independently verified there, and GPU and hexane/ethanol PME charge gradients remain unchecked on either branch.
- The PME/Enzyme thread-safety finding (section H) shows one way concurrent Enzyme gradients can silently corrupt results when they share a PME object; it was not established whether this, specifically, is the cause of the inter-epoch memory leaks and segmentation faults behind the per-epoch subprocess design (decision P in [[wiki/answers/ffrefine-generalist-package-plan-decisions]]), nor whether copying the PME object before versus inside a spawned task matters.
- `ParameterPlan`'s one-plan-per-thermodynamic-state requirement (A) was inferred from code reading, not exercised end-to-end in a probe.
- No full FFRefine experiment (water temperature ladder, hexane, ethanol solvation) has actually been run on master; this write-back is a static/probe-level compatibility analysis, not a completed migration.
