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
  - transferability
  - j-coupling
related:
  - "[[wiki/concepts/grappa-machine-learned-force-fields]]"
  - "[[wiki/concepts/espaloma-machine-learned-mm-force-fields]]"
  - "[[wiki/concepts/automated-force-field-training]]"
  - "[[wiki/claims/CLM-0032-gnn-mm-force-fields-need-downstream-simulation-validation]]"
  - "[[wiki/claims/CLM-0057-grappa-fullff-jointly-learns-nonbonded-parameters-without-degrading-bonded-accuracy]]"
sources:
  - SRC-0102
sensitivity: public
encryption: none
---

# Grappa Matches or Exceeds Espaloma Accuracy at MM Cost and Extends to New Chemistries

## Claim

A graph-attention network predicting only the bonded (bond, angle, dihedral, improper) parameters of a classical MM force field, while consuming externally assigned nonbonded parameters as an input feature, achieves energy/force accuracy competitive with or exceeding a comparable graph-neural-network force field that also learns nonbonded assignment (Espaloma), substantially exceeds traditional hand-typed force fields, extends with modest additional data to out-of-training-distribution chemistry (peptide radicals) without degrading accuracy on the original domain, and reproduces downstream experimental and MD observables (protein *J*-couplings, folding free energy, large-scale MD stability) at the same computational cost as conventional molecular mechanics. [SRC-0102]

## Evidence

- On the shared Espaloma-0.3 test partition (17,427 molecules, >1,000,000 conformations across small molecules, peptides, and RNA), Grappa matches or beats Espaloma-0.3 on energy and force RMSE for nearly every dataset, and both substantially outperform traditional force fields GAFF-2.11, ff99SB-ILDN/ff14SB, and RNA.OL3 (e.g. SPICE-PubChem force RMSE: Grappa 6.1, Espaloma 6.8, Gaff-2.11 14.6 kcal/mol/Å). [SRC-0102, Table 1]
- Trained on a purpose-built peptide-radical dataset, Grappa learns accurate bonded parameters for hydrogen-atom-transfer radicals (energy RMSE 3.1 kcal/mol, force RMSE 8.5 kcal/mol/Å vs. a 7.0/40.6 mean predictor) while its accuracy on the original (non-radical) Espaloma-derived test sets is essentially unchanged by the radical-data extension (Table 8 vs. Table 7), and it reproduces radical-induced Cα planarity (0.05 Å RMSD to QM-optimized geometry). [SRC-0102, Table 2, Table 8, Fig. 5]
- Grappa reproduces experimental *J*-couplings for 13 small peptides better than both Espaloma-0.3 and Amber ff14SB ($\chi^2=1.19\pm0.20$, RMSE $=0.46$ Hz, vs. Espaloma's $1.43\pm0.21$/$0.50$ Hz and ff14SB's $2.60\pm0.51$/$0.63$ Hz). [SRC-0102, Fig. 9]
- Grappa keeps a folded protein (ubiquitin) and a one-million-atom virus particle (STMV) stable over hundreds of nanoseconds and tens of nanoseconds of MD respectively, and recovers a chignolin-variant folding free energy ($-3.0\,k_BT$) closer to the experimental reference than a comparable traditional-force-field simulation reported elsewhere ($-4.0\,k_BT$). [SRC-0102, Figs. 7, 8, 14]
- Because Grappa evaluates parameters once per molecule and reuses the standard MM energy functional, it runs at ~101 timesteps/second for the one-million-atom STMV system on a single A100 GPU, contrasted with a published figure of 106 timesteps/second for a similarly sized system using the E(3)-equivariant Allegro potential, which required 4000 A100 GPUs — an approximate three-order-of-magnitude efficiency advantage for Grappa, though the comparison is not a matched, controlled benchmark. [SRC-0102, Sec. 3.5]

## Implementation Use

For MM force-field development, learning only the bonded parameters via a permutation-equivariant graph-attention architecture (holding nonbonded assignment fixed to an existing scheme, passed in as an input feature) is sufficient to reach or exceed the accuracy of a fully learned (bonded+nonbonded) alternative on gas-phase QM benchmarks, while remaining trivially swappable between different nonbonded parameter sets (AM1-BCC, ff99SB, CHARMM36) at closely matched accuracy; this decouples bonded-parameter learning from nonbonded-scheme choice. [SRC-0102]

## Caveats

- Grappa is somewhat less accurate than Espaloma for *energies* specifically on several datasets even though more accurate for *forces*; the paper frames the two as "competitive," not Grappa as uniformly superior. [SRC-0102, Sec. 3.1]
- Grappa's accuracy is bounded by the quality of whichever externally assigned nonbonded parameters it is paired with; it does not address nonbonded-parameter error itself (that limitation motivated the later `grappa-fullFF` extension; see [[wiki/claims/CLM-0057-grappa-fullff-jointly-learns-nonbonded-parameters-without-degrading-bonded-accuracy]]). [SRC-0102] [SRC-0101]
- On the out-of-distribution 3BPA dihedral benchmark, zero-shot Grappa performs only similarly to (not clearly better than) GAFF-2.11; meaningful improvement needs a small amount of targeted finetuning data. [SRC-0102, Sec. 4.4]
- The efficiency comparison against Allegro uses published numbers from different studies/hardware configurations rather than a matched, controlled benchmark. [SRC-0102, Sec. 3.5]

## Links

- [[wiki/sources/SRC-0102-grappa-a-machine-learned-molecular-mechanics-force-field]]
- [[wiki/concepts/grappa-machine-learned-force-fields]]
- [[wiki/concepts/espaloma-machine-learned-mm-force-fields]]
- [[wiki/concepts/automated-force-field-training]]
- [[wiki/claims/CLM-0032-gnn-mm-force-fields-need-downstream-simulation-validation]]
- [[wiki/claims/CLM-0057-grappa-fullff-jointly-learns-nonbonded-parameters-without-degrading-bonded-accuracy]]
