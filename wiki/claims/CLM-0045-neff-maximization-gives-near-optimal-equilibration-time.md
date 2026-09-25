---
type: claim
status: active
created: 2026-09-25
updated: 2026-09-25
claim_status: supported
claim_scope: local
areas:
  - research
categories:
  - research/molecular-simulation/molecular-dynamics
  - research/statistics/monte-carlo
tags:
  - claim
  - equilibration
  - statistical-inefficiency
  - effective-sample-size
related:
  - "[[wiki/sources/SRC-0090-a-simple-method-for-automated-equilibration-detection-in]]"
  - "[[wiki/concepts/statistical-inefficiency-and-automated-equilibration-detection]]"
  - "[[wiki/sources/SRC-0023-statistically-optimal-analysis-multiple-equilibrium-states-mbar]]"
sources:
  - SRC-0090
sensitivity: public
encryption: none
---

# N_eff Maximization Gives Near-Optimal Equilibration Time

## Claim

Choosing the equilibration time $t_0$ that maximizes a single trajectory's estimated effective number of uncorrelated samples $N_\text{eff}(t_0)=(T-t_0+1)/g_{t_0}$ gives a distribution-free, per-trajectory estimate of the bias-optimal equilibration time whose overall RMS error is close to the best achievable RMS error from any fixed $t_0$ chosen with knowledge of many replicate trajectories. [SRC-0090]

## Scope

This is a local, source-specific claim. It was demonstrated on a single simple Lennard-Jones liquid-argon system relaxing from an atypical initial density, for two observables (reduced density and reduced potential energy $u^*=\beta[u+pV]$), using 500 replicate OpenMM simulations to establish the oracle fixed-$t_0$ comparison. [SRC-0090] It is not a general guarantee across arbitrary MD systems or strongly non-Gaussian/multimodal observables. [SRC-0090]

## Evidence

- The fixed-$t_0$ RMS error, minimized only with knowledge of all 500 replicates, was $0.00152 \pm 0.00005$ at $t_0\sim100\tau$. [SRC-0090, Figure 4]
- The per-trajectory automated scheme (maximizing $N_\text{eff}(t_0)$ using only that trajectory's own data) achieved RMS error $0.00173 \pm 0.00005$, about 11% worse than the oracle fixed choice. [SRC-0090, Figure 4]
- Using all data without discarding any gave RMS error $0.00441 \pm 0.00007$, about 290% worse than the oracle fixed choice. [SRC-0090, Figure 4]
- The same qualitative and quantitative result was reproduced for the reduced potential energy observable. [SRC-0090, Figure 5]
- The bias-variance trade-off plot (Figure 3) shows the per-trajectory $N_\text{eff}$-maximizing choice landing close to the Pareto-optimal bias/variance point identifiable only from knowledge of the true expectation across many replicates. [SRC-0090, Figure 3]

## Caveats

- The method cannot correct a simulation that never reached true equilibrium: in that case no $t_0$ removes the bias. [SRC-0090]
- The method degrades if there is too little data to estimate the statistical inefficiency $g$ reliably; the author treats this as a sampling-adequacy problem rather than a defect specific to the equilibration-detection step. [SRC-0090]
- The favorable ~11% figure is specific to the tested liquid-argon benchmark and its two observables; it is not shown to generalize quantitatively to biomolecular systems with slower, more heterogeneous relaxation or multimodal observables. [SRC-0090]
- The result depends on the underlying statistical-inefficiency estimator used to compute $g_{t_0}$; the source paper notes only that its chosen "fast multiscale" estimator performed equivalently to Geyer's initial-sequence estimators for this case, not that all estimators are interchangeable. [SRC-0090]
- This claim addresses per-trajectory equilibration-time selection. It does not itself validate the correlated-sample handling required by downstream reweighting estimators such as MBAR, which is a related but separate requirement. [SRC-0023]

## Links

- [[wiki/sources/SRC-0090-a-simple-method-for-automated-equilibration-detection-in]]
- [[wiki/concepts/statistical-inefficiency-and-automated-equilibration-detection]]
- [[wiki/sources/SRC-0023-statistically-optimal-analysis-multiple-equilibrium-states-mbar]]
