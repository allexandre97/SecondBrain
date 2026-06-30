---
type: source
status: active
created: 2026-06-30
updated: 2026-06-30
source_id: SRC-0046
display_title: "The Maximal and Current Accuracy of Rigorous Protein-ligand Binding Free Energy Calculations"
short_title: "FEP+ Binding Free-Energy Accuracy"
aliases:
  - "SRC-0046"
  - "FEP+ Binding Free-Energy Accuracy"
  - "The Maximal and Current Accuracy of Rigorous Protein-ligand Binding Free Energy Calculations"
source_path: raw/sources/SRC-0046-the-maximal-and-current-accuracy-of-rigorous-protein.pdf
original_filename: "s42004-023-01019-9.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 3d133ce3a745255c773ce0ec2c76d0d3474f22ee2aa36c7c9937a1bb660d0d5d
areas:
  - research
categories:
  - research/molecular-simulation/binding-free-energy
tags:
  - FEP
  - FEP-plus
  - experimental-reproducibility
  - benchmarking
related:
  - "[[concepts/relative-binding-free-energy-benchmarking]]"
  - "[[concepts/free-energy-estimation]]"
sources:
  - SRC-0046
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: math-standard
---

# The Maximal and Current Accuracy of Rigorous Protein-ligand Binding Free Energy Calculations

Source ID: `SRC-0046`

## Raw source

- Repository path: `raw/sources/SRC-0046-the-maximal-and-current-accuracy-of-rigorous-protein.pdf`
- Local relative link: [Open raw source](../../raw/sources/SRC-0046-the-maximal-and-current-accuracy-of-rigorous-protein.pdf)

## Summary

This Communications Chemistry paper asks how accurate rigorous protein-ligand FEP calculations currently are and how close they are to experimental reproducibility limits. It combines an experimental relative-affinity reproducibility survey with a large FEP+ benchmark over curated protein-ligand congeneric series. [SRC-0046]

## Key Points

- The experimental survey compares relative binding free energies across assays for ligand series, rather than focusing on absolute affinity offsets. [SRC-0046, methods]
- The FEP benchmark collects congeneric series from prior FEP validation studies and includes transformation types such as R-group changes, charge changes, macrocyclization, scaffold hopping, fragments, and buried-water displacement. [SRC-0046, methods]
- Reported aggregate experimental reproducibility is a pairwise RMSE of 0.91 [0.83, 1.11] kcal/mol, while the FEP+ benchmark reports pairwise RMSE 1.25 [1.17, 1.33] kcal/mol. [SRC-0046, table 3]
- Experimental rank ordering is better than FEP+ rank ordering in the reported aggregate metrics: Kendall $\tau$ 0.71 [0.65, 0.74] for the experimental survey versus 0.51 [0.48, 0.55] for FEP+. [SRC-0046, table 3]
- The strongest practical message is that careful preparation of protonation states, ligand poses, rotamers, protein structures, and sampling details can move FEP+ accuracy toward experimental reproducibility. [SRC-0046, discussion]
- The authors caution that retrospective benchmark performance can be optimistic compared with prospective drug-discovery use. [SRC-0046, discussion]

## Key equations

**Assay ratio approximation, source Eq. (1) [SRC-0046]:**

$$
\frac{\mathrm{IC}_{50}^a}{\mathrm{IC}_{50}^b}
=
\frac{K_i^a}{K_i^b}
=
\frac{K_d^a}{K_d^b}.
$$

**Relative binding free energy from an assay readout, source Eq. (2) [SRC-0046]:**

$$
\Delta\Delta G^{ab} = -kT \ln \frac{X^b}{X^a}.
$$

Here $X$ may be an $\mathrm{IC}_{50}$, $K_d$, or $K_i$ from the same assay. [SRC-0046, methods]

**Weighted RMSE aggregation, source Eq. (3) [SRC-0046]:**

$$
\mathrm{RMSE} =
\sqrt{
\frac{1}{\sum_i^M w_i}
\sum_i^M w_i \mathrm{RMSE}_i^2
}.
$$

The paper uses edge counts for edgewise RMSE weights and compound counts for pairwise RMSE weights. [SRC-0046, metrics]

## Variable glossary

- $X$: assay readout used for affinity comparison, such as $\mathrm{IC}_{50}$, $K_d$, or $K_i$. [SRC-0046, methods]
- $\Delta\Delta G^{ab}$: relative binding free energy between ligands $a$ and $b$. [SRC-0046, methods]
- $k$: Boltzmann constant. [SRC-0046, methods]
- $T$: temperature, assumed to be 300 K in the assay comparisons. [SRC-0046, methods]
- $w_i$: benchmark aggregation weight for graph or assay comparison $i$. [SRC-0046, metrics]

## Equation inventory

| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |
| Assay ratio approximation | Eq. (1) | Key equations | Relates IC50, Ki, and Kd ratios for relative affinities | $\mathrm{IC}_{50}$, $K_i$, $K_d$ | Justifies mixed assay comparison under assumptions |
| Relative binding free energy | Eq. (2) | Key equations | Converts assay ratios into $\Delta\Delta G$ | $X$, $k$, $T$ | Needed for benchmark error computation |
| Weighted RMSE | Eq. (3) | Key equations | Aggregates per-graph or per-assay errors | $\mathrm{RMSE}_i$, $w_i$ | Needed to interpret reported benchmark summaries |

## Limitations

- The FEP benchmark is retrospective and partly assembled from prior successful FEP studies, so it may underestimate prospective error. [SRC-0046, discussion]
- The reported maximal/current accuracy estimates apply to the heterogeneous assay-quality regime represented in the benchmark and survey, not to all possible experimental settings. [SRC-0046, discussion]
- Some experimental affinity measurements differ substantially between assays, so FEP can appear inaccurate when the comparison experiment is itself poorly reproducible. [SRC-0046, discussion]
- The benchmark still lacks some target and transformation coverage, including more membrane proteins and transition-metal complexes. [SRC-0046, discussion]

## Links

- [[concepts/relative-binding-free-energy-benchmarking]]
- [[concepts/free-energy-estimation]]

## Ingestion QA

### Retrieval questions checked

- What experimental accuracy limit does the paper estimate for relative affinities?
- What current FEP+ benchmark accuracy does it report?
- Which equations convert assay readouts into relative binding free energies?
- Why does experimental reproducibility matter for judging FEP accuracy?
- What types of ligand transformations are included?
- What setup steps improve benchmark accuracy?
- Which caveats apply to prospective drug-discovery use?

### Coverage decision

Complete at `coverage_profile: math-standard`. The page captures the experimental-limit framing, benchmark metrics, central equations, and caveats needed for retrieval.

### Known gaps

- The wiki does not reproduce all per-system benchmark tables, supplementary curation details, or per-target structural-preparation decisions.
