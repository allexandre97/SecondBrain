---
type: answer
status: active
created: 2026-10-02
updated: 2026-10-02
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
project_evidence:
  - "FFRefine project investigation, 2026-10-02: static diffs between Molly AWHGrads head `e122c88b` (2026-07-31) and Molly master head `587d3644` (2026-10-02); merge base `491668ae` (AWHGrads has 50 commits not on master, master has 184 not on AWHGrads); compared against FFRefine commit `6b20031`, which currently runs only on AWHGrads"
  - "FFRefine project probes, 2026-10-02: small Julia probe scripts (not kept; scripts were temporary) built with FFRefine's own garnet force-field XMLs and PDBs, run on CPU in Float64 against both Molly checkouts"
  - "Full project-local write-up: `molly_master_migration.md` in the FFRefine repository root"
---

# Molly Master Migration Constraints for FFRefine

## Question

What must change in FFRefine, and in how it uses Molly.jl, to run on Molly's `master` branch instead of Molly's `AWHGrads` branch, and why?

## Short answer

FFRefine (commit `6b20031`) currently runs only on Molly's `AWHGrads` branch. A 2026-10-02 diff-and-probe investigation compared `AWHGrads` head `e122c88b` against `master` head `587d3644` and found six areas that block a direct port: a differently shaped parameter-gradient API with no charge support (A), a replay-archive logger that exists only on `AWHGrads` (B), missing unit/precision conversion helpers plus a changed default accumulation float type (C), small PME energy drift on fixed coordinates (D), materially different alchemical-state semantics that change intermediate-$\lambda$ energies and discontinuity behaviour (E), and a pre-existing, branch-independent PME charge-gradient mismatch between Enzyme and finite differences (F). None of these invalidate FFRefine's scientific approach, but items B and E mean that TSS replay archives, free-energy seeds, and alchemical-state semantics built under `AWHGrads` are not portable to `master` without re-establishing parity. This is all FFRefine project evidence from diffs and probes run against FFRefine's own force-field files; no literature source is involved. The full write-up is `molly_master_migration.md` in the FFRefine repository root.

## Detailed answer

### A. Master's parameter-gradient API (`src/parameters.jl`)

Master's API has a different shape from `AWHGrads`: `extract_parameters(sys, ff)` returns a `Dict{String,T}` with atom mass/σ/ϵ keyed by atom type plus each interaction's declared `parameter_prefix`/`parameter_fields` entries, but **no atomic charges**. `ParameterPlan(sys, dict)` is built once outside the loss, and `inject_gradients(sys, dict, plan, coords)` returns a new `System`. All three throw `DimensionError` on `units=true` systems, so this path is unitless-only (verified).

What worked in probes: a custom ordered, vector-backed `AbstractDict` is compatible with `ParameterPlan`/`inject_gradients` and with Enzyme reverse mode. Charges injected afterward by rebuilding `Atom`s gave Enzyme gradients matching central finite differences to about $10^{-8}$, checked for charges, σ, ϵ, DEXP α, and bond $k$, on water with reaction field.

Pitfalls found: a `ParameterPlan` caches host copies of its own system's atoms, including λ and alchemical role, so (from code reading, not yet tested end-to-end) one plan is needed per thermodynamic state. Rebuilding the System using the *injected* system as template raised `EnzymeNoTypeError` with PME; taking non-parameter fields from the reference system instead works. Master's fast Enzyme rule for dictionary lookup applies only to `Base.Dict`.

Parameter names changed: master shares prefixes across a family (all Coulomb variants use `inter_CO_`; DEXP and DEXP soft-core both use `inter_DEXP_`), and `extract_parameters` keeps only the first value seen per shared prefix. Renames relative to `AWHGrads`: `inter_DEXPSC_*` → `inter_DEXP_*`, and `inter_CRF_*`/`inter_CE_*` → `inter_CO_*`.

**Decision:** keep charge parameters on the FFRefine side (a local ordered container plus post-injection charge rebuilding) rather than adopting the upstream atom-type-keyed design. FFRefine needs molecular-template, not atom-type, charge keys (an existing implementation lesson in [[wiki/concepts/awh-replay-force-field-optimization]]), which the upstream design does not cover.

### B. TSS replay archive

`TSSReplayLogger`, `TSSReplayFrame`, `tss_replay_archive`, and the `TSSSimulation` `replay_logger` keyword exist only on `AWHGrads`. Capturing a frame needs the active window, active state, and estimator from inside Molly's private TSS cycle loop; master's public loggers see only the physical system, so the archive cannot be rebuilt robustly downstream of Molly. Recommendation: port it upstream (roughly 230 lines; its dependencies are unchanged on master), or add a generic per-step TSS hook that an external logger can use. The rest of the TSS/MBAR machinery FFRefine relies on is unchanged, with one exception: master's MBAR implementation rejects $+\infty$ reduced potentials, where `AWHGrads` treated them as zero support.

### C. Conversion helpers and precision

Absent on master: whole-system unit stripping (`ustrip(::System)`), device transfer (`from_device(::System)`), float conversion (`_float_precision_convert`), and `nonbonded_energy_type`. Master introduces `float_type_high` as the energy-accumulation type, defaulting to Float64 even on CUDA, and the System float type must now be passed explicitly (on CPU it still defaults to Float64 regardless of the force field's own type).

### D. Energy parity on fixed coordinates

Reaction-field energies for water, hexane, and ethanol are bit-identical across branches. PME energies are identical for water but differ by 0.019 and 0.107 kJ/mol for hexane and ethanol respectively (about $2\times10^{-6}$ relative). `AlchemicalPartition` energies agree with direct per-state evaluation to $\le 7\times10^{-9}$ kJ/mol on both branches.

### E. Alchemical semantics

Probed on ethanol-in-water plus a vacuum leg, with FFRefine-style states (soft-core DEXP; scaled reaction-field or plain Coulomb; solute atoms given the Insert role; `DefaultLambdaScheduler`; λ from 1 to 0; electrostatics off for λ ≤ 0.5; sterics staged over λ < 0.5):

1. **Roles were renumbered.** `AWHGrads`: Core = 0, Insert = 1, Delete = 2. Master: Env = 0, Core = 1, CoreI = 2, CoreD = 3, Insert = 4, Delete = 5. Serialized alchemical states are not portable between branches.
2. **Intra-solute sterics.** Master's `DefaultLambdaScheduler` defaults to `intraLJ=false`, scaling solute-solute steric pairs (annihilation); `AWHGrads` kept them on (decoupling). `intraLJ=true` reproduces `AWHGrads` exactly at λ > 0.
3. **Reaction-field / plain Coulomb electrostatics differ in how pairs scale with λ.** `AWHGrads` scaled each solute charge, so a solute-solute pair scales as $\lambda_e^2$, where $\lambda_e$ is the electrostatic coupling; master scales the pair energy by the pair λ, so the pair scales as $\lambda_e$. Endpoints are identical but intermediate states differ: at λ = 0.75, solvated energy is −62427.81 kJ/mol (`AWHGrads`) versus −62441.01 kJ/mol (master); vacuum is 11.909 versus 8.083 kJ/mol. The PME path is unaffected because the mesh scales charges on both branches. Both branches annihilate intramolecular solute electrostatics, which connects to the overlay-correction caveat in [[wiki/claims/CLM-0023-decoupling-implementations-must-preserve-intramolecular-solute-terms]] and [[wiki/questions/md-free-energy-decoupling-implementation-validation]].
4. **λ = 0 discontinuity on `AWHGrads`.** `AWHGrads`' `LJZeroShortcut` skips every pair involving an atom with λ = 0, so intra-solute DEXP interactions vanish exactly at λ = 0 but are present for every λ > 0 (for ethanol, about 0.05 kJ/mol: vacuum 15.786 at λ = 0 versus 15.736 at λ = 0.25 and 0.5). Master with `intraLJ=true` is continuous.
5. **Consequence.** TSS biases, initial free-energy seeds, and replay archives are tied to the exact alchemical Hamiltonian definition and are not portable across this backend change; ΔG between the physical endpoints is unchanged in principle, but replay parity must be re-established after any switch.

### F. PME charge-gradient mismatch (pre-existing, branch-independent)

Using water with the garnet force field (2661 atoms), PME with `grad_safe=true`, CPU Float64, single thread, the derivative of potential energy with respect to the shared O charge ($q=-0.9052$) gave Enzyme $9.415971\times10^{4}$ versus central finite difference $9.380141\times10^{4}$ ($h=10^{-6}$), a relative error of $3.8\times10^{-3}$. Split by component: real-space pair part relative error $6.4\times10^{-9}$; Ewald exclusion-correction part $8.4\times10^{-10}$; PME reciprocal + self part Enzyme $3.308299\times10^{5}$ versus finite difference $3.304716\times10^{5}$, relative error $1.1\times10^{-3}$. Finite differences are trusted here because the energy is quadratic in the charges (no truncation error) with rounding at about $10^{-9}$ relative; σ and DEXP α gradients through the same PME system match finite differences at $10^{-10}$ and $10^{-9}$. This exists identically on both branches and matters only when charges (e.g. QEq) are trained with PME; FFRefine's water and hexane runs default to reaction field. See [[wiki/questions/QST-0014-pme-charge-gradient-enzyme-vs-finite-difference-mismatch]] for the open-question write-up.

## Recommended strategy

- Port the TSS replay archive logger upstream to master (or add a generic per-step TSS hook), since it cannot be reconstructed robustly from master's public loggers (B).
- Keep an FFRefine-side parameter container, charge layer, and system converter rather than adopting master's atom-type-keyed `extract_parameters`/`ParameterPlan` design as-is: a local ordered dict for charges, post-injection charge rebuilding, and project-local replacements for the removed `ustrip(::System)`/`from_device(::System)`/`_float_precision_convert` helpers, with the System float type passed explicitly (A, C).
- Make an explicit alchemical decision rather than inheriting master's defaults silently: set `intraLJ=true` to preserve `AWHGrads`' decoupling semantics, and explicitly accept or replace the reaction-field/plain-Coulomb λ-scaling change (pair-λ instead of per-charge-λ) (E).
- Do not reuse `AWHGrads`-era TSS replay archives, free-energy seeds, or serialized alchemical states on master; the role numbering and intermediate-λ Hamiltonian differ even though endpoints agree (E).

## Validation checklist

- Energy parity on fixed coordinates, reaction field and PME, across the systems FFRefine uses (water, hexane, ethanol), and over the full λ grid for alchemical legs, not just the values sampled in this investigation (D, E).
- Finite-difference gradient checks per parameter family (charges, σ, ϵ, DEXP α/β, bond $k$) after porting the parameter layer, mirroring the probes in A.
- The QEq Jacobian check (per [[wiki/concepts/awh-replay-force-field-optimization]]'s existing compressed-site lesson) re-run against the master-based parameter layer.
- Replay parity, endpoint free-energy parity, and effective-sample-size diagnostics from fresh TSS runs on master, not reused `AWHGrads` archives.
- A short GPU TSS run, since conversion helpers, device transfer, and the `float_type_high` default changed (C).

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

## Wiki updates made

- Added this answer note.
- Added [[wiki/questions/QST-0014-pme-charge-gradient-enzyme-vs-finite-difference-mismatch]] for the F finding.
- Added section E as project evidence to [[wiki/questions/md-free-energy-decoupling-implementation-validation]], linked to [[wiki/claims/CLM-0023-decoupling-implementations-must-preserve-intramolecular-solute-terms]].
- Added a short pointer to this note in [[wiki/answers/ffrefine-current-implementation-status]].

## Remaining gaps

- The probe scripts were not kept, so these numbers cannot be independently re-run from this write-back; they should be treated as a one-time 2026-10-02 measurement, not a regression-tested result.
- The root cause of the F mismatch (PME reciprocal/self Enzyme rule versus the self-energy term's charge derivative) is unresolved.
- `ParameterPlan`'s one-plan-per-thermodynamic-state requirement (A) was inferred from code reading, not exercised end-to-end in a probe.
- No full FFRefine experiment (water temperature ladder, hexane, ethanol solvation) has actually been run on master; this write-back is a static/probe-level compatibility analysis, not a completed migration.
