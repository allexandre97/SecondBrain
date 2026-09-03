---
type: source
status: active
created: 2026-09-03
updated: 2026-09-03
source_id: SRC-0078
display_title: "Predictive all-atom simulations of disordered proteins and biomolecular condensates through osmometry-guided force-field optimization"
short_title: "Osmometry-Guided Force-Field Optimization"
aliases:
  - "SRC-0078"
  - "Osmometry-Guided Force-Field Optimization"
  - "Predictive All-Atom Condensate Simulations"
source_path: raw/sources/SRC-0078-predictive-all-atom-simulations-of-disordered-proteins-and.pdf
imported_path: raw/sources/SRC-0078-predictive-all-atom-simulations-of-disordered-proteins-and.pdf
original_filename: "2026.08.25.747127v1.full.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: becab1e8f78a3d6226c455c60c995bbba13500fcc4f64971e13190ca4046d716
authors:
  - "Miloš T. Ivanović"
  - "Valentin von Roten"
  - "Benjamin Schuler"
  - "Robert B. Best"
author_entities: []
year: 2026
venue: "bioRxiv preprint"
doi: "10.64898/2026.08.25.747127"
arxiv:
metadata_review_status: reviewed
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/molecular-simulation/molecular-dynamics
  - research/biomolecules/proteins
  - research/experimental-benchmarking
tags:
  - scientific-paper
  - preprint
  - math-heavy
  - osmotic-pressure
  - intrinsically-disordered-proteins
  - biomolecular-condensates
  - charge-interactions
  - Lennard-Jones
  - FRET
  - NMR
  - nsFCS
related:
  - "[[wiki/concepts/osmometry-guided-force-field-optimization]]"
  - "[[wiki/concepts/force-field-training-from-experimental-observables]]"
  - "[[wiki/concepts/protein-force-field-benchmark-datasets]]"
  - "[[wiki/claims/CLM-0041-osmometry-calibrated-charge-interactions-transfer-to-complex-protein-systems]]"
  - "[[wiki/claims/CLM-0042-lennard-jones-refinement-outperforms-charge-scaling-after-shared-osmometry-fit]]"
  - "[[wiki/questions/QST-0008-osmometry-guided-protein-nucleic-acid-transfer]]"
  - "[[wiki/tensions/TEN-0006-observable-fitting-gain-vs-transferability-tradeoff]]"
sources:
  - SRC-0078
cites_sources: []
citation_match_status: partial
cqt_review_status: linked
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: math-standard
peer_review_status: not-peer-reviewed
license: CC-BY-NC-ND-4.0
---

# Predictive All-Atom Simulations of Disordered Proteins and Biomolecular Condensates Through Osmometry-Guided Force-Field Optimization

Source ID: `SRC-0078`

## Raw source

- Repository path: `raw/sources/SRC-0078-predictive-all-atom-simulations-of-disordered-proteins-and.pdf`
- Open raw source: [raw/sources/SRC-0078-predictive-all-atom-simulations-of-disordered-proteins-and.pdf](../../raw/sources/SRC-0078-predictive-all-atom-simulations-of-disordered-proteins-and.pdf)

## Summary

Ivanović et al. introduce an experimental force-field calibration workflow that uses concentration-dependent osmotic pressures of solutions containing charged amino acids and monovalent ions to isolate residue–residue, residue–ion, and ion–ion interactions. Small all-atom simulations reproduce the experimental compositions with virtual semipermeable walls, allowing candidate electrostatic and Lennard-Jones parameters to be screened before expensive protein simulations. [SRC-0078, abstract and pp. 4–8]

Two parameter routes fit the osmometry benchmark: Amber ff99SBws-CS scales charged side chains and monovalent ions to net charges of $\pm 0.93e$, with limited ion–water Lennard-Jones adjustments; Amber ff99SBws-LJ retains integral charges and instead adjusts residue–water, ion, and pair-specific ion–ion Lennard-Jones terms. Only the LJ route consistently improved transfer validation across 16 monomeric intrinsically disordered regions (IDRs), the ProTα–histone-H1 complex, and ProTα condensates formed with H1 or protamine. [SRC-0078, pp. 9–18]

The strongest improvement occurred for arginine-rich condensates, where the original model made ProTα reconfiguration more than an order of magnitude slower than experiment. The authors connect the improvement to shorter transient contacts after weakening over-stabilized charged interactions. The paper is a bioRxiv preprint and several condensate kinetic estimates do not pass its Chapman–Kolmogorov convergence criterion, so its quantitative transfer claims remain system- and analysis-specific. [SRC-0078, pp. 16–19 and 34–36]

## Calibration and optimization

- New vapor-pressure-osmometry measurements cover Lys–Glu, Lys–Asp, Arg–Glu, Arg–Asp, Asp–Na$^+$, and Asp–K$^+$; literature data complete the residue–ion and NaCl/KCl benchmark. Measurements span concentrations because errors that are small in the dilute limit can accumulate at higher concentration. [SRC-0078, pp. 6–8 and 20–21]
- Experimental association strength is chemically specific: the reported amino-acid ordering is Arg–Asp $>$ Arg–Glu $>$ Lys–Asp $>$ Lys–Glu. The original ff99SBws model is especially too attractive for arginine/sodium combinations with anionic amino acids. [SRC-0078, pp. 6–9]
- Charge scaling reduced the four residue-pair unreduced $\chi^2$ from 45.6 to 7.1 at $|q|=0.93e$ but still needed ion–water diameter corrections. [SRC-0078, p. 10]
- A uniform 1% residue–water diameter reduction lowered the same $\chi^2$ to 6.0; residue-specific changes lowered it to 4.5. The selected diameter factors were 0.99 for lysine, 0.985 for arginine, 0.99 for aspartate, and 0.995 for glutamate. [SRC-0078, p. 11]
- Pair-specific Na$^+$–Cl$^-$ and K$^+$–Cl$^-$ corrections were required so improvements to residue–ion interactions did not create unrealistic concentrated-electrolyte coordination. [SRC-0078, pp. 11–12]

## Validation evidence

- Across 16 equal-length, sequence-diverse IDRs, the concordance correlation coefficient between simulated and experimental mean FRET efficiency was 0.84 for the original model, 0.83 for the charge-scaled model, and 0.91 for the LJ-refined model. The largest LJ improvements were in charge-rich sequences. [SRC-0078, pp. 12–14 and Fig. 3]
- For disordered ProTα bound to the folded globular domain of histone H1, the LJ model improved residue-resolved $R_1$ and $R_2$ NMR relaxation and reduced the mean ProTα–H1 contact lifetime from $12.0 \pm 1.0$ ns to $6.3 \pm 0.4$ ns. [SRC-0078, pp. 14–16 and Fig. 4]
- Four condensates combined ProTα with lysine-rich H1 or arginine-rich protamine at 8 or 128 mM KCl in systems of 2.6–4.0 million atoms. LJ refinement preserved or improved mean-FRET agreement, reduced restricted ProTα chains in the 128 mM H1 condensate from 23 of 96 to 10 of 96, and substantially improved the arginine-rich reconfiguration times. [SRC-0078, pp. 16–18 and Fig. 5]
- Intermolecular contact lifetime correlates with ProTα reconfiguration time under both force fields, supporting the interpretation that transient contacts contribute effective friction to chain motion. [SRC-0078, pp. 17–18 and Fig. S8]

## Limitations and validation boundaries

- Calibration-equivalent parameterizations were not transfer-equivalent: the CS model fit osmometry but did not improve the 16-IDR FRET benchmark. The calibration target alone therefore did not select the better transferable model. [SRC-0078, pp. 10–14]
- Parameter changes are specific to Amber ff99SBws with TIP4P/2005 water and the stated monovalent-ion baseline; the work does not establish the same corrections for other force-field/water combinations. [SRC-0078, pp. 8–12 and Methods]
- The paper tests charged protein systems but not the proposed protein–DNA or protein–RNA applications. [SRC-0078, p. 19]
- Several condensate reconfiguration analyses did not pass the CK test and are reported as best-effort, not-converged estimates. Original-force-field trajectories were also substantially shorter in some paired comparisons and may underestimate its reconfiguration times. [SRC-0078, pp. 34–36]
- The low-salt ProTα–protamine simulation at 8 mM KCl is compared with the nearest feasible experiment at 25 mM added KCl rather than an exactly matched condition. [SRC-0078, Fig. 5]
- The source is a preprint that was not peer reviewed at the version ingested. [SRC-0078, PDF header]

## Mathematical structure

The paper first relates osmotic pressure to net interaction strength, then estimates simulated pressure mechanically from virtual-wall forces. Parameter scans minimize a global discrepancy across interaction pairs and concentrations. Transfer tests use FRET forward models, NMR relaxation, contact lifetimes, and a one-dimensional Smoluchowski model of chain-distance dynamics. A bootstrap-calibrated Chapman–Kolmogorov score selects acceptable lag times for kinetic estimates. [SRC-0078, pp. 6–12 and 20–35]

## Key equations

For non-interacting solute particles, ideal osmotic pressure and the osmotic coefficient are [SRC-0078, pp. 6–7]:

$$
\Pi_{\mathrm{ideal}} = c_{\mathrm{tot}}RT,
\qquad
\phi = \frac{\Pi}{\Pi_{\mathrm{ideal}}},
\qquad
c_{\mathrm{tot}}=\sum_i c_i.
$$

In the virtual-semipermeable-wall simulations, pressure is the average restoring force on the two walls divided by twice their cross-sectional area [SRC-0078, eq. 1, p. 23]:

$$
\Pi = \frac{\langle F_+ + F_-\rangle}{2A}.
$$

The transfer-efficiency forward model used for condensate ProTα is [SRC-0078, eqs. 2–3, p. 31]:

$$
E(r)=\frac{R_0^6}{R_0^6+r^6},
\qquad
r=d\left(\frac{N+9}{N}\right)^\nu,
$$

with $R_0=5.9$ nm and $\nu=0.6$ for the stated labeling geometry. The likelihood for a discretized one-dimensional Smoluchowski model is [SRC-0078, eq. 4, p. 32]:

$$
\ln L = \sum_{i,j} N_{ji}(\Delta t)\ln\left(\exp[\Delta tK]\right)_{ji}.
$$

The CK score compares model-predicted and empirical transition matrices against a bootstrap finite-sampling threshold [SRC-0078, eqs. 6–7, pp. 33–34]:

$$
d_m = \sum_i w_i\frac{1}{2}\sum_j
\left|T^{\mathrm{emp}}_{ji}(m\Delta t)-T^{\mathrm{model}}_{ji}(m\Delta t)\right|,
\qquad m\in\{2,3,4\},
$$

$$
S_{\mathrm{CK}}=\max_{m=2,3,4}\frac{d_m}{q^{\mathrm{boot}}_{95,m}},
$$

with acceptance at $S_{\mathrm{CK}}\leq 1$.

## Variable glossary

- $\Pi$, $\Pi_{\mathrm{ideal}}$, $\phi$: simulated/measured osmotic pressure, ideal osmotic pressure, and osmotic coefficient.
- $c_i$, $c_{\mathrm{tot}}$, $R$, $T$: species and total solute concentration, molar gas constant, and absolute temperature.
- $F_+$, $F_-$, $A$: instantaneous wall-force magnitudes and wall cross-sectional area.
- $E$, $r$, $d$, $R_0$, $N$, $\nu$: FRET efficiency, estimated interdye distance, Cα distance, Förster radius, labeling-site sequence separation, and linker correction exponent.
- $N_{ji}$, $K$, $\Delta t$: observed transition counts, discretized rate matrix, and lag time.
- $T^{\mathrm{emp}}$, $T^{\mathrm{model}}$, $w_i$: empirical/model transition matrices and origin-bin populations.
- $d_m$, $q^{\mathrm{boot}}_{95,m}$, $S_{\mathrm{CK}}$: predictive discrepancy, bootstrap noise threshold, and CK acceptance score.

## Equation inventory

| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |
| Ideal osmotic pressure and coefficient | SRC-0078, pp. 6–7 | This page; osmometry concept | Relates departures from ideality to net interactions. | $\Pi$, $\phi$, $c_i$, $R$, $T$ | Defines the calibration observable. |
| Experimental uncertainty | SRC-0078, p. 21 | Mathematical gaps below | Combines 1% instrument error and calibration tolerance. | $\sigma_\Pi$, $\Pi$ | Weights experimental uncertainty. |
| Virtual-wall pressure | SRC-0078, eq. 1, p. 23 | This page; osmometry concept | Converts restoring force into pressure. | $F_+$, $F_-$, $A$ | Core simulation estimator. |
| FRET efficiency and linker correction | SRC-0078, eqs. 2–3, p. 31 | This page | Maps simulation distances to the measured observable. | $E$, $r$, $d$, $R_0$, $N$, $\nu$ | Required for condensate FRET comparison. |
| Smoluchowski likelihood | SRC-0078, eq. 4, p. 32 | This page | Fits free energies and a constant diffusion coefficient from transitions. | $N_{ji}$, $K$, $\Delta t$ | Kinetic parameter inference. |
| Reconfiguration time | SRC-0078, eq. 5, p. 33 | Mathematical gaps below | Computes $\tau_c$ from nonstationary rate-matrix modes. | $\lambda_n$, $\Psi_n^R$, $r$ | Converts the fitted kinetic model into the reported timescale. |
| CK discrepancy and score | SRC-0078, eqs. 6–7, pp. 33–34 | This page | Tests longer-lag transition predictions against sampling noise. | $T$, $w_i$, $d_m$, $q_{95,m}^{\mathrm{boot}}$ | Selects/report flags for lag-dependent estimates. |

## Proof map

There are no theorem proofs. The methodological chain is: define concentration-dependent osmometry targets; implement and validate the virtual-wall pressure estimator against Luo–Roux salt simulations; tune two parameter families; check electrolyte coordination to prevent compensating artifacts; transfer parameters without further adjustment; and evaluate structure/dynamics with increasingly complex held-out systems. The kinetic analysis then fits a rate matrix, predicts longer-lag transitions, bootstraps finite-sampling discrepancies, and accepts or flags reconfiguration estimates through $S_{\mathrm{CK}}$. [SRC-0078, pp. 5–19 and 22–36]

## Implementation notes

- Match experimental and simulated solution composition over a concentration series, not only a single state point. [SRC-0078, pp. 5–8]
- In GROMACS, the paper implements semipermeable walls as flat-bottomed position restraints normal to $z$; ions are restrained directly and amino acids through Cα while water remains unrestrained. [SRC-0078, pp. 22–23]
- Validate residue–ion corrections jointly with concentrated ion–ion coordination and osmotic pressure so one subsystem is not improved by creating an electrolyte artifact. [SRC-0078, pp. 11–12 and 26]
- Treat calibration fit and transfer validation as separate gates. Agreement on osmometry did not make CS and LJ parameterizations equivalent on protein benchmarks. [SRC-0078, pp. 9–18]
- Preserve CK pass/fail status and trajectory-length asymmetry with every reported reconfiguration time. [SRC-0078, pp. 33–36]

## Mathematical gaps

- The full reconfiguration-time eigenmode expression (eq. 5) is not reproduced because PDF text extraction leaves its vector contractions ambiguous; consult the raw PDF before implementation.
- Supplementary figures/tables and the complete force-field files are not present in the supplied PDF. The source points to Zenodo DOI `10.5281/zenodo.20031526` for numerical source data and optimized parameters. [SRC-0078, p. 36]
- The optimization is described as iterative scans rather than a single general differentiable objective/algorithm; no proof of parameter identifiability or uniqueness is given. [SRC-0078, pp. 9–12]

## Claims

- [[wiki/claims/CLM-0041-osmometry-calibrated-charge-interactions-transfer-to-complex-protein-systems]]
- [[wiki/claims/CLM-0042-lennard-jones-refinement-outperforms-charge-scaling-after-shared-osmometry-fit]]

## Questions

- [[wiki/questions/QST-0008-osmometry-guided-protein-nucleic-acid-transfer]]

## Tensions

- [[wiki/tensions/TEN-0006-observable-fitting-gain-vs-transferability-tradeoff]]

## Links

- [[wiki/concepts/osmometry-guided-force-field-optimization]]
- [[wiki/concepts/force-field-training-from-experimental-observables]]
- [[wiki/concepts/protein-force-field-benchmark-datasets]]

## Metadata notes

- Bibliographic metadata was checked against the title page and PDF header: bioRxiv version posted 26 August 2026, DOI `10.64898/2026.08.25.747127`, four listed authors, and not certified by peer review.
- The ingested 45-page PDF contains the main paper, methods, and references. Supplementary figures and tables are cited but not included; because no separate supplement was provided, this remains a single-source ingestion rather than a source bundle.
- The authors state that figure source data, osmometry data, and optimized parameter files are available separately on Zenodo. That external deposit was not part of the requested source and was not ingested. [SRC-0078, p. 36]

## Citation links

- The reference list was inspected for exact matches to currently ingested sources. No match was accepted; `cites_sources` remains empty.
- Citation matching is partial because the review targeted force-field optimization, osmometry, and condensate references rather than independently resolving every bibliography entry.

## Ingestion QA

### Retrieval questions checked

- What problem does the paper address? Excessively strong charged-residue and ion interactions in additive all-atom force fields, especially for disordered proteins and condensates. [SRC-0078, pp. 2–5]
- What is the central method? Calibrate isolated residue–residue, residue–ion, and ion–ion interactions against concentration-dependent osmotic pressure from matched experiments and virtual-wall simulations. [SRC-0078, pp. 5–8 and 20–26]
- What parameterizations were produced? Charge-scaled ff99SBws-CS and integral-charge, Lennard-Jones-refined ff99SBws-LJ. [SRC-0078, pp. 9–12]
- Which model transferred better? ff99SBws-LJ, despite both variants fitting osmometry. [SRC-0078, pp. 12–19]
- What evidence supports transfer? FRET for 16 IDRs, NMR relaxation/contact kinetics for ProTα–H1, and FRET/nsFCS reconfiguration for four multi-million-atom condensates. [SRC-0078, pp. 12–18]
- Where was the largest improvement? Arginine-rich ProTα–protamine condensates, consistent with arginine requiring the largest calibration correction. [SRC-0078, pp. 17–19]
- What are the main limitations? One force-field/water family, a non-peer-reviewed preprint, unmatched low-salt comparison, and several best-effort condensate kinetic estimates that fail the CK test. [SRC-0078, Fig. 5 and pp. 34–36]
- What future application is proposed? Osmometry-guided calibration of protein–DNA and protein–RNA interactions using amino acid–nucleotide and nucleotide–ion solutions. [SRC-0078, p. 19]

### Coverage decision

Complete at `coverage_profile: math-standard`. The wiki captures the calibration observable, parameter routes, central numerical choices, multi-level transfer tests, important equations and variables, implementation logic, convergence flags, limitations, reusable claims, and future-work question.

### Known gaps

- External Zenodo data and force-field files were not requested and are not ingested.
- Supplementary figures and numerical tables cited by the paper were not included in the supplied PDF.
- Equation 5 should be recovered from the typeset PDF before direct implementation.
