---
type: source
status: active
created: 2026-06-30
updated: 2026-06-30
source_id: SRC-0052
display_title: "LINCS: A Linear Constraint Solver for Molecular Simulations"
short_title: "LINCS Constraint Solver"
authors:
  - Berk Hess
  - Henk Bekker
  - Herman J. C. Berendsen
  - Johannes G. E. M. Fraaije
year: 1997
venue: "Journal of Computational Chemistry"
aliases:
  - "SRC-0052"
  - "LINCS Constraint Solver"
  - "LINCS: A Linear Constraint Solver for Molecular Simulations"
source_path: raw/sources/SRC-0052-lincs-a-linear-constraint-solver-for-molecular-simulations.pdf
original_filename: "J Comput Chem - 1998 - Hess - LINCS A linear constraint solver for molecular simulations.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 6f0a0dffd46a0835fd880c8a198db1694758e3df6ed988a980643e56bd8be558
areas:
  - research
categories:
  - research/molecular-simulation/molecular-dynamics
tags:
  - constraints
  - LINCS
  - SHAKE
  - molecular-dynamics
related:
  - "[[wiki/concepts/molecular-dynamics-constraint-solvers]]"
sources:
  - SRC-0052
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: math-standard
metadata_review_status: reviewed
citation_match_status: partial
cqt_review_status: linked
---

# LINCS: A Linear Constraint Solver for Molecular Simulations

Source ID: `SRC-0052`

## Raw source

- Repository path: `raw/sources/SRC-0052-lincs-a-linear-constraint-solver-for-molecular-simulations.pdf`
- Open raw source: [raw/sources/SRC-0052-lincs-a-linear-constraint-solver-for-molecular-simulations.pdf](../../raw/sources/SRC-0052-lincs-a-linear-constraint-solver-for-molecular-simulations.pdf)

## Summary

Hess et al. introduce LINCS, a linear constraint solver for molecular simulations with bond constraints. LINCS resets constraints after an unconstrained update, uses a sparse constraint coupling matrix, and is reported as three to four times faster than SHAKE at the same accuracy. [SRC-0052]

## Key Points

- LINCS solves the same constraint-resetting problem as SHAKE but uses a noniterative linearized correction plus optional rotational correction. [SRC-0052]
- The sparse constraint coupling matrix is inverted with a power series, exploiting the local nature of constraint coupling. [SRC-0052]
- The method is designed for leap-frog or Verlet-type MD and is straightforward to parallelize when constraint coupling is local. [SRC-0052]
- The paper reports good stability and accuracy for protein and peptide tests. [SRC-0052]

## Key equations

Constraint equations: [SRC-0052]

$$
g_h(r) = 0.
$$

Constraint gradient matrix:

$$
B_{hi} = \frac{\partial g_h}{\partial r_i}.
$$

Constrained equation of motion form: [SRC-0052, eq. 5]

$$
-M\frac{d^2r}{dt^2} + B^T\lambda + f = 0.
$$

## Variable glossary

- $g_h$: constraint equation $h$. [SRC-0052]
- $B$: matrix of constraint directions/gradients. [SRC-0052]
- $M$: mass matrix. [SRC-0052]
- $\lambda$: Lagrange multipliers for constraints. [SRC-0052]
- $f$: force vector. [SRC-0052]

## Equation inventory

| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |
| Constraint equation | Section theory | Key equations | Defines holonomic constraints | $g_h(r)$ | Baseline constrained dynamics |
| Constraint gradient | Eq. (4) | Key equations | Defines constraint direction matrix | $B$, $g_h$, $r_i$ | Core LINCS matrix |
| Constrained motion | Eq. (5) | Key equations | Includes constraint forces with multipliers | $M$, $B$, $\lambda$, $f$ | Derivation of correction |
| Power-series inverse | Algorithm section | Mathematical gaps | Approximates sparse coupling inverse | constraint coupling matrix | Main algorithmic approximation |

## Limitations

- The wiki does not reproduce the full LINCS pseudocode or power-series derivation; implementation should consult the source. [SRC-0052]
- LINCS convergence depends on constraint coupling topology and expansion order; highly coupled constraints require care. [SRC-0052]

## Mathematical gaps

- Full projection/correction formulas, rotation correction, and pseudocode are summarized rather than reproduced.

## Links

- [[wiki/concepts/molecular-dynamics-constraint-solvers]]

## Claims

- [[wiki/claims/CLM-0025-constraints-and-long-range-electrostatics-change-pressure-tensor-accounting]]

## Questions

- [[wiki/questions/md-virial-pressure-implementation-for-autodiff-and-many-body-potentials]]

## Tensions

- [[wiki/tensions/TEN-0013-analytic-constraint-virials-vs-autodiff-energy-gradients]]

## Citation links

- Citation review status: partial. Bibliographic metadata was checked from the PDF first page; this page is a cited local target of SRC-0054.

## Ingestion QA

### Retrieval questions checked

- What problem does LINCS solve?
- How does it differ from SHAKE?
- Which matrix is central to the method?
- Why is it parallelizable?
- What speed claim is made?
- What implementation details remain in the raw source?

### Coverage decision

Complete at `coverage_profile: math-standard`. The page captures the constraint equations, main algorithmic idea, evidence, and gaps.
