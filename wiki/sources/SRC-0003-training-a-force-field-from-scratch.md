---
type: source
status: active
created: 2026-06-29
updated: 2026-09-07
source_id: SRC-0003
display_title: "Training a Force Field for Proteins and Small Molecules from Scratch"
short_title: "Garnet Force Field"
aliases:
  - "SRC-0003"
  - "Garnet Force Field"
  - "Training a Force Field for Proteins and Small Molecules from Scratch"
source_path: raw/sources/SRC-0003-training-a-force-field-from-scratch.pdf
imported_path: raw/sources/SRC-0003-training-a-force-field-from-scratch.pdf
original_filename: "Garnet_paper.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: e76edc629afd9742b1ae074a1de16a72ff6b574ce296b37eb23f89a026ab2bee
authors:
  - "Alexandre Blanco-González"
  - "Thea K Schulze"
  - "Evianne Rovers"
  - "Joe G Greener"
author_entities: []
year: 2026
venue: "arXiv"
doi:
arxiv: "2603.16770"
metadata_review_status: reviewed
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/machine-learning/scientific-modeling
  - research/biomolecules/proteins
  - research/machine-learning/molecular-modeling
  - research/experimental-benchmarking
tags:
  - molecular-dynamics
  - force-fields
  - graph-neural-networks
related:
  - "[[wiki/concepts/garnet-force-field]]"
  - "[[wiki/concepts/automated-force-field-training]]"
  - "[[wiki/questions/garnet-validation-scope]]"
  - "[[wiki/claims/CLM-0002-garnet-automates-parameter-assignment]]"
  - "[[wiki/tensions/TEN-0002-garnet-broad-coverage-vs-validation-gaps]]"
  - "[[wiki/sources/SRC-0090-training-force-field-proteins-small-molecules]]"
  - "[[wiki/sources/SRC-0091-training-force-field-proteins-small-molecules-supplement]]"
sources:
  - SRC-0003
cites_sources:
  - SRC-0016
  - SRC-0021
  - SRC-0023
  - SRC-0025
  - SRC-0043
  - SRC-0044
  - SRC-0046
  - SRC-0061
  - SRC-0072
citation_match_status: reviewed
cqt_review_status: linked
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: standard
---

# Training a Force Field for Proteins and Small Molecules from Scratch

Source ID: `SRC-0003`

## Raw source

- Repository path: `raw/sources/SRC-0003-training-a-force-field-from-scratch.pdf`
- Open raw source: [raw/sources/SRC-0003-training-a-force-field-from-scratch.pdf](../../raw/sources/SRC-0003-training-a-force-field-from-scratch.pdf)

## Summary

This revised manuscript introduces Garnet, a graph-neural-network system that predicts molecular mechanics force-field parameters for proteins and small molecules without reusing legacy force-field parameters. It trains from quantum mechanical data, condensed-phase properties, and protein NMR data, and reports performance competitive with established force fields across small molecules, folded proteins, protein complexes, disordered proteins, water, and selected relative binding free energy benchmarks. The revision adds explicit dipole and small-molecule condensed-phase validation; these results strengthen the evidence base while also exposing over-polarized electrostatics and overly strong attractive intermolecular interactions. Garnet is presented as a platform for automated force-field discovery rather than as a universally validated force field. [SRC-0003]

## Key Points

- Garnet uses continuous atom typing from molecular topology to assign force-field parameters for bonds, angles, torsions, charges, and double-exponential non-bonded terms. [SRC-0003]
- Training used DFT force, potential-energy-difference, and charge data from SPICE, Espaloma, GEMS, and MACE-OFF, plus condensed-phase enthalpy data and GB3 protein NMR observables. [SRC-0003]
- The model trains all parameters from scratch, including water parameters, although GAFF/TIP3P and Amber14SB/TIP3P reference trajectories were used early in training to provide conformations. [SRC-0003]
- The authors report that Lennard-Jones was difficult to train once simulations entered the automated pipeline, while the double exponential potential trained effectively and ran about 15--20% slower than Lennard-Jones in their OpenMM comparison. [SRC-0003, section "The Garnet force field"]
- Benchmarks include held-out SPICE subsets, the OpenFF Industry Benchmark small-molecule set, dipole comparisons, density and enthalpy-of-vapourisation tests, folded-protein NMR comparisons, protein complex simulations, IDP observables, water properties, and RBFE calculations on selected OpenFE benchmark systems. [SRC-0003]
- In the added dipole benchmark, Garnet's over-polarization affects both dipole magnitude and orientation. [SRC-0003, section "Small molecule benchmark"]
- On 12 small-molecule condensed-phase test systems, Garnet correlates with experimental density and enthalpy of vapourisation but performs worse than OpenFF 2.2.1 by RMSE and tends to overestimate both properties, suggesting overly strong attractive intermolecular interactions. The three molecules represented in Garnet's condensed-phase training data are predicted better. [SRC-0003, section "Small molecule benchmark"]
- Garnet performed comparably to existing methods on several benchmarks, but the paper notes caveats such as possible overfitting on GB3, over-compaction of intrinsically disordered proteins, occasional aromatic-ring planarity issues, over-polarized charges, condensed-phase property overestimation, and RBFE coverage limited to 8 of 58 public benchmark systems. [SRC-0003]
- Future directions include broader validation for nucleic acids, lipids, metals, carbohydrates, IDPs, and other polymers; functional-form exploration; polarization and charge flux; and direct optimization against binding free energy data. [SRC-0003]
- The Garnet force field, scripts, validation tools, and data are reported as available under a permissive license. [SRC-0003]

## Links

- [[wiki/concepts/garnet-force-field]]
- [[wiki/concepts/automated-force-field-training]]
- [[wiki/concepts/double-exponential-potential]]
- [[wiki/concepts/relative-binding-free-energy-benchmarking]]
- [[wiki/questions/garnet-validation-scope]]
- [[wiki/claims/CLM-0002-garnet-automates-parameter-assignment]]
- [[wiki/tensions/TEN-0002-garnet-broad-coverage-vs-validation-gaps]]

## Claims

- [[wiki/claims/CLM-0002-garnet-automates-parameter-assignment]] - Garnet predicts force-field parameters from topology using continuous atom typing rather than fixed manually assigned atom types. [SRC-0003]

## Questions

- [[wiki/questions/garnet-validation-scope]] - Which molecule classes and simulation tasks still need validation before treating Garnet as broadly transferable? [SRC-0003]

## Tensions

- [[wiki/tensions/TEN-0002-garnet-broad-coverage-vs-validation-gaps]] - Garnet's broad automated-force-field framing coexists with validation gaps and reported failure modes. [SRC-0003]

## Citation links

- [[wiki/sources/SRC-0072-machine-learned-molecular-mechanics-force-fields-from-large]] - cited as the Espaloma-0.3 force-field study. [SRC-0003, ref. 16]
- [[wiki/sources/SRC-0061-openfe-rbfe-benchmark-journal-version]] - cited as the public OpenFE RBFE benchmark. [SRC-0003, ref. 15]
- [[wiki/sources/SRC-0044-spice-a-dataset-of-drug-like-molecules-and]] - cited as a central quantum-chemical training dataset. [SRC-0003, ref. 40]
- [[wiki/sources/SRC-0025-building-force-fields-automatic-systematic-reproducible-approach]] - cited for automated, reproducible force-field construction. [SRC-0003, ref. 26]
- [[wiki/sources/SRC-0016-fine-tuning-mm-force-fields-to-experimental-free-energies]] and [[wiki/sources/SRC-0021-tuning-potential-functions-host-guest-binding-data]] - cited for fitting force fields to experimental free-energy data. [SRC-0003, refs. 66--67]
- [[wiki/sources/SRC-0023-statistically-optimal-analysis-multiple-equilibrium-states-mbar]] - cited as a possible improvement to ensemble-reweighting accuracy. [SRC-0003, ref. 68]
- [[wiki/sources/SRC-0043-structure-based-experimental-datasets-for-benchmarking-protein-simulation]] - cited for protein force-field benchmark data. [SRC-0003, ref. 75]
- [[wiki/sources/SRC-0046-the-maximal-and-current-accuracy-of-rigorous-protein]] - cited as the FEP+ comparison used in the RBFE assessment. [SRC-0003, ref. 56]

## Published version

- The peer-reviewed journal version of this preprint is ingested as [[wiki/sources/SRC-0090-training-force-field-proteins-small-molecules]] (Chemical Science, DOI 10.1039/D6SC02874H, published 17 September 2026) with its supplementary information at [[wiki/sources/SRC-0091-training-force-field-proteins-small-molecules-supplement]]. The scientific content is largely shared; SRC-0090 adds the final DOI, venue, CC-BY licence, author-contribution statement, and the supplementary tables/figures.

## Revision history

- On 2026-09-07, the 44-page user-provided revision `Garnet_paper.pdf` replaced the repository copy while retaining stable source ID `SRC-0003`. Its SHA256 is `e76edc629afd9742b1ae074a1de16a72ff6b574ce296b37eb23f89a026ab2bee`.
- The removed copy was the 38-page arXiv v1 file `2603.16770v1.pdf`, SHA256 `d84bc9589f33dc1c4c7011240b8bdb5d394154e2fa254857dc6dec461ca74262`. It is not retained in `raw/sources/`.
- Material additions include dipole-vector validation, density and enthalpy-of-vapourisation benchmarks for small molecules, explicit double-exponential timing and fitted global-parameter values, updated references, and author-contribution information. [SRC-0003]

## Open Questions

- [[wiki/questions/garnet-validation-scope]] - Which molecule classes and simulation tasks still need validation before treating Garnet as broadly transferable? [SRC-0003]

## Ingestion QA

### Retrieval questions checked

- What is Garnet and what central contribution does the paper claim?
- What problem in molecular mechanics force-field development is Garnet trying to solve?
- What role does the graph neural network play in parameter assignment?
- What training data sources and training signals were used?
- Why did the authors use a double exponential non-bonded potential instead of Lennard-Jones?
- What benchmark families were used to evaluate Garnet?
- What do the revised dipole, density, and enthalpy-of-vapourisation benchmarks reveal?
- What limitations, caveats, and validation boundaries does the paper report?
- What future directions does the paper identify?
- What claims should not be overgeneralized from this paper?

### Coverage decision

Complete at `coverage_profile: standard`. The source page and linked concept/question pages can answer the main future retrieval questions about Garnet's contribution, problem framing, model role, training data, functional-form choice, revised dipole and condensed-phase evidence, benchmark scope, limitations, and future work. This is not `deep` coverage; detailed numerical benchmark tables, full architecture equations, and implementation-level simulation settings remain in the raw source.

### Known gaps

- The wiki does not reproduce detailed numerical benchmark tables or full methods equations.
- RBFE coverage is summarized at benchmark-family level, not as a complete per-target result table.
- The revised density and enthalpy-of-vapourisation results are represented qualitatively; exact per-molecule values and confidence intervals remain in the raw source.
- The paper's implementation details are summarized only where needed for retrieval; close technical reuse still requires consulting the raw source.
- Garnet should be treated as promising and broadly benchmarked, not as universally validated across all biomolecular species or simulation tasks. [SRC-0003]
