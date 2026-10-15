---
type: claim
status: active
created: 2026-10-12
updated: 2026-10-12
claim_status: supported
claim_scope: validation
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/machine-learning/molecular-modeling
  - research/experimental-benchmarking
tags:
  - claim
  - force-fields
  - validation
  - graph-neural-networks
  - nonbonded-parameters
  - energy-degeneracy
related:
  - "[[wiki/concepts/grappa-machine-learned-force-fields]]"
  - "[[wiki/concepts/espaloma-machine-learned-mm-force-fields]]"
  - "[[wiki/concepts/automated-force-field-training]]"
  - "[[wiki/claims/CLM-0032-gnn-mm-force-fields-need-downstream-simulation-validation]]"
sources:
  - SRC-0101
sensitivity: public
encryption: none
---

# grappa-fullFF Jointly Learns Nonbonded Parameters Without Degrading Bonded Accuracy

## Claim

With physics-informed regularization (matching the predicted electrostatic potential and per-atom effective-volume ratios to quantum-mechanical references), a single graph-attention model can learn both bonded and nonbonded molecular-mechanics parameters consistently from QM energies and forces alone, without externally assigned nonbonded parameters, and without measurably degrading the bonded-parameter (geometry-optimization) accuracy of its bonded-only predecessor. [SRC-0101]

## Evidence

- On the OpenFF Industry Benchmark Season 1 v1.1 geometry-optimization benchmark, `grappa-fullFF` (RMSE med 0.2661 Å, TFD med 0.0221, ddE MAE 1.589 kcal/mol) is nearly indistinguishable from its bonded-only predecessor `grappa-bonded` (0.2571 Å, 0.0232, 1.608 kcal/mol), and both outperform GAFF-2.11, OpenFF-2.1.0, and espaloma-0.3.2 on all three metrics. [SRC-0101, Table 2]
- Full cumulative distribution functions (not just medians/means) for RMSE, TFD, and |ddE| show the grappa-bonded and grappa-fullFF distributions nearly overlapping. [SRC-0101, Appendix A.2, Fig. 4]
- Without the ESP/charge regularizers, the implicitly learned nonbonded parameters are not physically meaningful (large ESP RMSE increase, mean-charge-magnitude ratio to MBIS only 0.74), showing the regularization is necessary, not merely helpful, to resolve the bonded/nonbonded energy-degeneracy ambiguity. [SRC-0101, Appendix B, Table 4]
- The predicted charges reproduce the QM electrostatic potential about as accurately as expensive MBIS electron-density partitioning, and more accurately than AM1-BCC or espaloma-charge, despite never being supervised against reference atomic charges directly. [SRC-0101, Table 1, Fig. 3]
- In 500 ns explicit-solvent MD of capped alanine dipeptide, grappa-fullFF reproduces the Ramachandran free-energy surface with a Jensen-Shannon divergence from AMBER99SB-ILDN of 0.0820 nats, about twice as close as espaloma-0.3.2 (0.1596 nats) and close to grappa-bonded (0.0691 nats), even though grappa-fullFF was trained only on gas-phase monomers and never on solvated or condensed-phase configurations. [SRC-0101, Table 3]

## Implementation Use

For graph-neural-network MM force-field training, jointly predicting nonbonded parameters is feasible without a separate empirical-parameter pipeline, provided the training loss includes physics-informed regularization terms (e.g., ESP matching, reference effective-volume/polarizability ratios) that are evaluated on a subset of configurations with available electron-density data; energy/force fitting alone leaves the bonded/nonbonded decomposition underconstrained. [SRC-0101]

## Caveats

- grappa-fullFF's dipeptide Ramachandran-FES divergence from AMBER99SB-ILDN (JS = 0.0820) is somewhat larger than grappa-bonded's (JS = 0.0691); the paper characterizes the difference as small ($\Delta$JS = 0.013 nats) but it is a measurable regression attributable to the jointly learned nonbonded parameters. [SRC-0101, Table 3]
- Generalization is validated only for gas-phase-trained small molecules, dipeptides, and one explicit-solvent peptide system; broader condensed-phase, larger-molecule, or more-delocalized-molecule generalization is explicitly left as future work. [SRC-0101, Discussion]
- This is a NeurIPS workshop paper, not yet peer-reviewed in a journal. [SRC-0101]

## Links

- [[wiki/sources/SRC-0101-learning-consistent-molecular-mechanics-force-fields-from-first]]
- [[wiki/concepts/grappa-machine-learned-force-fields]]
- [[wiki/concepts/espaloma-machine-learned-mm-force-fields]]
- [[wiki/concepts/automated-force-field-training]]
- [[wiki/claims/CLM-0032-gnn-mm-force-fields-need-downstream-simulation-validation]]
