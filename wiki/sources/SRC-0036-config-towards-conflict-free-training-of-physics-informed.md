---
type: source
status: active
created: 2026-06-30
updated: 2026-07-01
source_id: SRC-0036
display_title: "ConFIG: Towards Conflict-Free Training of Physics-Informed Neural Networks"
short_title: "ConFIG"
aliases:
  - "SRC-0036"
  - "ConFIG"
  - "ConFIG: Towards Conflict-Free Training of Physics-Informed Neural Networks"
source_path: raw/sources/SRC-0036-config-towards-conflict-free-training-of-physics-informed.pdf
original_filename: "ICLR-2025-config-towards-conflict-free-training-of-physics-informed-neural-networks-Paper-Conference.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 19693055bc10cf5980c36c62990fbffc37a3585daaddf987441ebedae73625b9
authors:
  - "Qiang Liu"
  - "Mengyu Chu"
  - "Nils Thuerey"
author_entities: []
year: 2025
venue: "ICLR"
doi:
arxiv:
metadata_review_status: reviewed
citation_match_status: reviewed
cqt_review_status: source-local
cites_sources: []
areas:
  - research
categories:
  - research/machine-learning/scientific-modeling
tags:
  - PINNs
  - multi-objective-optimization
  - gradient-conflict
  - ConFIG
related:
  - "[[wiki/concepts/conflict-free-pinn-training]]"
sources:
  - SRC-0036
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: math-standard
---

# ConFIG: Towards Conflict-Free Training of Physics-Informed Neural Networks

Source ID: `SRC-0036`

## Raw source

- Repository path: `raw/sources/SRC-0036-config-towards-conflict-free-training-of-physics-informed.pdf`
- Open raw source: [raw/sources/SRC-0036-config-towards-conflict-free-training-of-physics-informed.pdf](../../raw/sources/SRC-0036-config-towards-conflict-free-training-of-physics-informed.pdf)

## Summary

ConFIG proposes a gradient-aggregation method for multi-loss training, with emphasis on physics-informed neural networks. It constructs a final update direction whose dot product with each loss-specific gradient is positive, while equalizing projection lengths so that loss terms decrease at a consistent rate. [SRC-0036]

## Key Points

- PINNs combine losses for PDE residuals, initial conditions, and boundary conditions; these gradients can have different magnitudes, convergence rates, and directions. [SRC-0036, section 1]
- ConFIG treats a loss-specific gradient as conflicting with an update if the dot product is negative. [SRC-0036, section 3.1]
- The method uses the pseudoinverse of the normalized gradient matrix to find a conflict-free direction, then scales the update based on the projection lengths of loss-specific gradients. [SRC-0036, section 3.1]
- M-ConFIG reduces cost by maintaining per-loss momentum and updating only one loss-specific gradient per iteration, avoiding a full backpropagation for every loss at every step. [SRC-0036, section 3.2]
- The paper reports strong results on challenging PINN PDE cases and a CelebA multi-task benchmark, but notes that M-ConFIG can degrade as the number of loss terms increases. [SRC-0036, sections 4-5]

## Key equations

**Conflict-free condition [SRC-0036, section 3.1]:**

$$
g_i^\top g_c > 0
$$

for every loss-specific gradient $g_i$ and final update $g_c$.

**ConFIG update, source Eqs. (2)-(3) [SRC-0036]:**

$$
g_{\mathrm{ConFIG}} =
G(g_1,\ldots,g_m) :=
\left(\sum_{i=1}^{m} g_i^\top g_u\right) g_u
$$

$$
g_u =
U\left([U(g_1),U(g_2),\ldots,U(g_m)]^{-\top}\mathbf{1}_m\right)
$$

where $U(g)=g/(|g|+\epsilon)$ and $[\,]^{-\top}$ denotes a pseudoinverse of the transposed normalized gradient matrix. [SRC-0036]

## Proof map

- The convex proof assumes differentiable convex objectives and a Lipschitz-continuous summed gradient. [SRC-0036, theorem 1]
- The descent argument uses the two defining ConFIG properties: equal positive projection on each loss-specific gradient and update magnitude equal to the sum of projection lengths. [SRC-0036, appendix A.1]
- Under a small enough step size, the total loss is non-increasing until the ConFIG direction vanishes or an optimum/stationary point is reached. [SRC-0036, theorem 1 and theorem 2]

## Equation inventory

| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |
| Projection ratio | Eq. (1) | Key Points | Defines equal projection-rate motivation | $g_c$, $g_i$, $\hat w_i$ | Explains rate balancing |
| ConFIG update | Eqs. (2)-(3) | Key equations | Aggregates loss gradients into conflict-free update | $g_i$, $g_u$, $U$, $\mathbf{1}_m$ | Core update rule |
| Two-loss form | Eqs. (4)-(5) | Mathematical gaps | Avoids pseudoinverse for two losses | $g_1$, $g_2$ | Useful special-case implementation |
| M-ConFIG | Algorithm 1 | Key Points | Momentum approximation for lower cost | per-loss momenta | Practical PINN training variant |

## Limitations

- M-ConFIG performance can degrade as the number of loss terms grows, because each momentum is updated less frequently. [SRC-0036, limitations]
- Memory consumption grows with parameter count and number of loss terms because per-gradient momentum must be stored. [SRC-0036, limitations]
- Removing loss-gradient conflict does not solve all PINN training challenges, including chaotic problems or architectural deficiencies. [SRC-0036, limitations]

## Mathematical gaps

- The wiki does not reproduce the full non-convex proof or all appendix algorithms.
- Experimental tables are summarized rather than copied.

## Claims

- Source-local note: ConFIG is in the requested migration scope but is not a bioimage/STED or filament-segmentation source, so no first-class fiber-analysis claim was promoted from it. [SRC-0036]

## Citation Links

- Targeted citation review found no new confirmed `cites_sources` links to add for currently ingested sources. [SRC-0036]

## Links

- [[wiki/concepts/conflict-free-pinn-training]]

## Ingestion QA

### Retrieval questions checked

- What training problem does ConFIG address?
- How is gradient conflict defined?
- What does the ConFIG update guarantee?
- How does M-ConFIG reduce computational cost?
- What convergence claims are made?
- What limitations remain for many losses and hard PINN cases?

### Coverage decision

Complete at `coverage_profile: math-standard`. The source page records the core update, proof structure, algorithmic role, evidence scope, and limitations.

### Known gaps

- Full algorithmic variants and all PDE benchmark details remain in the raw source.
