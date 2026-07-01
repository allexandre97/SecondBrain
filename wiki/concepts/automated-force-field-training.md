---
type: concept
status: active
created: 2026-06-29
updated: 2026-06-30
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/machine-learning/scientific-modeling
tags:
  - automation
  - molecular-dynamics
related:
  - "[[wiki/concepts/garnet-force-field]]"
  - "[[wiki/concepts/force-field-training-from-experimental-observables]]"
  - "[[wiki/concepts/free-energy-reweighting-for-force-field-fine-tuning]]"
  - "[[wiki/concepts/symbolic-regression-interatomic-potentials]]"
  - "[[wiki/concepts/stability-aware-mlff-training]]"
  - "[[wiki/concepts/machine-learned-interatomic-potential-foundation-models]]"
  - "[[wiki/concepts/forcebalance]]"
  - "[[wiki/concepts/opc-water-model]]"
  - "[[wiki/concepts/machine-learning-potential-datasets]]"
  - "[[wiki/concepts/mlp-driven-bespoke-smirnoff-force-field-fitting]]"
sources:
  - SRC-0003
  - SRC-0014
  - SRC-0016
  - SRC-0017
  - SRC-0018
  - SRC-0019
  - SRC-0021
  - SRC-0024
  - SRC-0025
  - SRC-0027
  - SRC-0042
  - SRC-0044
  - SRC-0059
  - SRC-0060
  - SRC-0066
sensitivity: public
encryption: none
---

# Automated Force Field Training

## Summary

Automated force-field training aims to learn molecular mechanics parameters and functional-form choices from data with less manual tuning than conventional force-field development. [SRC-0003]

## Key Points

- SRC-0003 frames manual force-field tuning as a source of limited transferability and weak reproducibility. [SRC-0003]
- Garnet combines DFT-derived force, potential-energy-difference, and charge data from SPICE, Espaloma, GEMS, and MACE-OFF with condensed-phase enthalpy data and protein NMR observables. [SRC-0003]
- Condensed-phase training includes enthalpies of vapourisation for water, methanol, and benzene, plus enthalpies of mixing for selected molecular pairs. [SRC-0003]
- Protein training uses GB3 NMR data through ensemble reweighting, with gradients reused across batches because the protein simulations are expensive. [SRC-0003]
- The paper argues that automated training enables systematic exploration of force-field functional forms. [SRC-0003]
- The approach is not fully universal yet; future work should expand validated species to nucleic acids, lipids, metals, carbohydrates, IDPs, and other polymers. [SRC-0003]
- Later ingested sources broaden the training picture: experimental SAXS and binding observables can be direct ForceBalance targets, neural force fields can be fine-tuned by reweighting, and symbolic regression can search over interpretable functional forms. [SRC-0014] [SRC-0016] [SRC-0017] [SRC-0021]
- RNA force-field development needs motif-level validation because small systems such as UUCG tetraloops can reveal coupled errors that are not captured by broader or easier benchmarks. [SRC-0055] [SRC-0056]
- Across these approaches, regularization and validation outside the fitted observable are central because force-field training can improve one target while degrading transfer properties. [SRC-0014] [SRC-0021]
- SRC-0024 adds a stability-aware MLFF training view: downstream MD stability and observable recovery are training targets, not just energy/force errors. [SRC-0024]
- SRC-0025 introduces ForceBalance as a reproducible optimization framework for fitting force-field parameters, demonstrated on TIP3P-FB and TIP4P-FB water models. [SRC-0025]
- SRC-0027 shows a complementary water-model strategy where charge geometry is derived from electrostatic multipole matching before validating liquid and hydration properties. [SRC-0027]
- Large quantum-chemistry datasets such as SPICE and OMol25 supply broad energy/force labels for training general-purpose molecular ML potentials, but downstream simulation reliability still requires validation beyond random-split energy and force errors. [SRC-0044] [SRC-0042]
- Foundation-model MLIPs extend the automated-training question from parameter fitting to transferability, scale, long-range physics, simulation efficiency, and benchmark design. SRC-0059 argues that progress should not be reduced to only more data, only better architectures, or only larger models. [SRC-0059, sections 1-2]
- UBio-MolFM is a biology-focused instance of this broader program, combining a domain-specific DFT dataset, energy-force-consistent training, long-short range equivariant architecture, and downstream MD observable checks. [SRC-0060]
- `presto` uses transferable MLPs as fast reference models for fitting bespoke SMIRNOFF valence parameters, trading direct QM fitting cost for MLP evaluation speed while preserving a conventional MM functional form. [SRC-0066]

## Links

- [[wiki/sources/SRC-0003-training-a-force-field-from-scratch]]
- [[wiki/sources/SRC-0014-lipid-force-field-saxs-reparameterization]]
- [[wiki/sources/SRC-0016-fine-tuning-mm-force-fields-to-experimental-free-energies]]
- [[wiki/sources/SRC-0017-symbolic-regression-reinforcement-learning-interatomic-potentials]]
- [[wiki/sources/SRC-0021-tuning-potential-functions-host-guest-binding-data]]
- [[wiki/sources/SRC-0024-stable-training-machine-learning-force-fields-boltzmann-estimators]]
- [[wiki/sources/SRC-0025-building-force-fields-automatic-systematic-reproducible-approach]]
- [[wiki/sources/SRC-0027-building-water-models-different-approach-opc]]
- [[wiki/sources/SRC-0059-six-open-questions-in-machine-learned-interatomic-potential]]
- [[wiki/sources/SRC-0060-ubio-molfm-universal-molecular-foundation-model]]
- [[wiki/sources/SRC-0066-presto-bespoke-smirnoff-force-fields-mlps]]
- [[wiki/concepts/garnet-force-field]]
- [[wiki/concepts/double-exponential-potential]]
- [[wiki/concepts/force-field-training-from-experimental-observables]]
- [[wiki/concepts/free-energy-reweighting-for-force-field-fine-tuning]]
- [[wiki/concepts/rna-force-field-limitations]]
- [[wiki/concepts/symbolic-regression-interatomic-potentials]]
- [[wiki/concepts/stability-aware-mlff-training]]
- [[wiki/concepts/forcebalance]]
- [[wiki/concepts/opc-water-model]]
- [[wiki/concepts/machine-learning-potential-datasets]]
- [[wiki/concepts/machine-learned-interatomic-potential-foundation-models]]
- [[wiki/concepts/mlp-driven-bespoke-smirnoff-force-field-fitting]]
- [[wiki/concepts/ubio-molfm-biological-molecular-foundation-model]]
- [[wiki/questions/force-field-training-validation-scope]]
