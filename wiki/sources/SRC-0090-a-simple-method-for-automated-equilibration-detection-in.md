---
type: source
status: active
created: 2026-09-25
updated: 2026-09-25
source_id: SRC-0090
display_title: "A Simple Method for Automated Equilibration Detection in Molecular Simulations"
short_title: "Automated Equilibration Detection"
aliases:
  - "SRC-0090"
  - "Automated Equilibration Detection"
  - "A Simple Method for Automated Equilibration Detection in Molecular Simulations"
source_path: raw/sources/SRC-0090-a-simple-method-for-automated-equilibration-detection-in.pdf
imported_path: raw/sources/SRC-0090-a-simple-method-for-automated-equilibration-detection-in.pdf
original_filename: "ct5b00784.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 8cd541a5a3c109ac512c26e5244f361bd8fa1f968a315bb814f31a84da656a5e
authors:
  - "John D. Chodera"
author_entities:
  - "[[wiki/entities/authors/john-d-chodera]]"
year: 2016
venue: "Journal of Chemical Theory and Computation"
doi: "10.1021/acs.jctc.5b00784"
arxiv:
metadata_review_status: reviewed
areas:
  - research
categories:
  - research/molecular-simulation/molecular-dynamics
  - research/statistics/monte-carlo
tags:
  - equilibration
  - statistical-inefficiency
  - effective-sample-size
  - autocorrelation
  - molecular-dynamics
  - pymbar
  - math-heavy
related:
  - "[[wiki/concepts/statistical-inefficiency-and-automated-equilibration-detection]]"
  - "[[wiki/sources/SRC-0023-statistically-optimal-analysis-multiple-equilibrium-states-mbar]]"
  - "[[wiki/concepts/multistate-bennett-acceptance-ratio]]"
  - "[[wiki/sources/SRC-0091-use-of-the-weighted-histogram-analysis-method-for]]"
sources:
  - SRC-0090
cites_sources:
  - SRC-0023
  - SRC-0091
citation_match_status: partial
cqt_review_status: linked
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: math-standard
---

# A Simple Method for Automated Equilibration Detection in Molecular Simulations

Source ID: `SRC-0090`

## Raw source

- Repository path: `raw/sources/SRC-0090-a-simple-method-for-automated-equilibration-detection-in.pdf`
- Open raw source: [raw/sources/SRC-0090-a-simple-method-for-automated-equilibration-detection-in.pdf](../../raw/sources/SRC-0090-a-simple-method-for-automated-equilibration-detection-in.pdf)

## Summary

This single-author JCTC article (received 14 Aug 2015, published 15 Jan 2016) proposes a simple, automated procedure for choosing how much of the initial portion of a molecular simulation trajectory to discard as "equilibration" (burn-in) before computing an equilibrium average. [SRC-0090]

Instead of assuming a distribution for the observable of interest or requiring a statistical normality test on the reversed time series (as in the reverse cumulative averaging, RCA, method of Yang et al.), the method chooses the equilibration time $t_0$ that maximizes the estimated effective number of uncorrelated samples $N_\text{eff}(t_0)$ remaining in the production region $[t_0, T]$. [SRC-0090]

The author demonstrates the method on two observables (reduced density and reduced potential energy) of a Lennard-Jones liquid-argon system relaxing from an atypical initial density, using 500 replicate OpenMM simulations to establish ground truth. A reference Python implementation is distributed as `pymbar.timeseries.detectEquilibration()`. [SRC-0090]

## Key Points

- Molecular simulations are often started from atypical configurations (extended chains, crystallographic geometries, artificially assembled solvent/lipid boxes), producing an initial transient in observables that biases naive cumulative averages unless discarded. [SRC-0090]
- The bias from atypical starting conditions can persist for surprisingly long times (~2000$\tau$ in the paper's liquid-argon example) and is present even when averaging over many independent replicates started from the same atypical condition. [SRC-0090, Figure 1]
- For a fixed equilibration time $t_0$, the estimator's mean squared error decomposes exactly into a variance term and a squared-bias term (Eqs. 4-7). [SRC-0090]
- If $t_0$ is large enough to eliminate bias, the remaining timeseries is stationary and time-reversible, and the mean squared error reduces to $\sigma_{t_0}^2/(T_{t_0}/g_{t_0})$, i.e., the sample variance divided by the number of effectively uncorrelated samples. [SRC-0090, Eq. 9]
- The statistical inefficiency $g$ (Eq. 11) and the effective number of uncorrelated samples $N_\text{eff}(t_0) \equiv (T-t_0+1)/g_{t_0}$ can be computed from a single trajectory using the integrated autocorrelation time (Eq. 12) of the observable timeseries. [SRC-0090]
- As $t_0$ increases from zero, average statistical inefficiency $g_{t_0}$ starts large (dominated by relaxation from atypical initial conditions), drops rapidly once the system reaches its true equilibrium region, and $N_\text{eff}(t_0)$ correspondingly peaks near the true equilibration time; bias is essentially eliminated at that peak. [SRC-0090, Figure 2]
- The proposed algorithm is simply: pick $t_0^\text{opt} = \arg\max_{t_0} N_\text{eff}(t_0) = \arg\max_{t_0} (T-t_0+1)/g_{t_0}$ (Eq. 14), using only the single trajectory being analyzed. [SRC-0090]
- Applied per-realization (without knowledge of the other 499 replicates), this individualized $t_0$ selection achieves an RMS error only about 11% worse than the best possible *fixed* $t_0$ chosen with full knowledge of the bias-variance trade-off across all 500 replicates (0.00173 vs. 0.00152), and dramatically better than using all data without discarding any (0.00441, about 290% worse). [SRC-0090, Figure 4]
- The same scheme performs equivalently well for the reduced potential energy $u^*(x) \equiv \beta[u(x)+pV(x)]$ (the isothermal-isobaric reduced potential), showing the approach generalizes across observables. [SRC-0090, Figure 5]
- The method requires no distributional assumptions about the observable and needs only the saved scalar timeseries $\{a_t\}_{t=1}^T$, not full configurations. [SRC-0090]
- The author explicitly warns of two failure modes: (1) if the simulation is not long enough to reach equilibrium, no choice of $t_0$ can produce an unbiased estimate; (2) if there is insufficient data to estimate the statistical inefficiency well, the algorithm's $t_0$ estimate will be poor, but in that case the trajectory itself should be suspect regardless of this method. [SRC-0090]
- Robust computation of $g$ from a finite timeseries is nontrivial: naive replacement of expectations in $C_t$ (Eq. 13) by sample estimates lets estimation error in $C_t$ grow with lag $t$ and dominate the sum in Eq. 12, so practical estimators (e.g., Geyer's initial sequence methods, or the "fast multiscale method" used in the reference implementation) truncate or otherwise control this noise. [SRC-0090, "Practical Computation of Statistical Inefficiencies"]

## Key equations

Expectation of interest and finite-timeseries estimator:

$$
\langle A \rangle \equiv \int dx\, A(x)\pi(x),
\qquad
\hat A_{[1,T]} \equiv \frac{1}{T}\sum_{t=1}^{T} a_t .
$$

[SRC-0090, eqs. 1-2]

Estimator after discarding samples before $t_0$:

$$
\hat A_{[t_0,T]} \equiv \frac{1}{T-t_0+1}\sum_{t=t_0}^{T} a_t .
$$

[SRC-0090, eq. 3]

Bias-variance decomposition of the expected squared error:

$$
\delta^2 \hat A_{[t_0,T]}
= \operatorname{var}_{x_0}\!\big(\hat A_{[t_0,T]}\big)
+ \operatorname{bias}_{x_0}^2\!\big(\hat A_{[t_0,T]}\big),
$$

$$
\operatorname{var}_{x_0}(\hat A) \equiv E_{x_0}\!\big[(\hat A - E_{x_0}[\hat A])^2\big],
\qquad
\operatorname{bias}_{x_0}^2(\hat A) \equiv \big(E_{x_0}[\hat A]-\langle A\rangle\big)^2 .
$$

[SRC-0090, eqs. 4-7]

Error once bias is eliminated (stationary, time-reversible production segment):

$$
\delta^2 \hat A_{[t_0,T]}^{\text{equil}} \equiv \frac{\sigma_{t_0}^2}{T_{t_0}/g_{t_0}},
\qquad
T_{t_0} \equiv T-t_0+1 .
$$

[SRC-0090, eq. 9]

Statistical inefficiency, integrated autocorrelation time, and normalized fluctuation autocorrelation function:

$$
\sigma^2 \equiv \langle a_t^2\rangle - \langle a_t\rangle^2,
\qquad
g \equiv 1+2\tau_{ac},
$$

$$
\tau_{ac} \equiv \sum_{t=1}^{T-1}\Big(1-\frac{t}{T}\Big)C_t,
\qquad
C_t \equiv \frac{\langle a_n a_{n+t}\rangle - \langle a_n\rangle^2}{\langle a_n^2\rangle - \langle a_n\rangle^2}.
$$

[SRC-0090, eqs. 10-13]

Optimal-equilibration-time selection rule (the core algorithm):

$$
t_0^{\text{opt}} = \operatorname*{arg\,max}_{t_0} N_\text{eff}(t_0)
= \operatorname*{arg\,max}_{t_0} \frac{T-t_0+1}{g_{t_0}} .
$$

[SRC-0090, eq. 14]

## Equation inventory

| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |
| $\langle A\rangle$, $\hat A_{[1,T]}$ | SRC-0090, eqs. 1-2 | This page | Defines target expectation and naive full-trajectory estimator. | $A(x)$, $\pi(x)$, $a_t$, $T$ | Baseline (biased) estimator. |
| $\hat A_{[t_0,T]}$ | SRC-0090, eq. 3 | This page | Estimator after discarding $[0,t_0)$. | $t_0$, $T$ | Production-region average. |
| Bias-variance decomposition | SRC-0090, eqs. 4-7 | This page | Splits mean squared error into variance and bias-squared. | $\delta^2\hat A$, $\operatorname{var}_{x_0}$, $\operatorname{bias}_{x_0}^2$ | Motivates the trade-off the algorithm optimizes. |
| Equilibrated error formula | SRC-0090, eq. 9 | This page | Error once bias is eliminated, in terms of variance and $N_\text{eff}$. | $\sigma_{t_0}^2$, $T_{t_0}$, $g_{t_0}$ | Justifies maximizing $N_\text{eff}$. |
| $\sigma^2$, $g$, $\tau_{ac}$, $C_t$ | SRC-0090, eqs. 10-13 | This page; [[wiki/concepts/statistical-inefficiency-and-automated-equilibration-detection]] | Defines statistical inefficiency from the autocorrelation function. | $\sigma^2$, $g$, $\tau_{ac}$, $C_t$ | Core quantity computed from the timeseries. |
| $t_0^\text{opt}$ | SRC-0090, eq. 14 | This page; [[wiki/concepts/statistical-inefficiency-and-automated-equilibration-detection]] | Selects equilibration time by maximizing $N_\text{eff}(t_0)$. | $t_0$, $N_\text{eff}$, $g_{t_0}$ | The paper's automated algorithm; implemented as `pymbar.timeseries.detectEquilibration()`. |

## Algorithmic recursions

The algorithm as stated is a direct search: for a candidate set of $t_0$ values (in the reference implementation, one candidate per available sample index), compute the statistical inefficiency $g_{t_0}$ of the timeseries restricted to $[t_0,T]$ via Eqs. 12-13, form $N_\text{eff}(t_0)=(T-t_0+1)/g_{t_0}$, and return the $t_0$ that maximizes $N_\text{eff}$. [SRC-0090, eq. 14]

The paper does not reproduce the internal recursion of the "fast multiscale" statistical-inefficiency estimator it actually uses; it only states that this estimator behaves equivalently to Geyer's initial-sequence estimators in the tested cases. [SRC-0090, "Practical Computation of Statistical Inefficiencies"] The estimator itself (cited to "section 5.2 of ref 10," i.e., Chodera, Swope, Pitera, Seok, and Dill, J. Chem. Theory Comput. 2007, 3, 26-41) is now ingested and fully reproduced, including its lag-schedule and truncation rule, at [[wiki/sources/SRC-0091-use-of-the-weighted-histogram-analysis-method-for]], section "Section 5.2: computing integrated correlation times." [SRC-0091]

## Evidence

- 500 replicate liquid-argon (Lennard-Jones fluid, OpenMM 6.3) simulations initiated from the same atypical dense initial configuration establish ground-truth bias/variance behavior as a function of $t_0$ for both reduced density and reduced potential energy. [SRC-0090, Figures 1-2, 5]
- The bias-variance trade-off (Figure 3) shows that per-trajectory $t_0$ selection by maximizing $N_\text{eff}$ (black triangle) lands close to the Pareto-optimal point identifiable only with knowledge of all 500 replicates. [SRC-0090, Figure 3]
- RMS error comparison (Figure 4): fixed-$t_0$ minimum RMS error 0.00152 $\pm$ 0.00005 (at $t_0\sim100\tau$, only determinable with multiple realizations) versus 0.00173 $\pm$ 0.00005 for the per-trajectory automated scheme (11% worse) versus 0.00441 $\pm$ 0.00007 for using all data without discarding (290% worse). [SRC-0090]
- The reduced-potential-energy analysis (Figure 5) reproduces the same qualitative and quantitative behavior, supporting generality across observables. [SRC-0090]

## Limitations and Caveats

- The method assumes the observable timeseries, once past $t_0$, is stationary and time-reversible; it does not assume any particular marginal distribution for the observable. [SRC-0090]
- If the simulation has not run long enough to reach equilibrium at all, no choice of $t_0$ can remove the bias; the method cannot detect this failure mode by itself. [SRC-0090]
- If there is too little data to estimate the statistical inefficiency reliably, the estimated $t_0$ will be poor, though the author notes this scenario should itself be treated as suspect (insufficient sampling), independent of the equilibration-detection method. [SRC-0090]
- Robust estimation of the statistical inefficiency $g$ from a finite, noisy autocorrelation function is a nontrivial sub-problem; the paper surveys several competing estimators (Geyer's initial convex/positive sequence methods; the "fast multiscale" method used for the paper's own results) without deriving them in full, and notes they "may not perform well for all problems." [SRC-0090]
- Demonstrated only on a simple, single-component Lennard-Jones liquid; behavior on biomolecular systems with highly non-Gaussian, multimodal, or slowly interconverting observables is asserted by analogy, not separately benchmarked in this paper. [SRC-0090]

## Links

- [[wiki/concepts/statistical-inefficiency-and-automated-equilibration-detection]]
- [[wiki/sources/SRC-0023-statistically-optimal-analysis-multiple-equilibrium-states-mbar]]
- [[wiki/concepts/multistate-bennett-acceptance-ratio]]
- [[wiki/entities/authors/john-d-chodera]]
- [[wiki/sources/SRC-0091-use-of-the-weighted-histogram-analysis-method-for]] - ref 10, cited by name for its section 5.2 "fast multiscale" statistical-inefficiency estimator; now ingested and fully reproduced there.

## Claims

- [[wiki/claims/CLM-0045-neff-maximization-gives-near-optimal-equilibration-time]] - Maximizing the single-trajectory effective-sample-size estimate over candidate equilibration times gives a near bias-optimal, distribution-free automated equilibration-time choice, but it inherits the underlying statistical-inefficiency estimator's data requirements. [SRC-0090]

## Questions

- (none added; see Open Questions below, kept source-local)

## Tensions

- (none identified; no contradiction with other ingested sources was found)

## Open Questions

- How does the automated $N_\text{eff}$-maximization scheme behave on strongly non-Gaussian, multimodal, or metastable biomolecular observables, where a single simulation may not sample all relevant states even after nominal "equilibration"? [SRC-0090]
- How sensitive is the final $t_0^\text{opt}$ choice to which statistical-inefficiency estimator (fast multiscale vs. Geyer initial sequence methods) is used on a given finite timeseries? [SRC-0090]

## Citation links

- Footnote 11 of SRC-0090 cites "Shirts, M. R.; Chodera, J. D. J. Chem. Phys. 2008, 129, 124105" for the definition of the isothermal-isobaric reduced potential $u^*(x)=\beta[u(x)+pV(x)]$; this is a strong (author + year + journal + volume + page) match to the already-ingested [[wiki/sources/SRC-0023-statistically-optimal-analysis-multiple-equilibrium-states-mbar]]. Recorded in frontmatter `cites_sources`. [SRC-0090]
- Reference (10), "Chodera, J. D.; Swope, W. C.; Pitera, J. W.; Seok, C.; Dill, K. A. J. Chem. Theory Comput. 2007, 3, 26-41," is a strong (author list + journal + year + volume + page) match to the now-ingested [[wiki/sources/SRC-0091-use-of-the-weighted-histogram-analysis-method-for]]. The in-text citation explicitly names "section 5.2 of ref 10" as the source of the "fast multiscale" statistical-inefficiency estimator. Recorded in frontmatter `cites_sources`. [SRC-0090; SRC-0091]
- The remaining 15 references (RCA method, Geyer's initial-sequence theory, OpenMM, and others) were not individually checked against the current source list; `citation_match_status` remains `partial`.

## Mathematical gaps

- ~~The internal recursion of the "fast multiscale" statistical-inefficiency estimator actually used to produce the paper's numerical results (cited to section 5.2 of ref 10) is not reproduced here.~~ Resolved: this estimator (lag schedule $t_i=1+i(i-1)/2$, gap-weighted summation, and truncation at the first zero-crossing of $C_t$) is now fully reproduced at [[wiki/sources/SRC-0091-use-of-the-weighted-histogram-analysis-method-for]], section "Section 5.2: computing integrated correlation times." SRC-0090's own characterization of it (equivalent to Geyer estimators in the tested case, fast, not guaranteed optimal for all problems) remains recorded here and is preserved as SRC-0090's own claim, distinct from SRC-0091's text. [SRC-0090; SRC-0091]
- Geyer's initial convex sequence (ICS) and initial positive sequence (IPS) estimators, and the theorem (Geyer 1992, theorem 3.1) establishing positivity/monotonicity/convexity properties of $\Gamma_k$, are mentioned but not derived; consult SRC-0090's cited references 15-16 directly if the derivation is needed. SRC-0091 does not derive or name these either; it independently proposes its own zero-crossing truncation rule.
- The full derivation of Eq. 9 from Eq. 8 (the intermediate double-sum expansion, Eq. 8, splitting variance and cross-correlation terms) is summarized rather than reproduced step-by-step.

## Ingestion QA

### Retrieval questions checked

- What problem does this paper solve, and why does it matter for MD post-processing? Answered above (Summary, Key Points).
- What is the proposed automated equilibration-time selection rule? Answered (Eq. 14; Key equations).
- How is statistical inefficiency / effective sample size defined and estimated? Answered (Eqs. 10-13; noted practical-estimation caveats).
- What evidence supports the method's performance? Answered (Evidence: liquid-argon density and reduced-potential benchmarks, RMS error comparison).
- What are the method's stated limitations and failure modes? Answered (Limitations and Caveats).
- How does this relate to other ingested free-energy/reweighting sources? Answered via the confirmed citation link to SRC-0023 and the shared "decorrelate before trusting covariance estimates" concern already recorded on [[wiki/concepts/multistate-bennett-acceptance-ratio]].
- Is this paper referenced by or does it inform current FFRefine project work? Checked: no current mention of equilibration detection, statistical inefficiency, or `detectEquilibration` in the FFRefine answer notes as of this ingestion; no link was forced into that material.

### Coverage decision

Complete at `coverage_profile: math-standard`. The central problem statement, bias-variance framework, statistical-inefficiency/effective-sample-size definitions, and the automated selection algorithm (the paper's main contribution) are captured with equation-level fidelity; the underlying finite-sample statistical-inefficiency estimator internals are recorded as an explicit gap rather than reconstructed. [SRC-0090]

### Known gaps

- ~~The "fast multiscale" statistical-inefficiency estimator implementation detail is not reproduced.~~ Resolved by ingesting [[wiki/sources/SRC-0091-use-of-the-weighted-histogram-analysis-method-for]] (ref 10), which fully documents section 5.2's lag-schedule and truncation rule.
- Full bibliography citation matching beyond footnote 11 and reference 10 was not performed; 15 references remain unchecked against the current source list (`citation_match_status: partial`).
- No current FFRefine or TSS project material was found to explicitly use this equilibration-detection method; the link to the wider knowledge base is topical (shared MBAR/decorrelation concern) rather than a documented project dependency.
