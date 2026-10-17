---
type: answer
status: needs-review
created: 2026-10-16
updated: 2026-10-16
question: "Which combination of chemical proposals, physical or learned guidance, population management, and alchemical sampling best fits atom-cloud ligand design?"
answer_status: partially-answered
areas:
  - research
categories:
  - research/computational-drug-discovery
  - research/molecular-simulation/free-energy
  - research/molecular-simulation/force-fields
  - research/machine-learning/molecular-modeling
tags:
  - research-proposal
  - ligand-design
  - atom-cloud
  - diffusion
  - alchemical-gradients
  - garnet
related:
  - "[[wiki/concepts/diffusion-guided-alchemical-molecular-design]]"
  - "[[wiki/concepts/garnet-force-field]]"
  - "[[wiki/concepts/boltzmann-generators-equilibrium-sampling]]"
  - "[[wiki/answers/ffrefine-step15-enzyme-struct-layout-gradient-loss]]"
sources:
  - SRC-0013
  - SRC-0099
  - SRC-0041
sensitivity: internal
encryption: none
wiki_pages_used:
  - "[[wiki/concepts/lambda-dynamics-with-bias-updated-gibbs-sampling]]"
  - "[[wiki/concepts/garnet-force-field]]"
  - "[[wiki/sources/SRC-0099-training-force-field-proteins-small-molecules]]"
  - "[[wiki/sources/SRC-0041-boltzmann-generators-sampling-equilibrium-states-of-many-body]]"
  - "[[wiki/answers/ffrefine-step15-enzyme-struct-layout-gradient-loss]]"
raw_sources_consulted: []
wiki_pages_updated:
  - "[[wiki/concepts/diffusion-guided-alchemical-molecular-design]]"
project_evidence:
  - "2026-10-16: Architecture expansion requested by the user after discussion of gradient-informed discrete search, population annealing/sequential Monte Carlo, generative flow networks, and expanded-ensemble chemical sampling. Preserve A/B/C and record new candidates and compatible combinations; no architecture selected."
  - "2026-10-16: Latest clarification: the user requested that all three considered architectures remain represented as live alternatives: no diffusion, alternating diffusion and molecular dynamics, and learned guidance. Architecture selection is open; the earlier preference for learned guidance is exploratory rather than a final decision."
  - "2026-10-16: Follow-up design decision: the user explicitly preferred learned guidance over alternating physical simulation and denoising steps, and requested revision of the notes. Molecular-dynamics free energies and identity/connectivity gradients are training signals for a guidance predictor; simulations remain in an outer data-acquisition and validation loop."
  - "2026-10-16: User–assistant research-design conversation in SecondBrain. The user originated the atom-cloud proposal, explicitly preferred speculative exploration over restricting the project to scaffold substitutions, proposed atom-identity/absence weights and continuous typing, and selected diffusion sampling guided by molecular dynamics and identity gradients as the direction to record. No implementation or experimental results were presented."
scope: living
currency: current
as_of: 2026-10-16
---

# Alchemical Atom-Cloud Ligand Design: Candidate Architectures and Build Plan

## Short answer

Explore ligand design from an overlapping cloud of candidate atom slots using gradients with respect to relaxed atom identities, occupancies, and connectivity. Preserve three original architectures: direct physical-gradient optimization without diffusion (A), alternating diffusion and physical evaluation (B), and learned diffusion guidance (C). Also consider gradient-informed discrete search (D), population annealing or sequential Monte Carlo (E), generative flow-network construction (F), and expanded-ensemble chemical sampling (G). These are partly composable mechanisms, not seven mutually exclusive systems. All require consistent complex/solvent thermodynamics and independently evaluated discrete endpoints. No architecture has been selected. [Project evidence: 2026-10-16 architecture expansion]

This is an exploratory project specification, not a validated algorithm. Its shared hypothesis is that local alchemical gradients can help discover favorable discrete ligands. Whether diffusion improves chemical exploration, and whether a learned guidance model is worth its training cost and approximation error, are separate hypotheses to compare. Global convergence, chemical validity, physical accuracy, and computational advantage remain unproven. The existing file path is retained for link stability; diffusion is optional in the design space. [Project evidence: 2026-10-16 design conversation and latest clarification]

## Provenance and reading guide

The proposal and accepted direction originate in the conversation identified in `project_evidence`. Equations labeled as proposed constructions are design definitions or derivations recorded here, not claims that a cited paper implements this pipeline. Garnet supplies evidence for continuous parameter assignment from molecular graphs; Boltzmann generators supply evidence for learned equilibrium proposals and statistical correction. Neither establishes the complete proposed design. [SRC-0099; SRC-0041]

External papers discussed during the conversation are linked in the evidence section without assigning invented source IDs. They have not been ingested by this task. This note uses existing wiki summaries and the conversation; it does not alter raw material. The unpublished proposal is conservatively marked `internal`; this is storage metadata, not a claim of confidentiality made by the user.

The main sections move from the agreed objective to the representation, Hamiltonian, sampling loop, validation plan, and outstanding decisions. The companion [[wiki/concepts/diffusion-guided-alchemical-molecular-design]] provides a shorter retrieval entry point.

## Agreed direction and provisional choices

| Item | Position | Status |
| --- | --- | --- |
| Scientific objective | Find discrete ligands with favorable binding free energy under a fixed force-field model, then assess predictive value independently. | User's objective |
| Starting representation | A maximum of $N$ overlapping atom slots with alternative identities and an absent state. | Explicit user preference |
| Shared search principle | Use molecular-dynamics free-energy information and gradients with respect to relaxed chemical choices. | Shared research objective |
| Architecture A | Optimize the cloud directly using physical gradients, without diffusion. | Live candidate |
| Architecture B | Alternate diffusion proposals/repair and physical-gradient evaluation. | Live candidate |
| Architecture C | Guide diffusion using a predictor trained on physical values and derivatives; acquire labels in an outer loop. | Live candidate; earlier preference is not a final selection |
| Candidate D | Use continuous identity gradients to propose discrete chemical edits. | Additional candidate |
| Candidate E | Manage a population through mutation, selection, and annealing, optionally with rigorous sequential Monte Carlo weights. | Composable outer search framework |
| Candidate F | Learn a generative flow-network policy for constructing discrete molecular graphs. | Additional proposal architecture |
| Candidate G | Sample chemical states and coordinates in expanded ensembles, retaining consistent complex/solvent estimates. | Additional sampling architecture or evaluation engine |
| Molecular connectivity | Represent and modify bonds, allowing molecule construction rather than only fixed-scaffold substitutions. | Necessary proposed component |
| Continuous typing | Investigate a frozen Garnet-derived graph-to-parameter model. | Discussed candidate, not a confirmed dependency |
| Physical sampling | Begin with conventional molecular dynamics; consider learned equilibrium proposals later. | Assistant recommendation |
| Search population | Maintain several clouds and stochastic branches rather than one irreversible trajectory. | Assistant recommendation |
| Software and target | No implementation language, target protein, dataset, pretrained diffusion checkpoint, or compute budget selected. | Open |

The original analogy was FFRefine: replace force-field fitting with optimization of the molecule under a fixed parameterization rule. This is a design analogy, not an assertion that FFRefine already supports this workflow. Restricting the entire project to known-scaffold substitutions was explicitly not the user's preferred direction; such systems may still serve as controlled validation fixtures. [Project evidence: 2026-10-16 design conversation]

## Objective and physical assumptions

The initial scope is reversible, noncovalent binding at specified temperature, pressure or volume, solvent conditions, and protonation conventions. More negative standard binding free energy means stronger equilibrium binding under those conditions. Covalent reactions, unknown protonation equilibria, and unrestricted charge changes are outside the recommended first implementation; these are proposed scope limits, not permanently excluded capabilities.

Use a design objective of the form

$$
\mathcal J(\eta)=\Delta G_{\mathrm{bind}}(\eta)
+\lambda_{\mathrm{chem}}R_{\mathrm{chem}}(\eta)
+\lambda_{\mathrm{conn}}R_{\mathrm{conn}}(\eta)
+\lambda_{\mathrm{size}}R_{\mathrm{size}}(\eta).
$$

Here $\eta$ contains relaxed chemical choices. The regularizers are explicit design preferences for chemistry, connectivity, and size; they are not physical free-energy terms. Their forms and strengths remain to be chosen. Affinity alone is not a complete drug-design objective: selectivity, solubility, synthesis, and other properties can be added later, but their addition changes the optimization problem.

Coordinates used to propose a pose are distinct from coordinates sampled in the equilibrium ensemble. Optimizing one pose's potential energy does not substitute for integrating over configurations. Protein rearrangement, hydration, and the unbound ligand's conformational preferences must enter through the physical ensembles.

## State representation and notation

Represent one cloud by $Y=(R,P,B)$, with a fixed maximum number of slots:

| Symbol | Meaning |
| --- | --- |
| $N$ | Maximum number of atom slots, including potentially absent atoms |
| $M$ | Number of allowed identity labels, excluding absence |
| $R\in\mathbb R^{N\times3}$ | Proposal coordinates; one coordinate per slot |
| $z_{im}$ | Trainable identity logit for slot $i$ and label $m$ |
| $P\in[0,1]^{N\times(M+1)}$ | Relaxed identities; label zero denotes absence |
| $a_i$ | Occupancy of slot $i$ |
| $B_{ij,k}$ | Symmetric bond-state weights, including no bond |
| $c_{ij}$ | Bond-presence weight conditional on both atoms existing |
| $\eta$ | Independent design variables, such as identity and bond logits |
| $x$ | Physical configuration of ligand and sampled environment |
| $\Phi(\eta)$ | Force-field parameters assigned to the proposed design |
| $\tau$ | Identity or bond softmax temperature; not physical temperature |
| $\beta$ | Physical inverse thermal energy, with units consistent with the energy convention |

The proposed identity relaxation is

$$
p_{im}=\frac{\exp(z_{im}/\tau)}{\sum_{n=0}^{M}\exp(z_{in}/\tau)},
\qquad a_i=1-p_{i0},
\qquad N_{\mathrm{eff}}=\sum_i a_i.
$$

With a conventional force field, identities might be supported chemical atom states. With a Garnet-derived model, element and chemical-state features are more natural than enumerating manually assigned force-field types. The allowed element set, hydrogen representation, formal-charge states, aromaticity representation, and size prior need explicit decisions.

One coordinate shared by the alternative identities avoids storing $M$ separate particles per slot. Initialize overlapping but nonidentical coordinates; exact coincidence can create undefined angular geometry and symmetry that prevents separation. In a diffusion-first implementation, highly corrupted states need only be valid generative inputs, not physical molecular systems.

Absence must consistently remove physical interactions, graph messages, charge participation, and bonded terms. It is not enough to multiply nonbonded energy by occupancy. Retained ghost coordinates require a defined reference measure, discussed below.

## Relaxed identities are a computational Hamiltonian

For illustration, a pairwise relaxation can be defined as

$$
U_{ij}=\sum_{m=1}^{M}\sum_{n=1}^{M}p_{im}p_{jn}V_{mn}(r_{ij}).
$$

The absent state has zero pair interactions. Actual implementation additionally requires soft-core treatment, graph-dependent exclusions, charges, and bonded interactions. These weights define an interpolation, not necessarily probabilities whose averages equal the free energies of physical molecules.

To see the distinction, let $s$ denote a discrete chemical assignment and define $\bar U(x;P)=\mathbb E_{s\sim P}[U(x;s)]$. Then, in general,

$$
-\beta^{-1}\log\int e^{-\beta\bar U(x;P)}dx
\ne
\mathbb E_{s\sim P}\left[-\beta^{-1}\log\int e^{-\beta U(x;s)}dx\right].
$$

This follows from the nonlinear exponential and logarithm; it is a mathematical warning about the proposed relaxation. A fractional optimum can exploit interactions unavailable to any endpoint. Different interpolations can give different intermediate gradients even if they agree on all physical endpoints. Therefore endpoint projection, reparameterization, and independent evaluation are integral parts of the method, not optional final cleanup.

## Garnet-derived continuous parameter assignment

Garnet predicts molecular mechanics parameters from continuous graph embeddings, including bonded and nonbonded terms. Its established input is a molecular topology; continuous embeddings do not demonstrate valid behavior for fractional connectivity or absent atoms. [SRC-0099, Methods; [[wiki/concepts/garnet-force-field]]]

The proposed extension freezes the learned weights and computes

$$
h=f_\theta(P,B),\qquad \Phi=g_\theta(h,P,B),
$$

where $\theta$ denotes frozen network weights. The project optimizes graph inputs, not $\theta$ or arbitrary free embeddings. Parameters remain fixed during a sampling block and are reassigned when the design changes.

Required extension work includes soft element features, weighted message passing, smooth representations of chemical attributes, occupancy-aware charge assignment, and permutation-consistent interaction heads. A schematic message is

$$
m_i=\sum_{j\ne i}a_jc_{ij}\,\psi(h_i,h_j).
$$

Its normalization must be designed to recover the original network at discrete endpoints. This schematic is not a drop-in replacement for Garnet's actual aggregation. Aromaticity, degree features, formal-charge processing, and connected-component handling can contain discrete operations and need an explicit relaxation or an outer discrete update.

The first requirement is exact or tolerance-controlled agreement with unmodified parameter assignment on supported discrete molecules, including padding with absent slots. Fractional inputs are outside the established validation domain. Any retraining or calibration of the extension must be a separate, documented model-development step, not hidden force-field fitting inside the ligand search.

## Bonds, angles, torsions, and exclusions

### Interaction existence follows the graph

Proposed gates for distinct atom indices are

$$
w^{\mathrm{bond}}_{ij}=a_i a_jc_{ij},
$$

$$
w^{\mathrm{angle}}_{ijk}=a_i a_j a_kc_{ij}c_{jk},
$$

$$
w^{\mathrm{proper}}_{ijkl}=a_i a_j a_k a_lc_{ij}c_{jk}c_{kl}.
$$

For an improper centered at $j$ with three neighbors,

$$
w^{\mathrm{improper}}_{ijkl}=a_i a_j a_k a_lc_{ji}c_{jk}c_{jl}.
$$

Each occupancy appears once; multiplying already occupancy-weighted bond gates would introduce unwanted extra powers. These products are proposed continuous gates, not exact joint probabilities for correlated chemical choices. Improper eligibility and multiplicity must follow the selected endpoint force field; every degree-three center should not automatically receive an arbitrary improper.

### Interaction strength follows the chemical environment

Garnet supplies harmonic bond/angle forms and periodic proper/improper torsion forms with learned parameters. [SRC-0099, Methods]

The proposed gated angle and torsion energies are

$$
U_{\mathrm{angle}}=\sum_{(i,j,k)}w^{\mathrm{angle}}_{ijk}
\frac{k_{ijk}}{2}(\theta_{ijk}-\theta^0_{ijk})^2,
$$

$$
U_{\mathrm{proper}}=\sum_{(i,j,k,l)}w^{\mathrm{proper}}_{ijkl}
\sum_n K_{ijkl,n}[1+\cos(n\phi_{ijkl}-\delta_n)].
$$

Use the endpoint model's symmetry and counting conventions. Do not independently optimize angle and torsion stiffness merely to remove strain; derive parameters through the frozen chemical assignment model.

### Geometry and exclusions are coupled implementation problems

Zero-length bonds and collapsed planes make angular coordinates undefined. A zero gate multiplied by an undefined value does not produce a safe zero. Use a generative geometry-repair stage before physical sampling, and, if necessary, smooth regularized angular computations for intermediate states. Restore and test ordinary endpoint behavior. Small products of bond weights can also suppress torsion gradients; initializing a huge number of almost-zero edges may provide little chemical guidance.

Bond formation changes nonbonded exclusions and three-bond interaction scaling. The same relaxed graph must govern these changes. Rings introduce multiple paths between atom pairs, so a naive sum of soft path counts is not an exclusion probability. Deriving a smooth rule that reproduces the exact discrete conventions is a prerequisite for interpretable design gradients.

## Thermodynamic objective and design derivatives

For a parameter-independent configuration measure at fixed temperature, define

$$
Z_e(\eta)=\int e^{-\beta U_e(x;\eta)}dx,
\qquad F_e(\eta)=-\beta^{-1}\log Z_e(\eta).
$$

Differentiating under the integral gives

$$
\nabla_\eta F_e=\left\langle\nabla_\eta U_e\right\rangle_e.
$$

This is a derivation from the stated canonical partition function, not a new empirical claim. A pressure ensemble requires the corresponding measure and Hamiltonian conventions. Parameter-dependent constraints, masses, coordinate transformations, restraints, or state definitions require their additional contributions; they cannot silently be omitted.

For a consistent binding cycle with fixed receptor contribution,

$$
\nabla_\eta\Delta G_{\mathrm{bind}}
=\left\langle\nabla_\eta U_{\mathrm{complex}}\right\rangle
-\left\langle\nabla_\eta U_{\mathrm{solvent}}\right\rangle
+\nabla_\eta C.
$$

$C$ collects the corrections required by the chosen cycle, such as restraint and standard-state terms. This expression provides a local derivative; it does not automatically provide an absolute binding free energy. Relative endpoint comparisons require a reference and a valid free-energy estimator. The solvent leg contains the ligand in solvent, not solvent alone. Bound-state definitions and restraint policies must remain consistent as the design changes.

Differentiate both explicit topology gates and assigned parameters:

$$
\frac{dU}{d\eta}=\left.\frac{\partial U}{\partial\eta}\right|_\Phi
+\frac{\partial U}{\partial\Phi}\frac{\partial\Phi}{\partial\eta}.
$$

For identity logits,

$$
\nabla_z\Delta G_{\mathrm{bind}}
=\left(\frac{\partial P}{\partial z}\right)^{\mathsf T}
\nabla_P\Delta G_{\mathrm{bind}}.
$$

The equilibrium identity means that energy derivatives can be computed on sampled configurations without backpropagating through the entire molecular-dynamics history. This does not remove equilibration requirements. Differentiate the Hamiltonian at fixed sampled coordinates, then average under the appropriate ensemble; do not confuse this with differentiating an arbitrary finite-trajectory observable.

### Ghost atoms, charge, and association

Retained absent coordinates contribute a phase-space measure. Choose normalized ghost reference distributions or rigorously cancelling restraint/reference factors in both legs. Verify that adding unused slots does not change endpoint binding differences. A disconnected cloud is not automatically one ligand: translational entropy and association conventions differ until a connected endpoint and its reference state are defined.

The initial prototype should use a fixed net-charge convention and explicit hydrogen/protonation handling. Absence must not leave charge behind or allow ghost atoms to absorb the charge-normalization correction. Variable atom counts also introduce multiple equivalent slot assignments; treat permutation symmetry and size priors explicitly if assigning probabilities over designs.

## Diffusion sampling as an optional chemical proposal mechanism

This section applies to architectures B and C. Architecture A uses explicit chemical constraints and non-diffusion exploration instead. A pretrained diffusion model is therefore not a shared prerequisite.

The desired denoiser is conditioned on the pocket and jointly updates coordinates, identities, occupancy, and bond states. It should be permutation-equivariant over slots and respect rotations/translations; chirality handling must be explicit. Chemical dependencies should be learned jointly rather than treating every identity and bond as an unrelated categorical decision. This is a proposed architecture informed by the external molecular-diffusion precedents listed below.

Very noisy clouds are generative intermediates. The denoiser should establish sufficient geometry and connectivity before a relaxed Hamiltonian is physically sampled. Choose a readiness gate based on valid numerical geometry, bounded forces, usable chemical features, and defined reference states. Thresholds must be calibrated; none are selected here.

| Quantity | Meaning | What it must not be confused with |
| --- | --- | --- |
| Diffusion noise level | Corruption or uncertainty in a generative state | Physical elapsed time |
| Alchemical coupling | A parameter selecting an intermediate Hamiltonian | Automatically the diffusion schedule |
| Molecular-dynamics time | Sampling evolution under a fixed Hamiltonian | Progress toward a better molecule |
| Softmax temperature | Sharpness of identity or bond selection | Thermostat temperature |

Initially use deterministic softmax guidance. Optional Gumbel-softmax noise can create stochastic identity or bond proposals between design iterations. Hold the selected Hamiltonian fixed during each equilibrium block. Straight-through hard selections supply biased derivative estimators and should be benchmarked as an explicit alternative. Annealing too quickly can saturate logits and prevent rejected choices from recovering.

A denoiser can reverse a physically useful edit; a strong free-energy update can leave the denoiser's learned chemistry domain. Log both effects. Use small updates, partial re-noising, branching, and endpoint evaluations to study the tradeoff. Guidance through a predicted clean structure at a noisy time is an optimization heuristic unless the corresponding conditional diffusion guidance has been derived. It is not automatically exact sampling from an affinity-weighted target.

## Architecture comparison and selection status

The original three designs remain under consideration alongside D–G below. The user explored learned guidance as a streamlined option and subsequently clarified that the choice remains open. The following table preserves the original A/B/C comparison; additional mechanisms are compared separately because some operate at different levels. All tradeoffs are engineering hypotheses to test, not measured advantages. [Project evidence: 2026-10-16 clarification and architecture expansion]

| Dimension | A: no diffusion | B: alternating diffusion and physical evaluation | C: learned diffusion guidance |
| --- | --- | --- | --- |
| Chemical search | Direct relaxed-variable updates, constraints, and optional stochastic mutations | Denoising proposes/repairs coordinated changes around physical updates | Denoising is steered by an inexpensive learned predictor |
| Source of guidance | Fresh or validly reweighted physical ensemble gradients | Physical ensemble gradients between denoising segments | Derivatives of a predictor fitted to physical values and gradients |
| Simulation placement | Within optimization iterations | Between selected diffusion/proposal stages | Outside individual generation trajectories, in acquisition/validation batches |
| Additional learned models | None required beyond an optional continuous force-field parameterizer | Chemical diffusion model | Chemical diffusion model plus affinity-guidance predictor |
| Potential benefit | Direct connection to the physical objective; fewer learned components | Coordinated chemical proposals with direct physical feedback | Cheap repeated guidance and reuse of accumulated physical labels |
| Main additional risk | Difficult graph exploration and chemical validity; many local physical evaluations | Sampling latency and denoiser reversal of favorable edits | Surrogate exploitation, label coverage, and training overhead |
| Main comparison question | Are explicit constraints and stochastic exploration enough? | Does diffusion improve endpoint discovery enough to justify its cost? | Does amortized guidance repay its data cost without losing physical reliability? |

The original three retain the shared difficulties of fractional-state exploitation, graph-dependent exclusions, ghost reference states, and noisy equilibrium gradients. None is merely a fallback or a mandatory stepping stone to another. A shared physics implementation can support comparisons without committing to a production architecture.

## Architecture A: direct optimization without diffusion

1. Initialize a population of atom clouds and relaxed candidate graphs with an explicit occupancy and chemical-state prior.
2. Use geometric regularization, bounded interactions, and chemical constraints to produce numerically sampleable designs. Unlike a purely generative noisy state, each physically evaluated cloud must have a defined Hamiltonian and reference measure.
3. Hold each design fixed and sample complex and solvent ensembles. Estimate the physical design gradient and its uncertainty.
4. Take a bounded update in identity/bond logits, combined with explicit chemical-validity, connectivity, and size regularizers. Coordinate sampling remains distinct from chemical optimization.
5. Explore with multiple starts, temperature schedules, Gumbel proposals, or discrete graph mutations if useful; none requires a diffusion model. Refresh sampling after meaningful Hamiltonian changes.
6. Periodically discretize, check chemical validity, reparameterize, and independently evaluate endpoint molecules. Retain useful branches and stop under a declared budget.

A schematic update is

$$
\eta_{k+1}=\Pi_{\mathcal C}\left[\eta_k-\alpha_k\left(\widehat{\nabla_\eta\Delta G_{\mathrm{bind}}}+\nabla_\eta R\right)\right],
$$

where $R$ collects design penalties and $\Pi_{\mathcal C}$ enforces the selected feasible relaxed constraints. This is a proposed update rule, not a claim that a tractable projection onto all valid molecules exists. Projection may erase improvements and must be assessed. The key open problem is whether local gradients plus explicit chemical exploration can construct useful connected molecules from the cloud.

## Architecture B: alternating diffusion and molecular dynamics

1. Initialize clouds and partially denoise them into coherent candidate geometries and graphs.
2. At selected checkpoints, freeze the relaxed design and sample complex and solvent ensembles with consistent chemistry and reference conventions.
3. Estimate physical free-energy gradients, take a small chemical update, and assess uncertainty or overlap before reusing any trajectory information.
4. Resume denoising, apply a repair step, or partially re-noise and branch around the update. Record whether the denoiser preserves the physically favorable direction.
5. Repeat physical evaluation when the design changes, then discretize and independently evaluate endpoints.

This is the previously considered alternating architecture, preserved as a complete candidate rather than only a diagnostic baseline. The denoiser supplies coordinated chemical changes; the physical estimator provides direct feedback without a learned affinity predictor. Physical sampling need not occur at every diffusion timestep. Checkpoint frequency, step size, and repair strength remain open choices.

Its central risk is that physical updates become obsolete after denoising, or denoising reverses them. Measure actual endpoint benefit per total simulation and generation cost. This procedure is an optimization heuristic, not automatically an exact equilibrium or affinity-weighted sampler.

## Architecture C: learned diffusion guidance

In this candidate, physical free-energy values assess which designs are better and physical derivatives teach how affinity changes locally. Both train one scalar predictor, whose derivatives guide diffusion without a simulation call at each denoising step. The equations and training choices below are proposed implementation details, not validated results. This candidate remains attractive for streamlined generation, but it is not selected over A or B. [Project evidence: 2026-10-16 latest clarification]

### Scalar predictor trained on values and derivatives

Let $\widehat{\Delta G}_\psi(\eta,\mathcal P)$ predict binding free energy for relaxed design $\eta$ and pocket $\mathcal P$, with thermodynamic conditions fixed or explicitly supplied. Its gradient is obtained by differentiating this scalar function rather than training an unrelated vector field.

For comparable absolute labels $\widehat{\Delta G}_j$ and physical derivative labels $\hat g_j$, a proposed loss is

$$
\mathcal L(\psi)=
\sum_j w_j\left[\widehat{\Delta G}_\psi(\eta_j,\mathcal P_j)-\widehat{\Delta G}_j\right]^2
+\lambda\sum_j\left\|\nabla_\eta\widehat{\Delta G}_\psi(\eta_j,\mathcal P_j)-\hat g_j\right\|_{W_j}^2.
$$

Here $\|v\|_{W}^2=v^{\mathsf T}Wv$. Weights should reflect label uncertainty, correlations where estimable, and the scales of different design coordinates. Cap or regularize uncertainty weights; a spuriously small error estimate must not dominate training. Missing values or derivative components can be masked rather than invented. Training on derivatives requires differentiation of input derivatives with respect to model parameters, so smoothness, memory, and training cost need explicit checks.

For relative free-energy labels, replace the absolute-value residual by

$$
\widehat{\Delta G}_\psi(\eta_b,\mathcal P)
-\widehat{\Delta G}_\psi(\eta_a,\mathcal P)
-\widehat{\Delta\Delta G}_{a\to b}.
$$

Relative labels leave an additive offset undetermined within each unanchored reference network; gradients do not fix it. Preserve the reference network and do not interpret arbitrary offsets as absolute affinities across pockets. Free-energy values require a thermodynamic estimator; an ordinary short trajectory does not automatically supply a value merely because energy derivatives are available.

All derivative labels must use the same interpolation, independent coordinates, and units as the predictor. Prefer derivatives in a declared logit or independent-simplex coordinate system; do not confuse constrained identity derivatives with arbitrary unconstrained components. Include valid relaxed states in the training domain, since endpoint-only accuracy does not establish useful gradients between molecules. Record uncertainty and sampling conditions alongside every label.

### Guidance through predicted clean designs

A proposed first implementation uses the denoiser's predicted clean structure:

$$
\hat\eta_0=D_\theta(Y_t,t,\mathcal P),
\qquad
g_t=\nabla_{Y_t}\widehat{\Delta G}_\psi\left(D_\theta(Y_t,t,\mathcal P),\mathcal P\right).
$$

The diffusion sampler incorporates the direction $-g_t$ using a sampler-specific update and a noise-dependent guidance strength. This expression differentiates through the clean prediction; hard decoding or graph sanitization cannot be silently inserted into that path. Molecular-dynamics labels supervise chemical-design derivatives, not instantaneous pose forces or arbitrary derivatives of equilibrium free energy with respect to a starting coordinate. Coordinate guidance induced through the denoiser must be assessed separately.

Begin with reduced or disabled guidance at noise levels or predicted structures outside the predictor's validated domain. Estimate model uncertainty and calibrate it on held-out physical evaluations. Uncertainty estimates are diagnostics, not guarantees against extrapolation. Freeze model versions during each generation batch for reproducibility.

Training a noise-conditioned predictor directly is an alternative still to be selected. Its labels must represent the intended conditional clean-design objective at each noise level; evaluating a molecular force field on corrupted inputs is not an equivalent target. Neither clean-prediction guidance nor a generic noise-conditioned surrogate automatically yields exact sampling from an affinity-weighted distribution.

### Generation and outer physical-learning loop

1. Bootstrap a dataset from chemically valid seeds and selected numerically valid relaxed designs, using unguided generation or an existing dataset plus new physical evaluations. A pretrained chemistry denoiser does not itself provide binding-free-energy labels.
2. For selected fixed designs, construct consistent complex and solvent Hamiltonians, equilibrate replicas, and estimate values or differences, design derivatives, and uncertainties.
3. Train and validate the scalar guidance predictor with both label types. Split by molecular family or generation ancestry where appropriate to avoid treating near-duplicate relaxed samples as independent generalization tests.
4. Generate a population of clouds with learned guidance throughout denoising. No physical simulation is required inside each denoising trajectory.
5. Select a mixture of promising, diverse, uncertain, and coverage-improving candidates for new physical evaluations. Restrict relaxed candidates to the physical-readiness domain; evaluate discrete endpoints with their ordinary parameterization.
6. Add the new labels, recalibrate uncertainty, update the predictor, and generate another batch. Physical evaluation remains the authority when predictions disagree.
7. Stop under a declared total compute budget or lack of independently validated endpoint improvement. Keep final assessment independent of the labels used to fit or select the winning candidates.

Architectures A and B provide meaningful comparisons for separating surrogate errors from failures of the physical relaxation, while remaining viable designs themselves. Learned guidance, learned equilibrium sampling, and force-field parameter assignment are separate models with separate validation requirements.

## Candidate D: gradient-informed discrete chemical search

Use continuous identity derivatives to propose edits between discrete molecules rather than keeping the design fractional throughout optimization. For a candidate edit represented by $\delta\eta$, the first-order ranking is

$$
\Delta G_{\mathrm{bind}}(\eta+\delta\eta)-\Delta G_{\mathrm{bind}}(\eta)
\approx\nabla_\eta\Delta G_{\mathrm{bind}}^{\mathsf T}\delta\eta.
$$

The approximation is a local proposal score, not a reliable free-energy prediction for an arbitrary finite mutation. Gradient-directed molecular design has direct precedent in [gradient-directed Monte Carlo](https://arxiv.org/abs/0807.2429); [Gibbs with Gradients](https://proceedings.mlr.press/v139/grathwohl21a.html) provides a general gradient-informed discrete proposal framework. Applying these ideas to the present binding-free-energy cloud problem is a proposed extension.

1. Convert an initialized cloud into one or more coherent discrete candidate graphs, preserving alternative constructions where possible.
2. Obtain physical design gradients or derivatives from a validated affinity predictor.
3. Generate allowed local graph edits: identity changes, activating/removing slots, changing bonds, or coordinated rewrites with consistent valence and charge.
4. Rank or sample these edits using gradient-based scores while preserving exploratory proposals.
5. Evaluate selected endpoints physically, update the search state or population, and repeat.

Unlike A, this candidate uses derivatives primarily to choose discrete edits rather than to descend through an extended fractional design trajectory. Alchemical intermediates can still be required for derivatives and physical comparisons. A graph-edit grammar can improve endpoint validity, but coordinated changes and ring formation may be poorly predicted by a local linear score. Occasional larger moves and multiple starts are possible remedies to test.

The cloud-to-graph initialization remains a research component; this method does not by itself solve the original unconnected-cloud problem. An exact Monte Carlo interpretation also requires correct forward/reverse proposal probabilities and suitable acceptance estimators. Plugging noisy free-energy estimates into ordinary acceptance ratios is not automatically exact. Begin by describing any uncorrected variant as stochastic optimization.

## Candidate E: population annealing and sequential Monte Carlo over designs

Maintain a population of clouds or molecules that can represent incompatible atom counts, ring closures, and poses. A proposed annealed target over designs is

$$
\pi_t(\eta)\propto p_0(\eta)\exp[-\gamma_t J(\eta)],
$$

where $p_0$ is a chemical prior, $J$ is a declared design objective, and $\gamma_t$ increases selection pressure. This is an optimization distribution over designs, not physical equilibrium among different chemical species. Changes to priors or constraint penalties must be included if claiming correct weights for a sequence of targets.

At each stage, mutate or locally optimize candidates, assess merit and uncertainty, reweight/resample where appropriate, and rejuvenate duplicated candidates. Identity gradients can inform mutation proposals; discrete edits, direct relaxed updates, diffusion, or a learned construction policy can all be used. Molecular construction with sequential Monte Carlo has precedent in [Bayesian sequential stacking](https://arxiv.org/abs/2204.01847), while [conditional diffusion sampling](https://arxiv.org/abs/2306.17775) illustrates population steering of diffusion trajectories. Neither establishes the proposed physical-affinity implementation.

This makes population management a first-class algorithm rather than merely running several independent seeds. It can wrap A, B, C, D, or F. Population collapse, duplicate ancestry, and amplification of favorable noise are central risks. Monitor effective population diversity and validate winners independently. Rigorous sequential Monte Carlo requires target weights and valid transition accounting; arbitrary gradient descent followed by resampling is only a heuristic unless its transport and weighting are treated correctly.

## Candidate F: generative flow-network graph construction

A generative flow network learns a policy that builds discrete objects through actions, aiming for terminal probabilities proportional to a positive reward. Molecular-construction and active-learning precedents include [trajectory-balance training](https://openreview.net/pdf?id=5btWTw1vcw1) and [biological sequence design](https://arxiv.org/abs/2203.04115). The reward-proportional property is an objective under appropriate modeling and training assumptions, not a finite-training guarantee.

For this project, actions could activate slots, select identities, add bonds, close rings, or terminate construction. A proposed reward is

$$
R(G)=p_{\mathrm{chem}}(G)\exp[-\gamma\widehat{\Delta G}_{\mathrm{bind}}(G)],
$$

with explicitly defined chemical support and selection strength. Physical evaluations train or correct the reward predictor. Identity gradients could train that predictor, rank actions, or refine completed candidates; they are additional information, not required by the standard construction-policy objective.

Potential advantages are explicit discrete topology, partially enforceable validity through the action space, and a distribution of promising outputs. The method departs from simultaneous cloud refinement. One speculative adaptation would retain cloud coordinates as pocket-aware spatial context while the policy chooses which slots to activate and connect. Coordinate/pose generation would still need a component of its own.

Multiple construction orders, slot permutations, ring closure, and the treatment of invalid terminal states require careful bookkeeping. Surrogate reward exploitation and training cost remain. This is a distinct candidate if chemical validity becomes the dominant bottleneck, not an already validated replacement for the cloud.

## Candidate G: expanded-ensemble chemical-state sampling

Sample physical coordinates and chemical alternatives within a shared scheme, schematically

$$
(x,\eta)\longrightarrow(x',\eta)\longrightarrow(x',\eta').
$$

Coordinate moves relax the environment; chemical-state moves explore alternatives. Adaptive biases can maintain exploration and free-energy estimators reconstruct relative state weights. The existing wiki records that lambda-dynamics with bias-updated Gibbs sampling alternates coordinate sampling and discrete alchemical-state updates for predefined ligand alternatives. It does not establish unrestricted graph construction. [SRC-0013; [[wiki/concepts/lambda-dynamics-with-bias-updated-gibbs-sampling]]]

For a cloud extension, occupancy and identity variables could be sampled alchemically, with gradients informing proposals. Unknown connectivity, changing state libraries, chemical validity, and reference measures introduce additional research problems. Favorable populations in the complex alone do not imply favorable binding: combine bias-corrected complex and solvent free energies through a consistent cycle. Updating a state library or bias changes what must be tracked by the estimator.

Candidate G could be a local physical-evaluation engine for another architecture: generate a family of related candidates with A–F, then jointly explore suitable chemical alternatives in each environment. Coordinate mixing, state-space growth, and overlap determine whether work is actually shared efficiently. This can reduce redundant physical work in principle; no speedup is established for the proposed cloud system.

## Composable design axes and candidate combinations

| Axis | Choices under consideration |
| --- | --- |
| Chemical representation | Relaxed cloud; discrete graph with alchemical derivatives; constructed graph with cloud context |
| Proposal mechanism | Direct gradient update; diffusion; gradient-ranked discrete edit; generative flow-network action |
| Guidance source | Direct physical estimates; learned value-and-gradient predictor; mixed acquisition/correction |
| Population management | Independent trajectories; branching; population annealing or sequential Monte Carlo |
| Physical evaluator | Separate fixed-design simulations; expanded-ensemble chemical-state sampling; optional learned equilibrium proposals |

Example combinations to investigate include E+D (population search with gradient-informed graph edits), E+C (population-managed learned-guided diffusion), and D+G (discrete chemical proposals evaluated in related-state ensembles). F can use the same value-and-gradient predictor considered in C without requiring diffusion. These combinations are suggestions, not selected architectures.

The central comparison is whether gradients should directly modify a relaxed molecule, rank discrete chemical edits, or train a learned guidance function. Population management and physical sampling can be compared independently of that choice. The assistant suggested prioritizing D as a new standalone candidate and E as a shared outer framework; the user has requested documentation, not selected that priority or committed to an implementation order.

## Memory and computational strategy

Avoid materializing all atom-pair/type-pair combinations. The pairwise formula is a contraction, not a demand to store an $N\times N\times M\times M$ array. For a separable pair potential,

$$
V_{mn}(r)=\sum_\ell C^{(\ell)}_{mn}f_\ell(r),
\qquad
U_{ij}=\sum_\ell f_\ell(r_{ij})\,\mathbf p_i^{\mathsf T}C^{(\ell)}\mathbf p_j.
$$

Shared coefficient matrices, batching, and suitable factorizations can reduce memory. Ordinary Lennard–Jones terms admit two radial basis functions, but type-dependent soft-core or double-exponential forms do not necessarily share that exact separation. Parameter interpolation and energy interpolation are different choices; do not exchange them merely for speed without documenting the resulting Hamiltonian.

Continuous typing avoids enumerating $M^3$ angle or $M^4$ torsion type combinations. It does not remove the number of possible graph paths. A dense graph has cubic angle and quartic torsion growth; a candidate graph of maximum degree $d$ has approximately $O(Nd^2)$ angle and $O(Nd^3)$ proper-torsion candidates. These are counting estimates for bounded-degree candidate graphs, not measured runtimes.

Use sparse candidate connectivity with explicit proposals for new edges. Do not permanently remove an edge simply because its current weight is small. Keep candidate lists fixed within sampling blocks; changes need renewed physical evaluation. A spatially overlapping cloud need not be a complete covalent candidate graph.

Keep differentiation tapes local to energy/parameter computations rather than whole trajectories. Accumulate derivative statistics in batches and retain selected configurations for diagnostics. Early performance measurements should separate simulation time, parameter assignment, derivative evaluation, diffusion generation, and endpoint validation.

## What to borrow from Boltzmann generators

Boltzmann generators learn configurational proposals and use statistical correction against a physical target. Original examples use invertible flows; they are not synonymous with molecular diffusion models. Adequate support and overlap remain necessary, and learned proposals can miss states. [SRC-0041]

A later conditional sampler could model $q_\phi(x\mid\eta,e)$ for each design and environment, with weights

$$
w(x)=\frac{\exp[-\beta U_e(x;\eta)]}{q_\phi(x\mid\eta,e)}.
$$

These weights require a compatible evaluable density and measure. For diffusion proposals, tractable endpoint densities or valid path-space corrections cannot be assumed. Propose ligand conformational or pose changes before attempting full solvated-complex generation, and derive the correct acceptance or weighting for local moves. Brief solvent relaxation alone is not a correction guarantee. [SRC-0041; proposed extension]

The variational free-energy identity gives another useful warning. For normalized $q$ and target $\pi$ on the same measure,

$$
\mathcal F[q]=\mathbb E_q[U]+\beta^{-1}\mathbb E_q[\log q]
=F+\beta^{-1}D_{\mathrm{KL}}(q\|\pi).
$$

Here $D_{\mathrm{KL}}$ denotes Kullback–Leibler divergence. The identity follows by substituting $\log\pi=-\beta U-\log Z$. Subtracting two variational estimates leaves the difference of their divergence errors, which need not cancel. A design optimizer could exploit unequal sampling errors between environments. Therefore learned ensemble models must not silently replace validated free-energy estimation.

## Optional distribution over designs

Instead of retaining only one optimum, define a desired distribution over chemically valid designs,

$$
\rho^*(\eta\mid\mathcal P)\propto\rho_0(\eta\mid\mathcal P)
\exp[-\gamma\Delta G_{\mathrm{bind}}(\eta)],
$$

where $\mathcal P$ is the pocket, $\rho_0$ a chemical prior, and $\gamma$ an inverse-energy selection parameter. This is an optional design definition, not a physical population of molecules. It corresponds formally to minimizing expected binding free energy plus $\gamma^{-1}D_{\mathrm{KL}}(\rho\|\rho_0)$ when the distributions and objective are well defined.

Physical configurational entropy is already part of binding free energy; diversity over different molecules is a separate design choice. The formal objective does not provide a tractable diffusion-training estimator automatically. Keep exact distributional targeting as an optional extension; all three candidate searches can be evaluated as optimization without claiming that distribution.

## Suggested implementation boundaries

The following are proposed module responsibilities, not existing code. Representation, physical modeling, ensemble evaluation, and endpoint validation are shared. Diffusion applies to B/C; C requires an affinity predictor and acquisition loop, which D/F may also reuse. A/B use direct optimization controllers; D additionally needs an edit grammar and proposal ranking; E needs population/ancestry management and any claimed weighting scheme; F needs construction actions and a policy trainer; G needs chemical-state/bias bookkeeping and consistent estimators. These components are alternatives where indicated, not a requirement to implement every model before an initial experiment.

| Component | Inputs and outputs | Required invariant |
| --- | --- | --- |
| Cloud representation | Slot features, bond logits, masks, coordinates | Permutation consistency; one meaning of absence |
| Chemical proposal model | Noisy cloud and pocket to proposed cloud | Reproducible random seeds and recorded model version |
| Graph relaxation | Relaxed nodes/edges to interaction tuples and exclusions | Discrete topology conventions recovered |
| Parameter assignment | Graph features to force-field parameters | Frozen weights; endpoint agreement |
| Hamiltonian evaluation | Configuration and design to energy and derivatives | Finite energies/derivatives in allowed intermediate states |
| Ensemble runner | Fixed design and environment to configurations/statistics | Explicit thermodynamic state and equilibration policy |
| Gradient estimator | Complex/solvent derivative samples to design gradient | Correct signs, corrections, units, and uncertainty |
| Guidance predictor | Relaxed design and pocket to scalar free-energy prediction and input derivatives | Consistent label coordinates and reference offsets; calibrated uncertainty |
| Guidance trainer | Physical values/differences and derivative labels to predictor | No reference leakage; derivative supervision and uncertainty weighting |
| Guided sampler | Denoiser and predictor to candidate population | Sampler-specific guidance; fixed model versions per batch |
| Acquisition controller | Candidate population and uncertainty to physical-evaluation requests | Diversity and coverage; fixed Hamiltonian per sampling block |
| Endpoint evaluator | Discrete molecular graph to independently evaluated result | Ordinary chemical parameterization and traceable reference |

Store for each evaluated design: ancestry, random seeds, model versions, graph and identity state, thermodynamic conditions, correction conventions, sample counts, derivative uncertainties, projection changes, validity checks, elapsed cost, and endpoint results. These records are needed to distinguish genuine improvement from a change in model or sampling policy.

## Build milestones and acceptance evidence

These are recommendations for making the idea testable, not an implementation commitment or a promised schedule.

### Milestone 1: representation and endpoint recovery

Build a small-slot representation with a deliberately limited chemical vocabulary. Verify permutation behavior, symmetric bonds, occupancy consistency, charge conservation, padded-ghost invariance, and discrete topology recovery on known molecules. Recover ordinary Garnet parameters and energies at endpoints before interpreting any soft-graph gradient. Determine whether the existing model can be adapted or whether a separately trained extension is needed.

### Milestone 2: differentiable Hamiltonian

Implement only the interactions needed by the chosen fixtures, including exclusions and soft-core conventions. Compare automatic derivatives with central finite differences over multiple step sizes. Test combined interactions, not only isolated terms: the FFRefine record demonstrates that a derivative path can fail silently depending on the combination of interaction implementations. [[wiki/answers/ffrefine-step15-enzyme-struct-layout-gradient-loss]]

Use small analytically tractable or numerically integrable systems to test ensemble derivatives. Then compare gradient-integrated local changes with independently computed free-energy differences for known molecular transformations. Separate numerical derivative errors from sampling uncertainty.

### Milestone 3: comparable architecture prototypes

Choose a small informative subset of A–G or their combinations; implementing every candidate is not a prerequisite. A tests explicit constraints and direct updates; B tests diffusion repair and physical checkpoints; C tests value-and-gradient predictor guidance; D tests whether gradients rank useful discrete edits. E can test population management with one fixed proposal mechanism; F tests constrained construction; G tests shared chemical-state sampling on a defined candidate family. Resolve atom ordering, hydrogen handling, chirality, and coordinate meaning consistently. Implementation order is open, and comparisons should isolate one mechanism where possible.

### Milestone 4: closed-loop pilot

Choose a small, tractable protein–ligand or host–guest benchmark with reference comparisons, while retaining the cloud-origin objective. Compare selected architectures using common endpoint evaluation, comparable chemical vocabularies, and declared total budgets. Include cloud-to-graph initialization, label acquisition, model training, generation, and physical sampling where applicable. Report both startup cost and marginal generation cost; amortization over many candidates may change the result. Use restricted chemical fixtures as diagnostics, not as a replacement of the user's cloud objective.

Possible comparisons include continuous versus discrete gradient use (A versus D), adding diffusion repair (A versus B), replacing direct guidance with a surrogate (B versus C), and adding population management (one chosen proposal method with and without E). Evaluate G against separate physical calculations on the same candidate family. For C or surrogate-guided F, compare value-only and value-and-gradient training. Repeat with independent seeds and compare valid endpoint yield, physically evaluated affinity, diversity, failure rates, uncertainty, and total cost. No candidate wins merely because its relaxed or predicted objective decreases.

### Milestone 5: expansion only after interpretable success

Use the comparison evidence to select an architecture, retain multiple architectures for different workloads, or redesign the common relaxation. Expand vocabulary, slot count, ring/topology changes, and target complexity only when results remain interpretable. Learned equilibrium proposals are an optional extension to physical sampling in any architecture. An improved surrogate prediction or relaxed objective is insufficient to pass a milestone whose objective is better discrete molecules.

## Measurements and failure criteria

| Question | Evidence to collect | Failure signal |
| --- | --- | --- |
| Does the interpolation recover the model? | Endpoint parameters, energies, forces, and exclusions | Discrete recovery mismatch |
| Are derivatives correct? | Finite differences and independent free-energy checks | Persistent disagreement beyond uncertainty |
| Does learned guidance generalize? | Held-out physical values, gradient agreement, and calibrated uncertainty | Diffusion exploits confidently wrong predictions |
| Do gradient labels help? | Value-only versus value-and-gradient guidance at matched cost | No improvement in physically validated endpoints |
| Does guidance survive discretization? | Relaxed change versus endpoint change | Improvement disappears after projection |
| Does diffusion cooperate with guidance? | Edit retention and proposal validity | Denoising repeatedly undoes favorable edits |
| Are ensembles reliable? | Replicas, correlation, overlap, pose/water-state diagnostics | Gradient direction changes with sampling history |
| Is the method useful computationally? | Endpoint affinity and diversity at matched total cost | No benefit over simpler baselines |
| Does it generalize physically? | Independent protocols and ultimately experiments | Gains restricted to the optimized model |

Set numerical tolerances and budget thresholds before the pilot, using calibration systems rather than arbitrary universal values. Archive negative results: they may identify an unsuitable interpolation, inadequate sampling, or a poor diffusion prior rather than invalidate every version of the idea.

## Main unresolved risks

- **Relaxation exploitation:** fractional charge, size, bond, or exclusion states may outperform all realizable molecules.
- **Soft-graph extrapolation:** a pretrained parameterizer may produce smooth but chemically meaningless parameters between known graphs.
- **Slow environment response:** water, protein side chains, or ligand poses can lag behind design changes.
- **Reference-state inconsistency:** changing occupancy, connectivity, charge, or restraints can introduce uncancelled entropy or correction terms.
- **Denoiser conflict:** chemical-prior repair may remove useful modifications or bias exploration toward familiar chemistry.
- **Sampling-error selection:** optimization can preferentially select designs with favorable estimation errors.
- **Surrogate exploitation:** diffusion may find confident predictor errors, especially on fractional graphs outside the label distribution. Acquisition must cover uncertainty and diversity rather than only predicted winners.
- **Model exploitation:** improved predicted affinity may reflect force-field deficiencies rather than experimental improvement.
- **Topology cost:** angles, torsions, and exclusion paths may dominate if the candidate graph becomes dense.
- **Probability bookkeeping:** equivalent slot permutations and absent-state multiplicities can distort a purported distribution over molecules.
- **Novelty uncertainty:** local alchemical optimization, continuous typing, and molecular diffusion all have prior art; the novelty of the specific combination requires a fuller literature review.

## Decisions needed before implementation

Architecture selection is explicitly unresolved across A–G and their compatible combinations. Consider expected candidate count, available training data, chemical validity, sampling cost, surrogate reliability, and implementation complexity. Distinguish proposal, guidance, population, and physical-sampling choices rather than assuming every candidate must be tested as a mutually exclusive full pipeline.

1. Which target or diagnostic system, reference ligand, solvent conditions, and net-charge convention should be used?
2. Which elements, hydrogen representation, bond states, and maximum slot count form the first vocabulary?
3. Which diffusion checkpoint or dataset is compatible with explicit bonds, occupancy, and pocket conditioning?
4. Can Garnet be extended while preserving endpoint behavior, and how will soft chemical features be defined?
5. What is the exact Hamiltonian, including interpolation, exclusions, ghosts, restraints, and charge normalization?
6. Which free-energy cycle and estimator will anchor the design derivatives to endpoint comparisons?
7. What physical-readiness gate and sampling policy will be used for label acquisition?
8. What compute budget, baselines, and predeclared success criteria make the pilot informative?
9. Should guidance act through predicted clean designs or use a noise-conditioned predictor, and how should guidance strength depend on noise and uncertainty?
10. What seed label dataset, derivative coordinate system, uncertainty model, reference network, acquisition policy, and retraining cadence will be used?
11. Should gradients directly update relaxed identities, rank discrete edits, or supervise a learned guide? What cloud-to-graph transition is needed for D/F?
12. Would population management improve exploration sufficiently to justify its additional cost, and is rigorous weighting required or heuristic optimization sufficient?
13. Can suitable candidate families share expanded-ensemble evaluation, and how will changing chemical libraries and biases be recorded?

## Evidence and related literature

### Existing wiki evidence

- [[wiki/concepts/lambda-dynamics-with-bias-updated-gibbs-sampling]] — predefined discrete alchemical alternatives, coordinate/state updates, and sampling caveats. [SRC-0013]

- [[wiki/sources/SRC-0099-training-force-field-proteins-small-molecules]] — Garnet parameter assignment, functional forms, benchmarks, and limitations. [SRC-0099]
- [[wiki/concepts/garnet-force-field]] — durable overview of continuous force-field typing.
- [[wiki/sources/SRC-0041-boltzmann-generators-sampling-equilibrium-states-of-many-body]] — learned configurational proposals, energy/example training, reweighting, and coverage limitations. [SRC-0041]
- [[wiki/answers/ffrefine-step15-enzyme-struct-layout-gradient-loss]] — dated project evidence motivating independent derivative checks; not evidence that this ligand-design method has been implemented.

### External references discussed, not ingested here

- [A gradient-directed Monte Carlo approach to molecular design](https://arxiv.org/abs/0807.2429) — continuous derivatives informing discrete molecular search.
- [Oops I Took A Gradient: Scalable Sampling for Discrete Distributions](https://proceedings.mlr.press/v139/grathwohl21a.html) — gradient-informed discrete proposals and acceptance correction.
- [Bayesian Sequential Stacking Algorithm for Concurrently Designing Molecules and Synthetic Reaction Networks](https://arxiv.org/abs/2204.01847) — population-based molecular construction precedent.
- [Practical and Asymptotically Exact Conditional Sampling in Diffusion Models](https://arxiv.org/abs/2306.17775) — sequential Monte Carlo steering of diffusion under its stated assumptions.
- [Trajectory balance: Improved credit assignment in GFlowNets](https://openreview.net/pdf?id=5btWTw1vcw1) — reward-based construction-policy training.
- [Biological Sequence Design with GFlowNets](https://arxiv.org/abs/2203.04115) — active learning and uncertainty-aware candidate generation.

- [Optimization of Protein–Ligand Electrostatic Interactions Using an Alchemical Free-Energy Method](https://pmc.ncbi.nlm.nih.gov/articles/PMC7007198/) — precedent for charge optimization against binding free energy followed by chemical interpretation.
- [Identification of Optimal Ligand Growth Vectors Using an Alchemical Free-Energy Method](https://pubs.acs.org/doi/10.1021/acs.jcim.0c00610) — related continuous interaction-parameter optimization.
- [Addressing Intersite Coupling Unlocks Large Combinatorial Chemical Spaces for Alchemical Free Energy Methods](https://pmc.ncbi.nlm.nih.gov/articles/PMC9700482/) — related multisite alchemical exploration; does not establish unrestricted cloud generation.
- [Categorical Reparameterization with Gumbel-Softmax](https://arxiv.org/abs/1611.01144) — categorical relaxation and stochastic proposal ingredient.
- [TargetDiff](https://arxiv.org/abs/2303.03543) — joint pocket-conditioned coordinate and identity generation.
- [DiffGui](https://www.nature.com/articles/s41467-025-63245-0) — joint atom/bond diffusion and property guidance.
- [Scalable Equilibrium Sampling with Sequential Boltzmann Generators](https://arxiv.org/abs/2502.18462) — possible future learned-proposal and statistical-correction direction.

These references support ingredients or precedents, not the performance of the proposed pipeline. A dedicated literature and implementation review remains necessary before claiming novelty or selecting dependencies.

## Wiki updates made

- Created this living design note and [[wiki/concepts/diffusion-guided-alchemical-molecular-design]] as a durable conceptual entry point.
- Added navigation and log entries; generated category and graph navigation is maintained by repository tooling.
- No sources ingested and no raw material modified.

## Changes

- 2026-10-16: Expanded the design space with gradient-informed discrete search, population annealing/sequential Monte Carlo, generative flow-network construction, and expanded-ensemble chemical sampling. Added workflows, evidence links, compatibility axes, and open decisions; retained A/B/C and left architecture selection open.

- 2026-10-16: Recorded the originating conversation, selected cloud/diffusion/identity-gradient direction, mathematical construction, implementation boundaries, validation milestones, and open decisions. No implementation results are claimed.
- 2026-10-16: Recorded the then-preferred learned-guidance architecture, including value-and-gradient predictor training, relative-label handling, clean-prediction guidance, and an outer physical-acquisition loop.
- 2026-10-16: Reopened architecture selection at the user's request. Preserved no-diffusion optimization, alternating diffusion/physical evaluation, and learned guidance as three live candidates with explicit workflows, tradeoffs, shared requirements, and comparative milestones.
