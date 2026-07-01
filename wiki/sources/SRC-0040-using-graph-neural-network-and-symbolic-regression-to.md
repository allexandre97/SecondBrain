---
type: source
status: active
created: 2026-06-30
updated: 2026-06-30
source_id: SRC-0040
display_title: "Using Graph Neural Network and Symbolic Regression to Model Disordered Systems"
short_title: "GNN to Symbolic-Regression Potentials"
aliases:
  - "SRC-0040"
  - "GNN to Symbolic-Regression Potentials"
  - "Using Graph Neural Network and Symbolic Regression to Model Disordered Systems"
source_path: raw/sources/SRC-0040-using-graph-neural-network-and-symbolic-regression-to.pdf
original_filename: "s41598-025-05205-8.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 70fd4354bfb7e8bebbf3f7b80c1b1f2cbbf87a506cab2ae6a4b41be1a795725d
authors:
  - "Ruoxia Chen"
  - "Mathieu Bauchy"
  - "Wei Wang"
  - "Yizhou Sun"
  - "Xiaojie Tao"
  - "Jaime Marian"
author_entities: []
year: 2025
venue: "Scientific Reports"
doi: "10.1038/s41598-025-05205-8"
arxiv:
metadata_review_status: reviewed
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/machine-learning/scientific-modeling
  - research/machine-learning/molecular-modeling
tags:
  - graph-neural-networks
  - symbolic-regression
  - disordered-materials
  - interatomic-potentials
related:
  - "[[wiki/concepts/gnn-to-symbolic-regression-potentials]]"
  - "[[wiki/concepts/symbolic-regression-interatomic-potentials]]"
sources:
  - SRC-0040
cites_sources: []
citation_match_status: reviewed
cqt_review_status: source-local
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: standard
---

# Using Graph Neural Network and Symbolic Regression to Model Disordered Systems

Source ID: `SRC-0040`

## Raw source

- Repository path: `raw/sources/SRC-0040-using-graph-neural-network-and-symbolic-regression-to.pdf`
- Open raw source: [raw/sources/SRC-0040-using-graph-neural-network-and-symbolic-regression-to.pdf](../../raw/sources/SRC-0040-using-graph-neural-network-and-symbolic-regression-to.pdf)

## Summary

Chen et al. propose a two-stage workflow that trains a graph neural network on system-level molecular-dynamics energies, then uses symbolic regression on the trained edge model outputs to recover an interpretable pair-potential expression. The paper validates the idea on a normalized Lennard-Jones system. [SRC-0040]

## Key Points

- The workflow first trains a GNN to predict total system potential energy from atomic coordinates, then records edge-model outputs for atom pairs and fits symbolic expressions from pair distance to edge output. [SRC-0040, Materials and methods]
- The benchmark system uses 128 identical atoms with normalized Lennard-Jones interactions, cutoff $r_c=2.5$, and a dataset of 7000 MD configurations collected through iterative quench simulations. [SRC-0040, Dataset]
- The GNN is intentionally small and physically structured: the learnable part is an edge MLP, while node and global updates use summation to mirror pairwise additive energy. [SRC-0040, GNN results]
- The paper reports GNN average RMSE per atom of 0.028028 over five runs, about 1.36% relative error compared with the average potential energy per atom in the MD dataset. [SRC-0040, GNN results]
- Low-temperature data below the glass-transition temperature gives better coverage of short-range, high-curvature repulsive regions and helps symbolic regression recover the Lennard-Jones form more effectively. [SRC-0040, Symbolic regression results]

## Limitations

- The current setup assumes energy decomposes into two-body terms, which holds for Lennard-Jones but may fail for many-body systems. [SRC-0040]
- The edge representation lacks rotational invariance and introduces cutoff discontinuities; the authors suggest distance/angular features and smooth cutoffs as future improvements. [SRC-0040]
- Extending to many-body systems would likely increase symbolic complexity and development cost even if the final expression remains cheap at runtime. [SRC-0040]

## Claims

- Source-local only: the reusable content is already represented through the GNN-to-symbolic-regression and Garnet functional-form concepts; no separate first-class claim is needed for this cluster. [SRC-0040]

## Citation Links

- No confirmed links to currently ingested wiki sources were identified during the targeted cluster pass. [SRC-0040]

## Links

- [[wiki/concepts/gnn-to-symbolic-regression-potentials]]
- [[wiki/concepts/symbolic-regression-interatomic-potentials]]
- [[wiki/concepts/automated-force-field-training]]

## Ingestion QA

### Retrieval questions checked

- What is the two-stage GNN plus symbolic-regression workflow?
- Why use Lennard-Jones as the benchmark?
- What data are used to train the GNN?
- How are edge outputs turned into symbolic-regression data?
- What evidence supports the method?
- What limits generalization beyond pair potentials?

### Coverage decision

Complete at `coverage_profile: standard`. The page captures the workflow, benchmark, evidence, and limitations without reproducing every candidate expression.

### Known gaps

- Exact selected symbolic expressions and supplementary training details remain in the raw source.
