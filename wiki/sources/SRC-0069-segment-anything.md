---
type: source
status: active
created: 2026-07-01
updated: 2026-07-01
source_id: SRC-0069
display_title: "Segment Anything"
short_title: "Segment Anything"
aliases:
  - "SRC-0069"
  - "Segment Anything"
  - "SAM"
  - "Segment Anything Model"
  - "SA-1B"
  - "arXiv:2304.02643v1"
source_path: raw/sources/SRC-0069-segment-anything.pdf
imported_path: raw/sources/SRC-0069-segment-anything.pdf
original_filename: "2304.02643v1.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: c6ca524e47200c3e542587ca76ac1dbc89cc67340f948c819250d16fdbd90cfb
areas:
  - research
categories:
  - research/computer-vision/biomedical-imaging
  - research/machine-learning/scientific-modeling
  - research/data-management
  - research/experimental-benchmarking
tags:
  - image-segmentation
  - foundation-model
  - promptable-segmentation
  - sam
  - dataset
related:
  - "[[wiki/concepts/promptable-segmentation-foundation-models]]"
  - "[[wiki/concepts/deep-learning-cytoskeleton-image-analysis]]"
  - "[[wiki/concepts/self-configuring-u-net-medical-image-segmentation]]"
sources:
  - SRC-0069
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: standard
---

# Segment Anything

Source ID: `SRC-0069`

## Raw source

- Repository path: `raw/sources/SRC-0069-segment-anything.pdf`
- Open raw source: [raw/sources/SRC-0069-segment-anything.pdf](../../raw/sources/SRC-0069-segment-anything.pdf)

## Summary

Kirillov et al. introduce the Segment Anything project: a promptable segmentation task, the Segment Anything Model (SAM), and the SA-1B dataset of over 1 billion masks on 11 million licensed and privacy-protecting images. The paper frames SAM as a segmentation foundation-model attempt, trained for zero-shot transfer through prompts rather than for a fixed segmentation label set. [SRC-0069, abstract and section 1]

## Key Points

- The promptable segmentation task asks the model to return a valid mask for any segmentation prompt, including points, boxes, masks, or text-like prompts; ambiguous prompts are acceptable if the output is a reasonable mask for at least one valid object interpretation. [SRC-0069, sections 1-2]
- SAM has three main components: a heavy image encoder, a flexible prompt encoder, and a lightweight mask decoder that can be queried repeatedly after the image embedding is computed. [SRC-0069, section 3]
- The model is explicitly ambiguity-aware: for ambiguous prompts it predicts multiple masks and confidence scores, which helps avoid averaging incompatible valid masks. [SRC-0069, section 3]
- SA-1B was built with a three-stage data engine: assisted manual annotation, semi-automatic annotation, and fully automatic mask generation from grid prompts. [SRC-0069, section 4]
- The released dataset contains 11 million images and 1.1 billion masks; 99.1% of masks were generated fully automatically, with sampled automatic masks compared against professional corrections. [SRC-0069, section 5]
- The paper includes a Responsible AI analysis covering geographic/income representation and segmentation performance across perceived people attributes, while noting possible biases when SAM is used inside larger systems. [SRC-0069, section 6]
- Zero-shot experiments test single-point masks, edge detection, object proposals, instance segmentation via detector-box prompts, and exploratory text-to-mask prediction. [SRC-0069, section 7]
- The authors report that SAM beats RITM on 16 of 23 datasets by mean IoU for one-point prompting, and that human annotators rated SAM masks higher than RITM masks in the evaluated subset. [SRC-0069, section 7.1]

## Limitations

- SAM can miss fine structures, hallucinate small disconnected components, and produce less crisp boundaries than methods that zoom in computationally. [SRC-0069, section 7.6]
- Dedicated interactive segmentation tools can outperform SAM when many points are provided, because SAM prioritizes breadth and generality rather than maximizing high-IoU interactive segmentation. [SRC-0069, section 7.6]
- The full system is not real-time when the heavy image encoder must run, even though prompt decoding is fast after image embedding. [SRC-0069, sections 3 and 7.6]
- Text-to-mask prompting is presented as exploratory and not fully robust. [SRC-0069, sections 7.5-7.6]
- The paper states that domain-specific tools are expected to outperform SAM in their own domains, which is important for biological microscopy or fiber-network workflows. [SRC-0069, section 7.6]
- The authors explicitly leave open whether SAM will ultimately be treated as a foundation model by the community. [SRC-0069, section 8]

## Links

- [[wiki/concepts/promptable-segmentation-foundation-models]]
- [[wiki/concepts/deep-learning-cytoskeleton-image-analysis]]
- [[wiki/concepts/self-configuring-u-net-medical-image-segmentation]]

## Ingestion QA

### Retrieval questions checked

- What are the three components of the Segment Anything project?
- What is promptable segmentation?
- What architecture does SAM use?
- How was SA-1B collected?
- What evidence supports zero-shot segmentation transfer?
- What Responsible AI analysis does the paper report?
- What limitations matter for biological or fiber-image segmentation?

### Coverage decision

Complete at `coverage_profile: standard`. The source page and linked concept page cover the task/model/data contribution, dataset scale, evaluation scope, Responsible AI notes, and limitations relevant to reuse as a segmentation foundation model.

### Known gaps

- The wiki does not reproduce appendix implementation details, full benchmark tables, model cards, dataset cards, or annotation guidelines.
- Later SAM versions, downstream biomedical adaptations, and post-release evaluations are outside this source ingestion.
