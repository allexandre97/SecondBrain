---
type: source
status: active
created: 2026-06-30
updated: 2026-06-30
source_id: SRC-0019
display_title: "MDRefine"
short_title: "MDRefine"
aliases:
  - "SRC-0019"
  - "MDRefine"
source_path: raw/sources/SRC-0019-mdrefine-python-package-refining-md-trajectories.pdf
imported_path: raw/sources/SRC-0019-mdrefine-python-package-refining-md-trajectories.pdf
original_filename: "192501_1_5.0256841.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 8304c8e6adcdb7d5ac0997de7ec768efacc7db2167dcdf672cdba26833b7d67b
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
tags:
  - mdrefine
  - ensemble-refinement
  - forward-model-refinement
  - force-field-refinement
  - math-heavy
related:
  - "[[sources/SRC-0020-mdrefine-supplementary-material]]"
  - "[[concepts/ensemble-and-force-field-refinement]]"
  - "[[concepts/free-energy-reweighting-for-force-field-fine-tuning]]"
sources:
  - SRC-0019
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: math-standard
---

# MDRefine

Source ID: `SRC-0019`

## Raw source

- Repository path: `raw/sources/SRC-0019-mdrefine-python-package-refining-md-trajectories.pdf`
- Local relative link: [Open raw source](../../raw/sources/SRC-0019-mdrefine-python-package-refining-md-trajectories.pdf)

## Source bundle

Main paper for SRC-0020, the supplementary material. [SRC-0019] [SRC-0020]

## Summary

This 2025 JCP software paper introduces MDRefine, a Python package for refining MD ensembles, force-field corrections, and forward-model parameters against experimental data. [SRC-0019]

The package unifies maximum-entropy ensemble reweighting, force-field correction fitting, forward-model fitting, and hyperparameter selection with cross-validation. [SRC-0019]

## Key Points

- MDRefine treats disagreement with experiment as potentially arising from ensemble sampling, force-field errors, or forward-model errors. [SRC-0019]
- The software supports experimental observables with uncertainties, upper/lower bounds, and thermodynamic-cycle free-energy data. [SRC-0019]
- Ensemble refinement uses a relative-entropy regularized maximum-entropy form. [SRC-0019]
- Simultaneous refinement introduces force-field parameters $\phi$ and forward-model parameters $\theta$, with hyperparameters $\alpha,\beta,\gamma$ setting regularization weights. [SRC-0019]
- The inner ensemble-refinement problem can be reduced to optimizing Lagrange multipliers $\lambda$, making the outer problem lower-dimensional and more robust. [SRC-0019]
- JAX automatic differentiation is used for gradients, and BFGS/L-BFGS-B is used for optimization. [SRC-0019]

## Key equations

Regularized ensemble refinement:

$$
L[P]=
\frac{1}{2}\chi^2[P]+\alpha D_{\mathrm{KL}}[P\Vert P_0].
$$

[SRC-0019]

Maximum-entropy reweighted ensemble:

$$
P_{\lambda}(x)=
\frac{P_0(x)\exp[-\lambda\cdot g(x)]}{Z_{\lambda}}.
$$

[SRC-0019]

Reduced convex objective for $\lambda$:

$$
\Gamma(\lambda)=
\log Z_{\lambda}
+\lambda\cdot g_{\mathrm{exp}}
+\alpha\sum_i \lambda_i^2\sigma_{i,\mathrm{exp}}^2.
$$

[SRC-0019]

Joint ensemble, force-field, and forward-model loss:

$$
L(P,\phi,\theta)
=
-\alpha\Gamma(\lambda;\phi,\theta)
+\beta R_1(\phi)+\gamma R_2(\theta).
$$

[SRC-0019]

## Equation inventory

| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |
| $L[P]$ | SRC-0019 loss section | This page; [[concepts/ensemble-and-force-field-refinement]] | Balances experiment fit and entropy to prior. | $P$, $P_0$, $\alpha$ | Ensemble refinement objective. |
| $P_{\lambda}$ | SRC-0019 loss section | This page | Gives exponential reweighting form. | $\lambda$, $g(x)$, $Z_{\lambda}$ | Reweighted ensemble. |
| $\Gamma(\lambda)$ | SRC-0019 loss section | This page | Convex reduced optimization problem. | $\lambda$, $g_{\mathrm{exp}}$, $\sigma$ | Inner minimization. |
| Joint loss | SRC-0019 loss section | This page | Combines ensemble, force field, and forward model. | $\phi$, $\theta$, $R_1$, $R_2$ | Simultaneous refinement. |

## Evidence

The paper demonstrates the package on examples that include ensemble reweighting, force-field correction, forward-model refinement, and thermodynamic-cycle free energies. [SRC-0019]

## Limitations and Caveats

- Reweighting quality depends on overlap between the prior trajectory and the refined ensemble. [SRC-0019]
- Hyperparameter choices control the tradeoff between matching data and preserving the prior ensemble or reference model. [SRC-0019]
- Joint refinement can fit multiple error sources, but identifiability between ensemble, force-field, and forward-model errors remains a conceptual risk. [SRC-0019]

## Links

- [[sources/SRC-0020-mdrefine-supplementary-material]]
- [[concepts/ensemble-and-force-field-refinement]]
- [[concepts/free-energy-reweighting-for-force-field-fine-tuning]]
- [[questions/force-field-training-validation-scope]]

## Open Questions

- How reliably can cross-validation separate force-field error from forward-model error when both are flexible? [SRC-0019]

## Mathematical gaps

- The main-page equations are supplemented by SRC-0020, which contains derivative and hyperparameter-gradient details.

## Ingestion QA

### Retrieval questions checked

- What does MDRefine refine?
- How is maximum-entropy ensemble refinement represented?
- What are $\lambda$, $\phi$, and $\theta$?
- How are force-field and forward-model regularizations combined?
- What does the supplement add?

### Coverage decision

Complete at `coverage_profile: math-standard`. [SRC-0019]

### Known gaps

- Individual example numerical outcomes are not exhaustively reproduced.
