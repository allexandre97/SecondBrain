---
type: concept
status: active
created: 2026-10-12
updated: 2026-10-12
areas:
  - research
categories:
  - research/biomolecules/proteins
  - research/machine-learning/molecular-modeling
  - research/experimental-benchmarking
tags:
  - protein-design
  - diffusion-model
  - generative-model
  - structure-prediction
  - symmetric-oligomers
  - binder-design
  - motif-scaffolding
related:
  - "[[wiki/sources/SRC-0104-de-novo-design-of-protein-structure-and-function]]"
  - "[[wiki/concepts/adflip-discrete-flow-matching-inverse-folding]]"
sources:
  - SRC-0104
sensitivity: public
encryption: none
---

# RFdiffusion: Diffusion-Based De Novo Protein Design

## Summary

RFdiffusion is a denoising diffusion probabilistic model (DDPM) for de novo protein *backbone* design, built by fine-tuning the RoseTTAFold (RF) structure-prediction network to reverse a noising process applied to protein backbone coordinates and orientations, instead of predicting structure from sequence. Starting from random residue frames, iterative denoising produces diverse, novel protein backbones; sequences are then designed for these backbones with ProteinMPNN. A single architecture and training recipe (with task-specific fine-tuning and optional auxiliary conditioning) spans unconditional monomer generation, fold-conditioned generation, symmetric-oligomer design of any point-group symmetry, functional-motif scaffolding (including enzyme active sites), symmetric motif/metal-binding-site scaffolding, and target-conditioned protein-binder design, each validated computationally and experimentally. [SRC-0104]

## Key Points

- **Repurposing a structure-prediction network as a generative denoiser.** RFdiffusion keeps RF's SE(3)-equivariant rigid-frame residue representation and conditioning machinery, but swaps the primary input from sequence (RF structure prediction) to noised/diffused coordinates (RFdiffusion), training with an MSE loss (not the FAPE loss used for RF prediction) so that the global coordinate frame stays continuous across denoising steps. Fine-tuning from pretrained RF weights, rather than training from scratch for equivalent compute, is empirically essential to good performance. [SRC-0104, p. 1090, Extended Data Fig. 1F-G]
- **Self-conditioning improves generation.** Letting the model condition on its own previous-step prediction (analogous to AF2 "recycling") measurably improves in silico success on both unconditional and conditional tasks; the effect is attributed at least partly to increased coherence between denoising steps. [SRC-0104, p. 1090, Extended Data Fig. 1E]
- **One framework, many design problems.** The same denoising process accepts different auxiliary conditioning — none for unconditional generation, secondary-structure/block-adjacency ("fold") information for topology control, point-group symmetry specifications (with explicit resymmetrization each step) for oligomers, 3D functional-motif coordinates (with side chains) for motif scaffolding, or target-structure "interface hotspot" residues (plus optional fold conditioning) for binder design. [SRC-0104, Fig. 1b]
- **Outperforms prior deep-learning design methods.** Against RF Hallucination (Monte Carlo/gradient-descent sequence search) and RFjoint Inpainting (the authors' earlier deterministic single-step motif-scaffolding method), RFdiffusion wins decisively on the AF2-based in silico success metric for unconditional generation (z = 9.5, p = 1.6 × 10⁻²¹) and solves 23/25 vs. 15/25 (Hallucination) and 19/25 (RFjoint) problems on a 25-problem motif-scaffolding benchmark, while also being far more compute-efficient (seconds vs. minutes per design) and requiring no problem-specific hyperparameter tuning. [SRC-0104, p. 1091, 1094]
- **Symmetric assemblies beyond cyclic symmetry.** Unlike prior Hallucination-based symmetric-assembly design (limited to cyclic symmetries), RFdiffusion generates cyclic, dihedral, tetrahedral, and icosahedral assemblies without having been trained on symmetric inputs, by replicating and resymmetrizing a single monomer's frames at each step; several resulting topologies (e.g. expanded "TIM-barrel-like" cyclic barrels, a C10 two-layer beta barrel) are not represented in the PDB. [SRC-0104, p. 1092-1093]
- **Experimentally dominant binder-design success rate.** Fine-tuned on protein complexes with target "hotspot" conditioning, RFdiffusion plus AF2-based filtering raised experimental binder hit rates by roughly two orders of magnitude over a prior physics-based (Rosetta) method on the same four shared targets, identifying binders from fewer than 100 designs per target where the prior method needed thousands. [SRC-0104, p. 1097]
- **Atomic-accuracy confirmation by cryo-EM.** A designed influenza-haemagglutinin binder (HA_20, 28 nM affinity) was solved in complex with HA by cryo-EM at 2.9 Å resolution; the experimental structure matches the RFdiffusion design model to 0.63 Å backbone RMSD over the complex. [SRC-0104, p. 1098]
- **Acknowledged limitations.** RFdiffusion cannot currently model bound small-molecule ligands explicitly (only implicitly, via an external pocket potential); binder-design specificity and generalization to polar/novel-site targets are only partially characterized; large unconditional designs (>~600 residues) are difficult to validate even in silico. The authors propose extending the underlying RF architecture to nucleic acids and ligand atoms as future directions. [SRC-0104, p. 1096, 1098-1099]
- **Relation to inverse-folding generative models (ADFLIP).** RFdiffusion generates a protein *backbone* de novo and hands sequence design off to a separate network (ProteinMPNN); ADFLIP ([[wiki/concepts/adflip-discrete-flow-matching-inverse-folding]], SRC-0103) instead solves the complementary *inverse-folding* problem — designing a sequence for an already-specified (all-atom, possibly multi-conformation) structure. SRC-0103 cites this RFdiffusion paper (exact venue/volume/page match) as related protein-design generative-modelling work, but does not build on its methodology directly; the two represent different stages of a typical structure-then-sequence design pipeline, and both use diffusion/flow-based generative modelling applied to the protein-design problem. [SRC-0103 bibliography; SRC-0104]

## Evidence

- Unconditional-generation vs. Hallucination success: z = 9.5, p = 1.6 × 10⁻²¹ (n = 400/condition). [SRC-0104, Fig. 2d]
- Motif-scaffolding benchmark: RFdiffusion 23/25, RFjoint Inpainting 19/25, Hallucination 15/25 problems solved. [SRC-0104, p. 1094]
- Binder design: ~19% overall experimental hit rate across 5 targets (HA, IL-7Rα, PD-L1, InsR, TrkA), roughly two orders of magnitude above the prior Rosetta-based method on the four shared targets. [SRC-0104, p. 1097]
- Cryo-EM structure of HA_20/HA complex: 2.9 Å map, 0.63 Å RMSD to the design model. [SRC-0104, p. 1098]
- Metal-binding design: 18/36 ITC-tested C4 oligomers bound Ni²⁺ at the designed 1:4 stoichiometry; H52A mutation abolished/reduced binding in 17/17 testable cases. [SRC-0104, p. 1096]

Further per-task numeric results (symmetric-oligomer SEC/nsEM validation counts, enzyme-active-site RMSD/pAE metrics, individual binder Kd values) are transcribed on the source page. [[wiki/sources/SRC-0104-de-novo-design-of-protein-structure-and-function]]

## Links

- [[wiki/sources/SRC-0104-de-novo-design-of-protein-structure-and-function]]
- [[wiki/claims/CLM-0061-rfdiffusion-self-conditioning-and-mse-loss-are-necessary-for-design-quality]]
- [[wiki/claims/CLM-0062-rfdiffusion-raises-binder-design-success-two-orders-of-magnitude-with-cryo-em-confirmed-accuracy]]
- [[wiki/concepts/adflip-discrete-flow-matching-inverse-folding]]

## Caveats

- No bound small-molecule ligand can currently be explicitly modelled during generation; enzyme active-site scaffolding only implicitly accounts for a substrate via an external Cα-level pocket potential. [SRC-0104, p. 1096]
- Binder-design specificity was tested for only 6 of many designs (competition BLI against a validated positive control); proteome-wide specificity is explicitly flagged by the authors as unassessed. [SRC-0104, p. 1098]
- All five binder-design targets in this study were characterized by the authors as "non-polar sites"; generalization to more polar or native-partner-free targets is untested here. [SRC-0104, p. 1098]
- The explicit mathematical formalism (noising/denoising equations, self-conditioning interpolation formula, potential functional forms) lives in a separately published Supplementary Methods document not available in the ingested PDF; see the source page's Mathematical gaps. [SRC-0104]

## Open Questions

- How much of the gap between in silico success and experimental success at each design stage (backbone generation, ProteinMPNN sequence design, AF2 filtering, expression) is attributable to which stage? [SRC-0104, implicit]
- How well does RFdiffusion binder design generalize to polar target sites or targets without known native binding partners? [SRC-0104, p. 1098]
- How accurately do the proposed extensions (nucleic-acid binding design, explicit ligand/small-molecule modelling via extended RF architectures) perform once implemented? [SRC-0104, p. 1099]
