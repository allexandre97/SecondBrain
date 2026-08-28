---
type: tension
status: active
created: 2026-08-20
updated: 2026-08-28
tension_status: active
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/molecular-simulation/free-energy
  - research/statistics/monte-carlo
tags:
  - tension
  - ffrefine
  - observable-sensitivity
  - replay-support
  - trust-region
  - gradient-reproducibility
  - fisher-information
related:
  - "[[wiki/answers/ffrefine-retrospective-fisher-treatment-development]]"
  - "[[wiki/answers/ffrefine-long-archive-target-gradient-convergence]]"
  - "[[wiki/answers/ffrefine-average-observable-trainability-validation]]"
  - "[[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]"
  - "[[wiki/claims/CLM-0038-fixed-archive-gradient-validation-does-not-establish-fresh-archive-trainability]]"
  - "[[wiki/questions/QST-0006-average-observable-trainability-sampling-budget]]"
related_claims:
  - "[[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]"
  - "[[wiki/claims/CLM-0038-fixed-archive-gradient-validation-does-not-establish-fresh-archive-trainability]]"
related_questions:
  - "[[wiki/questions/QST-0006-average-observable-trainability-sampling-budget]]"
sources:
  - SRC-0018
  - SRC-0023
sensitivity: public
encryption: none
project_evidence:
  - "FFRefine fresh-archive enthalpy/cutoff and dielectric/PME parameter-shift scans completed 2026-08-20"
  - "FFRefine reaction-field dielectric full-gradient campaign 20260821-124443"
  - "FFRefine cross-fitted reaction-field dielectric direction run 20260821-151000"
  - "FFRefine reaction-field dielectric replica comparison run 20260821-190105"
  - "FFRefine cross-observable reaction-field target/Fisher reproducibility run 20260822-204246"
  - "FFRefine two-independent-100ns reaction-field target-gradient convergence comparison completed 2026-08-26"
  - "FFRefine retrospective Fisher-treatment screen and paired cross-archive replay completed 2026-08-28"
---

# Average-Observable Signal vs Replay Support

## Tension

Larger parameter perturbations can produce an easier-to-measure enthalpy or dielectric response, but the same perturbations can destroy overlap with the fixed archive. Smaller perturbations preserve replay support while leaving the observable displacement below sampling uncertainty. [SRC-0018] [SRC-0023]

## Evidence

In the FFRefine 20 ns scans, the best support- and KL-valid SNRs were 0.1121 for enthalpy and 0.08847 for PME dielectric. Much larger raw signals appeared for oxygen-sigma changes, including SNR 19.87 for enthalpy and 22.49 for dielectric, but those proposals had KL values above 10 and failed replay support.

The later reaction-field whole-gradient campaign found a different boundary case. A full QEq-plus-bounded proposal reduced one 10 ns archive's replay loss by 2.26% with strong ESS retention, but its paired confidence interval was inconclusive and empirical KL was 0.010535 for a nominal 0.01 step. Thus a combined direction can improve the archive-local objective without yet being statistically distinguishable or safely inside a strict empirical trust region.

The four-archive cross-fitted repetition substantially narrowed this tension. The frozen candidate reduced replay loss on all four archives by 2.36–3.12%; pooled development and held-out improvements were 2.722% and 2.718%. Both pooled confidence intervals excluded zero, development/held-out Fisher-metric direction cosine was 0.9325, and norm ratio was 0.9975. Replay support remained strong. The formal failure came from one empirical KL of 0.010215 against a 0.01 ceiling and from confidence bounds that established positive improvement but not an improvement of at least 1%.

The corrected replica comparison run `20260821-190105` did not reproduce that coherence. At matched aggregate production cost, two 5 ns replicas gave development/held-out direction cosine -0.072 and a held-out loss increase of 0.29%. Two 10 ns replicas doubled aggregate production, passed every empirical-KL check, roughly doubled local ESS, and improved chronological gradient stability to three of four archives, but direction cosine remained only 0.287 and the held-out point improvement was 0.52% with an interval crossing zero. Within-archive replica direction cosines remained poor in both variants.

The cross-observable reaction-field run `20260822-204246` separated Fisher variation from observable-gradient variation under matched conditions. Density and RDF natural-gradient cosines were at least 0.996 between shared replicas, independent archives, and pooled arms. Enthalpy cosines were 0.170, -0.545, and 0.589; dielectric cosines were 0.265, -0.089, and 0.764. All endpoints retained the same five Fisher modes, and minimum Fisher-subspace principal cosines exceeded 0.9999. A shared gradient evaluated with the two endpoint Fishers gave cosines of 0.989–1.000, whereas a shared Fisher did not repair the enthalpy or dielectric disagreement. The instability is therefore target-gradient dependent, with Fisher inversion acting as an amplifier rather than an archive-dependent root cause.

Replay transfer made the distinction operational. Independent density and RDF proposals improved both archives. Independent enthalpy proposals reduced their source losses by 7.69% and 11.81% but increased the other losses by 6.54% and 5.26%. Independent dielectric proposals reduced source losses by 2.08% and 2.23% but increased the other losses by 0.47% and 0.17%. All replay-support checks passed, with minimum local ESS retention at least 0.9004 and candidate ESS retention at least 0.9781.

The same run also limits a simple “internally stable but externally unstable” account. All four individual 10 ns trajectories had stable density/RDF half-directions and unstable enthalpy/dielectric half-directions. Dielectric target-value splits nevertheless passed in all four trajectories, showing that convergence of the mean observable does not establish convergence of its parameter gradient. Independent pooling improved the dielectric signal: the pooled-arm cosine reached 0.764 at the default Fisher floor and exceeded 0.8 at two alternative predeclared floors, while pooled cross-replay point estimates were favorable. One campaign seed and point estimates without paired confidence intervals are not enough to treat that direction as validated.

Finally, setting nominal KL and the hard empirical ceiling both to 0.01 left no calibration margin. Only 3 of 56 member-level probes passed empirical KL, despite all 56 passing support. A smaller nominal target or empirical backtracking is required, but this control correction cannot by itself repair archive-specific gradients.

This adds a second tension: conventional support and time-split diagnostics can improve while the force-field direction remains replica dependent. Every replica covered the complete thermodynamic ladder, so thermodynamic-state coverage did not guarantee equilibration of the dipole-fluctuation modes controlling dielectric response.

The leading failure hypothesis is therefore not that differentiation is algebraically wrong or that the Fisher estimate is generically unstable, but that an archive-local gradient need not be a reproducible estimate of the equilibrium gradient. It may look internally coherent in some runs and fail even chronological-half comparison in others. If archive-specific gradient error is of the same order as the equilibrium gradient, Fisher inversion can amplify that error, and resimulation between macro epochs can rotate or reverse the apparent descent direction after a successful replay step.

This is not a choice between “use a detectable step” and “use a conservative step.” A detectable but unsupported reweighting estimate is not a valid teacher signal, while a supported but unresolved estimate cannot establish a stable optimization direction.

The two-independent-100 ns reaction-field comparison shows that this tension can resolve differently by target family under the same sampling and Fisher geometry. Dielectric's cumulative natural direction became continuously reproducible from 60 through 100 ns and reached cosine 0.9743 at 100 ns. Enthalpy's raw-gradient cosine reached 0.9691, yet full Fisher preconditioning reduced natural-direction agreement to 0.6288. A common gradient with the two archive Fishers gave unit agreement, whereas a common Fisher did not repair the enthalpy result. The Fisher is therefore a target-dependent error amplifier rather than an archive-dependent global failure in this experiment. [[wiki/answers/ffrefine-long-archive-target-gradient-convergence]]

This adds a third tension: cumulative independent-archive agreement versus within-archive time stability. The two 100 ns dielectric directions agreed, but their chronological-half cosines were only 0.451 and 0.269. A cumulative estimate can average toward a common direction without each half being individually precise. More archive length and more independent archives answer related but noninterchangeable questions.

The retrospective Fisher-treatment campaign adds two further tensions. First, exact direction reproducibility and finite-step replay descent are not equivalent. Small-$\gamma$ enthalpy directions had poor independent-archive cosine but nevertheless reduced the opposite archive's loss in both directions with paired intervals below zero. A conservative cosine gate can therefore reject directions that lie in a broad shared descent cone. It remains useful because the treatment was selected on the same data and the paired intervals do not measure between-campaign uncertainty.

Second, regularisation strength and replay signal are not ordered by a single notion of conservatism. The production hard floor removed two positive normalized modes near $8.2\times10^{-5}$ and $2.5\times10^{-4}$. Damping with $\gamma=10^{-4}$ restored them with large gains and produced the strongest dielectric and enthalpy replay responses. It also exposed the optimisation to low-Fisher modes whose population stability is unknown. Modal-SNR filtering did not address this tradeoff because it only downweighted already retained modes.

Nominal and empirical trust regions also separated. Identity and diagonal directions were scaled to the same estimated KL 0.005 as the other treatments but realised empirical KL around 0.00025--0.00089 for the difficult targets. Their smaller and often inconclusive loss changes therefore mix optimiser geometry with a much smaller realised perturbation. A fair prospective comparison must preserve support while matching empirical replay KL.

## Interpretation

The tension should be managed by increasing genuinely independent information while keeping support and fresh-simulation requirements fixed. Density and RDF should remain matched positive controls because they distinguish pipeline-wide Fisher failures from target-specific gradient failures. The long-archive result and its paired replay follow-up justify a prospective dielectric comparison with the production hard Fisher and predeclared $\gamma=10^{-4}$ damping; neither the 60 ns crossing nor the damping value may be retuned on the new pair. Enthalpy requires the same separation of sampling from optimiser geometry, with the damped shared-descent result treated as a lead rather than an eligibility pass. Identity and diagonal arms require empirical-KL-matched scaling before their weaker response is interpreted. Replicas sharing one TSS preparation must not be counted as equivalent to independently prepared archives, and neither cumulative two-archive agreement nor paired uncertainty conditional on those archives replaces broader independent validation. SRC-0018's frozen-reference workflow makes support and resimulation part of optimisation validity, not optional diagnostics. [SRC-0018]

## Links

- [[wiki/answers/ffrefine-retrospective-fisher-treatment-development]]
- [[wiki/answers/ffrefine-average-observable-trainability-validation]]
- [[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]
- [[wiki/claims/CLM-0038-fixed-archive-gradient-validation-does-not-establish-fresh-archive-trainability]]
- [[wiki/questions/QST-0006-average-observable-trainability-sampling-budget]]
- [[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]
- [[wiki/sources/SRC-0023-statistically-optimal-analysis-multiple-equilibrium-states-mbar]]
