---
type: answer
status: active
created: 2026-10-16
updated: 2026-10-16
question: "What did FFRefine refactor step 15 (2026-10-16) establish about Enzyme silently dropping gradients depending on Molly interaction-struct layout, and about the electrostatic alchemical λ path when the intra-solute steric scheduler difference is held fixed?"
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
  - validation
related:
  - "[[wiki/questions/QST-0017-enzyme-struct-field-layout-silently-drops-gradient]]"
  - "[[wiki/questions/QST-0016-enzyme-map-struct-rebuild-silently-drops-gradient]]"
  - "[[wiki/questions/QST-0014-pme-charge-gradient-enzyme-vs-finite-difference-mismatch]]"
  - "[[wiki/answers/ffrefine-step14-enzyme-gradient-injection-and-beta-precision-validation]]"
  - "[[wiki/answers/molly-master-migration-constraints-for-ffrefine]]"
  - "[[wiki/concepts/molly-jl-simulation-package-facts]]"
  - "[[wiki/answers/ffrefine-decision-register]]"
  - "[[wiki/claims/CLM-0023-decoupling-implementations-must-preserve-intramolecular-solute-terms]]"
sources: []
sensitivity: public
encryption: none
wiki_pages_used:
  - "[[wiki/questions/QST-0016-enzyme-map-struct-rebuild-silently-drops-gradient]]"
  - "[[wiki/answers/molly-master-migration-constraints-for-ffrefine]]"
  - "[[wiki/concepts/molly-jl-simulation-package-facts]]"
raw_sources_consulted: []
wiki_pages_updated:
  - "[[wiki/questions/QST-0017-enzyme-struct-field-layout-silently-drops-gradient]]"
  - "[[wiki/questions/QST-0016-enzyme-map-struct-rebuild-silently-drops-gradient]]"
  - "[[wiki/answers/molly-master-migration-constraints-for-ffrefine]]"
  - "[[wiki/concepts/molly-jl-simulation-package-facts]]"
  - "[[wiki/answers/ffrefine-decision-register]]"
project_evidence:
  - "FFRefine refactor step 15, 2026-10-16 (Enzyme 0.13.216, Enzyme_jll 0.0.303, Julia 1.12.7, Linux x86_64; Molly master): bisected an Enzyme gradient bug affecting DoubleExponentialSoftCore and later pairwise interactions in the same tuple, built a standalone Enzyme reproducer, and reordered struct fields; the DoubleExponentialSoftCore reorder is merged into Molly master, the LennardJones/Mie/AshbaughHatch reorder is on an unmerged branch; Molly's parameter-gradient testset passes 181/181 with no broken entries after the fix, and all 2443 Molly CPU tests still pass"
  - "FFRefine refactor step 15, 2026-10-16: CPU Float64 comparison (a Float64 copy of a Float32-built system) of Molly master with DefaultLambdaScheduler(intraLJ=true) against Molly AWHGrads, ethanol hydration (9 solute atoms), reaction-field solvated leg and plain-Coulomb vacuum leg, at lambda = 0, 0.25, 0.5, 0.75, 1"
scope: snapshot
currency: current
as_of: 2026-10-16
as_of_commit:
  - FFRefine@ad6ccd9
---

# FFRefine Step 15: Enzyme Struct-Layout Gradient Loss and the Electrostatic Alchemical λ Path

## Short answer

FFRefine refactor step 15 (2026-10-16) produced two durable findings. First, Enzyme reverse-mode AD on Molly master can silently return an exactly-zero gradient for a pairwise interaction's `Float64` parameter field, with no error, depending only on that interaction struct's field layout (a `Bool` field followed by a zero-size field and/or padding before the parameter) combined with a never-executed, type-unstable branch elsewhere in the differentiated call graph; this affected `DoubleExponentialSoftCore`'s `weight_14` and every field of any pairwise interaction listed after it, and separately `LennardJones`/`Mie`/`AshbaughHatch`'s `weight_14`. Reordering the affected structs' fields fixes it; the `DoubleExponentialSoftCore` fix is merged into Molly master, the others are on an unmerged branch. The root Enzyme mechanism remains unresolved; see [[wiki/questions/QST-0017-enzyme-struct-field-layout-silently-drops-gradient]]. Second, a controlled comparison that holds the intra-solute steric scheduler fixed (`intraLJ=true` on both Molly branches) isolates and confirms the electrostatic λ-path difference already recorded in [[wiki/answers/molly-master-migration-constraints-for-ffrefine]] (section E, point 3): Molly master and `AWHGrads` agree to machine precision at λ = 1, 0.5, 0.25, diverge by a few kJ/mol at λ = 0.75 from the pair-scaling-versus-per-charge-scaling difference, and agree again at λ = 0 because both branches fully annihilate intra-solute electrostatics there.

## Detailed answer

### A. Enzyme silently zeros a gradient depending on interaction-struct field layout and a dead type-unstable branch

Auditing Molly master's own parameter-gradient test suite found several interactions marked `@test_broken` for specific fields: `DoubleExponentialSoftCore`'s `weight_14`, and `weight_14` for `LennardJones`, `Mie`, and `AshbaughHatch`. Probing these directly against central finite differences confirmed Enzyme (`set_runtime_activity(Reverse)`, Enzyme 0.13.216, Enzyme_jll 0.0.303, Julia 1.12.7) returns exactly `0.0` for these gradients where finite differences are non-zero, with no error or warning raised. The failure was not confined to the one broken field: every field of every pairwise interaction listed *after* a triggering interaction in Molly's `general_inters` tuple was also zeroed (for example `coulomb_const` and `weight_14` of a `CoulombScaled` or plain `Coulomb` following a `DoubleExponentialSoftCore`), while atom parameters (σ, ϵ, charges) and fields of interactions listed *before* the trigger were correct.

Bisection found the loss appears only once the parameter-injected interactions are stored in the mutable `System` and read back inside the differentiated energy function, which routes through Molly's `with_pairwise_partition`. That function branches at runtime on each interaction's `use_neighbors::Bool`, and in the mixed case (not every interaction in the tuple uses the neighbor list) calls the pairwise loop on `filter()`-ed sub-tuples of the small, `isbits`, heterogeneous interaction tuple — a type-unstable operation whose result type depends on runtime values. A single interaction's own derivative, computed directly from the bare struct or passed to the energy function by keyword, was always correct; the loss required going through this stored-and-partitioned code path.

A standalone, Molly-independent minimal reproducer isolates the same failure:

```julia
using Enzyme
struct Z end
struct Bad; flag::Bool; z::Z; w::Float64; end       # Bool, zero-size field, Float64: d/dw lost
struct NoZ; flag::Bool; w::Float64; end             # correct
struct BoolLast; z::Z; w::Float64; flag::Bool; end  # correct
make(::Type{Bad}, w) = Bad(true, Z(), w)
make(::Type{NoZ}, w) = NoZ(true, w)
make(::Type{BoolLast}, w) = BoolLast(Z(), w, true)
mutable struct Box{X, I}; xs::X; inters::I; end
flag(i) = i.flag
function energy(xs, inters)
    e = 0.0
    for x in xs; e += inters[1].w * x; end
    return e
end
# filter branch never taken (flag is true), but its result type depends on runtime values
with_flagged(g, t) = all(flag, t) ? g(t) : g(filter(flag, t))
function f(w, T, xs)
    box = Box(xs, (make(T, w),))
    return with_flagged(t -> energy(box.xs, t), box.inters)
end
xs = [1.0, 2.0, 3.0]
for T in (Bad, NoZ, BoolLast)
    g = autodiff(set_runtime_activity(Reverse), Const(f), Active, Active(0.5), Const(T), Const(xs))[1][1]
    println(T, " d/dw = ", g, "  (expected ", sum(xs), ")")
end
```

This prints `Bad → 0.0`, `NoZ → 6.0`, `BoolLast → 6.0` (all three should print `6.0`). All three ingredients are needed together: the layout (`Bool`, zero-size field, then `Float64`, leaving a padding byte before the parameter), the never-taken but type-unstable `filter` branch, and a closure that reads a field of the mutable struct holding the tuple. Without `set_runtime_activity`, Enzyme instead throws `EnzymeRuntimeActivityError` rather than silently returning a wrong value. A separate, apparently unrelated internal Enzyme failure (`AssertionError: length(remaining) < length(dead)`) appeared when differentiating anonymous closures that close over globals, during the same debugging session; it was not reduced further.

**Fix.** Reordering fields so a `Bool` does not sit before the `Float64` parameters with intervening padding or zero-size fields fixes the symptom: for `DoubleExponentialSoftCore`, moving its scheduler field to immediately follow `use_neighbors` (matching Molly's other λ-interactions' layout); for `LennardJones`/`Mie`/`AshbaughHatch`, moving `use_neighbors::Bool` to be the last field. After the reorder, Molly's own parameter-gradient testset passes 181/181 with no broken entries, and all 2443 Molly CPU tests still pass. The `DoubleExponentialSoftCore` reorder has been merged into Molly master; the `LennardJones`/`Mie`/`AshbaughHatch` reorder exists only on an unmerged branch as of this writing.

**Negative result: fixing the branch, not the layout, is not reliable.** Moving the mixed-partition branch into a `@noinline` function fixes the pure reproducer above but does **not** fix Molly's real `potential_energy`. None of the following fixed Molly either: replacing the mixed branch with an error; restructuring it as a check followed by an ordinary two-way branch instead of `filter`; marking the mixed-case path `EnzymeRules.inactive`; forcing per-interaction static dispatch; or giving the loop a distinct method instance. Semantically identical code differed in outcome — a `do`-block closure failed where an equivalent local named function or inline closure, doing the same thing, did not. **Conclusion:** the `filter` branch reproduces the bug but is not its cause; the failure is sensitive to incidental compilation shape in a way that makes structural workarounds unreliable, so the struct-layout fix plus a finite-difference gate is the available defence, not a code-shape rule that can be stated and checked by inspection. The root cause inside Enzyme is unresolved (see [[wiki/questions/QST-0017-enzyme-struct-field-layout-silently-drops-gradient]]); the operator plans to file an Enzyme.jl issue with the reproducer above but has not done so as of this writing.

**Related, found in the same investigation.** On Molly master, CPU gradients of "mixed" systems (some pairwise interactions use the neighbor list, some do not) fail with `IllegalTypeAnalysisException` instead of returning a silently wrong value; Molly's GPU reverse-mode rules reject mixed systems explicitly. These are distinct, erroring failure modes in the same code region (`with_pairwise_partition`'s mixed-case handling), and may or may not share a root cause with the silent zero above.

**Lesson, consistent with [[wiki/questions/QST-0016-enzyme-map-struct-rebuild-silently-drops-gradient]].** Differentiable-simulation gradient paths need a finite-difference gate per interaction type *and* per combination of interactions present in one system — a single-interaction check would have missed this, since the fault depends on which interactions share a tuple and in what order. Cross-checking two Enzyme-based formulations against each other is not sufficient, because both can share the same silent failure; this is now confirmed by three independently-found Enzyme silent-gradient-loss mechanisms across FFRefine's Molly-master migration (this one; the non-inlined `map`-over-two-arrays case in step 14; the missing-PME-shadow case in [[wiki/questions/QST-0014-pme-charge-gradient-enzyme-vs-finite-difference-mismatch]]).

### B. Electrostatic λ path, isolated from the intra-solute steric scheduler difference

[[wiki/answers/molly-master-migration-constraints-for-ffrefine]] (section E) already records that Molly master scales reaction-field/plain-Coulomb pair energy by the λ coupling (so a solute-solute pair scales as $\lambda_e$), where Molly `AWHGrads` scaled each solute charge (so a solute-solute pair scales as $\lambda_e^2$), and that this is a deliberate, accepted change (FFR-024). The numbers recorded there, however, were taken with `DefaultLambdaScheduler`'s default `intraLJ=false` on master, which also changes intra-solute steric (an)nihilation versus decoupling relative to `AWHGrads` (section E, point 2) — confounding the electrostatic-path comparison with the steric-scheduler difference.

Holding `intraLJ=true` fixed on master isolates the electrostatic path alone. On FFRefine's ethanol hydration setup (soft-core double-exponential sterics, reaction-field solvated leg, plain-Coulomb vacuum leg, solute = ethanol's 9 atoms), comparing CPU, Float64 (a Float64 copy of a Float32-built system), master with `intraLJ=true` minus `AWHGrads`:

| λ | Solvated Δ (kJ/mol) | Vacuum Δ (kJ/mol) |
|---|---|---|
| 1 | ≤ 2×10⁻¹⁵ | ≤ 2×10⁻¹⁵ |
| 0.5 | ≤ 2×10⁻¹⁵ | ≤ 2×10⁻¹⁵ |
| 0.25 | ≤ 2×10⁻¹⁵ | ≤ 2×10⁻¹⁵ |
| 0.75 | −13.205 | −3.827 |
| 0 | −0.050 | −0.050 |

Endpoints and the λ = 0.25/0.5 region agree to machine precision once the steric-scheduler difference is removed, confirming that point 3 of section E is specifically an electrostatic-path effect, not a combined effect. The λ = 0.75 differences are the pair-scaling-versus-per-charge-scaling difference acting alone. At λ = 0, both legs agree (−0.050 kJ/mol on both solvated and vacuum legs): `AWHGrads`' `LJZeroShortcut` makes intra-solute DEXP sterics vanish exactly at λ = 0, discontinuous with every λ > 0, while master with `intraLJ=true` is continuous through λ = 0 — this reproduces point 4 of section E (the λ = 0 discontinuity on `AWHGrads`) under the controlled `intraLJ=true` comparison and shows it is unaffected by the electrostatic-path choice.

**Consequence, unchanged from section E but now on cleaner evidence.** TSS biases, initial free-energy seeds, and replay archives built from `AWHGrads` runs are not valid for reaction-field λ ladders on master; the physical endpoints agree, so ΔG between them is path-independent in principle, but window overlap along the ladder may differ because the intermediate Hamiltonian differs. Both branches annihilate (not decouple) intra-solute electrostatics, consistently on both the solvated and vacuum legs, so the solvation thermodynamic cycle still closes on either branch; this connects to the overlay-correction caveat in [[wiki/claims/CLM-0023-decoupling-implementations-must-preserve-intramolecular-solute-terms]].

**Related, from step 14, recorded for context.** `ThermoState.beta` is stored at a different float precision across Molly eras (Float64 on master, the system's own float type — Float32 for FFRefine's builds — on `AWHGrads`), giving a uniform $3.6\times10^{-8}$ relative scale factor on every reduced potential at FFRefine's 301.15 K reference temperature; see [[wiki/answers/ffrefine-step14-enzyme-gradient-injection-and-beta-precision-validation]], section B. This factor is uniform and does not explain the λ = 0.75 differences above, which are two to three orders of magnitude larger and non-uniform between the solvated and vacuum legs.

## Key equations

$$
U_{\mathrm{AWHGrads}} \propto \lambda_e^2\, e_i e_j,
\qquad
U_{\mathrm{master}} \propto \lambda_e\, e_i e_j
\qquad \text{(reaction-field/plain-Coulomb solute-solute pair, as in [[wiki/answers/molly-master-migration-constraints-for-ffrefine]]).}
$$

## Sources used

None (no literature source). All content is FFRefine project evidence from refactor step 15, listed in this page's frontmatter.

## Wiki pages used

- [[wiki/answers/molly-master-migration-constraints-for-ffrefine]]
- [[wiki/questions/QST-0016-enzyme-map-struct-rebuild-silently-drops-gradient]]
- [[wiki/concepts/molly-jl-simulation-package-facts]]

## Wiki updates made

- Added this answer note.
- Added [[wiki/questions/QST-0017-enzyme-struct-field-layout-silently-drops-gradient]] for the open question behind finding A.
- Added a cross-link from [[wiki/questions/QST-0016-enzyme-map-struct-rebuild-silently-drops-gradient]] to the new question, since both document Enzyme silently dropping gradients depending on code shape or struct layout, by different mechanisms.
- Added a short addendum to section E of [[wiki/answers/molly-master-migration-constraints-for-ffrefine]] recording the controlled (`intraLJ=true`-held-fixed) electrostatic-path numbers above.
- Added a durable Molly fact (struct-layout/Enzyme pitfall) to [[wiki/concepts/molly-jl-simulation-package-facts]].
- Added a dated line to [[wiki/answers/ffrefine-decision-register]]'s `## Changes`, and a cross-reference from FFR-024's status.

## Remaining gaps

- The root Enzyme mechanism behind finding A is not understood, only worked around by struct reordering; see [[wiki/questions/QST-0017-enzyme-struct-field-layout-silently-drops-gradient]].
- The `LennardJones`/`Mie`/`AshbaughHatch` field reorder is verified against Molly's own test suite but is not yet merged into Molly master.
- Whether the `IllegalTypeAnalysisException` on mixed CPU systems and the GPU rejection of mixed systems share a root cause with finding A was not established.
- Finding B was probed on ethanol hydration only (CPU, Float64, a Float64 copy of a Float32-built system); hexane and water were not re-probed under the `intraLJ=true`-held-fixed comparison.
