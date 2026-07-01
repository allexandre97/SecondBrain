---
type: concept
status: active
created: 2026-06-30
updated: 2026-07-01
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/molecular-simulation/free-energy
tags:
  - reweighting
  - zwanzig
  - effective-sample-size
  - force-field-fine-tuning
related:
  - "[[wiki/concepts/free-energy-estimation]]"
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
  - "[[wiki/concepts/ensemble-and-force-field-refinement]]"
sources:
  - SRC-0016
  - SRC-0018
  - SRC-0019
  - SRC-0020
sensitivity: public
encryption: none
---

# Free Energy Reweighting for Force Field Fine-Tuning

## Summary

Free-energy reweighting fine-tunes force fields by estimating the effect of candidate parameter changes on free energies or observables using configurations sampled from a reference model. [SRC-0016] [SRC-0018] [SRC-0019]

## Key Points

- SRC-0016 uses Zwanzig reweighting to fine-tune espaloma charges against hydration free energies without resimulating each candidate. [SRC-0016]
- SRC-0018 uses frozen-bias AWH replay to estimate endpoint free energies and gradients from a frozen extended-ensemble reference. [SRC-0018]
- SRC-0019 and SRC-0020 use exponential reweighting and maximum-entropy logic to refine ensembles, force-field corrections, and forward models. [SRC-0019] [SRC-0020]
- Effective sample size, Kish size ratio, split-half checks, or parity checks are necessary because reweighting fails when the reference ensemble lacks support for the candidate model. [SRC-0016] [SRC-0018] [SRC-0020]

## Core equations

Zwanzig estimator:

$$
\Delta G(\theta)
=
-\beta^{-1}\log
\left\langle
\exp[-\beta\Delta U(x;\theta)]
\right\rangle_0.
$$

[SRC-0016]

Exponential ensemble reweighting:

$$
P_{\lambda}(x)=
\frac{P_0(x)\exp[-\lambda\cdot g(x)]}{Z_{\lambda}}.
$$

[SRC-0019]

Effective sample size:

$$
\mathrm{ESS}=
\frac{(\sum_i w_i)^2}{\sum_i w_i^2}.
$$

[SRC-0016]

## Implementation consequences

Reweighting turns simulation cost into storage, energy-evaluation, and support-diagnostic cost. It is efficient only when parameter changes are small enough that the reference samples still overlap the candidate distribution. [SRC-0016] [SRC-0018]

## Caveats

ESS and KSR detect weight concentration, but high values do not guarantee that all important conformations were sampled. [SRC-0016] [SRC-0020]

## Links

- [[wiki/sources/SRC-0016-fine-tuning-mm-force-fields-to-experimental-free-energies]]
- [[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]
- [[wiki/sources/SRC-0019-mdrefine-python-package-refining-md-trajectories]]
- [[wiki/concepts/free-energy-estimation]]
- [[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]
- [[wiki/questions/force-field-training-validation-scope]]
