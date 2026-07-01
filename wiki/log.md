---
type: overview
status: active
created: 2026-06-30
updated: 2026-07-01
areas: []
categories:
  - admin/wiki-maintenance
tags:
  - navigation
related: []
sources: []
sensitivity: public
encryption: none
graph_exclude: true
---
# Wiki Log

- 2026-06-29: Initialized the LLM wiki scaffold.
- 2026-06-29: Ingested SRC-0001, created source summary and core concept pages for the LLM wiki pattern.
- 2026-06-29: Updated schema and workflow guidance from SRC-0002 project design note without ingesting it as a wiki source.
- 2026-06-29: Ingested SRC-0002, added source summary, updated existing wiki-design concepts, and added metadata/privacy/task-contract concept pages.
- 2026-06-29: Imported and ingested SRC-0003, the Garnet force-field paper, adding molecular-simulation source, concept, and validation-scope question pages.
- 2026-06-29: Cleaned up SRC-0003 filenames to semantic normalized paths and verified source-page references.
- 2026-06-29: Applied ingestion completion contract QA migration to SRC-0003, expanding standard coverage and recording source-specific retrieval QA.
- 2026-06-29: Imported and ingested SRC-0004, a review on automated and semi-automated cytoskeletal network enhancement, segmentation, and tracing in microscopy images.
- 2026-06-29: Imported and deeply ingested SRC-0005, the Times Square Sampling paper on adaptive on-the-fly free energy estimation.
- 2026-06-29: Imported SRC-0006 and upgraded SRC-0005/SRC-0006 as the Times Square Sampling source bundle with math-deep equation, proof-map, implementation, and retrieval-QA coverage.
- 2026-06-30: Fixed Obsidian math formatting in existing Times Square Sampling wiki pages without re-ingesting sources.
- 2026-06-30: Added answer-note workflow guidance, template metadata, glossary terms, and `wiki/answers/` documentation.
- 2026-06-30: Added an answer note explaining the mathematics of TSS window free-energy stitching and updated the TSS implementation-patterns concept.
- 2026-06-30: Imported and ingested SRC-0007 through SRC-0009 as the accelerated weight histogram source bundle, adding source pages, an AWH concept page, and a validation-scope question.
- 2026-06-30: Imported and ingested SRC-0010 through SRC-0013 from the enhanced-sampling folder, including an OPES main/supplement bundle, MBAR with configuration mapping, and LaDyBUGS concept coverage.
- 2026-06-30: Imported and ingested SRC-0014 through SRC-0022 from the FF_train folder, covering SAXS lipid reparameterization, espaloma free-energy fine-tuning, symbolic-regression potentials, AWH replay optimization, MDRefine, and host-guest binding-data potential tuning.
- 2026-06-30: Imported and ingested SRC-0023, the original MBAR paper by Shirts and Chodera, adding a dedicated MBAR concept and updating free-energy estimation links.
- 2026-06-30: Imported and ingested SRC-0024 through SRC-0028 from the updated FF_train folder, covering StABlE MLFF training, ForceBalance water-model fitting, and OPC multipole-first water-model construction with supporting materials.
- 2026-06-30: Imported and ingested SRC-0029 through SRC-0035 from the Fibers folder, covering filament semantic and instance segmentation, actin quantification, clDice, DeepVesselNet, ToFiE, and SOAX.
- 2026-06-30: Imported and ingested SRC-0036 through SRC-0041 from the ML folder, covering ConFIG for PINNs, transferable/scalable Boltzmann generators, mixture-of-experts modeling, and GNN-to-symbolic-regression potentials.
- 2026-06-30: Imported and ingested SRC-0042 through SRC-0044 from the Datasets folder, covering OMol25, protein force-field benchmark datasets, and SPICE.
- 2026-06-30: Imported and ingested SRC-0045 through SRC-0047 from the BFE folder, covering OpenFE industrial RBFE benchmarking, FEP+/experimental reproducibility limits, and LAMMPS solvation free-energy decoupling.
- 2026-06-30: Imported and ingested SRC-0048 through SRC-0054 from the MD folder, covering pressure/stress tensor virials, smooth PME and prolate Ewald electrostatics, LINCS constraints, and GPU neighbor/nonbonded algorithms.
- 2026-06-30: Imported and ingested SRC-0055 and SRC-0056 from the RNA folder, covering UUCG tetraloop force-field failures and a comprehensive review of RNA molecular simulations.
- 2026-06-30: Imported and ingested SRC-0057/SRC-0058 as the overlay-databank-NMRlipids main/supplement bundle, adding concept coverage for reusable biomolecular simulation databanks.
- 2026-06-30: Hardened source-page navigation and raw-source links, added category registry and deterministic category index/audit tooling, and removed unused generic scaffold directories.
- 2026-06-30: Adopted the repository root as the Obsidian vault, normalized repo-root wikilinks and raw-source links, added deterministic category suggestions, repaired obvious multi-facet categories, and generated dashboard indexes without ingesting sources.
- 2026-06-30: Added `graph_exclude: true` metadata to navigation-heavy pages and documented the Obsidian Graph view filter.
- 2026-06-30: Added deterministic hygiene validation for skill frontmatter, source paths, local absolute path leakage, and graph-exclusion metadata; updated source import output to omit absolute original paths by default.
- 2026-06-30: Added an answer note comparing TSS with AWH and OPES as adaptive free-energy methods and updated the adaptive enhanced sampling concept.
- 2026-06-30: Imported and ingested SRC-0059, an arXiv perspective on six open questions for machine-learned interatomic potential foundation models.
- 2026-06-30: Updated category-page graph policy so `wiki/categories/` pages remain visible as Obsidian Graph grouping nodes.
- 2026-06-30: Imported and ingested SRC-0060, the UBio-MolFM technical report on a biology-focused molecular foundation model, UBio-Mol26, E2Former-V2, and short downstream biomolecular MD validations.
- 2026-06-30: Imported and ingested SRC-0061/SRC-0062 as the OpenFE RBFE benchmark journal-version bundle, adding the main JCIM article and supporting information with protocol-difference, outlier, and convergence diagnostics.
- 2026-07-01: Imported and ingested SRC-0063, a Journal of Structural Biology paper on STED imaging of tau filaments in Alzheimer's disease cortical grey matter, adding concept coverage for super-resolution imaging of tau pathology.
- 2026-07-01: Imported and ingested SRC-0064, a private unpublished DOCX manuscript draft on a neuronal culture system for templated tau assembly, adding draft-aware source and concept coverage.
- 2026-07-01: Imported and ingested SRC-0065, the ChemRxiv MACE-MDP preprint on molecular dipole/polarizability foundation modeling, SPICE-alpha, and IR/Raman spectroscopy benchmarks.
- 2026-07-01: Imported and ingested SRC-0066, the ChemRxiv presto preprint on fast MLP-driven bespoke SMIRNOFF valence force-field fitting.
- 2026-07-01: Imported and ingested SRC-0067, a Nature article on large-scale mHDX-MS discovery, analysis, and design of protein energy landscapes.
- 2026-07-01: Added an answer note recommending a topology-aware U-Net-style segmentation-to-graph architecture for STED tau filament morphology comparisons in SRC-0064 and updated the neuronal templated tau assembly concept.
- 2026-07-01: Imported and ingested SRC-0068, the nnU-Net arXiv paper on self-adapting U-Net-based medical image segmentation, adding concept coverage for self-configuring biomedical segmentation baselines.
- 2026-07-01: Checked requested clDice PDF `2003.07311v7.pdf` and confirmed it is byte-identical to already ingested SRC-0032; updated SRC-0032 metadata rather than creating a duplicate source.
- 2026-07-01: Imported and ingested SRC-0069, the Segment Anything arXiv paper introducing promptable segmentation, SAM, and the SA-1B dataset, adding concept coverage for promptable segmentation foundation models.
- 2026-07-01: Revised the STED tau topology answer note to focus on the unfinished SRC-0064 morphology quantification problem, adding nnU-Net/SAM context, a graph-and-object feature table, validation plan, and replicate-aware statistical design.
- 2026-07-01: Added an answer note on symbolic regression and differentiable functional-form search for a future Garnet force field, plus a reusable Garnet functional-form search concept.
- 2026-07-01: Added a deeper follow-up answer on where symbolic regression would fit in the Garnet pipeline, including residual distillation, parameter-count mismatch, multi-fidelity scoring, and per-epoch SR caveats.
- 2026-07-01: Merged the two Garnet symbolic-regression answer notes into one canonical answer page and updated navigation links.
- 2026-07-01: Added deterministic knowledge-graph build and query tooling, generated graph outputs, and updated answer-note workflow guidance to use graph neighborhoods where useful.
- 2026-07-01: Added first-class claim, question, and tension templates, future-ingestion guidance, audit tooling, dashboards, and a three-source pilot for TSS, Garnet, and clDice.
- 2026-07-01: Added structured author metadata guidance and audit tooling, plus a five-source author metadata pilot with one repeated-author entity page.
- 2026-07-01: Added generated concept dashboards for semantic browsing while keeping concept file paths flat and stable.
- 2026-07-01: Added an answer note on recurring validation problems across force-field fitting, machine-learning potentials, and free-energy estimators, plus a durable cross-domain validation concept.
- 2026-07-01: Added conservative citation-matching tooling, source citation metadata conventions, a generated citation-link dashboard, and pilot citation links for the TSS/AWH/MBAR cluster.
- 2026-07-01: Added an answer note comparing TSS, AWH, OPES, MBAR, LaDyBUGS, and Boltzmann generators by sample use, adaptive biasing, and reweighting, plus a reusable free-energy-estimation comparison section.
- 2026-07-01: Added source migration audit tooling and a generated dashboard for older source-page semantic backfill planning without re-ingesting sources.
- 2026-07-01: Backfilled first-class claims, questions, and tensions for the free-energy/adaptive-sampling source cluster without re-ingesting sources.
- 2026-07-01: Backfilled confirmed citation links for the OpenFE/FEP+/RBFE benchmark cluster using targeted reference checks without re-ingesting sources.
- 2026-07-01: Backfilled author metadata for the free-energy/adaptive-sampling source cluster and added repeated-author entities for Jack Lidmar and Michael R. Shirts without re-ingesting sources.
- 2026-07-01: Revised source-migration audit semantics to distinguish unchecked review, source-local semantic notes, no-needed first-class objects, linked first-class objects, and partial citation review without re-ingesting sources.
- 2026-07-01: Marked SRC-0001 and SRC-0002 as source-local wiki-design/admin sources for migration review without re-ingesting or rewriting source summaries.
- 2026-07-01: Completed semantic migration review statuses and cluster citation links for SRC-0005 through SRC-0013 and SRC-0023 without re-ingesting or rewriting source summaries.
- 2026-07-01: Backfilled semantic migration for the force-field fitting and experimental-refinement cluster, adding focused reusable claims and tensions without re-ingesting sources or rewriting summaries.
- 2026-07-01: Backfilled semantic migration for SRC-0047 through SRC-0054, adding focused MD implementation claims, questions, tensions, metadata, and local citation review without re-ingesting sources or rewriting summaries.
- 2026-07-01: Backfilled semantic migration for remaining RNA and overlay-databank sources plus scoped dataset citation review, adding reusable RNA validation and data-infrastructure claims without re-ingesting sources or rewriting summaries.
- 2026-07-02: Cleaned residual source-migration dashboard metadata debt by reviewing SRC-0018 local-draft metadata and preserving intentionally partial citation-review statuses without re-ingesting sources.
- 2026-07-01: Backfilled semantic migration for the ML potential, molecular dataset, and foundation-model cluster, adding focused dataset/model/benchmark validation claims without re-ingesting sources or rewriting summaries.
- 2026-07-01: Backfilled semantic migration for the RBFE, FEP+, OpenFE, and computational drug-discovery benchmark cluster, adding benchmark-specific validation claims without re-ingesting sources or rewriting summaries.
- 2026-07-01: Backfilled semantic migration for the bioimage, STED, and filament-segmentation cluster, adding topology, fiber-measurement, and STED validation objects without re-ingesting sources or rewriting summaries.
- 2026-07-02: Ran a graph-guided semantic-backfill acceptance answer on TSS, AWH, OPES, MBAR, LaDyBUGS, and Boltzmann generators, adding validation-diagnostic coverage without re-ingesting sources.
