---
type: source
status: active
created: 2026-09-18
updated: 2026-09-18
source_id: SRC-0091
display_title: "Supplementary Information for Training a force field for proteins and small molecules from scratch"
short_title: "Garnet Chemical Science Supplement"
aliases:
  - "SRC-0091"
  - "Garnet Supplement"
  - "Garnet Chemical Science SI"
source_path: raw/sources/SRC-0091-training-force-field-proteins-small-molecules-supplement.pdf
imported_path: raw/sources/SRC-0091-training-force-field-proteins-small-molecules-supplement.pdf
original_filename: "d6sc02874h2_suppl.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: db723477e4578643c5865ba627938ef0d86741308ccd40511f5533f4bdaf65c1
authors:
  - "Alexandre Blanco-González"
  - "Thea K. Schulze"
  - "Evianne Rovers"
  - "Joe G. Greener"
author_entities: []
year: 2026
venue: "Chemical Science supplementary information"
doi: "10.1039/D6SC02874H"
arxiv:
metadata_review_status: reviewed
source_bundle: garnet-training-force-field-from-scratch-2026
bundle_role: supplement
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/machine-learning/molecular-modeling
  - research/biomolecules/proteins
  - research/machine-learning/scientific-modeling
  - research/experimental-benchmarking
  - research/molecular-simulation/free-energy
tags:
  - garnet
  - supplementary-information
  - force-fields
  - rbfe
  - benchmark-tables
  - training-data
related:
  - "[[wiki/sources/SRC-0090-training-force-field-proteins-small-molecules]]"
  - "[[wiki/sources/SRC-0003-training-a-force-field-from-scratch]]"
  - "[[wiki/concepts/garnet-force-field]]"
  - "[[wiki/concepts/double-exponential-potential]]"
  - "[[wiki/concepts/relative-binding-free-energy-benchmarking]]"
  - "[[wiki/claims/CLM-0002-garnet-automates-parameter-assignment]]"
  - "[[wiki/questions/garnet-validation-scope]]"
  - "[[wiki/tensions/TEN-0002-garnet-broad-coverage-vs-validation-gaps]]"
sources:
  - SRC-0090
  - SRC-0091
cites_sources: []
citation_match_status: unchecked
cqt_review_status: linked
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: standard
peer_review_status: supplementary-material
---

# Supplementary Information for Training a Force Field for Proteins and Small Molecules from Scratch

Source ID: `SRC-0091`

## Raw source

- Repository path: `raw/sources/SRC-0091-training-force-field-proteins-small-molecules-supplement.pdf`
- Open raw source: [raw/sources/SRC-0091-training-force-field-proteins-small-molecules-supplement.pdf](../../raw/sources/SRC-0091-training-force-field-proteins-small-molecules-supplement.pdf)
- Main source: [[wiki/sources/SRC-0090-training-force-field-proteins-small-molecules]]

## Summary

The 12-page supplement supplies the embedding-space, parameter-distribution, dipole, condensed-phase, protein-complex, IDP, and RBFE figures and tables referenced from the main text, together with the full training-dataset weighting table and the training-loss progress plot. It is the source for the motif-enrichment tables, the small-molecule density/enthalpy-of-vapourisation numbers, the cmet RBFE failure, and the training-data composition. [SRC-0091]

## Embedding space and parameters

- SI Fig. 1: t-SNE projection of the 64-dimensional ubiquitin atom embeddings, annotated with the Amber14SB atom types found in different regions and the water atoms. [SRC-0091]
- SI Fig. 2: absolute partial-charge distribution for ubiquitin's 1,231 atoms. Garnet mean 0.33, median 0.19; Amber14SB mean 0.25, median 0.11, consistent with Garnet's over-polarised charges. [SRC-0091]
- SI Fig. 3: parameter-by-parameter comparison between Garnet and Amber14SB for ubiquitin (charges, $\sigma$, $\epsilon$, bond $k_b$/$r_0$, angle $k_a$/$\theta_0$). [SRC-0091]

## Small-molecule motif enrichment

SI Table 1 (lowest 1% structure-RMSD tier, i.e. well-described) lists pyrazole, aldehyde, thiol, pyrrole, phenol, carboxylic acid, indole, alkyne, diazo, fused aromatic, imidazole, fluorinated C, ketone, indazole, carboxylate, oxazole, imide, and azide with median enrichment and 95% bounds. [SRC-0091, Table 1]

SI Table 2 (highest 1% tier, i.e. poorly described) lists amide, tertiary amine, sulfonamide, quaternary amine, sulfone, aniline, ester, disulfide, pyrimidine, ether, alkene, nitrile, urea, indazole, isoxazole, oxazole, conjugated, sulfoxide, guanidine, enol, phosphonate, and enoxide. Complex nitrogen groups (amide, tertiary amine, sulfonamide, quaternary amine) fail for at least three methods, revealing a structure-RMSD bias that amplifies errors at flexible locations. [SRC-0091, Table 2]

## Condensed-phase small molecules

SI Table 3 reports ΔHv and density RMSE/Pearson's $r$ for GAFF, OpenFF-2.2.1, and Garnet on three training molecules and 12 independent test molecules. Garnet test ΔHv RMSE 4.29 [2.12, 6.12] kcal mol$^{-1}$ (Pearson $r$ 0.81) versus OpenFF 2.63 [0.48, 4.48] ($r$ 0.84); density RMSE 0.13 [0.11, 0.16] g mL$^{-1}$ ($r$ 0.93) versus OpenFF 0.041 [0.021, 0.058] ($r$ 0.99). Garnet trains on only three molecules (water, methanol, benzene). [SRC-0091, Table 3]

The 12 test molecules are butane, cyclohexane, 2-propanol, phenol, propane-1-thiol, acetic acid, acetone, N-methylpropanamide, trichloromethane, 4-methyl thiazole, fluorobenzene, and trimethylphosphate. [SRC-0090, Methods]

## Protein complexes and IDPs

- SI Fig. 6: monomer RMSD over time for the four protein complexes (barnase/barstar, CD2/CD58, colE7/Im7, SGPB/OMTKY3), for Garnet and Amber14SB. [SRC-0091]
- SI Fig. 7: radius-of-gyration densities for the four IDPs (drkN SH3, NTAIL, PaaA2, α-synuclein), showing Garnet over-compaction relative to experiment. [SRC-0091]

## RBFE supplementary results

- SI Fig. 8: calculated versus experimental ΔΔGbind for the eight protein systems (tyk2, cdk2, p38, mcl1, chk1, galectin, bace p3 arg368 in, t4 lysozyme). [SRC-0091]
- SI Table 4: cmet RBFE failure. Garnet pairwise RMSE 8.26 [7.74, 8.77] kcal mol$^{-1}$, Kendall's $\tau$ $-0.11$ [-0.36, 0.17], fraction of best ligands 0.16, versus OpenFE 1.99/0.63/0.55 and FEP+ 1.07/0.79/0.74. A single ligand transformation with a net charge change of 1 was poorly predicted, and that edge singly connected all charged to all uncharged ligands in the network. [SRC-0091, Table 4]
- SI Fig. 9: cmet calculated-versus-experimental ΔΔGbind, colour-coded by charge pair; ΔΔG between like-charged ligands were relatively well-predicted (Kendall's $\tau$ up to 0.63), while charge-changing pairs had large absolute deviations. [SRC-0091]

## Model variants and training data

- SI Fig. 10: ablation of neural-network hyperparameters (embedding dimension 8/64/128, layer count, GNN layer) and of MM functional-form components (removing harmonic bonds, angles, torsions, or van der Waals terms). Removing harmonic bonds, and to a lesser degree angles, greatly increased intramolecular force loss; removing torsions had little effect; removing van der Waals terms greatly increased intermolecular force loss. [SRC-0091]
- SI Table 5: DFT training datasets and weighting. Total 2,201,006 conformations, weighted to 4,013,229 conformations used, spanning SPICE subsets (dipeptides, solvated amino acids, DES370K, DES monomers, PubChem, amino-acid ligand, ion pairs, water clusters, boron/silicon, RNA), MACE-OFF water, and GEMS crambin. [SRC-0091, Table 5]
- SI Fig. 11: training-loss progress over 15 epochs; reference trajectories are used before epoch 6, then simulation-generated trajectories; the epoch-12 model is the final model. [SRC-0091]

## Limitations

- The cmet result is a specific, quantifiable failure mode tied to net-charge-changing alchemical transformations, not a general RBFE conclusion. [SRC-0091, Table 4]
- Motif-enrichment results depend on a structure-RMSD-centric tier definition that amplifies flexible-location errors. [SRC-0090]

## Ingestion QA

### Retrieval questions checked

- Which motifs are best and worst described by Garnet's small-molecule geometries?
- What are the exact condensed-phase ΔHv and density numbers?
- What quantitative evidence shows the cmet net-charge-change failure?
- Which training datasets and weightings were used?
- How do model-variant ablations attribute loss to each MM term?

### Coverage decision

`standard`. The supplement page records the tables, figures, and the cmet failure at retrieval-useful granularity without reproducing every table cell. Detailed per-motif numbers remain in the raw PDF.

### Known gaps

- Full SI Table 1/2 per-motif enrichment values and 95% bounds are not reproduced.
- Full SI Table 5 weighting rows are summarised, not reproduced verbatim.
- Figure-level visual content remains in the raw PDF.
