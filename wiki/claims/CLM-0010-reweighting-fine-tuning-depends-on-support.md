---
type: claim
status: active
created: 2026-07-01
updated: 2026-07-01
claim_status: limited
claim_scope: cross-source
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/molecular-simulation/free-energy
tags:
  - claim
  - reweighting
  - effective-sample-size
related:
  - "[[wiki/concepts/free-energy-reweighting-for-force-field-fine-tuning]]"
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
  - "[[wiki/questions/force-field-training-validation-scope]]"
sources:
  - SRC-0016
  - SRC-0018
  - SRC-0019
  - SRC-0020
sensitivity: public
encryption: none
---

# Reweighting Fine-Tuning Depends on Support

## Claim

Reweighting-based force-field fine-tuning is efficient only when the reference ensemble has enough support for the candidate parameter change, so ESS, KSR, parity, or split-half diagnostics are part of the method rather than optional reporting. [SRC-0016] [SRC-0018] [SRC-0019] [SRC-0020]

## Scope

This claim covers Zwanzig hydration-free-energy fine-tuning, AWH frozen-bias replay, and MDRefine-style ensemble or force-field refinement. It does not claim that a single diagnostic is sufficient for every system. [SRC-0016] [SRC-0018] [SRC-0019]

## Evidence

- SRC-0016 uses ESS regularization to keep one-shot charge fine-tuning within the support of the original simulations. [SRC-0016]
- SRC-0018 uses frozen-bias replay with ESS and parity checks before trusting force-field optimization steps. [SRC-0018]
- SRC-0019 and SRC-0020 frame ensemble, force-field, and forward-model refinement through reweighting and regularized maximum-entropy logic. [SRC-0019] [SRC-0020]

## Caveats

- A high ESS or KSR does not prove that all important conformations were sampled; it mainly detects weight collapse among available samples. [SRC-0016] [SRC-0020]

## Links

- [[wiki/sources/SRC-0016-fine-tuning-mm-force-fields-to-experimental-free-energies]]
- [[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]
- [[wiki/sources/SRC-0019-mdrefine-python-package-refining-md-trajectories]]
- [[wiki/sources/SRC-0020-mdrefine-supplementary-material]]
- [[wiki/concepts/free-energy-reweighting-for-force-field-fine-tuning]]
- [[wiki/questions/force-field-training-validation-scope]]
