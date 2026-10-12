---
type: answer
status: active
created: 2026-10-11
updated: 2026-10-12
question: "What phased implementation plan was proposed on 2026-07-02 for testing replay force-field optimization with AWH, TSS, and MBAR reference adapters?"
answer_status: answered
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/molecular-simulation/free-energy
  - research/adaptive-sampling
  - research/scientific-computing
tags:
  - force-field-optimization
  - replay-reweighting
  - times-square-sampling
  - mbar
  - awh
  - implementation-route
related:
  - "[[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]]"
  - "[[wiki/answers/ffrefine-current-implementation-status]]"
  - "[[wiki/answers/ffrefine-decision-register]]"
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
  - "[[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]"
  - "[[wiki/questions/force-field-training-validation-scope]]"
sources:
  - SRC-0005
  - SRC-0006
  - SRC-0018
  - SRC-0023
sensitivity: public
encryption: none
wiki_pages_used:
  - "[[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]]"
raw_sources_consulted: []
wiki_pages_updated: []
project_evidence:
  - "Route-plan analysis written on 2026-07-02 for the user's replay force-field optimization project (which became FFRefine), drawn from SRC-0005, SRC-0006, SRC-0018 and SRC-0023; a planning document, not a repository audit; originally part of [[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]]"
  - "FFRefine ethanol-solvation windowed-TSS replay scaffold test, commit `eb401bb` (2026-07-07), revising the windowed-TSS steps of Phase 4"
scope: snapshot
currency: historical
as_of: 2026-07-07
---

# Phased Implementation Plan for Testing Replay Force-Field Optimization With AWH, TSS, and MBAR (proposed 2026-07-02; windowed-TSS steps revised 2026-07-07)

> [!currency] Historical — describes the state as of 2026-07-07; kept as a record, not as the current state.
> Plan as proposed on 2026-07-02; windowed-TSS steps revised 2026-07-07 (commit eb401bb). FFRefine's later implementation and current plan are in ffrefine-current-implementation-status and ffrefine-decision-register.

## Short answer

On 2026-07-02 the recommended route was to define sampler-agnostic interfaces, lock down the SRC-0018 AWH path as the control, implement an MBAR baseline first, then a minimal nonwindowed TSS-as-reference prototype (adding windowed TSS only after that works), and finally compare AWH, TSS, and MBAR on one benchmark under the same validation standard. On 2026-07-07, a FFRefine ethanol-solvation implementation test (commit `eb401bb`) revised the windowed-TSS steps of Phase 4 below from preserving global reference-density metadata to computing and stitching local per-window replay estimates. The design analysis behind this plan (common inner machinery, adapter differences, key equations) is in [[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]]. This page keeps the plan as it stood after that revision; it was moved here from that page on 2026-10-11 when the design analysis was separated from project state.

## Detailed answer

### Phase 1: Define the sampler-agnostic interfaces

Implement or refactor around four interfaces:

| Interface | Responsibility | Method-specific? |
| --- | --- | --- |
| `ReferenceArchive` | Store frames, visited states/windows, volumes, reference energies, and metadata. | Mostly common. |
| `ReferenceAdapter` | Provide `log_reference_mixture(frame)` and readiness diagnostics. | Yes. |
| `ReplayEstimator` | Compute target free energies, observables, gradients, ESS, and split diagnostics. | Mostly common. |
| `TrustRegionOptimizer` | Build loss, Fisher metric, KL-scaled step, and acceptance decisions. | Common. |

The hard boundary is that `TrustRegionOptimizer` should not know whether the archive came from AWH, TSS, or MBAR. It should only consume predictions, gradients, Fisher estimates, and diagnostics.

### Phase 2: Lock down the AWH control path

Keep the existing SRC-0018 AWH path as the reference implementation. Add regression tests around:

- frozen reference mixture denominator,
- endpoint replay free energies,
- endpoint gradients,
- observable replay estimate and gradient,
- candidate-ensemble ESS,
- Fisher score covariance,
- line-search rejection on low ESS,
- replay/AWH parity gate. [SRC-0018]

This phase prevents the TSS and MBAR experiments from moving the target.

### Phase 3: Implement the MBAR baseline first

The MBAR baseline is the cleanest first alternative because it does not require adaptive sampler implementation.

1. Choose a small thermodynamic cycle, such as the ethanol hydration example already used by SRC-0018. [SRC-0018]
2. Run fixed equilibrium or biased simulations at a discrete lambda schedule.
3. Decorrelate or stride frames and build a cross-state reduced-potential matrix $u_k(x_n)$.
4. Solve MBAR for the reference sampled states or import the reference $\hat f_k$ values. [SRC-0023]
5. Implement `MBARReferenceAdapter.log_reference_mixture`.
6. Evaluate endpoint targets as unsampled candidate states against the fixed reference mixture.
7. Reuse the common replay gradient, observable, ESS, Fisher, and line-search logic.
8. After each accepted parameter update, run a short independent resimulation check before allowing additional trust-region steps.

Success criteria:

- free energies match standard MBAR at the reference parameterization,
- replay gradients pass finite-difference checks,
- ESS and overlap decline predictably as parameter perturbations grow,
- accepted updates improve the tolerance-normalized objective and survive resimulation.

### Phase 4: Implement a minimal TSS-as-reference prototype

Start with the smallest TSS feature set that can generate a fixed reference archive:

1. Implement a nonwindowed TSS sampler over the same lambda schedule, or choose a small enough schedule that windows are unnecessary.
2. Run adaptive TSS until free-energy estimates, rung occupancy, and visit-control diagnostics stabilize.
3. Freeze the TSS sampling distribution: no stochastic-approximation updates, no history forgetting, and no changing visit-control tilts during production.
4. Collect frozen production frames with visited rung metadata.
5. Export the exact frozen denominator used by the production kernel.
6. Plug the archive into the common replay estimator.

Only after this nonwindowed path works should the implementation add windowed TSS:

1. Store active window labels and local rung sets.
2. Export local window denominators for every retained frame.
3. Compute replay free energies and observable averages locally inside each active window.
4. Stitch local replay free-energy surfaces with the same reported TSS equations used for ordinary local estimates.
5. Stitch local observable averages with the reported window probabilities and global rung density.
6. Add window stitching diagnostics from SRC-0006 as readiness checks, but keep replay weights tied to the actual frozen production density. [SRC-0006]

Success criteria:

- TSS reported profile and replayed profile agree within configured tolerance on supported states,
- split-epoch and split-half estimates are stable,
- window offsets are connected and not dominated by one weak overlap,
- the same optimizer can consume TSS archives without sampler-specific branches.

### Phase 5: Compare AWH, TSS, and MBAR under one benchmark

Use one benchmark before expanding:

- same molecule or system,
- same lambda schedule where possible,
- same trainable parameter subset,
- same experimental or reference targets,
- same optimizer settings,
- same validation resimulations.

Report:

- wall-clock and force-evaluation cost,
- target loss improvement per macro epoch,
- ESS after each accepted step,
- split-half disagreement,
- parity or profile disagreement,
- number of rejected line-search proposals,
- number of forced resimulations,
- held-out observable or held-out lambda validation.

Do not rank methods by final training loss alone. The relevant question is which method produces reference archives that support reliable parameter updates under the same validation standard. [SRC-0018] [[wiki/questions/force-field-training-validation-scope]]

## Recommended first prototype

Build the MBAR baseline first, then the minimal nonwindowed TSS adapter.

MBAR first is useful because it tests the sampler-agnostic optimizer with the least new sampling code. It will also expose whether the current replay and Fisher implementation truly depends on AWH-specific assumptions. [SRC-0023] [SRC-0018]

TSS second is the real test of the user's idea. If TSS frozen archives give higher support or lower split uncertainty than AWH or MBAR for the same system, then TSS is not just another estimator; it becomes a better adaptive reference generator for replay-based force-field optimization. [SRC-0005] [SRC-0006]

## Sources used

- SRC-0018 for the AWH control path, replay regression targets, the ethanol hydration example, and the validation standard.
- SRC-0023 for the MBAR baseline.
- SRC-0005 and SRC-0006 for the nonwindowed and windowed TSS prototypes and window-stitching diagnostics.

## Wiki pages used

- [[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]]

## Wiki updates made

- Created on 2026-10-11 by moving the "Implementation route plan" and "Recommended first prototype" sections, unchanged, out of [[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]].

## Remaining gaps

- The wiki does not record a phase-by-phase account of how this plan was carried out. FFRefine's later implementation (TSS archives with window-mixture MBAR replay) is described in [[wiki/answers/ffrefine-current-implementation-status]] and its decisions in [[wiki/answers/ffrefine-decision-register]].
