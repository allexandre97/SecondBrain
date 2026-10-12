---
type: answer
status: active
created: 2026-06-30
updated: 2026-10-11
question: "How is TSS able to mix the free-energy surfaces of each window into a complete free energy surface that covers all the rungs?"
answer_status: answered
areas:
  - research
categories:
  - research/molecular-simulation/free-energy
  - research/adaptive-sampling
tags:
  - times-square-sampling
  - free-energy-estimation
  - windowing
  - math-heavy
related:
  - "[[wiki/concepts/times-square-sampling]]"
  - "[[wiki/concepts/tss-implementation-patterns]]"
  - "[[wiki/concepts/free-energy-estimation]]"
  - "[[wiki/questions/tss-generalization-scope]]"
sources:
  - SRC-0005
  - SRC-0006
sensitivity: public
encryption: none
wiki_pages_used:
  - "[[index]]"
  - "[[wiki/sources/SRC-0005-times-square-sampling-free-energy]]"
  - "[[wiki/sources/SRC-0006-times-square-sampling-supplement]]"
  - "[[wiki/concepts/times-square-sampling]]"
  - "[[wiki/concepts/tss-implementation-patterns]]"
  - "[[wiki/concepts/free-energy-estimation]]"
  - "[[wiki/questions/tss-generalization-scope]]"
raw_sources_consulted:
  - raw/sources/SRC-0006-times-square-sampling-supplement.pdf
wiki_pages_updated:
  - "[[wiki/concepts/tss-implementation-patterns]]"
scope: timeless
---

# How TSS Stitches Window Free-Energy Surfaces

## Short answer

TSS can mix per-window free-energy surfaces because overlapping windows turn the global problem into an additive-offset alignment problem. Each local window estimates a surface $F_{j;k}$ for rungs $k \in W_j$, but that local surface is only defined up to a window-specific constant. TSS estimates how much statistical mass each window contributes, then solves for offsets $f_j$ that put all local surfaces into one gauge. Once the offsets are known, the global free energy at rung $k$ is a weighted average of all offset-corrected local estimates that include $k$. [SRC-0005, section 3.1] [SRC-0006, sections 6.2 and 7.2]

The general idea is not specific to TSS: any method that produces overlapping local estimates of a potential, free energy, log normalizer, or log density ratio can be stitched this way if the overlaps provide enough connectivity to identify relative offsets.

## Detailed answer

Suppose the rungs are $k=1,\ldots,K$ and the windows are $W_j \subseteq \{1,\ldots,K\}$. In window $j$, TSS estimates local quantities

$$
F_{j;k}, \qquad k \in W_j.
$$

These are local free-energy estimates. They cannot be pasted together directly, because free energies are identifiable only up to an additive constant. Window $j$ may estimate the right shape over $W_j$, while window $i$ estimates the right shape over $W_i$, but their vertical origins can differ. Mathematically, the target relation is approximately

$$
F_{j;k} \approx F_k^* + c_j,
$$

where $F_k^*$ is the global free energy at rung $k$ and $c_j$ is a window-specific gauge constant. The stitching problem is therefore to infer the constants $c_j$ or offsets $f_j$ from overlapping windows. [SRC-0006, section 6.2]

TSS first determines how much each window should contribute. In the finite-visit-control construction, the window probabilities $p_j$ come from an eigenvector equation over the overlap graph:

$$
Qp=p,
$$

where the transition weights are built from the overlap between windows and the local densities and tilts. In the supplement's implementation notation,

$$
q_{ij}=\frac{1}{2}\frac{\sum_{k \in W_i \cap W_j}\gamma_{j;k}o_{j;k}}{\sum_{k \in W_j}\gamma_{j;k}o_{j;k}}.
$$

The point is that a window contributes to the global estimate in proportion to its stationary weight in the window-overlap process. [SRC-0006, eqs. 6.9, 7.23-7.25]

TSS then distinguishes two global reconstructions. The first is for sampling: the global visit-control free energies $F_k^\circ$. These use the tilts $o_{j;k}$ and a finite visit-control strength $\eta$. They solve a convex optimization problem or, equivalently, a fixed-point problem in window offsets $f_j$. These estimates drive the sampler, but they are noisy because the tilts are counting-based. [SRC-0006, sections 6.2.1 and 7.2.2]

The second reconstruction is for reporting the final free-energy surface. Near convergence, TSS assumes the tilts have approached $1$ and takes the $\eta \to \infty$ reporting limit. In that limit, the reported rung density is

$$
\gamma_k^{TSS}=\sum_{j \in win(k)}p_j\gamma_{j;k},
$$

where $win(k)$ is the set of windows containing rung $k$. [SRC-0006, eqs. 6.21-6.22]

Then the reported global free energy is

$$
F_k^{TSS}
=\frac{1}{\gamma_k^{TSS}}
\sum_{j \in win(k)}p_j\gamma_{j;k}\left(F_{j;k}-f_j^{TSS}\right).
$$

This equation is the actual mixing formula. For each rung $k$, it averages the free-energy estimates from every window that contains $k$, after subtracting that window's offset. The weights are $p_j\gamma_{j;k}$, normalized by $\gamma_k^{TSS}$. [SRC-0006, eq. 6.23]

The remaining question is how the offsets $f_j^{TSS}$ are chosen. In the reporting limit, they solve a linear system:

$$
\sum_{j=1}^J(\delta_{ij}-t_{ij})f_j^{TSS}
=
\sum_{k:\lambda_k \in W_i}\gamma_{i;k}F_{i;k}
-
\sum_{k:\lambda_k \in W_i}\sum_{j \in win(k)}
\frac{p_j\gamma_{j;k}\gamma_{i;k}}{\gamma_k^{TSS}}F_{j;k},
$$

with

$$
t_{ij}
=
\sum_{k \in W_i \cap W_j}
\gamma_{i;k}\frac{p_j\gamma_{j;k}}{\gamma_k^{TSS}}.
$$

The system is singular because adding the same constant to all offsets does not change any free-energy difference. TSS fixes this gauge by replacing one equation with a constraint such as

$$
\sum_j p_j f_j^{TSS}=0.
$$

After that, the offsets are determined, and the formula for $F_k^{TSS}$ gives one complete free-energy surface over all rungs connected by the window-overlap graph. [SRC-0006, eqs. 6.24-6.25]

## General form

The abstract version is simple. Let local model $j$ provide estimates $a_{j;k}$ for items $k \in W_j$, with

$$
a_{j;k}=A_k+c_j+\epsilon_{j;k}.
$$

Here $A_k$ is the unknown global surface, $c_j$ is a local additive offset, and $\epsilon_{j;k}$ is estimation noise. Choose nonnegative weights $w_{j;k}$ and solve

$$
\min_{A,c}\sum_j\sum_{k \in W_j}w_{j;k}\left(a_{j;k}-c_j-A_k\right)^2
$$

subject to a gauge condition such as $\sum_j \alpha_j c_j=0$ or $A_1=0$. If the bipartite graph connecting windows to rungs is connected, the global surface is identifiable up to one additive constant. If the graph has disconnected components, each component has its own arbitrary offset.

TSS's reported-free-energy construction is a structured version of this general offset-alignment problem. The weights are not arbitrary: they come from the window stationary probabilities $p_j$ and local rung densities $\gamma_{j;k}$. The final estimate is therefore not just an unweighted overlap average, but a statistically weighted gauge-aligned average. [SRC-0006, sections 6.2.2 and 7.2.3]

## Can this extend beyond TSS?

Yes, the stitching principle extends beyond TSS. What is TSS-specific is how the local estimates $F_{j;k}$, window weights $p_j$, local densities $\gamma_{j;k}$, and visit-control tilts $o_{j;k}$ are generated. The mathematical operation of combining local surfaces is more general:

- local estimates must overlap;
- local estimates must differ mainly by additive gauges, not incompatible shapes;
- the overlap graph must be connected;
- weights should reflect estimator reliability, sampling mass, or inverse variance;
- one global gauge constraint is needed because absolute free energies are not identifiable.

This makes the same idea applicable to umbrella sampling windows, thermodynamic-integration patches, local log-normalizer estimates, manifold charts, or any multi-window estimator whose outputs are local log quantities. TSS contributes a particular adaptive sampling and weighting mechanism, plus a careful separation between noisy visit-control free energies used for sampling and lower-noise reported free energies used as output. [SRC-0005, section 3.1] [SRC-0006, sections 6.2 and 7.2]

## Key equations

Window stationary probabilities:

$$
Qp=p.
$$

Reported rung density:

$$
\gamma_k^{TSS}=\sum_{j \in win(k)}p_j\gamma_{j;k}.
$$

Reported global free energy:

$$
F_k^{TSS}
=\frac{1}{\gamma_k^{TSS}}
\sum_{j \in win(k)}p_j\gamma_{j;k}\left(F_{j;k}-f_j^{TSS}\right).
$$

Gauge constraint:

$$
\sum_j p_j f_j^{TSS}=0.
$$

## Sources used

- [[wiki/sources/SRC-0005-times-square-sampling-free-energy]]
- [[wiki/sources/SRC-0006-times-square-sampling-supplement]]

## Wiki pages used

- [[index]]
- [[wiki/concepts/times-square-sampling]]
- [[wiki/concepts/tss-implementation-patterns]]
- [[wiki/concepts/free-energy-estimation]]
- [[wiki/questions/tss-generalization-scope]]

## Wiki updates made

- Updated [[wiki/concepts/tss-implementation-patterns]] with a focused window-stitching interpretation.

## Remaining gaps

- This answer gives the mathematical structure of the stitching step, not a source-code-level walkthrough of the D. E. Shaw implementation.
- The extension beyond TSS is a generalization from the equations, not a validation claim that every multi-window method will behave well with TSS-style weights.
