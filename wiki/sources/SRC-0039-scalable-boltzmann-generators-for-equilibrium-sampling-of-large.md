---
type: source
status: active
created: 2026-06-30
updated: 2026-06-30
source_id: SRC-0039
display_title: "Scalable Boltzmann Generators for Equilibrium Sampling of Large-Scale Materials"
short_title: "Scalable Boltzmann Generators"
aliases:
  - "SRC-0039"
  - "Scalable Boltzmann Generators"
  - "Scalable Boltzmann Generators for Equilibrium Sampling of Large-Scale Materials"
source_path: raw/sources/SRC-0039-scalable-boltzmann-generators-for-equilibrium-sampling-of-large.pdf
original_filename: "s41467-026-73900-9.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 16a9be2319ca1b07eb25eaa5b6bdd8d824dbe2e6034509e78755ef2cc463596e
authors:
  - "Maximilian Schebek"
  - "Frank Noe"
  - "Jutta Rogal"
author_entities: []
year: 2026
venue: "Nature Communications"
doi: "10.1038/s41467-026-73900-9"
arxiv:
metadata_review_status: reviewed
areas:
  - research
categories:
  - research/molecular-simulation/free-energy
  - research/machine-learning/scientific-modeling
  - research/machine-learning/molecular-modeling
tags:
  - Boltzmann-generators
  - normalizing-flows
  - materials-sampling
  - free-energy
related:
  - "[[wiki/concepts/boltzmann-generators-equilibrium-sampling]]"
  - "[[wiki/concepts/transferable-and-scalable-boltzmann-generators]]"
sources:
  - SRC-0039
cites_sources:
  - SRC-0041
citation_match_status: reviewed
cqt_review_status: linked
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: math-standard
---

# Scalable Boltzmann Generators for Equilibrium Sampling of Large-Scale Materials

Source ID: `SRC-0039`

## Raw source

- Repository path: `raw/sources/SRC-0039-scalable-boltzmann-generators-for-equilibrium-sampling-of-large.pdf`
- Open raw source: [raw/sources/SRC-0039-scalable-boltzmann-generators-for-equilibrium-sampling-of-large.pdf](../../raw/sources/SRC-0039-scalable-boltzmann-generators-for-equilibrium-sampling-of-large.pdf)

## Summary

Schebek, Noe, and Rogal introduce a local Boltzmann-generator architecture for large crystalline materials. It combines augmented coupling flows with graph neural networks over local environments, enabling energy-based training, faster inference, and transfer from small training cells to systems with more than 1000 atoms. [SRC-0039]

## Key Points

- The method uses locality to avoid global architectures whose interactions scale quadratically with system size. [SRC-0039, Results]
- The augmented model treats auxiliary coordinates as a noised copy of physical coordinates and alternates conditional updates between physical and auxiliary variables. [SRC-0039, Results]
- The architecture models displacements from an ideal crystal lattice rather than absolute positions, keeping inputs size-independent for transfer across system sizes. [SRC-0039, Results]
- Reported applications include Lennard-Jones crystals, mW water ice phases, and Stillinger-Weber silicon-related phase diagrams. [SRC-0039]
- Local BGs achieve much higher effective sample sizes than comparable global models in the reported mW ice and FCC Lennard-Jones cases, and can estimate free energies for larger systems using models trained on smaller cells. [SRC-0039, table 1 and Free energy estimation]

## Key equations

**Augmented base distribution, source Eq. (1) [SRC-0039]:**

$$
q(x,a)=q(x)N(a;x,\eta_q^2 I)
$$

**Change of variables, source Eq. (3) [SRC-0039]:**

$$
q_\theta(x',a')=q(x,a)\left|\det J_{F_\theta}(x,a)\right|^{-1}
$$

**Importance weights, source Eq. (13) [SRC-0039]:**

$$
w(x)=\exp\left(u_q(x)-u_p(F_\theta(x))+\log|\det J_{F_\theta}(x)|\right)
$$

**Targeted free-energy perturbation estimate, source Eq. (15) [SRC-0039]:**

$$
\Delta f_{qp}=-\log E_{x\sim q}[w(x)]
$$

## Equation inventory

| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |
| Augmented base distribution | Eq. (1) | Key equations | Defines auxiliary variables as noisy copies of physical variables | $x$, $a$, $\eta_q$ | Augmented coupling-flow setup |
| Local conditional update | Eq. (2) | Key Points | Updates particle coordinates conditioned on local embedding | $x_i$, $h_i^a$, $g$ | Local GNN flow transform |
| Augmented change of variables | Eq. (3) | Key equations | Computes joint generated density | $q_\theta$, $F_\theta$, $J_{F_\theta}$ | Exact likelihood/reweighting |
| KL/free-energy training loss | Eq. (12) | Mathematical gaps | Energy-based training objective | $L_{qp}$, $w$, $\Delta f_{qp}$ | Training diagnostic and objective |
| Importance weights | Eq. (13) | Key equations | Computes target/base density ratio through flow | $u_q$, $u_p$, $F_\theta$ | Reweighting and ESS |
| Kish ESS | Eq. (14) | Key Points | Diagnoses reweighting efficiency | $w(x_i)$ | Sampling-quality diagnostic |
| Targeted free energy perturbation | Eq. (15) | Key equations | Estimates free-energy difference from trained flow | $\Delta f_{qp}$, $w$ | Free-energy calculation |

## Limitations

- The architecture is demonstrated mainly for crystalline materials; extending it to liquid phases and broad chemical-space generalization is listed as future work. [SRC-0039, Discussion]
- The authors note different performance across potentials and structures, requiring further investigation. [SRC-0039, Discussion]
- For inexpensive empirical potentials, training can still take longer wall-clock time than a single MD+MBAR estimate, although the BG approach is more attractive when energy evaluations are expensive or reused across many conditions. [SRC-0039, Free energy estimation]

## Claims

- Local Boltzmann-generator architectures can improve scaling, but the free-energy and sampling claims still depend on effective sample size and reweighting support. [SRC-0039]
- [[wiki/claims/CLM-0016-boltzmann-generators-need-overlap-and-reweighting-support]]

## Tensions

- [[wiki/tensions/TEN-0009-boltzmann-generator-one-shot-sampling-vs-overlap-risk]]

## Citation Links

- `SRC-0041`: The references list Noe, Olsson, Kohler, and Wu, "Boltzmann generators: sampling equilibrium states of many-body systems with deep learning," Science 365, eaaw1147, matching the ingested original Boltzmann generators source. [SRC-0039, reference 3]

## Links

- [[wiki/concepts/boltzmann-generators-equilibrium-sampling]]
- [[wiki/concepts/transferable-and-scalable-boltzmann-generators]]
- [[wiki/concepts/free-energy-estimation]]

## Ingestion QA

### Retrieval questions checked

- What scaling limitation does this paper address?
- How does locality enter the BG architecture?
- Why use augmented variables?
- How does the model transfer across system size?
- What systems validate the approach?
- How are free energies computed?
- What limitations remain?

### Coverage decision

Complete at `coverage_profile: math-standard`. The page captures architecture, scaling mechanism, equations, evidence, and caveats.

### Known gaps

- Supplementary implementation and all phase-diagram details remain in the raw source.
