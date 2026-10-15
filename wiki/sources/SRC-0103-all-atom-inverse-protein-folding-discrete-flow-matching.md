---
type: source
status: active
created: 2026-10-12
updated: 2026-10-12
source_id: SRC-0103
display_title: "All-atom inverse protein folding through discrete flow matching"
short_title: "ADFLIP"
aliases:
  - "SRC-0103"
  - "ADFLIP"
  - "All-atom Discrete FLow matching Inverse Protein folding"
source_path: raw/sources/SRC-0103-all-atom-inverse-protein-folding-discrete-flow-matching.pdf
imported_path: raw/sources/SRC-0103-all-atom-inverse-protein-folding-discrete-flow-matching.pdf
original_filename: "2507.14156v1.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: f275442d14767c7f7989512c09917ab6023f10d3d788e0516517758eb9b3943f
authors:
  - "Kai Yi"
  - "Kiarash Jamali"
  - "Sjors H. W. Scheres"
author_entities: []
year: 2025
venue: "Proceedings of the 42nd International Conference on Machine Learning (ICML), PMLR 267"
doi:
arxiv: "2507.14156"
metadata_review_status: reviewed
source_bundle:
bundle_role: main
areas:
  - research
categories:
  - research/biomolecules/proteins
  - research/machine-learning/molecular-modeling
  - research/experimental-benchmarking
  - research/computational-drug-discovery
tags:
  - protein-design
  - inverse-protein-folding
  - flow-matching
  - discrete-generative-model
  - graph-neural-networks
  - side-chain-packing
  - classifier-guidance
  - nmr
  - benchmark
related:
  - "[[wiki/concepts/adflip-discrete-flow-matching-inverse-folding]]"
  - "[[wiki/sources/SRC-0104-de-novo-design-of-protein-structure-and-function]]"
sources:
  - SRC-0103
cites_sources:
  - SRC-0104
citation_match_status: partial
cqt_review_status: linked
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: math-standard
peer_review_status: peer-reviewed
---

# All-atom Inverse Protein Folding through Discrete Flow Matching

Source ID: `SRC-0103`

## Raw source

- Repository path: `raw/sources/SRC-0103-all-atom-inverse-protein-folding-discrete-flow-matching.pdf`
- Open raw source: [raw/sources/SRC-0103-all-atom-inverse-protein-folding-discrete-flow-matching.pdf](../../raw/sources/SRC-0103-all-atom-inverse-protein-folding-discrete-flow-matching.pdf)

## Summary

Yi, Jamali, and Scheres (MRC Laboratory of Molecular Biology) present ADFLIP (All-atom Discrete FLow matching Inverse Protein folding), a generative model for protein *inverse folding* — designing an amino-acid sequence that adopts a given 3D structure — conditioned on the full all-atom structure of a biomolecular complex, including non-protein components (small-molecule ligands, nucleotides, metal ions) and, optionally, multiple structural states of a dynamic complex (e.g. from NMR ensembles). ADFLIP uses discrete flow matching (following Campbell et al., 2024) to generate the sequence, a multi-scale graph neural network (GNN) denoiser that alternates between atom-level and residue-level message passing, concurrent side-chain packing (via the external PIPPACK network) that feeds predicted side-chain geometry back as structural context for subsequent denoising steps, and a training-free classifier-guidance mechanism that lets an arbitrary pre-trained regressor (not retrained for masked/intermediate inputs) steer sampling toward a target property, demonstrated with ligand-binding-affinity guidance via DSMBind. On held-out PDB benchmarks following the LigandMPNN protocol, ADFLIP achieves the best recovery rate and lowest perplexity of the compared methods (PiFold, ProteinMPNN, LigandMPNN) for residues near ligands, nucleotides, and metal ions, and on a newly curated 219-ensemble solution-NMR dataset, conditioning on the full conformational ensemble rather than a single structure further improves recovery. [SRC-0103]

## Key Points

- **Discrete flow matching for sequence generation.** ADFLIP models $p_\theta(S|X)$ for discrete protein sequences $S \in \{1,\dots,20\}^L$ conditioned on protein-complex structure $X = \{X_{\mathrm{protein}}, X_{\mathrm{non-protein}}\}$, with $X_{\mathrm{protein}} \in \mathbb{R}^{L\times4\times3}$ the backbone $(N, C_\alpha, C, O)$ coordinates and $X_{\mathrm{non-protein}} \in \mathbb{R}^{m\times3}$ the $m$ non-protein atom coordinates. The generating flow interpolates between a fully-masked noise distribution ($t=0$) and the data sequence ($t=1$) via a closed-form conditional flow, sampled at inference with Euler steps over a rate matrix (Eq. 1). This follows the discrete flow matching framework of Campbell et al. (2024), distinguished from the autoregressive sampling of earlier inverse-folding models (e.g. Ingraham et al. 2019, Hsu et al. 2022) and from the one-shot independent sampling of PiFold. [SRC-0103, Sec. 3.1]
- **Progressive side-chain incorporation.** Unlike most inverse-folding methods, which ignore side chains, ADFLIP couples sequence sampling with side-chain packing: at each denoising step, newly sampled residues' side-chain conformations $\chi$ are predicted by the external network PIPPACK (Randolph & Kuhlman, 2024) and fed back as structural context for the next step, while masked positions have their side-chain atoms removed to keep sequence and structure representations consistent (Algorithm 1). The authors motivate this by side chains often providing the chemical groups that define ligand/nucleotide/metal interactions. [SRC-0103, Sec. 3.1, Fig. 1]
- **Multi-scale GNN denoiser.** The denoiser $f_\theta$ has residue nodes (one per amino acid or nucleotide) and atom nodes (one per non-hydrogen atom), inspired by AlphaFold3's Transition Block/Fourier embeddings and LigandMPNN's residue encoder. Processing alternates atom-level Local Atom Attention (an Invariant-Point-Attention-like module augmented with frame averaging for rotation robustness) with residue-level message passing (a LigandMPNN-style GNN block modulated by diffusion-time conditioning, following the AdaLN-style time modulation of Peebles & Xie's DiT), connected by averaging (atom→residue) and scattering (residue→atom) operations, plus an optional Context Block that passes information from non-protein atoms to all protein features. A 3-layer Transformer decoder (GeLU activation) applied only to residue nodes produces the final amino-acid logits. [SRC-0103, Sec. 3.2, Fig. 2]
- **Adaptive ("purity") sampling.** Because side chains buried in the protein core often have strongly peaked (low-entropy) predicted amino-acid distributions, ADFLIP computes a per-position "purity score" (max predicted probability) at each step and samples only positions exceeding a threshold $\tau$ first, deferring harder (more ambiguous) positions; any positions that never reach the threshold are sampled independently at a final fallback step (Algorithm 2, Appendix B). The paper notes concurrent work (Peng et al., 2025) uses a similar entropy-based adaptive scheme for masked diffusion sampling. [SRC-0103, Sec. 3.1, App. B]
- **Training-free classifier guidance.** Rather than training a regressor $p(y|s_t)$ on noisy/intermediate sequence states (expensive to retrain, e.g. for AlphaFold2-style confidence scores), ADFLIP estimates the intermediate-state property prediction by taking the expectation of an existing, complete-sequence-only regressor $p_\phi(y|s_1)$ under the denoiser's own output distribution: $\hat p(y|s_t) = \mathbb{E}_{p_\theta(s_1|s_t)}[p_\phi(y|s_1)]$, letting arbitrary pre-trained property predictors be plugged in without retraining or architecture changes (Algorithm 3). Demonstrated with DSMBind (Jin et al., 2024), an unsupervised binding-affinity predictor, to guide generation toward higher-affinity ligand binders. [SRC-0103, Sec. 3.3, Algorithm 3]
- **Ensemble sampling across multiple structural states.** For complexes with multiple known conformations (e.g. an NMR ensemble of $N$ states), ADFLIP runs the denoiser independently on each conformation $x_n$ at each step and averages the resulting per-conformation sequence-probability predictions, $p(\hat s_1) = \frac{1}{N}\sum_n p_n(\hat s_1)$, before sampling and computing the rate matrix (Algorithm 1) — i.e. a single sequence is designed to be jointly consistent with all provided structural states. [SRC-0103, Sec. 3.1, Algorithm 1]
- **Benchmark design.** Training/evaluation follows the LigandMPNN protocol: PDB X-ray/cryo-EM entries deposited after 16 December 2022, resolution better than 3.5 Å, <6,000 residues, clustered at 30% sequence identity via MMseqs2 (since LigandMPNN's own training clusters were not released); the shared LigandMPNN validation/test sets comprise 317 small-molecule-ligand complexes, 74 nucleotide complexes, and 83 metal-ion complexes (training set: 27,818 clusters). A new NMR ensemble benchmark (219 ensembles, avg. 18 conformational states each, PDB entries deposited after January 2015 with >100 residues and ≥2 conformational states, MMseqs2-clustered at 30% identity) was curated for the multi-structure evaluation. [SRC-0103, Sec. 4.1-4.2, App. A]
- **Headline recovery-rate results.** Compared against PiFold, ProteinMPNN (backbone-only), and LigandMPNN (all-atom, retrained on the same clustering), ADFLIP achieves the lowest perplexity and highest recovery rate on interaction residues (within 5.0 Å of non-protein atoms) for all three complex types: ligand (62.19% vs. LigandMPNN 59.21%, ProteinMPNN 54.48%, PiFold 59.20%), nucleotide (50.21% vs. 46.14%, 40.29%, 38.41%), and metal ion (75.73% vs. 69.31%, 54.09%, 47.55%). The authors attribute the large metal-ion gain partly to the chemically conserved identity of metal-coordinating residues (His, Cys, Met, Tyr, Asp, Glu). [SRC-0103, Sec. 4.1, Table 1]
- **Foldability via refolding.** Generated sequences were refolded with Chai-1 (no MSA) and compared to the reference structure by RMSD, TM-score, and pLDDT; a sequence is "foldable" if TM-score ≥ 0.5. ADFLIP modestly improves RMSD over LigandMPNN for all three complex types (ligand: 1.15 vs. 1.21 Å; nucleotide: 5.55 vs. 5.99 Å; metal ion: 2.27 vs. 2.37 Å) and reaches 100% foldability for ligand complexes. Nucleotide complexes remain the hardest case for both methods (RMSD ~5-6 Å, foldability 79-84%). [SRC-0103, Sec. 4.1, Table 2]
- **Multi-structure (NMR) results.** Conditioning on the full NMR ensemble rather than a single (most-interacting) conformation, using the same trained model with no fine-tuning, improved recovery rate by 8.6 percentage points for ligand interactions and 5.8 points for nucleotide interactions; the metal-ion improvement was smaller (2.6 points), which the authors attribute to metal-binding sites remaining relatively conformationally stable even across the NMR ensemble. Average foldability RMSD dropped from 9.11 Å (single structure) to 7.61 Å (full ensemble), though absolute foldability on this dynamic-complex benchmark remains markedly worse than the static-structure benchmark. [SRC-0103, Sec. 4.2, Tables 3-4]
- **Guidance results.** On 210 single-ligand test complexes, using DSMBind to target a 10% binding-affinity improvement over wild type, training-free guidance raised the fraction of generated sequences exceeding the wild-type predicted affinity ("affinity gain") from 41.9% (unguided ADFLIP) to 58.1% (guided), while foldability dropped from 100% to 91.4%. The authors note the gain is currently limited because the protein backbone is held fixed and side-chain sampling is limited; refining the backbone jointly with the sequence is proposed as future work. [SRC-0103, Sec. 4.3, Table 5]
- **Qualitative structural comparisons (Fig. 3).** Refolded, ADFLIP-designed sequences are shown qualitatively to outperform ProteinMPNN/LigandMPNN on three case studies: a helix-loop-helix DNA-binding transcriptional activator (PDB 1AM9), an HNH homing endonuclease (PDB 1U3E), and the inhibitor-binding pocket of Factor Xa (PDB 2UWP), where the refolded ligand docks closer to the reference pocket for the ADFLIP-designed protein than for the baselines. [SRC-0103, Sec. 4.1, Fig. 3]

## Evidence

**Table 1 — Interaction-residue recovery rate on all-atom complex structures** (residues within 5.0 Å of non-protein atoms; 10 sampled sequences per complex, mean recovery rate):

| Metric / Model | Ligand | Nucleotide | Metal Ion |
| --- | --- | --- | --- |
| **Perplexity ↓** | | | |
| PiFold | 4.03 | 7.26 | 7.55 |
| ProteinMPNN | 4.46 | 6.48 | 4.59 |
| LigandMPNN | 3.84 | 4.97 | 2.73 |
| ADFLIP | 3.57 | 4.86 | 2.61 |
| **Recovery Rate (%) ↑** | | | |
| PiFold | 59.20 | 38.41 | 47.55 |
| ProteinMPNN | 54.48 | 40.29 | 54.09 |
| LigandMPNN | 59.21 | 46.14 | 69.31 |
| ADFLIP | 62.19 | 50.21 | 75.73 |

[SRC-0103, Table 1]

**Table 2 — Generated-sequence structure vs. native structure** (Chai-1 refolding without MSA; foldable if TM-score ≥ 0.5):

| Model | RMSD (Å) | TM-score | pLDDT | Foldability |
| --- | --- | --- | --- | --- |
| **Small Molecule** | | | | |
| LigandMPNN | 1.21 | 0.95 | 94.6 | 98.8% |
| ADFLIP | 1.15 | 0.96 | 90.6 | 100.0% |
| **Nucleotide** | | | | |
| LigandMPNN | 5.99 | 0.76 | 84.7 | 79.4% |
| ADFLIP | 5.55 | 0.77 | 87.5 | 83.5% |
| **Metal Ions** | | | | |
| LigandMPNN | 2.37 | 0.79 | 97.85 | 83.7% |
| ADFLIP | 2.27 | 0.78 | 98.38 | 85.1% |

[SRC-0103, Table 2]

**Table 3 — Recovery-rate performance on the NMR ensemble dataset** (219 ensembles, avg. 18 conformational states; "Single" = most-interacting conformation only, "Multiple" = full ensemble):

| Metric / Model | Ligand | Nucleotide | Metal Ion |
| --- | --- | --- | --- |
| **Perplexity ↓** | | | |
| LigandMPNN | 7.82 | 9.37 | 3.27 |
| ADFLIP (single) | 7.34 | 8.71 | 3.12 |
| ADFLIP (multiple) | 5.58 | 6.91 | 2.69 |
| **Recovery Rate (%) ↑** | | | |
| LigandMPNN | 40.58 | 32.63 | 64.82 |
| ADFLIP (single) | 41.48 | 34.48 | 65.44 |
| ADFLIP (multiple) | 50.08 | 40.33 | 68.01 |

[SRC-0103, Table 3]

**Table 4 — Generated-sequence structure vs. native structure, NMR dataset** (predicted structure compared to the lowest-RMSD member of the original NMR ensemble):

| Model | RMSD (Å) | TM-score | pLDDT | Foldability |
| --- | --- | --- | --- | --- |
| LigandMPNN | 8.34 | 0.68 | 78.4 | 84.5% |
| ADFLIP (single) | 9.10 | 0.67 | 79.5 | 81.7% |
| ADFLIP (multiple) | 7.21 | 0.69 | 80.19 | 82.5% |

[SRC-0103, Table 4]

**Table 5 — Ligand-binding-affinity-guided generation results** (210 single-ligand test complexes; target = 10% improvement over wild-type DSMBind-predicted affinity; 10 sequences generated per structure):

| Model | Affinity gain | Foldability |
| --- | --- | --- |
| ADFLIP (unguided) | 41.9% | 100% |
| ADFLIP (guided) | 58.1% | 91.4% |

[SRC-0103, Table 5]

## Equation inventory

| Equation / label | Source location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- |
| Conditional flow | unnumbered, Sec. 3.1, p.3 | Closed-form conditional flow interpolating from the mask token to the target sequence | $p_{t\|1}(s_t\|s_1)$, $\mathfrak{m}$, $\delta\{\cdot,\cdot\}$, $t\in[0,1]$ | Defines the forward corruption process used to generate training noise $s_t$ |
| Marginal distribution | unnumbered, Sec. 3.1, p.3 | Marginal $p_t(s_t)$ as expectation of the conditional flow over the data distribution | $p_t(s_t)$, $p_{\mathrm{data}}(s_1)$ | Establishes the generative target the rate matrix must reproduce |
| Transition probability | unnumbered, Sec. 3.1, p.3 | Infinitesimal-time transition probability via the rate matrix $R_t$ | $p_{t+dt\|t}(j\|s_t)$, $R_t(s_t,j)$ | Defines the continuous-time Markov-chain sampling process |
| Euler sampling step | Eq. 1, Sec. 3.1, p.3 | Finite-$\Delta t$ discretization of the rate-matrix sampling process used at inference | $s_{t+\Delta t}$, $\mathrm{Cat}(\cdot)$, $R_t(s_t,s_{t+\Delta t})$ | The actual sampling update used in Algorithms 1-3 |
| Rate matrix as expectation | unnumbered, Sec. 3.1, p.3 | Marginal rate matrix as expectation of a simpler conditional rate matrix over the denoiser's posterior | $R_t(s_t,j)$, $p_{1\|t}(s_1\|s_t)$ | Shows how the learned denoiser $p_{1\|t}$ is converted into a sampling rate matrix |
| Conditional rate matrix | unnumbered, Sec. 3.1, p.3 | Closed form of the conditional rate matrix for the mask-absorbing process | $R_t(s_t,j\|s_1) = \delta\{s_1,j\}\delta\{s_t,\mathfrak{m}\}/(1-t)$ | Direct implementation formula combined with the learned $p_{1\|t}$ to get $R_t(s_t,j)$ |
| Training (cross-entropy) loss | unnumbered, Sec. 3.1, p.4 | Loss used to train the denoiser $f_\theta$ to approximate $p_{1\|t}(s_1\|s_t,x,\chi_t)$ | $\mathcal{L}_{\mathrm{CE}}$, $p_{\mathrm{data}}(s_1)$, $U(t;0,1)$, $\chi_t$ | Top-level training objective; transcribed as printed (labelled a cross-entropy loss; see Mathematical gaps) |
| Guidance expectation | unnumbered, Sec. 3.3, p.6 | Estimates a complete-sequence regressor's prediction for an intermediate (masked) state by taking its expectation under the denoiser's own output | $\hat p(y\|s_t)$, $p_\theta(s_1\|s_t)$, $p_\phi(y\|s_1)$ | Core mechanism enabling training-free classifier guidance with arbitrary pre-trained regressors |
| Guidance pseudo-gradient (Algorithm 3) | unnumbered, Sec. 3.3/App. C | Approximates the guidance likelihood from the discrepancy between predicted and target property values | $p(y\|s_1) \approx -\nabla_{s_1}\lVert y-\hat y\rVert^2$, $\hat y = h_\phi(p(\hat s_1))$ | Used to reweight $p(\hat s_1)$ toward the target property $y$ during guided sampling |

## Mathematical gaps

- The full architectural equations for the multi-scale GNN denoiser (Local Atom Attention/frame averaging, the Fourier and word embedding layers of the Atom Encoder, the Residue Encoder's radial-basis distance/tetrahedral-angle features, the GNN Block's diffusion-time modulation, and the 3-layer Transformer decoder) are described qualitatively in the source (Sec. 3.2, Fig. 2) rather than given as explicit numbered equations; the paper itself does not provide closed-form equations for these components beyond prose description and the cited external modules (AlphaFold3's Transition Block/Invariant Point Attention, LigandMPNN's message-passing GNN, frame averaging per Puny et al. 2021/Huang et al. 2024, diffusion-time modulation per Peebles & Xie 2023). No information is lost relative to the source by this qualitative summary; a reader needing the literal architecture should consult the cited external papers and the released code (`github.com/ykiiiiii/ADFLIP`). [SRC-0103, Sec. 3.2]
- The training-loss equation ($\mathcal{L}_{\mathrm{CE}}$, Sec. 3.1) is transcribed exactly as printed in the source, which displays it as an expectation of $\log p_\theta^{1\|t}(s_1\|s_t,x,\chi_t)$ without an explicit leading minus sign, despite being described in prose as a "cross-entropy loss" (which is conventionally minimized as the *negative* log-likelihood); this is noted as a probable typesetting omission in the source rather than corrected, since the ingestion does not alter transcribed equations. [SRC-0103, Sec. 3.1]
- Algorithm 2's adaptive purity-sampling time increment ($t \leftarrow t + |I|/L$) and Algorithm 3's guidance-weighted sampling ($s_1 \sim p(\hat s_1)\,p(y\|\hat s_1)$) are reproduced here only as prose/algorithm-structure descriptions, not as a separate inventory row each, since they are direct applications of the equations already listed above.

## Limitations and Caveats

- Designed sequences have not been experimentally validated (synthesized, expressed, or assayed); all evaluation is computational (refolding with Chai-1, a structure predictor, and binding-affinity prediction with DSMBind, an unsupervised predictor). The authors explicitly flag this in the paper's Impact Statement. [SRC-0103, Impact Statement]
- Nucleotide-complex recovery and foldability remain substantially lower than for ligand or metal-ion complexes (e.g. Table 1: 50.21% vs. 62.19%/75.73% recovery; Table 2: ~5.5 Å vs. ~1.2-2.3 Å RMSD) even with ADFLIP's all-atom conditioning, which the authors attribute to possibly insufficient capture of the inherently higher conformational dynamics of nucleotide complexes by a single structure. [SRC-0103, Sec. 4.1-4.2, Sec. 5]
- The protein backbone is held fixed throughout generation; ADFLIP does not perform structural refinement jointly with sequence design. The authors note this limits the binding-affinity-guidance results specifically (Sec. 4.3) and propose future integration of backbone flexibility, citing RNAflow's integration with RosettaFold2NA as a template approach. [SRC-0103, Sec. 4.3, Sec. 5]
- Binding-affinity guidance trades off foldability for affinity gain (foldability drops from 100% unguided to 91.4% guided), and the achievable affinity improvement is described by the authors as "currently limited" by the fixed backbone and limited side-chain sampling. [SRC-0103, Sec. 4.3, Table 5]
- The large metal-ion recovery-rate advantage is explained post hoc by the conserved chemical identity of metal-coordinating residues (His, Cys, Met, Tyr, Asp, Glu); this is offered as a plausible mechanistic explanation by the authors, not independently validated in the paper. [SRC-0103, Sec. 4.1]
- Foldability assessment uses Chai-1 without multiple-sequence-alignment (MSA) information, and the TM-score ≥ 0.5 foldability threshold is a modelling convention, not a guarantee of biological function or stability. [SRC-0103, Sec. 4.1]
- PIPPACK (external side-chain packing network) and Chai-1/DSMBind (external evaluation and guidance models) are used as fixed, pre-trained components; their own accuracy and limitations are not characterized within this paper and are inherited by ADFLIP's downstream results. [SRC-0103, Sec. 3.1, 4.1, 4.3]

## Open Questions

- How should one best obtain a representative set of useful conformational states for protein-nucleotide complexes specifically (or any dynamic biomolecular complex in general) to use as ADFLIP's multi-structure input, given that NMR ensembles are not universally available? [SRC-0103, Sec. 5]
- Would integrating backbone structural refinement into the sequence-generation process (as in RNAflow/RosettaFold2NA) improve both baseline design quality and guided (e.g. binding-affinity) generation, as the authors speculate? [SRC-0103, Sec. 4.3, Sec. 5]
- Why does a single conformational state appear insufficient for nucleotide-complex design specifically, relative to ligand and metal-ion complexes — is this a property of nucleotide-binding interface dynamics, dataset size/diversity, or a limitation of the current architecture? [SRC-0103, Sec. 5]
- The paper frames ADFLIP as a step toward functional protein design but does not test generated sequences experimentally; it remains open whether the computational recovery/foldability/affinity-gain improvements translate into experimentally validated, functional designs. [SRC-0103, Impact Statement]

## Claims

- [[wiki/claims/CLM-0059-adflip-all-atom-and-multi-conformation-conditioning-improves-inverse-folding-recovery]]
- [[wiki/claims/CLM-0060-adflip-training-free-guidance-improves-affinity-targeted-generation-with-limited-gains]]

## Links

- [[wiki/concepts/adflip-discrete-flow-matching-inverse-folding]]
- [[wiki/sources/SRC-0104-de-novo-design-of-protein-structure-and-function]]

## Citation Links

- SRC-0103's reference list cites "Yim, J., Eisenach, H. E., Ahern, W., Borst, A. J., Ragotte, R. J., Milles, L. F., et al. De novo design of protein structure and function with rfdiffusion. Nature, 620(7976): 1089-1100, 2023" — an exact venue/volume/page match to the now-ingested [[wiki/sources/SRC-0104-de-novo-design-of-protein-structure-and-function]] (RFdiffusion). The citation appears in SRC-0103's bibliography as general related-work context (both papers are protein-design generative models), not as a methodological dependency discussed in SRC-0103's main text; RFdiffusion generates a protein backbone de novo, while ADFLIP designs a sequence for an already-specified structure, so the two address complementary stages of a typical design pipeline. [SRC-0103 bibliography; SRC-0104]
- SRC-0103 builds directly on LigandMPNN (Dauparas et al., 2023, "Atomic context-conditioned protein sequence design using ligandmpnn," bioRxiv) for its dataset-curation protocol, train/validation/test clustering baseline, and as its primary comparison method; LigandMPNN is not currently ingested as a separate SecondBrain source. [SRC-0103, Sec. 4.1, App. A]
- SRC-0103 compares against ProteinMPNN (Dauparas et al., 2022, *Science*) and PiFold (Gao et al., 2023b, ICLR); neither is currently ingested as a separate SecondBrain source. [SRC-0103, Sec. 4.1]
- SRC-0103 follows the discrete flow matching framework of Campbell, Yim, Barzilay & Jaakkola (2024, ICML, "Generative flows on discrete state-spaces"); not currently ingested. [SRC-0103, Sec. 2, Sec. 3.1]
- SRC-0103's GNN denoiser architecture is explicitly inspired by AlphaFold3 (Abramson et al., 2024, *Nature*, "Accurate structure prediction of biomolecular interactions with alphafold 3") and reuses components from LigandMPNN; neither AlphaFold3 nor LigandMPNN is currently ingested as a separate SecondBrain source. [SRC-0103, Sec. 3.2]
- Side-chain packing uses the external network PIPPACK (Randolph & Kuhlman, 2024, "Invariant point message passing for protein side chain packing," *Proteins*); binding-affinity guidance uses DSMBind (Jin et al., 2024, NeurIPS, "Unsupervised protein-ligand binding energy prediction via neural euler's rotation equation"); foldability evaluation uses Chai-1 (Chai Discovery, 2024, bioRxiv). None of these is currently ingested as a separate SecondBrain source. [SRC-0103, Sec. 3.1, 3.3, 4.1]
- Of SRC-0103's ~40 references, one matches a source now ingested in SecondBrain: the RFdiffusion paper (now [[wiki/sources/SRC-0104-de-novo-design-of-protein-structure-and-function]], confirmed exact venue/volume/page match, found 2026-10-12). No other reference was found to match SecondBrain's other existing machine-learning-for-biomolecules sources (e.g. SRC-0098 graph-nets partial charge prediction, SRC-0101/SRC-0102 Grappa, SRC-0086/SRC-0087 Breaking Timescales); the rest of SRC-0103's citation network (inverse protein folding / discrete generative models) remains largely separate from SecondBrain's otherwise force-field-focused machine-learning coverage. [SRC-0103]

## Metadata notes

- Published at the 42nd International Conference on Machine Learning (ICML 2025), PMLR vol. 267; also posted as arXiv:2507.14156 [q-bio.BM], 4 Jul 2025. Peer-reviewed conference proceedings. [SRC-0103]
- Affiliation: MRC Laboratory of Molecular Biology, Cambridge, UK; corresponding author Sjors H. W. Scheres. Funding: UK Medical Research Council (MC_UP_A025_1013). [SRC-0103]
- Code released at `github.com/ykiiiiii/ADFLIP`. [SRC-0103]
- No DOI is given in the PDF; the arXiv identifier is used as the primary bibliographic locator. [SRC-0103]

## Ingestion QA

### Retrieval questions checked

- What problem does ADFLIP solve, and how does it differ from prior inverse-folding approaches (autoregressive, one-shot, backbone-only)?
- What is the discrete flow matching formalism ADFLIP uses, and how is a sequence sampled from it at inference?
- How does ADFLIP's multi-scale GNN denoiser combine atom-level and residue-level information, and what external architectures does it draw on?
- How does ADFLIP incorporate side-chain information during generation, and why does this matter for ligand/nucleotide/metal-ion design?
- What benchmark datasets and metrics were used, and what were the headline recovery-rate/perplexity results against PiFold, ProteinMPNN, and LigandMPNN?
- How does ADFLIP handle structurally dynamic complexes (multiple conformational states), and what improvement does ensemble conditioning give on the NMR benchmark?
- What is ADFLIP's training-free classifier guidance mechanism, and what result does it achieve for binding-affinity-guided generation?
- What are the main limitations the authors acknowledge, and what future work do they propose?

### Coverage decision

Complete at `coverage_profile: math-standard`. The source page captures the discrete flow matching formalism and sampling algorithm (with a curated equation inventory), the three-component architecture (flow model, multi-scale GNN denoiser, training-free guidance), the adaptive purity-sampling scheme, all five main-text result tables transcribed in full (per the standing preference for benchmark-heavy papers), the qualitative case-study figure, limitations, and open questions. The full low-level GNN architectural equations (not given in closed form by the source itself) are recorded as a mathematical gap rather than invented.

### Known gaps

- Appendix D's PDB ID lists (small-molecule, nucleotide, metal-ion, and NMR benchmark entries), the crystallisation-aid/excluded-ligand CCD code lists, and the glycan CCD code list are not transcribed here; they are long identifier enumerations rather than analytical content, and are available in full in the raw source PDF (pp. 12-14) if specific entries need to be checked. [SRC-0103, App. D]
- Figure 1 (schematic overview) and Figure 3 (qualitative refolding comparison renders) are described from their captions rather than reproduced visually. [SRC-0103, Fig. 1, Fig. 3]
- Of this paper's ~40 cited references, only the RFdiffusion paper (SRC-0104) is currently ingested as a separate SecondBrain source (see Citation Links); `cites_sources` lists it, and `citation_match_status: partial` reflects that the remaining references are not ingested.
