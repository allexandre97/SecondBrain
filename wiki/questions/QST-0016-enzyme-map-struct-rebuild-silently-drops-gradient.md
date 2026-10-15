---
type: question
status: active
created: 2026-10-15
updated: 2026-10-15
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
  - "[[wiki/answers/ffrefine-step14-enzyme-gradient-injection-and-beta-precision-validation]]"
  - "[[wiki/questions/QST-0014-pme-charge-gradient-enzyme-vs-finite-difference-mismatch]]"
  - "[[wiki/concepts/molly-jl-simulation-package-facts]]"
sources: []
sensitivity: public
encryption: none
---

# Why Does Enzyme Reverse-Mode Silently Drop Part of a Gradient Through a Non-Inlined `map` That Rebuilds Structs?

## Question

Why does Enzyme (Julia, reverse mode, `set_runtime_activity`) silently return roughly half the correct Lennard-Jones σ/ϵ gradient, with no error or warning, when per-atom charge injection is written as `map(atoms, charges) do atom, q ... Atom(...) end` inside its own non-inlined function that returns a new `System`, while the same computation is correct when inlined into the differentiated closure, written as a broadcast or comprehension, or written as a `map` over `(atoms, indices)` instead of `(atoms, charges)`?

## Context

Found during FFRefine refactor step 14 (2026-10-15), while wiring Enzyme-differentiable parameter injection into production (Molly master `ac3ede15856d2ac8da18cbc7325a3fa49aaa8f0f`, Enzyme 0.13.216, Julia 1.12). FFRefine injects trained σ/ϵ/bonded parameters through Molly's own `inject_gradients`, then sets per-atom charges separately (master's parameter-container API has no charge support; see [[wiki/answers/molly-master-migration-constraints-for-ffrefine]], section A). The charge step was originally:

```julia
with_atom_charges(atoms, charges) = map(atoms, charges) do atom, q
    Atom(atom.index, atom.atom_type, atom.mass, q, atom.σ, atom.ϵ, atom.λ, atom.alch_role)
end
```

called from inside a non-inlined function that also called `inject_gradients` and rebuilt the `System`, then returned it to the differentiated loss closure. On a 3-molecule TIP3P water system this gave $\partial E/\partial \sigma_{\mathrm O} = -2.136$ from Enzyme versus $-4.4996$ from central finite differences — roughly half the correct magnitude, with no exception raised. Charge and bonded gradients computed in the same Enzyme call were correct; only the Lennard-Jones gradients of atoms whose charge passed through this specific `map` were affected.

Narrowing the reproduction found four variants that are all correct: (1) inlining the same injection/`map`/`System`-rebuild code directly into the body of the differentiated closure instead of calling a separate function; (2) replacing the `map` with a broadcast, `with_atom_charge.(atoms, charges)`; (3) replacing it with a comprehension; (4) keeping a `map`, but iterating over `(atoms, indices)` and looking up `charges[i]` inside the loop body instead of iterating over `(atoms, charges)` directly. Molly's own `inject_gradients` was correct in every variant tried; the fault tracked specifically to the `map`-over-two-parallel-arrays-while-constructing-a-struct shape, and specifically when that code sits across a non-inlined function boundary from the `autodiff` call site.

A related, but mechanistically distinct, failure was found in the same debugging session: differentiating through a container field that Enzyme treats as abstractly typed (a `Vector{Any}`-like field) made Enzyme compile `inject_gradients` behind a dynamic dispatch, which then failed loudly inside Molly's `inject_atoms` with `EnzymeNoDerivativeError` ("cannot handle unknown binary operator ... or disjoint i64"). That failure was fixed by calling `autodiff` on a function whose per-thermodynamic-state arguments are all concretely typed. Unlike the half-gradient bug this page is about, that one erred rather than silently returning a wrong value, so it is evidence that Enzyme can fail loudly on related code shapes, which sharpens rather than answers the question of why this particular shape fails silently instead.

This is FFRefine project evidence from refactor step 14 probes against FFRefine's own code and a small TIP3P water system; it has not been checked against an Enzyme issue tracker, an independent Enzyme test case outside Molly/FFRefine, or Enzyme release notes.

## Current Position

**Not resolved.** The practical workaround is established and verified (avoid `map` over two parallel arrays that builds a new struct inside a non-inlined function that itself returns the differentiated object; inline the code, use a broadcast/comprehension, or map over indices instead), and the final production validation after applying it shows water reaction-field and PME reduced-potential gradients against central finite differences agreeing to $\le 4\times10^{-8}$ relative for charges, σ, ϵ, DEXP α, and bond $k$ (see [[wiki/answers/ffrefine-step14-enzyme-gradient-injection-and-beta-precision-validation]], section A). But the underlying Enzyme mechanism — why this specific combination (two closed-over arrays consumed in lockstep by `map`, constructing a new struct per iteration, across a non-inlined function boundary) causes a partial, silent, non-erroring loss of exactly the cross-field (σ/ϵ) part of the gradient while leaving the charge and bonded gradients correct — is not understood. Candidate mechanisms that have not been tested against each other: an activity-inference error at the non-inlined function's boundary that marks one of the two mapped arrays (or the returned struct's non-charge fields) as inactive; an aliasing or shadow-reuse bug between the two arrays' shadows inside `map`; or a reverse-mode accumulation bug specific to constructing an immutable struct from two co-iterated arrays. This is a different symptom from the PME charge-gradient mismatch in [[wiki/questions/QST-0014-pme-charge-gradient-enzyme-vs-finite-difference-mismatch]] (that one affected charge gradients through PME's mutable grids and is resolved by passing PME `Duplicated`; this one affects σ/ϵ gradients through an ordinary immutable-struct rebuild, and no missing-shadow explanation has been identified).

**Evidence timeline**

- 2026-10-15: Found during FFRefine refactor step 14, on a 3-molecule TIP3P water system: Enzyme's $\partial E/\partial\sigma_{\mathrm O}=-2.136$ versus central finite difference $-4.4996$, with the fault isolated to a `map`-over-`(atoms, charges)`-rebuilding-`Atom`-structs pattern inside its own non-inlined function. Fixed by inlining, broadcasting, using a comprehension, or mapping over indices instead. Final production validation (same step) showed water reaction-field/PME gradients matching central finite differences to $\le4\times10^{-8}$ relative after the fix. [[wiki/answers/ffrefine-step14-enzyme-gradient-injection-and-beta-precision-validation]]

**Methodological lesson that does not depend on resolving the mechanism:** differentiable-simulation gradient paths need an explicit finite-difference gate; agreement between two Enzyme-based formulations of the same computation is not sufficient evidence of correctness, because both can share the same silent failure mode. FFRefine's own step-13a container benchmark compared a vector-θ Enzyme path against a `Base.Dict` Enzyme path to $10^{-12}$ agreement (FFR-049 in [[wiki/answers/ffrefine-decision-register]]) without exercising the post-injection charge rebuild, and so could not have caught this bug.

## Links

- [[wiki/answers/ffrefine-step14-enzyme-gradient-injection-and-beta-precision-validation]]
- [[wiki/questions/QST-0014-pme-charge-gradient-enzyme-vs-finite-difference-mismatch]]
- [[wiki/answers/molly-master-migration-constraints-for-ffrefine]]
- [[wiki/concepts/molly-jl-simulation-package-facts]]
- [[wiki/answers/ffrefine-decision-register]]
