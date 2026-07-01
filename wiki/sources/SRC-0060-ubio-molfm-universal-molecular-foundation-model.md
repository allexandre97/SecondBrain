---
type: source
status: active
created: 2026-06-30
updated: 2026-06-30
source_id: SRC-0060
display_title: "UBio-MolFM: A Universal Molecular Foundation Model for Bio-Systems"
short_title: "UBio-MolFM"
aliases:
  - "SRC-0060"
  - "UBio-MolFM"
  - "UBio-Mol26"
  - "E2Former-V2"
source_path: raw/sources/SRC-0060-ubio-molfm-universal-molecular-foundation-model.pdf
imported_path: raw/sources/SRC-0060-ubio-molfm-universal-molecular-foundation-model.pdf
original_filename: "2602.17709v1.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 26d60ebb1b5151f0d756347e9952da5858e9a56a53450551d5e44b84ed25ae37
authors:
  - "UBio Team"
author_entities: []
year: 2026
venue: "arXiv"
doi:
arxiv: "2602.17709"
metadata_review_status: reviewed
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/machine-learning/molecular-modeling
  - research/molecular-simulation/datasets
  - research/molecular-simulation/molecular-dynamics
  - research/biomolecules/proteins
  - research/biomolecules/rna
  - research/high-performance-computing
  - research/experimental-benchmarking
tags:
  - machine-learning-force-fields
  - foundation-models
  - equivariant-transformers
  - biological-simulation
  - quantum-chemistry
related:
  - "[[wiki/concepts/ubio-molfm-biological-molecular-foundation-model]]"
  - "[[wiki/concepts/machine-learned-interatomic-potential-foundation-models]]"
  - "[[wiki/concepts/machine-learning-potential-datasets]]"
  - "[[wiki/concepts/stability-aware-mlff-training]]"
sources:
  - SRC-0060
cites_sources:
  - SRC-0042
  - SRC-0044
citation_match_status: partial
cqt_review_status: linked
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: math-standard
---

# UBio-MolFM: A Universal Molecular Foundation Model for Bio-Systems

Source ID: `SRC-0060`

## Raw source

- Repository path: `raw/sources/SRC-0060-ubio-molfm-universal-molecular-foundation-model.pdf`
- Open raw source: [raw/sources/SRC-0060-ubio-molfm-universal-molecular-foundation-model.pdf](../../raw/sources/SRC-0060-ubio-molfm-universal-molecular-foundation-model.pdf)

## Summary

UBio-MolFM is a biology-focused molecular foundation model framework for all-atom biomolecular simulation. It combines the UBio-Mol26 dataset, the E2Former-V2 equivariant transformer, and a three-stage curriculum that moves from broad energy initialization to conservative energy-force training and biology-focused multi-fidelity fine-tuning. [SRC-0060]

The paper's central claim is that a biology-specific data distribution and hardware-aware equivariant architecture can narrow the scale-accuracy gap between quantum-mechanical fidelity and biomolecular system size. The reported evidence covers large out-of-distribution energy/force tests, short downstream molecular dynamics tests for water, ions, cyclic peptide conformations, and RNA magnesium coordination, plus single-H100 inference throughput benchmarks. [SRC-0060, sections 2-3]

## Key Points

- UBio-Mol26 contains 17 million bio-focused configurations, with system sizes up to about 1,200 atoms and an average size around 440 atoms in the overall dataset. [SRC-0060, section 4.1]
- The dataset is built with a two-pronged strategy: bottom-up enumeration of biochemical building blocks and top-down sampling of native protein environments from AlphaFold structures. [SRC-0060, section 4.1.1]
- Top-down sampling is currently applied to proteins only; DNA/RNA and cross-modal interfaces are more limited and largely bottom-up in this version. [SRC-0060, section 4.1.1]
- E2Former-V2 combines short-range local equivariant layers with long-short range modeling, Equivariant Axis-Aligned Sparsification, and an on-the-fly attention kernel to reduce tensor-product and edge-materialization bottlenecks. [SRC-0060, section 4.2]
- The training curriculum has three stages: fast OMol25 energy initialization with a direct force head, conservative energy-force consistency using forces as energy gradients, and mixed OMol25/SVP/TZVPD fine-tuning with separate SVP and high-fidelity heads. [SRC-0060, section 4.3.1]
- On the large extrapolation test set, UBio-MolFM (S3) improves protein force and relative-energy errors over the reported MACE-OMol and UMA-S-1p1 baselines, but DNA optimization has a worse consecutive-frame energy-difference metric after Stage 3 than after Stage 2. [SRC-0060, section 2.1.2]
- Downstream MD evidence is short-timescale: 200 ps NVT simulations for pure water, 0.15 mol/L NaCl, and Cyclosporine A, plus an RNA 1L2X magnesium-coordination simulation. [SRC-0060, section 2.2]
- The public-resource plan includes a protein-focused UBio-Protein26 5M dataset, E2Former-V2 code, and planned model-weight releases. [SRC-0060, section 5]

## Mathematical structure

The report is architecture- and implementation-heavy. Its central mathematical structure is SO(3)-equivariant message passing with conservative forces from an energy model. [SRC-0060, section 4.2]

Node features are represented as a direct sum of irreducible SO(3) components: [SRC-0060, eqs. 1-2]

$$
h_i=\bigoplus_{\ell=0}^{L} h_i^{(\ell)}, \qquad
h_i^{(\ell)} \mapsto D^{(\ell)}(R)h_i^{(\ell)}.
$$

Solid spherical harmonics encode geometry: [SRC-0060, eq. 3]

$$
R_m^{(\ell)}(\vec r)=\|\vec r\|^\ell Y_{\ell,m}\left(\frac{\vec r}{\|\vec r\|}\right).
$$

Equivariant attention aggregates neighbor messages with scalar invariant weights: [SRC-0060, eq. 5]

$$
m_i=\sum_{j\in N(i)}\alpha_{ij}m_{ij}.
$$

Long-short range modeling separates local and nonlocal neighborhoods: [SRC-0060, eq. 6]

$$
m_i^S=\sum_{j\in N_{r_{\mathrm{short}}}(i)}\alpha_{ij}m_{ij},
\qquad
m_i^L=\sum_{j\in N_{r_{\mathrm{long}}}(i)}\alpha_{ij}m_{ij}.
$$

Forces are computed conservatively as energy gradients: [SRC-0060, eqs. 7 and 10]

$$
\hat F_i=-\frac{\partial \hat E}{\partial \vec r_i}.
$$

## Variable glossary

- $h_i$: equivariant feature vector for atom or node $i$. [SRC-0060, section 4.2.1]
- $\ell$: angular momentum degree of an irreducible SO(3) representation. [SRC-0060, section 4.2.1]
- $m$: magnetic index for a degree-$\ell$ component or spherical harmonic. [SRC-0060, section 4.2.1]
- $D^{(\ell)}(R)$: Wigner-D matrix for rotation $R$. [SRC-0060, section 4.2.1]
- $\vec r_i$, $\vec r_{ij}$: atomic position and relative displacement. [SRC-0060, section 4.2.1]
- $\alpha_{ij}$: scalar attention weight on edge or neighbor pair $(i,j)$. [SRC-0060, eq. 5]
- $r_{\mathrm{short}}$, $r_{\mathrm{long}}$: short- and long-range neighborhood radii, described as about 5 Angstrom and 15 Angstrom respectively. [SRC-0060, section 4.2.1]
- $\hat E$, $\hat F_i$: predicted energy and conservative force. [SRC-0060, eq. 7]

## Equation inventory

| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |
| Irrep node features | SRC-0060, eqs. 1-2 | This page | Defines SO(3)-equivariant node representations. | $h_i,\ell,D^{(\ell)}$ | Basis for E2Former-V2 tensor features. |
| Solid spherical harmonics | SRC-0060, eq. 3 | This page | Encodes relative geometry. | $R^{(\ell)},Y_{\ell,m},\vec r$ | Input to equivariant coupling and attention. |
| Equivariant attention aggregation | SRC-0060, eq. 5 | This page | Aggregates neighbor messages with invariant weights. | $m_i,m_{ij},\alpha_{ij}$ | Core message-passing form. |
| Long-short range message split | SRC-0060, eq. 6 | This page | Separates local and longer-range neighborhoods. | $m_i^S,m_i^L,r_{\mathrm{short}},r_{\mathrm{long}}$ | Captures nonlocal effects without a fully connected graph. |
| Conservative force relation | SRC-0060, eqs. 7 and 10 | This page; [[wiki/concepts/ubio-molfm-biological-molecular-foundation-model]] | Computes forces from energy gradients. | $\hat E,\hat F_i,\vec r_i$ | Enforces energy-force consistency in Stage 2/3 training. |

## Proof map

The report does not present formal theorems. Its mathematical argument is constructive: define SO(3)-equivariant features, encode geometry with spherical harmonics, aggregate local and long-range messages with scalar attention, replace expensive dense tensor-product operations with EAAS, and compute forces conservatively from the learned energy surface. [SRC-0060, section 4.2]

## Implementation notes

- The E2Former-V2 design is explicitly hardware-aware: node-centric factorization confines edge dependence mostly to scalar attention, while a Triton on-the-fly attention kernel avoids materializing large edge tensors. [SRC-0060, section 4.2.2]
- Atom-budgeted batching packs samples by atom count rather than graph count, reducing load imbalance across GPUs when molecules vary from tens to more than a thousand atoms. [SRC-0060, section 4.3.2]
- Stage 3 uses an 8:1:1 data sampling ratio for OMol25, def2-SVP, and def2-TZVPD data; it also filters about 30% of TZVPD configurations with low force cosine similarity before force-only high-fidelity training. [SRC-0060, section 4.3.1]
- The paper reports that UBio-MolFM runs faster than compared equivariant baselines at 1K to 50K atoms, but it still runs out of memory at 100K atoms when long-range interactions are enabled. [SRC-0060, section 2.3]

## Evidence

- The extrapolation test set contains 2,616 entries across 38 trajectories, with average system sizes from about 1,290 to 1,525 atoms, larger than the approximately 1,200-atom training cap. [SRC-0060, section 2.1.1]
- UBio-MolFM (S3) reports the best force MAE for protein optimization, RNA optimization, and protein MD in Table 2, and strong relative-energy improvements for protein cases. [SRC-0060, table 2]
- Water and NaCl simulations are compared with RDF, peak-position, and coordination-number references; UBio-MolFM is reported to reproduce Na-O peak position and coordination number close to experimental values. [SRC-0060, section 2.2.1]
- Cyclosporine A simulations preserve open aqueous and closed vacuum conformations over 200 ps by the paper's hydrogen-bond diagnostics. [SRC-0060, section 2.2.2]
- RNA 1L2X simulations are reported to reproduce Mg-water and Mg-phosphate distances and flexible angle distributions more accurately than the compared Amber99 RNA OL3 and UMA-S-1p1 cases. [SRC-0060, section 2.2.3]
- Inference benchmarks report 61 steps/s at 1,000 atoms, 6.10 steps/s at 10,000 atoms, and 0.72 steps/s at 50,000 atoms on a single H100 under conservative-force evaluation. [SRC-0060, table 4]

## Limitations and Caveats

- The report is an arXiv v1 technical report, and several resources are described as planned or to be released rather than already complete. [SRC-0060, section 5]
- UBio-MolFM remains much slower than classical force fields, so validation is limited to shorter timescales for medium-sized systems. [SRC-0060, section 3.1]
- Stage 3 improves protein accuracy but reveals an observed DNA energy-difference regression, which the authors attribute to limited nucleic-acid top-down coverage. [SRC-0060, sections 2.1.2 and 3.2]
- The current top-down biological sampling is protein-focused; nucleic acids and cross-modal interfaces need broader top-down sampling before treating the model as uniformly validated across biomolecular classes. [SRC-0060, section 4.1.1]
- The 100K-atom benchmark still produces an out-of-memory result for UBio-MolFM with long-range interactions enabled. [SRC-0060, section 2.3]

## Claims

- UBio-MolFM separates static energy/force tests from downstream biomolecular MD checks, while its own limitations show why biomolecule-stratified validation remains necessary. [SRC-0060]
- [[wiki/claims/CLM-0013-energy-force-error-is-not-downstream-md-reliability]]
- [[wiki/claims/CLM-0014-dataset-scale-does-not-replace-coverage-validation]]
- [[wiki/claims/CLM-0015-molecular-datasets-have-distinct-intended-uses]]

## Questions

- [[wiki/questions/mlip-foundation-model-validation-scope]]
- [[wiki/questions/force-field-training-validation-scope]]

## Tensions

- [[wiki/tensions/TEN-0008-dataset-scale-vs-downstream-validation]]

## Citation Links

- `SRC-0042`: The report cites OMol25 as a recent large molecular dataset and uses OMol25 in training/evaluation context, matching the ingested OMol25 source. [SRC-0060]
- `SRC-0044`: The report cites SPICE as a small-molecule/drug-like molecular dataset, matching the ingested SPICE source. [SRC-0060]
- Partial citation review: the reference section is broad and includes many model and dataset sources; this pass confirmed only clear links to already ingested cluster sources. [SRC-0060]

## Links

- [[wiki/concepts/ubio-molfm-biological-molecular-foundation-model]]
- [[wiki/concepts/machine-learned-interatomic-potential-foundation-models]]
- [[wiki/concepts/machine-learning-potential-datasets]]
- [[wiki/concepts/stability-aware-mlff-training]]
- [[wiki/questions/force-field-training-validation-scope]]

## Open Questions

- How well will UBio-MolFM transfer to longer trajectories, larger systems, protein-ligand binding free energies, and protein-protein interactions? [SRC-0060, section 3.2]
- Can top-down DNA/RNA sampling remove the Stage 3 nucleic-acid regression without weakening protein gains? [SRC-0060, sections 2.1.2 and 3.2]
- How much of the reported benefit comes from UBio-Mol26 biological data, E2Former-V2 architecture, training curriculum, or their interaction? [SRC-0060, sections 2.1.2 and 4]
- What public checkpoints, inference scripts, and dataset subsets will be available after the planned release, and under what licenses? [SRC-0060, section 5]

## Mathematical gaps

- The full EAAS derivation and parity selection rules are not reproduced; the paper points to the E2Former-V2 reference for the full derivation. [SRC-0060, section 4.2.2]
- Algorithm 1 is summarized rather than transcribed because the source page captures the retrieval-relevant architecture and implementation consequences.
- Figure-level numeric details are summarized only where they materially support the paper's claims.

## Ingestion QA

### Retrieval questions checked

- What is UBio-MolFM's central contribution?
- What is in UBio-Mol26, and how is it constructed?
- What does E2Former-V2 change architecturally?
- How does the three-stage curriculum enforce energy-force consistency?
- What evidence supports the model's accuracy on large biomolecular systems?
- What downstream MD observables were tested?
- What are the main efficiency results and memory limits?
- What limitations should prevent overgeneralizing the results?
- What public resources does the report identify?

### Coverage decision

Complete at `coverage_profile: math-standard`. The wiki captures the source's central dataset, architecture, training, evaluation, implementation, equation, limitation, and release-status information. [SRC-0060]

### Known gaps

- The page does not reproduce all tables, figures, algorithm steps, or the complete derivation of EAAS.
- Public release links and license details are recorded only at the level stated in the paper; no external verification was performed during ingestion.
