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
  - research/computational-drug-discovery
tags:
  - protein-design
  - inverse-protein-folding
  - flow-matching
  - discrete-generative-model
  - graph-neural-networks
related:
  - "[[wiki/sources/SRC-0103-all-atom-inverse-protein-folding-discrete-flow-matching]]"
sources:
  - SRC-0103
sensitivity: public
encryption: none
---

# ADFLIP: All-Atom Discrete Flow Matching for Inverse Protein Folding

## Summary

ADFLIP (All-atom Discrete FLow matching Inverse Protein folding) is a generative model for *inverse protein folding* — designing an amino-acid sequence that folds to a target structure — that conditions on the full all-atom structure of a biomolecular complex (protein backbone plus non-protein components such as ligands, nucleotides, or metal ions) and, when available, on multiple structural states of a conformationally dynamic complex (e.g. a solution-NMR ensemble). It uses discrete flow matching for sequence generation, a multi-scale graph neural network (GNN) denoiser that mixes atom- and residue-level information, concurrent side-chain packing as progressive structural context, and training-free classifier guidance to steer generation toward arbitrary target properties without retraining. [SRC-0103]

## Key Points

- **Problem framed.** Most inverse-folding models (ProteinMPNN, PiFold, and their predecessors) condition only on the protein backbone and a single static structure; LigandMPNN extended this to all-atom, non-protein-aware conditioning but still on a single structure. ADFLIP targets both gaps simultaneously: all-atom conditioning *and* multi-structure (ensemble) conditioning for dynamic complexes. [SRC-0103, Sec. 1-2]
- **Discrete flow matching.** Following Campbell et al. (2024), the sequence-generating process is modelled as a continuous-time Markov chain with a closed-form conditional flow from a fully-masked state to the target sequence, sampled at inference via Euler updates over a learned rate matrix. This differs from the discrete-diffusion lineage (Austin et al. 2021; Hoogeboom et al. 2021; Campbell et al. 2022) mainly in offering simpler, faster training convergence while retaining non-autoregressive, order-free sequence generation appropriate for amino-acid sequences (which, unlike natural language, have no inherent left-to-right ordering). [SRC-0103, Sec. 2-3.1]
- **Side chains as structural context.** ADFLIP is coupled, at sampling time, with an external side-chain packing network (PIPPACK); as residues are sampled they are immediately given predicted side-chain geometry, which is fed back into the denoiser for subsequent steps. This matters because side chains (not the backbone) typically define specific ligand/nucleotide/metal-binding interactions, which most backbone-only inverse-folding methods cannot see. [SRC-0103, Sec. 3.1]
- **Multi-scale GNN denoiser.** The denoiser alternates atom-level attention (an Invariant-Point-Attention-like module with added frame averaging for rotation robustness) with residue-level, LigandMPNN-style message passing modulated by diffusion-time conditioning, connected by averaging/scattering operations between the two node types; it draws architectural inspiration from AlphaFold3 (Fourier/transition-block embeddings) and LigandMPNN (residue encoding). [SRC-0103, Sec. 3.2]
- **Adaptive sampling.** A "purity" (max predicted probability) threshold lets ADFLIP sample high-confidence positions earlier and spend more iterative refinement on harder (more ambiguous) positions, rather than sampling all positions on a fixed schedule. [SRC-0103, Sec. 3.1, App. B]
- **Training-free property guidance.** Instead of retraining a regressor to operate on noisy/intermediate sequence states, ADFLIP estimates an existing complete-sequence regressor's prediction for an intermediate state by taking its expectation under the denoiser's own predicted distribution, allowing arbitrary pre-trained property predictors (demonstrated with the binding-affinity predictor DSMBind) to guide sampling without retraining or architecture changes. [SRC-0103, Sec. 3.3]
- **Benchmark performance.** On PDB benchmarks following the LigandMPNN protocol, ADFLIP achieves the lowest perplexity and highest interaction-residue recovery rate of the compared methods (PiFold, ProteinMPNN, LigandMPNN) for ligand-, nucleotide-, and metal-ion-binding residues, with the largest margin for metal-ion sites. On a newly curated 219-ensemble solution-NMR dataset, conditioning on the full ensemble (vs. a single conformation) with the same trained model further improves recovery, most for ligand and nucleotide interactions and least for metal-ion interactions (attributed to metal sites being conformationally more stable). [SRC-0103, Sec. 4.1-4.2]
- **Guided generation trade-off.** Training-free guidance toward higher DSMBind-predicted binding affinity raised the fraction of generated sequences exceeding wild-type affinity from 41.9% to 58.1%, but foldability dropped from 100% to 91.4%; the authors attribute the limited absolute gain to the fixed protein backbone and limited side-chain sampling during guided generation. [SRC-0103, Sec. 4.3]
- **Relation to concurrent/related work.** The purity-based adaptive sampling scheme parallels concurrent path-planning work for masked diffusion sampling (Peng et al., 2025); the authors suggest integrating backbone structural refinement into sequence generation (as RNAflow does for RNA design in RosettaFold2NA) as a natural next step, which would also likely help guided generation. [SRC-0103, Sec. 3.1, Sec. 5]

## Evidence

- Interaction-residue recovery rate (Table 1): ADFLIP 62.19% (ligand) / 50.21% (nucleotide) / 75.73% (metal ion), vs. LigandMPNN 59.21% / 46.14% / 69.31%, ProteinMPNN 54.48% / 40.29% / 54.09%, PiFold 59.20% / 38.41% / 47.55%. [SRC-0103, Table 1]
- NMR ensemble conditioning improves recovery over single-structure conditioning with the same model: +8.6 points (ligand), +5.8 points (nucleotide), +2.6 points (metal ion). [SRC-0103, Table 3]
- Guided generation: affinity-gain success rate 41.9% → 58.1% at the cost of foldability 100% → 91.4%. [SRC-0103, Table 5]

Full benchmark tables (recovery rate, perplexity, RMSD/TM-score/pLDDT/foldability across ligand, nucleotide, metal-ion, and NMR-ensemble test sets) are transcribed on the source page. [[wiki/sources/SRC-0103-all-atom-inverse-protein-folding-discrete-flow-matching]]

## Links

- [[wiki/sources/SRC-0103-all-atom-inverse-protein-folding-discrete-flow-matching]]
- [[wiki/claims/CLM-0059-adflip-all-atom-and-multi-conformation-conditioning-improves-inverse-folding-recovery]]
- [[wiki/claims/CLM-0060-adflip-training-free-guidance-improves-affinity-targeted-generation-with-limited-gains]]

## Caveats

- All evaluation is computational (refolding with Chai-1, binding-affinity prediction with DSMBind); no generated sequence has been experimentally synthesized, expressed, or assayed. [SRC-0103, Impact Statement]
- Nucleotide-complex design remains substantially harder than ligand or metal-ion design on every metric, even with all-atom and multi-structure conditioning. [SRC-0103, Sec. 4.1-4.2]
- The protein backbone is held fixed throughout generation; no joint structural refinement is performed, which the authors identify as limiting guided-generation results specifically. [SRC-0103, Sec. 4.3]

## Open Questions

- How should a useful set of representative conformational states be obtained for protein-nucleotide (or other dynamic biomolecular) complexes when an NMR ensemble is not already available? [SRC-0103, Sec. 5]
- Would joint backbone refinement during sequence generation (as in RNAflow/RosettaFold2NA) improve both unguided design quality and property-guided generation? [SRC-0103, Sec. 4.3, Sec. 5]
- Does the nucleotide-complex performance gap reflect genuinely higher interface dynamics, limited/less diverse training data, or an architectural limitation specific to nucleotide representation? [SRC-0103, Sec. 5]
