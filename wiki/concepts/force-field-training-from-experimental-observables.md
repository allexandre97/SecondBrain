---
type: concept
status: active
created: 2026-06-30
updated: 2026-07-01
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/experimental-benchmarking
  - research/biomolecules/proteins
tags:
  - force-field-training
  - experimental-observables
  - forcebalance
related:
  - "[[wiki/concepts/automated-force-field-training]]"
  - "[[wiki/concepts/free-energy-reweighting-for-force-field-fine-tuning]]"
  - "[[wiki/concepts/forcebalance]]"
  - "[[wiki/concepts/protein-force-field-benchmark-datasets]]"
sources:
  - SRC-0014
  - SRC-0015
  - SRC-0021
  - SRC-0022
  - SRC-0025
  - SRC-0043
sensitivity: public
encryption: none
---

# Force Field Training from Experimental Observables

## Summary

Force-field parameters can be trained directly against experimental observables by defining a differentiable or gradient-estimable property pipeline, comparing simulated and experimental values, and regularizing parameter movement from a reference model. [SRC-0014] [SRC-0021]

## Key Points

- SRC-0014 trains CHARMM36 lipid Lennard-Jones parameters against SAXS intensities using ForceBalance-SAS. [SRC-0014]
- SRC-0021 trains OBC2 GB cavity radii against host-guest absolute binding free energies using OpenFF Evaluator and ForceBalance. [SRC-0021]
- In both cases, the property target is an experimental condensed-phase observable, not a direct QM energy label. [SRC-0014] [SRC-0021]
- Regularization or prior widths are essential because observable fitting can otherwise exploit parameter directions that improve one property while harming transferability. [SRC-0014] [SRC-0021] [SRC-0022]
- Validation must include observables not used in training: solvent-stressed membranes and pure-lipid properties for SRC-0014; host-guest test systems, protein-ligand ABFEs, and hydration free energies for SRC-0021. [SRC-0014] [SRC-0021]
- ForceBalance is the shared optimization framework behind several examples in this wiki, including water-model fitting, SAXS lipid fitting, and host-guest binding-data fitting. [SRC-0025] [SRC-0014] [SRC-0021]
- Protein force-field benchmark datasets should include multiple protein classes and observables, because no single structural observable gives a complete view of ensemble accuracy. [SRC-0043]

## Core equations

Generic regularized property fit:

$$
\mathcal L(\theta)=
\sum_i
\left[
\frac{y_i(\theta)-y_i^{\mathrm{exp}}}{\sigma_i}
\right]^2
+
\sum_j
\left[
\frac{\theta_j-\theta_{j,0}}{\sigma_{\theta,j}}
\right]^2.
$$

[SRC-0021]

Ensemble observable response:

$$
\frac{\partial \langle A\rangle_{\theta}}{\partial \theta_j}
=
\left\langle \frac{\partial A}{\partial \theta_j}\right\rangle_{\theta}
-\beta\,\mathrm{Cov}_{\theta}
\left(A,\frac{\partial U}{\partial \theta_j}\right).
$$

[SRC-0014]

## Implementation consequences

The property evaluator must return both predictions and either analytic, automatic-differentiation, finite-difference, or fluctuation-response gradients. [SRC-0014] [SRC-0021]

Observable-specific preprocessing can be part of the model. For example, SAXS intensities may need interpolation and amplitude fitting, while host-guest ABFEs require restraint, pose, and standard-state conventions. [SRC-0014] [SRC-0021]

## Caveats

Optimizing to one observable family can create tradeoffs with another; SRC-0021 improves binding while degrading HFEs, and SRC-0014 finds that SAXS-only information has transferability limits. [SRC-0014] [SRC-0021]

## Links

- [[wiki/sources/SRC-0014-lipid-force-field-saxs-reparameterization]]
- [[wiki/sources/SRC-0021-tuning-potential-functions-host-guest-binding-data]]
- [[wiki/sources/SRC-0025-building-force-fields-automatic-systematic-reproducible-approach]]
- [[wiki/concepts/automated-force-field-training]]
- [[wiki/concepts/forcebalance]]
- [[wiki/concepts/protein-force-field-benchmark-datasets]]
- [[wiki/questions/force-field-training-validation-scope]]
- [[wiki/claims/CLM-0009-observable-fitting-needs-held-out-validation]]
- [[wiki/claims/CLM-0012-forcebalance-reduces-manual-fitting-noise]]
- [[wiki/tensions/TEN-0006-observable-fitting-gain-vs-transferability-tradeoff]]
