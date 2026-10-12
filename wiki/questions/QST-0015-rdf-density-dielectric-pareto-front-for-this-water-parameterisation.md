---
type: question
status: active
created: 2026-10-04
updated: 2026-10-11
question_status: open
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/machine-learning/scientific-modeling
tags:
  - question
  - ffrefine
  - multi-objective-optimization
  - water-model
  - pareto-front
related:
  - "[[wiki/answers/ffrefine-config-vs-weighted-sum-water-campaign-results]]"
  - "[[wiki/tensions/TEN-0020-config-family-exclusion-versus-untreated-drift]]"
  - "[[wiki/questions/QST-0011-config-versus-weighted-sum-under-calibrated-direction-gates]]"
  - "[[wiki/concepts/tolerance-normalized-multi-observable-losses]]"
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
sources:
  - SRC-0018
sensitivity: public
encryption: none
project_evidence:
  - "FFRefine water runs 20260930-132911 (weighted sum) and 20260930-132851 (ConFIG), both still running; snapshot taken 2026-10-04 (weighted sum 23 epochs, ConFIG 27 epochs): from a shared start, weighted sum drove the dielectric residual from +50..+34 to +3.5..-1.8 while density's thermal-expansion residual worsened from -16.7 to -21.6 g/L over 27 degC; ConFIG roughly halved RDF RMS on every pair type and improved density's thermal-expansion residual to -14.6 g/L, but left the dielectric residual at +35..+25 after excluding that family for its last four epochs (as of this snapshot)"
  - "2026-10-05 update: weighted sum's step stopped oscillating on density (replaced by a crawl) over checkpoints 23-27 but density's thermal-slope residual stayed stuck at about -22 g/L the whole time, before the run ended on an unrelated out-of-memory crash; ConFIG's whitened rdf-density gradient cosine, previously mildly positive, turned negative (-0.31 to -0.77) over checkpoints 29-34, so all three families are now pairwise conflicting rather than only dielectric against the other two"
scope: timeless
---

# Do RDF, Density Thermal Expansion, and Dielectric Trade Off for This Water Parameterisation?

## Question

Under FFRefine's ten-parameter rigid-geometry, QEq-charge water model (Lennard-Jones sigma/epsilon for O and H, double-exponential repulsion alpha/beta, QEq electronegativity and hardness for H and O), do the RDF, density-thermal-expansion, and static-dielectric-constant target families sit on a genuine trade-off surface — so that, within reach of gradient-based fitting, no parameter setting can improve one family without worsening another — or does the apparent trade-off observed so far only reflect how two particular gradient-aggregation methods happened to walk the loss landscape? [SRC-0018]

## Context

A weighted-sum campaign and a ConFIG campaign, both still running, started from identical initial parameters and otherwise identical experiment configuration. At a snapshot taken 2026-10-04 they had reached different physical compromises: weighted sum converged the dielectric constant closely but made density's thermal-expansion residual worse than the starting point; ConFIG roughly halved RDF structural error and improved density's thermal slope but left dielectric essentially unimproved at this snapshot, in part because dielectric was excluded from ConFIG's aggregate step for its most recent four epochs. See [[wiki/answers/ffrefine-config-vs-weighted-sum-water-campaign-results]] for the full numbers, and [[wiki/tensions/TEN-0020-config-family-exclusion-versus-untreated-drift]] for why ConFIG's exclusion of dielectric was conflict-driven (whitened inter-family gradient cosines between dielectric and the other two families were consistently negative, -0.17 to -0.77) rather than purely a matter of dielectric's own sampling noise.

This pattern is consistent with a genuine Pareto front, but it is equally consistent with an aggregation artifact: ConFIG's dielectric result is confounded by exclusion (a family that is not optimised cannot improve), and weighted sum's density result is confounded by that family being the stiffest included direction, which the weighted-sum run's KL-capped step oscillated on rather than converged through (see [[wiki/answers/ffrefine-config-vs-weighted-sum-water-campaign-results]], step-oscillation section). The measured negative gradient cosines are evidence of local conflict between families at the particular parameter trajectories visited; they do not by themselves establish that the trade-off persists globally over the full ten-parameter space, nor that it cannot be resolved by a different parameterisation or a longer, non-oscillating, non-excluding optimisation path.

## Current Position

Open. As of 2026-10-05, evidence somewhat strengthens the case for a genuine trade-off (see Evidence timeline), but the confounds described below remain unresolved, and none of the three experiments proposed to disambiguate them has been attempted.

No experiment has yet tried to resolve the question directly, for example by: continuing weighted sum well past the point where it stopped oscillating on density, to see whether dielectric and density can both converge once the stiff-direction pathology is fixed; running ConFIG with a conflict-aware removal rule that does not simply drop dielectric, to see whether the rdf/density gains persist once dielectric remains included; or inspecting the Jacobian of the three families' predictions with respect to the ten latent parameters directly, independent of any optimiser trajectory, to check for near-collinear or opposing rows. Until one of these is done, the measured negative gradient cosines should be read as evidence of trade-off along the paths these two runs actually took, not as an established property of the model.

## Evidence timeline

- 2026-10-05: weighted sum did go on to stop oscillating on density (replaced by a crawl, checkpoints 23-27; see [[wiki/answers/ffrefine-config-vs-weighted-sum-water-campaign-results]]), which was one of this page's own proposed tests. Density's thermal-slope residual nonetheless stayed stuck at about -22 g/L the whole time, rather than resuming convergence once the oscillation pathology was gone — consistent with, but not conclusive proof of, a genuine trade-off, since the run ended on an unrelated out-of-memory crash before density had much further opportunity to move. Separately, ConFIG's whitened rdf-density gradient cosine, previously mildly positive, turned negative (-0.31 to -0.77) over checkpoints 29-34: **all three families are now measured as pairwise conflicting**, not only dielectric against the other two. This strengthens the case for a genuine trade-off surface somewhat, but the two outstanding confounds from the first snapshot remain unresolved: ConFIG's dielectric result is still confounded by repeated exclusion, and the crash cut off weighted sum's own test before it could run to a comparable conclusion. The Jacobian-based test proposed above has still not been attempted.

## Links

- [[wiki/answers/ffrefine-config-vs-weighted-sum-water-campaign-results]]
- [[wiki/tensions/TEN-0020-config-family-exclusion-versus-untreated-drift]]
- [[wiki/questions/QST-0011-config-versus-weighted-sum-under-calibrated-direction-gates]]
- [[wiki/concepts/tolerance-normalized-multi-observable-losses]]
- [[wiki/concepts/awh-replay-force-field-optimization]]
- [[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]
