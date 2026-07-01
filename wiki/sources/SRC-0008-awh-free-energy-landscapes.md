---
type: source
status: active
created: 2026-06-30
updated: 2026-07-01
source_id: SRC-0008
display_title: "Accelerated Weight Histogram Method for Exploring Free Energy Landscapes"
short_title: "AWH Free Energy Landscapes"
aliases:
  - "SRC-0008"
  - "AWH Free Energy Landscapes"
  - "Accelerated Weight Histogram Method for Exploring Free Energy Landscapes"
source_path: raw/sources/SRC-0008-accelerated-weight-histogram-method-for-exploring-free-energy.pdf
imported_path: raw/sources/SRC-0008-accelerated-weight-histogram-method-for-exploring-free-energy.pdf
original_filename: "044110_1_online.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: e3abfb199c09cb7f0763550a29490c3594607a05a5c4596dbbe6c54ff5c3931a
authors:
  - "V. Lindahl"
  - "Jack Lidmar"
  - "B. Hess"
author_entities:
  - "[[wiki/entities/authors/jack-lidmar]]"
year: 2014
venue: "Journal of Chemical Physics"
doi: "10.1063/1.4890371"
arxiv:
metadata_review_status: reviewed
areas:
  - research
categories:
  - research/molecular-simulation/free-energy
  - research/adaptive-sampling
  - research/statistics/monte-carlo
tags:
  - accelerated-weight-histogram
  - potential-of-mean-force
  - reaction-coordinate
  - adaptive-bias
  - gromacs
  - math-heavy
related:
  - "[[wiki/sources/SRC-0007-improving-efficiency-extended-ensemble-awh]]"
  - "[[wiki/concepts/accelerated-weight-histogram-method]]"
  - "[[wiki/concepts/adaptive-enhanced-sampling]]"
  - "[[wiki/concepts/free-energy-estimation]]"
  - "[[wiki/questions/awh-validation-scope]]"
sources:
  - SRC-0008
  - SRC-0007
cites_sources:
  - SRC-0007
citation_match_status: reviewed
cqt_review_status: linked
sensitivity: public
encryption: none
source_bundle: accelerated-weight-histogram
bundle_role: paper
ingestion_status: complete
coverage_profile: math-standard
---

# Accelerated Weight Histogram Method for Exploring Free Energy Landscapes

Source ID: `SRC-0008`

## Raw source

- Repository path: `raw/sources/SRC-0008-accelerated-weight-histogram-method-for-exploring-free-energy.pdf`
- Open raw source: [raw/sources/SRC-0008-accelerated-weight-histogram-method-for-exploring-free-energy.pdf](../../raw/sources/SRC-0008-accelerated-weight-histogram-method-for-exploring-free-energy.pdf)

## Summary

This 2014 Journal of Chemical Physics paper adapts AWH to atomistic molecular dynamics free-energy landscapes. It reformulates the method for reaction-coordinate sampling, estimates potentials of mean force through harmonic umbrellas and on-the-fly deconvolution, introduces free-energy-dependent target distributions, and gives practical setup guidance. [SRC-0008]

The paper demonstrates the method on lithium acetate ion pairing and the two-dimensional folding/misfolding landscape of chignolin. [SRC-0008, section III]

## Key Points

- AWH is formulated as an adaptive extended ensemble over configurations $x$ and a dynamic parameter $\lambda$, with a bias $g(\lambda)$ chosen from the current free-energy estimate and target distribution. [SRC-0008, section II.A]
- The Gibbs sampler chooses $\lambda$ from the conditional probability $\omega(\lambda \mid x)$, allowing large jumps in parameter space. [SRC-0008, eq. 3]
- The free-energy update compares the accumulated transition-probability histogram with the target histogram $N\rho(\lambda)$. [SRC-0008, eq. 4]
- For reaction-coordinate PMFs, AWH samples umbrella centers $\lambda$ and estimates the underlying PMF $\Phi(\xi)$ by deconvolving the umbrella-smeared free energy using sampled $\xi(x)$. [SRC-0008, section II.B]
- Free-energy-dependent target distributions can avoid wasting effort in high-free-energy or unphysical regions. [SRC-0008, section II.C]
- The effective number of samples $N$ controls update size; the paper discusses initialization, saturated error, and transition from robust early updates to asymptotic $1/t$ behavior. [SRC-0008, section II.D]
- Practical AWH setup depends mainly on the umbrella force constant $\kappa$, the time interval between $\lambda$ updates, and the initial effective sample count $N_0$. [SRC-0008, section III.A]

## Mathematical structure

The paper uses a joint density

$$
P(x,\lambda)=\frac{1}{Z}e^{-E(x,\lambda)+g(\lambda)}.
$$

The target distribution $\rho(\lambda)$ is achieved by setting the bias to the current free-energy estimate plus a target term:

$$
g(\lambda)=f(\lambda)+\log \rho(\lambda).
$$

Sampling and estimation are coupled because the current $f$ and $\rho$ determine $g$, which determines future $\lambda$ samples, which update $f$ again. [SRC-0008, section II.A]

For PMFs, the free energy of umbrella center $\lambda$ is a convolution of the underlying PMF with the umbrella potential. The paper's on-the-fly deconvolution uses sampled reaction-coordinate values to recover a higher-resolution PMF estimate. [SRC-0008, section II.B]

## Key equations

Observed marginal along $\lambda$: [SRC-0008, eq. 1]

$$
P(\lambda)=\frac{1}{Z}e^{-F(\lambda)+g(\lambda)}.
$$

Bias from free-energy estimate and target distribution: [SRC-0008, eq. 2]

$$
g(\lambda)=f(\lambda)+\log \rho(\lambda).
$$

Gibbs sampler for $\lambda$: [SRC-0008, eq. 3]

$$
\omega(\lambda \mid x)=P(\lambda \mid x)=\frac{1}{Z_\omega}e^{-E(x,\lambda)+g(\lambda)}.
$$

AWH free-energy update: [SRC-0008, eq. 4]

$$
\Delta f(\lambda)
=-\log\left(1+\frac{n_\Lambda \bar{\omega}(\lambda)}{N\rho(\lambda)}\right)+\text{constant}.
$$

PMF definition: [SRC-0008, eq. 5]

$$
\Phi(\xi)=-\log\int \pi_0(x)\delta(\xi-\xi(x))dx.
$$

Umbrella potential: [SRC-0008, eq. 6]

$$
Q_\kappa(\xi,\lambda)=\frac{\kappa}{2}(\xi-\lambda)^2.
$$

Umbrella-smeared free energy: [SRC-0008, eq. 7]

$$
e^{-F(\lambda)}
=\int e^{-Q_\kappa(\xi,\lambda)}e^{-\Phi(\xi)}d\xi.
$$

Free-energy cutoff target distribution: [SRC-0008, eq. 10]

$$
\rho(\lambda)=
\begin{cases}
\frac{1}{Z}\rho_0(\lambda), & f(\lambda)\le f_C,\\
\frac{1}{Z}\rho_0(\lambda)e^{-(f(\lambda)-f_C)}, & f(\lambda)>f_C.
\end{cases}
$$

## Equation inventory

| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |
| Marginal distribution, eq. (1) | SRC-0008 section II.A | This page; [[wiki/concepts/accelerated-weight-histogram-method]] | Connects bias, free energy, and sampled $\lambda$ density. | $P(\lambda)$, $F$, $g$ | Shows why $g=f+\log\rho$. |
| Bias formula, eq. (2) | SRC-0008 section II.A | This page; [[wiki/concepts/accelerated-weight-histogram-method]] | Sets bias from current estimate and target distribution. | $g$, $f$, $\rho$ | Core setup equation. |
| Gibbs sampler, eq. (3) | SRC-0008 section II.A | This page | Samples $\lambda$ conditionally on $x$. | $\omega$, $E$, $g$ | Enables large parameter jumps. |
| AWH update, eq. (4) | SRC-0008 section II.A | This page; [[wiki/concepts/accelerated-weight-histogram-method]] | Updates $f(\lambda)$ from transition-probability histogram. | $n_\Lambda$, $\bar{\omega}$, $N$, $\rho$ | Main adaptive recursion. |
| PMF definition, eq. (5) | SRC-0008 section II.B | This page; [[wiki/concepts/free-energy-estimation]] | Defines reaction-coordinate free energy. | $\Phi$, $\xi$, $\pi_0$ | Target of PMF calculations. |
| Umbrella potential, eq. (6) | SRC-0008 section II.B | This page | Couples $\xi$ to dynamic umbrella center $\lambda$. | $Q_\kappa$, $\xi$, $\lambda$, $\kappa$ | Reaction-coordinate implementation. |
| Umbrella convolution, eq. (7) | SRC-0008 section II.B | This page | Relates estimated $F(\lambda)$ to true PMF. | $F$, $\Phi$, $Q_\kappa$ | Explains deconvolution need. |
| PMF deconvolution, eq. (9) | SRC-0008 section II.B | [[wiki/concepts/accelerated-weight-histogram-method]] | Estimates PMF from sampled $\xi$. | $\phi$, $\gamma$, $a(t)$ | On-the-fly PMF reconstruction. |
| Free-energy cutoff, eq. (10) | SRC-0008 section II.C | This page | Avoids high-free-energy regions. | $\rho$, $\rho_0$, $f_C$ | Practical target distribution. |
| Error and saturation ratio, eqs. (11)-(13) | SRC-0008 section II.D | This page | Guides initial effective sample count. | $\epsilon$, $\epsilon_{sat}$, $\eta$ | Tuning and diagnostics. |

## Algorithmic recursions

The basic molecular AWH loop alternates MD or MC at fixed $\lambda$, Gibbs sampling of $\lambda$ using $\omega(\lambda \mid x)$, accumulation of transition probabilities, and updates of $f(\lambda)$ and $g(\lambda)$. [SRC-0008, section II.A]

For reaction coordinates, $\lambda$ is the umbrella center rather than the coordinate value itself. The PMF is recovered by accumulating a separate estimate over sampled $\xi(x)$ values and reweighting by the current umbrella-bias deconvolution factor. [SRC-0008, section II.B]

The early phase can keep $N$ conservative or grow it exponentially until coverage criteria are satisfied, then switch to the ordinary linearly growing, asymptotically $1/t$ update-size regime. [SRC-0008, sections II.D and III.A]

## Evidence

For lithium acetate in water, AWH estimated the PMF along the Li-carbonyl-carbon distance in four independent 50 ns runs and agreed with a reference constraint calculation based on 245 ns of simulation. The reported standard deviation for a selected free-energy difference was $0.16 k_B T$ for AWH. [SRC-0008, section III.C]

For chignolin, the paper used a two-dimensional reaction coordinate for native and misfolded hydrogen-bond distances, applied a free-energy cutoff target distribution, and recovered an error trend approaching $t^{-1/2}$ after the initial exploration phase. [SRC-0008, section III.D]

## Limitations and Caveats

- The most important remaining practical factor is the choice of reaction coordinate; AWH can diagnose poor choices through weight-histogram deviations, but it does not automatically invent a good coordinate. [SRC-0008, conclusion]
- Including improbable high-free-energy regions can waste sampling or produce instabilities, motivating but not universally solving the boundary-selection problem. [SRC-0008, sections II.C and III.D]
- The molecular demonstrations are LiAc and chignolin, not a broad benchmark suite. [SRC-0008, section III]

## Links

- [[wiki/sources/SRC-0007-improving-efficiency-extended-ensemble-awh]]
- [[wiki/sources/SRC-0009-awh-alchemical-free-energy]]
- [[wiki/concepts/accelerated-weight-histogram-method]]
- [[wiki/concepts/adaptive-enhanced-sampling]]
- [[wiki/concepts/free-energy-estimation]]
- [[wiki/questions/awh-validation-scope]]

## Claims

- [[wiki/claims/CLM-0007-awh-updates-bias-from-conditional-histograms]] - The molecular AWH extension uses conditional weights and target distributions to adapt free-energy biasing. [SRC-0008]

## Questions

- [[wiki/questions/awh-validation-scope]] - How robust are AWH target-distribution and reaction-coordinate guidelines beyond the tested atomistic examples? [SRC-0008]
- [[wiki/questions/adaptive-estimators-vs-fixed-sample-estimators]] - When should adaptive free-energy-landscape exploration be expected to outperform fixed-sample postprocessing? [SRC-0008]
- [[wiki/questions/windowed-local-free-energy-global-profile-reliability]] - What makes a locally sampled or umbrella-smoothed free-energy representation reliable as a global profile? [SRC-0008]

## Tensions

- [[wiki/tensions/TEN-0005-on-the-fly-bias-adaptation-vs-postprocessing-diagnostics]] - Adaptive free-energy-landscape exploration improves sampling only if final profile diagnostics support the result. [SRC-0008]

## Open Questions

- How robust are the reaction-coordinate and target-distribution guidelines for larger biomolecular systems with hidden slow degrees of freedom? [SRC-0008]

## Citation links

- `SRC-0007`: The references list J. Lidmar, Physical Review E 85, 056708 (2012), and the paper discusses it as the earlier AWH method. This matches the ingested original AWH source by first author, year, venue, and method title context. [SRC-0008]
- Citation review is complete for the currently ingested free-energy/adaptive-sampling cluster; it is not a full bibliography extraction.

## Metadata notes

- The title, source type, bundle role, public sensitivity, and `math-standard` coverage profile were inferred from the PDF title page and contents.

## Mathematical gaps

- The PMF deconvolution formula is recorded conceptually and in the equation inventory, but the full extracted equation typography is fragile in the PDF text; the PDF remains authoritative for exact formatting.
- The appendix's metadynamics correspondence is not deeply represented.

## Ingestion QA

### Retrieval questions checked

- What extension does the 2014 paper add to the original AWH method?
- How does AWH define the bias for a target distribution?
- What is the Gibbs sampler for $\lambda$?
- How does AWH estimate a PMF along a reaction coordinate?
- What does the umbrella convolution equation mean?
- How does a free-energy cutoff target distribution work?
- What does $N$ control?
- What molecular examples are used?
- What practical limitations remain?

### Coverage decision

Complete at `coverage_profile: math-standard`. The source page and linked concept page capture the central equations, PMF extension, target-distribution mechanism, practical setup guidance, molecular evidence, limitations, and QA. [SRC-0008]

### Known gaps

- Full appendix details and every simulation parameter remain in the source PDF.
