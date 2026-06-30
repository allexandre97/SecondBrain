---
type: source
status: active
created: 2026-06-30
updated: 2026-06-30
source_id: SRC-0021
display_title: "Tuning Potential Functions to Host-Guest Binding Data"
short_title: "Host-Guest Potential Tuning"
aliases:
  - "SRC-0021"
  - "Host-Guest Potential Tuning"
  - "Tuning Potential Functions to Host-Guest Binding Data"
source_path: raw/sources/SRC-0021-tuning-potential-functions-host-guest-binding-data.pdf
imported_path: raw/sources/SRC-0021-tuning-potential-functions-host-guest-binding-data.pdf
original_filename: "tuning-potential-functions-to-host-guest-binding-data.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 8cb7671c2b32e1eebe95ae82226b329bb451c6f173c9e1584edbb54a52606f57
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/computational-drug-discovery
tags:
  - host-guest
  - binding-free-energy
  - forcebalance
  - openff-evaluator
  - implicit-solvent
  - math-heavy
related:
  - "[[sources/SRC-0022-tuning-potential-functions-host-guest-binding-data-supporting-information]]"
  - "[[concepts/force-field-training-from-experimental-observables]]"
  - "[[concepts/relative-binding-free-energy-benchmarking]]"
sources:
  - SRC-0021
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: math-standard
---

# Tuning Potential Functions to Host-Guest Binding Data

Source ID: `SRC-0021`

## Raw source

- Repository path: `raw/sources/SRC-0021-tuning-potential-functions-host-guest-binding-data.pdf`
- Local relative link: [Open raw source](../../raw/sources/SRC-0021-tuning-potential-functions-host-guest-binding-data.pdf)

## Source bundle

Main paper for SRC-0022, the supporting information. [SRC-0021] [SRC-0022]

## Summary

This 2024 JCTC paper extends OpenFF Evaluator and ForceBalance to train potential-function parameters against host-guest absolute binding free energies. [SRC-0021]

As a proof of principle, the authors optimize OBC2 generalized Born cavity radii on 36 host-guest systems, test on 90 additional host-guest systems, and evaluate transfer to 59 protein-ligand systems and hydration free energies. [SRC-0021]

## Key Points

- The paper argues that host-guest complexes are simpler binding models than protein-ligand systems and can isolate force-field errors more cleanly. [SRC-0021]
- The infrastructure computes host-guest ABFEs and gradients with respect to force-field parameters, then passes them to ForceBalance. [SRC-0021]
- The initial application optimizes OBC2 GB cavity radii, not a full molecular mechanics force field. [SRC-0021]
- Refitting improves both training and host-guest test performance and shows encouraging transfer to protein-ligand ABFEs. [SRC-0021]
- The optimized radii are smaller than baseline radii and lead to excessively favorable hydration free energies, exposing a binding/HFE tradeoff. [SRC-0021]
- OBC2 implicit solvent in OpenMM gives about a 10-fold speedup relative to corresponding explicit-solvent ABFE calculations in this study. [SRC-0021]

## Key equations

OBC/GB electrostatic solvation form:

$$
G_{\mathrm{GB}}
=
-\frac{1}{2}
\left(1-\frac{1}{\epsilon}\right)
\sum_{i,j}
\frac{q_iq_j}{f_{\mathrm{GB}}(d_{ij},R_i,R_j)}.
$$

[SRC-0021]

Pose-combined binding free energy:

$$
\Delta G_b
=
-\beta^{-1}
\log\sum_{k=1}^{N_b}
\exp[-\beta\Delta G_{b,k}].
$$

[SRC-0021]

Gradient for multiple poses:

$$
\frac{\partial \Delta G_b}{\partial \theta}
=
\sum_{k=1}^{N_b}
p_k
\frac{\partial \Delta G_{b,k}}{\partial \theta},
\quad
p_k=
\frac{\exp[-\beta\Delta G_{b,k}]}
{\sum_l\exp[-\beta\Delta G_{b,l}]}.
$$

[SRC-0021]

ForceBalance objective:

$$
\mathcal L(\theta)
=
\sum_i
\left[
\frac{y_i(\theta)-y_i^{\mathrm{exp}}}{\sigma_i}
\right]^2
+
\sum_j
\left[
\frac{\theta_j-\theta_{j,0}}{\sigma_{\theta,j}}
\right]^2.
$$

[SRC-0021]

## Equation inventory

| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |
| GB solvation energy | SRC-0021 Methods | This page | Defines optimized implicit-solvent energy component. | $q_i$, $R_i$, $f_{\mathrm{GB}}$ | Parameter target. |
| Pose-combined $\Delta G_b$ | SRC-0021 Methods | This page | Combines asymmetric binding poses. | $\Delta G_{b,k}$, $N_b$ | ABFE prediction. |
| Pose-gradient mixture | SRC-0021 Methods | This page | Computes parameter gradient over poses. | $p_k$, $\theta$ | ForceBalance gradients. |
| ForceBalance least squares | SRC-0021 Methods | This page; [[concepts/force-field-training-from-experimental-observables]] | Fits properties with priors. | $y_i$, $\theta_j$, $\sigma_i$ | Optimization objective. |

## Evidence

The dataset includes 126 host-guest complexes, with 36 selected for training and 90 held out for host-guest testing. [SRC-0021]

The supporting information adds the train/test ABFE tables, protein-ligand benchmark tables, hydration free energy benchmarks, and prior-width sensitivity analysis. [SRC-0022]

## Limitations and Caveats

- The proof-of-principle fit improves binding but worsens hydration free energies, indicating that refitting one parameter class against one observable class can create property tradeoffs. [SRC-0021]
- The optimized radii are specific to OBC2 GBSA and should not be treated as generally transferable classical force-field parameters. [SRC-0021]
- Host-guest complexes reduce but do not eliminate modeling ambiguities such as restraints, protonation, and host flexibility. [SRC-0021]

## Links

- [[sources/SRC-0022-tuning-potential-functions-host-guest-binding-data-supporting-information]]
- [[concepts/force-field-training-from-experimental-observables]]
- [[concepts/relative-binding-free-energy-benchmarking]]
- [[questions/force-field-training-validation-scope]]

## Open Questions

- What additional GB model terms or training observables are required to fit both binding free energies and hydration free energies? [SRC-0021]

## Mathematical gaps

- The wiki records the optimization structure, but not every alchemical window and restraint schedule.

## Ingestion QA

### Retrieval questions checked

- Why use host-guest binding data for training?
- What framework was extended?
- Which parameters were optimized?
- How are binding free-energy gradients passed to ForceBalance?
- What transfer and failure modes were reported?

### Coverage decision

Complete at `coverage_profile: math-standard`. [SRC-0021]

### Known gaps

- Full benchmark tables remain in SRC-0022.
