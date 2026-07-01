---
type: source
status: active
created: 2026-07-01
updated: 2026-07-01
source_id: SRC-0064
display_title: "Versatile Neuronal Culture System of Faithful Templated Tau Assembly"
short_title: "Neuronal Templated Tau Assembly Manuscript"
aliases:
  - "SRC-0064"
  - "Neuronal Templated Tau Assembly Manuscript"
  - "Versatile neuronal culture system of faithful templated tau assembly"
source_path: raw/sources/SRC-0064-versatile-neuronal-culture-system-templated-tau-assembly.docx
imported_path: raw/sources/SRC-0064-versatile-neuronal-culture-system-templated-tau-assembly.docx
original_filename: "neurons_ms_20260615.docx"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 0532d2faec756a6a19f404c5da1f86dedf62317a7c01c5b0a0b303f5a6c2cd84
areas:
  - research
categories:
  - research/biomolecules/proteins
  - research/computer-vision/biomedical-imaging
tags:
  - manuscript-draft
  - tau
  - tauopathy
  - neuronal-culture
  - cryo-EM
  - STED
related:
  - "[[wiki/concepts/neuronal-templated-tau-assembly-systems]]"
  - "[[wiki/concepts/super-resolution-imaging-of-tau-pathology]]"
sources:
  - SRC-0064
sensitivity: private
encryption: none
ingestion_status: complete
coverage_profile: standard
source_kind: manuscript-draft
peer_review_status: not-peer-reviewed
---

# Versatile Neuronal Culture System of Faithful Templated Tau Assembly

Source ID: `SRC-0064`

## Raw source

- Repository path: `raw/sources/SRC-0064-versatile-neuronal-culture-system-templated-tau-assembly.docx`
- Open raw source: [raw/sources/SRC-0064-versatile-neuronal-culture-system-templated-tau-assembly.docx](../../raw/sources/SRC-0064-versatile-neuronal-culture-system-templated-tau-assembly.docx)

## Status note

This source is an unpublished MS Word manuscript draft, not a peer-reviewed article. Treat its findings as manuscript-reported and provisional; one section explicitly notes that quantification is still in progress. [SRC-0064]

DOCX metadata records creator and last modifier as Melissa Huang, creation time `2026-06-15T09:18:00Z`, modification time `2026-06-15T15:01:00Z`, revision 3, 22 pages, and about 5,525 words. [SRC-0064]

## Summary

The manuscript describes a mixed primary murine cortical culture system in which AAV-mediated neuronal expression of full-length human tau isoforms enables brain-derived tau seeds to induce HA-tagged templated tau assemblies. The central reported claim is that Alzheimer's disease tau seeds drive robust neuronal tau aggregation and yield cryo-EM tau filaments identical to Alzheimer's paired helical filaments, while seeds from Pick's disease, corticobasal degeneration, and progressive supranuclear palsy produce morphologically distinct aggregates by STED imaging. [SRC-0064]

## Key Points

- The system uses mixed primary cortical cultures from P0/P1 wild-type mice and AAV1/2-mediated expression of HA-tagged 0N3R or 0N4R human tau under a neuronal hSyn promoter. [SRC-0064]
- Addition of Alzheimer's disease brain-derived tau seeds at DIV03 induces somatic and neuritic HA-tau inclusions by DIV14, with sarkosyl-insoluble tau detectable and filamentous assemblies supported by pFTAA, AT100, and immuno-EM readouts. [SRC-0064]
- The manuscript uses HA-0N3R-V337M tau to distinguish newly templated assemblies from input seed; cryo-EM density at residue 337 is reported as consistent with methionine, supporting that the extracted filaments came from expressed mutant tau rather than re-extracted seed. [SRC-0064]
- Live-cell imaging with dendra2-tagged tau is reported to show bright aggregates appearing days after seeding, moving along neuronal processes, and growing in soma over hours. [SRC-0064]
- STED imaging resolves seeded HA-tau aggregates in fixed neurons, including a representative 71 nm full-width-half-maximum aggregate compared with 210 nm by confocal imaging. [SRC-0064]
- The draft reports different late-stage STED morphologies for tauopathy seeds: AD-seeded aggregates form dense somatic clumps, Pick's disease seeds form long fibre bundles, and corticobasal degeneration or progressive supranuclear palsy seeds form long thin filamentous networks with occasional thicker bundles. [SRC-0064]

## Methods and Evidence

- Culture and delivery: primary mixed cortical cultures are transduced at DIV0 with AAV vectors encoding HA-tagged human tau constructs and seeded at DIV03 with sarkosyl-insoluble brain-derived tau extracts. [SRC-0064]
- Biochemical evidence: sarkosyl-insoluble tau extraction and immunoblotting are used to detect insoluble tau after seeding. [SRC-0064]
- Imaging evidence: immunocytochemistry, confocal microscopy, live-cell imaging, STED microscopy, negative-stain EM, immuno-EM, and cryo-EM are used to characterize tau assemblies. [SRC-0064]
- Structural evidence: cryo-EM of HA-0N3R-V337M seeded cultures is used to argue that AD-seeded neuronal cultures generate PHFs with the Alzheimer fold rather than merely recovering the seed. [SRC-0064]

## Limitations and Caveats

- This is a manuscript draft rather than a peer-reviewed article, so claims should not be treated as externally validated. [SRC-0064]
- The manuscript itself notes that quantification of some STED morphology comparisons is still in progress. [SRC-0064]
- High seed concentrations can lead to seed re-extraction, which would confound downstream cryo-EM analysis. [SRC-0064]
- AAV-mediated tau overexpression may introduce artifacts, although the draft reports using viral titres without overt toxicity and notes that lower titres or Mapt knock-out cells may be needed for some questions. [SRC-0064]
- The primary neuron culture timeframe and relative immaturity limit observation of overt neurodegenerative phenotypes. [SRC-0064]

## Links

- [[wiki/concepts/neuronal-templated-tau-assembly-systems]]
- [[wiki/concepts/super-resolution-imaging-of-tau-pathology]]
- [[wiki/sources/SRC-0063-sted-imaging-tau-filaments-alzheimer-disease]]

## Metadata notes

- File type: DOCX manuscript draft.
- The source was imported as a single physical source, not as a bundle.
- Category uncertainty: a future registry pass may warrant a reusable neurodegeneration or cell-culture model category; for now this page uses existing protein and biomedical-imaging facets.

## Ingestion QA

### Retrieval questions checked

- Is this source peer reviewed?
- What model system does the manuscript describe?
- How does it distinguish templated assemblies from input tau seed?
- What evidence supports Alzheimer's PHF formation in the culture system?
- What role does STED imaging play?
- How are AD, Pick's disease, corticobasal degeneration, and progressive supranuclear palsy seeds reported to differ?
- What limitations are acknowledged by the draft?
- What claims should not be overgeneralized?

### Coverage decision

Complete at `coverage_profile: standard`. The source page captures the draft status, provenance, central model-system claim, main methods, reported evidence, limitations, and retrieval caveats without presenting the manuscript as peer-reviewed.

### Known gaps

- The wiki does not reproduce figure panels, supplementary videos, reference details, or incomplete quantification.
- DOCX comments, if any, were not separately represented; the archive listing did not show a comments file.
