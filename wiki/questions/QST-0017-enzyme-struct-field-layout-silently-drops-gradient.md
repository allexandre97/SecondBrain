---
type: question
status: active
created: 2026-10-16
updated: 2026-10-16
question_status: partially-answered
areas:
  - research
categories:
  - research/molecular-simulation/molecular-dynamics
  - research/molecular-simulation/force-fields
  - research/scientific-computing
tags:
  - question
  - enzyme
  - autodiff
  - molly
  - gradient-validation
related:
  - "[[wiki/answers/ffrefine-step15-enzyme-struct-layout-gradient-loss]]"
  - "[[wiki/questions/QST-0016-enzyme-map-struct-rebuild-silently-drops-gradient]]"
  - "[[wiki/questions/QST-0014-pme-charge-gradient-enzyme-vs-finite-difference-mismatch]]"
  - "[[wiki/concepts/molly-jl-simulation-package-facts]]"
sources: []
sensitivity: public
encryption: none
---

# Why Does Enzyme Reverse-Mode Silently Zero a Gradient Depending on Struct Field Layout and a Never-Taken Type-Unstable Branch?

## Question

Why does Enzyme (Julia, reverse mode, `set_runtime_activity(Reverse)`) silently return exactly `0.0` for a gradient with respect to a `Float64` field of an immutable struct — with no error or warning, while central finite differences give the correct non-zero value — depending only on (a) whether a `Bool` field of that struct is followed by a zero-size field and/or padding before the `Float64` field, and (b) whether the differentiated code contains a type-unstable branch (on a runtime `Bool`) whose non-taken side calls `filter` on a small heterogeneous tuple, even though that branch is never taken at the differentiated point?

## Context

Found during FFRefine refactor step 15 (2026-10-16), auditing Molly.jl master's own `@test_broken` parameter-gradient entries (Enzyme 0.13.216, Enzyme_jll 0.0.303, Julia 1.12.7, Linux x86_64 — the newest Enzyme release at the time). Symptom in Molly: gradients with respect to interaction-parameter fields injected through Molly's `inject_gradients`/`ParameterPlan` came out exactly `0.0` while central finite differences were non-zero, for `DoubleExponentialSoftCore`'s `weight_14` field and for every field of every later pairwise interaction in the same `general_inters` tuple (for example `coulomb_const` and `weight_14` of a `CoulombScaled` or plain `Coulomb` that followed a `DoubleExponentialSoftCore`). The same symptom affected `weight_14` of `LennardJones`, `Mie`, and `AshbaughHatch` (Molly's own tests already marked these `@test_broken`). Atom parameters (σ, ϵ, charges) and interaction fields positioned before the triggering field in the tuple were correct. No error, no warning.

Bisection on Molly's own code: a single pairwise interaction's own derivative, computed from the bare interaction struct or passed to the energy function by keyword, was correct. The gradient was lost only once the parameter-injected interactions were stored inside the mutable `System` and read back out from inside the differentiated energy function — i.e. once the computation went through Molly's `with_pairwise_partition`, which branches at runtime on each interaction's `use_neighbors::Bool` and, in the mixed case (some interactions use the neighbor list, some do not), calls the pairwise loop on `filter()`-ed sub-tuples of the (small, `isbits`) interaction tuple.

A pure-Julia minimal reproducer, with no Molly dependency, isolates the same failure:

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

This prints `Bad` → `0.0`, `NoZ` → `6.0`, `BoolLast` → `6.0` (expected `6.0` in all three cases). All three ingredients in this reproducer were needed together: the `Bad` field layout (`Bool`, then a zero-size field, then the `Float64`, leaving a padding byte before it), the never-taken but type-unstable `filter` branch, and a closure that reads a field of the mutable struct holding the tuple. Removing `set_runtime_activity` makes Enzyme throw `EnzymeRuntimeActivityError` instead of silently returning `0.0`. A separate, apparently unrelated internal Enzyme failure (`AssertionError: length(remaining) < length(dead)`) appeared while narrowing this down, when differentiating anonymous closures that close over globals; it was not reduced further and is not part of this reproducer.

**Fix that resolves the Molly symptom.** Reordering the affected structs' fields so a `Bool` does not precede the `Float64` parameters with intervening padding or zero-size fields — for `DoubleExponentialSoftCore`, moving its scheduler field to sit immediately after `use_neighbors`, matching Molly's other λ-interactions' layout; for `LennardJones`/`Mie`/`AshbaughHatch`, moving `use_neighbors::Bool` to be the last field — makes Molly's own parameter-injection gradient test suite pass 181/181 with no `@test_broken` entries, and does not change any of Molly's other 2443 CPU tests. The `DoubleExponentialSoftCore` reorder has been merged into Molly master; the `LennardJones`/`Mie`/`AshbaughHatch` reorder exists only on an unmerged branch as of this writing.

**Negative result: changing the branch instead of the struct does not fix Molly.** Moving the mixed-partition branch into a `@noinline` function fixes the pure reproducer above but not Molly's real `potential_energy`. Replacing the mixed branch with an error, restructuring it as a check followed by a two-way (rather than filter-based) branch, marking the mixed code path `EnzymeRules.inactive`, forcing per-interaction static dispatch, or giving the loop a distinct method instance also did not fix Molly. Semantically identical code differed in outcome: a `do`-block closure failed where an equivalent local named function, or an equivalent inline closure, passing through the same logic, did not. This indicates the `filter`-branch shape is one trigger that reproduces the bug in isolation, not the underlying cause, and that the loss is sensitive to incidental compilation shape in a way that makes code-level workarounds (as opposed to the struct-layout fix) unreliable.

**Related, found in the same investigation.** On Molly master, CPU gradients of "mixed" systems (where some pairwise interactions use the neighbor list and others do not) fail with `IllegalTypeAnalysisException` rather than returning a silently wrong value; Molly's GPU reverse-mode rules reject mixed systems explicitly. These are distinct failure modes from the silent zero described above (they error rather than silently returning a wrong answer), but occur in the same code region (`with_pairwise_partition`'s mixed-case handling) and may share a root cause with it.

This is FFRefine project evidence from refactor step 15 (2026-10-16), probing Molly master's own parameter-gradient test suite and a standalone Enzyme reproducer; it has not been checked against an Enzyme issue tracker or Enzyme release notes. The operator plans to file an Enzyme.jl issue using the minimal reproducer above, but has not done so as of this writing.

## Current Position

**Not resolved; workaround found and merged (partially) upstream.** The practical defence — reordering struct fields so a `Bool` field is not followed by a zero-size field or padding before `Float64` parameters — is verified to fix Molly's own test suite for `DoubleExponentialSoftCore` (merged into Molly master) and for `LennardJones`/`Mie`/`AshbaughHatch` (on an unmerged branch). The underlying Enzyme mechanism is not understood: why a `Bool`-then-zero-size-then-`Float64` layout, combined with a *never-executed* type-unstable branch elsewhere in the call graph, causes Enzyme's reverse pass to zero a derivative rather than compute it correctly or error. This is a different manifestation from [[wiki/questions/QST-0016-enzyme-map-struct-rebuild-silently-drops-gradient]] (that one silently halves a gradient through a non-inlined `map` that rebuilds structs from two parallel arrays; this one silently zeros a gradient depending on field layout and a dead branch) and from [[wiki/questions/QST-0014-pme-charge-gradient-enzyme-vs-finite-difference-mismatch]] (resolved; caused by a missing Enzyme shadow on PME's mutable grids, not by struct layout). Together, these three findings establish a pattern: **Enzyme reverse-mode AD, at this version, can silently drop or corrupt gradients in ways that depend on struct memory layout and on code shapes unrelated to the mathematics being differentiated** (a dead branch, a `map` over two arrays, a missing shadow). No single explanation covers all three; each needed its own bisection and finite-difference check to find.

**Methodological lesson that does not depend on resolving the mechanism.** Differentiable-simulation gradient code needs a finite-difference gate per interaction type *and* per combination of interaction types present in one system, not just per isolated interaction; a single-interaction check would have missed this bug, since only interactions sharing a tuple with a triggering layout, or sitting downstream of one, were affected. Cross-checking two Enzyme-based code paths against each other is insufficient, because both can share the same silent failure mode — the same lesson already recorded from [[wiki/questions/QST-0016-enzyme-map-struct-rebuild-silently-drops-gradient]]. A related, independent step-14 finding reinforces it: Enzyme dropped about half of a σ/ϵ gradient through a `map(f, a, b)` that built structs behind a non-inlined function boundary, while the equivalent broadcast or comprehension form was correct.

**Evidence timeline**

- 2026-10-16: Found during FFRefine refactor step 15, auditing Molly master's `@test_broken` parameter-gradient entries for `DoubleExponentialSoftCore`, `LennardJones`, `Mie`, and `AshbaughHatch`. Isolated to a pure-Julia reproducer requiring a `Bool`-then-zero-size-field-then-`Float64` struct layout plus a never-taken type-unstable `filter` branch. Fixed in Molly by reordering struct fields (merged for `DoubleExponentialSoftCore`; unmerged branch for `LennardJones`/`Mie`/`AshbaughHatch`); code-shape changes to the branch itself did not fix the real Molly code even where they fixed the pure reproducer. [[wiki/answers/ffrefine-step15-enzyme-struct-layout-gradient-loss]]

## Links

- [[wiki/answers/ffrefine-step15-enzyme-struct-layout-gradient-loss]]
- [[wiki/questions/QST-0016-enzyme-map-struct-rebuild-silently-drops-gradient]]
- [[wiki/questions/QST-0014-pme-charge-gradient-enzyme-vs-finite-difference-mismatch]]
- [[wiki/concepts/molly-jl-simulation-package-facts]]
- [[wiki/answers/ffrefine-decision-register]]
