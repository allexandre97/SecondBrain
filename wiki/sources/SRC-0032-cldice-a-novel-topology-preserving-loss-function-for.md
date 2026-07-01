---
type: source
status: active
created: 2026-06-30
updated: 2026-07-01
source_id: SRC-0032
display_title: "clDice - a Novel Topology-Preserving Loss Function for Tubular Structure Segmentation"
short_title: "clDice Topology-Preserving Loss"
aliases:
  - "SRC-0032"
  - "arXiv:2003.07311v7"
  - "clDice Topology-Preserving Loss"
  - "clDice - a Novel Topology-Preserving Loss Function for Tubular Structure Segmentation"
source_path: raw/sources/SRC-0032-cldice-a-novel-topology-preserving-loss-function-for.pdf
imported_path: raw/sources/SRC-0032-cldice-a-novel-topology-preserving-loss-function-for.pdf
original_filename: "Shi20b.pdf"
additional_filenames:
  - "2003.07311v7.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 2e952692e01cb534b8851712e27846ab5d0dc06dfd170c9c64daf4e70d7f3170
areas:
  - research
categories:
  - research/computer-vision/biomedical-imaging
  - research/machine-learning/scientific-modeling
  - research/bioimage-analysis/filament-segmentation
tags:
  - tubular-segmentation
  - topology
  - loss-function
  - cldice
related:
  - "[[wiki/concepts/topology-aware-tubular-structure-segmentation]]"
  - "[[wiki/concepts/deep-learning-cytoskeleton-image-analysis]]"
sources:
  - SRC-0032
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: math-standard
---

# clDice - a Novel Topology-Preserving Loss Function for Tubular Structure Segmentation

Source ID: `SRC-0032`

## Raw source

- Repository path: `raw/sources/SRC-0032-cldice-a-novel-topology-preserving-loss-function-for.pdf`
- Open raw source: [raw/sources/SRC-0032-cldice-a-novel-topology-preserving-loss-function-for.pdf](../../raw/sources/SRC-0032-cldice-a-novel-topology-preserving-loss-function-for.pdf)

## Summary

Shit et al. introduce centerlineDice (clDice), a connectivity-aware metric for tubular and curvilinear segmentation, and soft-clDice, a differentiable loss based on soft skeletonization. The paper argues that overlap metrics such as Dice and Jaccard can miss topological failures in vessels, neurons, and roads, where preserving connectedness is often more important than matching every voxel radius exactly. [SRC-0032]

## Key Points

- clDice compares skeletons and masks rather than only foreground voxels, so it emphasizes whether the predicted centerline lies inside the label and whether the label centerline is covered by the prediction. [SRC-0032, section 2]
- The authors prove that, under foreground/background skeleton assumptions, perfect clDice on foreground and background implies homotopy equivalence between prediction and label. [SRC-0032, section 3]
- soft-clDice approximates skeletonization with iterative min- and max-pooling so it can be used as a differentiable neural-network loss. [SRC-0032, section 4.1]
- The combined loss is benchmarked on five public datasets covering 2D retina vessels, roads, neurons, synthetic 3D vessels, and 3D brain vessels; the paper reports better connectivity, graph similarity, topology measures, and often volumetric scores relative to soft-Dice baselines. [SRC-0032, sections 5-6]

## Key equations

**Topology precision and sensitivity, source Eq. (1) [SRC-0032]:**

$$
T_{\mathrm{prec}}(S_P, V_L) = \frac{|S_P \cap V_L|}{|S_P|}, \qquad
T_{\mathrm{sens}}(S_L, V_P) = \frac{|S_L \cap V_P|}{|S_L|}
$$

**centerlineDice, source Eq. (2) [SRC-0032]:**

$$
\operatorname{clDice}(V_P, V_L) =
2 \times \frac{T_{\mathrm{prec}}(S_P, V_L) T_{\mathrm{sens}}(S_L, V_P)}
{T_{\mathrm{prec}}(S_P, V_L) + T_{\mathrm{sens}}(S_L, V_P)}
$$

## Variable glossary

- $V_P$: predicted binary segmentation mask. [SRC-0032]
- $V_L$: ground-truth binary label mask. [SRC-0032]
- $S_P$: skeleton extracted from $V_P$. [SRC-0032]
- $S_L$: skeleton extracted from $V_L$. [SRC-0032]
- $T_{\mathrm{prec}}$: fraction of the predicted skeleton lying within the ground-truth mask; penalizes false positive centerline branches. [SRC-0032]
- $T_{\mathrm{sens}}$: fraction of the label skeleton covered by the predicted mask; penalizes missing label branches. [SRC-0032]

## Proof map

- The paper assumes binary foreground and background structures admit skeleta and can be treated as subcomplexes of a voxel-grid cell complex. [SRC-0032, section 3]
- It states that, under these assumptions, the homotopy type is determined by graph-like foreground/background structure and first Betti-number behavior. [SRC-0032, section 3]
- Theorem 1 uses nested inclusions between skeleta and masks to show that the relevant inclusions are homotopy equivalences. [SRC-0032, section 3]
- Corollary 1.1 then connects the inclusion conditions to clDice: if the foreground skeletons lie inside the opposite foreground masks, and similarly for background, the prediction and label foregrounds and backgrounds are homotopy equivalent. [SRC-0032, section 3]

## Equation inventory

| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |
| Topology precision and sensitivity | Eq. (1) | Key equations | Measures centerline false positives and false negatives | $S_P$, $S_L$, $V_P$, $V_L$ | Basis for clDice and soft-clDice loss |
| centerlineDice | Eq. (2) | Key equations | Harmonic mean of topology precision and sensitivity | $T_{\mathrm{prec}}$, $T_{\mathrm{sens}}$ | Objective/evaluation metric for tubular segmentation |
| soft skeletonization algorithm | Algorithm 1 | Mathematical gaps | Differentiable approximation to skeleton extraction | image/probability map, iteration count $k$ | Needed to implement soft-clDice in neural-network training |

## Limitations

- The topological guarantee depends on structural assumptions about foreground and background skeleta; it is not a blanket guarantee for arbitrary segmentations or arbitrary topology. [SRC-0032, section 3]
- The soft-skeletonization iteration count is dataset-specific and must be at least as large as the maximum observed radius according to the paper. [SRC-0032, section 4.1]
- clDice improves topology-aware behavior but does not replace task-specific validation for downstream biological or physical analyses. [SRC-0032]

## Mathematical gaps

- The wiki does not reproduce the full soft-skeletonization algorithm line by line.
- The supplementary digital-topology explanation is not ingested in detail.

## Metadata notes

- The requested file `2003.07311v7.pdf` is byte-identical to the already imported raw source for `SRC-0032`; no duplicate source ID was created. [SRC-0032]
- The PDF identifies itself as arXiv:2003.07311v7, dated 15 July 2022. [SRC-0032]

## Links

- [[wiki/concepts/topology-aware-tubular-structure-segmentation]]
- [[wiki/concepts/deep-learning-cytoskeleton-image-analysis]]

## Ingestion QA

### Retrieval questions checked

- Why are ordinary Dice/Jaccard metrics insufficient for tubular structures?
- How is clDice defined?
- What do topology precision and topology sensitivity measure?
- What topological guarantee is claimed?
- How is clDice made differentiable for training?
- Which datasets support the empirical claim?
- What assumptions limit the guarantee?

### Coverage decision

Complete at `coverage_profile: math-standard`. The source page preserves the central definitions, key equations, proof map, implementation role, empirical scope, and mathematical caveats.

### Known gaps

- Full theorem details and supplementary topology discussion remain in the raw source.
- Dataset-specific training hyperparameters are summarized rather than exhaustively tabulated.
