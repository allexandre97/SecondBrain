---
type: question
status: active
created: 2026-09-20
updated: 2026-09-21
question_status: partially-answered
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/machine-learning/scientific-modeling
  - research/scientific-computing
tags:
  - question
  - ffrefine
  - fisher-information
  - fisher-damping
  - config
  - optimiser-constraints
  - implementation-limitations
related:
  - "[[wiki/answers/ffrefine-current-implementation-status]]"
  - "[[wiki/answers/adding-config-optimiser-to-ffrefine]]"
  - "[[wiki/answers/ffrefine-config-fisher-second-momentum]]"
  - "[[wiki/answers/ffrefine-prospective-dielectric-damped-fisher-training]]"
sources: []
sensitivity: public
encryption: none
project_evidence:
  - "FFRefine implementation audit on 2026-09-20"
  - "FFRefine damped-Fisher + ConFIG focused test rerun on 2026-09-21: 33/33 passed"
  - "FFRefine water-temperature run failed after production because WATER_TEMPERATURE_CONFIG combined :config with damped Fisher; corrected to :weighted_sum"
---

# How does FFRefine implement damped Fisher with ConFIG aggregation?

## Question

How does FFRefine implement and validate the combination of damped Fisher (`fisher_damping_gamma != nothing`) with `gradient_aggregation == :config`, including the interaction with nonzero `momentum_beta`?

## Implemented constraint

`OptimiserSettings` now accepts `fisher_damping_gamma != nothing` with `gradient_aggregation == :config`, while still requiring `momentum_beta == 0`. `fisher_factorization` uses the damped modal gains consistently in ConFIG's whitening factor. Hard-reference diagnostics compare against hard-cut ConFIG, not a weighted-sum reference, and raw/capped KL diagnostics use the selected Fisher metric and conditional metric. The earlier water configuration that selected `:config` with damped Fisher was corrected during the implementation work; the current compatibility guard is the no-momentum constraint.

Focused constructor, numerical, conditional-KL, ConFIG, hard-reference, and reporting checks are covered by `test/fisher_damping_checks.jl`. The rerun `source .env && TMPDIR=/tmp julia +1.11 --startup-file=no test/fisher_damping_checks.jl` passed 33/33; focused damped-Fisher, ConFIG, and momentum tests are also reported as passing. This is implementation evidence only.

## Why scientific validation remains open

No multi-family replay/fresh-resimulation campaign has validated the combined damped-Fisher + ConFIG method. `CLM-0040` records fresh-resimulation evidence for the damped conditional-Fisher dielectric protocol only; it is not evidence for this combined method. The implementation should therefore be treated as implemented but not scientifically or production validated.

## Remaining validation question

- Compare the combined route against the damped-Fisher `:weighted_sum` baseline under matched multi-family replay and fresh-resimulation campaigns.
- Preserve the current `momentum_beta == 0` constraint until nonzero-momentum damped-Fisher ConFIG has its own semantics and focused validation; nonzero momentum remains unsupported/open.
- Retain finite-step family guards, selected-metric KL diagnostics, and support checks in any scientific validation campaign; do not infer incompatibility from the former constructor rejection.

## Links

- [[wiki/answers/ffrefine-current-implementation-status]]
- [[wiki/answers/adding-config-optimiser-to-ffrefine]]
- [[wiki/answers/ffrefine-config-fisher-second-momentum]]
- [[wiki/answers/ffrefine-prospective-dielectric-damped-fisher-training]]
