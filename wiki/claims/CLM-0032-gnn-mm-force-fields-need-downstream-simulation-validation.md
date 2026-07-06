---
type: claim
status: active
created: 2026-07-02
updated: 2026-07-02
claim_status: supported
claim_scope: validation
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/machine-learning/molecular-modeling
  - research/computational-drug-discovery
tags:
  - claim
  - force-fields
  - validation
  - graph-neural-networks
related:
  - "[[wiki/concepts/espaloma-machine-learned-mm-force-fields]]"
  - "[[wiki/concepts/automated-force-field-training]]"
sources:
  - SRC-0072
  - SRC-0073
sensitivity: public
encryption: none
---

# GNN MM Force Fields Need Downstream Simulation Validation

## Claim

Graph-neural-network assignment of molecular-mechanics parameters can make force-field development more scalable, but validation must include downstream simulation observables because energy/force agreement with quantum chemistry does not by itself guarantee stable, transferable biomolecular simulations. [SRC-0072] [SRC-0073]

## Evidence

- SRC-0072 evaluates espaloma-0.3 beyond quantum-chemical energy/force RMSE, including small-molecule geometry preservation, peptide NMR scalar couplings, folded-protein NMR scalar couplings, Tyk2 MD, and protein-ligand binding free energies. [SRC-0072] [SRC-0073]
- The paper reports a sulfonamide geometry failure mode despite broad quantum-chemical performance improvements. [SRC-0072]
- Folded-protein benchmarks show slightly higher NMR scalar-coupling error and greater flexibility than ff14SB, indicating that conventional protein observables remain needed. [SRC-0072]
- The authors explicitly argue that condensed-phase property fitting and uncertainty quantification are future needs. [SRC-0072]

## Implementation Use

For ML-assisted MM force-field development, keep a validation ladder: train/test energy and force errors, geometry preservation, gas-phase torsion behavior, peptide and folded-protein observables, condensed-phase properties, free-energy benchmarks, and prospective system-specific checks. [SRC-0072]

## Links

- [[wiki/sources/SRC-0072-machine-learned-molecular-mechanics-force-fields-from-large]]
- [[wiki/sources/SRC-0073-supplementary-material-for-machine-learned-molecular-mechanics-force]]
- [[wiki/concepts/espaloma-machine-learned-mm-force-fields]]
