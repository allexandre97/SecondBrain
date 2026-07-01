---
type: concept
status: active
created: 2026-06-30
updated: 2026-06-30
areas:
  - research
categories:
  - research/molecular-simulation/free-energy
  - research/machine-learning/scientific-modeling
  - research/machine-learning/molecular-modeling
tags:
  - Boltzmann-generators
  - transfer-learning
  - scalability
  - materials
related:
  - "[[wiki/concepts/boltzmann-generators-equilibrium-sampling]]"
  - "[[wiki/concepts/free-energy-estimation]]"
  - "[[wiki/claims/CLM-0016-boltzmann-generators-need-overlap-and-reweighting-support]]"
  - "[[wiki/tensions/TEN-0009-boltzmann-generator-one-shot-sampling-vs-overlap-risk]]"
sources:
  - SRC-0037
  - SRC-0039
sensitivity: public
encryption: none
---

# Transferable and Scalable Boltzmann Generators

## Summary

Transferable and scalable Boltzmann generators try to amortize the cost of training a reweightable generative sampler across molecules, system sizes, thermodynamic states, or interaction parameters. SRC-0037 targets transfer across dipeptide chemical space; SRC-0039 targets scaling across crystalline materials system sizes using locality. [SRC-0037] [SRC-0039]

## Key Points

- Transfer across molecules requires molecular identity, atom type, topology, and chirality constraints to be represented well enough that generated samples remain valid for the target molecule. [SRC-0037]
- Flow matching and equivariant graph vector fields enable transferable continuous normalizing flows for small molecular systems. [SRC-0037]
- Scaling across material system size can exploit local environments, fixed neighbor counts, and displacement coordinates so the architecture does not depend on total atom count. [SRC-0039]
- Effective sample size is a central diagnostic because it measures whether reweighting can turn generated proposals into useful equilibrium estimates. [SRC-0037] [SRC-0039]
- Both transfer and scaling remain bounded by missing-state risk, architecture limitations, and the need for enough overlap with the target distribution. [SRC-0037] [SRC-0039]

## Links

- [[wiki/sources/SRC-0037-transferable-boltzmann-generators]]
- [[wiki/sources/SRC-0039-scalable-boltzmann-generators-for-equilibrium-sampling-of-large]]
- [[wiki/concepts/boltzmann-generators-equilibrium-sampling]]
- [[wiki/concepts/free-energy-estimation]]
- [[wiki/claims/CLM-0016-boltzmann-generators-need-overlap-and-reweighting-support]]
- [[wiki/tensions/TEN-0009-boltzmann-generator-one-shot-sampling-vs-overlap-risk]]

## Open Questions

- Can a single architecture preserve reweightable accuracy while scaling from small molecules or crystals to heterogeneous liquids, biomolecules, or chemically diverse materials?
