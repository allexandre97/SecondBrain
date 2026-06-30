---
type: source
status: active
created: 2026-06-30
updated: 2026-06-30
source_id: SRC-0034
display_title: "ToFiE, a Topology-Aware Fiber Extraction Workflow for 3D Biological Fiber Networks"
short_title: "ToFiE Fiber Extraction"
aliases:
  - "SRC-0034"
  - "ToFiE Fiber Extraction"
  - "ToFiE, a Topology-Aware Fiber Extraction Workflow for 3D Biological Fiber Networks"
source_path: raw/sources/SRC-0034-tofie-topology-aware-fiber-extraction-workflow-for-3d.pdf
original_filename: "Togo26.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 79ed5da5189f88df87d75619efe167279392119e09e248aea2492cbb1e0a1803
areas:
  - research
categories:
  - research/bioimage-analysis/cytoskeleton
  - research/computer-vision/biomedical-imaging
tags:
  - fiber-reconstruction
  - collagen
  - topology
  - 3d-microscopy
related:
  - "[[concepts/topology-aware-fiber-network-reconstruction]]"
  - "[[concepts/cytoskeleton-segmentation-and-tracing]]"
sources:
  - SRC-0034
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: standard
---

# ToFiE, a Topology-Aware Fiber Extraction Workflow for 3D Biological Fiber Networks

Source ID: `SRC-0034`

## Raw source

- Repository path: `raw/sources/SRC-0034-tofie-topology-aware-fiber-extraction-workflow-for-3d.pdf`
- Local relative link: [Open raw source](../../raw/sources/SRC-0034-tofie-topology-aware-fiber-extraction-workflow-for-3d.pdf)

## Summary

Togo et al. introduce ToFiE, an open-source semi-automated workflow for topology-aware 3D reconstruction of dense, heterogeneous biological fiber networks from microscopy images. The paper validates the workflow on synthetic fluorescence images with known topology and applies it to collagen I networks imaged by confocal fluorescence microscopy. [SRC-0034]

## Key Points

- ToFiE combines image preprocessing, Discrete-Morse-theory and persistent-homology-based skeletonization through DisPerSe, and post-processing that refines skeletons into biologically meaningful fibers, junctions, and graph connectivity. [SRC-0034, section 2.1]
- The workflow is motivated by the mechanical relevance of network topology: collagen and other stiff fiber networks are predicted to have mechanics linked to connectivity. [SRC-0034, section 1]
- Synthetic validation uses artificial confocal fluorescence images of networks with known topology and varying signal-to-noise ratio, then evaluates edge-length and orientation distributions with Kullback-Leibler divergence and node recovery with recall. [SRC-0034, sections 2.3 and 3.1]
- For synthetic networks with average connectivity between about 3 and 4 and SNR above 1, ToFiE reports high node recall, including approximately 0.99 for 3-junctions and 0.95 for 4-junctions. [SRC-0034, section 3.1]
- The method struggles more with higher-connectivity junctions, especially above $k_n > 6$, and the paper emphasizes calibration of the junction-merging length threshold for the target network. [SRC-0034, sections 3.1 and 4]
- Compared with Otsu thresholding plus Lee skeleton thinning, ToFiE is presented as better suited to dense collagen images with heterogeneous intensity and bright bundles because it does not rely on absolute intensity thresholding in the same way. [SRC-0034, section 4]

## Metric notes

- The source uses Kullback-Leibler divergence to compare reconstructed and ground-truth edge-length and azimuthal-angle distributions. [SRC-0034, section 2.3]
- Node recall is defined as the fraction of ground-truth nodes correctly reconstructed with matching connectivity within a spatial tolerance. [SRC-0034, section 2.3]
- Experimental collagen reconstructions are also checked by manual junction inspection, producing a junction accuracy score. [SRC-0034, section 2.4.3]

## Limitations

- ToFiE is semi-automated and requires parameter calibration for each dataset, especially the length threshold used in skeleton refinement. [SRC-0034, section 4]
- Higher-connectivity junctions have lower recall in synthetic tests, with limitations attributed partly to simulated image quality, sampling strategy, and discretization. [SRC-0034, section 4]
- The workflow does not yet include time-step tracking, which the authors identify as a useful extension for deformation and cell-mediated remodeling studies. [SRC-0034, section 4]
- ToFiE depends on DisPerSe for topology-preserving skeletonization; DisPerSe is an independently licensed package. [SRC-0034, section 2.1]

## Links

- [[concepts/topology-aware-fiber-network-reconstruction]]
- [[concepts/cytoskeleton-segmentation-and-tracing]]

## Ingestion QA

### Retrieval questions checked

- What is ToFiE?
- Why is topology preservation important for collagen and other fiber networks?
- What are the workflow stages?
- How is ToFiE validated on synthetic data?
- What metrics are used?
- What does it show on collagen networks?
- What limitations remain?

### Coverage decision

Complete at `coverage_profile: standard`. The page records the workflow, validation design, core metrics, results, limitations, and relation to topology-aware reconstruction concepts.

### Known gaps

- The wiki does not reproduce all supplementary parameter settings.
- Detailed collagen sample-preparation protocol remains in the raw source.
