---
type: concept
status: active
created: 2026-06-29
updated: 2026-07-01
areas:
  - research
categories:
  - research/molecular-simulation/free-energy
  - research/statistics/monte-carlo
tags:
  - free-energy-estimation
  - partition-functions
  - molecular-simulation
  - math-heavy
related:
  - "[[wiki/sources/SRC-0023-statistically-optimal-analysis-multiple-equilibrium-states-mbar]]"
  - "[[wiki/sources/SRC-0010-rethinking-metadynamics-opes]]"
  - "[[wiki/sources/SRC-0012-mbar-configuration-mapping]]"
  - "[[wiki/sources/SRC-0013-ladybugs-lambda-dynamics]]"
  - "[[wiki/concepts/on-the-fly-probability-enhanced-sampling]]"
  - "[[wiki/concepts/mbar-with-configuration-mapping]]"
  - "[[wiki/concepts/multistate-bennett-acceptance-ratio]]"
  - "[[wiki/concepts/lambda-dynamics-with-bias-updated-gibbs-sampling]]"
  - "[[wiki/sources/SRC-0007-improving-efficiency-extended-ensemble-awh]]"
  - "[[wiki/sources/SRC-0008-awh-free-energy-landscapes]]"
  - "[[wiki/sources/SRC-0009-awh-alchemical-free-energy]]"
  - "[[wiki/concepts/accelerated-weight-histogram-method]]"
  - "[[wiki/sources/SRC-0005-times-square-sampling-free-energy]]"
  - "[[wiki/sources/SRC-0006-times-square-sampling-supplement]]"
  - "[[wiki/concepts/times-square-sampling]]"
  - "[[wiki/concepts/adaptive-enhanced-sampling]]"
  - "[[wiki/concepts/on-the-fly-estimation-versus-mbar]]"
  - "[[wiki/concepts/boltzmann-generators-equilibrium-sampling]]"
  - "[[wiki/concepts/transferable-and-scalable-boltzmann-generators]]"
  - "[[wiki/sources/SRC-0045-large-scale-collaborative-assessment-of-binding-free-energy]]"
  - "[[wiki/sources/SRC-0046-the-maximal-and-current-accuracy-of-rigorous-protein]]"
  - "[[wiki/sources/SRC-0061-openfe-rbfe-benchmark-journal-version]]"
  - "[[wiki/sources/SRC-0047-performing-solvation-free-energy-calculations-in-lammps-using]]"
  - "[[wiki/concepts/relative-binding-free-energy-benchmarking]]"
  - "[[wiki/questions/rbfe-benchmark-prospective-use-scope]]"
  - "[[wiki/claims/CLM-0017-experimental-reproducibility-bounds-rbfe-error-interpretation]]"
  - "[[wiki/claims/CLM-0019-edgewise-rbfe-metrics-can-overstate-arbitrary-comparison-quality]]"
  - "[[wiki/concepts/solvation-free-energy-decoupling-in-lammps]]"
sources:
  - SRC-0023
  - SRC-0010
  - SRC-0012
  - SRC-0013
  - SRC-0007
  - SRC-0008
  - SRC-0009
  - SRC-0005
  - SRC-0006
  - SRC-0037
  - SRC-0039
  - SRC-0041
  - SRC-0045
  - SRC-0046
  - SRC-0061
  - SRC-0047
sensitivity: public
encryption: none
---

# Free Energy Estimation

## Summary

Free energy estimation computes differences between free energies, often by estimating ratios of partition functions or normalizing constants for probability distributions such as Gibbs distributions. [SRC-0005]

## Key Points

- In SRC-0005, each probability distribution is defined by a Hamiltonian and an unknown partition function; the dimensionless free energy is the negative logarithm of that partition function. [SRC-0005, eq. 1]
- Free energy differences are all that matter because the estimates are identifiable only up to a common additive constant. [SRC-0005, section 2.1]
- Enhanced sampling introduces intermediate distributions to improve exploration, but how sampling effort is allocated across those distributions strongly affects estimator variance. [SRC-0005, introduction]
- AWH estimates free-energy weights in an extended ensemble by using conditional probabilities over parameter values as fractional histogram data. [SRC-0007, section II]
- OPES estimates free-energy surfaces by reconstructing collective-variable probability distributions on the fly. [SRC-0010]
- Configuration mapping can extend MBAR to states with poor or zero raw configuration overlap by transforming samples and including Jacobian corrections. [SRC-0012]
- MBAR estimates free energy differences and equilibrium expectations from multiple equilibrium states without histogram binning and with asymptotic uncertainty estimates. [SRC-0023]
- TSS treats free energy estimation as both a stochastic root-finding problem and a resource-allocation problem. [SRC-0005, sections 2.1-2.2]
- The supplement translates the estimator into per-window, epoch-based formulas for implementation and error estimation. [SRC-0006, sections 7-8]
- Boltzmann generators estimate equilibrium observables and free energies by generating exact-density proposals and reweighting them to the target Boltzmann distribution. [SRC-0041] [SRC-0037] [SRC-0039]
- Protein-ligand RBFE benchmark accuracy should be interpreted against experimental reproducibility, because assay-derived relative affinities have their own error floor. [SRC-0046]
- OpenFE's journal benchmark reinforces that all-to-all pairwise metrics are more representative than edgewise metrics for arbitrary ligand comparisons, and that private active-project data can be substantially harder than curated public data. [SRC-0061, sections 3.1.1 and 3.2]
- LAMMPS solvation free-energy decoupling can be implemented by adding an overlay correction that preserves intramolecular Coulomb energy while solute charges are scaled for solute-solvent electrostatic staging. [SRC-0047]

## Sample, biasing, and reweighting patterns

Free-energy methods differ as much in when they use sample information as in what estimator they solve. TSS, AWH, OPES, and LaDyBUGS are adaptive methods: samples gathered during the run change later sampling. MBAR is primarily an offline reweighting estimator for a fixed set of samples. Boltzmann generators learn an exact-density proposal distribution and then reweight generated proposals to the target equilibrium distribution. [SRC-0005] [SRC-0007] [SRC-0010] [SRC-0013] [SRC-0023] [SRC-0041]

| Method | Sample use | Biasing role | Reweighting role |
| --- | --- | --- | --- |
| TSS | Uses simulated-tempering samples and conditional rung probabilities to update free-energy estimates during sampling. [SRC-0005, sections 2.1-2.2] | Current estimates, visit-control tilts, and windowed local estimates steer future rung allocation. [SRC-0005, section 3.1] [SRC-0006, sections 6-7] | Conditional probabilities enter the stochastic estimator, but the distinctive feature is on-the-fly self-adjustment rather than post hoc analysis. [SRC-0005, section 2.2.3] |
| AWH | Each configuration contributes fractional conditional weights to many $\lambda$ values. [SRC-0007, eq. 5] [SRC-0009, eq. 3] | The adaptive free-energy bias is updated so the sampled parameter marginal approaches a target distribution. [SRC-0008, section II.A] [SRC-0009, eq. 5] | Conditional weights and histograms provide the reweighting-like information used to refine free energies. [SRC-0007, section II] |
| OPES | Collective-variable samples build a weighted kernel estimate of the unbiased CV probability density. [SRC-0010, eq. 5] | The bias is derived from the ratio between the estimated probability and a target CV distribution, with regularization to bound the bias. [SRC-0010, eqs. 4 and 8] | Weighted probability reconstruction links biased CV exploration back to the underlying distribution, subject to CV and target-choice limits. [SRC-0010] [SRC-0011] |
| MBAR | Takes samples already collected from multiple equilibrium states and cross-evaluates their reduced potentials. [SRC-0023] | MBAR itself does not adaptively bias sampling; the simulation protocol supplies any bias. [SRC-0023] | Reweighting is the main estimator, solving coupled normalizing-constant equations for free energies, expectations, and uncertainties. [SRC-0023] |
| LaDyBUGS | Alternates short conditional MD sampling with Gibbs updates over many discrete ligand alchemical states. [SRC-0013] | Dynamic biases keep the discrete alchemical states sampled during one production simulation. [SRC-0013, eqs. 1 and 4] | FastMBAR periodically estimates free energies and feeds those estimates into later bias updates. [SRC-0013] |
| Boltzmann generators | Generate proposal samples from an exact-density learned model. [SRC-0041] | Training makes the proposal resemble the target through energy, entropy/Jacobian, and sometimes example-based objectives. [SRC-0041] | Importance reweighting corrects generated proposals to equilibrium estimates when overlap and effective sample size are adequate. [SRC-0041] [SRC-0037] [SRC-0039] |

MBAR with configuration mapping is a useful boundary case: it remains an MBAR-style reweighting estimator, but first applies invertible maps and Jacobian corrections to improve overlap between states before solving the MBAR equations. [SRC-0012]

## Core equations

Distribution, partition function, and free energy: [SRC-0005, eq. 1]

$$
\rho_\lambda(x)=\frac{e^{-H_\lambda(x)}}{Z_\lambda^*}, \qquad
Z_\lambda^*=\int_S e^{-H_\lambda(x)}dx, \qquad
F_\lambda^*=-\log Z_\lambda^*.
$$

Free energy difference between two rungs: [SRC-0005, section 2.1]

$$
F_a^*-F_b^*=-\log\frac{Z_a^*}{Z_b^*}.
$$

MBAR self-consistent equations for dimensionless free energies: [SRC-0023, eq. 11]

$$
\hat f_i=
-\log\sum_{j=1}^{K}\sum_{n=1}^{N_j}
\frac{\exp[-u_i(x_{jn})]}
{\sum_{k=1}^{K}N_k\exp[\hat f_k-u_k(x_{jn})]}.
$$

TSS's basic root-finding observable: [SRC-0005, eqs. 7-8]

$$
G_k^F(X;F)=1-\frac{p_{\gamma,F}(k \mid X)}{\gamma_k}, \qquad E_{\gamma,F^*}[G_k^F]=0.
$$

Auxiliary observable estimator: [SRC-0005, eq. 20]

$$
G_{km}^{\mu}(x;F,\mu,o)=\frac{p_{\pi,F}(k \mid x)}{\pi_k}(\psi_m(x)-\mu_{km}).
$$

Coordinate-invariant rung density from a metric: [SRC-0005, eq. 19] [SRC-0006, eqs. 7.10-7.18]

$$
\gamma_k \propto \sqrt{\det g(\lambda_k)}, \qquad
g_{ij}(\lambda)=E\left[\frac{\partial H}{\partial \lambda_i}\frac{\partial H}{\partial \lambda_j}\right]
-E\left[\frac{\partial H}{\partial \lambda_i}\right]E\left[\frac{\partial H}{\partial \lambda_j}\right].
$$

Solvation free energy by thermodynamic integration: [SRC-0047, eqs. 1-2]

$$
\Delta G_{\mathrm{solv}}^i
=
\int_{\lambda_i=0}^{\lambda_i=1}
\left\langle \frac{dU}{d\lambda_i} \right\rangle_{\lambda_i} d\lambda_i,
\qquad i \in \{\mathrm{LJ},\mathrm{coul}\}.
$$

Relative binding free energy from an assay readout: [SRC-0046, eq. 2]

$$
\Delta\Delta G^{ab} = -kT \ln \frac{X^b}{X^a}.
$$

## Variable glossary

- $\rho_\lambda$: probability density at parameter $\lambda$. [SRC-0005, eq. 1]
- $H_\lambda$: dimensionless Hamiltonian. [SRC-0005, eq. 1]
- $Z_\lambda^*$: partition function, generally unknown. [SRC-0005, eq. 1]
- $F_\lambda^*$: exact free energy, $-\log Z_\lambda^*$. [SRC-0005, eq. 1]
- $\lambda_k$: discretized parameter value or rung. [SRC-0005, section 2.1]
- $\psi_m$: auxiliary observable whose ensemble average may inform the target rung density. [SRC-0005, section 2.2.2]
- $\mu_{km}$: estimated average of $\psi_m$ under rung $k$. [SRC-0005, eq. 20]
- $f_\lambda$: AWH free-energy estimate or hyperparameter used to bias sampling along $\lambda$. [SRC-0008, section II.A] [SRC-0009, section I.A]
- $\hat f_i$: MBAR estimate of the dimensionless free energy of state $i$, up to a common additive constant. [SRC-0023]
- $\Delta\Delta G^{ab}$: relative binding free energy between ligands $a$ and $b$. [SRC-0046]
- $X$: assay readout such as $\mathrm{IC}_{50}$, $K_d$, or $K_i$. [SRC-0046]
- $\lambda_i$: coupling parameter for a staged free-energy calculation, such as LJ or Coulomb staging. [SRC-0047]

## Derivation sketch

The estimator uses simulated tempering to sample an extended distribution where the unknown free energies enter only through current estimates. Conditional rung probabilities can be computed from Hamiltonian values and current estimates, so the stochastic approximation update does not need the true partition functions. [SRC-0005, section 2.1]

The supplement's iterative-importance-sampling derivation rewrites free-energy estimation in partition-function coordinates, then converts back to logarithmic free-energy coordinates. This explains both the logarithmic update and the history-forgetting implementation. [SRC-0006, sections 1.2 and 6.3]

AWH uses a related extended-ensemble view: choose bias parameters so the sampled parameter marginal matches a target distribution. Since the correct bias is tied to the unknown free energy, AWH repeatedly updates the bias from conditional probability histograms. [SRC-0007, section II] [SRC-0008, section II.A]

MBAR uses all cross-state reduced potentials to solve coupled normalization-constant equations. This makes it a postprocessing estimator for fixed samples rather than an adaptive sampling rule. [SRC-0023]

## Implementation consequences

- Free energy estimates should be interpreted as differences or profiles, not absolute values. [SRC-0005, section 2.1]
- Estimator quality depends on overlap between neighboring distributions and on how often informative rungs are visited. [SRC-0005, introduction]
- Windowed implementations must combine local estimates into global reported free energies rather than directly report noisy visit-control free energies. [SRC-0006, section 6.2]
- Error bars in the supplement are jackknife estimates over stored epochs and require decorrelated epoch pseudo-values. [SRC-0006, section 8]
- MBAR uncertainty estimates require effectively uncorrelated samples; correlated trajectories should be subsampled or otherwise handled before interpreting asymptotic error bars. [SRC-0023]
- Boltzmann-generator free-energy estimates depend on generated-target overlap and effective sample size; low-variance estimates can still be unreliable if important states are missing. [SRC-0037] [SRC-0039] [SRC-0041]
- Binding free-energy benchmark error should not be interpreted independently of experimental reproducibility and assay heterogeneity. [SRC-0046]
- OpenFE public benchmark performance was better than private active-project performance, so curated benchmark accuracy is not automatically prospective industrial accuracy. [SRC-0061]

## Caveats

- A theoretically optimal estimator still depends on practical sampling quality; poor mixing in `S` or `Lambda` can make estimates unreliable. [SRC-0005, section 2.1] [SRC-0006, section 10]
- MBAR does not remove the need for phase-space overlap between sampled and target states. [SRC-0023]
- The source bundle gives examples and theory, but not universal validation across all alchemical schedules or molecular systems. [SRC-0006, section 10.1]

## Evidence

- SRC-0005 motivates TSS by arguing that the allocation of computational resources across rungs changes the variance of the desired free energy estimate. [SRC-0005, introduction]
- SRC-0006's aqueous-solution example reports free energy differences for eight alchemical edges and compares estimated errors under different TSS settings. [SRC-0006, section 10]
- SRC-0023 demonstrates MBAR by combining multiple optical-tweezer constant-force data sets to estimate a DNA hairpin PMF. [SRC-0023]

## Links

- [[wiki/sources/SRC-0005-times-square-sampling-free-energy]]
- [[wiki/sources/SRC-0007-improving-efficiency-extended-ensemble-awh]]
- [[wiki/sources/SRC-0008-awh-free-energy-landscapes]]
- [[wiki/sources/SRC-0009-awh-alchemical-free-energy]]
- [[wiki/sources/SRC-0010-rethinking-metadynamics-opes]]
- [[wiki/sources/SRC-0012-mbar-configuration-mapping]]
- [[wiki/sources/SRC-0013-ladybugs-lambda-dynamics]]
- [[wiki/sources/SRC-0023-statistically-optimal-analysis-multiple-equilibrium-states-mbar]]
- [[wiki/concepts/accelerated-weight-histogram-method]]
- [[wiki/concepts/on-the-fly-probability-enhanced-sampling]]
- [[wiki/concepts/mbar-with-configuration-mapping]]
- [[wiki/concepts/multistate-bennett-acceptance-ratio]]
- [[wiki/concepts/lambda-dynamics-with-bias-updated-gibbs-sampling]]
- [[wiki/sources/SRC-0006-times-square-sampling-supplement]]
- [[wiki/concepts/times-square-sampling]]
- [[wiki/concepts/adaptive-enhanced-sampling]]
- [[wiki/concepts/on-the-fly-estimation-versus-mbar]]
- [[wiki/sources/SRC-0041-boltzmann-generators-sampling-equilibrium-states-of-many-body]]
- [[wiki/sources/SRC-0037-transferable-boltzmann-generators]]
- [[wiki/sources/SRC-0039-scalable-boltzmann-generators-for-equilibrium-sampling-of-large]]
- [[wiki/sources/SRC-0045-large-scale-collaborative-assessment-of-binding-free-energy]]
- [[wiki/sources/SRC-0046-the-maximal-and-current-accuracy-of-rigorous-protein]]
- [[wiki/sources/SRC-0061-openfe-rbfe-benchmark-journal-version]]
- [[wiki/sources/SRC-0047-performing-solvation-free-energy-calculations-in-lammps-using]]
- [[wiki/concepts/boltzmann-generators-equilibrium-sampling]]
- [[wiki/concepts/transferable-and-scalable-boltzmann-generators]]
- [[wiki/concepts/relative-binding-free-energy-benchmarking]]
- [[wiki/questions/rbfe-benchmark-prospective-use-scope]]
- [[wiki/claims/CLM-0017-experimental-reproducibility-bounds-rbfe-error-interpretation]]
- [[wiki/claims/CLM-0019-edgewise-rbfe-metrics-can-overstate-arbitrary-comparison-quality]]
- [[wiki/concepts/solvation-free-energy-decoupling-in-lammps]]

## Open Questions

- When should free energy estimation prioritize broad exploration of intermediate distributions versus targeted sampling of high-variance regions? [SRC-0005]
