---
type: source
status: active
created: 2026-06-30
updated: 2026-06-30
source_id: SRC-0017
display_title: "Physically Interpretable Interatomic Potentials via Symbolic Regression and Reinforcement Learning"
short_title: "Symbolic-Regression Interatomic Potentials"
aliases:
  - "SRC-0017"
  - "Symbolic-Regression Interatomic Potentials"
  - "Physically Interpretable Interatomic Potentials via Symbolic Regression and Reinforcement Learning"
source_path: raw/sources/SRC-0017-symbolic-regression-reinforcement-learning-interatomic-potentials.pdf
imported_path: raw/sources/SRC-0017-symbolic-regression-reinforcement-learning-interatomic-potentials.pdf
original_filename: "s41524-025-01952-4.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: fc16263d75e83dc38af91332156626b248d7684521ed3341832bb76baaed5a98
authors:
  - "Bilvin Varughese"
  - "Troy D. Loeffler"
  - "Suvo Banik"
  - "Aditya Koneru"
  - "Sukriti Manna"
  - "Karthik Balasubramanian"
  - "Rohit Batra"
  - "Mathew J. Cherukara"
  - "Orcun Yildiz"
  - "Tom Peterka"
  - "Bobby G. Sumpter"
  - "Subramanian K.R.S. Sankaranarayanan"
author_entities: []
year: 2025
venue: "npj Computational Materials"
doi: "10.1038/s41524-025-01952-4"
arxiv:
metadata_review_status: reviewed
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/machine-learning/scientific-modeling
tags:
  - symbolic-regression
  - interatomic-potentials
  - reinforcement-learning
  - embedded-atom-model
related:
  - "[[wiki/concepts/symbolic-regression-interatomic-potentials]]"
  - "[[wiki/concepts/automated-force-field-training]]"
sources:
  - SRC-0017
cites_sources: []
citation_match_status: reviewed
cqt_review_status: linked
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: standard
---

# Physically Interpretable Interatomic Potentials via Symbolic Regression and Reinforcement Learning

Source ID: `SRC-0017`

## Raw source

- Repository path: `raw/sources/SRC-0017-symbolic-regression-reinforcement-learning-interatomic-potentials.pdf`
- Open raw source: [raw/sources/SRC-0017-symbolic-regression-reinforcement-learning-interatomic-potentials.pdf](../../raw/sources/SRC-0017-symbolic-regression-reinforcement-learning-interatomic-potentials.pdf)

## Summary

This 2026 npj Computational Materials paper uses equation-learner networks, symbolic regression, and continuous-action Monte Carlo Tree Search to discover interpretable embedded-atom-style potentials for copper from DFT data. [SRC-0017]

The paper positions symbolic regression as a middle ground between fixed-form empirical potentials and black-box machine-learning potentials: the learned model can change functional form while still producing explicit equations. [SRC-0017]

## Key Points

- Training data come from nested ensemble sampling and DFT energetics spanning crystalline, surface, defect, and highly disordered configurations. [SRC-0017]
- The method first demonstrates recovery of a known Sutton-Chen EAM form, then searches for improved SR1 and SR2 EAM-like models. [SRC-0017]
- MCTS explores equation structure while gradient descent optimizes continuous coefficients. [SRC-0017]
- SR1 and SR2 improve energy and force predictions over Sutton-Chen EAM, especially away from equilibrium. [SRC-0017]
- Validation includes equations of state, elastic constants, phonon dispersion, surface energies, defect formation energies, grain boundaries, polymorph ordering, and two-phase melting simulations. [SRC-0017]
- SR models predict copper melting near $1300$ K, closer to the experimental $1358$ K than the Sutton-Chen estimate reported at $1154$ K. [SRC-0017]

## Mathematical structure

The learned potential remains within an EAM-style decomposition:

$$
E=\sum_i F(\rho_i)+\frac{1}{2}\sum_{i\ne j}\phi(r_{ij}),
$$

where symbolic regression searches for explicit forms of the pair, density, and embedding terms. [SRC-0017]

## Equation inventory

| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |
| EAM decomposition | SRC-0017 methods/results | This page; [[wiki/concepts/symbolic-regression-interatomic-potentials]] | Defines the interpretable potential family. | $F$, $\rho_i$, $\phi(r)$ | Search space scaffold. |
| SR1/SR2 symbolic terms | SRC-0017 results | Source only | Learned explicit functions. | Pair/density/embedding terms | Model deployment. |
| Energy/force loss | SRC-0017 results/methods | This page conceptually | Fits DFT energies and forces. | DFT labels, model predictions | Training objective. |

## Evidence

For near-equilibrium structures, SR1 reduces energy MAE relative to SC-EAM, and for non-equilibrium structures it substantially reduces both energy and force errors. [SRC-0017]

The paper emphasizes that several validation properties, including melting dynamics and phonon dispersion, were not direct loss-function targets, so their recovery is used as a transferability argument. [SRC-0017]

## Limitations and Caveats

- The main demonstration is copper, so cross-element and molecular-transfer claims require separate validation. [SRC-0017]
- The symbolic search depends on the operator set, active-learning data coverage, and MCTS budget. [SRC-0017]
- Interpretability is functional-form interpretability, not automatic proof that every learned term has a unique physical mechanism. [SRC-0017]

## Links

- [[wiki/concepts/symbolic-regression-interatomic-potentials]]
- [[wiki/concepts/automated-force-field-training]]
- [[wiki/questions/force-field-training-validation-scope]]

## Questions

- [[wiki/questions/force-field-training-validation-scope]] - Which out-of-training properties are enough to trust symbolic-regression potentials beyond the demonstrated material system? [SRC-0017]

## Citation links

- Targeted citation review found no confirmed citations from this source to currently ingested force-field fitting/refinement cluster sources.

## Open Questions

- How robust is equation discovery when the target material requires charge transfer, chemistry, or multiple elements? [SRC-0017]

## Ingestion QA

### Retrieval questions checked

- What is learned by symbolic regression?
- How is MCTS used?
- What training data are used?
- How do SR1/SR2 compare with Sutton-Chen EAM?
- Which transfer validation properties are reported?

### Coverage decision

Complete at `coverage_profile: standard`. [SRC-0017]

### Known gaps

- The exact SR1/SR2 formula terms are left in the source rather than transcribed.
