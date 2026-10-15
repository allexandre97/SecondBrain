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
  - research/biomolecules/proteins
  - research/machine-learning/molecular-modeling
  - research/experimental-benchmarking
tags:
  - claim
  - protein-design
  - inverse-protein-folding
  - flow-matching
  - validation
related:
  - "[[wiki/concepts/adflip-discrete-flow-matching-inverse-folding]]"
sources:
  - SRC-0103
sensitivity: public
encryption: none
---

# ADFLIP's All-Atom and Multi-Conformation Conditioning Improves Inverse-Folding Recovery

## Claim

A discrete-flow-matching inverse-folding model that conditions jointly on all-atom non-protein structure (ligands, nucleotides, metal ions) and, when available, on multiple conformational states of a dynamic complex, achieves higher sequence-recovery rate and lower perplexity at non-protein interaction sites than backbone-only models (ProteinMPNN, PiFold) and than an all-atom but single-structure model (LigandMPNN), with the improvement from multi-conformation conditioning obtained from the same trained model without any fine-tuning. [SRC-0103]

## Evidence

- On held-out PDB complexes (residues within 5.0 Å of non-protein atoms, LigandMPNN-protocol clustering), ADFLIP's recovery rate exceeds LigandMPNN, ProteinMPNN, and PiFold for all three complex types: ligand 62.19% vs. 59.21%/54.48%/59.20%; nucleotide 50.21% vs. 46.14%/40.29%/38.41%; metal ion 75.73% vs. 69.31%/54.09%/47.55%. Perplexity is correspondingly lowest for ADFLIP in every case. [SRC-0103, Table 1]
- The largest backbone-only-vs-all-atom gap is for metal-ion sites (ProteinMPNN 54.09% → LigandMPNN 69.31% → ADFLIP 75.73%), which the authors attribute to the chemically conserved identity of metal-coordinating side chains (His, Cys, Met, Tyr, Asp, Glu) — information invisible to backbone-only models. [SRC-0103, Sec. 4.1]
- Refolding generated sequences with Chai-1 shows ADFLIP also modestly improves structural fidelity over LigandMPNN (RMSD/TM-score/foldability) for all three complex types, e.g. ligand complexes reach 100% foldability (TM-score ≥ 0.5) vs. LigandMPNN's 98.8%. [SRC-0103, Table 2]
- On a newly curated 219-ensemble solution-NMR dataset (avg. 18 conformational states per complex), feeding the full ensemble into the same trained ADFLIP model — rather than only its most-interacting single conformation — improves recovery rate by 8.6 points (ligand), 5.8 points (nucleotide), and 2.6 points (metal ion), and reduces mean refolding RMSD from 9.11 Å to 7.61 Å, without any fine-tuning. [SRC-0103, Sec. 4.2, Tables 3-4]
- The smaller multi-conformation gain for metal-ion sites is attributed to metal-binding conformations remaining relatively stable even across the NMR ensemble, consistent with the single-structure metal-ion recovery rate already being comparatively high. [SRC-0103, Sec. 4.2]

## Implementation Use

For inverse-folding or protein-design pipelines targeting ligand-, nucleotide-, or metal-binding functionality, conditioning the sequence-design model on explicit non-protein atomic structure (not just the protein backbone) is worth the added architectural complexity, with metal-binding design benefiting most. Where multiple structural states of a target complex are available (e.g. an NMR ensemble, or multiple crystal forms), conditioning on the full ensemble — by denoising each conformation independently and averaging the resulting sequence-probability predictions — can improve recovery at interaction sites without retraining, at the cost of running the denoiser once per conformation per sampling step. [SRC-0103]

## Caveats

- Even with all-atom and multi-structure conditioning, nucleotide-complex design (recovery and foldability) remains markedly worse than ligand or metal-ion design, so the improvement does not close this specific performance gap. [SRC-0103, Sec. 4.1-4.2]
- All improvements are measured computationally (recovery rate against native sequence; refolding-based foldability with Chai-1); no generated sequence has been experimentally validated. [SRC-0103, Impact Statement]
- The metal-ion recovery advantage is explained post hoc by residue-identity conservation, a plausible but not independently tested mechanistic account. [SRC-0103, Sec. 4.1]
- Comparisons use LigandMPNN retrained on the same data clustering as ADFLIP (for a fair comparison), but ProteinMPNN and PiFold comparisons use their original (not necessarily identically clustered) training; the paper does not report retraining ProteinMPNN/PiFold on the same split. [SRC-0103, Sec. 4.1]

## Links

- [[wiki/sources/SRC-0103-all-atom-inverse-protein-folding-discrete-flow-matching]]
- [[wiki/concepts/adflip-discrete-flow-matching-inverse-folding]]
- [[wiki/claims/CLM-0060-adflip-training-free-guidance-improves-affinity-targeted-generation-with-limited-gains]]
