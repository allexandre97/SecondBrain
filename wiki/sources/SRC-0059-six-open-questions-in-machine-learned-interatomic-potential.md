---
type: source
status: active
created: 2026-06-30
updated: 2026-06-30
source_id: SRC-0059
display_title: "Six Open Questions in Machine-Learned Interatomic Potential Foundation Models"
short_title: "Six Open Questions for MLIP Foundation Models"
aliases:
  - "SRC-0059"
  - "Six Open Questions for MLIPs"
  - "Six Open Questions in Machine-Learned Interatomic Potential Foundation Models"
  - "MLIP Foundation Models"
source_path: raw/sources/SRC-0059-six-open-questions-in-machine-learned-interatomic-potential.pdf
imported_path: raw/sources/SRC-0059-six-open-questions-in-machine-learned-interatomic-potential.pdf
original_filename: "2606.07327v2.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 50e76532cdc5617118160f72507ab646b025a3ab264d2287aebf645f2820c5a5
authors:
  - "Isabel Creed"
  - "Tim Rein"
  - "Ingvars Vitenburgs"
  - "Wojciech G. Stark"
  - "Viktor Ellingsson"
  - "Ahmed Y. Ismail"
  - "Guangyu Liu"
  - "Yuchen Lou"
  - "Bradley A. A. Martin"
  - "Cyprien Bone"
  - "Matthew A. H. Walker"
  - "Mueen Taj"
  - "Shirui Wang"
  - "Kelvin Wong"
  - "Ruiqi Wu"
  - "Prakriti Kayastha"
  - "Bingqing Cheng"
  - "Aditi Krishnapriyan"
  - "Michele Ceriotti"
  - "Marcel F. Langer"
  - "Jarvist Moore Frost"
  - "Alex M. Ganose"
  - "Venkat Kapil"
  - "Keith T. Butler"
author_entities: []
year: 2026
venue: "arXiv"
doi:
arxiv: "2606.07327"
metadata_review_status: reviewed
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/machine-learning/molecular-modeling
  - research/machine-learning/scientific-modeling
  - research/molecular-simulation/datasets
  - research/molecular-simulation/molecular-dynamics
  - research/experimental-benchmarking
  - research/high-performance-computing
tags:
  - machine-learned-interatomic-potentials
  - foundation-models
  - mlip
  - equivariance
  - long-range-interactions
  - benchmarking
related:
  - "[[wiki/concepts/machine-learned-interatomic-potential-foundation-models]]"
  - "[[wiki/concepts/machine-learning-potential-datasets]]"
  - "[[wiki/concepts/automated-force-field-training]]"
  - "[[wiki/concepts/stability-aware-mlff-training]]"
sources:
  - SRC-0059
cites_sources:
  - SRC-0042
citation_match_status: partial
cqt_review_status: linked
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: math-standard
---

# Six Open Questions in Machine-Learned Interatomic Potential Foundation Models

Source ID: `SRC-0059`

## Raw source

- Repository path: `raw/sources/SRC-0059-six-open-questions-in-machine-learned-interatomic-potential.pdf`
- Open raw source: [raw/sources/SRC-0059-six-open-questions-in-machine-learned-interatomic-potential.pdf](../../raw/sources/SRC-0059-six-open-questions-in-machine-learned-interatomic-potential.pdf)

## Summary

This arXiv v2 paper surveys foundation-model machine-learned interatomic potentials (MLIPs) through six open questions: what counts as an atomistic foundation model, whether progress needs more data, better data, or better models, whether MLIPs can handle long-range interactions, whether they can discover new physics, whether they can scale to useful simulations, and how they should be benchmarked. [SRC-0059]

The paper adapts a foundation-model taxonomy of expressivity, scalability, memorization, multimodality, and compositionality to atomistic simulation. It argues that MLIP foundation models are foundational for simulating chemistry and materials, but they are not direct analogues of very large language foundation models. [SRC-0059, section 1]

## Key Points

- Foundation MLIPs are framed as transferable, pretrained interatomic potentials intended to support many downstream simulations with minimal task-specific engineering. [SRC-0059, section 1]
- The paper treats expressivity, scalability, memorization, multimodality, and compositionality as criteria for deciding whether an atomistic model is meaningfully foundational. [SRC-0059, section 1]
- Progress is not presented as a simple choice between data scale and physical inductive bias; the paper argues that model complexity, dataset diversity, data fidelity, optimization, and infrastructure must scale together. [SRC-0059, section 2]
- Long-range interactions are not just electrostatics; the paper distinguishes physical tails, correlation lengths, global responses, and graph-theoretic influence as different senses of long range. [SRC-0059, section 3]
- MLIPs may enable access to regimes, system sizes, and collective phenomena that were previously inaccessible, but most current successes are closer to sophisticated interpolation over broad data than autonomous discovery of new physical laws. [SRC-0059, section 4]
- Scaling useful simulations requires inference efficiency, hardware-aware implementations, distillation, and training scalability in addition to predictive accuracy. [SRC-0059, section 5]
- Benchmarking should balance pragmatic task tests with representational diagnostics, and should document limitations to avoid Goodhart's Law and the McNamara fallacy. [SRC-0059, section 6]

## Mathematical structure

The paper is primarily a perspective/review, not a derivation paper. Its mathematical content is used to define foundation-model scaling, long-range interaction notions, and symmetry constraints for equivariant MLIPs. [SRC-0059]

Scaling-law schematic: [SRC-0059, eq. 1]

$$
L(N) \propto N^{-\alpha}, \qquad
L(P) \propto P^{-\beta}, \qquad
L(C) \propto C^{-\gamma}.
$$

Physics-based long-range pair tail: [SRC-0059, eq. 2]

$$
V(r) \propto r^{-\alpha}.
$$

Equivariance condition: [SRC-0059, eq. 3]

$$
f(\rho_X(g)x)=\rho_Y(g)f(x).
$$

Spherical-harmonic transformation: [SRC-0059, eq. 4]

$$
Y_m^\ell(R\hat{r}) =
\sum_{m'=-\ell}^{\ell}D_{m m'}^{(\ell)}(R)Y_{m'}^\ell(\hat{r}).
$$

Clebsch-Gordan coupling map: [SRC-0059, eq. 5]

$$
\left(a^{\ell_1}\otimes b^{\ell_2}\right)_m^\ell
=
\sum_{m_1,m_2}
C_{\ell_1 m_1,\ell_2 m_2}^{\ell m}
a_{m_1}^{\ell_1}b_{m_2}^{\ell_2}.
$$

## Variable glossary

- $L$: model loss or error metric in a scaling-law relation. [SRC-0059, eq. 1]
- $N$: dataset size. [SRC-0059, eq. 1]
- $P$: model parameter count. [SRC-0059, eq. 1]
- $C$: compute. [SRC-0059, eq. 1]
- $\alpha$, $\beta$, $\gamma$: scaling exponents for data, parameters, and compute. [SRC-0059, eq. 1]
- $V(r)$: distance-dependent pair-potential tail. [SRC-0059, eq. 2]
- $r$: separation distance. [SRC-0059, eq. 2]
- $d$: spatial dimension used when discussing strong or weak long-range interactions. [SRC-0059, section 3.1.1]
- $G$: symmetry group, typically $E(3)$ for atomistic modeling. [SRC-0059, section 5.1]
- $\rho_X$, $\rho_Y$: group representations acting on input and output spaces. [SRC-0059, eq. 3]
- $D^{(\ell)}(R)$: Wigner D-matrix for rotation $R$. [SRC-0059, eq. 4]
- $C_{\ell_1 m_1,\ell_2 m_2}^{\ell m}$: Clebsch-Gordan coefficient. [SRC-0059, eq. 5]

## Equation inventory

| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |
| Scaling-law schematic | SRC-0059, eq. 1 | This page; [[wiki/concepts/machine-learned-interatomic-potential-foundation-models]] | Relates error to data, parameters, and compute. | $L,N,P,C,\alpha,\beta,\gamma$ | Frames foundation-model scaling claims. |
| Long-range pair tail | SRC-0059, eq. 2 | This page; [[wiki/concepts/machine-learned-interatomic-potential-foundation-models]] | Defines one physical sense of long-range interaction. | $V(r),r,\alpha,d$ | Helps distinguish electrostatic, dispersion, and other tails. |
| Equivariance condition | SRC-0059, eq. 3 | This page; [[wiki/concepts/machine-learned-interatomic-potential-foundation-models]] | Defines group-equivariant maps. | $f,\rho_X,\rho_Y,g,x$ | Explains symmetry-preserving MLIP architecture constraints. |
| Spherical-harmonic transformation | SRC-0059, eq. 4 | This page | Shows SO(3) feature transformation. | $Y_m^\ell,D^{(\ell)}(R)$ | Used by equivariant tensor-feature models. |
| Clebsch-Gordan coupling | SRC-0059, eq. 5 | This page | Defines equivariant tensor-product coupling. | $a,b,C_{\ell_1m_1,\ell_2m_2}^{\ell m}$ | Explains compute/memory cost of equivariant layers. |

## Proof map

The paper does not present formal theorem proofs. Its argument is organized as a conceptual map: first define atomistic foundation-model criteria, then use those criteria to discuss data/model scaling, long-range physics, scientific discovery, simulation efficiency, and benchmarking. [SRC-0059]

## Implementation notes

- Foundation MLIPs need to be evaluated not only by energy/force accuracy but by downstream simulation stability, long-range behavior, inference cost, training cost, and task-specific benchmarks. [SRC-0059, sections 3, 5, and 6]
- Distillation is presented as a practical route to compress large foundation MLIPs into smaller specialized models that can run larger simulations with modest loss of accuracy. [SRC-0059, section 5.2]
- The paper notes that hardware-specific kernels and performance-portable frameworks matter because large equivariant models can be memory- and throughput-limited. [SRC-0059, section 5.3]

## Evidence

- The paper draws examples from M3GNet, CHGNet, MACE-MP, Matbench Discovery, OMat24, OMol25, OC20M, MatPES, MLIP-Arena, and other recent MLIP models or benchmarks to support its claims about data, scaling, long-range interactions, and benchmarking. [SRC-0059]
- It presents Matbench Discovery as a dominant but increasingly saturated benchmark whose single composite metric should not be treated as a complete answer to model quality. [SRC-0059, section 6]
- It points to distillation studies reporting large inference speedups for specialized student MLIPs while retaining near-teacher force accuracy. [SRC-0059, section 5.2]

## Limitations and Caveats

- The paper is explicitly a perspective built around selected open questions, not a systematic benchmark or exhaustive review of every MLIP foundation model. [SRC-0059]
- Several claims are intentionally framed as unsettled research questions, including whether physical inductive biases remain advantageous at extreme scale and whether a unified theory of long-range MLIPs will emerge. [SRC-0059, sections 2 and 3]
- It cautions that present-day MLIP successes mostly reflect broad interpolation and access to new regimes, not proof that MLIPs autonomously discover fundamentally new physical laws. [SRC-0059, section 4]
- It argues that no single benchmark should be overinterpreted because benchmark pressure can distort optimization targets and hide hard-to-measure failures. [SRC-0059, section 6]

## Claims

- [[wiki/claims/CLM-0013-energy-force-error-is-not-downstream-md-reliability]]
- [[wiki/claims/CLM-0014-dataset-scale-does-not-replace-coverage-validation]]

## Questions

- [[wiki/questions/mlip-foundation-model-validation-scope]]

## Tensions

- [[wiki/tensions/TEN-0008-dataset-scale-vs-downstream-validation]]

## Citation Links

- `SRC-0042`: The paper discusses and cites the Open Molecules 2025 dataset as a large molecular MLIP dataset, matching the ingested OMol25 source. [SRC-0059]
- Partial citation review: SRC-0059 is a broad perspective/review with many model, dataset, and benchmark references. The targeted pass recorded clear cluster-relevant links but did not attempt exhaustive bibliography normalization. [SRC-0059]

## Links

- [[wiki/concepts/machine-learned-interatomic-potential-foundation-models]]
- [[wiki/concepts/machine-learning-potential-datasets]]
- [[wiki/concepts/automated-force-field-training]]
- [[wiki/concepts/stability-aware-mlff-training]]
- [[wiki/concepts/garnet-force-field]]

## Open Questions

- Which criteria are actually necessary for an atomistic model to count as a foundation model? [SRC-0059, section 1]
- At what scale do learned symmetries, global attention, or transformer-style architectures outperform explicit physical inductive biases for MLIPs? [SRC-0059, sections 2 and 5]
- Can a single transferable long-range MLIP approach cover electrostatics, dispersion, screening, electronic delocalization, and charged defects? [SRC-0059, section 3]
- What benchmark mix best predicts real downstream simulation usefulness without collapsing into a single overoptimized metric? [SRC-0059, section 6]

## Mathematical gaps

- Detailed formulas for every architecture and benchmark discussed in the review are not transcribed; the source page captures only the equations central to the paper's argument structure.
- Figures are summarized conceptually rather than reproduced.

## Ingestion QA

### Retrieval questions checked

- What is the central contribution of the paper?
- How does the paper define or frame an atomistic foundation-model MLIP?
- What six open questions does the paper organize around?
- What does the paper say about more data versus better data versus better models?
- How does the paper define long-range interactions in MLIPs?
- What does the paper claim about MLIPs discovering new physics?
- What practical bottlenecks limit scaling MLIPs to useful simulations?
- What benchmarking caveats does the paper emphasize?

### Coverage decision

Complete at `coverage_profile: math-standard`. The wiki captures the paper's six-question structure, core definitions, central equations, implementation implications, and major caveats. [SRC-0059]

### Known gaps

- The source page does not enumerate every model, benchmark, or citation discussed in the 34-page review.
- The exact visual content of figures is not reproduced; only the role of each figure in the argument is summarized.
