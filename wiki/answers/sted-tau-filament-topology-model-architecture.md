---
type: answer
status: active
created: 2026-07-01
updated: 2026-07-01
question: "Given the manuscript draft wiki/sources/SRC-0064-versatile-neuronal-culture-system-templated-tau-assembly.md, how should the unfinished STED morphology comparisons be quantified, and what model architecture best supports topology-aware tau filament analysis across tauopathy seeds and days in vitro?"
answer_status: partially-answered
areas:
  - research
categories:
  - research/computer-vision/biomedical-imaging
  - research/bioimage-analysis/filament-segmentation
  - research/biomolecules/proteins
tags:
  - STED
  - tau
  - filament-topology
  - morphology-quantification
  - segmentation
  - graph-analysis
related:
  - "[[wiki/sources/SRC-0064-versatile-neuronal-culture-system-templated-tau-assembly]]"
  - "[[wiki/sources/SRC-0063-sted-imaging-tau-filaments-alzheimer-disease]]"
  - "[[wiki/concepts/neuronal-templated-tau-assembly-systems]]"
  - "[[wiki/concepts/super-resolution-imaging-of-tau-pathology]]"
  - "[[wiki/concepts/topology-aware-tubular-structure-segmentation]]"
  - "[[wiki/concepts/filament-instance-and-semantic-segmentation]]"
  - "[[wiki/concepts/cytoskeleton-segmentation-and-tracing]]"
  - "[[wiki/concepts/self-configuring-u-net-medical-image-segmentation]]"
  - "[[wiki/concepts/promptable-segmentation-foundation-models]]"
sources:
  - SRC-0004
  - SRC-0029
  - SRC-0030
  - SRC-0031
  - SRC-0032
  - SRC-0033
  - SRC-0034
  - SRC-0035
  - SRC-0063
  - SRC-0064
  - SRC-0068
  - SRC-0069
sensitivity: private
encryption: none
wiki_pages_used:
  - wiki/index.md
  - wiki/sources/SRC-0064-versatile-neuronal-culture-system-templated-tau-assembly.md
  - wiki/sources/SRC-0063-sted-imaging-tau-filaments-alzheimer-disease.md
  - wiki/concepts/neuronal-templated-tau-assembly-systems.md
  - wiki/concepts/super-resolution-imaging-of-tau-pathology.md
  - wiki/concepts/topology-aware-tubular-structure-segmentation.md
  - wiki/concepts/filament-instance-and-semantic-segmentation.md
  - wiki/concepts/cytoskeleton-segmentation-and-tracing.md
  - wiki/sources/SRC-0029-densely-connected-stacked-u-network-for-filament-segmentation.md
  - wiki/sources/SRC-0030-intersection-to-overpass-instance-segmentation-on-filamentous-structures.md
  - wiki/sources/SRC-0031-quantifying-actin-filaments-in-microscopic-images-using-keypoint.md
  - wiki/sources/SRC-0032-cldice-a-novel-topology-preserving-loss-function-for.md
  - wiki/sources/SRC-0033-deepvesselnet-vessel-segmentation-centerline-prediction-and-bifurcation-detection.md
  - wiki/sources/SRC-0034-tofie-topology-aware-fiber-extraction-workflow-for-3d.md
  - wiki/sources/SRC-0035-soax-software-for-quantification-of-3d-biopolymer-networks.md
  - wiki/sources/SRC-0068-nnu-net-self-adapting-framework-for-u-net.md
  - wiki/sources/SRC-0069-segment-anything.md
raw_sources_consulted: []
wiki_pages_updated:
  - wiki/answers/sted-tau-filament-topology-model-architecture.md
  - wiki/index.md
  - wiki/log.md
---

# How should STED tau filament morphology be quantified?

## Short answer

Treat the missing STED comparison as a measurement-design problem first and a neural-network problem second. The best architecture is still a topology-aware U-Net/nnU-Net-style segmentation-to-graph pipeline, but the important update is that the pipeline should be optimized for a fixed morphology feature table, not for pathology classification.

The recommended stack is:

1. a 2D or 2.5D nnU-Net-style baseline for tau-positive aggregate masks and region masks;
2. a multi-head filament model that also predicts centerlines, endpoints, junctions, local orientation, and distance-to-boundary or local width;
3. topology-aware training and validation, especially Dice/focal terms plus soft-clDice or skeleton-aware metrics;
4. graph extraction and measurement post-processing that turns masks into per-cell, per-compartment, per-field, seed-class, and DIV-level features;
5. hierarchical statistical comparison of those features across tauopathy seed class, DIV, donor or seed preparation, culture batch, field of view, and cell.

SAM-style promptable segmentation can help create masks or speed manual annotation, but it should not be the primary quantification engine for thin STED tau filaments because the SAM source itself flags missed fine structures and expects domain-specific methods to outperform it in specialized settings. [SRC-0069]

## Why this reframes the original answer

The manuscript reports that STED resolves seeded HA-tau aggregates in fixed neurons and that late-stage morphologies differ by tauopathy seed: AD-seeded aggregates are described as dense somatic clumps, Pick's disease seeds as long fibre bundles, and CBD/PSP seeds as long thin filamentous networks with occasional thicker bundles. It also says some STED morphology quantification is still in progress. [SRC-0064] That means the immediate scientific problem is not "can a model detect tau?" It is "can we convert heterogeneous STED morphology into robust, auditable numbers?"

The output should therefore be a morphology table with uncertainty and quality flags. A pathology classifier can be a secondary readout, but it should not replace interpretable morphology features. Otherwise the model may learn seed-class shortcuts while failing to explain whether the difference is compact clumping, bundle width, filament length, network connectedness, soma/neurite localization, or orientation.

## Architecture recommendation

Start with a conservative U-Net-family model, ideally nnU-Net-style configuration for the mask baseline. nnU-Net is relevant here because it emphasizes automatic adaptation of patch size, pooling geometry, preprocessing, inference, and cross-validation; its source argues that these configuration choices can matter more than architectural embellishments. [SRC-0068] For a small private STED dataset, that is a better first baseline than a large transformer-first architecture.

Add topology-specific heads rather than only making the encoder larger:

- **tau aggregate mask:** foreground aggregate or filament probability;
- **centerline mask:** skeleton-compatible filament ridge probability;
- **endpoint and junction keypoints:** graph nodes for branch and terminal events;
- **orientation bins or vector field:** local filament direction, useful for bundles, crossings, and anisotropy;
- **distance/radius map:** local thickness proxy for thin filament versus thick bundle comparisons;
- **optional compartment masks:** soma, neurite, and background regions, if the image channels support them.

This design follows the wiki's filament-analysis sources: stacked U-Net-style filament segmentation was motivated by reducing false disconnections that corrupt length and curvature measurements; orientation-aware outputs help separate filament fragments at intersections; keypoint plus fast-marching pipelines turn segmentation into count and length measurements; and DeepVesselNet provides a precedent for explicitly predicting topology-relevant centerline and bifurcation outputs. [SRC-0029] [SRC-0030] [SRC-0031] [SRC-0033]

Use topology-aware loss and evaluation. soft-clDice is directly relevant because it penalizes missing or spurious centerline branches more directly than overlap-only Dice/Jaccard losses. [SRC-0032] A practical loss is:

$$
\mathcal{L}
= \mathcal{L}_{mask}
+ \lambda_{cl}\mathcal{L}_{soft\text{-}clDice}
+ \lambda_{center}\mathcal{L}_{centerline}
+ \lambda_{kp}\mathcal{L}_{endpoint/junction}
+ \lambda_{ori}\mathcal{L}_{orientation}
+ \lambda_{width}\mathcal{L}_{width}.
$$

Tune these weights against graph-level validation, not only pixel Dice. A model with slightly worse pixel overlap but better centerline continuity, endpoint recovery, and feature reproducibility is likely more useful for the manuscript question.

## Quantification target

Predefine a small primary feature panel before looking at seed labels. I would make the primary STED morphology comparison a five-axis readout:

| Axis | Primary features | Biological contrast it targets |
| --- | --- | --- |
| Aggregate burden | tau-positive area fraction, object count, integrated intensity, cell-normalized and field-normalized load | aggregate amount, kept separate from topology |
| Compactness / clumping | object area, perimeter-normalized compactness, solidity, largest-object fraction, soma-localized aggregate fraction | AD-like dense somatic clumps reported in the draft |
| Filamentization | skeleton length per area, mean and distribution of edge lengths, endpoint density, branch length distribution | long filament or network formation |
| Bundling / thickness | local width or distance-transform distribution, thick-bundle fraction, width heterogeneity | PiD-like long fibre bundles versus thinner CBD/PSP-like networks |
| Network topology and orientation | connected components, largest connected component fraction, junction density, endpoint-to-junction ratio, node degree distribution, loop or persistence summaries, orientation anisotropy | connected thin networks, fragmented aggregates, and aligned bundles |

The feature table should be computed at multiple analysis levels: field of view, cell, soma compartment, neurite compartment, aggregate object, and graph edge. The manuscript's reported differences include somatic clumps and filamentous networks, so losing compartment information would throw away a key part of the STED phenotype. [SRC-0064]

Do not force every tau-positive object into a filament graph. Dense AD-like clumps may be better represented by object morphology, intensity texture, and compactness features, while PiD/CBD/PSP-like structures may need centerline and graph features. The pipeline should therefore keep both an object view and a graph view.

## Graph extraction and post-processing

After prediction, skeletonize the centerline map, attach endpoint and junction predictions, split or merge short spurs by calibrated rules, and store the result as a graph with coordinates, edge polylines, widths, intensities, and compartment labels. ToFiE is the closest wiki precedent for treating graph reconstruction itself as a topology-aware measurement workflow: it combines topology-preserving skeletonization, post-processing, node and edge validation, and distributional metrics such as edge-length and orientation comparisons. [SRC-0034]

SOAX should be run as a classical baseline or reviewer-facing sanity check, not as the only pipeline. It is useful because it extracts biopolymer centerlines and junctions and supports manual editing, but its source notes sensitivity to parameters, signal-to-noise ratio, filament separation, and dense unresolved structures. [SRC-0035]

For apparent crossings, be conservative. Published STED tau imaging reports strong lateral improvement but confocal-like axial resolution, and the manuscript's representative STED aggregate width is also a lateral-resolution readout. [SRC-0063] [SRC-0064] A 2D crossing in the STED image should be recorded as an image-graph junction or contact, not automatically interpreted as a true 3D physical branch.

## Annotation and validation plan

Use a stratified manual set across seed class, DIV, culture batch, donor or seed preparation, cell compartment, and image quality. Labels should include tau-positive masks, centerlines, endpoints, junctions or contacts, thick-bundle regions, clumps, soma/neurite compartments where possible, and an "ambiguous/unresolvable" label. The ambiguous class matters because STED can resolve more than confocal but still cannot settle all filament substructure questions that TEM or AFM would address. [SRC-0063]

Synthetic data should be used deliberately, not as a substitute for real validation. The filament instance and actin quantification sources use synthetic training data because real instance, endpoint, and junction labels are scarce. [SRC-0030] [SRC-0031] For this project, synthetic STED-like images should vary blur, noise, puncta, bundle width, crossings, clump density, and background, with known ground-truth graphs. They are most useful for pretraining orientation, endpoint, junction, and width heads and for stress-testing graph recovery.

Validation should report at least:

- pixel/object metrics: Dice, precision/recall, object detection F1;
- centerline metrics: clDice, SKIoU, centerline precision and sensitivity;
- graph metrics: endpoint F1, junction/contact F1, node recall, edge-length distribution error, orientation distribution error;
- feature stability: repeatability across annotators, thresholds, post-processing parameters, and held-out batches;
- biological robustness: whether the same seed-class and DIV trends survive cell-level and batch-level mixed-effects models.

This aligns the validation with the downstream measurements. A model that improves Dice while changing inferred branch counts or width distributions unpredictably has not solved the manuscript's unfinished comparison.

## Statistical comparison

Use seed class and DIV as biological predictors after feature extraction, not as inputs to the primary quantification model. Keep image metadata and experimental hierarchy explicit:

$$
\text{feature}_{cell}
\sim \text{seed class} \times \text{DIV}
+ (1 \mid \text{donor/seed prep})
+ (1 \mid \text{culture batch})
+ (1 \mid \text{field of view}).
$$

The exact random-effects structure should match the available metadata, but the principle is important: cells and fields are not independent replacements for biological or culture replicates. Report confidence intervals or posterior intervals for each morphology axis, and correct for multiple testing across the predefined feature panel.

For the manuscript, I would pre-register three primary contrasts:

- AD versus non-AD on soma-localized compact clumping;
- PiD versus CBD/PSP on bundle width and orientation anisotropy;
- CBD/PSP versus AD/PiD on thin-network length density, connectedness, and junction/contact density.

Those contrasts directly operationalize the draft's qualitative STED descriptions while keeping the conclusions provisional until the raw images and replicate structure are analyzed. [SRC-0064]

## Practical implementation order

1. Build a minimal ImageJ/napari-style annotation protocol and label 20-50 representative fields across seed class, DIV, and image quality.
2. Train an nnU-Net-style foreground and compartment baseline; use SAM only to accelerate annotation proposals and manual correction.
3. Add centerline, endpoint/junction, orientation, and width heads.
4. Generate synthetic STED-like networks to pretrain and stress-test graph outputs.
5. Extract graph and object features into a locked schema.
6. Freeze the feature definitions before running the seed-class/DIV statistics.
7. Keep a manual audit set for every figure-level morphology claim.

## Sources used

- [[wiki/sources/SRC-0064-versatile-neuronal-culture-system-templated-tau-assembly]]: manuscript motivation, tauopathy-seed STED morphology, draft status, incomplete quantification.
- [[wiki/sources/SRC-0063-sted-imaging-tau-filaments-alzheimer-disease]]: STED resolution and limits for tau filaments.
- [[wiki/sources/SRC-0068-nnu-net-self-adapting-framework-for-u-net]]: nnU-Net-style self-configuring U-Net baseline.
- [[wiki/sources/SRC-0069-segment-anything]]: promptable segmentation model and limitations for fine structures/domain-specific workflows.
- [[wiki/sources/SRC-0029-densely-connected-stacked-u-network-for-filament-segmentation]]: U-Net-style filament segmentation and skeleton-aware evaluation.
- [[wiki/sources/SRC-0030-intersection-to-overpass-instance-segmentation-on-filamentous-structures]]: orientation-aware instance decomposition.
- [[wiki/sources/SRC-0031-quantifying-actin-filaments-in-microscopic-images-using-keypoint]]: keypoint-plus-geodesic measurement pipeline.
- [[wiki/sources/SRC-0032-cldice-a-novel-topology-preserving-loss-function-for]]: soft-clDice topology-aware loss.
- [[wiki/sources/SRC-0033-deepvesselnet-vessel-segmentation-centerline-prediction-and-bifurcation-detection]]: centerline and bifurcation prediction precedent.
- [[wiki/sources/SRC-0034-tofie-topology-aware-fiber-extraction-workflow-for-3d]]: topology-aware graph reconstruction and validation workflow.
- [[wiki/sources/SRC-0035-soax-software-for-quantification-of-3d-biopolymer-networks]]: classical centerline/junction extraction baseline.
- [[wiki/sources/SRC-0004-automated-cytoskeletal-network-segmentation]]: broader cytoskeletal segmentation and tracing context.

## Wiki pages used

- [[wiki/index]]
- [[wiki/concepts/neuronal-templated-tau-assembly-systems]]
- [[wiki/concepts/super-resolution-imaging-of-tau-pathology]]
- [[wiki/concepts/topology-aware-tubular-structure-segmentation]]
- [[wiki/concepts/filament-instance-and-semantic-segmentation]]
- [[wiki/concepts/cytoskeleton-segmentation-and-tracing]]
- [[wiki/concepts/self-configuring-u-net-medical-image-segmentation]]
- [[wiki/concepts/promptable-segmentation-foundation-models]]

## Wiki updates made

- Revised this answer note to center the unfinished STED morphology quantification problem, add nnU-Net and SAM context, and define a concrete morphology feature table and validation plan.
- Updated [[wiki/index]] and [[wiki/log]] for the revised answer note.

## Remaining gaps

- This is still an analysis design, not a benchmark on the manuscript's raw STED images.
- The wiki does not yet contain a ground-truth annotation protocol for tau STED masks, centerlines, endpoints, junctions, clumps, thick bundles, or ambiguous regions.
- The manuscript is an unpublished draft and the STED morphology quantification is explicitly incomplete, so disease-specific morphology conclusions should remain provisional until the feature table is run on the raw images with replicate-aware statistics. [SRC-0064]
