---
type: answer
status: active
created: 2026-10-15
updated: 2026-10-15
question: "What did FFRefine refactor step 14 (2026-10-15) establish about wiring Enzyme-differentiable parameter injection into production, and about comparing gradients and reference numbers across the Molly `AWHGrads`-to-`master` precision change?"
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
  - validation
  - precision
related:
  - "[[wiki/answers/molly-master-migration-constraints-for-ffrefine]]"
  - "[[wiki/answers/ffrefine-decision-register]]"
  - "[[wiki/questions/QST-0014-pme-charge-gradient-enzyme-vs-finite-difference-mismatch]]"
  - "[[wiki/questions/QST-0016-enzyme-map-struct-rebuild-silently-drops-gradient]]"
  - "[[wiki/concepts/molly-jl-simulation-package-facts]]"
sources: []
sensitivity: public
encryption: none
wiki_pages_used:
  - "[[wiki/answers/molly-master-migration-constraints-for-ffrefine]]"
  - "[[wiki/answers/ffrefine-decision-register]]"
  - "[[wiki/questions/QST-0014-pme-charge-gradient-enzyme-vs-finite-difference-mismatch]]"
raw_sources_consulted: []
wiki_pages_updated:
  - "[[wiki/answers/ffrefine-decision-register]]"
  - "[[wiki/questions/QST-0016-enzyme-map-struct-rebuild-silently-drops-gradient]]"
project_evidence:
  - "FFRefine refactor step 14, 2026-10-15 (working tree on top of commit `a99b2a3`, \"Step 13b ready\"; not yet committed): wired the `FFParameterSet` parameter container (FFR-049) into production gradient injection in `src/gradients.jl`, `src/molly_compat.jl`, and `src/solvation_pipeline.jl`; added `test/finite_difference_checks.jl` as a finite-difference gate for Enzyme gradients. Molly pinned at master `ac3ede15856d2ac8da18cbc7325a3fa49aaa8f0f`, Enzyme 0.13.216, Julia 1.12."
scope: snapshot
currency: current
as_of: 2026-10-15
as_of_commit:
  - FFRefine@a99b2a3
  - Molly@ac3ede15856d2ac8da18cbc7325a3fa49aaa8f0f
---

# FFRefine Step 14: Enzyme Gradient-Injection Validation and Molly-Era β-Precision Mapping

## Short answer

Wiring FFRefine's Enzyme-differentiable parameter container (FFR-049) into production gradient injection, during refactor step 14 (2026-10-15, Molly master `ac3ede15`), produced two durable findings, both found only because a finite-difference gate was added rather than relying on agreement between two differentiable-simulation code paths. First, Enzyme reverse-mode silently dropped roughly half of the Lennard-Jones σ/ϵ gradient, with no error raised, when per-atom charge injection was written as a `map` over atoms and charges that rebuilds `Atom` structs inside its own non-inlined function; charge and bonded gradients computed in the same call were unaffected. Second, comparing Molly-master gradients and energies against Molly-`AWHGrads`-era reference numbers is confounded by a precision change in how `ThermoState.beta` is computed, which imposes a uniform relative scale factor on every reduced potential and parameter gradient; FFRefine now rescales `AWHGrads`-era references by this factor ("era mapping") before comparing them to master.

## Detailed answer

### A. Enzyme silently drops part of a gradient through a non-inlined `map` that rebuilds structs

FFRefine injects trained parameters into a Molly `System` by calling Molly's own `inject_gradients` (master's parameter-container API; see [[wiki/answers/molly-master-migration-constraints-for-ffrefine]], section A) and then setting per-atom charges separately, since master's `extract_parameters`/`ParameterPlan` does not carry charges. The charge step was written as

```julia
with_atom_charges(atoms, charges) = map(atoms, charges) do atom, q
    Atom(atom.index, atom.atom_type, atom.mass, q, atom.σ, atom.ϵ, atom.λ, atom.alch_role)
end
```

Differentiated with Enzyme reverse mode (`set_runtime_activity`) on a 3-molecule TIP3P water system, the Lennard-Jones gradients came out at about half their correct value, with no error or warning: $\partial E/\partial \sigma_{\mathrm O} = -2.136$ (Enzyme) versus $-4.4996$ (central finite difference). Charge and bonded gradients computed in the same differentiated call were correct. Splitting the investigation by code shape found the error appeared only when the parameter injection, the `map`-based charge rebuild, and the `System` reconstruction sat together in their own non-inlined function that returned the new `System`. The same code, inlined directly into the body of the differentiated closure, was correct; so was rewriting the charge step as a broadcast (`with_atom_charge.(atoms, charges)`), as a comprehension, or as a single `map` over `(atoms, indices)` instead of `(atoms, charges)`. Molly's own `inject_gradients` was correct in every variant tested; the fault was specific to this particular `map`-over-two-arrays-building-a-struct shape sitting across a non-inlined function boundary.

A related but distinct failure was found while debugging the same injection path: differentiating through a container field that Enzyme sees as abstractly typed (a `Vector{Any}`-like field) made Enzyme compile `inject_gradients` behind a dynamic dispatch, and it then failed inside Molly's `inject_atoms` with `EnzymeNoDerivativeError`, reporting "cannot handle unknown binary operator ... or disjoint i64". This was fixed by calling `autodiff` on a function whose per-thermodynamic-state arguments are all concretely typed, rather than on a function that closes over an abstractly typed container. Unlike the half-gradient bug, this one failed loudly rather than silently.

**Lesson.** Differentiable-simulation code paths need an explicit finite-difference gate; cross-checking two AD formulations against each other is not sufficient, because both can share the same silent failure. FFRefine's own step-13a container benchmark had compared a vector-θ Enzyme path against a `Base.Dict` Enzyme path and found them identical to $10^{-12}$ (see FFR-049 in [[wiki/answers/ffrefine-decision-register]]) — a check that could not have caught this bug, since both paths used Enzyme and neither exercised the post-injection charge rebuild. Only comparing against central finite differences surfaced it.

**Final validation (step 14).** With the charge-injection step fixed (inlined / broadcast / comprehension / `map` over indices, not over `(atoms, charges)` in its own function), water reaction-field and PME reduced-potential gradients against central finite differences agree to $\le 4\times10^{-8}$ relative for charges, σ, ϵ, DEXP α, and bond $k$. PME charge gradients specifically agree to about $10^{-9}$, including the PME reciprocal-space part alone ($4.7\times10^{-11}$). This reconfirms, on Molly master with PME passed as an Enzyme `Duplicated` general interaction (shadow created with `Enzyme.make_zero`), the resolution already recorded in [[wiki/questions/QST-0014-pme-charge-gradient-enzyme-vs-finite-difference-mismatch]]: the `AWHGrads`-era Enzyme charge-gradient values remain off from this result by the same $3.8\times10^{-3}$ (O) / $5.7\times10^{-3}$ (H) relative amounts recorded there. Step 14 adds no new information about QST-0014 itself; it independently reproduces the same numbers from the production injection path rather than a one-off probe.

### B. Molly-era β precision requires rescaling `AWHGrads`-era references

Molly's `AWHGrads` branch computed `ThermoState.beta` as `FT(ustrip(1/kBT))`, where `FT` is the system's own float type (Float32 for FFRefine's Float32-built systems). Molly `master` computes the same quantity as `TH(...)`, where `TH` is `float_type_high`, defaulting to Float64 (see [[wiki/answers/molly-master-migration-constraints-for-ffrefine]], section C, on `float_type_high`). At FFRefine's reference temperature of 301.15 K (`301.15f0` K as a Float32 literal), this changes every reduced potential and every one of its parameter gradients by the same uniform multiplicative factor,

$$
\frac{\beta_{64}}{\beta_{32}} = \frac{1/(k_BT)\ \text{in Float64}}{\mathrm{Float64}(\mathrm{Float32}(1/(k_BT)))} = 1 + 3.6128667\times10^{-8} .
$$

Because this factor is applied uniformly, reference numbers computed on `AWHGrads` cannot be matched against master at the $10^{-8}$ relative tolerance FFRefine otherwise uses for Enzyme-vs-finite-difference gates (section A above), even when both branches' physics and gradients are otherwise correct. FFRefine's Phase 0 baseline references (`test/baselines/`, recorded on `AWHGrads`) are therefore compared against master via an "era mapping": each reference value is rescaled by $\beta/\mathrm{Float64}(\mathrm{Float32}(\beta))$ before comparison. After this rescaling, residuals are $\le 3.8\times10^{-10}$.

**Generalizable lesson.** When reference numbers are carried across a library version change, a precision change in a derived thermodynamic constant (here β; the same reasoning applies to pressure or any other quantity computed from unit-stripped physical constants) can introduce a uniform scale offset that looks exactly like a gradient or energy error. The diagnostic is to check whether the relative offset between old and new values is identical across every quantity compared (energies, and every parameter family's gradient); a uniform offset points to a precision or unit-convention change upstream of the physics, not to a gradient bug, whereas a non-uniform offset (as in section A) points to an actual AD or implementation defect.

## Key equations

$$
\frac{\beta_{64}}{\beta_{32}} = 1 + 3.6128667\times10^{-8} \quad\text{at } T = 301.15\ \text{K, Float32 system}.
$$

## Sources used

None (no literature source). All content is FFRefine project evidence from refactor step 14, listed in this page's frontmatter.

## Wiki pages used

- [[wiki/answers/molly-master-migration-constraints-for-ffrefine]]
- [[wiki/answers/ffrefine-decision-register]]
- [[wiki/questions/QST-0014-pme-charge-gradient-enzyme-vs-finite-difference-mismatch]]

## Wiki updates made

- Added this answer note.
- Added [[wiki/questions/QST-0016-enzyme-map-struct-rebuild-silently-drops-gradient]] for the open question behind finding A (why a non-inlined `map`-based struct rebuild specifically triggers silent, partial gradient loss).
- Updated FFR-049 in [[wiki/answers/ffrefine-decision-register]] to record that the parameter container is now wired into production gradient injection, and added a dated line to that page's `## Changes`.

## Remaining gaps

- The exact Enzyme mechanism behind the silent half-gradient loss (finding A) is not understood, only worked around; see [[wiki/questions/QST-0016-enzyme-map-struct-rebuild-silently-drops-gradient]].
- Finding A was probed on a 3-molecule TIP3P system and the final validation on water reaction-field/PME; it has not been checked for hexane, ethanol, or GPU execution.
- The β-precision offset (finding B) was derived and checked at one temperature (301.15 K); the factor is temperature-dependent in general (it depends on how close the Float32 and Float64 roundings of $1/(k_BT)$ are), so it should be recomputed, not assumed constant, for other reference temperatures.
