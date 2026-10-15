---
type: source
status: active
created: 2026-10-12
updated: 2026-10-12
source_id: SRC-0101
display_title: "Learning consistent molecular mechanics force fields from first principles"
short_title: "grappa-fullFF"
aliases:
  - "SRC-0101"
  - "grappa-fullFF"
  - "Learning Consistent Molecular Mechanics Force Fields from First Principles"
source_path: raw/sources/SRC-0101-learning-consistent-molecular-mechanics-force-fields-from-first.pdf
imported_path: raw/sources/SRC-0101-learning-consistent-molecular-mechanics-force-fields-from-first.pdf
original_filename: "2610.08020v1.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 7463447bbe498cf563eba23fea6dd9149ff2c83da263504de75d44e211ac261e
authors:
  - "Berkay Günes"
  - "Leif Seute"
  - "Jigyasa Nigam"
  - "Frauke Gräter"
author_entities: []
year: 2026
venue: "40th Conference on Neural Information Processing Systems (NeurIPS 2026), Workshop: ML4Molecules"
doi:
arxiv: "2610.08020"
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
  - nonbonded-parameters
  - partial-charges
  - lennard-jones
  - electrostatic-potential
  - benchmark
related:
  - "[[wiki/concepts/grappa-machine-learned-force-fields]]"
  - "[[wiki/concepts/espaloma-machine-learned-mm-force-fields]]"
  - "[[wiki/concepts/automated-force-field-training]]"
  - "[[wiki/concepts/garnet-force-field]]"
  - "[[wiki/concepts/double-exponential-potential]]"
  - "[[wiki/sources/SRC-0072-machine-learned-molecular-mechanics-force-fields-from-large]]"
  - "[[wiki/sources/SRC-0098-graph-nets-partial-charge-prediction]]"
  - "[[wiki/sources/SRC-0003-training-a-force-field-from-scratch]]"
sources:
  - SRC-0101
cites_sources: []
citation_match_status: partial
cqt_review_status: linked
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: math-standard
peer_review_status: not-peer-reviewed
---

# Learning Consistent Molecular Mechanics Force Fields from First Principles

Source ID: `SRC-0101`

## Raw source

- Repository path: `raw/sources/SRC-0101-learning-consistent-molecular-mechanics-force-fields-from-first.pdf`
- Open raw source: [raw/sources/SRC-0101-learning-consistent-molecular-mechanics-force-fields-from-first.pdf](../../raw/sources/SRC-0101-learning-consistent-molecular-mechanics-force-fields-from-first.pdf)

## Status note

This is a NeurIPS 2026 ML4Molecules workshop paper (arXiv `2610.08020`, submitted 6 October 2026), not a peer-reviewed journal article. [SRC-0101]

## Summary

Günes, Seute, Nigam, and Gräter introduce `grappa-fullFF`, a graph-attention model that predicts both the bonded and nonbonded molecular-mechanics (MM) parameters of a classical force field simultaneously and consistently from ab initio quantum-mechanical (QM) reference data, rather than relying on externally assigned nonbonded (partial-charge and Lennard-Jones) parameters. It extends `grappa-bonded` (Seute et al., Chemical Science 2025, cited as reference 23, not separately ingested in SecondBrain) by adding two new prediction heads: an antisymmetric bond-charge-flux head for partial charges and a Tkatchenko-Scheffler van der Waals (TS-vdW) volume-ratio head for Lennard-Jones (LJ) parameters. Because energies and forces alone cannot uniquely separate bonded from nonbonded contributions ("energy degeneracy"), the model is regularized with physically motivated constraints: matching the predicted electrostatic potential (ESP) to the QM reference, and matching predicted per-atom effective volume ratios to ratios obtained from QM electron-density partitioning. [SRC-0101]

## Key Points

- The shared MM energy decomposition is $E_{\mathrm{MM}} = E_{\mathrm{bonded}} + E_{\mathrm{nonbonded}}$, with $E_{\mathrm{bonded}} = U_{\mathrm{bonds}} + U_{\mathrm{angles}} + U_{\mathrm{dihedrals}}$ and $E_{\mathrm{nonbonded}} = U_{\mathrm{vdW}} + U_{\mathrm{Coulomb}}$ (12-6 Lennard-Jones plus Coulomb). [SRC-0101]
- A shared graph-attention encoder produces atom embeddings; separate prediction heads (unchanged bonded heads from `grappa-bonded`, plus new charge-flux and volume-ratio heads) read out bond, angle, dihedral, partial-charge, and Lennard-Jones parameters from these embeddings. [SRC-0101]
- Partial charges are produced by an antisymmetric bond-charge-flux mechanism rather than charge equilibration (QEq): each atom starts at $q_i^{(t=0)} = Q_{\mathrm{tot}}/N$, and the model predicts charge flux $w_{ij}^{(t)}$ transferred between bonded atom pairs at each of $T$ message-passing refinement steps, with $w_{ij}^{(t)} = -w_{ji}^{(t)}$ enforced by construction so total charge is conserved without post-hoc normalization or charge equilibration. [SRC-0101]
- This bond-charge-flux mechanism follows the classical Bond-Charge Increment (BCI) idea from MMFF94 (Halgren 1996, ref. 34, not separately ingested) and is explicitly a different mechanism from the electronegativity/hardness QEq solve used by Espaloma and by the graph-net charge model of Wang et al.; see [[wiki/sources/SRC-0098-graph-nets-partial-charge-prediction]] and [[wiki/concepts/espaloma-machine-learned-mm-force-fields]] for the QEq alternative. [SRC-0101] [SRC-0098]
- Lennard-Jones parameters are not predicted directly. A per-atom effective/free atomic volume ratio $v_i = v_i^{\mathrm{eff}}/v_i^{\mathrm{free}}$ is predicted and mapped to $\sigma$ and $\epsilon$ through the TS-vdW relation $\sigma \propto v_i^{1/7}$, $\epsilon \propto C_6^{\mathrm{eff}}/\sigma^6$ with $C_6^{\mathrm{eff}} = v_i^2 C_6^{\mathrm{free}}$ and effective polarizability $\alpha_{\mathrm{eff}} = v_i \alpha_{\mathrm{free}}$; $v_i$ is constrained positive with a scaled ELU activation. [SRC-0101]
- Training optimizes a combined loss $\mathcal{L} = \lambda_E \mathcal{L}_E + \lambda_F \mathcal{L}_F + \lambda_{\mathrm{ESP}} \mathcal{L}_{\mathrm{ESP}} + \lambda_v \mathcal{L}_v$ through a fully differentiable MM energy/force functional (with GROMACS/OpenMM-style 1-2, 1-3 exclusions and 1-4 scaling), using mean squared energy and force errors plus two physics-informed nonbonded regularizers: $\mathcal{L}_{\mathrm{ESP}}$ (predicted charges' ESP matched to the QM-electron-density-derived reference ESP on Fibonacci-lattice grid shells at 1.4-2x van der Waals radii around each atom) and $\mathcal{L}_v$ (predicted volume ratios matched to MBIS-partitioned reference ratios). Partial charges are deliberately *not* supervised directly against reference atomic charges in the main model (only through the ESP). [SRC-0101]
- Training/evaluation data are the DES-monomer, dipeptide, and PubChem subsets of the SPICE dataset with QM energies and forces from the OMol25 dataset (ωB97M-V/def2-TZVPD), filtered to 10,240 unique molecules and ~441,000 conformers (matching the Espaloma / `grappa-bonded` filtering), of which 14,600 conformers have usable electron densities for the ESP/volume-ratio losses (reference ESP from Multiwfn; reference volumes from MBIS partitioning, averaged per atom across conformers). [SRC-0101]

## Evidence

**Table 1 — ESP and dipole RMSE by charge model and dataset** (ESP in $10^{-3}\,e/\text{Å}$, dipole in $e\text{Å}$; parenthetical values are the standard deviation on the last digit(s); MBIS and AM1-BCC require DFT calculations):

| Charge Model | PubChem ESP | PubChem Dipole | Dipeptide ESP | Dipeptide Dipole | DES Monomers ESP | DES Monomers Dipole |
| --- | --- | --- | --- | --- | --- | --- |
| MBIS¹ | **7.157(54)** | 1.190(26) | **8.47(37)** | 1.724(79) | 6.22(25) | 0.622(50) |
| AM1-BCC¹ | 10.414(87) | 1.156(25) | 12.32(54) | 1.88(10) | 8.50(40) | 0.597(47) |
| espaloma-charge | 35.7(10) | 2.084(40) | 30.3(11) | 2.174(71) | 18.2(17) | 0.758(66) |
| grappa-fullFF | 8.90(58) | **1.048(24)** | 12.7(13) | **1.584(81)** | **6.12(26)** | **0.561(46)** |

¹ Requires DFT calculations. [SRC-0101, Table 1]

**Table 2 — Geometry-optimization benchmark** (OpenFF Industry Benchmark Season 1 v1.1; RMSE med and TFD med are medians over conformers, ddE is relative-energy error vs. the QM reference):

| Force Field | RMSE med (Å) | TFD med | ddE MAE (kcal/mol) | ddE RMSE (kcal/mol) |
| --- | --- | --- | --- | --- |
| gaff-2.11 | 0.4997 | 0.0476 | 2.341 | 3.892 |
| openff-2.1.0 | 0.3688 | 0.0355 | 2.036 | 3.495 |
| espaloma-0.3.2 | 0.2725 | 0.0241 | 1.639 | 3.064 |
| grappa-bonded | 0.2571 | 0.0232 | 1.608 | 2.773 |
| grappa-fullFF | 0.2661 | 0.0221 | 1.589 | 2.973 |

[SRC-0101, Table 2]

**Table 3 — Divergence of each force field's Ramachandran free-energy surface (FES) from AMBER99SB-ILDN** (capped alanine dipeptide, ACE-ALA-NME, 500 ns explicit-solvent TIP3P MD, $5^\circ \times 5^\circ$ $(\phi,\psi)$ binning; smaller is closer to AMBER99SB-ILDN):

| Force field | Symmetric KL [nats] | Jensen-Shannon [nats] |
| --- | --- | --- |
| AMBER99SB-ILDN (reference) | 0.000 | 0.0000 |
| espaloma-0.3.2 | 1.752 | 0.1596 |
| grappa-bonded | **0.432** | **0.0691** |
| grappa-fullFF | 0.502 | 0.0820 |

[SRC-0101, Table 3]

**Table 4 — Appendix B ablation of the two nonbonded regularization terms** ($\mathcal{L}_q$ supervises charges directly against MBIS reference charges, Eq. 7; $\mathcal{L}_{\mathrm{ESP}}$ is the ESP loss, Eq. 6; $\lambda_E=2$, $\lambda_F=1$, $\lambda_v=100$ held fixed; ESP in $10^{-3}\,e/\text{Å}$; $\langle q_i\rangle/\langle q_i^{\mathrm{MBIS}}\rangle$ is the ratio of mean absolute charge magnitudes on 30 PubChem molecules; the last row is the configuration used to train grappa-fullFF):

| Config | $\lambda_q$ | $\lambda_{\mathrm{ESP}}$ | ESP PubChem | ESP Dipeptide | ESP DES | $\langle q_i\rangle/\langle q_i^{\mathrm{MBIS}}\rangle$ | ddE MAE |
| --- | --- | --- | --- | --- | --- | --- | --- |
| No regularization | 0 | 0 | 13.84 | 17.35 | 9.10 | 0.74 | — |
| Charge loss only | 1000 | 0 | 11.80 | 16.52 | 8.71 | 0.99 | 1.72 |
| Charge loss + ESP loss | 1000 | 100 | 11.07 | 20.24 | 7.55 | ≈1.00 | — |
| **ESP loss only (used for grappa-fullFF)** | **0** | **1000** | **8.86** | **12.84** | **6.13** | **0.78** | **1.58** |

[SRC-0101, Table 4]

- Without either charge regularizer ($\lambda_{\mathrm{ESP}}=\lambda_q=0$), ESP RMSE increases 35-56% across all three dataset partitions and the mean-charge-magnitude ratio to MBIS is only 0.74. Supervising charges directly ($\lambda_q=1000$, $\lambda_{\mathrm{ESP}}=0$) recovers the MBIS charge magnitude ratio (~1.0) but increases ESP error relative to ESP-only regularization. ESP regularization alone gives the lowest ESP error on all three partitions even though the charge-magnitude ratio only reaches 0.78. [SRC-0101, Appendix B]
- Qualitative ESP surface comparison (Fig. 3) on a representative polar molecule shows grappa-fullFF (deviation 0.0053 e/Å) closely matching MBIS (0.0061 e/Å), while AM1-BCC (0.0157 e/Å) and espaloma-0.3.2 (0.0397 e/Å) show larger deviations. [SRC-0101, Fig. 3]
- grappa-fullFF learns reduced LJ $\sigma$ values for polar hydrogens relative to the raw TS-vdW volume-ratio reference ($\sigma \approx 1.1$-$2.5$ Å predicted vs. $\approx 2.3$-$2.5$ Å from the TS-vdW reference), purely from energy/force gradients, enabling physically appropriate hydrogen bonding without the TS-vdW reference's unphysical Pauli repulsion in H-bonded environments. [SRC-0101, Appendix C, Fig. 5]
- The cumulative distribution functions (CDFs) for RMSE, TFD, and |ddE| (Fig. 4, Appendix A.2) show grappa-bonded and grappa-fullFF distributions nearly indistinguishable, supporting that jointly learning nonbonded parameters does not measurably degrade bonded-parameter accuracy despite the underlying energy-degeneracy ambiguity. [SRC-0101, Appendix A.2]
- MD protocol (Appendix D): capped alanine dipeptide solvated in a 2.4 nm cubic TIP3P box (418 waters, 1 Na+/2 Cl-, 0.15 M ionic strength, 1,278 atoms); 100 ps NVT + 1 ns NPT equilibration, then 500 ns NPT production at 2 fs/300 K (OpenMM `LangevinMiddleIntegrator`, 1 ps⁻¹ friction, Monte Carlo barostat at 1 atm, PME with 1.0 nm real-space cutoff, bonds-to-H constrained, rigid water); identical solvated topology and starting coordinates reused across all four compared force fields; frames saved every 1 ps (500,000 samples of $(\phi,\psi)$ per force field). For grappa-fullFF the solute was parameterized entirely by the network while TIP3P water kept its conventional parameters. [SRC-0101, Appendix D]

## Equation inventory

| Equation / label | Source location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- |
| MM energy decomposition | Eq. 1, p.1 | Defines bonded/nonbonded split of the MM potential energy | $E_{\mathrm{MM}}$, $\Phi_{\mathrm{FF}}$, $\Phi_{\mathrm{bonded}}$, $\Phi_{\mathrm{nonbonded}}$ | Same Class-I MM functional form as `grappa-bonded`/Espaloma; grappa-fullFF predicts all of $\Phi_{\mathrm{FF}}$ |
| Charge-flux update | Eq. 2, p.3 | Iteratively refines atomic charge from antisymmetric bond fluxes | $q_i^{(t)}$, $w_{ij}^{(t)}$, $\mathcal{N}(i)$ | Replaces QEq; guarantees charge conservation by construction |
| Initial charge flux | Eq. 3, p.3 | Seeds flux from atom embeddings at $t=0$ | $w_{ij}^{(0)}$, $h_i$, $h_j$, MLP$^{(0)}$ | Defines the bond-charge-flux readout head |
| Gated flux update, $t \geq 1$ | Eq. 4, p.3 | Refines flux using current charge state and local change | $w_{ij}^{(t)}$, $\xi_{ij}^{(t)}$, $\Delta q_{i,t}$, gating MLP | Multi-step message-passing refinement of partial charges |
| Training loss | Eq. 5, p.3 | Combined energy/force/ESP/volume-ratio objective | $\mathcal{L}$, $\mathcal{L}_E$, $\mathcal{L}_F$, $\mathcal{L}_{\mathrm{ESP}}$, $\mathcal{L}_v$, $\lambda$'s | Top-level training objective resolving energy degeneracy |
| ESP regularization loss | Eq. 6, p.4 | Matches predicted-charge ESP to QM reference ESP on grid shells | $\tilde V_{\mathrm{ESP}}$, $V_{\mathrm{ESP}}$, $\chi_j$, $\mu_{\mathrm{shell}}$, $N_\chi$ | Physics-informed charge regularization without direct charge supervision |
| Direct charge-supervision loss (ablation) | Eq. 7, p.12 (Appendix B) | Alternative MSE loss against MBIS reference charges | $\mathcal{L}_q$, $q_i^{\mathrm{MBIS}}$ | Used only in the Appendix B ablation, not in the main grappa-fullFF configuration |
| TS-vdW parameter mapping | Sec. 2.1, p.3 (prose, unnumbered) | Maps predicted volume ratio to LJ $\sigma,\epsilon$ | $v_i$, $\sigma$, $\epsilon$, $C_6^{\mathrm{eff}}$, $C_6^{\mathrm{free}}$, $\alpha_{\mathrm{eff}}$, $\alpha_{\mathrm{free}}$ | Physically constrained LJ parameterization; $\sigma \propto v_i^{1/7}$, $\epsilon \propto C_6^{\mathrm{eff}}/\sigma^6$ |

## Mathematical gaps

- The exact parametric forms of the bonded prediction heads (symmetric transformer / angle / dihedral parameter heads, inherited unchanged from `grappa-bonded`) are referenced but not reproduced here, since `grappa-bonded` itself (ref. 23, Seute et al., Chemical Science 2025) is not separately ingested in SecondBrain. [SRC-0101]
- The paper states the differentiable MM functional implements "classical 1-2 and 1-3 exclusion rules, as well as 1-4 scaling factors," but does not give the exact scaling-factor values used; these are not reproduced here. [SRC-0101, Sec. 2.2]
- The full architecture of the gating MLP ($\mathrm{MLP}_{\mathrm{gate}}^{(t)}$ in Eq. 4) and of the volume-ratio MLP head is described only at the level of Fig. 1 and prose, not as explicit layer-by-layer definitions. [SRC-0101]

## Limitations and Caveats

- grappa-fullFF was trained exclusively on isolated gas-phase monomers/small systems (SPICE/OMol25 subsets); its accurate reproduction of the explicit-solvent alanine-dipeptide Ramachandran FES (Table 3) is reported as a generalization result, not as evidence that training generalizes to larger or more delocalized molecules. [SRC-0101, Discussion]
- grappa-fullFF's Ramachandran-FES divergence from AMBER99SB-ILDN (JS = 0.0820 nats) is somewhat larger than `grappa-bonded`'s (0.0691 nats); the paper frames the $\Delta$JS = 0.013 nats difference as small/"negligible," but it is a measurable regression from using jointly learned rather than empirical nonbonded parameters. [SRC-0101, Sec. 3, Table 3]
- The ESP-only regularization strategy used for grappa-fullFF does not exactly recover MBIS reference charge magnitudes (ratio 0.78 rather than ~1.0; Table 4), even though it gives the lowest ESP error of the compared configurations. [SRC-0101, Appendix B]
- Electron-density-derived references (ESP, MBIS volume ratios) are only available for 14,600 of the ~441,000 total conformers, so $\mathcal{L}_{\mathrm{ESP}}$ and $\mathcal{L}_v$ are trained on a smaller data subset than $\mathcal{L}_E$ and $\mathcal{L}_F$. [SRC-0101, Sec. 3]
- The water solvent in the alanine-dipeptide MD benchmark used a conventional (non-learned) TIP3P model even for grappa-fullFF; the paper explicitly notes that extending training to explicit-solvent configurations is future work. [SRC-0101, Appendix D, Discussion]
- This is a workshop paper (NeurIPS 2026, ML4Molecules), not yet peer-reviewed in a journal. [SRC-0101]

## Open Questions

- Does training grappa-fullFF directly on explicit-solvent or condensed-phase configurations (rather than only gas-phase monomers) further improve its reproduction of the dipeptide Ramachandran FES, water-solute interface behavior, or other condensed-phase observables? [SRC-0101, Discussion]
- How does the antisymmetric bond-charge-flux charge model compare quantitatively to QEq-style electronegativity/hardness charge models (as used by Espaloma and Garnet) in settings where charges must respond to larger conformational or environmental changes, rather than only matching a static ESP? [SRC-0101] [SRC-0098]
- Would additional refinement steps or alternative charge-flux initialization schemes improve performance on larger, more delocalized molecules, as the authors suggest? [SRC-0101, Discussion]

## Claims

- [[wiki/claims/CLM-0057-grappa-fullff-jointly-learns-nonbonded-parameters-without-degrading-bonded-accuracy]]

## Links

- [[wiki/concepts/grappa-machine-learned-force-fields]]
- [[wiki/concepts/espaloma-machine-learned-mm-force-fields]]
- [[wiki/concepts/automated-force-field-training]]
- [[wiki/concepts/garnet-force-field]]
- [[wiki/concepts/double-exponential-potential]]
- [[wiki/sources/SRC-0072-machine-learned-molecular-mechanics-force-fields-from-large]]
- [[wiki/sources/SRC-0098-graph-nets-partial-charge-prediction]]
- [[wiki/sources/SRC-0003-training-a-force-field-from-scratch]]

## Citation Links

- `grappa-fullFF` extends `grappa-bonded` (Seute, Hartmann, Stühmer & Gräter, Chemical Science 16(6):2907-2930, 2025, doi `10.1039/d4sc05465b`, ref. 23); this prior Grappa paper is cited extensively but is not currently ingested in SecondBrain as its own source. [SRC-0101]
- The partial-charge QEq alternative discussed for contrast is confirmed, by title and content match, to be [[wiki/sources/SRC-0098-graph-nets-partial-charge-prediction]] (Wang, Fass, Stern, Luo & Chodera, arXiv `1909.07903`), already ingested and linked from the Espaloma concept page. [SRC-0101] [SRC-0098]
- The training/evaluation data reuse the OMol25 dataset (Eastman et al. 2026, arXiv `2505.08762`, ref. 44) and the SPICE dataset (Eastman et al. 2022, arXiv `2209.10702`, ref. 43); neither is currently ingested as its own SecondBrain source page, though OMol25 and SPICE are discussed as datasets in [[wiki/concepts/machine-learning-potential-datasets]]. [SRC-0101]
- Other cited comparison baselines (GAFF-2.11, OpenFF-2.1.0, AMBER99SB-ILDN, espaloma-0.3.2, Multiwfn, MBIS) are not separately ingested as SecondBrain sources. [SRC-0101]

## Metadata notes

- arXiv identifier: `2610.08020v1`, submitted 6 October 2026. [SRC-0101]
- Funding: European Research Council (ERC) grant 101002812; computations on the Otter HPC system at the Max Planck Computing and Data Facility. [SRC-0101]
- No code or data repository URL is given in the extracted text of this workshop paper. [SRC-0101]

## Ingestion QA

### Retrieval questions checked

- What is the central contribution of grappa-fullFF relative to grappa-bonded and Espaloma?
- How does grappa-fullFF predict partial charges, and how does that differ from QEq-style charge models?
- How does grappa-fullFF predict Lennard-Jones parameters, and what physical relationship constrains them?
- What is "energy degeneracy," and how does the paper address it?
- What benchmarks and datasets were used, and what were the main quantitative results (ESP/dipole accuracy, geometry optimization, Ramachandran free-energy divergence)?
- What does the regularization ablation (Appendix B) show about charge supervision vs. ESP regularization?
- What are the key limitations, and what future work does the paper propose?
- Which prior sources does this paper build on or compare against, and are they already in SecondBrain?

### Coverage decision

Complete at `coverage_profile: math-standard`. The source page captures the full MM energy decomposition, the charge-flux and TS-vdW volume-ratio parameterizations, the training loss and both regularization terms, all four result tables transcribed in full (not summarized, per data/benchmark-paper convention), the qualitative ESP/LJ-radius figures, the MD protocol, limitations, and open questions.

### Known gaps

- `grappa-bonded` (Seute et al. 2025, ref. 23) is cited throughout but not separately ingested; some bonded-head architectural detail is only available by reference to that uningested source. [SRC-0101]
- Reference list details for OMol25, SPICE, GAFF, OpenFF, AMBER99SB-ILDN, Multiwfn, and MBIS are recorded only as citation metadata, not ingested as separate source pages.
- Figures 3, 4, and 5 are described qualitatively from their captions and axis labels; exact per-pixel values are not extracted.
