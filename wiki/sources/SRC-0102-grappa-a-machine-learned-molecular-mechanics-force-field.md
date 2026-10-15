---
type: source
status: active
created: 2026-10-12
updated: 2026-10-12
source_id: SRC-0102
display_title: "Grappa - a machine learned molecular mechanics force field"
short_title: "grappa-bonded"
aliases:
  - "SRC-0102"
  - "grappa-bonded"
  - "Grappa – a machine learned molecular mechanics force field"
source_path: raw/sources/SRC-0102-grappa-a-machine-learned-molecular-mechanics-force-field.pdf
imported_path: raw/sources/SRC-0102-grappa-a-machine-learned-molecular-mechanics-force-field.pdf
original_filename: "d4sc05465b.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 11b360b9e339dbe345b62c0b2b66f82363d795154508a86e351d7c84b216313b
authors:
  - "Leif Seute"
  - "Eric Hartmann"
  - "Jan Stühmer"
  - "Frauke Gräter"
author_entities: []
year: 2025
venue: "Chemical Science (Royal Society of Chemistry), vol. 16, pp. 2907-2930"
doi: "10.1039/d4sc05465b"
arxiv:
metadata_review_status: reviewed
source_bundle:
bundle_role: main
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/machine-learning/molecular-modeling
  - research/machine-learning/scientific-modeling
  - research/experimental-benchmarking
tags:
  - force-fields
  - molecular-mechanics
  - graph-neural-networks
  - grappa
  - bonded-parameters
  - transformer
  - benchmark
  - protein-folding
  - j-coupling
related:
  - "[[wiki/concepts/grappa-machine-learned-force-fields]]"
  - "[[wiki/concepts/espaloma-machine-learned-mm-force-fields]]"
  - "[[wiki/concepts/automated-force-field-training]]"
  - "[[wiki/concepts/garnet-force-field]]"
  - "[[wiki/sources/SRC-0101-learning-consistent-molecular-mechanics-force-fields-from-first]]"
  - "[[wiki/sources/SRC-0072-machine-learned-molecular-mechanics-force-fields-from-large]]"
  - "[[wiki/sources/SRC-0098-graph-nets-partial-charge-prediction]]"
sources:
  - SRC-0102
cites_sources:
  - SRC-0072
citation_match_status: partial
cqt_review_status: linked
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: math-standard
peer_review_status: peer-reviewed
---

# Grappa - a Machine Learned Molecular Mechanics Force Field

Source ID: `SRC-0102`

## Raw source

- Repository path: `raw/sources/SRC-0102-grappa-a-machine-learned-molecular-mechanics-force-field.pdf`
- Open raw source: [raw/sources/SRC-0102-grappa-a-machine-learned-molecular-mechanics-force-field.pdf](../../raw/sources/SRC-0102-grappa-a-machine-learned-molecular-mechanics-force-field.pdf)

## Status note

This is the original, peer-reviewed Grappa paper (Chemical Science, received 14 August 2024, accepted 13 December 2024, published 15 January 2025, licensed CC-BY-NC 4.0). It introduces the model referred to elsewhere in SecondBrain as `grappa-bonded`, which [[wiki/sources/SRC-0101-learning-consistent-molecular-mechanics-force-fields-from-first]] (the `grappa-fullFF` workshop paper, ingested 2026-10-12) cites extensively as its prior work (ref. 23) but which was, until this ingestion, not itself ingested in SecondBrain. [SRC-0102]

## Summary

Seute, Hartmann, Stühmer, and Gräter introduce Grappa (Graph Attentional Protein Parametrization), a graph-attention neural network that predicts the **bonded** molecular-mechanics (MM) parameters (bond, angle, torsion, and improper-dihedral force constants and equilibrium values) of a classical force field directly from the 2D molecular graph, replacing hand-crafted atom-typing rules with a learned, permutation-equivariant parametrization. Nonbonded (partial-charge and Lennard-Jones) parameters are not predicted by Grappa; they are taken from an existing traditional or machine-learned force field and passed to Grappa as an input feature, so that bonded parameters can be learned consistently with whatever nonbonded scheme is already in use. The resulting force field is incorporated into GROMACS and OpenMM at the same computational cost as traditional MM force fields, and the paper reports state-of-the-art energy/force accuracy against Espaloma and traditional force fields, extensibility to peptide radicals, reproduction of experimental *J*-couplings and protein free-energy landscapes, and large-scale MD stability up to a one-million-atom virus particle. [SRC-0102]

## Key Points

- **Architecture (two-stage).** Grappa first computes $d$-dimensional atom embeddings $\nu = \{\nu_i \in \mathbb{R}^d \mid i \in \mathcal{V}\}$ from the molecular graph $\mathcal{G}=(\mathcal{V}, \mathcal{E})$ using a graph attentional neural network (GAT-style, local/neighbor-only attention, inspired by the Graph Transformer Network but omitting Laplacian-eigenvector positional encoding). Four such layers are used ($L_{\mathrm{GNN}}=4$, hidden dimension 512, 16 attention heads, embedding dimension 256). Then, for each interaction type $l \in \{\text{bonds, angles, torsions, impropers}\}$, a "symmetric transformer" $\psi^{(l)}$ maps the embeddings of the atoms in that interaction's subgraph to the respective MM parameters, $\xi_{ij\ldots}^{(l)} = \psi^{(l)}(\nu_i, \nu_j, \ldots)$. [SRC-0102, Sec. 2, Fig. 1]
- **Permutation symmetry.** The bonded energy contributions must be invariant under the isomorphisms of their respective subgraph (bonds: $ij \leftrightarrow ji$; angles: $ijk \leftrightarrow kji$; torsions: $ijkl \leftrightarrow lkji$), so Grappa enforces parameter invariance under these permutations directly (eqns 6-8). Improper dihedrals are not invariant under all six permutations that leave the central atom fixed, so Grappa instead predicts **two** improper force constants per improper and combines them (eqns 39-41) so the resulting energy is invariant, solving the problem by decomposing the improper term rather than by invariant pooling alone. [SRC-0102, Sec. 2.1, A.4]
- **Symmetric transformer mechanism.** The "symmetric transformer" (Fig. 2) adds a permutation-invariant positional encoding to the node features that is invariant under the required symmetry group but can still break other, unwanted symmetries (eqn 9, e.g. for angles: $(\nu_i,\nu_j,\nu_k)\mapsto(\nu_i\oplus 0,\ \nu_j\oplus 1,\ \nu_k\oplus 0)$, distinguishing the central atom but not $i$ from $k$). Equivariant transformer layers (multi-head dot-product attention, feed-forward, residual connections, layer norm) process the positionally-encoded node set, and a final symmetric pooling operation sums an MLP evaluated over every permutation $\sigma$ in the target symmetry group $\mathcal{P}$ (eqn 10), $z_{ij\ldots} = \sum_{\sigma \in \mathcal{P}} \mathrm{MLP}([\nu_{\sigma(i)}, \nu_{\sigma(j)}, \ldots])$. [SRC-0102, Sec. 2.1-2.2, Fig. 2]
- **Output scaling.** Parameter scores $z$ are mapped to physically sensible ranges (e.g. $(0,\infty)$ for force constants, $(0,\pi)$ for equilibrium angles) using scaled/shifted ELU (`ToPos`) and sigmoid (`ToRange`) functions chosen so that an approximately-standard-normal score distribution maps to an output distribution with a target mean/std matched to a traditional force field's parameter statistics; dihedral force constants additionally pass through a sigmoid gate (eqn 34) so the model can suppress unneeded periodicities. [SRC-0102, Sec. 2.2, A.2.3]
- **Input features.** Grappa's input node features are deliberately minimal: one-hot atomic number, one-hot loop membership (ring size up to 8), node degree, and the partial charge received from whatever traditional/ML nonbonded scheme is paired with Grappa (a scalar value plus a 16-dimensional binning in $[-2e, 2e]$), so that bonded parameters stay consistent with the nonbonded assignment used. No hand-crafted hybridization or aromaticity features are used. [SRC-0102, Sec. 2.2, A.2.1]
- **Training loss.** Grappa minimizes a weighted sum of energy and force MSE against QM references, plus (during an initial 2-epoch pretraining phase only, then phased out) a deviation term from a traditional force field's bonded parameters, and an $L_2$ regularizer on dihedral force constants (eqn 11): $\mathscr{L} = \mathrm{MSE}(E, E_{\mathrm{QM}}) + \lambda_F\,\mathrm{MSE}(\nabla_{\mathbf{x}}E, \nabla_{\mathbf{x}}E_{\mathrm{QM}}) + \lambda_{\mathrm{MM}}\,\mathrm{MSE}(\xi, \xi_{\mathrm{trad}}) + \lambda_{\mathrm{dih}}\lVert \xi^{(\mathrm{dih})}\rVert_2^2$. Training on forces (not just energies) is motivated both because forces are local/more numerous (factor of $3N$) and because matching derivatives has previously been shown to smooth and improve generalization. [SRC-0102, Sec. 2.3]
- **State-of-the-art accuracy.** Trained and evaluated on the same partition of the Espaloma-0.3 dataset (17,427 molecules, >1 million conformations: SPICE-PubChem, SPICE-DES-Monomers, SPICE-Dipeptide small molecules/peptides, and RNA-Diverse/RNA-Trinucleotide), Grappa matches or outperforms Espaloma on energy/force RMSE across nearly all subsets and substantially outperforms traditional force fields GAFF-2.11, ff99SB-ILDN, and RNA.OL3 (Table 1). Grappa is reported as more accurate for forces and somewhat less accurate for energies than Espaloma. [SRC-0102, Sec. 3.1, Table 1]
- **Extensibility to new chemistry (peptide radicals).** Because Grappa's only input features are connectivity, atomic number, and partial charge (no hand-crafted hybridization/aromaticity features that would need re-deriving), it generalizes to chemical space outside its training distribution with modest additional data. Trained on a purpose-built radical-peptide dataset (hydrogen-atom-transfer radicals, BMK/6-311+G(2df,p) QM via Psi4), Grappa learns accurate parameters for peptide radicals (Table 2) without degrading its accuracy on the original Espaloma datasets (Table 8), and reproduces radical-induced planarity around the C$_\alpha$ atom (Fig. 5, 0.05 Å RMSD to QM-optimized geometry). To the authors' knowledge, Grappa is the first MM force field covering this part of chemical space. [SRC-0102, Sec. 3.2, A.5.2]
- **Compatibility with multiple nonbonded schemes.** Because Grappa takes partial charges as an input feature rather than hard-coding a specific nonbonded scheme, it can be retrained to be consistent with different nonbonded parameter sets (AM1-BCC/OpenFF-2.0.0, ff99SB, CHARMM36) at closely matched accuracy (Table 3), enabling drop-in use in existing workflows where proteins are already parametrized with ff99SB or CHARMM36 (only the bonded topology is overwritten). [SRC-0102, Sec. 3.3, Table 3]
- **Reproduces dihedral free-energy landscapes without CMAPs.** Relaxed backbone dihedral scans (implicit solvent, Ace-Ala-Nme) show Grappa reproduces the diagonal $\alpha_R$ helix basin shape at $(\phi,\psi)=(-80°,-20°)$ and the $\alpha$-helix/$\beta$-sheet transition minimum at $(-90°, 80°)$ seen in Amber ff19SB, *without* requiring the residue-specific CMAP correction maps that ff19SB needed to fit the same QM profile; Grappa achieves this by jointly tuning dihedral, angle, and some neighboring-bond/nonbonded contributions together rather than fitting each term separately, which the paper frames as a general advantage of learning all bonded parameters jointly (shown via a per-term energy decomposition, Fig. 16). [SRC-0102, Sec. 3.4, Fig. 6, A.6]
- **Interpretability and latent space.** Despite having no hand-crafted chemical features, a 2D PCA of Grappa's learned atom embeddings recovers a periodic-table-like structure, with principal components corresponding approximately to main group and period (Fig. 4c), indicating Grappa implicitly learns chemically meaningful atom types from energies and forces alone. [SRC-0102, Sec. 3.1]
- **Tabulated Grappa variant.** To provide a conventional, fixed-parameter force field for comparison/trust purposes, the authors extract a tabulated protein force field from Grappa by parametrizing a systematic set of capped di/tripeptides (BLXLZ / BLX / XLZ / BLZ sequences spanning all natural amino acids, protonation states, hydroxyproline, DOPA, and Ace/Nme caps) and assigning per-residue, context-independent bonded parameters; this tabulated variant reaches 2.6 kcal/mol energy RMSE and 6.0 kcal/mol/Å force RMSE on a 300 K dipeptide test set, close to full (context-dependent) Grappa, indicating that Grappa's larger 7-bond field of view has only a marginal benefit for this task. [SRC-0102, Sec. 3.7, A.7, Fig. 15]
- **Efficiency.** Grappa evaluates parameters once per molecule (not per conformation), inheriting MM's computational cost; a one-million-atom simulation of the satellite tobacco mosaic virus (STMV, proteins + RNA) in solution achieves 101 timesteps/second on a single A100 GPU in GROMACS, which the authors contrast with Allegro (an E(3)-equivariant neural network potential), reported at 106 timesteps/second but requiring 4000 A100 GPUs for a comparable system size — framed as "more than three orders of magnitude higher efficiency" for Grappa. [SRC-0102, Sec. 3.5, Fig. 14]
- **Finetuning for out-of-distribution dihedral landscapes.** On the drug-like 3-(benzyloxy)pyridin-2-amine (3BPA) dataset (not in Grappa's training data, used elsewhere to test the E(3)-equivariant model MACE's extrapolation), zero-shot Grappa performs similarly to GAFF-2.11, but finetuning on a handful (10) of states from a relaxed dihedral slice substantially improves agreement with QM on that and nearby slices (Table 6, Figs. 10/17/18), demonstrating Grappa can be incrementally corrected for challenging torsional landscapes. [SRC-0102, Sec. 4.4, A.9]

## Evidence

**Table 1 — Accuracy of Grappa, Espaloma-0.3, and established MM force fields on the Espaloma test set** (RMSE of centered energies in kcal/mol, componentwise RMSE of forces in kcal/mol/Å; nonbonded contributions from AM1-BCC/OpenFF-2.0.0; uncertainties in Table 7):

| Dataset | Test mols | Confs | Metric | Grappa | Espaloma | Gaff-2.11 | ff99SB, RNA.OL3 | Mean predictor |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SPICE-PubChem | 1411 | 60 853 | Energy | 2.3 | 2.3 | 4.6 | — | 18.4 |
| | | | Force | 6.1 | 6.8 | 14.6 | — | 23.4 |
| SPICE-DES-Monomers | 39 | 2032 | Energy | 1.3 | 1.4 | 2.5 | — | 8.2 |
| | | | Force | 5.2 | 5.9 | 11.1 | — | 21.3 |
| SPICE-Dipeptide | 67 | 2592 | Energy | 2.3 | 3.1 | 4.5 | 4.6 | 18.7 |
| | | | Force | 5.4 | 7.8 | 12.9 | 12.1 | 21.6 |
| RNA-Diverse | 6 | 357 | Energy | 3.3 | 4.2 | 6.5 | 6.0 | 5.4 |
| | | | Force | 3.7 | 4.4 | 16.7 | 19.4 | 17.1 |
| RNA-Trinucleotide | 64 | 35 811 | Energy | 3.5 | 3.8 | 5.9 | 6.1 | 5.3 |
| | | | Force | 3.6 | 4.3 | 17.1 | 19.7 | 17.7 |

[SRC-0102, Table 1]

**Table 2 — Ablation study on extensibility to peptide radicals** (RMSE in kcal/mol/Å unless noted; "Grappa" = trained on radical dataset + original dataset; "Grappa-radicals" column header per source is the comparison with/without radical training — transcribed as printed):

| | Grappa-radicals | Grappa | Mean predictor |
| --- | --- | --- | --- |
| Energy RMSE | 3.1 ± 0.3 | 4.1 ± 0.3 | 7.0 ± 0.5 |
| Force RMSE | 8.5 ± 0.2 | 13.6 ± 0.3 | 40.6 ± 1.2 |

Note: per the source caption, "Grappa-radicals" is Grappa trained including the extended radical-peptide dataset, and "Grappa" is Grappa trained only on the original (non-radical) dataset and evaluated on the radical test set — i.e. the comparison isolates the benefit of training on radical data. [SRC-0102, Table 2]

**Table 3 — Ablation study on different nonbonded parameter schemes** (SPICE-Dipeptide dataset; RMSE in kcal/mol / kcal/mol/Å; "Grappa" = trained on the Espaloma dataset (Grappa-base in the column header); "Grappa-base" per the source column header is the extension including peptide nonbonded contributions from ff99SB and CHARMM36 — transcribed as printed):

| Nonbonded parameters | Metric | Grappa | Grappa-base |
| --- | --- | --- | --- |
| AM1BCC | Energy | 2.4 ± 0.1 | 2.4 ± 0.1 |
| | Force | 5.5 ± 0.1 | 5.6 ± 0.1 |
| ff99SB | Energy | 2.3 ± 0.1 | 2.6 ± 0.1 |
| | Force | 5.5 ± 0.1 | 6.1 ± 0.1 |
| CHARMM36 | Energy | 2.5 ± 0.1 | 3.1 ± 0.1 |
| | Force | 5.5 ± 0.1 | 6.4 ± 0.1 |

[SRC-0102, Table 3]

**Table 4 — Ablation study for different learnable bonded interactions** (dipeptides at 300 K with ff99SB partial charges; non-learnable interaction types take parameters from ff99SB-ILDN; RMSE in kcal/mol / kcal/mol/Å):

| Bond | Angle | Dihedral | Energy RMSE | Force RMSE |
| --- | --- | --- | --- | --- |
| ✓ | ✓ | ✓ | 2.5 | 5.9 |
| ✓ | ✓ | | 3.0 | 6.1 |
| ✓ | | | 3.9 | 7.4 |
| | | ✓ | 3.8 | 9.2 |
| | | | 3.5 | 11.0 |
| | | | 4.1 | 11.8 |

Note: the source table has six rows combining bond/angle/dihedral learnability flags; the last two rows (both blank in all three columns per the extracted layout) likely correspond to additional non-learnable-parameter baselines not fully disambiguated in the extracted text; treat the bottom two rows' exact configuration as uncertain. [SRC-0102, Table 4]

**Table 5 — Hyperparameters used for training Grappa**:

| Hyperparameter | Variable | Value |
| --- | --- | --- |
| GNN layers | $L_{\mathrm{GNN}}$ | 4 |
| GNN hidden dimension | $d$ | 512 |
| GNN attention heads | $N_{\mathrm{heads}}$ | 16 |
| GNN embedding dimension | $d_{\mathrm{emb}}$ | 256 |
| GNN dropout probability | | 0.3 |
| Transformer layers | $L_{\mathrm{T}}$ | 1 |
| Transformer hidden dim | $d_{\mathrm{T}}$ | 512 |
| Transformer attention heads | $N_{\mathrm{T\text{-}heads}}$ | 8 |
| Pooling layers | $L_{\mathrm{pool}}$ | 3 |
| Pooling hidden dim | $d_{\mathrm{pool}}$ | 256 |
| Transformer dropout probability | | 0.5 |
| Learning rate | | $10^{-5}$ |
| Molecules per batch | | 32 |
| States per molecule | | 32 |
| Force weight | $\lambda_F$ | 0.8 |
| Dihedral $L_2$ weight | $\lambda_{\mathrm{dih}}$ | 1 |
| Traditional MM weight | $\lambda_{\mathrm{trad}}$ | 0 (after 100-epoch pretraining phase; $10^{-3}$ during it) |
| Torsion periodicities | | {1, 2, 3} |
| Improper periodicities | | {2} |

Optimizer: Adam, $\epsilon=10^{-8}$, $\beta_1=0.9$, $\beta_2=0.999$; 1000 epochs on the Espaloma dataset (~25 hours on an A100 GPU); validation loss is a weighted (1:3 energy:force) average RMSE across the Table 1 sub-datasets, used for early stopping and learning-rate scheduling. [SRC-0102, Table 5, A.3]

**Table 6 — Finetuning on the 3BPA dataset** (Energy/Force RMSE in kcal/mol and kcal/mol/Å; "Grappa" trained on the extended Espaloma dataset; "Grappa-finetuned" additionally finetuned on 300 K training states plus 10 states from the $\beta=150°$ slice; "Grappa-finetuned-300K" finetuned only on the 300 K states):

| Dataset | Confs | Metric | Gaff-2.11 | Grappa | Grappa-finetuned | Grappa-finetuned-300K |
| --- | --- | --- | --- | --- | --- | --- |
| Slice $\beta=180°$ | 2350 | Energy | 3.1 | 2.7 | **2.5** | 2.6 |
| | | Force | 11.8 | 7.1 | **4.2** | 4.4 |
| Slice $\beta=150°$ | 2350 | Energy | 1.3 | 1.0 | **0.7** | 0.9 |
| | | Force | 11.1 | 6.3 | **2.6** | 2.9 |
| Slice $\beta=120°$ | 2347 | Energy | 1.4 | 1.3 | **1.1** | 1.2 |
| | | Force | 10.7 | 6.0 | **3.2** | 3.5 |
| Test 300 K | 1669 | Energy | 3.1 | 1.7 | **1.2** | 1.2 |
| | | Force | 12.8 | 8.1 | 5.4 | **5.4** |
| Test 600 K | 2138 | Energy | 4.4 | 2.7 | 2.4 | **2.3** |
| | | Force | 14.2 | 9.9 | 8.1 | **8.1** |
| Test 1200 K | 2139 | Energy | 8.5 | 6.7 | 6.5 | **6.4** |
| | | Force | 19.4 | 16.3 | 14.9 | **14.7** |

[SRC-0102, Table 6]

**Table 7 — Accuracy of Grappa, Espaloma-0.3, and established MM force fields, with bootstrapped uncertainties (1000 resamples), including torsion-scan and optimization-trajectory test sets** (RMSE of molwise-centered energies in kcal/mol; componentwise RMSE of forces in kcal/mol/Å):

*Boltzmann sampled*

| Dataset | Test mols | Confs | Metric | Grappa | Espaloma | Gaff-2.11 | ff14SB, RNA.OL3 | Mean predictor |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SPICE-PubChem | 1411 | 60 853 | Energy | 2.3 ± 0.1 | 2.3 ± 0.1 | 4.6 | — | 18.4 |
| | | | Force | 6.1 ± 0.3 | 6.8 ± 0.1 | 14.6 | — | 23.4 |
| SPICE-DES-Monomers | 39 | 2032 | Energy | 1.3 ± 0.1 | 1.4 ± 0.3 | 2.5 | — | 8.2 |
| | | | Force | 5.2 ± 0.2 | 5.9 ± 0.5 | 11.1 | — | 21.3 |
| SPICE-Dipeptide | 67 | 2592 | Energy | 2.3 ± 0.1 | 3.1 ± 0.1 | 4.5 | 4.6 | 18.7 |
| | | | Force | 5.4 ± 0.1 | 7.8 ± 0.2 | 12.9 | 12.1 | 21.6 |
| RNA-Diverse | 6 | 357 | Energy | 3.3 ± 0.1 | 4.2 ± 0.3 | 6.5 | 6.0 | 5.4 |
| | | | Force | 3.7 ± 0.1 | 4.4 ± 0.1 | 16.7 | 19.4 | 17.1 |
| RNA-Trinucleotide | 64 | 35 811 | Energy | 3.5 ± 0.1 | 3.8 ± 0.2 | 5.9 | 6.1 | 5.3 |
| | | | Force | 3.6 ± 0.1 | 4.3 ± 0.1 | 17.1 | 19.7 | 17.7 |

*Torsion scan*

| Dataset | Test mols | Confs | Metric | Grappa | Espaloma | Gaff-2.11 | Mean predictor |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gen2-Torsion | 131 | 21 890 | Energy | 1.7 ± 0.2 | **1.6 ± 0.3** | 2.7 | 4.7 |
| | | | Force | 4.0 ± 0.4 | 4.7 ± 0.6 | 9.4 | 5.5 |
| Protein-Torsion | 9 | 6624 | Energy | 2.2 ± 0.4 | **1.9 ± 0.2** | 3.0 | 3.5 |
| | | | Force | 3.8 ± 0.5 | 3.5 ± 0.3 | 9.7 | 5.1 |

*Optimization*

| Dataset | Test mols | Confs | Metric | Grappa | Espaloma | Gaff-2.11 | ff14SB | Mean predictor |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gen2-Opt | 154 | 40 055 | Energy | 1.8 ± 0.1 | **1.7 ± 0.5** | 3.0 | — | 3.9 |
| | | | Force | 3.8 ± 0.1 | 4.5 ± 0.8 | 9.7 | — | 5.1 |
| Pepconf-Opt | 55 | 14 884 | Energy | 3.2 ± 0.3 | **2.8 ± 0.3** | 5.1 | 4.1 | 6.3 |
| | | | Force | 3.6 ± 0.2 | 4.0 ± 0.4 | 10.2 | 10.2 | 5.3 |

[SRC-0102, Table 7]

**Table 8 — Accuracy of Grappa (trained on the Espaloma dataset extended with peptide radicals, plus SPICE-Dipeptide/Protein-Torsion with ff99SB and CHARMM36 nonbonded contributions) vs. Espaloma-0.3, Gaff-2.11, and ff99SB-ILDN on unseen test molecules** (bootstrapped 1000x; RMSE of molwise-centered energies in kcal/mol, componentwise RMSE of forces in kcal/mol/Å; parenthetical dataset names denote the nonbonded scheme used; openff-2.0.0/AM1-BCC used where unspecified):

| Dataset | Test mols | Confs | Metric | Grappa | Espaloma | Gaff-2.11 | ff99SB-ILDN | Mean predictor |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SPICE-PubChem | 1411 | 60 853 | Energy | 2.3 ± 0.1 | 2.3 ± 0.1 | 4.6 ± 0.1 | — | 18.8 |
| | | | Force | 6.1 ± 0.3 | 6.8 ± 0.3 | 14.6 ± 0.3 | — | 41.3 |
| SPICE-DES-Monomers | 39 | 2032 | Energy | 1.3 ± 0.1 | 1.4 ± 0.3 | 2.5 ± 0.2 | — | 8.6 |
| | | | Force | 5.3 ± 0.2 | 5.9 ± 0.5 | 11.1 ± 0.6 | — | 37.4 |
| SPICE-Dipeptide | 67 | 2592 | Energy | 2.4 ± 0.1 | 3.1 ± 0.1 | 4.5 ± 0.1 | — | 19.1 |
| | | | Force | 5.6 ± 0.1 | 7.8 ± 0.2 | 12.9 ± 0.3 | — | 38.4 |
| SPICE-Dipeptide (FF99SB) | 67 | 2592 | Energy | 2.3 ± 0.1 | — | — | 4.5 ± 0.1 | 19.1 |
| | | | Force | 5.6 ± 0.1 | — | — | 12.8 ± 0.3 | 38.4 |
| SPICE-Dipeptide (CHARMM36) | 67 | 2592 | Energy | 2.5 ± 0.1 | — | — | — | 19.1 |
| | | | Force | 5.5 ± 0.1 | — | — | — | 38.4 |
| RNA-Diverse | 6 | 357 | Energy | 3.2 ± 0.2 | 4.2 ± 0.3 | 6.5 ± 0.1 | — | 6.1 |
| | | | Force | 3.7 ± 0.0 | 4.4 ± 0.1 | 16.8 ± 0.1 | — | 30.2 |
| RNA-Trinucleotide | 64 | 23 811 | Energy | 3.5 ± 0.0 | 3.8 ± 0.2 | 6.0 ± 0.1 | — | 6.1 |
| | | | Force | 3.6 ± 0.0 | 4.3 ± 0.1 | 17.0 ± 0.0 | — | 31.2 |
| Radical-Dipeptides (ff99SB) | 28 | 272 | Energy | 3.3 ± 0.3 | — | — | — | 8.7 |
| | | | Force | 6.8 ± 0.2 | — | — | — | 41.3 |
| Gen2-Opt (optimization) | 154 | 29 055 | Energy | 1.7 ± 0.1 | **1.7 ± 0.5** | 2.8 ± 0.2 | — | 4.2 |
| | | | Force | 4.5 ± 0.2 | 4.5 ± 0.8 | 9.8 ± 0.3 | — | 8.7 |
| Pepconf-Opt (optimization) | 55 | 9084 | Energy | 2.9 ± 0.2 | **2.8 ± 0.3** | 4.7 ± 0.3 | — | 6.5 |
| | | | Force | 3.9 ± 0.2 | 4.0 ± 0.4 | 10.4 ± 0.3 | — | 9.4 |
| Gen2-Torsion (torsion scan) | 131 | 19 290 | Energy | 1.7 ± 0.1 | **1.6 ± 0.3** | 2.6 ± 0.1 | — | 4.7 |
| | | | Force | 4.7 ± 0.1 | 4.7 ± 0.6 | 9.5 ± 0.4 | — | 8.9 |
| Protein-Torsion | 9 | 6024 | Energy | 2.0 ± 0.2 | **1.9 ± 0.2** | 2.9 ± 0.2 | — | 3.5 |
| | | | Force | 5.3 ± 0.3 | 3.5 ± 0.3 | 9.8 ± 0.4 | — | 9.0 |
| Protein-Torsion (FF99SB) | 9 | 6024 | Energy | 2.4 ± 0.2 | — | — | — | 3.5 |
| | | | Force | 6.2 ± 0.3 | — | — | — | 9.0 |
| Protein-Torsion (CHARMM36) | 9 | 6024 | Energy | 2.3 ± 0.2 | — | — | — | 3.5 |
| | | | Force | 6.0 ± 0.3 | — | — | — | 9.0 |

Bold marks cases in the source table where Espaloma's mean is numerically lower than Grappa's, reproduced as printed. [SRC-0102, Table 8]

- **Protein stability (ubiquitin, 200 ns).** C$\alpha$ RMSD from the initial structure stays bounded around 4 Å with both Grappa and Amber ff99SB-ILDN over 200 ns in explicit solvent, indicating the folded state remains stable with Grappa; the mean C$\alpha$ RMSD as a function of time-lag $\Delta t$ (bootstrapped over 1000 random frame pairs) is comparable between the two force fields. [SRC-0102, Sec. 4.1, Fig. 7]
- **Folding free energy (chignolin variant CLN025, 2×4 μs).** Grappa (with ff99SB nonbonded parameters and TIP3P water) reproduces multiple folding/unfolding events and gives a calculated folding free energy of $-3.0\,k_BT$ at 340 K, closer to the experimental reference than the $-4.0\,k_BT$ reported elsewhere for Amber ff99SB with the same water model; the central structure of the most populated cluster has 0.77 Å C$\alpha$ RMSD to the experimental structure. The paper notes that protein nonbonded parameters (not tuned by Grappa here, since Grappa only alters bonded terms) have a sizeable impact on MD-derived folding free energies and remain a source for further improvement. [SRC-0102, Sec. 4.2, Fig. 8]
- ***J*-coupling benchmark (13 small peptides, pH 2).** Grappa (ff99SB nonbonded parameters) achieves $\chi^2 = 1.19 \pm 0.20$, RMSE $= 0.46$ Hz against experimental *J*-couplings, outperforming Espaloma-0.3 ($\chi^2=1.43\pm0.21$, RMSE $=0.50$ Hz, AM1-BCC charges) and substantially outperforming Amber ff14SB ($\chi^2=2.60\pm0.51$, RMSE $=0.63$ Hz). [SRC-0102, Sec. 4.3, Fig. 9]
- **Virus-scale simulation (STMV, ~1,000,000 atoms, 30 ns).** Grappa (ff99SB protein + RNA.OL3 RNA nonbonded parameters) keeps both protein C$\alpha$ and RNA backbone-carbon RMSD stable over a 30 ns MD simulation in solution, at 101 timesteps/second on a single A100 GPU with no system-specific optimization. [SRC-0102, Sec. 3.5, 4.5, Fig. 14]
- **Parametrization runtime.** For molecules up to 300,000 atoms, CPU-mode Grappa parametrization runtime is dominated by fixed import/overhead costs rather than the model forward pass itself (Fig. 11); up to ~10,000 atoms, total runtime stays under ~10 s.

## Equation inventory

| Equation / label | Source location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- |
| Bonded MM energy | Eq. 1, p.1 (Sec. 1.1) | Harmonic bond/angle + periodic (Fourier) dihedral energy, the functional form Grappa parametrizes | $E_{\mathrm{bonded}}$, $k_{ij}$, $r_{ij}^{(0)}$, $\theta_{ijk}^{(0)}$, $k_{ijkl}$, $n$ | Defines the Class-I MM bonded functional form shared with Espaloma/grappa-fullFF |
| MM parameter set | Eq. 2, p.2 | Notation for the full bonded parameter collection $\xi$ | $\xi$ | Notational convention used throughout |
| Atom embeddings | Eq. 3, p.2 | $d$-dimensional per-atom embedding from the graph | $\nu$, $d$, $\mathcal{V}$ | Shared encoder output consumed by all four symmetric transformers |
| Parameter readout | Eq. 4, p.2 | Transformer $\psi^{(l)}$ maps embeddings to interaction-type parameters | $\xi_{ij\ldots}^{(l)}$, $\psi^{(l)}$ | Defines per-interaction-type readout heads |
| Conformation energy | Eq. 5, p.2 | MM energy as a function of parameters and spatial conformation | $E(\mathbf{x})$, $E_{\mathrm{MM}}$ | Makes explicit that $\xi$ is evaluated once per molecule, re-used per conformation |
| Bond/angle/torsion permutation symmetries | Eqs. 6-8, p.3 (Sec. 2.1) | Required parameter invariances under subgraph isomorphism | $\xi^{(\mathrm{bond})}_{ij}=\xi^{(\mathrm{bond})}_{ji}$, etc. | Constrains the symmetric transformer's target symmetry group $\mathcal{P}$ per interaction type |
| Angle positional encoding | Eq. 9, p.3 | Permutation-invariant-but-symmetry-breaking positional tag distinguishing the central atom | $\oplus$ append operator | Lets attention layers break unnecessary symmetries while keeping required ones |
| Symmetric pooling | Eq. 10, p.3 | Sum of an MLP over all permutations in the symmetry group, giving $\mathcal{P}$-invariant scores | $z_{ij\ldots}$, MLP, $\sigma \in \mathcal{P}$ | Defines the "symmetric transformer" pooling step (Fig. 2) |
| Training loss | Eq. 11, p.3 (Sec. 2.3) | Weighted energy + force + traditional-MM-deviation + dihedral-$L_2$ loss | $\mathscr{L}$, $\lambda_F$, $\lambda_{\mathrm{MM}}$, $\lambda_{\mathrm{dih}}$ | Top-level training objective; $\lambda_{\mathrm{MM}}$ used only for 100-epoch pretraining |
| GNN node update (linear + ELU) | Eq. 12, p.A2 (A.2.1) | Initial node-feature projection | $W$, $b$, ELU | First layer of the graph attentional network |
| GNN attention layers | Eqs. 13-19, p.A2-A3 | Multi-head dot-product graph attention with layer norm, residuals, 2-layer feed-forward | $e_{ii'}^{(k)}$, $\mathrm{att}_{ii'}^{(k)}$, $V_i^{(k)}$, $W_O$, $W_1$, $W_2$ | Full definition of the $L_{\mathrm{GNN}}$ attentional layers producing atom embeddings |
| Embedding output projection | Eq. 24, p.A3 | Final linear projection to embedding dimension $d_{\mathrm{emb}}$ | $W \in \mathbb{R}^{d_{\mathrm{emb}}\times d}$ | Produces the atom embeddings passed to the symmetric transformers |
| Torsion/improper positional encodings | Eqs. 25-27, p.A3 | Symmetry-respecting positional tags for torsion and improper subgraphs | $\mathrm{PE}_{\mathrm{angle}}$, $\mathrm{PE}_{\mathrm{torsion}}$, $\mathrm{PE}_{\mathrm{improper}}$ | Extends eqn 9's construction to all four interaction types |
| Parameter score mapping (bonds/angles) | Eqs. 28-34, p.A3 | Transformer layers, pooling, and ToPos/ToRange mapping to final $k_{ij}$, $r_{ij}^{(0)}$, $k_{ijk}$, $\theta_{ijk}^{(0)}$, gated $k_{ijkl,m}$ | $z_{ij}$, $z_{ijk}$, $z_{ijkl}$, ToPos, ToRange | Full parameter-head pipeline from embeddings to output MM parameters |
| Output scaling functions | Eqs. 35-38, p.A4 (A.2.3) | ELU/sigmoid-based maps to $(0,\infty)$ and $(\mu-\sigma\cdot c,\mu+\sigma\cdot c)$-like target ranges, matched to a chosen target mean/std; small-$z$ Taylor expansions showing the mapping approximately preserves target mean/variance | ToPos$[\mu,\sigma]$, ToRange$[\gamma/2,\sigma]_{(0,\gamma)}$ | Explains why GNN output scores can be treated as approximately standard-normal during training |
| Improper dihedral decomposition | Eqs. 39-41, p.A4 (A.4) | Two force constants per improper combined so the improper energy is invariant under all 6 central-atom-fixing permutations | $E_{\mathrm{improper}}$, $k_{ijkl}^{(\mathrm{improper})}=k_{ljki}^{(\mathrm{improper})}$ | Solves the improper-symmetry problem noted in Sec. 2.1; directly implementation-relevant for improper terms |
| Force RMSE definition | unnumbered, p.A5-6 (A.6) | Componentwise force RMSE as used throughout Tables 1/7/8 | $N$, $f_{ij}$, $f_{ij}^{(\mathrm{ref})}$ | Defines the force-accuracy metric reported in all result tables |

## Mathematical gaps

- Equations 12-24 (the full graph-attentional-network layer stack, A.2.1) and equations 28-34 (the symmetric-transformer-to-parameter pipeline, A.2.2) are summarized above at the level of their role and key variables rather than reproduced equation-by-equation in the inventory table; all are captured in the source PDF and are each individually short (single attention/feed-forward steps), so no information is lost by this condensation, but a reader needing the literal per-equation LaTeX should consult the raw source directly. [SRC-0102, A.2]
- The paper references (but the ingestion does not reproduce) the general formula for dihedral-angle permutation symmetry from ref. 51 (Blondel & Karplus 1996) used to derive eqn 40; this external derivation is not reproduced here. [SRC-0102, A.4]

## Limitations and Caveats

- Grappa predicts **only bonded** MM parameters; nonbonded (partial-charge, Lennard-Jones) parameters must be supplied externally from a traditional or other ML force field, and Grappa's own accuracy is therefore partly contingent on the quality of whichever nonbonded scheme it is paired with. This limitation is what motivates the later `grappa-fullFF` follow-up ([[wiki/sources/SRC-0101-learning-consistent-molecular-mechanics-force-fields-from-first]]), which jointly predicts nonbonded parameters too. [SRC-0102, Sec. 2.2] [SRC-0101]
- Like all standard MM force fields, Grappa assumes a fixed molecular graph topology (enforced via harmonic bonds), so it cannot describe bond-breaking/forming chemical reactions; the paper explicitly notes this as a "fundamental limitation of standard MM" that Grappa inherits by design, trading reactivity for interpretability and stability. [SRC-0102, Sec. 1.1, Sec. 6]
- The paper reports Grappa is *less* accurate than Espaloma for energies on several datasets even though it is *more* accurate for forces (Table 1); the two models are described as "competitive" overall rather than one uniformly dominating. [SRC-0102, Sec. 3.1]
- Grappa's finite field-of-view (bounded by its 4-layer GNN message-passing radius, reaching atoms within 7 bonds with the hyperparameters in Table 5) means very long-range through-bond electronic effects beyond that radius cannot influence predicted parameters; for the dipeptide test case studied, extending the field of view beyond the directly bonded interaction atoms had only a marginal accuracy effect, but this was tested on a specific (regular-polymer) dataset and is not established as general. [SRC-0102, Sec. 3.7]
- On the 3BPA out-of-distribution dihedral benchmark, zero-shot (non-finetuned) Grappa performs only similarly to, not better than, the general-purpose GAFF-2.11 force field; meaningful improvement there requires finetuning on a small number of additional dihedral-slice states, i.e. Grappa is not unconditionally extrapolation-robust. [SRC-0102, Sec. 4.4]
- Protein nonbonded parameters (fixed, not learned by Grappa) are noted by the authors as having a "sizeable impact" on MD-derived folding free energies and are flagged as "a potential source for further improvement," i.e. Grappa's own bonded-only scope leaves nonbonded-parameter quality as an unaddressed accuracy bottleneck for folding thermodynamics specifically. [SRC-0102, Sec. 4.2]
- The STMV virus simulation (Sec. 4.5) is explicitly described as a stability/efficiency demonstration ("For large scale conformational changes or artificial viral capsid disruption, higher RMSD values would be expected"), not a claim of quantitative accuracy at that scale. [SRC-0102, A.8.4]
- Efficiency comparisons against the E(3)-equivariant Allegro model are based on published performance numbers for a similarly sized but not identical system/hardware configuration (Allegro: 106 timesteps/s on 4000 A100 GPUs per ref. 43; Grappa: 101 timesteps/s on 1 A100 GPU for STMV), so the "three orders of magnitude" efficiency claim is an approximate, not strictly controlled, comparison. [SRC-0102, Sec. 3.5]
- This paper (SRC-0102) predates and is cited as prior work by `grappa-fullFF` (SRC-0101, a 2026 NeurIPS workshop paper not yet peer-reviewed); SRC-0102 itself does not discuss `grappa-fullFF` or joint nonbonded-parameter learning. [SRC-0102] [SRC-0101]

## Open Questions

- Does extending Grappa to predict nonbonded parameters directly (rather than only consuming externally assigned ones) further improve accuracy, as speculated in the paper's own Conclusions ("an extension of the framework to nonbonded parameters is a straightforward next step... could potentially improve its accuracy further")? This question is substantially addressed by the later `grappa-fullFF` work. [SRC-0102, Sec. 5] [SRC-0101]
- How much of Grappa's remaining folding-free-energy discrepancy from experiment (CLN025, $-3.0\,k_BT$ vs. experimental reference) is attributable to the fixed (non-learned) nonbonded parameters versus the learned bonded parameters or the water model? [SRC-0102, Sec. 4.2]
- Would Grappa's accuracy on peptide radicals (or other out-of-distribution chemistries) improve further with larger or more diverse task-specific training sets, given its reported high general data efficiency (Fig. 19)? [SRC-0102, Sec. 3.2]
- How does Grappa's accuracy/efficiency trade-off compare, under a matched hardware/system-size benchmark (rather than published numbers from different studies), to E(3)-equivariant models such as Allegro, NequIP, or MACE? [SRC-0102, Sec. 3.5]

## Claims

- [[wiki/claims/CLM-0058-grappa-matches-or-exceeds-espaloma-accuracy-at-mm-cost-and-extends-to-new-chemistries]]

## Links

- [[wiki/concepts/grappa-machine-learned-force-fields]]
- [[wiki/concepts/espaloma-machine-learned-mm-force-fields]]
- [[wiki/concepts/automated-force-field-training]]
- [[wiki/concepts/garnet-force-field]]
- [[wiki/sources/SRC-0101-learning-consistent-molecular-mechanics-force-fields-from-first]]
- [[wiki/sources/SRC-0072-machine-learned-molecular-mechanics-force-fields-from-large]]
- [[wiki/sources/SRC-0098-graph-nets-partial-charge-prediction]]
- [[wiki/claims/CLM-0058-grappa-matches-or-exceeds-espaloma-accuracy-at-mm-cost-and-extends-to-new-chemistries]]

## Citation Links

- Grappa (SRC-0102) is trained and evaluated on the dataset reported in the Espaloma follow-up paper (ref. 10: Takaba, Friedman, Cavender *et al.*, "Machine-learned molecular mechanics force fields from large-scale quantum chemical data," *Chem. Sci.*, 2024, 15, 12861-12878). By title, author, and venue/year match, this is confirmed to be [[wiki/sources/SRC-0072-machine-learned-molecular-mechanics-force-fields-from-large]], already ingested in SecondBrain; Grappa reuses its exact train/validation/test partition (by isomeric SMILES). [SRC-0102] [SRC-0072]
- Grappa is itself cited (as ref. 23, "grappa-bonded") by the later workshop paper [[wiki/sources/SRC-0101-learning-consistent-molecular-mechanics-force-fields-from-first]], confirmed previously by DOI (`10.1039/d4sc05465b`) match; this ingestion fills the gap SRC-0101 recorded as "not separately ingested." [SRC-0102] [SRC-0101]
- SRC-0102 compares against and cites GAFF-2.11 (ref. 19), Amber ff14SB (ref. 20) and ff19SB (ref. 27), Amber ff99SB-ILDN (ref. 25), CHARMM36 (ref. 26), RNA.OL3 (ref. 21), the OpenFF-2.0.0 small-molecule force field (ref. 18), and the SPICE dataset (ref. 22); none of these are currently ingested as separate SecondBrain sources. [SRC-0102]
- SRC-0102 cites and benchmarks efficiency/accuracy against several E(3)-equivariant neural network potentials: Allegro (ref. 42/43, Musaelian/Batzner/Kozinsky *et al.*), NequIP (ref. 4, Schütt & Gastegger), and MACE (ref. 2, Batatia *et al.*), and uses the 3BPA dataset (ref. 40, Kovács *et al.*, Linear Atomic Cluster Expansion) that was originally used to test MACE's extrapolation; none of these are currently ingested as separate SecondBrain sources, though a different MACE-derived paper (MACE-MDP, SRC-0065) is already present and is not the same source. [SRC-0102]
- SRC-0102 also cites GB-FFs (ref. 6: Chen, Jaffrelot Inizan, Plé *et al.*, "Advancing Graph Force Fields Parameterization: A Directed Graph Attention Networks Approach," *J. Chem. Theory Comput.*, 2024) as a contemporaneous machine-learned MM force field; not currently ingested as a separate SecondBrain source. [SRC-0102]
- SRC-0102 is not cited by Garnet-related sources in SecondBrain in the material reviewed to date; the Grappa-vs-Garnet comparison recorded on [[wiki/concepts/grappa-machine-learned-force-fields]] and [[wiki/concepts/garnet-force-field]] is project-level synthesis from the two independently ingested papers, not a citation relationship asserted by either source.

## Metadata notes

- Peer-reviewed RSC Edge Article, CC-BY-NC 4.0, received 14 August 2024, accepted 13 December 2024, published 15 January 2025. [SRC-0102]
- Funding: Klaus Tschira Foundation; European Research Council (ERC) grant 101002812 under Horizon 2020. [SRC-0102]
- Open-source release: Grappa is released under GNU GPL v3.0, available via `pip install grappa-ff`, GitHub (`graeter-group/grappa`), and PyPI; pretrained model weights are downloaded via a release tag (e.g. `grappa-1.3`); all results in the validation section used Grappa-1.4.0. Peptide-radical and dipeptide dataset-creation code is at a separate `LeifSeute/grappa-data-creation` repository, and the validation-reproduction code at `LeifSeute/validate-grappa`. [SRC-0102, Data availability, A.1]
- No conflicts of interest declared. [SRC-0102]

## Ingestion QA

### Retrieval questions checked

- What is Grappa's central architectural contribution, and how does the "symmetric transformer" enforce the required permutation symmetries (including the improper-dihedral special case)?
- What MM parameters does Grappa predict, and what does it rely on externally (nonbonded parameters)?
- What benchmark datasets and metrics were used, and what were the headline energy/force accuracy results versus Espaloma and traditional force fields?
- How does Grappa demonstrate extensibility to new chemical space (peptide radicals), and does this degrade accuracy on the original training distribution?
- What downstream MD validation was performed (protein stability, folding free energy, *J*-couplings, virus-scale simulation), and what were the results?
- How efficient is Grappa compared to E(3)-equivariant neural network potentials, and under what caveats is that comparison made?
- What are the main limitations acknowledged by the authors, and what future work (nonbonded-parameter prediction, reactive chemistry) do they propose?
- Which prior or related sources does this paper cite or get cited by, and are they already present in SecondBrain?

### Coverage decision

Complete at `coverage_profile: math-standard`. The source page captures the two-stage architecture (GNN + symmetric transformer) and its symmetry-enforcement mechanism, the training loss and hyperparameters, all eight main-text and appendix result tables transcribed in full (per the standing preference for data/benchmark papers), the four downstream MD validation studies (ubiquitin stability, chignolin folding, *J*-couplings, STMV virus), the efficiency comparison, the 3BPA finetuning study, the tabulated-force-field construction, limitations, and open questions, plus a curated equation inventory covering the central symmetry, loss, and parameter-mapping equations.

### Known gaps

- Reference list details for GAFF-2.11, Amber ff14SB/ff19SB/ff99SB-ILDN, CHARMM36, RNA.OL3, OpenFF-2.0.0, SPICE, Allegro, NequIP, MACE, 3BPA/MACE's extrapolation study, and GB-FFs are recorded only as citation metadata in this page, not ingested as separate source pages. [SRC-0102]
- Table 2's and Table 3's column headers in the source PDF reuse the labels "Grappa" and "Grappa-base"/"Grappa-radicals" in a way that is slightly ambiguous without the full caption context; the transcription above preserves the printed values and includes an explanatory note, but the exact training-set definition for each column should be checked against the source PDF (or the authors' code release) before using these numbers in further analysis. [SRC-0102, Tables 2-3]
- Figures 4c (latent-space PCA), 6/16 (dihedral free-energy landscapes and per-term decomposition), 7-9 (ubiquitin/folding/*J*-coupling), 14 (STMV), and 19-20 (learning curve, parameter distributions) are described qualitatively from their captions and axis labels; exact per-pixel/per-point values are not extracted.
- The exact numeric values of the 1-4 scaling factors and nonbonded-exclusion conventions used in Grappa's MM energy functional are not given explicitly in the main text reviewed; they are referenced only as using the "same energy functional as Amber ff14SB." [SRC-0102, Sec. 3.4]

