---
type: source
status: active
created: 2026-10-12
updated: 2026-10-12
source_id: SRC-0104
display_title: "De novo design of protein structure and function with RFdiffusion"
short_title: "RFdiffusion"
aliases:
  - "SRC-0104"
  - "RFdiffusion"
  - "RoseTTAFold diffusion"
source_path: raw/sources/SRC-0104-de-novo-design-of-protein-structure-and-function.pdf
imported_path: raw/sources/SRC-0104-de-novo-design-of-protein-structure-and-function.pdf
original_filename: "s41586-023-06415-8.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: c881805616f7034577682a0b38b043f379a9973aaf02aec2393ab91c79fddc58
authors:
  - "Joseph L. Watson"
  - "David Juergens"
  - "Nathaniel R. Bennett"
  - "Brian L. Trippe"
  - "Jason Yim"
  - "Helen E. Eisenach"
  - "Woody Ahern"
  - "Andrew J. Borst"
  - "Robert J. Ragotte"
  - "Lukas F. Milles"
  - "Basile I. M. Wicky"
  - "Nikita Hanikel"
  - "Samuel J. Pellock"
  - "Alexis Courbet"
  - "William Sheffler"
  - "Jue Wang"
  - "Preetham Venkatesh"
  - "Isaac Sappington"
  - "Susana Vázquez Torres"
  - "Anna Lauko"
  - "Valentin De Bortoli"
  - "Emile Mathieu"
  - "Sergey Ovchinnikov"
  - "Regina Barzilay"
  - "Tommi S. Jaakkola"
  - "Frank DiMaio"
  - "Minkyung Baek"
  - "David Baker"
author_entities: []
year: 2023
venue: "Nature"
doi: "10.1038/s41586-023-06415-8"
arxiv:
metadata_review_status: reviewed
source_bundle:
bundle_role: main
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
  - metal-binding-protein
  - cryo-em
sources:
  - SRC-0104
related:
  - "[[wiki/sources/SRC-0103-all-atom-inverse-protein-folding-discrete-flow-matching]]"
cites_sources: []
citation_match_status: partial
cqt_review_status: linked
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: standard
peer_review_status: peer-reviewed
---

# De novo design of protein structure and function with RFdiffusion

Source ID: `SRC-0104`

## Raw source

- Repository path: `raw/sources/SRC-0104-de-novo-design-of-protein-structure-and-function.pdf`
- Open raw source: [raw/sources/SRC-0104-de-novo-design-of-protein-structure-and-function.pdf](../../raw/sources/SRC-0104-de-novo-design-of-protein-structure-and-function.pdf)
- The imported PDF is the published Nature "Article" plus Extended Data figures/table and the Nature Portfolio Reporting Summary cover page; it does not include the separately published Supplementary Information (full Supplementary Methods, Supplementary Tables, Supplementary Figures), so equations and some numeric tables referenced in-text (e.g. "Supplementary Methods 2.4/2.5/4.4/4.5", "Supplementary Table 1/9/10") are not present in this file. See Mathematical gaps and Known gaps.

## Summary

Watson, Juergens, Bennett, Trippe, Yim, Eisenach, Ahern et al. (Institute for Protein Design, University of Washington, with MIT and University of Cambridge collaborators; corresponding author David Baker) introduce **RFdiffusion** (RoseTTAFold diffusion), a denoising diffusion probabilistic model (DDPM) for de novo protein design built by fine-tuning the RoseTTAFold (RF) structure-prediction network as a structure denoiser. Rather than predicting structure from sequence (as in ordinary RF/AlphaFold2 structure prediction), RFdiffusion is trained to reverse a noising process applied to protein backbones (Cα coordinates perturbed with 3D Gaussian noise; residue orientations perturbed by Brownian motion on the manifold of rotation matrices), so that starting from random noise it can generate diverse, novel protein backbones through iterative denoising. Generated backbones are then assigned sequences with the existing ProteinMPNN network. The paper demonstrates one unified generative framework across five previously disparate design problems — unconditional monomer generation, fold-conditioned monomer generation, symmetric oligomer design (any point-group symmetry), functional-motif scaffolding (including enzyme active sites), symmetric functional-motif scaffolding (including metal-binding sites), and target-conditioned protein-binder design — and backs each with extensive experimental characterization (circular dichroism, size-exclusion chromatography, negative-stain and cryogenic electron microscopy, biolayer interferometry, isothermal titration calorimetry), including a 2.9 Å cryo-EM structure of a designed influenza-haemagglutinin binder that matches the design model to 0.63 Å RMSD. [SRC-0104]

## Key Points

- **Architecture: RF fine-tuned as a denoiser.** RFdiffusion reuses RoseTTAFold's rigid-frame residue representation (a Cα coordinate plus N-Cα-C orientation per residue) and its architecture for conditioning on sequence, templates, and 3D coordinates, but repurposes it: in RF structure prediction, sequence is the primary input with structure provided as auxiliary template/recycled-coordinate information; in RFdiffusion, the noised/diffused residue frames become the primary input, with sequence, partial structure, fold information, or functional-motif coordinates available as auxiliary conditioning. Other equivariant structure-prediction networks (AlphaFold2, OmegaFold, ESMFold) are noted as substitutable in principle. [SRC-0104, p. 1090]
- **Noising and training.** Forward noising perturbs Cα coordinates with 3D Gaussian noise (translations) and applies Brownian motion on the SO(3) manifold of rotation matrices to residue orientations (building on prior Riemannian score-based/SO(3) diffusion work), over up to 200 steps, using structures sampled from the PDB. The model is trained with a per-residue mean-squared-error (MSE) loss between frame predictions and the true structure (no alignment), rather than the frame-aligned point error (FAPE) loss used for RF structure-prediction training; unlike FAPE, MSE is not invariant to the global reference frame, which the authors argue promotes continuity of the coordinate frame across denoising timesteps. [SRC-0104, p. 1090]
- **Self-conditioning.** Two training strategies were compared: "canonical" diffusion, where the denoising prediction at each timestep is independent of previous-timestep predictions, versus self-conditioning (after Chen, Zhang & Hinton, 2023), where the model also receives its own previous-timestep prediction as an extra template-like input, analogous to AlphaFold2-style "recycling." Self-conditioning measurably improved in silico success on both conditional and unconditional benchmarks. [SRC-0104, p. 1090]
- **Fine-tuning from pretrained RF weights matters.** Ablations show fine-tuning RFdiffusion from pretrained RF structure-prediction weights substantially outperforms training an equivalent amount of compute from untrained weights; MSE loss (vs. FAPE) and self-conditioning are each independently important for unconditional-generation quality (two-proportion z-tests reported, e.g. MSE-vs-FAPE z = 4.1, p = 4.1 × 10⁻⁵; self-conditioning z = 11.4, p = 6.1 × 10⁻³⁰). For motif-scaffolding problems, where the motif itself anchors the global coordinate frame across timesteps, FAPE performs about as well as MSE, suggesting MSE's benefit is specifically about frame continuity, not its L2 (vs. FAPE's L1) functional form. [SRC-0104, Extended Data Fig. 1D-G]
- **In silico "success" metric.** For all in silico benchmarks, a design is scored by feeding the ProteinMPNN-designed sequence into AlphaFold2 (AF2) structure prediction and requiring (1) AF2 mean predicted aligned error (pAE) < 5, (2) AF2-vs-design backbone RMSD < 2 Å globally, and (3) AF2-vs-design backbone RMSD < 1 Å on any scaffolded functional site. The authors report this correlates with experimental success and is markedly more stringent than TM-score-based metrics used in some prior work. [SRC-0104, p. 1091]
- **Unconditional monomer generation.** RFdiffusion generates diverse, PDB-novel monomers up to ~600 residues (divergence from the PDB, measured by highest TM-score to known structures, increases with length), closely re-predicted by AF2 up to ~400 residues. Six 300-residue and three 200-residue designs were experimentally characterized by circular dichroism: all showed spectra consistent with the design's mixed alpha-beta topology and were "extremely thermostable." RFdiffusion strongly outperforms Hallucination-with-RF on the AF2 success metric at unconditional generation (two-proportion z-test, n = 400 designs/condition, z = 9.5, p = 1.6 × 10⁻²¹) and is far more compute-efficient (a 100-residue design in ~11 s on an NVIDIA RTX A4000 GPU vs. ~8.5 min for RF Hallucination). Fine-tuning on secondary-structure/block-adjacency ("fold") information enabled fold-constrained generation, e.g. TIM barrels (42.5% in silico success) and NTF2 folds (54.1%); 8 of 11 experimentally tested TIM-barrel designs were soluble, thermostable, and CD-consistent with the design model. [SRC-0104, p. 1091-1092]
- **Symmetric oligomer design.** Given a point-group symmetry specification and chain length, RFdiffusion generates one monomer's random starting frames, replicates them under the specified symmetry, and explicitly resymmetrizes predictions at each denoising step (RFdiffusion's equivariance keeps deviation from exact symmetry small); for octahedral/icosahedral symmetries only the minimal generating subset of chains is modelled explicitly to reduce cost. Despite never being trained on symmetric inputs, RFdiffusion generates high-success cyclic, dihedral, tetrahedral, and icosahedral assemblies, several with topologies not seen in the PDB (e.g. a C10 two-layer beta barrel; expanded "TIM-barrel-like" cyclic oligomers, such as an 18-strand/18-helix C6 barrel and a 16/16 C8 barrel). Of 608 oligomer designs selected for experimental testing, size-exclusion chromatography (SEC) was consistent with the intended oligomeric state for at least 87 (within 95% CI; 126 within 99% CI). Negative-stain EM (nsEM) 2D class averages and 3D reconstructions for a subset (C3, C5, C6, C8, D3, D4, a 12-chain tetrahedron, and a 15 nm icosahedral assembly, HE0902) closely matched design models; a D4 design (HE0537) was additionally confirmed by cryo-EM. [SRC-0104, p. 1092-1093]
- **Functional-motif scaffolding.** Motifs (3D coordinates including sequence and side chains) are provided as input during both conditional training and inference; RFdiffusion builds a scaffold holding the motif atoms in the required geometry. On a 25-problem in silico benchmark collected from six prior publications (spanning inpainting-style problems, viral epitopes, receptor traps, small-molecule-binding sites, binding interfaces, and enzyme active sites), RFdiffusion solved 23/25 problems versus 15/25 for RF Hallucination and 19/25 for RFjoint Inpainting, generally with higher per-problem success rates, no hyperparameter tuning, and no reliance on motif presence in the training set. A fine-tuned complex-conditioned model scaffolding the p53 helix that binds MDM2 produced 55/96 designs with detectable MDM2 binding at 10 μM, including 0.5 nM and 0.7 nM binders — roughly 1,000-fold higher affinity than the native 600 nM p53-peptide interaction. A separate fine-tuning enabled scaffolding of minimal enzyme-active-site descriptions (a few catalytic side chains/backbone atoms) across several EC classes with high in silico success, extended via an external "pocket" potential (repulsive + attractive fields around an implicitly modelled substrate) to scaffold a retroaldolase catalytic triad with a shape-complementary binding pocket (without explicitly modelling the ligand). [SRC-0104, p. 1093-1096]
- **Symmetric functional-motif scaffolding and metal-binding design.** Combining symmetric-oligomer and motif-scaffolding capabilities, RFdiffusion designed C3-symmetric trimers rigidly presenting three copies of the AHB2 ACE2-mimic binder domain to match the SARS-CoV-2 spike trimer's three receptor-binding sites, and C4-symmetric assemblies scaffolding four histidine imidazoles in an ideal square-planar Ni²⁺-coordination geometry. Of 44 Ni²⁺-binder designs expressed and purified, 37 had the expected SEC oligomeric state; 18 of 36 tested bound Ni²⁺ by isothermal titration calorimetry (ITC, low-nanomolar to low-micromolar Kd, 1:4 ion:monomer stoichiometry as designed); mutating the key histidine (H52A) abolished or strongly reduced binding in 17/17 testable cases. nsEM (NiB1.17: 3D reconstruction) confirmed the intended fourfold symmetry for a subset of designs. [SRC-0104, p. 1096-1097]
- **De novo protein-binder design.** Fine-tuned on protein-complex structures with a "hotspot residue" feature marking the target binding site (and optionally fold-conditioning via secondary-structure/block-adjacency input), RFdiffusion designed binders against five targets: influenza HA, IL-7Rα, PD-L1, insulin receptor (InsR), and TrkA. Designs were filtered by AF2 confidence (interface and monomer) before expression; single-point biolayer interferometry (BLI) screening at 10 μM gave an overall experimental hit rate of ~19% (binding ≥ 50% of positive-control response), with binders identified for all five targets from fewer than 100 designs per target each — roughly two orders of magnitude higher than the prior Rosetta-based de novo binder-design method on the same four shared targets (IL-7Rα, InsR, PD-L1, TrkA); the authors attribute about one order of magnitude to RFdiffusion itself and the other to AF2-based filtering. Several binders reached nanomolar affinity with no further optimization (e.g. ~30 nM for HA and IL-7Rα hits). [SRC-0104, p. 1097-1098]
- **Cryo-EM confirmation of atomic accuracy.** The highest-affinity influenza-HA binder, HA_20 (Kd = 28 nM by BLI), was solved in complex with Iowa/43 H1 HA by cryo-EM: a 2.9 Å, C3-symmetric reconstruction showed all three HA stem epitopes occupied, with the experimental structure matching the RFdiffusion design model to 0.63 Å RMSD over the complex (0.6 Å over the binder alone), and side-chain interface contacts markedly different from the nearest PDB structural homolog. [SRC-0104, p. 1098, Extended Data Fig. 9, Extended Data Table 1]
- **Stated extensions and limitations (Discussion).** The authors note RFdiffusion cannot currently explicitly model bound small-molecule ligands (handled only implicitly via an external pocket potential), and point to prospective extensions via RF variants incorporating nucleic acids/protein-nucleic-acid complexes and ligand atoms. They cite concurrent/companion work (Vázquez Torres et al.) showing RFdiffusion can design picomolar-affinity peptide binders and can be used for structure refinement via partial noising/denoising of an input structure. [SRC-0104, p. 1099]

## Evidence

Precise numeric results reported in the main text (no raw benchmark data tables — e.g. Supplementary Tables 1, 9, 10 — are included in this PDF; see Known gaps):

**Monomer generation and ablations**
- Unconditional generation vs. Hallucination (AF2 success metric): RFdiffusion significantly outperforms, two-proportion z-test n = 400 designs/condition, z = 9.5, p = 1.6 × 10⁻²¹. [SRC-0104, Fig. 2d]
- Ablation z-tests (unconditional 300-aa generation, AF2-vs-design RMSD as outcome): no MSE loss (FAPE instead) z = 4.1, p = 4.1 × 10⁻⁵; no self-conditioning z = 11.4, p = 6.1 × 10⁻³⁰ (n = 800 designs/condition for the self-conditioning comparison). [SRC-0104, Extended Data Fig. 1D-E]
- Generation speed: 100-residue protein in ~11 s (RTX A4000 GPU) for RFdiffusion vs. ~8.5 min for RF Hallucination. [SRC-0104, p. 1091]
- Fold-conditioned in silico success: TIM barrels 42.5%, NTF2 folds 54.1%; 8/11 TIM-barrel designs experimentally soluble/thermostable/CD-consistent. [SRC-0104, p. 1092, Extended Data Fig. 4d]

**Symmetric oligomers**
- 608 designs selected for experimental characterization; ≥ 87 (95% CI) to 126 (99% CI) had SEC-consistent oligomeric states. [SRC-0104, p. 1092]
- 38 D2, 7 D3, 3 D4 dihedral designs had expected molecular weights by SEC. [SRC-0104, p. 1093]
- AF2-vs-design backbone RMSD for nsEM/cryo-EM-validated designs: HE0822 (C3) 1.33 Å; HE0626 (C6) 1.03 Å; HE0490 (D3) 0.60 Å; HE0675 (C8) 0.74 Å; HE0537 (D4) 0.75 Å. [SRC-0104, Fig. 3 caption]

**Motif scaffolding**
- 25-problem benchmark success counts: RFdiffusion 23/25, RFjoint Inpainting 19/25, Hallucination 15/25; RFdiffusion has the highest per-problem success rate in 19 of its 23 solved problems. [SRC-0104, p. 1094]
- p53/MDM2 scaffolding: 55/96 designs bound detectably at 10 μM; top affinities 0.5 nM and 0.7 nM (p53_design_53, p53_design_89) vs. native p53-peptide affinity of 600 nM. [SRC-0104, p. 1095]
- Enzyme active-site scaffolding examples (AF2-vs-design backbone RMSD / AF2-vs-design-motif backbone RMSD / AF2-vs-design-motif full-atom RMSD / AF2 pAE): EC1 0.88 Å / 0.53 Å / 1.05 Å / 4.47; EC2 0.93 Å / 0.50 Å / 1.29 Å / 3.51; EC3 0.92 Å / 0.60 Å / 1.07 Å / 4.59; EC4 0.93 Å / 0.80 Å / 1.03 Å / 4.41; EC5 0.78 Å / 0.44 Å / 1.14 Å / 3.32. [SRC-0104, Fig. 4f-g, Extended Data Fig. 6A-D]
- Retroaldolase pocket potential: with vs. without the external pocket potential, two-proportion z-tests (n = 71/51 designs) show reduced clashes (z = −2.05, p = 0.02) and more designs with a genuine pocket (z = −2.27, p = 0.01). [SRC-0104, Extended Data Fig. 6F]

**Metal-binding design**
- 44 Ni²⁺-binder designs expressed/purified; 37 SEC-consistent; 18/36 ITC-tested bound Ni²⁺ (low-nM to low-µM Kd, 1:4 stoichiometry); H52A mutation abolished/reduced binding in 17/17 testable cases. [SRC-0104, p. 1096]

**Binder design**
- Overall BLI experimental hit rate (≥ 50% of positive-control response at 10 μM): ~19%, roughly two orders of magnitude above the prior Rosetta-based method on the shared four targets; estimated AF2-filtered success rates for the prior campaigns if AF2 filtering had been used: HA 0%, IL-7Rα 2.2%, InsR 5.5%, PD-L1 3.7%, TrkA 1.5%. [SRC-0104, p. 1097, Fig. 6b]
- Representative Kd values: HA_20 28 nM; IL7Ra_55 30 nM (approx., text) with BLI titration Kd ≈ 30 nM; InsulinR_30, PDL1_77, TrkA_88 reported with individual BLI titrations (exact Kd values given per-plot in Fig. 6c, not individually re-transcribed here as the figure reports them graphically rather than as a table). [SRC-0104, Fig. 6c-d]
- Cryo-EM: 2.9 Å map resolution for the HA/HA_20 complex; design-vs-experimental-structure RMSD 0.63 Å (complex), 0.6 Å (binder alone). [SRC-0104, p. 1098]

No table in the main text or Extended Data figures presented in this PDF is a plain numeric data table suitable for full transcription in the sense used for the dielectric-permittivity/density benchmark sources in this wiki (SRC-0094-SRC-0097); all quantitative results above are reported as prose, bar-chart figures, or per-plot annotations, and the underlying raw per-design dataset is hosted externally (see Data availability in Known gaps). Extended Data Table 1 (cryo-EM data collection/refinement/validation statistics) is present as a caption header only in the extracted main-text pages; its full numeric content was not transcribed here since it duplicates standard cryo-EM processing metadata (map resolution, particle counts, refinement statistics) already summarized above and in the main text, and would require OCR of a dense statistics table image rather than reliable text extraction.

## Mathematical gaps

The full mathematical formalism (explicit noising/denoising update equations, the self-conditioning interpolation formula, the symmetry-resymmetrization procedure, and the external-potential functional forms) is described only in prose in this PDF and is deferred to a separately published Supplementary Methods document (referenced in-text as "Supplementary Methods 2.4", "2.5", "4.4", "4.5", etc.) that is not included in the imported file. Specifically missing:
- The exact SO(3) Brownian-motion noising/reverse-step formulas for residue orientations (Supplementary Methods, building on refs. 23-24 in the paper: De Bortoli et al. 2022 Riemannian score-based generative modelling; Leach et al. 2022 DDPMs on SO(3)).
- The exact self-conditioning interpolation formula `interp(Xt, X̂0) + ε` shown schematically in Fig. 1a is named but not given as an explicit equation in the main text.
- The functional form and parameters of the enzyme-active-site "pocket" external potential (Supplementary Methods 4.4).
- The inter/intrachain symmetric-oligomer contact potential (Extended Data Fig. 5c) and the resymmetrization procedure (Supplementary Methods).
This is recorded as a known gap rather than reconstructed from description alone, consistent with "do not guess formulas that cannot be reliably reconstructed."

## Limitations and Caveats

- The paper's own in silico success metric is validated by correlation with experimental success in this and prior work, but AF2-based self-consistency checks remain a proxy, not a guarantee, of true structural accuracy or function. [SRC-0104, p. 1091]
- Very large unconditional designs (> ~600 residues) are "difficult to validate in silico" because they are likely beyond AF2/ESMFold single-sequence prediction capability; the paper does not claim experimental validation at this scale. [SRC-0104, p. 1092]
- RFdiffusion cannot currently explicitly model bound small-molecule ligands; enzyme-active-site scaffolding only implicitly accounts for a substrate via an external pocket potential on Cα atoms (not side-chain atoms). [SRC-0104, p. 1096]
- Binder-design specificity was only partially assessed: six IL-7Rα binders were shown to compete with a validated positive control at the same site by competition BLI, but the authors explicitly state "further work is required to fully characterize proteome-wide specificity." [SRC-0104, p. 1098]
- Binder-design targets in this study were described as "non-polar sites"; the authors note further studies are needed to assess success rates on more polar target sites and sites without known native binding partners. [SRC-0104, p. 1098]
- Some designed proteins showed endothermic (rather than the more common exothermic) Ni²⁺ binding, suggesting entropically driven coordination in those cases — noted as an observation, not fully mechanistically explained. [SRC-0104, p. 1096]

## Open Questions

- What determines whether a structurally plausible, in-silico-successful design will actually be experimentally soluble/foldable/functional — i.e., how much of the (often large) gap between in silico and experimental success rates is attributable to each design stage (backbone generation, sequence design, AF2 filtering, expression)? [SRC-0104, implicit throughout]
- How well does RFdiffusion's binder-design success generalize to polar or otherwise more challenging target sites and to targets lacking known native binding partners? [SRC-0104, p. 1098]
- How will RFdiffusion's reported extension to nucleic-acid-binding design and explicit ligand modelling (both proposed in the Discussion as future RF-derived extensions) actually be realized, and with what accuracy? [SRC-0104, p. 1099]

## Links

- [[wiki/concepts/rfdiffusion-diffusion-based-de-novo-protein-design]]
- [[wiki/claims/CLM-0061-rfdiffusion-self-conditioning-and-mse-loss-are-necessary-for-design-quality]]
- [[wiki/claims/CLM-0062-rfdiffusion-raises-binder-design-success-two-orders-of-magnitude-with-cryo-em-confirmed-accuracy]]

## Citation Links

- SRC-0104 is cited by [[wiki/sources/SRC-0103-all-atom-inverse-protein-folding-discrete-flow-matching]] (ADFLIP, Yi, Jamali & Scheres, ICML 2025) as prior/related protein-design generative-modelling work: SRC-0103's reference list cites "Yim, J., Eisenach, H. E., Ahern, W., Borst, A. J., Ragotte, R. J., Milles, L. F., et al. De novo design of protein structure and function with rfdiffusion. Nature, 620(7976): 1089-1100, 2023," which is an exact venue/volume/page match to this source (confirmed by direct text search of SRC-0103's bibliography). SRC-0103 does not otherwise discuss RFdiffusion's methodology in its main text; the citation appears to be a general related-work reference rather than a direct methodological dependency (ADFLIP is an inverse-folding/sequence-design model, distinguished from RFdiffusion's backbone-generation task; in a typical design pipeline RFdiffusion would generate a backbone and a model like ProteinMPNN or ADFLIP would then design its sequence). [SRC-0103 bibliography, ref. for Yim et al. 2023]
- SRC-0104 cites ProteinMPNN (Dauparas et al. 2022, *Science*) as its sequence-design step for all generated backbones, RoseTTAFold (Baek et al. 2021, *Science*) as its structure-prediction backbone, and AlphaFold2 (Jumper et al. 2021, *Nature*) as its in silico validation oracle; none of these three is currently ingested as a separate SecondBrain source. [SRC-0104, refs. 1, 17, 18]
- SRC-0104's other ~58 references (prior diffusion-model work, Hallucination/RFjoint Inpainting precursors, binder-design and symmetric-assembly applications, DDPM theory) were reviewed by title/author/year against SecondBrain's currently ingested sources; no further matches were found. [SRC-0104, references 1-58]

## Metadata notes

- Published in *Nature*, vol. 620, pp. 1089-1100, 31 August 2023 (received 14 December 2022; accepted 7 July 2023; published online 11 July 2023). Open access. DOI: 10.1038/s41586-023-06415-8. [SRC-0104]
- Code released at `github.com/RosettaCommons/RFdiffusion` (academic, personal, and commercial use), with a Google Colab notebook. [SRC-0104, Code availability]
- Design structures, AF2 models, and experimental measurements are hosted externally (figshare, not included in this ingestion); cryo-EM maps/models for the HA binder are deposited at PDB 8SK7 / EMDB-40557; the HE0537 oligomer's EM data are at EMDB-40602. [SRC-0104, Data availability]
- The imported PDF is the merged Nature "Article" (main text, Extended Data figures 1-9, Extended Data Table 1, and the Nature Portfolio Reporting Summary cover sheet); the full Supplementary Information (Supplementary Methods, Supplementary Tables 1-10, Supplementary Figures) referenced throughout the main text is a separate publication artifact not present in this file.

## Ingestion QA

### Retrieval questions checked

- What problem does RFdiffusion solve, and how does it differ from prior protein-design deep-learning methods (Hallucination, RFjoint Inpainting)?
- How is RFdiffusion built from RoseTTAFold, and what is the noising/denoising process over residue frames?
- Why does self-conditioning and MSE (rather than FAPE) loss matter for RFdiffusion's performance, and what ablation evidence supports this?
- What design problems does RFdiffusion address (unconditional monomers, fold-conditioned monomers, symmetric oligomers, motif scaffolding, symmetric motif/metal-binding scaffolding, binder design), and what in silico/experimental success rates are reported for each?
- How was RFdiffusion experimentally validated (CD, SEC, nsEM/cryo-EM, BLI, ITC), and what is the headline cryo-EM accuracy result?
- How does RFdiffusion's binder-design success rate compare to the prior Rosetta-based de novo binder-design method on shared targets?
- What are RFdiffusion's acknowledged limitations (ligand modelling, specificity characterization, target polarity) and proposed future extensions?
- Is RFdiffusion cited by or related to any other SecondBrain source (specifically SRC-0103/ADFLIP)?

### Coverage decision

`coverage_profile: standard`. The paper's qualitative methodology (diffusion over SE(3) residue frames, self-conditioning, training-loss design, symmetrization, external potentials) and its full range of design problems, in silico benchmarks, and experimental validation are represented with inline provenance. The explicit mathematical formalism (noising/denoising update equations, potential functional forms) is not reconstructable from this PDF alone, since it lives in a separately published Supplementary Methods document not included in the imported file; no equation is reproduced or guessed, so `math-standard`/`math-deep` would overstate this page's mathematical coverage. The gap is recorded under Mathematical gaps instead. Coverage is otherwise complete for the main-text and Extended Data content actually present in the PDF.

### Known gaps

- Full Supplementary Information (Supplementary Methods with explicit equations, Supplementary Tables 1-10 including the full motif-scaffolding benchmark results table, Supplementary Figures) is not included in this PDF and was not separately sourced.
- Raw per-design numeric data (the complete set of in silico success rates, individual design metrics, and experimental measurements) is hosted externally via a figshare link (`https://figshare.com/s/439fdd59488215753bc3`) rather than included in the PDF or this wiki page.
- Extended Data Table 1's cryo-EM collection/refinement/validation statistics were not individually transcribed (see Evidence section note).
