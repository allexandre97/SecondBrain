---
type: source
status: active
created: 2026-06-30
updated: 2026-06-30
source_id: SRC-0018
display_title: "Force-Field Optimization via AWH, Frozen-Bias Replay, and Information Geometry"
short_title: "AWH Replay Force-Field Optimization"
aliases:
  - "SRC-0018"
  - "AWH Replay Force-Field Optimization"
  - "Force-Field Optimization via AWH, Frozen-Bias Replay, and Information Geometry"
source_path: raw/sources/SRC-0018-force-field-optimization-via-awh-gradients.pdf
imported_path: raw/sources/SRC-0018-force-field-optimization-via-awh-gradients.pdf
original_filename: "AWH_Gradients.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 9c12541564089350a6fa68eb4bd5b67ec6c60f255b1d103227bc5980542168ee
authors:
  - "Alexandre Blanco Gonzalez"
author_entities: []
year: 2026
venue: "Local draft"
doi:
arxiv:
metadata_review_status: reviewed
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/adaptive-sampling
  - research/molecular-simulation/free-energy
tags:
  - awh
  - force-field-optimization
  - replay-reweighting
  - natural-gradient
  - math-heavy
related:
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
  - "[[wiki/concepts/accelerated-weight-histogram-method]]"
  - "[[wiki/concepts/free-energy-reweighting-for-force-field-fine-tuning]]"
sources:
  - SRC-0018
cites_sources: []
citation_match_status: reviewed
cqt_review_status: linked
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: math-standard
---

# Force-Field Optimization via AWH, Frozen-Bias Replay, and Information Geometry

Source ID: `SRC-0018`

## Raw source

- Repository path: `raw/sources/SRC-0018-force-field-optimization-via-awh-gradients.pdf`
- Open raw source: [raw/sources/SRC-0018-force-field-optimization-via-awh-gradients.pdf](../../raw/sources/SRC-0018-force-field-optimization-via-awh-gradients.pdf)

## Summary

This 2026 local/draft-style theory document describes a force-field optimization pipeline that uses AWH to build a broad reference ensemble, freezes the bias, collects production frames, and performs offline replay reweighting to compute endpoint free energies, gradients, observables, ESS diagnostics, and Fisher-metric trust-region steps. [SRC-0018]

The important conceptual separation is that the optimizer does not differentiate through the adaptive AWH update rule; AWH is used to construct a reusable reference mixture, and the optimization math is then standard importance reweighting plus natural-gradient step control. [SRC-0018]

## Key Points

- Adaptive AWH is used only until readiness criteria pass, after which frozen-bias production data are collected. [SRC-0018]
- Replay reweighting evaluates target lambda states from stored extended-ensemble frames. [SRC-0018]
- Endpoint free-energy gradients are weighted averages of parameter energy gradients under target-state replay weights. [SRC-0018]
- General state observables can be added with the same replay machinery, so training targets need not be limited to free energies. [SRC-0018]
- The optimizer constructs a latent-space empirical Fisher matrix from score covariances and uses it as a KL-local metric. [SRC-0018]
- Step control combines diagonal regularization, Jacobi preconditioning, eigentruncation, KL-target scaling, ESS checks, and split-half confidence moderation. [SRC-0018]

## Key equations

Frozen extended-ensemble reference density:

$$
p_{\mathrm{ref},\ell}(x,V,i)
\propto
\exp[-u_{\mathrm{ref},\ell}(x,V,i)+g_{\mathrm{ref},\ell}(i)].
$$

[SRC-0018]

Replay free energy at target state $m$:

$$
\tilde F_{\ell,m}(\theta)
=
-\beta_{\ell}^{-1}\log
\sum_n
\frac{\exp[-u_{\ell}(x_n,V_n,m;\theta)]}
{\sum_{i\in\Lambda_{\ell}}\exp[-u_{\mathrm{ref},\ell}(x_n,V_n,i)+g_{\mathrm{ref},\ell}(i)]}.
$$

[SRC-0018]

Endpoint gradient:

$$
\nabla_{\theta} \tilde F_{\ell,m}(\theta)
=
\beta_{\ell}^{-1}\sum_n
w_{\ell,m}^{\mathrm{rep}}(n;\theta)
\nabla_{\theta}u_{\ell}(x_n,V_n,m;\theta).
$$

[SRC-0018]

Local KL geometry:

$$
D_{\mathrm{KL}}(p_{\phi}\Vert p_{\phi+\Delta\phi})
=
\frac{1}{2}\Delta\phi^{\top}I(\phi)\Delta\phi+O(\|\Delta\phi\|^3).
$$

[SRC-0018]

Empirical Fisher as score covariance:

$$
I(\phi)=\mathrm{Cov}_{p_{\phi}}\left[\nabla_{\phi}u(x,V,i;\phi)\right].
$$

[SRC-0018]

## Equation inventory

| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |
| Frozen reference density | SRC-0018 section 2 | This page; [[wiki/concepts/awh-replay-force-field-optimization]] | Defines frozen AWH mixture. | $u_{\mathrm{ref}}$, $g_{\mathrm{ref}}$, $i$ | Reference data distribution. |
| Replay target free energy | SRC-0018 sections 3-4 | This page | Estimates target-state free energies. | $m$, $\Lambda_{\ell}$, $\theta$ | Endpoint/cycle predictions. |
| Endpoint gradient | SRC-0018 section 5 | This page | Differentiates replayed free energies. | $w^{\mathrm{rep}}$, $\nabla_{\theta}u$ | Optimizer gradient. |
| KL expansion | SRC-0018 sections 9-10 | This page | Justifies Fisher trust region. | $\phi$, $I(\phi)$ | Step scaling. |
| Fisher covariance | SRC-0018 section 10 | This page | Builds empirical metric. | score vectors | Natural-gradient preconditioner. |

## Algorithmic recursions

The macro-epoch pipeline is: run adaptive AWH until Stage A readiness passes, run frozen-bias probe for Stage B split/parity validation, collect frozen production frames, replay selected frames under candidate Hamiltonians, assemble predictions and gradients, build Fisher/KL step, line search with ESS and drift checks, then start the next macro epoch. [SRC-0018]

## Limitations and Caveats

- Correctness depends on frozen-bias reference support; replay cannot recover target states absent from the sampled support. [SRC-0018]
- Fisher/KL scaling is local and requires empirical stabilization when finite samples make the Fisher matrix ill-conditioned. [SRC-0018]
- This is a method/theory document rather than a peer-reviewed benchmark paper. [SRC-0018]

## Links

- [[wiki/concepts/awh-replay-force-field-optimization]]
- [[wiki/concepts/accelerated-weight-histogram-method]]
- [[wiki/concepts/free-energy-reweighting-for-force-field-fine-tuning]]
- [[wiki/questions/force-field-training-validation-scope]]
- [[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]

## Claims

- [[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]] - Frozen-bias replay optimization requires support diagnostics before trusting parameter updates. [SRC-0018]

## Questions

- [[wiki/questions/force-field-training-validation-scope]] - When do ESS, parity, and split-half diagnostics justify replay-based force-field updates? [SRC-0018]

## Citation links

- Targeted citation review found no confirmed citations from this source to currently ingested force-field fitting/refinement cluster sources.

## Open Questions

- Which readiness and ESS thresholds best predict successful updates across chemically diverse force-field parameterizations? [SRC-0018]

## Mathematical gaps

- The wiki records the central replay and Fisher geometry, but not every code-facing configuration option in the document.
- Bibliographic metadata was reviewed from the local draft title page; ordinary DOI/arXiv metadata are not applicable. [SRC-0018]

## Ingestion QA

### Retrieval questions checked

- Does the method differentiate through online AWH updates?
- What is frozen-bias replay?
- How are endpoint gradients computed?
- Why is Fisher the metric tensor?
- How does KL-target scaling relate to ESS?
- How are non-free-energy observables incorporated?

### Coverage decision

Complete at `coverage_profile: math-standard`. [SRC-0018]

### Known gaps

- Implementation examples are summarized, not reproduced.
