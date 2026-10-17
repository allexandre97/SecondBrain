---
type: concept
status: needs-review
created: 2026-10-16
updated: 2026-10-16
areas:
  - research
categories:
  - research/computational-drug-discovery
  - research/molecular-simulation/free-energy
  - research/machine-learning/molecular-modeling
tags:
  - ligand-design
  - diffusion
  - alchemical-gradients
  - research-hypothesis
related:
  - "[[wiki/answers/diffusion-guided-alchemical-atom-cloud-ligand-design]]"
  - "[[wiki/concepts/garnet-force-field]]"
  - "[[wiki/concepts/boltzmann-generators-equilibrium-sampling]]"
sources:
  - SRC-0013
  - SRC-0099
  - SRC-0041
sensitivity: internal
encryption: none
---

# Alchemical Molecular Design With Optional Diffusion Guidance

## Summary

Alchemical molecular design uses physical free-energy information to explore chemical identities and connectivity, followed by evaluation of discrete molecules. Candidate mechanisms include continuous optimization, diffusion, gradient-informed discrete edits, population search, learned graph construction, and expanded-ensemble chemical sampling. They can be combined at the proposal, guidance, population, and physical-evaluation levels. The hypothesis, literature links, and provenance are documented in [[wiki/answers/diffusion-guided-alchemical-atom-cloud-ligand-design]]. Architecture selection remains open.

## Candidate workflows and composable mechanisms

- **A: no diffusion.** Sample fixed designs in complex and solvent, update relaxed chemical variables using physical gradients and explicit constraints, explore alternative graphs, and evaluate discrete endpoints. Chemical exploration and validity must be supplied without a denoiser.
- **B: alternating diffusion and molecular dynamics.** Denoise or repair a proposal, evaluate physical gradients, update it, and resume denoising. Sampling cost and whether denoising preserves favorable edits are central questions.
- **C: learned guidance.** Train a scalar affinity predictor on physical values and derivatives, use its gradients during diffusion, and acquire new physical labels in an outer loop. Label coverage and surrogate exploitation are central questions.
- **D: gradient-informed discrete search.** Use continuous derivatives to rank or sample chemically valid graph edits, then evaluate selected discrete proposals. Local derivatives may miss coordinated mutations; cloud-to-graph initialization is still required.
- **E: population annealing or sequential Monte Carlo.** Mutate, select, resample, and rejuvenate a population. This can wrap other proposal mechanisms; rigorous sampling needs correct weights and transitions, while heuristic search must not claim exactness.
- **F: generative flow-network construction.** Train a policy to construct discrete graphs toward a reward-weighted distribution. Physical gradients can supervise a reward predictor or inform actions. Cloud slots may supply spatial context, but sequential construction changes the original simultaneous-refinement picture.
- **G: expanded-ensemble chemical sampling.** Explore coordinate and chemical states in a shared sampling scheme. Predefined alchemical-state sampling has a wiki precedent in [[wiki/concepts/lambda-dynamics-with-bias-updated-gibbs-sampling]]; unrestricted graph discovery is a proposed extension. [SRC-0013]

These workflows are proposals from the linked design conversation. Direct physical feedback and learned guidance can be compared as full architectures, not only as baselines for a predetermined winner.

This is an unvalidated synthesis. Garnet demonstrates continuous parameter assignment from molecular graphs, and Boltzmann generators demonstrate learned proposals for equilibrium configurations with statistical correction. Neither source demonstrates this complete design strategy. [SRC-0099; SRC-0041]

## Shared and optional roles

1. **Chemical proposal:** direct updates in A, diffusion in B/C, gradient-ranked discrete edits in D, or a construction policy in F. E can manage populations using any of these. Highly noisy generative intermediates need not represent physical systems; physically evaluated designs do.
2. **Physical model:** a fixed graph-to-parameter rule defines interactions for each candidate. Extending Garnet from discrete graphs to fractional connectivity is additional research, not an established capability. [SRC-0099; proposed extension in the linked design note]
3. **Thermodynamic evaluation:** complex and solvent ensembles supply training labels and independent validation. Learned equilibrium proposals can help sampling only with appropriate coverage and correction. [SRC-0041]
4. **Optional learned guidance:** C requires a scalar predictor trained on physical values and derivatives; D/F may reuse one. Relative labels constrain differences and leave reference offsets to be handled explicitly. Direct physical guidance remains possible. These combinations are proposals from the linked design conversation, not results established by the cited sources.

Diffusion noise, alchemical coupling, and simulation time have different meanings. Learned affinity guidance produces a search procedure, not automatically an exact equilibrium sampler. A scalar affinity surrogate, a chemical denoiser, a force-field parameterizer, and a learned equilibrium sampler have distinct responsibilities.

## Reusable mathematical distinction

For a differentiable Hamiltonian with parameter-independent integration measure, differentiating its canonical partition function yields

$$
\nabla_\eta F=\left\langle\nabla_\eta U\right\rangle.
$$

Applying this derivation to a consistent binding cycle gives a complex-minus-solvent derivative plus any correction derivatives. The derivation and assumptions are spelled out in [[wiki/answers/diffusion-guided-alchemical-atom-cloud-ligand-design]]. It does not require differentiating through every simulation timestep, but it does require reliable equilibrium sampling.

A continuous Hamiltonian constructed by averaging identity-dependent energies generally does not have the average free energy of the discrete molecules. This follows from the nonlinear partition-function expression. Therefore continuous improvement, chemical validity, and endpoint affinity are separate validation questions; a proposal must be discretized and independently evaluated.

## Open questions

- Can local identity gradients guide coordinated graph edits that retain improvement after discretization?
- Can a soft graph-to-parameter extension preserve exact endpoint behavior while giving useful intermediate gradients?
- Does learned denoising preserve beneficial physical edits or systematically erase them?
- Can a scalar predictor learn useful chemical derivatives from noisy physical labels, and can uncertainty-aware acquisition limit surrogate exploitation?
- Does derivative supervision improve physically validated endpoints over value-only guidance at matched total cost?
- Can the combined method outperform unguided generation and simpler search at matched total cost?
- Should gradients update relaxed molecules, rank discrete edits, or train a generator's guidance model?
- Which compatible proposal, guidance, population, and sampling choices best balance validity, reliability, diversity, and total cost?

These are research questions originating in the linked design conversation, not conclusions of the cited literature. Do not cite this page as evidence of demonstrated ligand-design performance.

## Links

- [[wiki/concepts/lambda-dynamics-with-bias-updated-gibbs-sampling]] — predefined chemical-state sampling precedent and limits. [SRC-0013]

- [[wiki/answers/diffusion-guided-alchemical-atom-cloud-ligand-design]] — full proposal, provenance, equations, milestones, and unresolved implementation decisions.
- [[wiki/concepts/garnet-force-field]] — continuous typing foundation. [SRC-0099]
- [[wiki/concepts/boltzmann-generators-equilibrium-sampling]] — sampling and correction foundation. [SRC-0041]
