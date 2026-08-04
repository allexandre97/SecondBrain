---
type: source
status: active
created: 2026-07-31
updated: 2026-07-31
source_id: SRC-0074
display_title: "Convergence Is Not Correctness: Context-Dependent Performance of Enhanced-Sampling Methods Across Biological Complexity"
short_title: "Convergence Is Not Correctness"
aliases:
  - "SRC-0074"
  - "Convergence Is Not Correctness"
  - "Context-Dependent Enhanced-Sampling Performance"
source_path: raw/sources/SRC-0074-convergence-is-not-correctness-context-dependent-performance-of.pdf
imported_path: raw/sources/SRC-0074-convergence-is-not-correctness-context-dependent-performance-of.pdf
original_filename: "s41467-026-74165-y.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: c29a694cb4099f89c759f6c45e11935d9492da88c1d78da5907e91fb8098854f
authors:
  - "Christopher Kang"
  - "Cheng Giuseppe Chen"
  - "Chenyu Tang"
  - "Sergio Contreras Arredondo"
  - "Mengchen Zhou"
  - "Haohao Fu"
  - "Lan Yang"
  - "James C. Gumbart"
  - "Ashkan Fakharzadeh"
  - "Mahmoud Moradi"
  - "Haochuan Chen"
  - "Rui Sun"
  - "Jonathan Harris"
  - "Benoit Roux"
  - "Christophe Chipot"
author_entities: []
year: 2026
venue: "Nature Communications"
doi: "10.1038/s41467-026-74165-y"
arxiv:
metadata_review_status: reviewed
areas:
  - research
categories:
  - research/adaptive-sampling
  - research/molecular-simulation/free-energy
  - research/molecular-simulation/molecular-dynamics
  - research/experimental-benchmarking
tags:
  - enhanced-sampling
  - convergence-diagnostics
  - cross-method-validation
  - reus
  - well-tempered-metadynamics
  - wtm-eabf
  - opes
  - math-heavy
related:
  - "[[wiki/concepts/enhanced-sampling-validation]]"
  - "[[wiki/concepts/adaptive-enhanced-sampling]]"
  - "[[wiki/concepts/on-the-fly-probability-enhanced-sampling]]"
  - "[[wiki/concepts/free-energy-estimation]]"
sources:
  - SRC-0074
cites_sources:
  - SRC-0010
  - SRC-0023
citation_match_status: partial
cqt_review_status: linked
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: math-standard
---

# Convergence Is Not Correctness: Context-Dependent Performance of Enhanced-Sampling Methods Across Biological Complexity

Source ID: `SRC-0074`

## Raw source

- Repository path: `raw/sources/SRC-0074-convergence-is-not-correctness-context-dependent-performance-of.pdf`
- Open raw source: [raw/sources/SRC-0074-convergence-is-not-correctness-context-dependent-performance-of.pdf](../../raw/sources/SRC-0074-convergence-is-not-correctness-context-dependent-performance-of.pdf)

## Summary

This Nature Communications benchmark compares replica-exchange umbrella sampling (REUS), well-tempered metadynamics (WT-MtD), well-tempered metadynamics-extended adaptive-biasing force (WTM-eABF), and on-the-fly probability enhanced sampling (OPES) on five biomolecular free-energy landscapes. The assays span one-dimensional ligand dissociation, membrane permeation, and ion conduction, plus two-dimensional ligand-coupled conformational change and kinase activation. [SRC-0074, pp. 1-3]

The main result is diagnostic rather than a universal ranking: a free-energy landscape can become stable relative to its own final estimate while remaining inconsistent with other methods and long reference simulations. Within this five-system benchmark, REUS was most economical for the three well-defined one-dimensional coordinates, WTM-eABF was most robust for the two multidimensional landscapes, WT-MtD was useful for exploration but fragile on a rugged kinase landscape, and OPES was competitive when its barrier parameter was appropriate but could self-converge to an incorrect profile when it was not. [SRC-0074, pp. 8-10]

The authors therefore recommend reporting cross-method agreement or an independent extended-timescale reference alongside self-convergence. These prescriptions are evidence from a deliberately varied but still small benchmark, not proofs that the same method ordering applies to every system or implementation. [SRC-0074, pp. 9-10]

## Benchmark design

| Process | Landscape / coordinate | Main observed boundary |
| --- | --- | --- |
| Abl-SH3:p41 dissociation | One-dimensional center-of-mass separation | All methods recovered a bound basin, but some OPES barrier settings self-converged to profiles inconsistent with the other methods. [SRC-0074, pp. 2-4] |
| Ribose binding to RBP | Two-dimensional hinge angle and ligand distance | WTM-eABF recovered the common HC, HO, and AO basins; REUS retained a seeded low-free-energy corridor shifted toward an AC state. [SRC-0074, pp. 4-5 and 9] |
| BCR-Abl1 DFG flip | Two-dimensional dihedral landscape | WT-MtD did not self-converge within 2.0 microseconds; REUS topology converged but its basin difference retained initialization bias; WTM-eABF was the most consistent. [SRC-0074, pp. 5-6 and 9] |
| Dideoxyadenosine membrane permeation | One-dimensional membrane-normal displacement | REUS reached consensus fastest; low OPES barrier settings produced qualitatively incorrect central hysteresis despite internal stability. [SRC-0074, pp. 6-7 and 9-10] |
| Sodium permeation through nAChR | One-dimensional channel-axis displacement | REUS self-converged fastest; all methods resolved the main barriers, with method-specific height differences and an ion-occupancy caveat. [SRC-0074, pp. 7-9] |

All production calculations were performed independently and blindly with respect to the other methods' final landscapes. Parameters followed the authors' stated best practices. Evaluation combined a self-convergence RMSD, comparison to a method-marginalized consensus landscape, and independent multi-microsecond multiple-walker WTM-eABF trajectories. [SRC-0074, p. 2]

## Key findings

- Self-convergence is necessary but not sufficient: internal stability measures whether a profile has stopped changing, not whether it represents the correct thermodynamics. [SRC-0074, pp. 9-10 and eq. 20]
- Method performance depended more on landscape dimensionality and topology than on a single global method ranking in these assays. [SRC-0074, p. 8]
- REUS was the authors' recommended default for well-defined one-dimensional coordinates, but it requires window preparation, overlap, synchronized replicas, and representative initial structures. [SRC-0074, pp. 8-10]
- WTM-eABF was the most consistently reliable method for the two coupled or multidimensional landscapes, but it adds parameters for extended-system coupling and for the balance between eABF and metadynamics. [SRC-0074, pp. 9-10]
- OPES barrier selection is part of the validation protocol. Testing one barrier value and observing a stable profile was insufficient in the Abl-SH3 and membrane assays. [SRC-0074, pp. 9-10]
- WT-MtD is recommended as a first-pass mapper when topology is unknown, followed by a quantitative REUS or WTM-eABF refinement rather than relying on WT-MtD alone. [SRC-0074, p. 10]

## Mathematical structure

The paper reviews the four biasing methods, then defines a consensus construction and two convergence diagnostics. The validation equations below are the most distinctive mathematical contribution for retrieval. [SRC-0074, Methods]

For method $m$, the final free-energy landscape $A_m(\xi)$ is converted to a normalized probability distribution: [SRC-0074, eq. 14]

$$
P_m(\xi)=
\frac{\exp[-\beta A_m(\xi)]}
{\sum_{j=1}^{N}\exp[-\beta A_m(\xi_j)]}.
$$

Bootstrap resampling of the method-specific distributions gives a probability-space consensus, which is converted back to a landscape up to an additive constant: [SRC-0074, eqs. 15-17]

$$
P^{(b)}(\xi)=\frac{1}{M}\sum_{m\in\mathcal{M}^{(b)}}P_m(\xi),
\qquad
A^{(b)}(\xi)=-\frac{1}{\beta}\ln P^{(b)}(\xi)+A_0,
$$

$$
\langle A(\xi)\rangle=\frac{1}{B}\sum_{b=1}^{B}A^{(b)}(\xi).
$$

After removing the arbitrary additive offset, self-convergence compares the instantaneous landscape with the final landscape from the same run: [SRC-0074, eqs. 19-20]

$$
\operatorname{RMSD}_{\mathrm{self}}(t)=
\left[
\frac{1}{N}\sum_{i=1}^{N}
\left(\widetilde A(\xi_i,t)-A(\xi_i,t_\infty)\right)^2
\right]^{1/2}.
$$

Cross-method consistency instead compares the aligned instantaneous landscape with the marginalized average: [SRC-0074, eq. 21]

$$
\operatorname{RMSD}_{\mathrm{ref}}(t)=
\left[
\frac{1}{N}\sum_{i=1}^{N}
\left(\widetilde A(\xi_i,t)-\langle A(\xi_i)\rangle\right)^2
\right]^{1/2}.
$$

The study classifies a simulation as self-converged when $\operatorname{RMSD}_{\mathrm{self}}$ reaches a stable plateau no larger than $k_BT$. Agreement with the consensus and the independent long WTM-eABF runs is evaluated separately. [SRC-0074, p. 2 and Methods]

## Variable glossary

- $A_m(\xi)$: final free-energy landscape from method $m$ along collective variable $\xi$. [SRC-0074, eq. 14]
- $P_m(\xi)$: normalized probability distribution implied by $A_m$. [SRC-0074, eq. 14]
- $\beta=(k_BT)^{-1}$: inverse thermal energy. [SRC-0074]
- $M$: number of method-specific landscapes, four in this benchmark. [SRC-0074, eq. 15]
- $B$: number of bootstrap replicas. [SRC-0074, eqs. 15-18]
- $N$: number of bins on the common collective-variable grid. [SRC-0074, eqs. 14 and 19-21]
- $\widetilde A(\xi,t)$: instantaneous landscape after subtracting the mean offset that best aligns it to the reference. [SRC-0074, eq. 19]
- $t_\infty$: end of the completed trajectory used as the run's final estimate. [SRC-0074, eqs. 19-20]

## Equation inventory

| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |
| Method landscape normalization | SRC-0074, eq. 14 | This page; [[wiki/concepts/enhanced-sampling-validation]] | Removes arbitrary free-energy offsets before consensus construction. | $A_m$, $P_m$, $\beta$, $N$ | Put method outputs on a common probability grid. |
| Bootstrap marginalized average | SRC-0074, eqs. 15-18 | This page | Builds an inter-method consensus and uncertainty band. | $M$, $B$, $P^{(b)}$, $A^{(b)}$ | Cross-method comparison; not an independent ground truth. |
| Free-energy alignment | SRC-0074, eq. 19 | Summarized here | Removes the mean additive offset between two landscapes. | $A$, $\widetilde A$, $N$ | Required before profile RMSDs are meaningful. |
| Self-convergence RMSD | SRC-0074, eq. 20 | This page; [[wiki/concepts/enhanced-sampling-validation]] | Tests stability against the same run's final profile. | $\widetilde A$, $A(t_\infty)$ | Internal stopping diagnostic. |
| Reference RMSD | SRC-0074, eq. 21 | This page; [[wiki/concepts/enhanced-sampling-validation]] | Tests agreement with the method-marginalized landscape. | $\widetilde A$, $\langle A\rangle$ | External consistency diagnostic. |

## Proof map

The paper has no theorem proofs. Its argument is empirical: define matched collective variables and four production protocols; stop runs using an internal stability criterion; compare the resulting landscapes to a probability-space consensus and longer WTM-eABF calculations; identify failures where those diagnostics disagree; then infer context-specific selection and validation guidance. [SRC-0074, pp. 2-10 and Methods]

## Implementation notes

- Store self-convergence and external-reference RMSDs separately. A single `converged` flag loses the distinction tested by this paper. [SRC-0074, eqs. 20-21]
- Compare free-energy surfaces only after removing their arbitrary additive constants, preferably through normalized probabilities or explicit mean-offset alignment. [SRC-0074, eqs. 14 and 19]
- For OPES on a new system, run a barrier-parameter sensitivity series and require agreement across plausible settings or against another method. [SRC-0074, pp. 9-10]
- For multidimensional REUS, inspect whether steered initial structures impose a persistent corridor and verify window overlap and exchange, rather than relying only on the final landscape's time stability. [SRC-0074, pp. 9 and 11-15]
- For unknown landscapes, use exploration and quantitative refinement as distinct stages, with independent validation of the refined profile. [SRC-0074, p. 10]

## Evidence

- REUS met the self-convergence threshold in 0.2 microseconds for Abl-SH3:p41, 0.3 microseconds for membrane permeation, and under 0.1 microseconds for sodium conduction, faster than the other methods in the latter two one-dimensional assays. [SRC-0074, table 1 and p. 8]
- WT-MtD did not self-converge for the kinase DFG flip within its 2.0-microsecond allocation, while WTM-eABF self-converged in 1.0 microseconds and recovered a near-isoenergetic basin difference consistent with prior literature. [SRC-0074, table 1 and p. 9]
- OPES barrier values of 18 and 25 kcal/mol for Abl-SH3:p41 passed the internal threshold but disagreed with the other methods; for membrane permeation, 10 and 15 kcal/mol settings produced incorrect central hysteresis despite apparent self-consistency. [SRC-0074, pp. 9-10]
- Long multiple-walker WTM-eABF references generally agreed with the marginalized landscapes, providing a check outside the four-profile consensus construction. [SRC-0074, pp. 2-9]

## Limitations and caveats

- The benchmark contains five systems and two nominal dimensionality classes. Its recommendations should be tested on additional collective variables, force fields, implementations, and biological processes before being treated as universal. [SRC-0074, pp. 1-10]
- The marginalized average is an inter-method consensus, not ground truth; correlated errors shared by all methods or by the common collective variables can survive averaging. The authors partly address this with longer WTM-eABF trajectories. [SRC-0074, p. 2 and Methods]
- WTM-eABF is both one compared method and the independent long-trajectory reference. Longer sampling reduces finite-time bias, but the choice can still share method-specific assumptions. [SRC-0074, p. 2]
- Method settings followed stated best practices but were not exhaustively optimized. The conclusions therefore characterize the tested protocols, not every possible tuning of each algorithm. [SRC-0074, p. 2]
- REUS times are aggregate sampling across windows, while adaptive methods report total single-replica or stratified sampling. These values describe simulation effort under the paper's accounting and do not by themselves capture wall-clock time, setup effort, hardware utilization, or replica-failure risk. [SRC-0074, table 1 and pp. 8-10]
- Supplementary convergence analyses and the long-reference details are cited by the article but were not included in the user-provided file; this ingestion therefore preserves the main-paper results and records the supplement as an un-ingested retrieval gap. [SRC-0074, Data availability]

## Claims

- [[wiki/claims/CLM-0033-self-convergence-does-not-establish-free-energy-correctness]]
- [[wiki/claims/CLM-0034-enhanced-sampling-method-performance-is-context-dependent]]

## Questions

- [[wiki/questions/QST-0002-independent-validation-for-enhanced-sampling-landscapes]]

## Tensions

- [[wiki/tensions/TEN-0016-internal-convergence-vs-external-free-energy-correctness]]

## Links

- [[wiki/concepts/enhanced-sampling-validation]]
- [[wiki/concepts/adaptive-enhanced-sampling]]
- [[wiki/concepts/on-the-fly-probability-enhanced-sampling]]
- [[wiki/concepts/free-energy-estimation]]
- [[wiki/sources/SRC-0010-rethinking-metadynamics-opes]]
- [[wiki/sources/SRC-0023-statistically-optimal-analysis-multiple-equilibrium-states-mbar]]

## Citation links

- `SRC-0010`: reference 21 is an exact title, authorship, year, and journal match to "Rethinking metadynamics: from bias potentials to probability distributions," the ingested OPES paper. [SRC-0074, reference 21]
- `SRC-0023`: reference 42 is an exact title, authorship, year, and journal match to the original MBAR paper. [SRC-0074, reference 42]
- Citation review is partial: the two exact matches to already-ingested method sources were confirmed, but the full 86-reference bibliography was not normalized. [SRC-0074]

## Mathematical gaps

- The standard REUS, WT-MtD, WTM-eABF, and OPES equations (source eqs. 2-13) are summarized by their operational roles rather than reproduced in full; existing wiki pages already preserve detailed OPES and general free-energy equations. [SRC-0010] [SRC-0074, Methods]
- The bootstrap standard-deviation equation (source eq. 18) and full offset-alignment expression (source eq. 19) remain in the raw paper; the equations needed to distinguish internal and external convergence are represented above. [SRC-0074, eqs. 18-19]
- System-specific parameter tables and supplementary convergence curves remain in the raw paper or the un-ingested supplementary information. [SRC-0074]

## Ingestion QA

### Retrieval questions checked

- What four enhanced-sampling methods were compared, and on which five biomolecular processes?
- Why can a free-energy profile be self-converged but incorrect?
- Which methods performed best for the tested one-dimensional and multidimensional landscapes?
- What characteristic failure modes were observed for REUS, WT-MtD, WTM-eABF, and OPES?
- How were self-convergence, cross-method consensus, and independent references defined?
- Why must OPES barrier settings be varied on new systems?
- What workflow is recommended when the free-energy landscape topology is unknown?
- What limits the generality and independence of this benchmark?

### Coverage decision

Complete at `math-standard` depth for the main article. The source page and linked semantic pages answer the central benchmark, diagnostic, method-selection, evidence, limitation, and implementation questions. The unprovided supplementary information is an explicit gap rather than an inferred source. [SRC-0074]

### Known gaps

- Supplementary figures and detailed convergence traces were not provided or imported.
- The five complete numerical landscapes and all per-parameter profiles are left in the raw PDF rather than duplicated.
- No independent reanalysis of the Zenodo input files or source data was performed.

