---
type: concept
status: active
created: 2026-06-30
updated: 2026-10-12
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/adaptive-sampling
  - research/molecular-simulation/free-energy
tags:
  - awh
  - replay-reweighting
  - natural-gradient
  - force-field-optimization
related:
  - "[[wiki/answers/ffrefine-direction-gates-and-production-policy]]"
  - "[[wiki/answers/ffrefine-config-vs-weighted-sum-water-campaign-results]]"
  - "[[wiki/concepts/accelerated-weight-histogram-method]]"
  - "[[wiki/concepts/free-energy-reweighting-for-force-field-fine-tuning]]"
  - "[[wiki/concepts/times-square-sampling]]"
  - "[[wiki/concepts/multistate-bennett-acceptance-ratio]]"
  - "[[wiki/concepts/tolerance-normalized-multi-observable-losses]]"
  - "[[wiki/answers/ffrefine-current-implementation-status]]"
  - "[[wiki/answers/ffrefine-paper-methods-knowledge-base]]"
  - "[[wiki/answers/ffrefine-kl-definition-for-extended-ensemble-training]]"
  - "[[wiki/answers/adding-config-optimiser-to-ffrefine]]"
  - "[[wiki/answers/ffrefine-loss-gate-diagnostic-policy]]"
  - "[[wiki/claims/CLM-0044-config-must-exclude-directionally-unreliable-families]]"
  - "[[wiki/tensions/TEN-0020-config-family-exclusion-versus-untreated-drift]]"
  - "[[wiki/answers/molly-master-migration-constraints-for-ffrefine]]"
  - "[[wiki/answers/qeq-per-type-electronegativity-hardness-redundancy]]"
  - "[[wiki/sources/SRC-0098-graph-nets-partial-charge-prediction]]"
  - "[[wiki/answers/ffrefine-generalist-package-plan-decisions]]"
  - "[[wiki/answers/ffrefine-decision-register]]"
sources:
  - SRC-0005
  - SRC-0006
  - SRC-0018
  - SRC-0023
  - SRC-0025
  - SRC-0026
  - SRC-0036
  - SRC-0098
sensitivity: public
encryption: none
scope: timeless
---

# AWH Replay Force Field Optimization

## Summary

AWH replay force-field optimization uses adaptive AWH to obtain a broad reference ensemble, freezes the bias, and performs offline replay reweighting to optimize force-field parameters against free-energy and observable targets. [SRC-0018]

The reusable idea is broader than AWH: the optimizer needs a fixed, supported reference ensemble plus a way to evaluate target-state replay weights, gradients, ESS diagnostics, and a Fisher/KL trust-region step. AWH supplies one such reference ensemble; TSS could supply another if its adaptive estimates are frozen before production, while MBAR can supply a fixed-sample reference-mixture estimator when samples from known states are already available. This is an implementation inference from SRC-0018's sampler/optimizer separation, TSS's extended-ensemble structure, and MBAR's fixed-sample estimator structure. [SRC-0018] [SRC-0005] [SRC-0006] [SRC-0023]

## Key Points

- The optimizer treats AWH as a data-generation mechanism, not as a differentiable online update rule. [SRC-0018]
- Frozen-bias replay estimates endpoint free energies and gradients for candidate parameter sets. [SRC-0018]
- The same replay machinery can estimate general state observables and their gradients. [SRC-0018]
- A latent-space empirical Fisher matrix provides the local metric for natural-gradient-like steps. [SRC-0018]
- KL-target scaling and ESS checks limit proposed updates to regions still supported by the frozen reference ensemble. [SRC-0018]
- When the enhanced-sampling state marginal is prescribed and expected to readapt, proposal geometry should use state-wise centered conditional Fishers; the frozen-bias joint Fisher should be retained separately as a state-occupancy and bias-portability diagnostic. This is an FFRefine design recommendation; its prospective evidence is limited to dielectric-only reaction-field training. [[wiki/answers/ffrefine-kl-definition-for-extended-ensemble-training]] [[wiki/claims/CLM-0040-damped-conditional-fisher-dielectric-training-survives-fresh-resimulation]]
- A sampler-agnostic implementation should isolate the reference-ensemble adapter from the replay estimator and optimizer, so AWH, TSS, or MBAR-style archives can be compared under the same target losses and support gates. [SRC-0018] [SRC-0005] [SRC-0006] [SRC-0023]

## Core equations

Endpoint replay gradient:

$$
\nabla_{\theta} \tilde F_m(\theta)
=
\beta^{-1}\sum_n
w_m^{\mathrm{rep}}(n;\theta)
\nabla_{\theta}u(x_n,m;\theta).
$$

[SRC-0018]

Fisher/KL step geometry:

$$
D_{\mathrm{KL}}(p_{\phi}\Vert p_{\phi+\Delta\phi})
\approx
\frac{1}{2}\Delta\phi^{\top}I(\phi)\Delta\phi.
$$

[SRC-0018]

## Implementation consequences

Training can mix free-energy-cycle targets and observable targets because the loss is assembled after replay and normalized by target tolerances. [SRC-0018]

For target families with different cardinalities, tolerance normalization should be paired with a family-level weighted mean so the number of scalar bins does not silently determine scientific priority. Within-family weights and between-family coefficients have distinct meanings; see [[wiki/concepts/tolerance-normalized-multi-observable-losses]].

For a generalized implementation, the common interface should export stored frames, visited states or windows, reference reduced potentials, a log reference-mixture denominator, target-state energy evaluations, target-state gradients, candidate-ensemble weights for ESS, and split or parity diagnostics. The method-specific part is how that reference denominator is obtained: frozen AWH uses a frozen Gibbs mixture, TSS needs the exact frozen simulated-tempering or windowed denominator, and MBAR uses the sampled-state mixture implied by cross-evaluated reduced potentials and state counts. [SRC-0018] [SRC-0005] [SRC-0006] [SRC-0023]

The numbered lessons below come from FFRefine project work; when each was observed is listed in the Evidence timeline. Other wiki pages refer to them by number.

**Lesson 1: windowed TSS replay must stay local to the active window.** Treating all windowed frames as one global replay pool with an active-window offset produced multi-$k_BT$ replay/TSS disagreement in an FFRefine scaffold test. Computing local replay weights and local free-energy or observable estimates per active window, then stitching those local estimates with the reported TSS window probabilities, offsets, and global rung density, restored replay/TSS agreement to sub-$k_BT$ scale for the ethanol-solvation scaffold. This is an implementation lesson grounded in SRC-0006's window-stitching equations, not a new literature claim. [SRC-0006]

**Lesson 2: replay/TSS parity should be a decision with uncertainty, not a bare maximum-discrepancy threshold.** A solvated production archive that missed a $1.0\,k_BT$ threshold by about $0.036\,k_BT$ after the parity probe had already passed is better treated as statistically inconclusive than as a definitive sampler failure. A robust policy should estimate replay/TSS uncertainty from delete-block or split-half diagnostics, accept only when an upper confidence bound is within tolerance, reject only when a lower confidence bound exceeds tolerance, and otherwise extend the affected frozen-production leg. If the affected leg exhausts frozen extensions or shows a clear parity failure, retry adaptive sampling for that leg while retaining valid production archives for other legs. This is a project implementation lesson about validation policy for SRC-0018-style frozen-reference replay and TSS readiness, not a new literature claim. [SRC-0018] [SRC-0005] [SRC-0006]

**Lesson 3: thermodynamic-cycle optimization should not bake in labels such as solvent or vacuum.** The theory in SRC-0018 indexes replay estimates by a generic leg, and implementation should mirror that by treating leg identifiers as configuration-level symbols, assembling a global latent parameter coordinate system from the union of per-leg latent names, and projecting that global vector into each leg by name. This supports one-leg targets, two-leg hydration cycles, and future three-or-more-leg cycles without changing the optimizer. Parameters absent from a leg should contribute zero gradients and Fisher entries for that leg, while shared parameter names remain coupled across all legs. This is an FFRefine implementation lesson grounded in SRC-0018's coefficient-weighted thermodynamic-cycle formulation, not a new literature claim. [SRC-0018]

**Lesson 4: the replay-gradient basis must encode chemical parameter equivalence independently of particle-instance count.** In solvated systems with many repeated solvent molecules, a force-field parameter coordinate should represent a reusable chemical parameter, not an individual atom instance, unless the model intentionally assigns molecule-specific parameters. Atomic charge extraction is especially easy to get wrong because per-particle charge fields can create one derivative slot per atom. Two groupings achieve the sharing. Topology-aware keys built from molecule-template identity and local site identity let repeated copies of the same molecule share charge coordinates while distinct sites within a molecule remain separate; for the ethanol-in-water FFRefine case, this reduced the solvated active physical basis from thousands of per-atom charge slots to 22 shared physical parameters, with 12 shared charge sites and 24 QEq/LJ latent coordinates. Atom-type keys achieve the same sharing by a coarser grouping, and match the way Molly.jl already keys its own σ/ϵ parameters by atom type. Which grouping FFRefine uses is project state, recorded as FFR-003 and FFR-004 in [[wiki/answers/ffrefine-decision-register]]. This is a project implementation lesson about constructing the parameter basis for SRC-0018-style replay optimization, not a new literature claim. [SRC-0018]

**Lesson 5: replay acceptance is not the same as validated improvement.** If a replay optimizer accepts and applies any parameter change, the next macro epoch should resimulate with those parameters even when the optimizer also reports local convergence, Fisher degeneracy, split disagreement, or inability to find a further improving replay step. The fresh simulation is the only check that the accepted parameters improve the loss under newly sampled data rather than only under the old frozen archive. If no proposal is accepted or applied, the pipeline can stop without resimulation; if ESS collapse occurs, the candidate still becomes the resimulation target because the archive no longer supports replay validation. A final accepted update at the configured optimization-epoch limit should therefore be followed by one simulation-only validation epoch, without allowing another optimizer step. This is a project control-flow lesson for SRC-0018-style frozen-reference replay optimization, not a new literature claim. [SRC-0018]

**Lesson 6: bounded force-field training parameters are better treated as epoch-local relative trust regions than as fixed absolute intervals.** A relative radius such as 5% should be evaluated around the current physical value at the start of each macro epoch, so a parameter that moved from 1.0 to 1.2 is next allowed within 1.2 plus or minus 5%, assuming the previous replay step was accepted and resimulated. For descriptor-based QEq parameters, the trust region should be expressed first in physical electronegativity or hardness units, then converted to the latent coefficient bounds used by the optimizer; if several descriptors share one feature coefficient, the converted intervals should be intersected. This keeps the optimizer local in the same sense as ESS and Fisher/KL controls, while avoiding stale absolute boxes that either overconstrain later epochs or silently allow large relative moves for small parameters. This is a project implementation lesson for SRC-0018-style local replay optimization, not a new literature claim. [SRC-0018]

**Lesson 7: compressed charge descriptors must preserve physical site multiplicity.** When chemically equivalent sites are compressed into one shared charge descriptor, charge-equilibration solves and Jacobians must still preserve physical site multiplicity. The molecular net-charge constraint counts repeated sites, but the quadratic QEq objective also counts them; otherwise the compressed model gives the constraint the right multiplicity while giving the electronegativity and hardness terms the wrong weight. For water with shared H and O descriptors, the per-site diagonal QEq solve gives $q_H=(\chi_O-\chi_H+\eta_O Q)/(2\eta_O+\eta_H)$, not the unweighted compressed expression with $\eta_H+4\eta_O$ in the denominator. The practical validation pattern is to compare the compressed implementation against an expanded-site KKT oracle that includes equality constraints for shared descriptors, then check the latent Jacobian against finite differences. This is a project implementation lesson about topology-aware compressed parameterization for SRC-0018-style replay optimization, not a new literature claim. [SRC-0018]

**Lesson 8: a disposable worker process per macro epoch is the robust memory-reclamation boundary.** In a Julia replay-optimization loop, ordinary object reuse and explicit garbage collection may reduce per-epoch allocation without returning the resident set to the operating system after a large optimization phase. For memory-heavy macro epochs that combine PME workspaces, threaded replay, automatic differentiation, FFT/native library state, and candidate optimization, the robust reclamation boundary is a disposable worker process per macro epoch. The supervisor should pass only compact serialized epoch requests and responses, wait for worker exit before deserializing the result or starting resimulation, and record both child memory telemetry and supervisor RSS after exit. This is a project operational lesson for long SRC-0018-style replay/resimulation loops, not a new scientific claim. [SRC-0018]

**Lesson 9: multi-objective aggregation and acceptance gating** (two parts, from one multi-family water run).

First, when multiple target families are combined through ConFIG-style Fisher-whitened gradient aggregation, every family that participates gets equal angular weight in the shared descent direction regardless of how reliable its estimated direction is, because the construction normalizes each included family's whitened gradient to unit norm. [SRC-0036] A family whose treated direction is directionally unreliable, as estimated from delete-block reliability rather than from a small raw gradient norm or a low pairwise cosine alone, can therefore collapse the aggregate step by orders of magnitude if it stays active while the other families disagree with it. In the observed run, a near-stationary density family with collapsing raw gradient norm and unstable delete-block reliability stayed active and shrank the aggregate step to an estimated KL of 0.0017; a synthetic unit test reproduced the mechanism directly, with a three-family step more than 100x smaller than the corresponding two-family step. Excluding `:uncertain` and `:negligible` families from the aggregation and renormalizing the remaining family weights, while keeping excluded families in monitoring, support, and KL accounting, trades aggregate-step integrity against the risk that an excluded, marginally-resolved, high-loss family receives no training signal for the epochs it is excluded; FFRefine adopted this response (FFR-013 in [[wiki/answers/ffrefine-decision-register]]). This is a project implementation lesson and finding, not a claim evaluated in SRC-0036. [[wiki/answers/adding-config-optimiser-to-ffrefine]] [[wiki/claims/CLM-0044-config-must-exclude-directionally-unreliable-families]] [[wiki/tensions/TEN-0020-config-family-exclusion-versus-untreated-drift]]

Second, in the same run, KL and ESS trust-region bounds were what actually limited replay steps: fresh loss fell monotonically across five macro epochs, and a point-loss veto and stale-progress stop never fired. A paired delete-block loss-confidence acceptance gate fired only on already-small, well-supported steps, truncating one chain and forcing an unneeded production extension, while it passed every step of a chain whose replay prediction later over-predicted the fresh-archive improvement for one family. Under a KL/ESS-bounded architecture, loss-based acceptance gates are therefore better treated as diagnostics, relying on the KL/ESS bounds plus a loud post hoc warning on significant fresh-loss regression; FFRefine made them diagnostic by default while retaining an enforcing mode (FFR-014), and later decided to remove them entirely (FFR-036). This is FFRefine's project-specific policy given its KL/ESS-bounded architecture and this run's evidence; it is not a claim that loss-based step rejection is unhelpful in general, and it does not reproduce or contradict ForceBalance's noise-based Levenberg-Marquardt step rejection. [SRC-0018] [SRC-0025] [SRC-0026] [[wiki/answers/ffrefine-loss-gate-diagnostic-policy]]

**Lesson 10: decide which target families a replay step may use with an out-of-sample test of the step the optimiser will actually take.** Direction readiness is better decided this way than by a fixed angle threshold between archive halves. One such test cross-fits the aggregated step over jackknife time blocks and asks whether it still decreases each held-out block's loss with confidence, with Monte Carlo calibrated multipliers; FFRefine used it to decide family eligibility from 2026-09-30 (FFR-017 in [[wiki/answers/ffrefine-decision-register]]). A failed test cannot distinguish "no descent" from "not enough data", and every fresh macro-epoch archive restarts the evidence, so the only way to accumulate evidence at fixed parameters is to extend the current archive; such a retest after failure is optional stopping and needs an α-spending correction. These are project lessons, not results from SRC-0018. See [[wiki/answers/ffrefine-direction-gates-and-production-policy]], [[wiki/claims/CLM-0049-few-block-pseudo-value-covariance-understates-promise-null]] and [[wiki/claims/CLM-0050-retesting-a-failed-gate-after-extension-needs-alpha-spending]].

**Lesson 11: replay archives are tied to the backend's exact alchemical Hamiltonian.** TSS replay archives, free-energy seeds, and serialized alchemical states are tied to the exact alchemical Hamiltonian definition of the Molly version that produced them, not only to the physical force field and λ schedule. On an ethanol-in-water probe, the Molly.jl `AWHGrads` branch and `master` agreed on free-energy endpoints but disagreed at intermediate λ, because `AWHGrads` scales each solute charge (pair energy $\propto\lambda^2$) while master scales the pair energy directly (pair energy $\propto\lambda$), because master's default `intraLJ=false` annihilates rather than decouples solute-solute sterics, and because `AWHGrads`' zero-shortcut makes intra-solute sterics discontinuous exactly at λ = 0 while master is continuous; alchemical role indices were also renumbered between the two branches. The practical consequence is that energy parity on fixed coordinates and over the full λ grid, not only at the endpoints, should be checked before reusing an archive, seed, or serialized state across a sampler or backend version change, even when the underlying free-energy theory is unchanged. This is a project implementation lesson from diffs and probes against FFRefine's own force-field files, not a new literature claim. [[wiki/answers/molly-master-migration-constraints-for-ffrefine]]

**Lesson 12: per-type QEq hardness is redundant with electronegativity for a fixed fitting problem.** This is a durable scientific/mathematical result rather than a code-level finding: when electronegativity and hardness coefficients are shared per atom type (looked up) instead of predicted per atom by a graph net, hardness is redundant with electronegativity for any single fixed fitting problem. For any feasible charge vector $\mathbf q^*$, setting electronegativity $\mathbf e=-\mathbf q^*$, hardness $\mathbf h=\mathbf 1$, and zero Lagrange multipliers reaches $\mathbf q^*$ exactly and uniquely, so the $(\mathbf e,\mathbf h)\to\mathbf q$ Jacobian has rank $p-r$ ($p$ shared charge parameters, $r$ independent net-charge constraints) with every hardness column exactly $q_k$ times the corresponding electronegativity column; a per-type QEq Fisher or Gauss-Newton block is therefore structurally singular, not merely ill-conditioned, along the hardness directions and a uniform electronegativity shift. Hardness only becomes a meaningful, non-gauge direction once shared coefficients are expected to transfer to molecules with a different net-charge constraint structure than the one used to fit them -- which is why hardness is trainable in Espaloma's per-atom, supervised, many-molecule setting but is pure gauge within a replay-reweighting fit to a small, fixed set of training species. This result traces the QEq functional form to [[wiki/sources/SRC-0098-graph-nets-partial-charge-prediction]] (Wang et al. 2019) and Gilson et al. 2003, and is derived in full in [[wiki/answers/qeq-per-type-electronegativity-hardness-redundancy]].

**Lesson 13: a report-only diagnostic must evaluate the same step or rule the optimiser actually takes, or it is uninformative.** FFRefine's direction gates, once made report-only, tested the natural-gradient direction; at `110fe64` the optimiser introduced a damped Levenberg-Marquardt trust-region step, which on 2026-10-11 became the canonical regime, superseding the natural-gradient step as the canonical step (the natural-gradient path is still in the code at `110fe64` and is decided for removal, FFR-035; whether the trust-region step replaces it in every experiment is not recorded). So even as diagnostics the gates could describe a step not actually taken, independent of whether the gates' own statistics were well calibrated; in report mode they also never excluded or blocked anything. The 2026-10-11 planning document gives these two reasons for removing the gates (FFR-031 in [[wiki/answers/ffrefine-decision-register]]); the general statement is the wiki's generalisation from them, and applies beyond FFRefine's specific gates. [[wiki/answers/ffrefine-generalist-package-plan-decisions]]

## Caveats

The method is only as good as the support of the frozen ensemble; failed replay/AWH parity or low ESS indicates that new sampling is needed before trusting an update. [SRC-0018]

TSS and MBAR variants need their own readiness and support diagnostics. TSS readiness should include adaptive-profile uncertainty, replay/TSS parity intervals, coverage checks, split-half disagreement, and ESS, with recovery actions targeted to the leg that failed when the diagnostic is leg-local. TSS's variance comparison with MBAR is scoped to the paper's assumptions and should not be treated as a general guarantee for force-field parameter optimization, while MBAR does not provide adaptive sample allocation by itself. [SRC-0005] [SRC-0006] [SRC-0023]

## Evidence timeline

- 2026-07-07: an FFRefine ethanol-solvation scaffold test showed the multi-$k_BT$ failure of global-offset windowed replay and its repair by local replay plus stitching (lesson 1). [[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]]
- 2026-07-13: an FFRefine validation update, prompted by a solvated archive missing the parity threshold by about $0.036\,k_BT$, gave lesson 2.
- 2026-07-15: an FFRefine parameter-training refactor gave lesson 3, and a shared-parameter update introduced molecule-template charge keys (lesson 4, ethanol-in-water basis numbers).
- 2026-07-16: FFRefine commit `d48d2f1` ("Group charges by atom type") switched production to atom-type charge keys; the molecule-template key code (`molecular_template_charge_keys`) became dead, unreachable code, as confirmed by a 2026-10-11 audit. [[wiki/answers/molly-master-migration-constraints-for-ffrefine]] [[wiki/answers/ffrefine-decision-register]]
- 2026-07-18: an FFRefine epoch-control update gave lesson 5.
- 2026-07-22: an FFRefine parameter-bounds update gave lesson 6.
- 2026-07-24: an FFRefine QEq validation update gave lesson 7.
- 2026-07-29: an FFRefine code audit described the implementation as a project-local replay-optimization framework, not a production-validated force-field fitting package. The code had a sampler-agnostic backend that consumed completed named TSS simulations, a local TSS replay parity path, a window-mixture MBAR optimization path, QEq and bounded latent parameter maps, multi-leg target assembly, split validation, ESS/Fisher gates, ConFIG aggregation, post-Fisher momentum, and history/reporting. Its concrete experiment surfaces were ethanol solvation and water-temperature fitting. Ethanol trained solvation free energy by default, with density defined but disabled; water trained density and RDF targets, while dielectric support code existed but was disabled in the active target set and split validation. Focused tests supported implementation details, but full production improvement and transferability claims remained unvalidated. The later state is in [[wiki/answers/ffrefine-current-implementation-status]]; see also [[wiki/answers/ffrefine-paper-methods-knowledge-base]].
- 2026-07-29: an FFRefine water-temperature memory update gave lesson 8.
- 2026-08-29: an FFRefine conditioning analysis recommended state-wise centered conditional Fishers for proposal geometry; at that date the recommendation had not been prospectively tested. [[wiki/answers/ffrefine-kl-definition-for-extended-ensemble-training]]
- 2026-09-02 to 2026-09-03: prospective dielectric-only reaction-field campaigns gave the first fresh-resimulation evidence for the damped state-conditional Fisher protocol. [[wiki/claims/CLM-0040-damped-conditional-fisher-dielectric-training-survives-fresh-resimulation]]
- 2026-09-24: an FFRefine multi-family water run gave lesson 9. [[wiki/answers/adding-config-optimiser-to-ffrefine]] [[wiki/answers/ffrefine-loss-gate-diagnostic-policy]]
- 2026-10-01: an audit of FFRefine master `6b20031` recorded the cross-fitted direction gates deciding since 2026-09-30, giving lesson 10. [[wiki/answers/ffrefine-direction-gates-and-production-policy]]
- 2026-10-02: an FFRefine investigation into migrating the Molly.jl backend from `AWHGrads` to `master` gave lesson 11. [[wiki/answers/molly-master-migration-constraints-for-ffrefine]]
- 2026-10-07: a review of QEq's literature origin gave lesson 12. [[wiki/answers/qeq-per-type-electronegativity-hardness-redundancy]]
- 2026-10-11: the FFRefine package-planning session gave the reasons behind lesson 13 and, because atom-type charge keys match Molly's σ/ϵ keying, proposed adding per-atom-type charge parameters to Molly itself as a separate pull request (work item U7). [[wiki/answers/ffrefine-generalist-package-plan-decisions]] [[wiki/answers/ffrefine-decision-register]]

## Links

- [[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]
- [[wiki/concepts/accelerated-weight-histogram-method]]
- [[wiki/concepts/free-energy-reweighting-for-force-field-fine-tuning]]
- [[wiki/concepts/times-square-sampling]]
- [[wiki/concepts/multistate-bennett-acceptance-ratio]]
- [[wiki/concepts/tolerance-normalized-multi-observable-losses]]
- [[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]]
- [[wiki/answers/ffrefine-paper-methods-knowledge-base]]
- [[wiki/answers/adding-config-optimiser-to-ffrefine]]
- [[wiki/answers/ffrefine-loss-gate-diagnostic-policy]]
- [[wiki/claims/CLM-0044-config-must-exclude-directionally-unreliable-families]]
- [[wiki/tensions/TEN-0020-config-family-exclusion-versus-untreated-drift]]
- [[wiki/answers/ffrefine-direction-gates-and-production-policy]]
- [[wiki/answers/molly-master-migration-constraints-for-ffrefine]]
- [[wiki/answers/ffrefine-config-vs-weighted-sum-water-campaign-results]]
- [[wiki/answers/qeq-per-type-electronegativity-hardness-redundancy]]
- [[wiki/sources/SRC-0098-graph-nets-partial-charge-prediction]]
- [[wiki/answers/ffrefine-generalist-package-plan-decisions]]
- [[wiki/answers/ffrefine-decision-register]]
