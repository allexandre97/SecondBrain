---
type: source
status: active
created: 2026-06-30
updated: 2026-07-01
source_id: SRC-0061
display_title: "Large-Scale Collaborative Assessment of Binding Free Energy Calculations for Drug Discovery Using OpenFE"
short_title: "OpenFE RBFE Benchmark Journal Version"
aliases:
  - "SRC-0061"
  - "OpenFE RBFE Benchmark Journal Version"
  - "Large-Scale Collaborative Assessment of Binding Free Energy Calculations for Drug Discovery Using OpenFE"
source_path: raw/sources/SRC-0061-openfe-rbfe-benchmark-journal-version.pdf
imported_path: raw/sources/SRC-0061-openfe-rbfe-benchmark-journal-version.pdf
original_filename: "large-scale-collaborative-assessment-of-binding-free-energy-calculations-for-drug-discovery-using-openfe.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 89019fe6cdd853a058f6af326076a67554d0e501589e343bc7f688c03f1d909f
authors:
  - "Hannah M. Baumann"
  - "Joshua T. Horton"
  - "Michael M. Henry"
  - "Alyssa Travitz"
  - "Benjamin Ries"
  - "Richard J. Gowers"
  - "David W. H. Swenson"
  - "Ivan Pulido"
  - "Dominic Rufa"
  - "David L. Dotson"
  - "Nupur Bansal"
  - "Joseph P. Bluck"
  - "Howard Broughton"
  - "Kira A. Campbell"
  - "Lili Cao"
  - "Benedikt Frieg"
  - "Vytautas Gapsys"
  - "Hendrik Goddeke"
  - "Marco Klahn"
  - "Sirish Kaushik Lakkaraju"
  - "Stephanie M. Linker"
  - "Thomas Lohr"
  - "Aniket Magarkar"
  - "Sergio Perez-Conesa"
  - "Hans E. Purkey"
  - "Hayk Saribekyan"
  - "Jenke Scheen"
  - "Christina E. M. Schindler"
  - "Thomas Steinbrecher"
  - "Chaya D. Stern"
  - "Patricia Suriana"
  - "William C. Swope"
  - "Gary Tresadern"
  - "Lev Tsidilkovski"
  - "Binqing Wei"
  - "Alexander H. Williams"
  - "Yao Wu"
  - "Ivy Zhang"
  - "John D. Chodera"
  - "James R. B. Eastwood"
  - "David L. Mobley"
  - "Irfan Alibay"
author_entities:
  - "[[wiki/entities/authors/john-d-chodera]]"
year: 2026
venue: "Journal of Chemical Information and Modeling"
doi: "10.1021/acs.jcim.6c00089"
arxiv:
metadata_review_status: reviewed
areas:
  - research
categories:
  - research/molecular-simulation/free-energy
  - research/computational-drug-discovery
  - research/experimental-benchmarking
  - research/biomolecules/proteins
tags:
  - rbfe
  - openfe
  - benchmarking
  - drug-discovery
related:
  - "[[wiki/sources/SRC-0062-openfe-rbfe-benchmark-supporting-information]]"
  - "[[wiki/sources/SRC-0045-large-scale-collaborative-assessment-of-binding-free-energy]]"
  - "[[wiki/concepts/relative-binding-free-energy-benchmarking]]"
  - "[[wiki/concepts/free-energy-estimation]]"
sources:
  - SRC-0061
  - SRC-0062
cites_sources:
  - SRC-0023
  - SRC-0046
citation_match_status: partial
cqt_review_status: linked
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: math-standard
source_bundle: openfe-rbfe-benchmark-2026
bundle_role: main
---

# Large-Scale Collaborative Assessment of Binding Free Energy Calculations for Drug Discovery Using OpenFE

Source ID: `SRC-0061`

## Raw source

- Repository path: `raw/sources/SRC-0061-openfe-rbfe-benchmark-journal-version.pdf`
- Open raw source: [raw/sources/SRC-0061-openfe-rbfe-benchmark-journal-version.pdf](../../raw/sources/SRC-0061-openfe-rbfe-benchmark-journal-version.pdf)

## Summary

This J. Chem. Inf. Model. article is the journal version of the OpenFE large-scale RBFE benchmark. It evaluates the OpenFE default relative hybrid-topology protocol across 58 public protein-ligand systems and 37 blinded private industry datasets, totaling more than 1,700 ligands. [SRC-0061]

The study reports that OpenFE's out-of-the-box protocol is promising for industrial-scale RBFE use, but that performance drops on private active-project datasets compared with curated public benchmarks. It also identifies practical error modes: buried-water sampling, ligand alignment, atom mapping, charge-changing transformations, partial fused-ring transformations, assay-limit data, stereochemical/tautomer ambiguity, and private-data setup quality. [SRC-0061, sections 3-4]

This source is linked to [[wiki/sources/SRC-0062-openfe-rbfe-benchmark-supporting-information]], the supporting information. It also supersedes but does not replace [[wiki/sources/SRC-0045-large-scale-collaborative-assessment-of-binding-free-energy]], an earlier preprint copy already present in the wiki. [SRC-0045] [SRC-0061] [SRC-0062]

## Key Points

- Public benchmark selection used 58 systems and 876 ligands from the Schrodinger 2023 benchmark release, excluding membrane-bound systems and major topological transformations not supported by the OpenFE tooling at the time. [SRC-0061, section 2.1]
- The private benchmark used 37 blinded industry datasets with 842 ligands, intended to reflect real drug-discovery projects more directly than public curated benchmarks. [SRC-0061, section 2.1]
- The OpenFE protocol used `openfe-v1.0.1`, OpenMM, Amber14SB protein, TIP3P water, OpenFF Sage-2.2.0 ligands/cofactors, AM1-BCC charges, Hamiltonian replica exchange, MBAR via `pymbar`, and triplicate simulations. [SRC-0061, sections 2.4-2.5]
- Neutral transformations used 11 lambda windows and 5 ns per window; charge-changing transformations used 22 windows and 20 ns per window with the co-alchemical water method. [SRC-0061, section 2.5]
- Public all-to-all pairwise performance was a weighted RMSE of about 1.72 kcal/mol over 58 systems, with 10 systems reaching sub-kcal/mol accuracy. [SRC-0061, section 3.1.1]
- Private all-to-all pairwise performance was worse, with weighted RMSE about 2.44 kcal/mol and only 2 systems reaching sub-kcal/mol accuracy. [SRC-0061, section 3.2]
- Edgewise metrics are more optimistic than all-to-all pairwise metrics because network planning preferentially simulates more similar ligand transformations. [SRC-0061, section 3.1.1]
- The FEP+ comparison is informative but not controlled: the compared FEP+ results used manual tuning, REST2, GCMC water sampling, OPLS4, custom torsions, and different lambda/repeat settings. [SRC-0061, section 4.1] [SRC-0062, table S3]
- Protocol diagnostics suggest that triplicate repeats improve reproducibility more than median accuracy in most well-behaved systems, and that 80% of the default sampling time often gives similar edgewise accuracy. [SRC-0061, sections 3.3.1-3.3.2]

## Mathematical structure

The article is benchmark- and protocol-focused, with central equations for relative free-energy cycles, relative absolute error, assay-limit correction, and weighted RMSE aggregation. [SRC-0061]

Relative binding free energy cycle, as stated around Figure 1 and Methods: [SRC-0061, figure 1 and section 2.4]

$$
\Delta\Delta G_{\mathrm{bind}, A\to B}
= \Delta G_{\mathrm{solvent}} - \Delta G_{\mathrm{complex}}.
$$

Relative absolute error metric: [SRC-0061, eq. 1]

$$
\mathrm{RAE} =
\frac{\sum_i^N |X_i - Y_i|}
{\sum_i^N |Y_i - \bar{Y}|}.
$$

Weighted RMSE aggregation over systems: [SRC-0061, eq. 3]

$$
\mathrm{RMSE} =
\sqrt{
\frac{1}{\sum_i^M w_i}
\sum_i^M w_i \mathrm{RMSE}_i^2
}.
$$

## Variable glossary

- $\Delta G_{\mathrm{complex}}$: alchemical free-energy change for the ligand transformation in the receptor complex leg. [SRC-0061, section 2.4]
- $\Delta G_{\mathrm{solvent}}$: alchemical free-energy change for the ligand transformation in solvent. [SRC-0061, section 2.4]
- $\Delta\Delta G$: relative binding free energy between two ligands. [SRC-0061]
- $X_i$: predicted value in the RAE definition. [SRC-0061, eq. 1]
- $Y_i$: reference value in the RAE definition. [SRC-0061, eq. 1]
- $\bar{Y}$: mean reference value used as the simple baseline for RAE. [SRC-0061, eq. 1]
- $\mathrm{RMSE}_i$: RMSE for benchmark system $i$. [SRC-0061, eq. 3]
- $w_i$: system weight, set to the number of ligands for all-to-all pairwise RMSE aggregation. [SRC-0061, section 3.1.1]
- $M$: number of systems in the weighted aggregate. [SRC-0061, eq. 3]

## Equation inventory

| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |
| RBFE thermodynamic cycle | Figure 1 and section 2.4 | This page; [[wiki/concepts/relative-binding-free-energy-benchmarking]] | Computes relative binding free energy from complex and solvent legs. | $\Delta G_{\mathrm{complex}}$, $\Delta G_{\mathrm{solvent}}$ | Defines the protocol output. |
| Relative absolute error | SRC-0061, eq. 1 | This page | Compares predictions to an average-reference baseline. | $X_i$, $Y_i$, $\bar{Y}$ | Used in deviation statistics. |
| Assay-limit correction | SRC-0061, eq. 2 | Not transcribed; summarized in Methods/Limitations | Adjusts private-set error calculation for assay detection limits. | estimated and observed assay values | Relevant to private-set benchmark interpretation. |
| Weighted RMSE | SRC-0061, eq. 3 | This page; [[wiki/concepts/relative-binding-free-energy-benchmarking]] | Aggregates system-level RMSE values. | $\mathrm{RMSE}_i$, $w_i$, $M$ | Used for public/private headline accuracy. |

## Proof map

The paper does not contain theorem proofs. Its argument is empirical: define a default OpenFE RBFE workflow, benchmark it across public and private datasets, compare with published FEP+ and MM-GBSA results where possible, analyze failure modes and convergence diagnostics, then identify protocol-improvement targets. [SRC-0061]

## Implementation notes

- The default workflow uses triplicate transformations; uncertainty for triplicate runs comes from the standard deviation of independent estimates, while single-run MBAR analytical uncertainty can be overoptimistic. [SRC-0061, section 3.3.1]
- Neutral simulations are likely longer than necessary for many well-behaved edges; reducing 5 ns to 4 ns per lambda window is proposed as a possible default-speed improvement. [SRC-0061, sections 3.3.2 and 4.3]
- Poor ligand alignment can produce poor 3D atom mappings with larger alchemical regions; the modular OpenFE framework makes mapper substitution or alignment improvements practical. [SRC-0061, sections 3.1.3 and 4.3]
- The benchmark identified a Kartograf atom-mapper bug involving bond-breaking mappings; the supporting information describes the fix and validates the corrected mappings. [SRC-0061, section 3.1.3] [SRC-0062, section S3]
- Future OpenFE improvements include adaptive lambda schedules, adaptive simulation length, better atom mapping/network scoring, better bonded dummy-core treatment, membrane support, ring-opening/closing support, enhanced sampling, and buried-water methods. [SRC-0061, section 4.3]

## Evidence

- Public weighted all-to-all pairwise RMSE: about 1.72 kcal/mol, with 47.4% of pairwise estimates within 1 kcal/mol and 78.3% within 2 kcal/mol. [SRC-0061, section 3.1.1]
- Published manually tuned FEP+ public comparison: weighted RMSE about 1.20 kcal/mol and 19 systems reaching sub-kcal/mol accuracy, but under different workflow and tuning conditions. [SRC-0061, section 3.1.1] [SRC-0062, table S3]
- Public edgewise performance: RMSE about 1.37 kcal/mol and MUE about 1.05 kcal/mol over 1181 edges. [SRC-0061, section 3.1.1]
- Private all-to-all pairwise performance: weighted RMSE about 2.44 kcal/mol, with 43.1% of pairwise estimates within 1 kcal/mol and 71.9% within 2 kcal/mol. [SRC-0061, section 3.2]
- Private edgewise performance: RMSE about 1.93 kcal/mol and MUE about 1.37 kcal/mol after filtering problematic ligand cases and assay-limit edges. [SRC-0061, section 3.2]
- Reproducibility: 83.5% of public edges and 71.7% of private edges had an inter-repeat range under 1 kcal/mol; MBAR-overlap filtering improved these fractions. [SRC-0061, section 3.3.1]
- Production framing: the paper reports low public edge failure, triplicate reproducibility, and mean public-set throughput of about 5.8 h for neutral edges and 31.0 h for charge-changing edges on an NVIDIA L40S GPU. [SRC-0061, section 4]

## Limitations and Caveats

- The headline public/private contrast should not be interpreted as a pure protocol effect; the private data have more setup ambiguity, assay-limit complications, stereochemical/tautomer uncertainty, and active-project heterogeneity. [SRC-0061, sections 3.2 and 4.2]
- The FEP+ comparison is not a controlled method comparison because the workflows differ in tuning, sampling length, force field, ligand preparation, enhanced sampling, and water treatment. [SRC-0061, section 4.1] [SRC-0062, table S3]
- Membrane proteins and major ring-breaking or macrocyclization transformations were outside the supported domain of the benchmark. [SRC-0061, sections 2.1 and 4.3]
- Charge-changing transformations, buried-water cases, partial fused-ring transformations, poor alignments, moving formal charges, and large private transformations remain important error modes. [SRC-0061, sections 3.1.2-3.2]
- Public data and scripts are available, but private input structures are not distributed. [SRC-0061, section 5]

## Claims

- [[wiki/claims/CLM-0017-experimental-reproducibility-bounds-rbfe-error-interpretation]]
- [[wiki/claims/CLM-0018-public-rbfe-benchmarks-can-be-easier-than-private-active-project-data]]
- [[wiki/claims/CLM-0019-edgewise-rbfe-metrics-can-overstate-arbitrary-comparison-quality]]

## Questions

- [[wiki/questions/rbfe-benchmark-prospective-use-scope]]

## Tensions

- [[wiki/tensions/TEN-0010-rbfe-benchmark-success-vs-prospective-use]]

## Links

- Supporting information: [[wiki/sources/SRC-0062-openfe-rbfe-benchmark-supporting-information]]
- Earlier preprint copy: [[wiki/sources/SRC-0045-large-scale-collaborative-assessment-of-binding-free-energy]]
- [[wiki/concepts/relative-binding-free-energy-benchmarking]]
- [[wiki/concepts/free-energy-estimation]]
- [[wiki/sources/SRC-0046-the-maximal-and-current-accuracy-of-rigorous-protein]]

## Open Questions

- Which proposed OpenFE improvements will most improve accuracy versus cost: adaptive lambda schedules, shorter/adaptive simulations, atom mapping, force-field changes, enhanced water sampling, or REST2-like sampling? [SRC-0061, section 4.3]
- How predictive are curated public RBFE benchmarks for prospective active-project performance once input preparation is automated? [SRC-0061, sections 3.2 and 4.2]
- What benchmark sets best isolate specific transformation classes such as charge changes, buried waters, partial fused rings, macrocycles, and metal-containing binding sites? [SRC-0061, section 4.2]

## Citation Links

- `SRC-0046`: The references list Ross, Lu, Scarabelli, Albanese, Houang, Abel, Harder, and Wang, "The maximal and current accuracy of rigorous protein-ligand binding free energy calculations," Communications Chemistry 2023, 6, 222. This is an exact title, first-author, and year match to the ingested FEP+ accuracy source. [SRC-0061, reference 42]
- `SRC-0023`: The references list Shirts and Chodera, "Statistically optimal analysis of samples from multiple equilibrium states," Journal of Chemical Physics 2008, 129, 124105. This is an exact title, first-author, and year match to the ingested original MBAR source. [SRC-0061, reference 89]
- Partial citation review: the targeted pass confirmed the cluster-relevant FEP+ and MBAR links. Full bibliography normalization is left partial because this benchmark cites many software, method, and benchmark sources not currently ingested. [SRC-0061]

## Mathematical gaps

- The piecewise assay-limit correction equation is summarized but not fully transcribed because the source-page retrieval need is the correction's interpretation rather than its exact case notation. [SRC-0061, eq. 2]
- MBAR equations are not reproduced here; the paper uses MBAR operationally through `pymbar` rather than deriving it. [SRC-0061, section 2.4]
- Per-system table values and all supporting figures remain in the raw source and supporting-information page rather than being duplicated.

## Ingestion QA

### Retrieval questions checked

- What is the main contribution of the OpenFE journal article?
- How are the public and private benchmarks defined?
- What protocol settings define the OpenFE RBFE workflow?
- What headline public and private RMSE values were reported?
- Why are all-to-all pairwise metrics less optimistic than edgewise metrics?
- Why is the FEP+ comparison not controlled?
- What practical failure modes were identified?
- What protocol improvements does the paper recommend?
- What information is in the supporting material?

### Coverage decision

Complete at `coverage_profile: math-standard`. The source page captures the main paper, supporting-information link, benchmark scope, protocol settings, core equations, headline metrics, production-readiness framing, limitations, and retrieval QA. [SRC-0061] [SRC-0062]

### Known gaps

- Per-target metric tables and all figure-level details remain in the PDF and associated repositories.
- The private benchmark structures and identifiers are intentionally unavailable; the wiki captures only the paper's aggregate and anonymized descriptions.
