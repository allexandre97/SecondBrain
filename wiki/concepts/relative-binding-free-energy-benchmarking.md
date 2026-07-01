---
type: concept
status: active
created: 2026-06-29
updated: 2026-06-30
areas:
  - research
categories:
  - research/molecular-simulation/free-energy
  - research/computational-drug-discovery
  - research/experimental-benchmarking
  - research/biomolecules/proteins
tags:
  - rbfe
  - drug-discovery
related:
  - "[[wiki/concepts/garnet-force-field]]"
  - "[[wiki/concepts/free-energy-estimation]]"
  - "[[wiki/questions/rbfe-benchmark-prospective-use-scope]]"
  - "[[wiki/claims/CLM-0017-experimental-reproducibility-bounds-rbfe-error-interpretation]]"
  - "[[wiki/claims/CLM-0018-public-rbfe-benchmarks-can-be-easier-than-private-active-project-data]]"
  - "[[wiki/claims/CLM-0019-edgewise-rbfe-metrics-can-overstate-arbitrary-comparison-quality]]"
  - "[[wiki/tensions/TEN-0010-rbfe-benchmark-success-vs-prospective-use]]"
sources:
  - SRC-0003
  - SRC-0045
  - SRC-0046
  - SRC-0061
  - SRC-0062
sensitivity: public
encryption: none
---

# Relative Binding Free Energy Benchmarking

## Summary

Relative binding free energy benchmarking evaluates how well simulations rank or predict ligand binding differences against experimental binding data, with accuracy bounded in practice by experimental reproducibility and setup quality. [SRC-0003] [SRC-0046]

## Key Points

- SRC-0003 evaluates Garnet on selected systems from a public OpenFE benchmark set, including targets such as Tyk2, Cdk2, P38, Mcl1, chk1, galectin, BACE, T4 lysozyme, and c-Met. [SRC-0003]
- The authors modified OpenFE to support the double exponential potential and related soft-core potential. [SRC-0003]
- Garnet is reported as broadly comparable to OpenFE on the tested systems, with a chk1 outlier noted. [SRC-0003]
- Some transformations failed in the BACE and c-Met systems; the authors removed redundant failed edges from the analysis network. [SRC-0003]
- The benchmark is limited relative to the full 58-system public benchmark set, so it supports promising but not definitive RBFE generalization. [SRC-0003]
- SRC-0046 estimates experimental relative-affinity reproducibility at pairwise RMSE 0.91 [0.83, 1.11] kcal/mol and FEP+ benchmark accuracy at pairwise RMSE 1.25 [1.17, 1.33] kcal/mol. [SRC-0046, table 3]
- SRC-0061, the journal version of the OpenFE benchmark, reports that default OpenFE reached weighted all-to-all pairwise RMSE about 1.72 kcal/mol on 58 public systems and about 2.44 kcal/mol on 37 blinded private systems. [SRC-0061, sections 3.1.1 and 3.2]
- Edgewise errors can be optimistic because transformation networks preferentially connect similar ligands; all-to-all pairwise $\Delta\Delta G$ metrics better represent arbitrary ligand-to-ligand comparisons within a series. [SRC-0061, section 3.1.1] [SRC-0046, metrics]
- Manual preparation choices such as protonation, tautomer, binding pose, rotamer, water sampling, and atom mapping can materially affect reported FEP accuracy. [SRC-0046, discussion] [SRC-0061, section 4.1]
- Supporting information for the journal OpenFE benchmark records protocol differences from FEP+, private problematic-ligand categories, atom-mapping outlier analyses, repeat and sampling-length diagnostics, and convergence/edge-score analyses. [SRC-0062]

## Core equations

Relative binding free energy from an assay readout: [SRC-0046, eq. 2]

$$
\Delta\Delta G^{ab} = -kT \ln \frac{X^b}{X^a}.
$$

Weighted benchmark RMSE aggregation: [SRC-0061, eq. 3] [SRC-0046, eq. 3]

$$
\mathrm{RMSE} =
\sqrt{
\frac{1}{\sum_i^M w_i}
\sum_i^M w_i \mathrm{RMSE}_i^2
}.
$$

## Caveats

- Retrospective FEP benchmarks can overstate prospective performance because systems may have been selected from prior successful studies and because manual expert setup is difficult to reproduce under medicinal-chemistry timelines. [SRC-0046, discussion]
- Curated public benchmark accuracy may not transfer directly to private active-project datasets containing assay-limit, stereochemical, tautomeric, pose, water-sampling, metal, or large-transformation issues. [SRC-0061, sections 3.2 and 4.2]
- Experimental comparison data are not ground truth without uncertainty; poorly reproducible assays can make a physically reasonable prediction appear inaccurate. [SRC-0046, discussion]
- Comparisons between default OpenFE and published FEP+ results should not be treated as controlled force-field or software comparisons because workflow tuning, sampling, enhanced water methods, force fields, and ligand preparation differ. [SRC-0061, section 4.1] [SRC-0062, table S3]

## Links

- [[wiki/sources/SRC-0003-training-a-force-field-from-scratch]]
- [[wiki/sources/SRC-0045-large-scale-collaborative-assessment-of-binding-free-energy]]
- [[wiki/sources/SRC-0046-the-maximal-and-current-accuracy-of-rigorous-protein]]
- [[wiki/sources/SRC-0061-openfe-rbfe-benchmark-journal-version]]
- [[wiki/sources/SRC-0062-openfe-rbfe-benchmark-supporting-information]]
- [[wiki/concepts/garnet-force-field]]
- [[wiki/concepts/free-energy-estimation]]
- [[wiki/questions/garnet-validation-scope]]
- [[wiki/questions/rbfe-benchmark-prospective-use-scope]]
- [[wiki/claims/CLM-0017-experimental-reproducibility-bounds-rbfe-error-interpretation]]
- [[wiki/claims/CLM-0018-public-rbfe-benchmarks-can-be-easier-than-private-active-project-data]]
- [[wiki/claims/CLM-0019-edgewise-rbfe-metrics-can-overstate-arbitrary-comparison-quality]]
- [[wiki/tensions/TEN-0010-rbfe-benchmark-success-vs-prospective-use]]
