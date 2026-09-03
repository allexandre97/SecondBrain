---
type: question
status: active
created: 2026-08-20
updated: 2026-09-03
question_status: partially-answered
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/molecular-simulation/free-energy
  - research/statistics/monte-carlo
tags:
  - question
  - ffrefine
  - enthalpy
  - dielectric-constant
  - sampling-budget
  - trainability
  - trust-region
  - kl-conditioning
related:
  - "[[wiki/answers/ffrefine-prospective-dielectric-damped-fisher-training]]"
  - "[[wiki/questions/QST-0007-checkpoint-assessment-versus-next-direction-readiness]]"
  - "[[wiki/answers/ffrefine-retrospective-fisher-treatment-development]]"
  - "[[wiki/answers/ffrefine-long-archive-target-gradient-convergence]]"
  - "[[wiki/answers/ffrefine-average-observable-trainability-validation]]"
  - "[[wiki/claims/CLM-0038-fixed-archive-gradient-validation-does-not-establish-fresh-archive-trainability]]"
  - "[[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]"
  - "[[wiki/claims/CLM-0039-trust-region-kl-must-match-replay-conditioning]]"
  - "[[wiki/claims/CLM-0040-damped-conditional-fisher-dielectric-training-survives-fresh-resimulation]]"
  - "[[wiki/questions/force-field-training-validation-scope]]"
sources:
  - SRC-0018
  - SRC-0023
sensitivity: public
encryption: none
project_evidence:
  - "FFRefine fresh-archive enthalpy/cutoff and dielectric/PME trainability runs completed 2026-08-20"
  - "FFRefine reaction-field dielectric full-gradient campaign 20260821-124443"
  - "FFRefine cross-fitted reaction-field dielectric direction run 20260821-151000"
  - "FFRefine reaction-field dielectric replica comparison run 20260821-190105"
  - "FFRefine cross-observable reaction-field target/Fisher reproducibility run 20260822-204246"
  - "FFRefine two-independent-100ns reaction-field target-gradient convergence comparison completed 2026-08-26"
  - "FFRefine retrospective Fisher-treatment screen and paired cross-archive replay completed 2026-08-28"
  - "FFRefine post hoc within-state/between-state Fisher decomposition completed 2026-08-29"
  - "FFRefine state-conditional Fisher-treatment screen and replay completed 2026-08-30 through 2026-08-31"
  - "FFRefine dielectric-only damped-Fisher reaction-field water-temperature run 20260901-171027, completed 2026-09-02"
  - "FFRefine higher-KL dielectric-only damped-Fisher reaction-field water-temperature run 20260902-115818, intentionally stopped during epoch 8 on 2026-09-03 after six paired-confirmed fresh updates"
---

# Average-Observable Trainability Sampling Budget

## Question

What archive length, number of independent replicas, uncertainty estimator, and parameter-direction basis are required before FFRefine can identify a five-standard-error enthalpy or dielectric teacher signal without leaving replay support or the KL trust region?

## Context

Controlled fixed-archive checks validate the implemented enthalpy and PME dielectric mathematics, but fresh 10 ns and 20 ns scans found no eligible direction among the tested coordinate shifts. The best support- and KL-valid SNR was 0.1121 for enthalpy and 0.08847 for PME dielectric at 20 ns, versus the required SNR of 5. [[wiki/answers/ffrefine-average-observable-trainability-validation]]

Reweighting methods require sampled support for the candidate distribution, and fresh resimulation is required before an archive-local improvement is treated as robust. [SRC-0018] [SRC-0023]

## Current position

Twenty nanoseconds in one sequentially extended archive was insufficient under the original settings. A subsequent reaction-field campaign tested the production optimizer's complete QEq-plus-bounded-parameter gradient. Its first 10 ns archive produced a supported 2.26% replay-loss reduction, but paired confidence was inconclusive and empirical KL was 0.010535 for a nominal 0.01 step. After extension, both 20 ns archives were `sampling_limited`; the old output did not retain the exact failing subgate.

The completed cross-fitted run `20260821-151000` then used two independent 10 ns development archives to estimate one pooled full-gradient proposal and two independent 10 ns held-out archives to test that fixed proposal. All four archive point estimates improved by 2.36–3.12%. Pooled point improvements were 2.722% in development and 2.718% held out; both confidence intervals excluded zero. The development and held-out Fisher-metric direction cosine was 0.9325 with norm ratio 0.9975. This establishes a reproducible replay direction under pooling, even though every individual archive's chronological half-gradient comparison failed.

The formal result remained `inconclusive`. One development empirical KL was 0.010215, 2.15% above the hard 0.01 ceiling, while the other three passed. The conservative lower bounds established only 0.815% and 0.236% loss improvement, below the protocol's requirement to establish at least 1%. The remaining sampling-budget question has therefore moved: the existence and sign of a pooled full-gradient replay response are supported, but the budget needed for a predefined minimum effect size and for fresh candidate simulation remains unknown.

Run `20260821-190105` implemented those corrections and compared two replicas in every TSS phase. The cost-matched variant used 5 ns per replica, or 10 ns aggregate production per archive; the higher-power variant used 10 ns per replica, or 20 ns aggregate. Both retained two independently prepared development and two independently prepared held-out archives.

Both variants remained `inconclusive`. Development/held-out Fisher direction cosines were -0.072 and 0.287, while mean within-archive replica cosines were -0.277 and 0.090. The higher-power variant improved ESS, within-archive loss uncertainty, and chronological gradient stability, but one held-out archive improved while the other worsened. Its held-out point improvement was only 0.52%, below the prospective 1% threshold, and its confidence interval crossed zero. All of its empirical KL values passed.

The sampling-budget question has therefore narrowed again. More production within shared-preparation replicas improves conventional diagnostics but has not established directional reproducibility. The next evidence should quantify variation across independently prepared archives or independent campaign repetitions, rather than treating replica count alone as an effective independent sample size.

The main working hypothesis is that each finite archive yields a mathematically valid but archive-specific estimate of the dielectric gradient, and that the between-archive error is currently comparable to or larger than the equilibrium gradient. This would make a direction selected in one macro epoch unreliable after fresh resimulation. The hypothesis is supported by the coexistence of chronological stability in three of four higher-power archives with poor replica and development/held-out direction agreement. It remains provisional because one earlier four-archive run did produce a coherent direction.

Run `20260822-204246` added density and RDF as matched positive controls and enthalpy as a second difficult observable. It compared two 10 ns replicas sharing one reaction-field TSS archive with two independently prepared one-replica 10 ns archives. Density and RDF directions agreed with cosines of at least 0.996 under every full-path comparison. Enthalpy and dielectric failed between shared replicas, between independent archives, between pooled arms at the default Fisher floor, and between chronological halves. Independent enthalpy and dielectric proposals improved their source archives but worsened the other archive; density and RDF proposals transferred.

The run substantially weakens a pipeline-wide Fisher-error explanation. Every endpoint retained the same five modes, Fisher subspaces had minimum principal cosines above 0.9999, and changing Fishers while holding the gradient fixed preserved the direction. The disagreement remained when gradients were changed under a common Fisher. The open budget is therefore the amount and organization of independent information required to estimate the enthalpy or dielectric gradient covariance, not merely the amount required to estimate the Fisher matrix or the mean observable.

Pooling 20 ns of shared-replica production and 20 ns from two independent archives raised dielectric direction agreement to 0.764 at the default Fisher floor. It exceeded the 0.8 threshold at floors 0.0001 and 0.01, and pooled proposals had favorable cross-arm point responses. This is a prospective lead, not a resolved answer: only one campaign seed was run, individual directions remained inconsistent, paired replay-loss confidence intervals were not reported, and the nominal KL target of 0.01 exceeded the 0.01 empirical ceiling in 53 of 56 member-level probes.

The next budget experiment should therefore repeat independently pooled arms across new seeds, predeclare the Fisher floor, retain density and RDF controls, leave empirical-KL margin, and report paired replay-loss uncertainty. Only a direction that repeats under those conditions should advance to fresh candidate simulations.

That long-budget diagnostic has now been reanalysed with the corrected state-conditional Fisher and maximum conditional-KL constraint. The configurations, targets, and raw gradients are unchanged. Density and RDF still pass throughout. Dielectric now passes continuously from 40 through 100 ns and reaches cosine 0.9955 at 100 ns. Enthalpy reaches cosine 0.8143 with norm ratio 1.0079 at 100 ns and therefore passes only the final tested endpoint; its 90 ns cosine is 0.7368. [[wiki/answers/ffrefine-long-archive-target-gradient-convergence]]

The sampling-budget question has therefore changed but remains open. For dielectric, 40–100 ns cumulative archives are a plausible range for prospective repetition, not a validated minimum. For enthalpy, the corrected geometry removes the previous categorical 100 ns failure, but an isolated endpoint crossing does not establish stationarity: both 100 ns chronological-half comparisons fail and local blocks remain unstable. Additional independent archive pairs are required for both families.

Historical retrospective treatment development on the same pair produced finite-step replay evidence for proposals constructed with the old joint-Fisher geometry. Those exact proposals remain valid observations: hard-Fisher dielectric and small-$\gamma$ enthalpy directions transferred across this archive pair. They are not, however, validation of the corrected conditional-Fisher proposals, and their treatment ranking was not performed at a conditioning-matched KL. [[wiki/answers/ffrefine-retrospective-fisher-treatment-development]]

The low identity/diagonal KL has now been explained. Their scale factors correctly enforced mixed-Fisher KL 0.005, but about 80--84% of that nominal budget came from covariance of mean scores between thermodynamic states. The empirical replay KL normalizes each state's weights separately and sees only within-state configurational change. Hard and mildly damped full-Fisher directions spent about 98--99% of their nominal budget within states, explaining why their empirical KL remained near 0.005. This result splits the open budget question again: archive length and gradient uncertainty remain unresolved, but the trust-region metric must also be matched to the conditioning of the replay diagnostic. [[wiki/claims/CLM-0039-trust-region-kl-must-match-replay-conditioning]]

At that stage, dielectric's corrected cumulative direction was highly reproducible on one archive pair, but its finite-step replay and fresh-simulation performance under the corrected backend remained unknown. For enthalpy, the unresolved quantity was whether the marginal 100 ns endpoint pass would repeat and produce held-out or fresh descent. The subsequent conditional campaign addressed the first dielectric gap without resolving enthalpy.

The conditional retrospective campaign and first prospective dielectric run have now finished. The corrected campaign made hard full Fisher, damped $\gamma=0.03$ and $0.1$, diagonal, and selected modal-SNR dielectric proposals eligible. Damped $\gamma=0.1$ was frozen for the prospective run as a smooth full-correlation treatment. It passed three consecutive optimization-archive direction gates. The first two resulting checkpoints then produced paired fresh loss changes of -0.6168 and -0.5267 with intervals below zero, and two final-validation replicas reproduced the best checkpoint.

The fourth macro archive passed direct dielectric splitting but failed the damped direction cosine gate at 0.657. Consequently, 60 ns in one replica is demonstrably sufficient in some parameter states and insufficient in another realization/state of the same campaign. The dielectric budget question has shifted from “can a fresh update ever work?” to “what adaptive allocation reliably restores an optimization-ready direction when a later macro archive fails?” [[wiki/answers/ffrefine-prospective-dielectric-damped-fisher-training]]

The higher-KL run `20260902-115818` changes the balance of evidence again. With the same one-replica 60 ns production budget and $\gamma=0.1$ treatment, all seven completed optimization archives passed the damped direction gate, and checkpoints 1 through 6 each passed paired fresh comparison. This answers the existence question more strongly: one 60 ns replica can repeatedly resolve a useful dielectric direction along a sustained local trajectory.

It does not identify a minimum or universal budget. The run is one additional campaign trajectory, its lowest accepted target-state ESS retention was only 0.5098 against a 0.5 threshold, and it was intentionally stopped before checkpoint 7 received a fresh comparison or terminal replicate validation. The open question is now primarily how success frequency, direction readiness, and collateral-property preservation vary across independent seeds and parameter regions, rather than whether dielectric training can work at all. [[wiki/claims/CLM-0040-damped-conditional-fisher-dielectric-training-survives-fresh-resimulation]]

The run cannot answer whether longer continuation, multiple independent replicas, or an independently prepared archive is most cost effective because no production extension was allowed. It also cannot characterize campaign-to-campaign success probability from one seed. Checkpoint 3 was not paired against its parent after the direction failure, exposing a separate pipeline question that must be fixed before sampling strategies are compared. [[wiki/questions/QST-0007-checkpoint-assessment-versus-next-direction-readiness]]

## Validation boundaries

- Do not weaken SNR or support thresholds merely to produce an eligible candidate.
- Do not infer $1/\sqrt{t}$ error scaling from one sequential extension.
- Coordinate-wise positive shifts may miss a supported combined direction, but changing the direction basis creates a new experiment.
- Pooling development archives must not leak candidate selection into the held-out archives; the proposed parameter vector is frozen before held-out replay.
- A confidence interval below zero establishes descent but does not establish that the decrease exceeds a chosen minimum effect size; those are distinct claims and need distinct gates.
- A hard empirical-KL ceiling should be enforced while selecting the line-search scale, not only after a proposal has otherwise been selected.
- PME dielectric and cutoff/reaction-field enthalpy results do not isolate electrostatics dependence.
- A candidate that passes the replay prescreen still requires independent teacher archives and fresh macro-recovery validation. [SRC-0018]
- Replicas sharing one TSS state and bias are not interchangeable with independently prepared archives when assessing direction uncertainty.
- Chronological split stability can coexist with replica-direction disagreement; both axes must be reported for slowly mixing average observables.
- Archive-local gradient validity must not be reported as population-gradient reproducibility; macro training requires the latter.
- Mean-observable split agreement must not be used as a proxy for gradient convergence; dielectric target splits passed while its chronological and independent gradients failed.
- Fisher regularization choices must be predeclared or validated on separate campaign repetitions; pooled dielectric crossed the cosine threshold only under alternative floors in one observed run.
- Density and RDF should remain matched controls when changing the sampling budget or Fisher treatment.
- A first sustained cumulative-prefix crossing must not be reported as a universal minimum budget when it was selected from the observed trajectory.
- Agreement between two complete archives does not erase failed chronological-half checks; report both and obtain additional independent archive pairs.
- A retrospective treatment selected and replayed on the same archive pair is development evidence, even when each archive-specific proposal is evaluated on the other archive.
- Paired delete-block intervals quantify finite-step uncertainty conditional on one archive; they do not estimate treatment-selection or between-campaign uncertainty.
- Match realised empirical replay KL before interpreting identity, diagonal, hard, and damped loss-effect sizes.
- Before matching KL numerically, predeclare whether it represents state-conditional canonical reweighting or the joint extended ensemble; log within-state and between-state Fisher contributions and use a matching empirical diagnostic.
- Small-$\gamma$ damping reintroduces modes below the production hard floor; freeze the damping value and monitor modal uncertainty rather than retuning it on prospective data.
- A per-epoch budget that succeeds several times and fails once is not a universal threshold; predeclare the extension/replica rule before rerunning.
- A failed next-direction gate must not prevent paired evaluation of the already simulated checkpoint.

## Links

- [[wiki/answers/ffrefine-prospective-dielectric-damped-fisher-training]]
- [[wiki/questions/QST-0007-checkpoint-assessment-versus-next-direction-readiness]]
- [[wiki/answers/ffrefine-retrospective-fisher-treatment-development]]
- [[wiki/answers/ffrefine-average-observable-trainability-validation]]
- [[wiki/claims/CLM-0038-fixed-archive-gradient-validation-does-not-establish-fresh-archive-trainability]]
- [[wiki/tensions/TEN-0018-average-observable-signal-versus-replay-support]]
- [[wiki/questions/force-field-training-validation-scope]]
- [[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]
