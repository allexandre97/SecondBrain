---
type: concept
status: active
created: 2026-06-30
updated: 2026-06-30
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/machine-learning/scientific-modeling
  - research/data-management
  - research/molecular-simulation/datasets
  - research/machine-learning/molecular-modeling
  - research/biomolecules/proteins
tags:
  - datasets
  - machine-learning-potentials
  - quantum-chemistry
sources:
  - SRC-0042
  - SRC-0044
  - SRC-0059
  - SRC-0060
  - SRC-0065
related:
  - "[[wiki/concepts/automated-force-field-training]]"
  - "[[wiki/concepts/stability-aware-mlff-training]]"
  - "[[wiki/concepts/machine-learned-interatomic-potential-foundation-models]]"
  - "[[wiki/concepts/ubio-molfm-biological-molecular-foundation-model]]"
  - "[[wiki/concepts/molecular-response-property-foundation-models]]"
  - "[[wiki/claims/CLM-0014-dataset-scale-does-not-replace-coverage-validation]]"
  - "[[wiki/claims/CLM-0015-molecular-datasets-have-distinct-intended-uses]]"
  - "[[wiki/questions/mlip-foundation-model-validation-scope]]"
  - "[[wiki/tensions/TEN-0008-dataset-scale-vs-downstream-validation]]"
sensitivity: public
encryption: none
---

# Machine Learning Potential Datasets

## Summary

Machine-learning potential datasets provide quantum-chemistry energies, forces, structures, and sometimes auxiliary electronic properties for training ML models that approximate expensive electronic-structure calculations. SPICE targets drug-like molecules and protein-relevant chemistry; OMol25 expands scale, elements, charge/spin diversity, system size, and evaluation tasks. [SRC-0044] [SRC-0042]

## Key Points

- Dataset usefulness depends on both chemical-space coverage and conformational-space coverage. [SRC-0044]
- Forces are especially valuable because each conformation supplies many force components in addition to one energy. [SRC-0044]
- Consistent level of theory matters because heterogeneous quantum-chemistry labels can confound model training and evaluation. [SRC-0042] [SRC-0044]
- Charge and spin awareness are central for broader molecular chemistry datasets; OMol25 explicitly includes wide charge and spin variation. [SRC-0042]
- Practical evaluation should include downstream or domain-informed tasks, not only random-split energy and force errors. [SRC-0042]
- Overlay databanks address a complementary dataset problem: existing simulation trajectories can be made reusable for data-driven analyses by adding metadata, naming, quality-evaluation, and API layers without moving all raw data into one repository. [SRC-0057]
- For foundation-model MLIPs, dataset scale alone is insufficient: SRC-0059 argues that data diversity, local-environment coverage, label fidelity, model expressivity, optimization, and compute must be balanced together. [SRC-0059, section 2]
- High-throughput DFT datasets can contain systematic and unsystematic noise, near-equilibrium bias, and inconsistent settings; these issues can limit transferability even when the dataset is large. [SRC-0059, section 2.3]
- UBio-Mol26 is a biology-focused dataset intended to complement OMol25 by covering larger solvated biological systems up to about 1,200 atoms; its current top-down component is protein-focused, leaving nucleic-acid diversity as an identified gap. [SRC-0060, sections 4.1 and 4.1.1]
- SPICE-alpha is a response-property extension of SPICE that adds first-principles polarizabilities for training and evaluating dipole/polarizability models rather than only potential-energy models. [SRC-0065]

## Evidence

- SPICE reports more than 1.1 million conformations with DFT energies and forces for 15 elements. [SRC-0044]
- OMol25 reports more than 140 million DFT single-point calculations covering 83 elements, systems up to 350 atoms, and benchmark tasks such as conformer ranking, protonation, ionization, spin gaps, ligand-pocket interactions, and distance scaling. [SRC-0042]
- SRC-0059 compares large datasets and benchmarks such as OMat24, OMol25, MatPES, and Matbench Discovery to argue that useful evaluation needs downstream and physics-informed tests, not only aggregate energy/force errors. [SRC-0059, sections 2 and 6]
- SRC-0060 reports UBio-Mol26 as 17 million configurations across proteins, drug-like molecules, DNA/RNA fragments, lipid bilayers, explicit solvent, trace ions, and mixed basis-set fidelity levels. [SRC-0060, section 4.1]
- SRC-0065 reports SPICE-alpha as a large neutral-organic training set for MACE-MDP, with dipole moments and full polarizability tensors used for spectroscopy-oriented response-property prediction.

## Links

- [[wiki/sources/SRC-0042-the-open-molecules-2025-omol25-dataset-evaluations-and]]
- [[wiki/sources/SRC-0044-spice-a-dataset-of-drug-like-molecules-and]]
- [[wiki/sources/SRC-0059-six-open-questions-in-machine-learned-interatomic-potential]]
- [[wiki/sources/SRC-0060-ubio-molfm-universal-molecular-foundation-model]]
- [[wiki/sources/SRC-0065-mace-mdp-molecular-dipole-moments-polarizabilities]]
- [[wiki/sources/SRC-0057-overlay-databank-unlocks-data-driven-analyses-of-biomolecules]]
- [[wiki/concepts/overlay-databanks-for-biomolecular-simulation-data]]
- [[wiki/concepts/automated-force-field-training]]
- [[wiki/concepts/stability-aware-mlff-training]]
- [[wiki/concepts/machine-learned-interatomic-potential-foundation-models]]
- [[wiki/concepts/ubio-molfm-biological-molecular-foundation-model]]
- [[wiki/concepts/molecular-response-property-foundation-models]]
- [[wiki/claims/CLM-0014-dataset-scale-does-not-replace-coverage-validation]]
- [[wiki/claims/CLM-0015-molecular-datasets-have-distinct-intended-uses]]
- [[wiki/questions/mlip-foundation-model-validation-scope]]
- [[wiki/tensions/TEN-0008-dataset-scale-vs-downstream-validation]]

## Open Questions

- Which dataset properties best predict downstream simulation stability and thermodynamic accuracy, beyond energy/force MAE?
