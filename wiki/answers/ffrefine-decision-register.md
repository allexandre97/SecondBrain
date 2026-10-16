---
type: answer
status: active
created: 2026-10-11
updated: 2026-10-16
question: "What has the FFRefine project decided, what is implemented, and what is still open?"
answer_status: answered
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/molecular-simulation/free-energy
  - research/scientific-computing
tags:
  - ffrefine
  - project-decision
  - decision-register
  - implementation-status
related:
  - "[[wiki/answers/ffrefine-current-implementation-status]]"
  - "[[wiki/answers/ffrefine-generalist-package-plan-decisions]]"
  - "[[wiki/answers/ffrefine-direction-gates-and-production-policy]]"
  - "[[wiki/answers/ffrefine-loss-gate-diagnostic-policy]]"
  - "[[wiki/answers/adding-config-optimiser-to-ffrefine]]"
  - "[[wiki/answers/ffrefine-improved-gates-water-run-lessons]]"
  - "[[wiki/answers/ffrefine-multi-series-equilibration-cut-calibration]]"
  - "[[wiki/answers/molly-master-migration-constraints-for-ffrefine]]"
  - "[[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]]"
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
  - "[[wiki/answers/ffrefine-config-vs-weighted-sum-water-campaign-results]]"
  - "[[wiki/answers/ffrefine-kl-definition-for-extended-ensemble-training]]"
  - "[[wiki/claims/CLM-0039-trust-region-kl-must-match-replay-conditioning]]"
  - "[[wiki/claims/CLM-0044-config-must-exclude-directionally-unreliable-families]]"
  - "[[wiki/claims/CLM-0047-calibrated-materiality-threshold-prevents-multi-series-equilibration-over-cutting]]"
  - "[[wiki/claims/CLM-0048-family-weight-renormalisation-changes-natural-gradient-step-length]]"
  - "[[wiki/claims/CLM-0049-few-block-pseudo-value-covariance-understates-promise-null]]"
  - "[[wiki/claims/CLM-0050-retesting-a-failed-gate-after-extension-needs-alpha-spending]]"
  - "[[wiki/questions/QST-0006-average-observable-trainability-sampling-budget]]"
  - "[[wiki/questions/QST-0007-checkpoint-assessment-versus-next-direction-readiness]]"
  - "[[wiki/questions/QST-0010-damped-fisher-config-compatibility]]"
  - "[[wiki/questions/QST-0011-config-versus-weighted-sum-under-calibrated-direction-gates]]"
  - "[[wiki/questions/QST-0012-persistent-replay-prediction-optimism-for-one-family]]"
  - "[[wiki/questions/QST-0013-step-length-policy-after-family-exclusion]]"
  - "[[wiki/questions/QST-0014-pme-charge-gradient-enzyme-vs-finite-difference-mismatch]]"
  - "[[wiki/questions/QST-0015-rdf-density-dielectric-pareto-front-for-this-water-parameterisation]]"
  - "[[wiki/questions/QST-0016-enzyme-map-struct-rebuild-silently-drops-gradient]]"
  - "[[wiki/answers/ffrefine-step14-enzyme-gradient-injection-and-beta-precision-validation]]"
  - "[[wiki/questions/QST-0017-enzyme-struct-field-layout-silently-drops-gradient]]"
  - "[[wiki/answers/ffrefine-step15-enzyme-struct-layout-gradient-loss]]"
  - "[[wiki/questions/force-field-training-validation-scope]]"
  - "[[wiki/tensions/TEN-0020-config-family-exclusion-versus-untreated-drift]]"
sources: []
sensitivity: public
encryption: none
wiki_pages_used:
  - "[[wiki/answers/ffrefine-current-implementation-status]]"
  - "[[wiki/answers/ffrefine-generalist-package-plan-decisions]]"
  - "[[wiki/answers/ffrefine-direction-gates-and-production-policy]]"
  - "[[wiki/answers/ffrefine-loss-gate-diagnostic-policy]]"
  - "[[wiki/answers/adding-config-optimiser-to-ffrefine]]"
  - "[[wiki/answers/ffrefine-improved-gates-water-run-lessons]]"
  - "[[wiki/answers/ffrefine-multi-series-equilibration-cut-calibration]]"
  - "[[wiki/answers/molly-master-migration-constraints-for-ffrefine]]"
  - "[[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]]"
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
raw_sources_consulted: []
wiki_pages_updated:
  - "[[wiki/answers/ffrefine-current-implementation-status]]"
  - "[[wiki/answers/ffrefine-direction-gates-and-production-policy]]"
  - "[[wiki/answers/ffrefine-loss-gate-diagnostic-policy]]"
  - "[[wiki/answers/adding-config-optimiser-to-ffrefine]]"
  - "[[wiki/answers/ffrefine-improved-gates-water-run-lessons]]"
  - "[[wiki/answers/ffrefine-multi-series-equilibration-cut-calibration]]"
  - "[[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]]"
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
  - "[[wiki/answers/molly-master-migration-constraints-for-ffrefine]]"
  - "[[wiki/questions/QST-0017-enzyme-struct-field-layout-silently-drops-gradient]]"
  - "[[wiki/concepts/molly-jl-simulation-package-facts]]"
project_evidence:
  - "FFRefine ethanol-solvation windowed-TSS replay scaffold test, 2026-07-07"
  - "FFRefine parameter-training refactor and shared-parameter (charge-key) update, 2026-07-15"
  - "FFRefine commit d48d2f1 (2026-07-16, \"Group charges by atom type\")"
  - "FFRefine epoch-control update, 2026-07-18"
  - "FFRefine parameter-bounds update, 2026-07-22"
  - "FFRefine window-mixture MBAR implementation and focused tests, 2026-07-24"
  - "FFRefine ConFIG optimizer and post-Fisher momentum implementation and focused tests, 2026-07-28"
  - "FFRefine water-temperature memory isolation implementation, 2026-07-29"
  - "FFRefine Fisher/KL conditioning analysis, 2026-08-29"
  - "FFRefine clean HEAD audit on 2026-09-23 at a3b6aa5 (ConFIG finite-step family regressions reported, not vetoed)"
  - "FFRefine run water_rdf-dens-diel_aggressive, observed 2026-09-24 (ConFIG step collapse; loss-gate behaviour)"
  - "FFRefine water run 20260924-204914 and the `improved-gates` design work, 2026-09-28"
  - "FFRefine master audit on 2026-10-01 at 6b20031 (direction gates authoritative since 26affa0 and production policy since e49cfde, both 2026-09-30)"
  - "FFRefine commit 110fe64 (2026-10-07, \"Damped Levenberg-Marquardt trust-region step; report-only direction gates\")"
  - "FFRefine repository planning document `ffrefine_package_plan.md`, dated 2026-10-11 (decisions A, B, L, F, E, P, C, S, R, D, K, H, Q, N and the Molly work list U1-U8)"
  - "FFRefine audit on 2026-10-11 confirming that the molecule-template charge-key code is dead"
  - "FFRefine Molly-master probes on 2026-10-15 against Molly master `623d314a` plus the unmerged system-conversion PR branch (U2, head `0e4b8819`): PME charge-gradient Enzyme-vs-finite-difference resolution, PME/Enzyme thread safety, PME energy parity against Phase 0 baselines, and a parameter-container benchmark on garnet ethanol; see [[wiki/answers/molly-master-migration-constraints-for-ffrefine]]"
  - "FFRefine refactor step 13a, 2026-10-15 (working tree on top of commit `68a2aae`, not yet committed): pinned Molly to master `ac3ede15856d2ac8da18cbc7325a3fa49aaa8f0f` via `Project.toml` `[sources]`; implemented and unit-tested the `FFParameterSet`/`ParameterSchema`/`atom_parameter_indices` container (`src/molly_compat.jl`, `test/parameter_container_checks.jl`, 156/156 pass); `julia +1.12 --project=. -e 'using FFRefine'` loads"
  - "FFRefine refactor step 15, 2026-10-16: found and fixed an Enzyme bug where parameter-interaction struct field layout (Bool field followed by padding/zero-size fields before Float64 parameters) combined with a never-taken type-unstable branch in Molly's with_pairwise_partition silently zeroed gradients for DoubleExponentialSoftCore, LennardJones, Mie, and AshbaughHatch weight_14 and every later interaction in the same tuple; and isolated the electrostatic lambda-path difference between Molly AWHGrads and master from the intraLJ steric-scheduler difference on ethanol hydration; see [[wiki/answers/ffrefine-step15-enzyme-struct-layout-gradient-loss]]"
scope: living
currency: current
as_of: 2026-10-16
as_of_commit:
  - FFRefine@110fe64
---

# FFRefine Decision Register

## Short answer

This register lists FFRefine's durable project decisions with a stable ID (`FFR-001`, ...), their implementation status, and the page that records the evidence and rationale. As of 2026-10-11 (FFRefine `110fe64`):

- **Canonical regime decided (FFR-029):** a damped Levenberg-Marquardt trust-region step with weighted-sum aggregation. The step and report-only direction gates exist in code since `110fe64` (FFR-020); why that change was made is not recorded.
- **Decided but not implemented (FFR-030 to FFR-040):** remove the direction gates, rescue/extension sizing, ConFIG, momentum, the natural-gradient path, loss gates in every mode, the archive KL budget, Huber loss, several report-only diagnostics, and the dead local-window replay-gradient machinery. Implementation is planned for Phase 0 of the package plan.
- **Package and migration plan decided (FFR-021 to FFR-028, FFR-041, FFR-042, FFR-045 to FFR-047):** package shell, then Molly `master` migration, then generalisation, then publication. Phase 1 migration started in code 2026-10-15 (step 13a: Molly pinned to `master`, parameter container implemented; working tree, not yet committed; see FFR-021, FFR-049).
- **Open:** QEq hardness default (FFR-043), package name (FFR-044), where system conversion lands (FFR-048), plus the questions listed under Open questions below.

Earlier decisions (FFR-001 to FFR-019) are kept with their current status, including those since superseded. Long rationale stays on the linked pages.

## Decisions

Status values: `implemented` (with commit where known), `decided, not implemented`, `open`, or `superseded by FFR-xxx`. "Plan" is the decision letter in the 2026-10-11 planning document.

| ID | Plan | Topic | Decision | Status | Decided | Rationale | Recorded in |
|---|---|---|---|---|---|---|---|
| FFR-001 | — | Windowed TSS replay | Replay a frozen windowed TSS archive locally within each active window and stitch the local estimates with the reported TSS window equations, not as one global pool with an active-window offset | present at the `a3b6aa5`/`6b20031` audits; commit not recorded; now used only by the replay/TSS parity probe (see FFR-007, FFR-040) | 2026-07-07 | Global-offset replay gave about $6\,k_BT$ replay/TSS disagreement; local replay plus stitching gave about $0.37\,k_BT$ | [[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]] |
| FFR-002 | — | Thermodynamic-cycle legs | Treat leg identifiers as configuration symbols; build the global latent vector from the union of per-leg latent names and project it into each leg by name | present at the `a3b6aa5`/`6b20031` audits; commit not recorded; the cycle prediction itself still hard-codes `solvated`/`vacuum` labels and `T0`/`P0` globals (2026-10-11 plan), to be generalised by FFR-047 | 2026-07-15 | Supports one-, two- and three-or-more-leg cycles without optimizer changes | [[wiki/concepts/awh-replay-force-field-optimization]], [[wiki/answers/ffrefine-generalist-package-plan-decisions]] |
| FFR-003 | — | Charge-parameter keys | Key charges by molecule-template identity plus local site | superseded by FFR-004 | 2026-07-15 | Repeated solvent copies share charge coordinates while distinct sites stay separate | [[wiki/concepts/awh-replay-force-field-optimization]] |
| FFR-004 | — | Charge-parameter keys | Key charges by atom type | implemented, FFRefine `d48d2f1` (2026-07-16, "Group charges by atom type"); the molecule-template key code (`molecular_template_charge_keys`) is dead code (2026-10-11 audit) | 2026-07-16 | Rationale for the switch not recorded; atom-type keys match how Molly keys σ/ϵ, which motivates FFR-041 | [[wiki/concepts/awh-replay-force-field-optimization]], [[wiki/answers/molly-master-migration-constraints-for-ffrefine]] |
| FFR-005 | — | Epoch control | Resimulate after any accepted and applied parameter change; stop without resimulation only when nothing was accepted; follow a final accepted update at the epoch limit with one simulation-only validation epoch | described in the 2026-07-18 epoch-control update; implementation state not independently recorded | 2026-07-18 | Only fresh simulation shows that accepted parameters improve the loss on newly sampled data | [[wiki/concepts/awh-replay-force-field-optimization]] |
| FFR-006 | — | Parameter bounds | Epoch-local relative trust regions (for example 5% around the current value) for bounded parameters; QEq bounds set in physical units, then converted to latent bounds | present at the `a3b6aa5`/`6b20031` audits; commit not recorded | 2026-07-22 | Keeps the optimizer local like the ESS and KL controls; avoids stale absolute boxes | [[wiki/concepts/awh-replay-force-field-optimization]] |
| FFR-007 | — | Training estimator | Window-mixture MBAR (frozen TSS windows as sampled states) for all optimization free energies, observables, gradients, candidate ESS and Fisher estimates; local-window replay only for replay/TSS parity | present at the `a3b6aa5`/`6b20031` audits; commit not recorded | 2026-07-24 | Every archived frame can contribute to every target; local replay plus stitching remains the right parity check | [[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]], [[wiki/answers/ffrefine-current-implementation-status]] |
| FFR-008 | — | Gradient aggregation | Family-level Fisher-whitened ConFIG as an opt-in aggregation; weighted sum stays the default | in code at `110fe64`; removal decided (FFR-033), not implemented | 2026-07-28 | A weighted sum can hide a rise in one family; ConFIG must work in the Fisher geometry of the step actually taken | [[wiki/answers/adding-config-optimiser-to-ffrefine]] |
| FFR-009 | — | Momentum | Chain-local post-Fisher first-moment momentum (`OptimiserSettings` default `momentum_beta = 0.5`, component-wise guard under ConFIG) | in code at `110fe64`; removal decided (FFR-034), not implemented | 2026-07-28 | Controlled first-moment smoothing inside the trust-region machinery | [[wiki/answers/adding-config-optimiser-to-ffrefine]] |
| FFR-010 | — | Process isolation | One disposable worker process per macro epoch | present at the `a3b6aa5`/`6b20031` audits; commit not recorded; confirmed as the production default by FFR-026 | 2026-07-29 | Process exit is the reliable memory-reclamation boundary | [[wiki/answers/ffrefine-current-implementation-status]] |
| FFR-011 | — | Fisher conditioning | Orient proposals with the state-conditional Fisher; control finite steps by maximum state-conditional KL and state-wise ESS; keep the joint frozen-bias Fisher as a diagnostic | present at the `a3b6aa5`/`6b20031` audits; commit not recorded; how it enters the FFR-020 trust-region step is not recorded | 2026-08-29 | The trust-region KL must match the replay conditioning ([[wiki/claims/CLM-0039-trust-region-kl-must-match-replay-conditioning]]) | [[wiki/answers/ffrefine-kl-definition-for-extended-ensemble-training]] |
| FFR-012 | — | ConFIG finite-step acceptance | Report finite-step family regressions under ConFIG in `failed_components` instead of vetoing; aggregate-loss, support and KL constraints still apply | in code at `110fe64`; removal decided (FFR-033), not implemented (implemented at `a3b6aa5`, 2026-09-23) | 2026-09-23 | ConFIG's common-descent guarantee is first-order only | [[wiki/answers/adding-config-optimiser-to-ffrefine]] |
| FFR-013 | — | ConFIG family set | Exclude families classified `:uncertain` or `:negligible` by the delete-block reliability screen from ConFIG and renormalise the remaining family weights | superseded by FFR-017 | 2026-09-24 | An unreliable included family collapsed the ConFIG step to estimated KL 0.0017 ([[wiki/claims/CLM-0044-config-must-exclude-directionally-unreliable-families]]) | [[wiki/answers/adding-config-optimiser-to-ffrefine]] |
| FFR-014 | — | Loss gates | Loss-confidence gates diagnostic by default (`loss_gate_mode=:diagnostic`), `:enforce` kept available | in code at `110fe64`; removal decided (FFR-036), not implemented | 2026-09-24 | The gate cost work on small KL-bounded steps and missed the observed over-prediction failure | [[wiki/answers/ffrefine-loss-gate-diagnostic-policy]] |
| FFR-015 | — | Loss scale after exclusion | Report losses on the full-objective scale; the step keeps renormalising weights over included families until a step-length policy is decided | present at the `6b20031` audit; commit not recorded (decided 2026-09-28, after the `a3b6aa5` audit, so not verified present there); step policy open ([[wiki/questions/QST-0013-step-length-policy-after-family-exclusion]]) | 2026-09-28 | Renormalisation changes the uncapped natural-gradient step length ([[wiki/claims/CLM-0048-family-weight-renormalisation-changes-natural-gradient-step-length]]) | [[wiki/answers/adding-config-optimiser-to-ffrefine]], [[wiki/answers/ffrefine-improved-gates-water-run-lessons]] |
| FFR-016 | — | Equilibration cut | Multi-series $N_\text{eff}$-maximising cut with a calibrated materiality threshold, report-only (stage 1), water only | present at the `6b20031` audit; commit not recorded (decided 2026-09-28, after the `a3b6aa5` audit, so not verified present there); kept as the equilibration report under FFR-030 | 2026-09-28 | Expected transient is small (about 100 ps of 50 ns); calibration prevents over-cutting ([[wiki/claims/CLM-0047-calibrated-materiality-threshold-prevents-multi-series-equilibration-over-cutting]]) | [[wiki/answers/ffrefine-multi-series-equilibration-cut-calibration]] |
| FFR-017 | — | Direction gates | Block-based, aggregation-aware direction gates decide family eligibility ($B=8$, Monte Carlo calibrated size filter for ConFIG, cross-fitted promise test, promise drift report-only by default) | superseded by FFR-020 | 2026-09-30 (authoritative in `26affa0`) | The legacy half-archive cosine gate reacted to noise and cost about 13% of wall time | [[wiki/answers/ffrefine-direction-gates-and-production-policy]], [[wiki/answers/ffrefine-improved-gates-water-run-lessons]] |
| FFR-018 | — | Production policy | Generic extend-or-exclude policy taken before the replay chain: optimise, extend once to rescue an excluded family (expected-value sizing, α-spending), or stop at the noise floor | in code at `110fe64`; removal decided (FFR-032), not implemented | 2026-09-30 (`e49cfde`) | Buy an extension only when it is expected to pay; a retest after failure needs α-spending ([[wiki/claims/CLM-0050-retesting-a-failed-gate-after-extension-needs-alpha-spending]]) | [[wiki/answers/ffrefine-direction-gates-and-production-policy]] |
| FFR-019 | — | Configuration surface | Resolve every policy field from `<PREFIX>_<GROUP>_<FIELD>` environment variables, nested config, legacy keys or defaults, and record each value and its source in the run metadata; FFR-045 excludes `ENV` reads from the future library | implemented (present at `6b20031`) | 2026-09-30 | rationale not recorded | [[wiki/answers/ffrefine-direction-gates-and-production-policy]] |
| FFR-020 | — | Optimizer step and gates | Introduce a damped Levenberg-Marquardt trust-region step, superseding the natural-gradient step as the canonical step once FFR-029 was decided; make the direction gates report-only (`gate_mode=report`) so they no longer decide family eligibility or the production decision. The natural-gradient path is still in the code at `110fe64` and its removal is decided (FFR-035); whether the trust-region step replaces it in every experiment is not recorded | implemented, FFRefine `110fe64` (2026-10-07) | 2026-10-07 | rationale not recorded | [[wiki/answers/ffrefine-current-implementation-status]] |
| FFR-021 | A | Sequencing | Package shell on `AWHGrads` (Phase 0), then migrate to Molly `master` (Phase 1), then generalise (Phase 2), then prove and publish (Phase 3) | decided; Phase 1 started in code (step 13a, 2026-10-15: Molly pinned to `master` `ac3ede15`, package loads, parameter container implemented — FFR-049; working tree, not yet committed) | 2026-10-11 | Migration changes numerics and generalisation changes structure; each needs a fixed reference | [[wiki/answers/ffrefine-generalist-package-plan-decisions]], [[wiki/answers/molly-master-migration-constraints-for-ffrefine]] |
| FFR-022 | B | Shape of Molly U1 | A generic per-sample TSS hook in Molly; FFRefine owns the archive format built from it | decided, not implemented | 2026-10-11 | Replaces porting the `AWHGrads`-only replay logger upstream as-is | [[wiki/answers/ffrefine-generalist-package-plan-decisions]] |
| FFR-023 | L | Target loggers | Attach target loggers to the FFRefine ensemble, mirroring `TSSSimulation(...; loggers)` | decided, not implemented | 2026-10-11 | Molly `master` ignores loggers on a `ThermoState`'s own system in generalized-ensemble runs | [[wiki/answers/ffrefine-generalist-package-plan-decisions]] |
| FFR-024 | F | Electrostatic λ path | Accept Molly `master`'s pair scaling (pair energy ∝ λ) instead of `AWHGrads`' per-charge scaling (∝ λ²) | decided, not implemented; magnitude confirmed in isolation 2026-10-16 (step 15: holding `intraLJ=true` fixed on both branches, the electrostatic-path difference alone is 0 at λ = 1, 0.5, 0.25, 0, and a few kJ/mol at λ = 0.75 — see [[wiki/answers/ffrefine-step15-enzyme-struct-layout-gradient-loss]]) | 2026-10-11 | rationale not recorded | [[wiki/answers/ffrefine-generalist-package-plan-decisions]], [[wiki/answers/molly-master-migration-constraints-for-ffrefine]], [[wiki/answers/ffrefine-step15-enzyme-struct-layout-gradient-loss]] |
| FFR-025 | E | Ethanol λ ladder | Keep FFRefine's own alchemical-ladder builder until Molly (via work item U6) can reproduce it | decided; the local builder remains in use | 2026-10-11 | Molly lacks the DEXP-to-λ conversion needed to reproduce the ladder | [[wiki/answers/ffrefine-generalist-package-plan-decisions]] |
| FFR-026 | P | Process isolation | Keep one subprocess per macro epoch as the production default; in-process mode only for tests and debugging | implemented (existing behaviour, FFR-010); whether one continuous process is now safe is open | 2026-10-11 | Contains inter-epoch memory leaks and unpredictable segmentation faults (suspected PME, multithreading and Enzyme interaction; not independently validated). A related but distinct PME/Enzyme/threading hazard — concurrent Enzyme gradients sharing one PME object giving silently wrong results, traced to non-thread-safe FFTW re-planning — was directly probed and confirmed 2026-10-15 (see section H in [[wiki/answers/molly-master-migration-constraints-for-ffrefine]]), without establishing that it is the same mechanism behind the leaks/segfaults | [[wiki/answers/ffrefine-generalist-package-plan-decisions]], [[wiki/answers/molly-master-migration-constraints-for-ffrefine]] |
| FFR-027 | C | Checkpoints | Breaking change: pre-package checkpoint and run formats cannot be resumed after the migration | decided, not implemented | 2026-10-11 | rationale not recorded | [[wiki/answers/ffrefine-generalist-package-plan-decisions]] |
| FFR-028 | S | Inputs | Do not track inputs in version control until the paper's experiments are fixed; tests use synthetic fixtures and Molly's bundled data | decided, not implemented | 2026-10-11 | rationale not recorded | [[wiki/answers/ffrefine-generalist-package-plan-decisions]] |
| FFR-029 | R | Canonical regime | A damped Levenberg-Marquardt trust-region step with weighted-sum aggregation is the canonical regime and the package's future default | decided; the regime exists in code at `110fe64` (FFR-020), the package default is not implemented | 2026-10-11 | Matches the water runs of 2026-10-06 to 2026-10-08; no further rationale recorded | [[wiki/answers/ffrefine-generalist-package-plan-decisions]], [[wiki/answers/ffrefine-current-implementation-status]] |
| FFR-030 | D | Diagnostics policy | Keep only diagnostics that decide something or are genuinely informative: validity checks (MBAR ESS with the ESS-retention retry, replay/TSS parity, split validation, window coverage), fresh-archive losses with block standard errors, replay calibration (predicted versus realised change per family), step-to-family angles and step efficiency, archive reachability, the equilibration report (water), memory tracking, per-target curves | decided, not implemented | 2026-10-11 | Diagnostics should be necessary (decide something) or genuinely informative | [[wiki/answers/ffrefine-generalist-package-plan-decisions]] |
| FFR-031 | D | Direction gates | Remove the direction gates entirely: block statistics, promise test, Monte Carlo calibration, family selection, exclusion | decided, not implemented | 2026-10-11 | In report mode they never exclude or block anything; they test the natural-gradient direction, not the trust-region step actually taken. Removal does not retract [[wiki/claims/CLM-0049-few-block-pseudo-value-covariance-understates-promise-null]] or [[wiki/claims/CLM-0050-retesting-a-failed-gate-after-extension-needs-alpha-spending]], which remain statistical findings about the calibration procedure; FFRefine only stops applying it | [[wiki/answers/ffrefine-generalist-package-plan-decisions]] |
| FFR-032 | D | Production decision | Remove rescue and extension sizing; the production decision becomes "extend production once if validity fails, otherwise optimise" | decided, not implemented | 2026-10-11 | Out-of-regime removal under FFR-029; no further rationale recorded | [[wiki/answers/ffrefine-generalist-package-plan-decisions]] |
| FFR-033 | D | Gradient aggregation | Remove ConFIG aggregation | decided, not implemented | 2026-10-11 | Out-of-regime removal under FFR-029; the ConFIG-versus-weighted-sum comparison is no longer pursued operationally, whatever its scientific outcome | [[wiki/answers/ffrefine-generalist-package-plan-decisions]] |
| FFR-034 | D | Momentum | Remove post-Fisher momentum | decided, not implemented | 2026-10-11 | Out-of-regime removal under FFR-029; makes moot the 6b20031-era question of whether the gates should certify the momentum step | [[wiki/answers/ffrefine-generalist-package-plan-decisions]] |
| FFR-035 | D | Natural-gradient path | Remove the natural-gradient step and its proposal path | decided, not implemented | 2026-10-11 | Out-of-regime removal under FFR-029 | [[wiki/answers/ffrefine-generalist-package-plan-decisions]] |
| FFR-036 | D | Loss gates | Remove loss gates in all modes (`:diagnostic` and `:enforce`), including the paired delete-block loss-confidence comparison and the stale-progress stop | decided, not implemented | 2026-10-11 | No loss-gate-specific rationale recorded; the wiki's loss-gate note applied the direction-gate reasoning, because the loss gate was built around the natural-gradient trust region being replaced. Does not revisit the 2026-09-24 evidence | [[wiki/answers/ffrefine-generalist-package-plan-decisions]], [[wiki/answers/ffrefine-loss-gate-diagnostic-policy]] |
| FFR-037 | D | Archive KL budget | Remove the archive Kullback-Leibler (KL) budget; the effective-sample-size (ESS)-retention retry replaces it | decided, not implemented | 2026-10-11 | rationale not recorded | [[wiki/answers/ffrefine-generalist-package-plan-decisions]] |
| FFR-038 | D | Loss function | Remove Huber loss; mean squared error only | decided, not implemented | 2026-10-11 | rationale not recorded | [[wiki/answers/ffrefine-generalist-package-plan-decisions]] |
| FFR-039 | D | Report-only diagnostics | Remove the backward replay comparison (parent parameters replayed on the new archive), the Fisher-treatment report (damped versus hard-cut comparison), the paired proposal-loss confidence interval, stale-progress tracking, and the legacy half-cosine (the early-versus-late pseudo-value cosine, computed inside the gate evaluation, so it goes with FFR-031) | decided, not implemented | 2026-10-11 | Not necessary or informative under FFR-030 | [[wiki/answers/ffrefine-generalist-package-plan-decisions]] |
| FFR-040 | D | Local-window replay | Keep local-window TSS replay only as the replay/TSS parity probe; remove its gradient, Fisher and ESS machinery | decided, not implemented | 2026-10-11 | All training uses window-mixture MBAR; that machinery is dead code, reachable only through the parity probe, which uses local weights and free energies without gradients | [[wiki/answers/ffrefine-current-implementation-status]] |
| FFR-041 | K | Per-type charges in Molly (U7) | Propose atom-type charge parameters as a separate Molly PR, starting with an investigation; FFRefine keeps local charge injection until it merges | decided, not implemented | 2026-10-11 | Atom-type charge keys (FFR-004) match Molly's σ/ϵ keying | [[wiki/answers/ffrefine-generalist-package-plan-decisions]], [[wiki/answers/molly-master-migration-constraints-for-ffrefine]] |
| FFR-042 | H | Repository hygiene | Defer until the architecture is stable; cleanup may happen here or in a new repository | decided (deferred) | 2026-10-11 | rationale not recorded | [[wiki/answers/ffrefine-generalist-package-plan-decisions]] |
| FFR-043 | Q | QEq hardness default | Keep today's behaviour for now (no gauge fixing; bounded hardness latent; regularisation per experiment); decide before Phase 2 parameter-layer work | open | 2026-10-11 | Per-type hardness is redundant with electronegativity for a fixed fit ([[wiki/answers/qeq-per-type-electronegativity-hardness-redundancy]]), but Garnet 2.0 may need a different parameterisation | [[wiki/answers/ffrefine-generalist-package-plan-decisions]] |
| FFR-044 | N | Package name | `FFRefine` is the working name; decide before Phase 3 documentation | open | 2026-10-11 | It may be too close to the unrelated `MDRefine` project | [[wiki/answers/ffrefine-generalist-package-plan-decisions]] |
| FFR-045 | — | User API | Mirror Molly: users build `System`s, `ThermoState`s and ensemble settings; one verb `refine!`; keyword-constructed structs; no `ENV` reads in the library | decided, not implemented | 2026-10-11 | Adopt Molly's own conventions instead of a custom configuration surface | [[wiki/answers/ffrefine-generalist-package-plan-decisions]] |
| FFR-046 | — | Target observables | Declare targets with ordinary Molly loggers; FFRefine re-evaluates the logger's observable function on archived frames at candidate parameters | decided, not implemented | 2026-10-11 | Needed to evaluate an observable at unsampled parameters and to differentiate it with Enzyme | [[wiki/answers/ffrefine-generalist-package-plan-decisions]] |
| FFR-047 | — | Thermodynamic cycles (Molly U5) | Add an estimator-agnostic `ThermodynamicCycle`/`Leg` abstraction to Molly (Phase 2) | decided, not implemented | 2026-10-11 | Molly has no cycle abstraction; generalises FFRefine's endpoint-only, label-bound cycle prediction | [[wiki/answers/ffrefine-generalist-package-plan-decisions]] |
| FFR-048 | — | System conversion (Molly U2) | Whether unit stripping, float-type conversion and device transfer land in Molly or stay a local FFRefine converter | open | 2026-10-11 | `master` may have dropped these helpers deliberately | [[wiki/answers/ffrefine-generalist-package-plan-decisions]] |
| FFR-049 | — | Parameter container design | FFRefine's parameter container is an immutable key schema (sorted parameter names plus a name-to-index `Dict`, shared by copy and by zero) paired with a mutable values vector; Enzyme differentiates the values vector; per-atom parameter indices are computed from atom types rather than stored; the schema is never lazily cached and the values vector is written only on copies or between parallel phases, with a private shadow per concurrent gradient | implemented, FFRefine step 13a (2026-10-15; working tree, not yet committed) as `FFParameterSet`/`ParameterSchema`/`atom_parameter_indices` in `src/molly_compat.jl`; unit-tested in `test/parameter_container_checks.jl` (156/156 pass); wired into production gradient injection in FFRefine step 14 (2026-10-15; working tree, not yet committed), which found and fixed an Enzyme bug where a non-inlined `map`-based post-injection charge rebuild silently halved the σ/ϵ gradient (see [[wiki/questions/QST-0016-enzyme-map-struct-rebuild-silently-drops-gradient]]) and established a β-precision rescaling needed to compare against `AWHGrads`-era references (see [[wiki/answers/ffrefine-step14-enzyme-gradient-injection-and-beta-precision-validation]]) | 2026-10-15 | Benchmarking on garnet ethanol (6282 atoms, DEXP+RF, 223 keys) found master's `extract_parameters`/`ParameterPlan` reads the parameter dictionary once per key and then works on a flat vector, so `Base.Dict`, a vector-backed `AbstractDict`, and a plain values vector all gave the same 178 ms gradient time and identical gradients; container choice is therefore performance-irrelevant, so the simplest design (schema plus values vector) was chosen. Replaces the `AWHGrads`-era `ParameterSet`, which existed only to avoid per-atom dictionary lookups that master's `ParameterPlan` already avoids. Implementation confirmed the design: masses are excluded (Molly injects one mass per atom type, which would undo hydrogen-mass repartitioning); the container is the union of all thermodynamic states' keys, with zero gradient at a state that does not use a given key; key order is sorted by name, not by `Dict` hash or per-state plan order, and matched by name everywhere; no custom `Molly.dict_get` method was needed. Enzyme gradients through `ParameterPlan`/`inject_gradients` matched the `Base.Dict` path to rtol $10^{-12}$ in both the `Duplicated(θ, dθ)` vector form (loss rewraps `FFParameterSet(p, θ)`) and `Duplicated(p, zero(p))`; 8 concurrent gradients against one shared container/system/plan were bit-identical to the serial results and left the shared values vector unchanged | [[wiki/answers/molly-master-migration-constraints-for-ffrefine]] |

The remaining Molly work items (U3 unit-aware parameter API, U4 parameter-prefix namespacing, U6 DEXP-to-λ conversion, and the optional U8 and M6) are listed with their phases in [[wiki/answers/ffrefine-generalist-package-plan-decisions]].

## Open questions

Open project decisions: FFR-043 (QEq hardness default), FFR-044 (package name), FFR-048 (system conversion), whether one continuous process is now safe (FFR-026), and the unrecorded rationale for FFR-020.

Open questions recorded on their own pages:

- [[wiki/questions/QST-0006-average-observable-trainability-sampling-budget]]: what sampling budget makes enthalpy or dielectric teacher signals identifiable within replay support.
- [[wiki/questions/QST-0007-checkpoint-assessment-versus-next-direction-readiness]]: separating checkpoint evaluation from direction readiness; the readiness side was implemented through the direction gates, which FFR-031 removes.
- [[wiki/questions/QST-0010-damped-fisher-config-compatibility]]: damped Fisher with ConFIG; ConFIG is decided for removal (FFR-033).
- [[wiki/questions/QST-0011-config-versus-weighted-sum-under-calibrated-direction-gates]]: no longer pursued operationally (FFR-033); the scientific comparison remains unresolved.
- [[wiki/questions/QST-0012-persistent-replay-prediction-optimism-for-one-family]]: what to do about one family's persistently optimistic replay predictions; two of its recorded candidate responses act on mechanisms decided for removal (the archive KL budget, FFR-037, and ConFIG protection, FFR-033).
- [[wiki/questions/QST-0013-step-length-policy-after-family-exclusion]]: posed for the KL-capped natural-gradient step (removal decided, FFR-035); whether it carries over to the trust-region step is not recorded.
- [[wiki/questions/QST-0014-pme-charge-gradient-enzyme-vs-finite-difference-mismatch]]: PME charge-gradient mismatch, relevant to charge training and FFR-041. Resolved 2026-10-15 for CPU, Float64, water PME on Molly master (PME must be passed `Duplicated`, not `Const`); open for independent verification on `AWHGrads`, and for GPU and hexane/ethanol PME charge gradients.
- [[wiki/questions/QST-0015-rdf-density-dielectric-pareto-front-for-this-water-parameterisation]]: whether RDF, density and dielectric genuinely trade off for this water model.
- [[wiki/questions/QST-0016-enzyme-map-struct-rebuild-silently-drops-gradient]]: why Enzyme silently halves a Lennard-Jones gradient through a non-inlined `map`-based struct rebuild; a workaround is verified but the mechanism is not understood.
- [[wiki/questions/QST-0017-enzyme-struct-field-layout-silently-drops-gradient]]: why Enzyme silently zeroes a gradient depending on interaction-struct field layout (a `Bool` field followed by padding/zero-size fields before `Float64` parameters) and a never-taken type-unstable branch; a struct-reorder workaround is verified (merged for `DoubleExponentialSoftCore`, unmerged for `LennardJones`/`Mie`/`AshbaughHatch`) but the mechanism is not understood.
- [[wiki/questions/force-field-training-validation-scope]]: what evidence would show transfer beyond the fitted observables and systems.
- [[wiki/tensions/TEN-0020-config-family-exclusion-versus-untreated-drift]]: family exclusion versus untreated drift, tied to FFR-013 and FFR-017.

## Sources used

None (no literature source). Every entry is FFRefine project evidence listed in this page's frontmatter and recorded on the linked pages.

## Wiki pages used

- [[wiki/answers/ffrefine-current-implementation-status]]
- [[wiki/answers/ffrefine-generalist-package-plan-decisions]]
- [[wiki/answers/ffrefine-direction-gates-and-production-policy]]
- [[wiki/answers/ffrefine-loss-gate-diagnostic-policy]]
- [[wiki/answers/adding-config-optimiser-to-ffrefine]]
- [[wiki/answers/ffrefine-improved-gates-water-run-lessons]]
- [[wiki/answers/ffrefine-multi-series-equilibration-cut-calibration]]
- [[wiki/answers/molly-master-migration-constraints-for-ffrefine]]
- [[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]]
- [[wiki/concepts/awh-replay-force-field-optimization]]

## Wiki updates made

- Created this register and moved post-snapshot decisions into it from the pages listed under `wiki_pages_updated`.

## Remaining gaps

- Commits are not recorded for most decisions before 2026-09-23 or for FFR-015 and FFR-016.
- Rationale is not recorded for FFR-020 and several 2026-10-11 removals; this register does not supply one.

## Changes

- 2026-10-11: register created from [[wiki/answers/ffrefine-current-implementation-status]], [[wiki/answers/ffrefine-generalist-package-plan-decisions]], [[wiki/answers/ffrefine-direction-gates-and-production-policy]], [[wiki/answers/ffrefine-loss-gate-diagnostic-policy]], [[wiki/answers/adding-config-optimiser-to-ffrefine]], [[wiki/answers/ffrefine-multi-series-equilibration-cut-calibration]], [[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]], and [[wiki/concepts/awh-replay-force-field-optimization]].
- 2026-10-12: corrected statuses of decided-but-unimplemented removals and inferred implementation rows after review.
- 2026-10-15: added FFR-049 (parameter container design: immutable key schema plus values vector) from the 2026-10-15 Molly-master probes; added a cross-reference to the confirmed PME/Enzyme thread-safety hazard in FFR-026's rationale; updated the QST-0014 open-questions blurb to reflect its 2026-10-15 resolution for CPU, Float64, water PME on master. See [[wiki/answers/molly-master-migration-constraints-for-ffrefine]].
- 2026-10-15: recorded FFRefine refactor step 13a: FFR-049 (parameter container) is now implemented and verified, not just decided; FFR-021 (migration sequencing) and the short answer's phase summary updated to reflect that Phase 1 migration started in code (Molly pinned to `master`, package loads). See the new section I in [[wiki/answers/molly-master-migration-constraints-for-ffrefine]].
- 2026-10-15: recorded FFRefine refactor step 14: FFR-049's parameter container is now wired into production gradient injection, not only unit-tested in isolation. Step 14 found and fixed an Enzyme bug in which a non-inlined `map`-based post-injection charge rebuild silently returned about half the correct σ/ϵ gradient with no error (added [[wiki/questions/QST-0016-enzyme-map-struct-rebuild-silently-drops-gradient]] for the unresolved mechanism), and established that comparing gradients/energies against `AWHGrads`-era references needs a β-precision rescaling because `ThermoState.beta` is computed at a different float precision on `master`. See [[wiki/answers/ffrefine-step14-enzyme-gradient-injection-and-beta-precision-validation]].
- 2026-10-16: recorded FFRefine refactor step 15: a second, independent Enzyme silent-gradient-loss mechanism was found and partly fixed, triggered by interaction-struct field layout (a `Bool` field followed by padding/zero-size fields before `Float64` parameters) plus a never-taken type-unstable branch in Molly's `with_pairwise_partition` (added [[wiki/questions/QST-0017-enzyme-struct-field-layout-silently-drops-gradient]] for the unresolved mechanism; the `DoubleExponentialSoftCore` field-reorder fix is merged into Molly master, the `LennardJones`/`Mie`/`AshbaughHatch` fix is on an unmerged branch); and FFR-024's electrostatic λ-path difference was isolated from the `intraLJ` steric-scheduler difference and confirmed on ethanol hydration. See [[wiki/answers/ffrefine-step15-enzyme-struct-layout-gradient-loss]].
