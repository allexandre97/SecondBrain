---
type: source
status: active
created: 2026-06-30
updated: 2026-06-30
source_id: SRC-0024
display_title: "Stability-Aware Training of Machine Learning Force Fields with Differentiable Boltzmann Estimators"
short_title: "StABlE MLFF Training"
aliases:
  - "SRC-0024"
  - "StABlE MLFF Training"
  - "Stability-Aware Training of Machine Learning Force Fields with Differentiable Boltzmann Estimators"
source_path: raw/sources/SRC-0024-stable-training-machine-learning-force-fields-boltzmann-estimators.pdf
imported_path: raw/sources/SRC-0024-stable-training-machine-learning-force-fields-boltzmann-estimators.pdf
original_filename: "2402.13984v3.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 7bfebbdab1ab649dc430b4d475f92959e16fc8f597e29a5bd8e4f8adf4f39b9c
authors:
  - "Sanjeev Raja"
  - "Ishan Amin"
  - "Fabian Pedregosa"
  - "Aditi Krishnapriyan"
author_entities: []
year: 2025
venue: "Transactions on Machine Learning Research"
doi:
arxiv: "2402.13984v3"
metadata_review_status: reviewed
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/machine-learning/scientific-modeling
  - research/machine-learning/molecular-modeling
  - research/molecular-simulation/molecular-dynamics
tags:
  - machine-learning-force-fields
  - stable-training
  - boltzmann-estimator
  - differentiable-simulation
  - math-heavy
related:
  - "[[wiki/concepts/stability-aware-mlff-training]]"
  - "[[wiki/concepts/automated-force-field-training]]"
sources:
  - SRC-0024
cites_sources: []
citation_match_status: reviewed
cqt_review_status: linked
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: math-standard
---

# Stability-Aware Training of Machine Learning Force Fields with Differentiable Boltzmann Estimators

Source ID: `SRC-0024`

## Raw source

- Repository path: `raw/sources/SRC-0024-stable-training-machine-learning-force-fields-boltzmann-estimators.pdf`
- Open raw source: [raw/sources/SRC-0024-stable-training-machine-learning-force-fields-boltzmann-estimators.pdf](../../raw/sources/SRC-0024-stable-training-machine-learning-force-fields-boltzmann-estimators.pdf)

## Summary

This 2025 TMLR paper introduces Stability-Aware Boltzmann Estimator Training, abbreviated StABlE, for training machine-learning force fields that remain stable in MD simulations while matching reference observables. [SRC-0024]

The method alternates between running many MD replicas to find near-unstable regions and learning from observable discrepancies using a Boltzmann Estimator, avoiding direct backpropagation through long MD trajectories and requiring no new ab initio labels for the unstable configurations. [SRC-0024]

## Key Points

- StABlE combines conventional energy/force supervision with observable matching. [SRC-0024]
- The observable loss compares an equilibrium expectation under the current MLFF distribution to a reference observable. [SRC-0024]
- The Boltzmann Estimator differentiates equilibrium expectations by using the Boltzmann form of the target distribution rather than unrolling the MD integrator. [SRC-0024]
- The training loop searches for instability by running parallel MD replicas and then rewinds unstable replicas to near-instability states for learning. [SRC-0024]
- The paper demonstrates the method on aspirin, an alanine tetrapeptide, and all-atom water with SchNet, NequIP, and GemNet-T architectures. [SRC-0024]
- Reported benefits include longer stable simulation times, better observable agreement, and better temperature generalization than energy/force-only baselines. [SRC-0024]

## Key equations

Observable-matching loss:

$$
L_{\mathrm{obs}}(\theta)
=
\left\|
E_{\Gamma\sim P_{\theta}}[g(\Gamma)]-g_{\mathrm{ref}}
\right\|_2^2.
$$

[SRC-0024, eq. 2]

Boltzmann distribution in the canonical ensemble:

$$
P_{\theta}(\Gamma)
=
\frac{\exp[-H_{\theta}(\Gamma)/(k_B T)]}{C(\theta)}.
$$

[SRC-0024]

Gradient chain rule for the observable loss:

$$
\nabla_{\theta}L_{\mathrm{obs}}^{\top}
=
2\left(E_{\Gamma\sim P_{\theta}}[g(\Gamma)]-g_{\mathrm{ref}}\right)^{\top}
\frac{\partial E_{\Gamma\sim P_{\theta}}[g(\Gamma)]}{\partial\theta}.
$$

[SRC-0024, eq. 3]

N-sample Boltzmann Estimator:

$$
\mathcal E(\Gamma_1,\ldots,\Gamma_N)
=
\frac{N}{k_BT(N-1)}
\left(
\hat E[g(\Gamma)]\hat E[\nabla_{\theta}U_{\theta}(\Gamma)]^{\top}
-
\hat E[g(\Gamma)\cdot\nabla_{\theta}U_{\theta}(\Gamma)^{\top}]
\right).
$$

[SRC-0024, eq. 4]

Combined StABlE loss:

$$
L_{\mathrm{StABlE}}(\theta)=L_{\mathrm{obs}}+\lambda L_{\mathrm{QM}}.
$$

[SRC-0024, eq. 6]

## Equation inventory

| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |
| $L_{\mathrm{obs}}$ | SRC-0024 section 3.1 | This page; [[wiki/concepts/stability-aware-mlff-training]] | Matches equilibrium observables. | $g(\Gamma)$, $g_{\mathrm{ref}}$, $P_{\theta}$ | Observable supervision. |
| Boltzmann distribution | SRC-0024 section 3.1 | This page | Defines equilibrium distribution induced by MLFF. | $H_{\theta}$, $T$, $C(\theta)$ | Differentiation target. |
| Observable-loss gradient | SRC-0024 eq. 3 | This page | Reduces training gradient to expectation Jacobian. | $\theta$, $g$ | Optimization. |
| Boltzmann Estimator | SRC-0024 eq. 4 | This page; [[wiki/concepts/stability-aware-mlff-training]] | Estimates Jacobian without unrolling MD. | $\nabla_{\theta}U_{\theta}$, $N$, $k_BT$ | Differentiable training. |
| $L_{\mathrm{StABlE}}$ | SRC-0024 eq. 6 | This page | Regularizes observable training with QM data. | $\lambda$, $L_{\mathrm{QM}}$ | Prevents underconstrained fitting. |

## Algorithmic recursions

StABlE pretrains on energy/force data, launches parallel MD replicas from training states, marks and rewinds unstable replicas, runs short MD from near-unstable states, computes observable losses and Boltzmann Estimator gradients, updates the MLFF, and repeats until instability drops or a budget is reached. [SRC-0024]

## Limitations and Caveats

- Observable supervision is underconstrained without the energy/force regularizer. [SRC-0024]
- Stability criteria and selected observables are system-dependent design choices. [SRC-0024]
- The estimator targets equilibrium expectations; biased or poorly equilibrated simulation data can still create training signal problems. [SRC-0024]

## Links

- [[wiki/concepts/stability-aware-mlff-training]]
- [[wiki/concepts/automated-force-field-training]]
- [[wiki/questions/force-field-training-validation-scope]]
- [[wiki/claims/CLM-0011-stability-aware-mlff-training-targets-md-stability]]

## Claims

- [[wiki/claims/CLM-0011-stability-aware-mlff-training-targets-md-stability]] - StABlE treats downstream MD stability and observable recovery as training targets. [SRC-0024]

## Questions

- [[wiki/questions/force-field-training-validation-scope]] - How should downstream MD stability be weighted against static energy and force errors? [SRC-0024]

## Citation links

- Targeted citation review found no confirmed citations from this source to currently ingested force-field fitting/refinement cluster sources.

## Open Questions

- Which observables are most reliable for stabilizing general-purpose MLFFs without hiding dynamical errors? [SRC-0024]

## Ingestion QA

### Retrieval questions checked

- What problem does StABlE solve?
- How is the Boltzmann Estimator defined?
- Why does the method avoid backpropagating through long MD?
- How does the training loop find unstable regions?
- What systems and architectures were tested?

### Coverage decision

Complete at `coverage_profile: math-standard`. [SRC-0024]

### Known gaps

- Supplementary implementation details are referenced by the paper but not present as a separate local source in this folder.
