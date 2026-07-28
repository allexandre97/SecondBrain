---
type: answer
status: active
created: 2026-07-14
updated: 2026-07-14
question: "How should force-field optimization make initially disabled Lennard-Jones parameters trainable, and are exactly zero atomic charges affected in the same way?"
answer_status: answered
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/molecular-simulation/free-energy
  - research/scientific-computing
tags:
  - force-field-optimization
  - lennard-jones
  - parameterization
  - automatic-differentiation
  - identifiability
  - water-models
related:
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
  - "[[wiki/concepts/free-energy-reweighting-for-force-field-fine-tuning]]"
  - "[[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]]"
  - "[[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]"
  - "[[wiki/questions/force-field-training-validation-scope]]"
  - "[[wiki/tensions/TEN-0007-physical-water-construction-vs-empirical-fitting]]"
  - "[[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]"
sources:
  - SRC-0016
  - SRC-0018
  - SRC-0025
  - SRC-0027
sensitivity: public
encryption: none
wiki_pages_used:
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
  - "[[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]"
  - "[[wiki/questions/force-field-training-validation-scope]]"
  - "[[wiki/tensions/TEN-0007-physical-water-construction-vs-empirical-fitting]]"
raw_sources_consulted: []
---

# Training Initially Disabled Lennard-Jones Parameters

## Short answer

An atomic Lennard-Jones site with exactly zero well depth is not reliably trainable under ordinary geometric epsilon mixing and a zero-interaction shortcut. Its energy is zero, its sigma derivative is zero, and the epsilon derivative is either singular in the mathematical expression or replaced by a zero derivative when the implementation branches around the interaction. An atom with exactly zero charge is different: its electrostatic derivative is generally finite and nonzero, so it does not require an artificial charge seed.

Initializing a disabled Lennard-Jones site with small positive sigma and epsilon is a defensible engineering workaround, but it does not fully solve the parameterization problem. The seed changes the reference Hamiltonian, its cross-interaction strength is set by the mixing rules rather than by the atomic values alone, sigma remains weakly identifiable when epsilon is tiny, and a strictly positive bounded map cannot let the optimizer switch the site exactly off again.

The cleaner design is to optimize a nonnegative Lennard-Jones amplitude

$$
a_i = \sqrt{\epsilon_i}
$$

and evaluate geometric epsilon mixing as

$$
\epsilon_{ij} = a_i a_j.
$$

Use an optimizer that supports the exact boundary $a_i=0$. Keep sigma fixed or strongly regularized while the amplitude is zero, then allow sigma to move after the site becomes active. This conclusion is a 2026-07-14 FFRefine implementation analysis, not a claim taken directly from the cited literature.

## Why zero epsilon disables both Lennard-Jones parameters

Under Lorentz-Berthelot mixing,

$$
U_{ij}
= 4\sqrt{\epsilon_i\epsilon_j}
\left[
\left(\frac{(\sigma_i+\sigma_j)/2}{r_{ij}}\right)^{12}
-
\left(\frac{(\sigma_i+\sigma_j)/2}{r_{ij}}\right)^6
\right].
$$

At $\epsilon_i=0$, the interaction energy is zero and

$$
\frac{\partial U_{ij}}{\partial \sigma_i}=0.
$$

The derivative with respect to the physical parameter $\epsilon_i$ contains the derivative of $\sqrt{\epsilon_i}$ and is singular at zero when $\epsilon_j>0$. That singularity is not a useful training direction. In an implementation such as Molly that uses a zero shortcut, the energy routine returns zero before evaluating the mixing rule whenever an atomic Lennard-Jones parameter is exactly zero. Automatic differentiation then follows a constant-zero branch and reports zero rather than an activating gradient.

This is structural non-identifiability, not merely poor optimizer scaling. When the amplitude is zero, no energy observation contains information about sigma. No smooth re-scaling of the same physical epsilon coordinate can make sigma identifiable at that point.

## Why zero charge is normally trainable

For pairwise electrostatics,

$$
U_{\mathrm{elec}}
= k q_i\sum_j\frac{q_j}{r_{ij}},
\qquad
\frac{\partial U_{\mathrm{elec}}}{\partial q_i}
= k\sum_j\frac{q_j}{r_{ij}}.
$$

The derivative is generally nonzero at $q_i=0$. Therefore, an exactly neutral atomic site can normally acquire charge without a nonzero initialization. When molecular net charge is constrained, the meaningful direction transfers charge between at least two atoms, and its gradient is the corresponding difference in electrostatic potential.

The charge direction can still be unidentifiable in special cases: exact symmetry, a constraint that removes the direction, or an environment containing no electrostatic coupling. Those cases should be diagnosed from the constrained Jacobian or gradient, not inferred from $q_i=0$ alone.

## Limits of a small positive seed

Suppose a disabled site is initialized with $\sigma_i=0.01$ nm and $\epsilon_i=0.001$ kJ/mol. Against a site with $\sigma_j=0.30$ nm and $\epsilon_j=0.5$ kJ/mol, Lorentz-Berthelot mixing gives

$$
\sigma_{ij}=0.155\ \mathrm{nm},
\qquad
\epsilon_{ij}\approx0.022\ \mathrm{kJ/mol}.
$$

Thus, the atomic seed is not the cross-interaction size or well depth. In particular, a small atomic sigma does not remove the cross-site excluded volume under arithmetic sigma mixing, and geometric epsilon mixing makes the cross well depth scale with the square root of the seed.

A seed should instead be selected from two explicit design choices:

1. A chemically defensible sigma prior, such as an element- or force-field-family value. A placeholder sigma that was irrelevant only because epsilon was zero should not automatically become the prior.
2. A target scale for the resulting cross interactions. If the desired cross well depth against a representative site is $\delta$, then the corresponding atomic seed is $\epsilon_i=\delta^2/\epsilon_j$ under geometric mixing.

The seed must be large enough to give the optimizer a measurable sigma direction but small enough not to destabilize sampling or destroy replay overlap. These objectives conflict, so there is no universal safe seed.

## Recommended amplitude parameterization

Introduce a nonnegative amplitude $a_i$ and use it directly in the energy mixing rule:

$$
U_{ij}=4a_i a_j f(r_{ij},\sigma_i,\sigma_j).
$$

At $a_i=0$,

$$
\frac{\partial U_{ij}}{\partial a_i}
=4a_j f(r_{ij},\sigma_i,\sigma_j),
$$

which is finite and generally nonzero. The optimizer can therefore decide to activate the site. A projected constraint $a_i\ge0$ also allows it to return exactly to zero. By contrast, a sigmoid or softplus map only approaches zero asymptotically, and mapping a latent amplitude back through $\epsilon_i=a_i^2$ before an ordinary zero-shortcut energy evaluation restores the dead-gradient problem.

Sigma still has zero gradient at $a_i=0$. A robust policy is therefore:

1. Give sigma a physically motivated prior.
2. Optimize amplitude while sigma is fixed or strongly regularized.
3. Unlock sigma after amplitude exceeds a declared activation threshold, or optimize it jointly with a prior whose strength dominates near zero amplitude.
4. Use projected optimization or another boundary-capable method so amplitude can become exactly zero.
5. Report both the optimized amplitude and the derived physical well depth $\epsilon_i=a_i^2$.

This staged policy separates model selection---whether the site exists---from shape fitting---what sigma it should have once it exists.

## Implementation scope in FFRefine and Molly

The existing FFRefine seeded-activation route can remain entirely project-local: detect zero-epsilon sites, require explicit interior sigma and epsilon initial values, and construct the reference systems from those values.

An exact-zero amplitude implementation also does not strictly require editing Molly. FFRefine can define a custom epsilon mixing type whose result is the product of atomic amplitudes, construct the Lennard-Jones interactions with that mixing rule, and disable the Lennard-Jones zero shortcut. FFRefine must then consistently convert between stored amplitudes and reported physical epsilon values, rename parameter descriptors, handle units, and use a boundary-capable latent map.

A first-class Molly implementation would nevertheless be cleaner if amplitude-based Lennard-Jones parameters are expected to be reusable. It could provide explicit amplitude semantics, force-field conversion, unit handling, serialization, zero-safe shortcuts, and compatible treatment of all Lennard-Jones variants. Special-pair interactions and any precomputed terms must follow the same representation.

Long-range Lennard-Jones dispersion corrections require particular care. A correction precomputed from the starting atomic parameters is invalid when sigma or epsilon changes. It must be disabled, rebuilt for each candidate parameter set, or reformulated as a differentiable parameter-dependent term.

## Sampling and validation consequences

Activating a formerly absent repulsive or attractive site changes the Hamiltonian and may introduce energy barriers in configurations that were harmless under the original force field. A small initial perturbation does not guarantee that a frozen reference archive supports the candidate model. Replay-based optimization should therefore retain ESS, parity, split-sample, and resimulation checks as acceptance conditions rather than treating activation as a purely local gradient problem. [SRC-0016] [SRC-0018] [[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]

For water hydrogens, a zero-epsilon site is usually an intentional part of the water-model functional form rather than missing numerical data. Allowing hydrogen Lennard-Jones interactions expands the model class and can introduce compensating changes between hydrogen and oxygen parameters. It should be regularized and tested on held-out thermodynamic and structural properties. [SRC-0025] [SRC-0027] [[wiki/tensions/TEN-0007-physical-water-construction-vs-empirical-fitting]] [[wiki/questions/force-field-training-validation-scope]]

Recommended diagnostics are:

- gradient and Fisher eigenvalue magnitudes for the amplitude and sigma directions;
- sensitivity to multiple defensible amplitude and sigma initializations;
- candidate-versus-reference energy differences and replay ESS;
- short resimulation after activation;
- held-out observables and systems;
- whether the fitted site returns reproducibly to zero or remains active across independent starts.

## Decision summary

| Parameter at zero | Directly trainable? | Preferred treatment |
| --- | --- | --- |
| Atomic charge $q_i$ | Usually yes | Train directly under physically appropriate charge constraints. |
| Physical LJ epsilon $\epsilon_i$ with geometric mixing | No reliable finite gradient | Use a positive seed as a temporary workaround or optimize amplitude $a_i=\sqrt{\epsilon_i}$. |
| LJ sigma $\sigma_i$ when amplitude is zero | No | Supply a prior and delay or regularize sigma fitting until the amplitude activates. |
| LJ amplitude $a_i$ with product mixing | Yes, against active partners | Use a nonnegative boundary-capable optimizer and allow exact zero. |

## Links

- [[wiki/concepts/awh-replay-force-field-optimization]]
- [[wiki/concepts/free-energy-reweighting-for-force-field-fine-tuning]]
- [[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]]
- [[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]
- [[wiki/questions/force-field-training-validation-scope]]
- [[wiki/tensions/TEN-0007-physical-water-construction-vs-empirical-fitting]]
- [[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]
