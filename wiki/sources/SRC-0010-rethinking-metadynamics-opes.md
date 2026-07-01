---
type: source
status: active
created: 2026-06-30
updated: 2026-07-01
source_id: SRC-0010
display_title: "Rethinking Metadynamics"
short_title: "Rethinking Metadynamics"
aliases:
  - "SRC-0010"
  - "Rethinking Metadynamics"
source_path: raw/sources/SRC-0010-rethinking-metadynamics-from-bias-potentials-to-probability-distributions.pdf
imported_path: raw/sources/SRC-0010-rethinking-metadynamics-from-bias-potentials-to-probability-distributions.pdf
original_filename: "rethinking-metadynamics-from-bias-potentials-to-probability-distributions.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 5b9e25b1e7e852d7a5ead4a6454b25c80b509f70b30c1b48d975447196b85062
authors:
  - "Michele Invernizzi"
  - "Michele Parrinello"
author_entities: []
year: 2020
venue: "Journal of Physical Chemistry Letters"
doi: "10.1021/acs.jpclett.0c00497"
arxiv:
metadata_review_status: reviewed
areas:
  - research
categories:
  - research/adaptive-sampling
  - research/molecular-simulation/free-energy
tags:
  - opes
  - metadynamics
  - probability-reconstruction
  - collective-variables
  - math-heavy
related:
  - "[[wiki/sources/SRC-0011-opes-supporting-information]]"
  - "[[wiki/concepts/on-the-fly-probability-enhanced-sampling]]"
  - "[[wiki/concepts/adaptive-enhanced-sampling]]"
  - "[[wiki/concepts/free-energy-estimation]]"
sources:
  - SRC-0010
  - SRC-0011
cites_sources: []
citation_match_status: reviewed
cqt_review_status: linked
sensitivity: public
encryption: none
source_bundle: opes-rethinking-metadynamics
bundle_role: main
ingestion_status: complete
coverage_profile: math-standard
---

# Rethinking Metadynamics

Source ID: `SRC-0010`

## Raw source

- Repository path: `raw/sources/SRC-0010-rethinking-metadynamics-from-bias-potentials-to-probability-distributions.pdf`
- Open raw source: [raw/sources/SRC-0010-rethinking-metadynamics-from-bias-potentials-to-probability-distributions.pdf](../../raw/sources/SRC-0010-rethinking-metadynamics-from-bias-potentials-to-probability-distributions.pdf)
## Source bundle

This is the main paper in the `opes-rethinking-metadynamics` bundle. The supporting information is [[wiki/sources/SRC-0011-opes-supporting-information]]. [SRC-0010] [SRC-0011]

## Summary

This 2020 paper introduces on-the-fly probability-enhanced sampling, or OPES. The central shift is to reconstruct the probability distribution in collective-variable space and derive the bias from that estimate, rather than directly constructing a history-dependent bias potential as in metadynamics. [SRC-0010]

OPES keeps some useful metadynamics behavior, such as on-the-fly adaptation, but adds an explicit target distribution, weighted kernel-density estimation, explored-region normalization, a bounded bias, and straightforward umbrella-style reweighting. [SRC-0010]

## Key Points

- OPES frames enhanced sampling as probability-distribution reconstruction rather than direct bias-potential accumulation. [SRC-0010]
- The target distribution $p^{tg}(s)$ defines what distribution should be sampled once the method converges. [SRC-0010, eq. 4]
- The paper focuses on a well-tempered target $p^{tg}(s)\propto[P(s)]^{1/\gamma}$, with a flat target recovered in the $\gamma\to\infty$ limit. [SRC-0010]
- The probability estimate is built on the fly with weighted Gaussian kernels, where each new kernel is weighted by the previous bias. [SRC-0010, eq. 5]
- Kernel bandwidths shrink according to a Silverman-rule-style formula using an effective sample size. [SRC-0010, eq. 6]
- A normalization over the explored collective-variable region $\Omega_n$ improves exploration speed and robustness in higher-dimensional spaces. [SRC-0010, eq. 7]
- The regularization term $\epsilon$ caps the applied bias and helps avoid forcing the simulation into uninteresting high-free-energy regions. [SRC-0010, eq. 8]
- Tests compare OPES with well-tempered metadynamics on model and peptide systems, including alanine dipeptide and alanine tetrapeptide. [SRC-0010]

## Mathematical structure

The unbiased probability density in collective-variable space is $P(s)$, with free energy $F(s)=-\beta^{-1}\log P(s)$. A bias $V(s)$ changes the sampled distribution; unbiased statistics can be recovered by reweighting. [SRC-0010]

Classic probability-based adaptive umbrella sampling can be written as a bias proportional to $\log \hat{P}_n(s)$. OPES generalizes this by introducing a target distribution and constructing a KDE estimate $\tilde{P}_n(s)$ from biased samples. [SRC-0010, eqs. 3-5]

## Key equations

Bias for a target distribution: [SRC-0010, eq. 4]

$$
V(s)=\frac{1}{\beta}\log\frac{P(s)}{p^{tg}(s)}.
$$

Weighted KDE probability estimate: [SRC-0010, eq. 5]

$$
\tilde{P}_n(s)=\frac{\sum_k^n w_k G(s,s_k)}{\sum_k^n w_k},
\qquad
w_k=e^{\beta V_{k-1}(s_k)}.
$$

Bandwidth rescaling: [SRC-0010, eq. 6]

$$
\sigma_i^{(n)}=\sigma_i^{(0)}\left[N_{\mathrm{eff}}^{(n)}(d+2)/4\right]^{-1/(d+4)}.
$$

Explored-region normalization: [SRC-0010, eq. 7]

$$
Z_n=\frac{1}{|\Omega_n|}\int_{\Omega_n}\tilde{P}_n(s)\,ds.
$$

OPES bias: [SRC-0010, eq. 8]

$$
V_n(s)=\left(1-\frac{1}{\gamma}\right)\frac{1}{\beta}
\log\left(\frac{\tilde{P}_n(s)}{Z_n}+\epsilon\right).
$$

## Equation inventory

| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |
| Reweighting identity, eq. (1) | SRC-0010 introduction | [[wiki/concepts/on-the-fly-probability-enhanced-sampling]] | Recovers unbiased $P(s)$ from biased ensemble. | $P(s)$, $V(s)$ | Analysis and observables. |
| Metadynamics bias, eq. (2) | SRC-0010 introduction | This page | Defines baseline MetaD accumulation. | $G$, $\gamma$, $V$ | Comparison target. |
| Probability-based bias, eq. (3) | SRC-0010 method | This page | Shows adaptive umbrella-style probability reconstruction. | $\hat{P}_n$, $V_n$ | Historical connection. |
| Target-distribution bias, eq. (4) | SRC-0010 method | This page; [[wiki/concepts/on-the-fly-probability-enhanced-sampling]] | Defines bias that samples $p^{tg}$. | $P$, $p^{tg}$ | Conceptual core. |
| Weighted KDE, eq. (5) | SRC-0010 method | This page; [[wiki/concepts/on-the-fly-probability-enhanced-sampling]] | Estimates probability from biased samples. | $\tilde{P}_n$, $w_k$, $G$ | Main estimator. |
| Bandwidth rescaling, eq. (6) | SRC-0010 method; SRC-0011 | This page | Shrinks kernels as effective sample size grows. | $\sigma_i$, $N_{\mathrm{eff}}$, $d$ | Resolution schedule. |
| Explored-region normalization, eq. (7) | SRC-0010 method; SRC-0011 | This page | Normalizes over explored CV region. | $Z_n$, $\Omega_n$ | High-dimensional robustness. |
| OPES bias, eq. (8) | SRC-0010 method | This page | Final bias with regularization cap. | $V_n$, $\epsilon$, $\gamma$ | Production bias. |

## Algorithmic recursions

OPES periodically deposits a weighted Gaussian kernel at the current collective-variable point, updates or compresses the kernel representation, recomputes the explored-region normalization, and updates the bias from the reconstructed probability estimate. [SRC-0010] [SRC-0011]

## Evidence

The paper reports faster convergence and reduced bias oscillations relative to standard well-tempered metadynamics in representative tests, especially with suboptimal or multidimensional collective-variable sets. Demonstrations include alanine dipeptide and alanine tetrapeptide. [SRC-0010]

## Limitations and Caveats

- The paper compares against standard well-tempered metadynamics rather than exhaustively optimizing all competing enhanced-sampling methods. [SRC-0010]
- The method still depends on meaningful collective variables; OPES improves robustness but does not remove the CV-selection problem. [SRC-0010]
- Only well-tempered and flat targets are treated in the paper, even though the framework can support other targets. [SRC-0010]

## Links

- [[wiki/sources/SRC-0011-opes-supporting-information]]
- [[wiki/concepts/on-the-fly-probability-enhanced-sampling]]
- [[wiki/concepts/adaptive-enhanced-sampling]]
- [[wiki/concepts/free-energy-estimation]]

## Claims

- [[wiki/claims/CLM-0006-opes-reconstructs-probability-to-derive-bias]] - OPES derives an adaptive bias from an on-the-fly collective-variable probability estimate and an explicit target distribution. [SRC-0010]

## Questions

- [[wiki/questions/adaptive-estimators-vs-fixed-sample-estimators]] - How should OPES-style adaptive biasing be compared against fixed-sample postprocessing estimators? [SRC-0010]

## Tensions

- [[wiki/tensions/TEN-0005-on-the-fly-bias-adaptation-vs-postprocessing-diagnostics]] - OPES changes sampling during the run, but final free-energy use still depends on reweighting and diagnostics. [SRC-0010]

## Open Questions

- Which target distributions beyond well-tempered and flat targets are most useful in practical biomolecular OPES applications? [SRC-0010]

## Citation links

- Targeted citation review found no confirmed citations from this source to currently ingested free-energy/adaptive-sampling cluster sources.

## Metadata notes

- This document was identified as the main text because the PDF title, article page, and supporting-information pointer match SRC-0011.

## Mathematical gaps

- The wiki records the core OPES equations but not every example setup or the full numerical comparison details.

## Ingestion QA

### Retrieval questions checked

- What does OPES change relative to metadynamics?
- What is the target-distribution formulation?
- How is the probability estimate built?
- How are bandwidth and explored-region normalization handled?
- What does the regularization parameter do?
- How does OPES reweight?
- What examples support the method?
- What limitations remain?

### Coverage decision

Complete at `coverage_profile: math-standard` for the main paper component of the OPES bundle. [SRC-0010]

### Known gaps

- Exact simulation inputs and extended plots remain in the supporting information and PLUMED-NEST archive.
