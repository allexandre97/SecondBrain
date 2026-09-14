---
type: concept
status: active
created: 2026-09-14
updated: 2026-09-14
areas:
  - research
categories:
  - research/adaptive-sampling
  - research/molecular-simulation/free-energy
  - research/molecular-simulation/molecular-dynamics
  - research/machine-learning/molecular-modeling
  - research/biomolecules/proteins
tags:
  - generative-sampling
  - committor
  - transition-path-sampling
  - rare-events
  - Gen-COMPAS
  - math-heavy
related:
  - "[[wiki/sources/SRC-0086-breaking-timescales-generative-sampling-conformational-transitions]]"
  - "[[wiki/sources/SRC-0087-breaking-timescales-generative-sampling-conformational-transitions-supplement]]"
  - "[[wiki/concepts/adaptive-enhanced-sampling]]"
  - "[[wiki/concepts/free-energy-estimation]]"
  - "[[wiki/concepts/enhanced-sampling-validation]]"
  - "[[wiki/concepts/boltzmann-generators-equilibrium-sampling]]"
  - "[[wiki/claims/CLM-0043-generated-transition-proposals-require-dynamical-validation]]"
  - "[[wiki/questions/QST-0009-scalable-independent-validation-of-learned-committors]]"
  - "[[wiki/tensions/TEN-0016-internal-convergence-vs-external-free-energy-correctness]]"
sources:
  - SRC-0086
  - SRC-0087
sensitivity: public
encryption: none
---

# Generative Committor-Guided Path Sampling

## Summary

Generative committor-guided path sampling uses learned structural proposals to seed explicit molecular dynamics, then uses a learned committor to focus later sampling near transition regions. In Gen-COMPAS, diffusion-generated structures are refined by bidirectional targeted molecular dynamics (TMD), followed by unbiased shooting, committor learning, and RiteWeight reconstruction of stationary free-energy landscapes. [SRC-0086, pp. 2, 7–8] [SRC-0087, Algorithm S1]

## Key points

- The workflow requires endpoint structures and basin definitions but not a small set of predefined collective variables to drive proposal generation or committor learning. [SRC-0086, pp. 2–3]
- Generated configurations are proposal targets, not equilibrium samples or final transition states. Only post-TMD unbiased trajectories enter kinetic and thermodynamic analyses. [SRC-0086, p. 7]
- The committor $q(x)$ is both a probabilistic progress coordinate and the selection signal for structures near the $q=1/2$ separatrix. [SRC-0086, pp. 2, 7]
- Full $3N-6$ Z-matrix coordinates for selected atoms reduce dependence on a few intuitive CVs, but atom selection, model expressivity, force field, basin definitions, and sampling coverage remain important priors. [SRC-0086, p. 8]
- RiteWeight is needed because short unbiased trajectories start from deliberately non-equilibrium ensembles near TMD endpoints or the separatrix. [SRC-0087, pp. S15–S16]
- The method is intended for exploratory transition-region and pathway analysis. Its local or projected FEL stability does not by itself establish global equilibrium free energies or exhaustive pathway discovery. [SRC-0086, pp. 3, 6]

## Core equations

For basins $A$ and $B$, the committor is [SRC-0086, Eq. 1]

$$
q(x)=\mathbb P\!\left(\tau_B(x)<\tau_A(x)\right).
$$

The transition-state ensemble is associated with $q\approx1/2$. A VCN learns $q$ by minimizing a lagged correlation functional with endpoint penalties: [SRC-0086, Eqs. 2–5]

$$
C[q;\tau]=\frac12\left\langle\left(q(\tau)-q(0)\right)^2\right\rangle,
$$

$$
\mathcal L[q_\omega]
=
2C[q_\omega;\tau]
+
\lambda\left(
\left.F_\omega(z)^2\right|_{z\in A}
+
\left.\left(F_\omega(z)-1\right)^2\right|_{z\in B}
\right).
$$

After RiteWeight estimates frame weights $w(x)$, a post-selected coordinate $\xi$ is assigned the free energy [SRC-0087, Eqs. S11–S12]

$$
F(\xi)=-k_BT\ln\left[\sum_{x\in D}w(x)\delta\!\left(\xi(x)-\xi\right)\right]+C.
$$

## Algorithmic dependencies

1. Endpoint trajectories define the initial system-specific training set. [SRC-0087, Algorithm S1]
2. The DDPM expands structural proposals beyond the endpoint samples. [SRC-0087, pp. S12–S14]
3. Bidirectional TMD tests accessibility from each basin and produces refined starting configurations. [SRC-0086, p. 8]
4. Unbiased shooting provides dynamical transition data and removes TMD trajectories from estimators. [SRC-0086, pp. 7–8]
5. RiteWeight addresses non-equilibrium starting ensembles; the VCN then learns a committor used to focus the next iteration. [SRC-0087, pp. S10–S16]
6. Structural coverage, trajectory connectivity, TMD consistency, shooting, bootstrap, and model-ensemble diagnostics test different failure modes. [SRC-0087, pp. S16–S35]

## Relation to Boltzmann generators

Both approaches use generative models in molecular sampling, but their estimator roles differ. Boltzmann generators learn an exact-density proposal and can importance-reweight generated configurations toward equilibrium. Gen-COMPAS treats DDPM output only as structural targets; explicit-Hamiltonian TMD refinement and subsequent unbiased dynamics supply the analyzed trajectories, while RiteWeight estimates their stationary weights. [SRC-0041] [SRC-0086, pp. 2–3, 7]

## Evidence

- Trp-cage independent aimless shooting yielded $r=0.898$ and $R^2=0.806$ between predicted and sampled committors over 91 retained structures. [SRC-0087, pp. S26–S27]
- Gen-COMPAS used 594 ns of aggregate unbiased Trp-cage sampling versus a 208.8 $\mu$s DESRES reference trajectory; the paper explicitly limits this to a trajectory-budget comparison rather than an equal-error or wall-clock speedup. [SRC-0086, p. 4]
- Larger applications recovered interpretable AAC, $V_o$, ribose-binding-protein, and nAChR pathways, but direct shooting was not scaled to all of them. [SRC-0086, pp. 4–6] [SRC-0087, pp. S5–S9, S31]

## Implementation consequences

- Tune TMD force and duration by comparing early and late RMSD distributions; generated-model loss alone is not an acceptance criterion. [SRC-0087, pp. S33–S35]
- Preserve trajectory identity in bootstrap resampling because frames within one trajectory are correlated. [SRC-0087, p. S18]
- Report aggregate MD time separately from DDPM, VCN, generation, and TMD compute; trajectory-length ratios are not end-to-end speedups. [SRC-0086, p. 4] [SRC-0087, Table S6]
- Treat ensemble disagreement as an uncertainty proxy, not proof against shared systematic committor bias. [SRC-0087, p. S31]

## Caveats

- A stable projected FEL can remain wrong because of missed channels, weak trajectory connectivity, projection degeneracy, or common model bias. [SRC-0086, pp. 3, 6] [SRC-0087, pp. S16–S21]
- “No predefined CVs” does not mean “no structural priors”: endpoints, basins, selected atoms, coordinates, force field, TMD settings, and model architecture remain specified. [SRC-0086, pp. 2–3, 8]
- The source's AAC calculation supplied an $O$ state and decomposed the route into $C$–$O$ and $O$–$M$ committors; that application is not endpoint-only discovery of $O$ from $C$ and $M$. [SRC-0086, p. 9]

## Links

- [[wiki/sources/SRC-0086-breaking-timescales-generative-sampling-conformational-transitions]]
- [[wiki/sources/SRC-0087-breaking-timescales-generative-sampling-conformational-transitions-supplement]]
- [[wiki/concepts/adaptive-enhanced-sampling]]
- [[wiki/concepts/free-energy-estimation]]
- [[wiki/concepts/enhanced-sampling-validation]]
- [[wiki/concepts/boltzmann-generators-equilibrium-sampling]]
- [[wiki/claims/CLM-0043-generated-transition-proposals-require-dynamical-validation]]
- [[wiki/questions/QST-0009-scalable-independent-validation-of-learned-committors]]
- [[wiki/tensions/TEN-0016-internal-convergence-vs-external-free-energy-correctness]]

## Open questions

- Can direct-shooting or independent-reference validation scale to the largest systems without erasing the method's computational advantage? [SRC-0087, p. S31]
- Can ensemble disagreement reveal shared committor bias, or only stochastic model uncertainty? [SRC-0087, p. S31]
- How reliably does pairwise decomposition recover multistate networks when important intermediate basins are not supplied? [SRC-0086, pp. 6, 9]
