---
type: answer
status: active
created: 2026-07-01
updated: 2026-10-11
question: "For the next version of Garnet, could symbolic regression let the model choose the best functional for a given interaction, where would SR fit in the pipeline, and how should parameter-count mismatch and training cost be handled?"
answer_status: answered
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/machine-learning/molecular-modeling
  - research/machine-learning/scientific-modeling
  - research/molecular-simulation/free-energy
  - research/scientific-computing
tags:
  - garnet
  - symbolic-regression
  - functional-form-search
  - differentiable-simulation
  - architecture-search
related:
  - "[[wiki/concepts/garnet-functional-form-search]]"
  - "[[wiki/concepts/garnet-force-field]]"
  - "[[wiki/concepts/double-exponential-potential]]"
  - "[[wiki/concepts/symbolic-regression-interatomic-potentials]]"
  - "[[wiki/concepts/gnn-to-symbolic-regression-potentials]]"
  - "[[wiki/concepts/free-energy-reweighting-for-force-field-fine-tuning]]"
  - "[[wiki/concepts/stability-aware-mlff-training]]"
  - "[[wiki/concepts/force-field-training-from-experimental-observables]]"
sources:
  - SRC-0003
  - SRC-0014
  - SRC-0016
  - SRC-0017
  - SRC-0018
  - SRC-0021
  - SRC-0024
  - SRC-0025
  - SRC-0040
sensitivity: public
encryption: none
wiki_pages_used:
  - wiki/index.md
  - wiki/concepts/garnet-functional-form-search.md
  - wiki/concepts/garnet-force-field.md
  - wiki/concepts/double-exponential-potential.md
  - wiki/concepts/automated-force-field-training.md
  - wiki/concepts/symbolic-regression-interatomic-potentials.md
  - wiki/concepts/gnn-to-symbolic-regression-potentials.md
  - wiki/concepts/free-energy-reweighting-for-force-field-fine-tuning.md
  - wiki/concepts/stability-aware-mlff-training.md
  - wiki/concepts/force-field-training-from-experimental-observables.md
  - wiki/sources/SRC-0003-training-a-force-field-from-scratch.md
  - wiki/sources/SRC-0017-symbolic-regression-reinforcement-learning-interatomic-potentials.md
  - wiki/sources/SRC-0040-using-graph-neural-network-and-symbolic-regression-to.md
raw_sources_consulted:
  - raw/sources/SRC-0003-training-a-force-field-from-scratch.pdf
  - raw/sources/SRC-0016-fine-tuning-mm-force-fields-to-experimental-free.pdf
  - raw/sources/SRC-0017-symbolic-regression-reinforcement-learning-interatomic-potentials.pdf
  - raw/sources/SRC-0018-force-field-optimization-via-awh-gradients.pdf
  - raw/sources/SRC-0021-tuning-potential-functions-host-guest-binding-data.pdf
  - raw/sources/SRC-0024-stable-training-machine-learning-force-fields-boltzmann-estimators.pdf
  - raw/sources/SRC-0025-building-force-fields-automatic-systematic-reproducible-approach.pdf
  - raw/sources/SRC-0040-using-graph-neural-network-and-symbolic-regression-to.pdf
wiki_pages_updated:
  - wiki/concepts/garnet-functional-form-search.md
  - wiki/index.md
  - wiki/log.md
scope: timeless
---

# Symbolic Regression for Garnet Functional-Form Search

## Short answer

Symbolic regression is plausible for proposing better analytical interaction forms for Garnet, but it should not sit inside every Garnet gradient step. The clean place for SR is between a trained or partially trained Garnet model and a later Garnet retraining run:

1. Garnet creates structured evidence: residuals, local contributions, embeddings, or failure cases.
2. SR searches a constrained expression space using that evidence.
3. A small number of expressions are converted into differentiable Garnet/OpenMM terms.
4. Garnet retrains or fine-tunes those terms in the real multi-objective pipeline.
5. Expensive simulation and observable losses are used for final selection, not for raw SR exploration. [SRC-0003] [SRC-0040] [SRC-0017]

Using the whole Garnet training pipeline as the SR loss is scientifically natural, but too expensive as the primary SR search objective. It should be a late-stage evaluator for a shortlist. [SRC-0003] [SRC-0025]

## Why Garnet is a good setting

Garnet already shows that functional form matters. The paper reports that Lennard-Jones became difficult to train once simulations entered the automated pipeline, whereas the double exponential non-bonded potential trained effectively. Garnet's authors also tested multiple functional-form variants, including buffered 14-7, Lennard-Jones 6-9, Buckingham, Morse, Urey-Bradley, and alternative combination rules. Some trained, some were unstable, and some did not improve performance. [SRC-0003]

This makes Garnet an evaluator of functional forms, but not automatically a cheap discoverer of arbitrary forms. Full training with simulation data is expensive: protein NMR gradients were slow enough to be recomputed only periodically and reused across DFT batches, and full training required high memory and multi-day runtime. [SRC-0003]

## Where SR fits

SR should be used as a proposal or distillation layer, then Garnet should evaluate the selected proposals.

The key precedent is SRC-0040. That paper trains a GNN on total system energies, records edge-model outputs for atom pairs, and gives SR a table whose inputs are pair distances and whose targets are GNN edge outputs. SR is not asked to rerun the whole GNN training loop per expression. It solves a smaller supervised problem created by a model whose architecture makes edge outputs interpretable as pair contributions. [SRC-0040]

For Garnet, analogous SR inputs could be:

- Residual table: energy or force residuals after subtracting baseline Garnet.
- Contribution table: non-bonded, torsion, angle, or local correction channels exposed by Garnet.
- Failure table: short-range clashes, aromatic-planarity failures, IDP over-compaction cases, RBFE outliers, or condensed-phase failures. [SRC-0003] [SRC-0040]

## How a baseline Garnet seeds SR

A baseline Garnet should not seed SR by handing over its current parameter vector. That fails when candidate expressions have different numbers or meanings of parameters.

Instead, the baseline model seeds SR by producing supervised targets:

$$
\Delta U(x)=U_{\mathrm{ref}}(x)-U_{\mathrm{Garnet}}(x),
$$

and, when force labels are available,

$$
\Delta F_i(x)=F_{i,\mathrm{ref}}(x)-F_{i,\mathrm{Garnet}}(x).
$$

SR then fits a new expression to $\Delta U$, $\Delta F$, or a local decomposition of those residuals. This is most defensible when the residual can be localized to one interaction family, such as a radial non-bonded correction or torsion correction. [SRC-0003] [SRC-0040]

## The parameter-count issue

Parameter-count mismatch is real, but not a conceptual blocker. It means the search should be organized around expressions rather than the baseline parameter vector.

For a candidate expression

$$
U_m(x;\alpha_1,\ldots,\alpha_{k_m}),
$$

SR searches both the symbolic structure $m$ and its expression-local coefficients $\alpha$. Different candidates can have different $k_m$. SRC-0017 does this in an EAM scaffold: MCTS explores equation structure, then gradient descent optimizes continuous coefficients. [SRC-0017]

After candidate selection, Garnet has several implementation options:

- Global coefficients: the expression has a small number of global trainable coefficients, like Garnet's double-exponential global parameters $\alpha$ and $\beta$. [SRC-0003]
- Contextual coefficients: Garnet adds a readout head that maps atom, bond, angle, torsion, or pair embeddings to the coefficients required by the expression. [SRC-0003]
- Padded superset: define a maximum coefficient vector and use masks so each expression consumes only the coefficients it needs.
- Library gating: build a small library of candidate terms and let Garnet learn sparse weights or gates over them.

The highest-risk option is letting SR invent arbitrary expressions whose coefficients have no stable mapping from Garnet embeddings. The safer option is scaffolded SR: constrain the grammar so every accepted expression has a clear interface, such as radial pair input, angle input, torsion input, or local descriptor input. [SRC-0017] [SRC-0040]

## Why full Garnet loss is a late-stage evaluator

ForceBalance gives a useful analogy. It treats simulated-property fitting as an expensive objective, uses gradients and regularization, and adaptively controls simulation effort. That is an optimizer for a chosen parameterization, not a cheap evaluator for arbitrary symbolic trees. [SRC-0025]

The better design is multi-fidelity:

1. Cheap score: static energy/force residual loss on cached configurations.
2. Local score: contribution-distillation loss from Garnet internals, if the architecture exposes meaningful local targets.
3. Reweighting score: cached-trajectory estimates for small perturbations, with ESS or support diagnostics. [SRC-0016] [SRC-0018]
4. Short-simulation score: stability checks and cheap observables.
5. Full Garnet score: complete retraining and validation only for the top candidates. [SRC-0003] [SRC-0024]

Reweighting sources show how to avoid resimulating every candidate. SRC-0016 fine-tunes an espaloma charge model by Zwanzig reweighting cached hydration-free-energy trajectories and uses ESS regularization to avoid leaving the reliable trust region. SRC-0018 similarly uses frozen-bias replay rather than differentiating through online AWH updates. These methods do not solve arbitrary large functional-form jumps, but they are useful screening tools for small corrections. [SRC-0016] [SRC-0018]

## Does per-epoch SR make sense?

An epoch-by-epoch loop in which Garnet emits features, SR proposes formulas, and the model retrains is conceptually possible but operationally fragile. If the formula changes every ordinary training epoch, the loss landscape, parameter interface, optimizer state, and simulation backend may all change. That is closer to repeated architecture search than ordinary end-to-end differentiable training. [SRC-0017] [SRC-0024]

A safer version is a macro-epoch loop:

1. Train Garnet for several epochs or to a plateau.
2. Freeze or snapshot the model.
3. Export an SR dataset: embeddings, distances, angles, torsions, predicted local channels, residual energies, residual forces, and failure labels.
4. Run SR offline with a fixed grammar and complexity penalty.
5. Insert one to five candidate terms into Garnet.
6. Fine-tune with energy, force, observable, and stability losses.
7. Keep the term only if it survives transfer and simulation validation.

This is close to what SRC-0040 does in miniature: train the GNN first, create the SR dataset from edge outputs, then run SR. Garnet would need a richer decomposition than a pairwise Lennard-Jones benchmark. [SRC-0040]

## Concrete first experiment

Start with a non-bonded residual correction rather than all interactions.

Garnet already found that Lennard-Jones was unstable in the automated pipeline while double exponential and buffered 14-7 forms were trainable. The double exponential term has two per-atom parameters plus global parameters and is implementable through OpenMM custom forces, making the non-bonded radial term the best first SR testbed. [SRC-0003]

A practical experiment:

1. Train or use baseline Garnet.
2. Build a dataset of pair distances, atom embeddings, element/pair metadata, and DFT intermolecular force residuals where available.
3. Fit symbolic residual forms such as

$$
U(r,z)=U_{\mathrm{DE}}(r;\sigma,\epsilon,\alpha,\beta)+g_{\mathrm{SR}}(r,z;\alpha_1,\ldots,\alpha_k),
$$

where $g_{\mathrm{SR}}$ is constrained to be smooth, finite, cutoff-compatible, and cheap.
4. Screen candidates on static residuals and force smoothness.
5. Reweight or replay cached condensed-phase trajectories for small candidate corrections when support diagnostics remain acceptable. [SRC-0016] [SRC-0018]
6. Retrain Garnet with the top candidates.
7. Validate on held-out SPICE-like data, liquid properties, water behavior, protein stability, and RBFE targets relevant to the intended release. [SRC-0003]

This makes SR useful without requiring SR to discover the entire force field from scratch.

## Recommendation

The best near-term architecture is:

$$
\text{Garnet baseline}
\rightarrow
\text{residual or contribution dataset}
\rightarrow
\text{scaffolded SR}
\rightarrow
\text{candidate differentiable terms}
\rightarrow
\text{Garnet retraining and validation}.
$$

The full Garnet pipeline is the right final loss for selected proposals. It is the wrong loss for every raw SR proposal. Use it after cheap screening, not during symbolic search.

The idea where Garnet predicts something SR can use is promising if "something" means stable descriptors or local contribution targets, and if SR runs on a slower macro-epoch schedule. It becomes fragile if SR is asked to change the functional form every neural training epoch. [SRC-0040] [SRC-0017]

## Sources used

- [[wiki/sources/SRC-0003-training-a-force-field-from-scratch]] - Garnet functional-form experiments, double exponential details, simulation-coupled training cost, and future directions including symbolic regression.
- [[wiki/sources/SRC-0017-symbolic-regression-reinforcement-learning-interatomic-potentials]] - SR/MCTS plus gradient optimization over expression structures and coefficients.
- [[wiki/sources/SRC-0040-using-graph-neural-network-and-symbolic-regression-to]] - GNN edge-output distillation into SR pair-potential recovery.
- [[wiki/sources/SRC-0016-fine-tuning-mm-force-fields-to-experimental-free-energies]] - one-shot reweighting and ESS regularization for cheap force-field fine-tuning.
- [[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]] - frozen-bias replay as an offline optimization layer rather than differentiating through online adaptive sampling.
- [[wiki/sources/SRC-0024-stable-training-machine-learning-force-fields-boltzmann-estimators]] - simulation-stability training and the cost/underconstraint of observable losses.
- [[wiki/sources/SRC-0025-building-force-fields-automatic-systematic-reproducible-approach]] - ForceBalance as an expensive but systematic simulated-property parameter optimizer.
- [[wiki/concepts/force-field-training-from-experimental-observables]] - gradient-estimable observable fitting and validation caveats.

## Wiki pages used

- [[wiki/concepts/garnet-functional-form-search]]
- [[wiki/concepts/garnet-force-field]]
- [[wiki/concepts/double-exponential-potential]]
- [[wiki/concepts/automated-force-field-training]]
- [[wiki/concepts/symbolic-regression-interatomic-potentials]]
- [[wiki/concepts/gnn-to-symbolic-regression-potentials]]
- [[wiki/concepts/free-energy-reweighting-for-force-field-fine-tuning]]
- [[wiki/concepts/stability-aware-mlff-training]]
- [[wiki/concepts/force-field-training-from-experimental-observables]]

## Wiki updates made

- Merged the previous detailed pipeline-placement answer into this canonical answer note.
- Updated [[wiki/concepts/garnet-functional-form-search]] to link only to this canonical answer.

## Remaining gaps

- Garnet-specific implementation internals are still not represented in the wiki, so the exact software insertion point for new functional modules remains unresolved.
- The wiki does not yet contain a worked numerical prototype for residual localization, contribution extraction, or SR grammar design.
- It remains an empirical question whether Garnet's current architecture can expose meaningful local contribution targets without adding new decomposition constraints.
