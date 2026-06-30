---
type: source
status: active
created: 2026-06-30
updated: 2026-06-30
source_id: SRC-0030
display_title: "Intersection to Overpass: Instance Segmentation on Filamentous Structures"
short_title: "Filament Instance Segmentation"
aliases:
  - "SRC-0030"
  - "Filament Instance Segmentation"
  - "Intersection to Overpass: Instance Segmentation on Filamentous Structures"
source_path: raw/sources/SRC-0030-intersection-to-overpass-instance-segmentation-on-filamentous-structures.pdf
original_filename: "Liu19.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 9e958916e725212b130173b98588f20f742ccbeb358e19390be4907cb2b2c67a
areas:
  - research
categories:
  - research/bioimage-analysis/cytoskeleton
  - research/computer-vision/biomedical-imaging
tags:
  - filament-instance-segmentation
  - microtubules
  - orientation-aware-network
  - deep-learning
related:
  - "[[concepts/filament-instance-and-semantic-segmentation]]"
  - "[[concepts/deep-learning-cytoskeleton-image-analysis]]"
sources:
  - SRC-0030
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: standard
---

# Intersection to Overpass: Instance Segmentation on Filamentous Structures

Source ID: `SRC-0030`

## Raw source

- Repository path: `raw/sources/SRC-0030-intersection-to-overpass-instance-segmentation-on-filamentous-structures.pdf`
- Local relative link: [Open raw source](../../raw/sources/SRC-0030-intersection-to-overpass-instance-segmentation-on-filamentous-structures.pdf)

## Summary

Liu et al. address instance segmentation of filamentous structures by replacing difficult local intersection reasoning with an orientation-aware decomposition. A convolutional network outputs six orientation-associated filament layers, and a terminus-pairing algorithm reconnects fragments across layers into individual filaments. [SRC-0030]

## Key Points

- The central idea is to turn intersections into overpasses: branches separate filament fragments by orientation so junction areas do not need to be regrouped directly inside the intersection. [SRC-0030, section 2]
- The training data are synthetic: 120,000 small images are generated from deformed line segments split into six orientation bins, because labeled biological filament instances are scarce. [SRC-0030, section 2.1.2]
- The method takes semantic segmentation as input, so it inherits errors from the preceding segmentation stage. [SRC-0030, sections 3.2 and 3.5]
- On the authors' microtubule dataset of 10 images, the method reports F1 0.7161, precision 0.6456, recall 0.8189, and average SKIoU 0.8166, compared with SOAX F1 0.2691 and SIFNE F1 0.2875. [SRC-0030, table 1]
- The paper also tests a public microtubule dataset and a road-network dataset to show that the orientation decomposition can transfer to other elongated thin structures when semantic segmentation is adequate. [SRC-0030, sections 3.3-3.4]

## Limitations

- The real microtubule labels were manually corrected from the method's own outputs, which the authors explicitly identify as a possible bias toward their approach. [SRC-0030, section 3.2]
- Failure modes include incomplete reconstruction from the six side outputs, incorrect terminus pairing, and dependence on segmentation accuracy. [SRC-0030, section 3.5]
- The method is slower than the SIFNE regrouping step on the reported full images, although faster than SOAX end-to-end in the paper's comparison. [SRC-0030, section 3.2]

## Links

- [[concepts/filament-instance-and-semantic-segmentation]]
- [[concepts/deep-learning-cytoskeleton-image-analysis]]

## Ingestion QA

### Retrieval questions checked

- What problem does the paper solve?
- What does "intersection to overpass" mean?
- How are orientation-associated branches used?
- What role does the terminus-pairing algorithm play?
- What data support the method?
- What are the reported limitations?

### Coverage decision

Complete at `coverage_profile: standard`. The source page captures the method, evidence, metrics, dependencies, limitations, and links to shared filament-segmentation concepts.

### Known gaps

- The terminus-pairing geometric scoring details are summarized rather than fully specified.
- The wiki does not preserve all qualitative examples from the figures.
