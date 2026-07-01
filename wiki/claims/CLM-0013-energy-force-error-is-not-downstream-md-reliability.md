---
type: claim
status: active
created: 2026-07-01
updated: 2026-07-01
claim_status: limited
claim_scope: cross-source
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/machine-learning/molecular-modeling
  - research/experimental-benchmarking
tags:
  - claim
  - machine-learning-potentials
  - validation
  - molecular-dynamics
related:
  - "[[wiki/concepts/machine-learned-interatomic-potential-foundation-models]]"
  - "[[wiki/concepts/machine-learning-potential-datasets]]"
  - "[[wiki/questions/mlip-foundation-model-validation-scope]]"
  - "[[wiki/claims/CLM-0011-stability-aware-mlff-training-targets-md-stability]]"
sources:
  - SRC-0042
  - SRC-0059
  - SRC-0060
  - SRC-0065
  - SRC-0066
sensitivity: public
encryption: none
---

# Energy/Force Error Is Not Downstream MD Reliability

## Claim

Low energy or force error is useful but insufficient evidence for downstream molecular-dynamics reliability; validation must also check the downstream observables, system classes, timescales, and failure modes where the model will be used. [SRC-0042] [SRC-0059] [SRC-0060]

## Scope

This claim covers MLIP datasets, foundation-model MLIPs, response-property models coupled to MLIPs, and MLP-driven force-field fitting workflows. It does not imply that every source performs full downstream validation. [SRC-0042] [SRC-0059] [SRC-0065] [SRC-0066]

## Evidence

- OMol25 includes domain-informed evaluation tasks because random energy/force metrics alone do not show practical chemistry usefulness. [SRC-0042]
- SRC-0059 argues that foundation-model MLIPs need pragmatic downstream tasks and representational diagnostics rather than single-metric benchmark dominance. [SRC-0059, section 6]
- UBio-MolFM reports short downstream MD tests after static energy/force tests and still identifies longer trajectories, larger systems, protein-ligand binding, and nucleic-acid coverage as future validation needs. [SRC-0060, sections 2-3]
- MACE-MDP shows that spectroscopy quality can be limited by the underlying MLIP's force and frequency errors even when the response-property model is part of the workflow. [SRC-0065]
- `presto` improves several torsion and conformer metrics but does not establish broad RBFE superiority over existing OpenFF parameters. [SRC-0066]

## Caveats

- Downstream validation is task-specific; a test that is persuasive for small-molecule conformers may not validate proteins, nucleic acids, long trajectories, reactive events, or condensed-phase observables. [SRC-0059] [SRC-0060]

## Links

- [[wiki/sources/SRC-0042-the-open-molecules-2025-omol25-dataset-evaluations-and]]
- [[wiki/sources/SRC-0059-six-open-questions-in-machine-learned-interatomic-potential]]
- [[wiki/sources/SRC-0060-ubio-molfm-universal-molecular-foundation-model]]
- [[wiki/sources/SRC-0065-mace-mdp-molecular-dipole-moments-polarizabilities]]
- [[wiki/sources/SRC-0066-presto-bespoke-smirnoff-force-fields-mlps]]
- [[wiki/questions/mlip-foundation-model-validation-scope]]
