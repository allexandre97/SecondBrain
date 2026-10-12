---
type: answer
status: active
created: 2026-07-01
updated: 2026-10-11
question: "What are the recurring validation problems across force-field fitting, ML potentials, and free-energy estimators?"
answer_status: answered
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/molecular-simulation/free-energy
  - research/machine-learning/molecular-modeling
  - research/experimental-benchmarking
  - research/statistics/monte-carlo
tags:
  - validation
  - transferability
  - benchmarking
  - molecular-simulation
related:
  - "[[wiki/concepts/cross-domain-validation-problems-in-molecular-simulation]]"
  - "[[wiki/questions/force-field-training-validation-scope]]"
  - "[[wiki/concepts/stability-aware-mlff-training]]"
  - "[[wiki/concepts/machine-learning-potential-datasets]]"
  - "[[wiki/concepts/free-energy-estimation]]"
  - "[[wiki/concepts/relative-binding-free-energy-benchmarking]]"
sources:
  - SRC-0005
  - SRC-0006
  - SRC-0007
  - SRC-0008
  - SRC-0009
  - SRC-0014
  - SRC-0016
  - SRC-0018
  - SRC-0019
  - SRC-0020
  - SRC-0021
  - SRC-0023
  - SRC-0024
  - SRC-0042
  - SRC-0044
  - SRC-0046
  - SRC-0059
  - SRC-0060
  - SRC-0061
  - SRC-0062
sensitivity: public
encryption: none
wiki_pages_used:
  - wiki/index.md
  - wiki/questions/force-field-training-validation-scope.md
  - wiki/concepts/automated-force-field-training.md
  - wiki/concepts/force-field-training-from-experimental-observables.md
  - wiki/concepts/free-energy-reweighting-for-force-field-fine-tuning.md
  - wiki/concepts/ensemble-and-force-field-refinement.md
  - wiki/concepts/stability-aware-mlff-training.md
  - wiki/concepts/machine-learning-potential-datasets.md
  - wiki/concepts/machine-learned-interatomic-potential-foundation-models.md
  - wiki/concepts/free-energy-estimation.md
  - wiki/concepts/relative-binding-free-energy-benchmarking.md
  - wiki/questions/tss-generalization-scope.md
  - wiki/questions/awh-validation-scope.md
  - wiki/sources/SRC-0020-mdrefine-supplementary-material.md
raw_sources_consulted: []
wiki_pages_updated:
  - wiki/concepts/cross-domain-validation-problems-in-molecular-simulation.md
  - wiki/index.md
  - wiki/log.md
scope: timeless
---

# Recurring Validation Problems Across Force-Field Fitting, Machine-Learning Potentials, and Free-Energy Estimators

## Short answer

The recurring problem is that a local success metric is repeatedly mistaken for downstream validity. In force-field fitting, this is fitting one observable, system, or benchmark and assuming transfer. In machine-learning potentials, it is treating static energy/force accuracy or dataset scale as enough for molecular dynamics. In free-energy estimation, it is trusting formal estimator optimality or error bars without checking overlap, mixing, decorrelation, and benchmark realism. [SRC-0014] [SRC-0021] [SRC-0024] [SRC-0059] [SRC-0023]

The common validation standard should be: test the method on held-out systems, held-out observables, the actual simulation protocol, explicit sampling-support diagnostics, realistic uncertainty estimates, and benchmarks that resemble the intended prospective use. [SRC-0016] [SRC-0018] [SRC-0046] [SRC-0061] [SRC-0062]

## Detailed answer

The wiki points to eight recurring validation problems.

1. **Transferability is narrower than the fitted loss.** Force-field fitting can improve the fitted target while degrading another observable: the wiki records host-guest binding-data fitting that improves binding free energies while worsening hydration free energies, and lipid SAXS fitting with transfer limits under solvent-stress validation. [SRC-0014] [SRC-0021]

2. **Static accuracy is not simulation reliability.** For machine-learning potentials, low energy or force error is not enough if molecular dynamics enters unstable or unphysical regions. Stability-aware training therefore adds downstream observable losses and unstable-trajectory discovery, while UBio-MolFM adds short downstream biomolecular molecular-dynamics tests but still lists longer, larger validation as future work. [SRC-0024] [SRC-0060]

3. **Dataset size does not equal coverage.** SPICE and OMol25 show why chemical-space and conformational-space coverage matter, but the dataset pages also emphasize label consistency, downstream tasks, charge/spin diversity, and domain-informed evaluation. The machine-learned interatomic-potential foundation-model page makes the same point at model scale: progress depends on data diversity, label fidelity, model expressivity, long-range physics, and benchmark design together. [SRC-0042] [SRC-0044] [SRC-0059]

4. **Sampling support is a hidden failure mode.** Reweighting-based force-field fine-tuning and free-energy methods need the reference ensemble to overlap the target distribution. Effective sample size, split-half checks, parity checks, and Kish-size diagnostics can reveal weight collapse, but high diagnostic values still do not prove that unsampled conformations are irrelevant. [SRC-0016] [SRC-0018] [SRC-0020]

5. **Estimator theory is not a substitute for trajectory diagnostics.** Free-energy estimators can have strong formal properties under stated assumptions, but practical molecular dynamics brings correlation, poor mixing, weak phase-space overlap, and setup-dependent window behavior. Times Square Sampling variance and convergence claims remain tied to its assumptions; Multistate Bennett acceptance ratio uncertainty estimates require effectively uncorrelated samples; AWH still needs independent repeats for robust uncertainty. [SRC-0005] [SRC-0006] [SRC-0023] [SRC-0009]

6. **Benchmarks can be too curated.** Relative binding free-energy benchmarks show that public curated systems can be easier than blinded private active-project systems, and retrospective FEP benchmarks can look better than prospective use because of selection and expert setup. Experimental data also have reproducibility limits, so disagreement with experiment is not automatically model error. [SRC-0046] [SRC-0061]

7. **Single summary metrics hide the failure mode.** Edgewise relative binding free-energy errors can be optimistic because transformation networks connect similar ligands; all-to-all pairwise metrics better represent arbitrary ligand comparisons. Machine-learning potential benchmarks have a related issue: a single leaderboard score can encourage optimization of the metric rather than downstream scientific usefulness. [SRC-0061] [SRC-0059]

8. **Error-source identifiability is weak.** When simulation and experiment disagree, the cause can be a force-field parameter, a forward model, an ensemble error, poor sampling, a bad setup choice, or noisy experiment. MDRefine records that multiple correction mechanisms can explain the same reduction in error, and relative binding free-energy benchmarking records that preparation choices such as protonation, pose, water sampling, and atom mapping can materially affect accuracy. [SRC-0019] [SRC-0046] [SRC-0061]

## Practical checklist

- Use held-out systems and held-out observable families, not only lower training loss. [SRC-0014] [SRC-0021]
- Validate the actual downstream simulation: trajectory stability, relevant observables, timescale, system size, and long-range physics. [SRC-0024] [SRC-0059] [SRC-0060]
- Report sampling-support diagnostics for reweighting and free-energy estimates, and treat them as necessary but not sufficient. [SRC-0016] [SRC-0018] [SRC-0020]
- Check estimator assumptions against practical trajectories: overlap, decorrelation, mixing, and independent repeats. [SRC-0006] [SRC-0023] [SRC-0009]
- Prefer benchmark designs that reflect prospective use, include uncertainty, and expose outliers rather than hiding them in aggregates. [SRC-0046] [SRC-0061] [SRC-0062]
- Separate possible error sources instead of treating one metric as proof of one cause. [SRC-0019] [SRC-0046]

## Key equations

No new equations are needed for this answer. The important shared quantitative diagnostic is effective sample size for reweighting support, already represented in [[wiki/concepts/free-energy-reweighting-for-force-field-fine-tuning]]. [SRC-0016]

## Sources used

- [[wiki/questions/force-field-training-validation-scope]] - Cross-source force-field fitting validation boundaries.
- [[wiki/concepts/stability-aware-mlff-training]] and [[wiki/concepts/machine-learning-potential-datasets]] - Machine-learning potential validation beyond static energy/force metrics.
- [[wiki/concepts/free-energy-estimation]] and [[wiki/concepts/relative-binding-free-energy-benchmarking]] - Estimator assumptions, overlap, benchmark uncertainty, and curated-versus-prospective benchmark limits.
- [[wiki/concepts/cross-domain-validation-problems-in-molecular-simulation]] - Durable synthesis page created for this answer.

## Wiki pages used

- [[wiki/index]]
- [[wiki/questions/force-field-training-validation-scope]]
- [[wiki/concepts/automated-force-field-training]]
- [[wiki/concepts/force-field-training-from-experimental-observables]]
- [[wiki/concepts/free-energy-reweighting-for-force-field-fine-tuning]]
- [[wiki/concepts/stability-aware-mlff-training]]
- [[wiki/concepts/machine-learning-potential-datasets]]
- [[wiki/concepts/machine-learned-interatomic-potential-foundation-models]]
- [[wiki/concepts/free-energy-estimation]]
- [[wiki/concepts/relative-binding-free-energy-benchmarking]]
- [[wiki/questions/tss-generalization-scope]]
- [[wiki/questions/awh-validation-scope]]
