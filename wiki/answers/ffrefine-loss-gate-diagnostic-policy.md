---
type: answer
status: active
created: 2026-09-24
updated: 2026-10-11
question: "Should paired loss-confidence acceptance gates block FFRefine's KL/ESS-bounded replay proposals, or serve only as diagnostics?"
answer_status: answered
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/molecular-simulation/free-energy
  - research/scientific-computing
tags:
  - ffrefine
  - loss-gate
  - trust-region
  - replay-reweighting
  - kl-conditioning
  - validation-policy
related:
  - "[[wiki/answers/ffrefine-direction-gates-and-production-policy]]"
  - "[[wiki/answers/adding-config-optimiser-to-ffrefine]]"
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
  - "[[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]"
  - "[[wiki/questions/QST-0007-checkpoint-assessment-versus-next-direction-readiness]]"
  - "[[wiki/concepts/forcebalance]]"
  - "[[wiki/answers/ffrefine-generalist-package-plan-decisions]]"
sources:
  - SRC-0018
  - SRC-0025
  - SRC-0026
sensitivity: public
encryption: none
wiki_pages_used:
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
  - "[[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]"
  - "[[wiki/concepts/forcebalance]]"
raw_sources_consulted: []
wiki_pages_updated:
  - "[[wiki/answers/ffrefine-loss-gate-diagnostic-policy]]"
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
  - "[[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]"
  - "[[wiki/index]]"
  - "[[wiki/log]]"
project_evidence:
  - "FFRefine run water_rdf-dens-diel_aggressive, epochs 1-5, observed 2026-09-24: fresh loss 10.02, 7.74, 7.19, 5.96, 5.49; four of six replay chains ended at the ESS-retention support boundary after cumulative KL 0.29-0.38 against a 2.0 budget; point-loss veto and stale-progress stop never fired; paired delete-block loss-confidence gate fired only on small steps (KL 0.075 and 0.0017), truncating one chain despite a 0.47 fresh-loss decrease and forcing a production extension; the same gate passed every step in a chain whose replay predictions later over-predicted fresh improvement (predicted -1.89 vs fresh -0.55 overall; dielectric predicted 3.47 vs fresh 4.73)"
---

# Should Loss-Confidence Gates Block FFRefine's Replay Proposals?

## Short answer

No, not by default. FFRefine's KL/ESS trust-region bounds are what actually limited replay steps in the inspected run; the point-loss veto and stale-progress stop never fired, and the paired delete-block loss-confidence gate intervened only on already-small, KL-bounded steps, truncating one chain that would otherwise have kept improving and forcing an unnecessary production extension. Meanwhile the gate passed every step of the chain that produced the run's actual failure: a chain whose replay prediction substantially over-estimated the fresh-archive improvement for one family. Loss-based acceptance gates therefore cost work without guarding against the risk that was actually observed, so FFRefine now treats them as diagnostic by default (`loss_gate_mode=:diagnostic`), while keeping an `:enforce` mode available and warning loudly on a significant fresh-loss regression.

This is FFRefine's own policy choice for its specific KL/ESS-bounded replay trust region, evidenced by one multi-family run. It is not a reproduction of, or a disagreement with, ForceBalance's noise-based step rejection, which is built around a different optimizer architecture. See [[wiki/concepts/forcebalance]].

## Detailed answer

### What limited the run in practice

In run `water_rdf-dens-diel_aggressive`, fresh loss fell monotonically across five macro epochs: 10.02, 7.74, 7.19, 5.96, 5.49. Across the epoch's replay chains, four of six ended at the ESS-retention support boundary after accumulating roughly 0.29 to 0.38 cumulative KL against a 2.0 nominal budget. The point-loss veto and the stale-progress stop never fired during the run. This is consistent with the general SRC-0018 picture in which a frozen-reference replay proposal is bounded by support (ESS) and by the KL trust region around the frozen archive, not by an independent scalar loss check. [SRC-0018]

### Where the paired loss-confidence gate actually intervened

FFRefine's paired delete-block loss-confidence gate compares candidate and parent replay loss with an uncertainty estimate before accepting a step. In this run it fired twice, and both times on small steps: KL 0.075 and KL 0.0017. In the KL-0.0017 case the truncated chain still had a fresh loss decrease of 0.47 remaining, and the truncation forced a production extension that would not otherwise have been needed. The gate was therefore costing simulation time on steps that were already small and well inside the KL/ESS trust region, not on steps large enough to plausibly be unreliable.

### Where the gate did not intervene

The run's actual failure mode passed the paired loss-confidence gate on every step: a chain over-predicted its own fresh-archive improvement. Predicted change was -1.89 against a fresh change of -0.55 overall, and predicted dielectric was 3.47 against a fresh value of 4.73. A gate built around paired loss confidence at the replay-archive level did not detect this discrepancy, because the discrepancy only appears once fresh resimulation is available; it is not visible from the frozen archive the gate evaluates against.

### Conclusion drawn and adopted policy

Given this evidence, ESS and KL bounds are the effective safety mechanism for step size and support in FFRefine's replay trust region, while the paired loss-confidence gate adds cost (truncated chains, forced extensions) without guarding against the observed risk (archive-to-fresh over-prediction). FFRefine's default is therefore `loss_gate_mode=:diagnostic`: the paired loss-confidence comparison is still computed and recorded for every proposal, but it does not by itself truncate a chain or reject a candidate. `:enforce` mode is retained for cases where a stricter policy is wanted. The pipeline still warns loudly when fresh loss shows a significant regression after an accepted, resimulated update, which is the check that actually caught the over-prediction failure in this run, after the fact, rather than pre-emptively.

### Caveat: this is not a claim about ForceBalance

ForceBalance's TIP3P-FB supporting information describes a Levenberg-Marquardt trust-region optimizer that rejects a proposed step when noise makes the objective increase, then extends sampling and retries. [SRC-0025] [SRC-0026] That is a real precedent for loss-based step rejection in force-field fitting, and it is not contradicted by this finding. FFRefine's architecture differs in a way that matters here: its trust region is already defined by an explicit KL divergence and ESS support bound against a frozen reference archive, evaluated before any loss-based check, whereas ForceBalance's Levenberg-Marquardt step size is itself adapted using the noisy objective outcome. The evidence above supports making loss confidence diagnostic *given FFRefine's KL/ESS-bounded architecture and this one run's observed failure mode*; it is not evidence that loss-based step rejection is unhelpful in general, or that ForceBalance's approach is inferior for its own optimizer design.

## Key equations

FFRefine's trust region follows the same KL geometry as the rest of the AWH replay route:

$$
D_{\mathrm{KL}}(p_{\phi}\Vert p_{\phi+\Delta\phi})
\approx
\frac{1}{2}\Delta\phi^{\top}I(\phi)\Delta\phi.
$$

[SRC-0018]

No new equation is introduced by the loss-gate policy; it is an acceptance-logic change, not a change to the replay estimator or Fisher geometry.

## Sources used

- SRC-0018 for the frozen-reference replay/KL/ESS trust-region framework that the loss gate sits alongside.
- SRC-0025 and SRC-0026 for ForceBalance's Levenberg-Marquardt noisy-step rejection, cited only as a contrasting precedent, not as evidence for FFRefine's specific policy.

## Wiki pages used

- [[wiki/concepts/awh-replay-force-field-optimization]]
- [[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]
- [[wiki/concepts/forcebalance]]

## Wiki updates made

- Added this answer note.
- Updated [[wiki/concepts/awh-replay-force-field-optimization]] with a ninth implementation lesson summarizing this finding and the ConFIG family-exclusion finding.
- Updated [[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]'s related links to point to this note; its evidence chronology was read but not rewritten.
- Updated [[wiki/index]] and [[wiki/log]].
- **2026-10-11:** added the status-update section below and linked [[wiki/answers/ffrefine-generalist-package-plan-decisions]].

## Status (2026-10-01)

Still current at FFRefine master `6b20031`: `loss_gate_mode` defaults to `:diagnostic`. Under `:enforce`, the loss gate is now the first rule of the generic production policy; because the production decision is taken before the replay chain, the enforced rule is re-applied after the chain (a rejected proposal stops the epoch; an inconclusive, blocked proposal extends production once while extensions remain). See [[wiki/answers/ffrefine-direction-gates-and-production-policy]].

## Status update (2026-10-11): loss gates decided for removal in every mode

FFRefine's 2026-10-11 package-planning document declares a damped Levenberg-Marquardt trust-region step with weighted-sum aggregation the project's canonical regime, and decides (not yet implemented in code as of 2026-10-11) to remove loss gates **in all modes** — both `:diagnostic` and `:enforce` — including the paired delete-block loss-confidence comparison and the stale-progress stop. This is a broader removal than the 2026-10-01 status above, which only recorded `:diagnostic` as the default while keeping `:enforce` available; `:enforce` itself is now also planned for removal, not merely de-emphasised. The reasoning recorded for the direction gates generally — that a diagnostic is only useful if it evaluates the step the optimiser actually takes — applies here too, since the loss gate was built around the KL/ESS-bounded natural-gradient replay trust region this page describes, which is itself being replaced. See [[wiki/answers/ffrefine-generalist-package-plan-decisions]] and [[wiki/answers/ffrefine-current-implementation-status]] for the full removal list.

This status update does not revisit this page's own evidence or conclusion (that the loss gate cost work without guarding against the observed failure mode); it only records that FFRefine's production policy is moving away from loss-based acceptance gating entirely, rather than continuing to keep `:enforce` as an available but unused option.

## Remaining gaps

- Evidenced by one multi-family water run; no campaign has compared `:diagnostic` against `:enforce` loss-gate modes under matched conditions.
- The fresh-loss regression warning is a post hoc check on an already-accepted, already-resimulated update; it does not prevent a bad step from being taken, only from being trusted silently afterward.
- Whether a different paired-confidence design (for example, one that also uses a prior chain's archive-to-fresh gap as a calibration signal) would catch the observed over-prediction failure pre-emptively is untested.
