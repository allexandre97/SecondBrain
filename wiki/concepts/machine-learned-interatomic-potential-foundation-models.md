---
type: concept
status: active
created: 2026-06-30
updated: 2026-06-30
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/machine-learning/molecular-modeling
  - research/machine-learning/scientific-modeling
  - research/molecular-simulation/datasets
  - research/molecular-simulation/molecular-dynamics
  - research/experimental-benchmarking
  - research/high-performance-computing
tags:
  - machine-learned-interatomic-potentials
  - foundation-models
  - mlip
  - equivariance
  - long-range-interactions
  - benchmarking
related:
  - "[[wiki/sources/SRC-0059-six-open-questions-in-machine-learned-interatomic-potential]]"
  - "[[wiki/sources/SRC-0060-ubio-molfm-universal-molecular-foundation-model]]"
  - "[[wiki/concepts/machine-learning-potential-datasets]]"
  - "[[wiki/concepts/automated-force-field-training]]"
  - "[[wiki/concepts/stability-aware-mlff-training]]"
  - "[[wiki/concepts/ubio-molfm-biological-molecular-foundation-model]]"
  - "[[wiki/concepts/molecular-response-property-foundation-models]]"
  - "[[wiki/concepts/garnet-force-field]]"
  - "[[wiki/claims/CLM-0013-energy-force-error-is-not-downstream-md-reliability]]"
  - "[[wiki/claims/CLM-0014-dataset-scale-does-not-replace-coverage-validation]]"
  - "[[wiki/questions/mlip-foundation-model-validation-scope]]"
  - "[[wiki/tensions/TEN-0008-dataset-scale-vs-downstream-validation]]"
sources:
  - SRC-0059
  - SRC-0060
  - SRC-0065
sensitivity: public
encryption: none
---

# Machine-Learned Interatomic Potential Foundation Models

## Summary

Machine-learned interatomic potential foundation models are pretrained, transferable MLIPs intended to support many molecular or materials simulations with little task-specific engineering. SRC-0059 argues that they should be evaluated through expressivity, scalability, memorization, multimodality, and compositionality, but also cautions that MLIP foundation models are not direct analogues of very large language foundation models. [SRC-0059, section 1]

## Key Points

- A foundation MLIP should be more than a highly accurate narrow force field: it should transfer across chemical, structural, and simulation contexts with limited retraining or fine-tuning. [SRC-0059, section 1]
- Better MLIP progress likely requires coordinated improvements in model expressivity, dataset diversity, data fidelity, optimization, and infrastructure, not simply larger datasets or larger models alone. [SRC-0059, section 2]
- Physical inductive biases such as equivariance improve data efficiency and consistency, but there is an unresolved tradeoff between explicitly encoding physics and learning broader behavior from very large datasets. [SRC-0059, section 2]
- Long-range MLIP behavior should be understood broadly: electrostatics, dispersion, screening, electronic delocalization, correlation length, global response, and graph-theoretic influence are different long-range problems. [SRC-0059, section 3]
- Current MLIPs can enable simulations in regimes that were previously difficult, but SRC-0059 treats most evidence as broad interpolation and hypothesis generation rather than autonomous discovery of new physical laws. [SRC-0059, section 4]
- Useful simulation scale depends on inference efficiency, distillation, hardware-specific kernels, memory use, training scalability, and reporting of performance metrics, not only benchmark accuracy. [SRC-0059, section 5]
- Model quality should be assessed with both representational diagnostics and pragmatic downstream tasks; single-metric benchmark dominance risks Goodhart's Law and the McNamara fallacy. [SRC-0059, section 6]
- UBio-MolFM is an example of a domain-focused molecular foundation-model strategy: it pairs a biology-specific dataset, long-short range equivariant architecture, and hardware-aware kernels with downstream MD observable tests. [SRC-0060]
- MACE-MDP illustrates a complementary direction: foundation-style models for molecular response properties such as dipole moments and polarizability tensors, which can be coupled to MLIPs for IR and Raman spectroscopy rather than replacing the potential-energy model itself. [SRC-0065]

## Core equations

Foundation-model scaling schematic: [SRC-0059, eq. 1]

$$
L(N) \propto N^{-\alpha}, \qquad
L(P) \propto P^{-\beta}, \qquad
L(C) \propto C^{-\gamma}.
$$

Long-range physical tail: [SRC-0059, eq. 2]

$$
V(r) \propto r^{-\alpha}.
$$

Equivariance condition: [SRC-0059, eq. 3]

$$
f(\rho_X(g)x)=\rho_Y(g)f(x).
$$

## Interpretation

SRC-0059 frames foundation MLIPs as an active research program rather than a settled class. The key issue is not whether one model has a strong leaderboard score, but whether it reliably covers the downstream scientific regime of interest: high-energy configurations, charged systems, interfaces, long-range responses, large systems, long trajectories, or experimentally constrained observables may each stress a different failure mode. [SRC-0059]

This complements existing wiki coverage of [[wiki/concepts/machine-learning-potential-datasets]]: dataset scale matters, but dataset quality, non-equilibrium coverage, local-environment diversity, and fidelity weighting can be more important than brute-force data volume. [SRC-0059, section 2]

SRC-0060 operationalizes several of these concerns for biomolecular simulation: it extends dataset coverage beyond small molecules, explicitly targets long-range and large-system efficiency, and reports short downstream MD validations rather than relying only on random-split force errors. Its own limitations, especially nucleic-acid imbalance and 100K-atom memory failure, are examples of why foundation-model claims still need task-specific validation. [SRC-0060, sections 2-3]

## Implementation consequences

- Prefer evaluating a foundation MLIP against the intended downstream simulation, not only a random-split energy or force score. [SRC-0059, section 6]
- Check whether the model's architecture or training data can support the relevant long-range physics before trusting charged, interfacial, polar, dielectric, or delocalized systems. [SRC-0059, section 3]
- Treat distillation as a practical route when a large foundation model is accurate but too slow or memory-heavy for production molecular dynamics. [SRC-0059, section 5.2]
- Report inference performance, memory use, and training cost where possible, because large models can be scientifically unusable if they cannot reach needed system sizes or timescales. [SRC-0059, section 5]
- For biology-focused foundation MLIPs, separate protein, nucleic-acid, solvent, ion, and binding benchmarks; UBio-MolFM's Stage 3 protein gains do not remove the reported DNA regression. [SRC-0060, sections 2.1.2 and 3.2]

## Caveats

- "Foundation model" remains partly definitional in atomistic simulation; SRC-0059 deliberately presents the criteria and questions as unsettled. [SRC-0059, section 1]
- A model that works on common benchmarks may still fail rare events, high-energy structures, long-range responses, or practical stability tests. [SRC-0059, sections 4 and 6]
- Scaling data, parameters, or compute along one axis can saturate or degrade if model expressivity, data quality, or physical fidelity becomes the limiting factor. [SRC-0059, section 2]

## Links

- [[wiki/sources/SRC-0059-six-open-questions-in-machine-learned-interatomic-potential]]
- [[wiki/sources/SRC-0060-ubio-molfm-universal-molecular-foundation-model]]
- [[wiki/sources/SRC-0065-mace-mdp-molecular-dipole-moments-polarizabilities]]
- [[wiki/concepts/machine-learning-potential-datasets]]
- [[wiki/concepts/ubio-molfm-biological-molecular-foundation-model]]
- [[wiki/concepts/molecular-response-property-foundation-models]]
- [[wiki/concepts/automated-force-field-training]]
- [[wiki/concepts/stability-aware-mlff-training]]
- [[wiki/concepts/garnet-force-field]]
- [[wiki/claims/CLM-0013-energy-force-error-is-not-downstream-md-reliability]]
- [[wiki/claims/CLM-0014-dataset-scale-does-not-replace-coverage-validation]]
- [[wiki/questions/mlip-foundation-model-validation-scope]]
- [[wiki/tensions/TEN-0008-dataset-scale-vs-downstream-validation]]

## Open Questions

- Which atomistic foundation-model criteria are necessary rather than merely desirable? [SRC-0059, section 1]
- When does learning physical structure from data beat encoding it by design? [SRC-0059, sections 2 and 5]
- Can long-range MLIP approaches be unified the way many short-range representations can be related to ACE-style frameworks? [SRC-0059, section 3]
- Which benchmark designs best predict downstream scientific usefulness without encouraging overfitting to the benchmark itself? [SRC-0059, section 6]
