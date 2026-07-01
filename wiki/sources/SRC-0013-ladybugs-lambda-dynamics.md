---
type: source
status: active
created: 2026-06-30
updated: 2026-07-01
source_id: SRC-0013
display_title: "Fast Free Energy Estimates from Lambda-Dynamics with Bias-Updated Gibbs Sampling"
short_title: "LaDyBUGS Lambda-Dynamics"
aliases:
  - "SRC-0013"
  - "LaDyBUGS Lambda-Dynamics"
  - "Fast Free Energy Estimates from Lambda-Dynamics with Bias-Updated Gibbs Sampling"
source_path: raw/sources/SRC-0013-fast-free-energy-estimates-from-lambda-dynamics-with.pdf
imported_path: raw/sources/SRC-0013-fast-free-energy-estimates-from-lambda-dynamics-with.pdf
original_filename: "s41467-023-44208-9-1.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: af91ee22aada070287484dd19c2e890d799e68bc16aee3dcf8bb831dac1bc8c3
authors:
  - "Michael T. Robo"
  - "Ryan L. Hayes"
  - "Xinqiang Ding"
  - "Brian Pulawski"
  - "Jonah Z. Vilseck"
author_entities: []
year: 2023
venue: "Nature Communications"
doi: "10.1038/s41467-023-44208-9"
arxiv:
metadata_review_status: reviewed
areas:
  - research
categories:
  - research/molecular-simulation/free-energy
  - research/computational-drug-discovery
  - research/adaptive-sampling
tags:
  - ladybugs
  - lambda-dynamics
  - relative-binding-free-energy
  - gibbs-sampling
  - fastmbar
  - math-heavy
related:
  - "[[wiki/concepts/lambda-dynamics-with-bias-updated-gibbs-sampling]]"
  - "[[wiki/concepts/relative-binding-free-energy-benchmarking]]"
  - "[[wiki/concepts/free-energy-estimation]]"
  - "[[wiki/concepts/adaptive-enhanced-sampling]]"
sources:
  - SRC-0013
cites_sources:
  - SRC-0008
  - SRC-0023
citation_match_status: reviewed
cqt_review_status: linked
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: math-standard
---

# Fast Free Energy Estimates from Lambda-Dynamics with Bias-Updated Gibbs Sampling

Source ID: `SRC-0013`

## Raw source

- Repository path: `raw/sources/SRC-0013-fast-free-energy-estimates-from-lambda-dynamics-with.pdf`
- Open raw source: [raw/sources/SRC-0013-fast-free-energy-estimates-from-lambda-dynamics-with.pdf](../../raw/sources/SRC-0013-fast-free-energy-estimates-from-lambda-dynamics-with.pdf)

## Summary

This 2023 Nature Communications paper introduces λ-dynamics with bias-updated Gibbs sampling, abbreviated LaDyBUGS. The method combines discrete Gibbs-sampler λ-dynamics with dynamic bias updates and periodic FastMBAR estimates to compute many relative binding free energies in one simulation. [SRC-0013]

The main motivation is to remove the separate static-bias identification stage used by previous λ-dynamics workflows while preserving collective sampling of multiple ligand analogues. [SRC-0013]

## Key Points

- LaDyBUGS samples coordinates $X$ and discrete alchemical states $\lambda$ by alternating $P(X\mid\lambda)$ molecular dynamics with $P(\lambda\mid X)$ Gibbs sampling. [SRC-0013, Methods]
- Dynamic scalar biases $E_i$ are updated continuously to force smooth sampling of all $\lambda_i$ states, rather than relying on precomputed static biases. [SRC-0013]
- FastMBAR is called periodically during the run to estimate free-energy differences and refine biases. [SRC-0013]
- The method evaluates all $\lambda$ state energies during Gibbs sampling, so MBAR inputs are available without separate trajectory postprocessing. [SRC-0013]
- Benchmarks cover five protein-ligand systems: MUP1, DNA ligase, c-Met, thrombin, and PFKFB3. [SRC-0013]
- Reported RMSEs against experiment are near or below $1.0$ kcal/mol, with efficiency gains over TI/MBAR of 18-66-fold for small perturbations and 100-200-fold for whole aromatic ring substitutions. [SRC-0013]

## Key equations

Conditional distribution for discrete $\lambda_i$: [SRC-0013, eq. 1]

$$
P(\lambda_i\mid X)=
\frac{\exp[-\beta(V^{SS}(X,\lambda_i)+V^{MS}(X,\lambda_i)+E_i)]}
{\sum_{l=1}^{M}\exp[-\beta(V^{SS}(X,\lambda_l)+V^{MS}(X,\lambda_l)+E_l)]}.
$$

Single-site alchemical potential: [SRC-0013, eq. 2]

$$
V^{SS}(X)=\sum_{y=1}^{S}\sum_{c=1}^{N_y}
\lambda_{y,c}\left[V(x^0,x^{y,c})+V(x^{y,c})\right].
$$

Multisite interaction potential: [SRC-0013, eq. 3]

$$
V^{MS}(X,\lambda)=
\sum_{y=1}^{S}\sum_{c=1}^{N_y}\sum_{z=y+1}^{S}\sum_{d=1}^{N_z}
\lambda_{y,c}\lambda_{z,d}V(x^{y,c},x^{z,d}).
$$

Dynamic bias update after FastMBAR estimate: [SRC-0013, eq. 4]

$$
E_i=-\Delta G_i^{t=u}+\epsilon_b\,2^{L_i-\min[L(\lambda)]}.
$$

Number of discrete $\lambda$ states for single-site perturbations: [SRC-0013, eq. 5]

$$
N_\lambda=N_s+\frac{N_s(N_s-1)}{2}\left(\frac{1}{\Delta\lambda}-1\right).
$$

## Equation inventory

| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |
| Gibbs conditional, eq. (1) | SRC-0013 Methods | This page; [[wiki/concepts/lambda-dynamics-with-bias-updated-gibbs-sampling]] | Samples discrete alchemical states. | $\lambda_i$, $X$, $E_i$, $V^{SS}$, $V^{MS}$ | Core sampler. |
| Single-site potential, eq. (2) | SRC-0013 Methods | This page | Defines single-site alchemical energy. | $x^0$, $x^{y,c}$, $\lambda_{y,c}$ | Single-site ligand modifications. |
| Multisite potential, eq. (3) | SRC-0013 Methods | This page | Adds interactions between alchemical sites. | $y,z,c,d$ | Multisite extension. |
| Bias update, eq. (4) | SRC-0013 Methods | This page; [[wiki/concepts/lambda-dynamics-with-bias-updated-gibbs-sampling]] | Combines FastMBAR free energy and visit-count penalty. | $E_i$, $\Delta G_i$, $L_i$, $\epsilon_b$ | Dynamic biasing. |
| State-count scaling, eq. (5) | SRC-0013 Methods | This page | Counts discrete lambda states. | $N_\lambda$, $N_s$, $\Delta\lambda$ | Cost scaling. |
| Relative-to-absolute conversion, eq. (6) | SRC-0013 Methods | This page | Converts computed relative free energies for experiment comparison. | $\Delta G_{\mathrm{comp}}$ | Benchmark analysis. |

## Algorithmic recursions

The LaDyBUGS cycle is: sample $P(X\mid\lambda)$ with short MD, evaluate all $\lambda$ energies and sample $P(\lambda\mid X)$, update biases after each Gibbs step, periodically stop to run FastMBAR, replace the free-energy component of the bias with the latest FastMBAR estimates, and continue. [SRC-0013]

## Evidence

Across 45 ligands in five benchmark systems, LaDyBUGS achieved an overall RMSE of $0.97$ kcal/mol against experiment with 15 ns sampling and a Kendall $\tau$ of $0.65$. [SRC-0013]

LaDyBUGS 15 ns used 18.3-66.0 times less sampling than the TI/MBAR 5 ns-per-window comparisons. For larger aromatic ring perturbations, LaDyBUGS 5 ns used 55-198 times less sampling than TI/MBAR 5 ns per window while maintaining useful agreement. [SRC-0013]

The paper reports that λD required 609 ns of bias-identification sampling before production, whereas LaDyBUGS avoids this static-bias identification cost. [SRC-0013]

## Limitations and Caveats

- Efficiency claims are relative to the paper's benchmark setup, implementations, and sampling schedules. [SRC-0013]
- The method assumes short MD segments adequately sample $P(X\mid\lambda)$ for the Gibbs-step logic and FastMBAR use. [SRC-0013]
- The paper notes implementation and future-work issues, including PME support and broader software integration. [SRC-0013]
- The approach is most naturally aligned with ligand series where multiple analogues can be sampled collectively around a common core. [SRC-0013]

## Links

- [[wiki/concepts/lambda-dynamics-with-bias-updated-gibbs-sampling]]
- [[wiki/concepts/relative-binding-free-energy-benchmarking]]
- [[wiki/concepts/free-energy-estimation]]
- [[wiki/concepts/adaptive-enhanced-sampling]]

## Claims

- [[wiki/claims/CLM-0008-ladybugs-couples-gibbs-sampling-with-fastmbar-bias-updates]] - LaDyBUGS couples Gibbs sampling over discrete lambda states with periodic FastMBAR bias updates. [SRC-0013]

## Questions

- [[wiki/questions/adaptive-estimators-vs-fixed-sample-estimators]] - When do bias-updated lambda-dynamics workflows outperform conventional TI/MBAR schedules under matched validation? [SRC-0013]
- [[wiki/questions/overlap-support-diagnostics-for-free-energy-estimators]] - How should support and overlap be diagnosed when FastMBAR estimates are fed back into adaptive biases? [SRC-0013]

## Tensions

- [[wiki/tensions/TEN-0005-on-the-fly-bias-adaptation-vs-postprocessing-diagnostics]] - FastMBAR updates improve online biasing, but final estimates still need support and uncertainty diagnostics. [SRC-0013]

## Open Questions

- How well does LaDyBUGS scale to larger perturbation networks and ligand series with more substantial scaffold changes? [SRC-0013]

## Citation links

- `SRC-0023`: The references list Shirts and Chodera, "Statistically optimal analysis of samples from multiple equilibrium states," Journal of Chemical Physics 129, matching the ingested original MBAR source. [SRC-0013]
- `SRC-0008`: The references list Lindahl, Lidmar, and Hess under "Accelerated weight histogram," matching the ingested AWH free-energy-landscapes source by author set and method title context. [SRC-0013]
- Citation review is complete for the currently ingested free-energy/adaptive-sampling cluster; it is not a full bibliography extraction.

## Metadata notes

- This source is a standalone enhanced-sampling paper, not part of the OPES source bundle.

## Mathematical gaps

- Supplementary mathematical proof details are referenced by the paper but not present in this folder; the wiki records the main-text workflow and equations.

## Ingestion QA

### Retrieval questions checked

- What is LaDyBUGS?
- How does it differ from previous discrete Gibbs-sampler λ-dynamics?
- What is the Gibbs conditional over $\lambda$?
- How are dynamic biases updated?
- How is FastMBAR used?
- What benchmark systems are reported?
- What efficiency gains are claimed?
- What limitations and assumptions remain?

### Coverage decision

Complete at `coverage_profile: math-standard`. [SRC-0013]

### Known gaps

- The paper references supplementary proof details not included as a separate local source in this folder.
