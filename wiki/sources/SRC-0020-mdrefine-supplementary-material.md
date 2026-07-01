---
type: source
status: active
created: 2026-06-30
updated: 2026-06-30
source_id: SRC-0020
display_title: "Supplementary Material for MDRefine"
short_title: "MDRefine Supplement"
aliases:
  - "SRC-0020"
  - "MDRefine Supplement"
  - "Supplementary Material for MDRefine"
source_path: raw/sources/SRC-0020-mdrefine-supplementary-material.pdf
imported_path: raw/sources/SRC-0020-mdrefine-supplementary-material.pdf
original_filename: "mdrefine_supplementary.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 439168947f23e54b3dfe9cab2d5b565b431152e28d98f2a554a8788b3504a5e8
authors:
  - "Ivan Gilardoni"
  - "Valerio Piomponi"
  - "Thorben Frohlking"
  - "Giovanni Bussi"
author_entities: []
year: 2025
venue: "Journal of Chemical Physics"
doi: "10.1063/5.0256841"
arxiv:
metadata_review_status: reviewed
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/molecular-simulation/free-energy
tags:
  - supporting-information
  - mdrefine
  - automatic-differentiation
  - hyperparameter-optimization
  - math-heavy
related:
  - "[[wiki/sources/SRC-0019-mdrefine-python-package-refining-md-trajectories]]"
  - "[[wiki/concepts/ensemble-and-force-field-refinement]]"
sources:
  - SRC-0020
cites_sources: []
citation_match_status: reviewed
cqt_review_status: source-local
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: math-standard
---

# Supplementary Material for MDRefine

Source ID: `SRC-0020`

## Raw source

- Repository path: `raw/sources/SRC-0020-mdrefine-supplementary-material.pdf`
- Open raw source: [raw/sources/SRC-0020-mdrefine-supplementary-material.pdf](../../raw/sources/SRC-0020-mdrefine-supplementary-material.pdf)
## Source bundle

Supporting material for SRC-0019. [SRC-0019] [SRC-0020]

## Summary

This supplement gives derivative formulas, implementation notes, hyperparameter-gradient logic, Kish-size diagnostics, and additional validation figures for MDRefine. [SRC-0020]

The most reusable mathematical result is the use of stationarity of the inner $\lambda^*(\mu)$ minimization to avoid differentiating through the full optimizer when computing outer gradients. [SRC-0020]

## Key Points

- The supplement defines $\mu=(\phi,\theta)$ for force-field and forward-model parameters. [SRC-0020]
- Because $\lambda^*(\mu)$ minimizes the inner objective, the derivative of $L_1(\mu)=L(\lambda^*(\mu),\mu)$ drops the $\partial \lambda^*/\partial\mu$ term at first order. [SRC-0020]
- Hyperparameter derivatives of validation $\chi^2$ are computed by combining derivatives of $\chi^2$ with derivatives of optimal parameters with respect to $\alpha,\beta,\gamma$. [SRC-0020]
- Hessians of the inner and outer minimizations enter the implicit differentiation formulas. [SRC-0020]
- Boundary-active $\lambda$ variables are treated as locally fixed at the boundary for derivative purposes. [SRC-0020]
- Kish size ratio is used to monitor how concentrated the reweighted ensemble has become. [SRC-0020]

## Key equations

Outer loss with explicit inner optimum:

$$
L_1(\mu)=L(\lambda^*(\mu),\mu)
=-\alpha\Gamma(\lambda^*(\mu);\mu)+\beta R_1(\phi)+\gamma R_2(\theta).
$$

[SRC-0020]

Stationarity simplification:

$$
\frac{\partial L_1}{\partial \mu_j}
=
\left.
\frac{\partial L}{\partial \mu_j}
\right|_{\lambda^*(\mu)}.
$$

[SRC-0020]

Inner optimum:

$$
\lambda^*(\mu;\alpha)=\arg\min_{\lambda}\Gamma(\lambda;\mu,\alpha).
$$

[SRC-0020]

Outer optimum:

$$
\mu^*(\alpha,\beta,\gamma)=
\arg\min_{\mu}L_1(\mu;\alpha,\beta,\gamma).
$$

[SRC-0020]

Kish effective size ratio:

$$
\mathrm{KSR}=
\frac{(\sum_i w_i)^2}{N\sum_i w_i^2}.
$$

[SRC-0020]

## Equation inventory

| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |
| $L_1(\mu)$ | SRC-0020 S1 | This page; [[wiki/concepts/ensemble-and-force-field-refinement]] | Defines outer loss after inner minimization. | $\mu$, $\lambda^*$, $\alpha,\beta,\gamma$ | Outer optimizer. |
| Stationarity gradient | SRC-0020 S1 | This page | Avoids differentiating through inner optimizer at first order. | $\partial L/\partial\lambda=0$ | Autodiff simplification. |
| Implicit optimum equations | SRC-0020 S1 | This page | Basis for hyperparameter derivatives. | Hessians, mixed derivatives | Hyperparameter optimization. |
| KSR | SRC-0020 S2 | This page | Tracks reweighting degeneracy. | $w_i$, $N$ | Validation diagnostic. |

## Evidence

The supplement shows additional plots where hyperparameter choices control overfitting and reweighting concentration, including comparisons between L2 and relative-entropy regularization. [SRC-0020]

## Limitations and Caveats

- Implicit derivative formulas assume local smoothness and must be adapted when constraints or boundaries are active. [SRC-0020]
- KSR/ESS diagnostics detect weight concentration but do not by themselves prove conformational coverage. [SRC-0020]

## Links

- [[wiki/sources/SRC-0019-mdrefine-python-package-refining-md-trajectories]]
- [[wiki/concepts/ensemble-and-force-field-refinement]]
- [[wiki/concepts/free-energy-reweighting-for-force-field-fine-tuning]]

## Citation links

- Source-local review only; no separate first-class citation links were added beyond the main-paper bundle relationship. [SRC-0020]

## Open Questions

- When are validation-gradient hyperparameter searches more reliable than grid scans in rugged refinement problems? [SRC-0020]

## Mathematical gaps

- The wiki records the derivative map and diagnostics, not every supplementary figure and table.

## Ingestion QA

### Retrieval questions checked

- What derivative simplification is used for $L_1(\mu)$?
- How are hyperparameter derivatives framed?
- How are boundary-active $\lambda$ values handled?
- What is KSR used for?

### Coverage decision

Complete at `coverage_profile: math-standard`. [SRC-0020]

### Known gaps

- Full supplementary numerical tables are not transcribed.
