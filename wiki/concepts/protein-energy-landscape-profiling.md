---
type: concept
status: active
created: 2026-07-01
updated: 2026-07-01
areas:
  - research
categories:
  - research/biomolecules/proteins
  - research/experimental-benchmarking
  - research/data-management
  - research/machine-learning/scientific-modeling
tags:
  - proteins
  - energy-landscapes
  - hydrogen-deuterium-exchange
  - protein-stability
  - conformational-fluctuations
related:
  - "[[wiki/concepts/protein-force-field-benchmark-datasets]]"
sources:
  - SRC-0067
sensitivity: public
encryption: none
---

# Protein Energy Landscape Profiling

## Summary

Protein energy landscape profiling measures not only whether a protein domain is globally folded, but how costly it is for different parts of the domain to access partially open conformations. SRC-0067 shows that multiplex mHDX-MS can scale this idea to thousands of small domains and reveal conformational fluctuation differences that native-structure prediction and global stability measurements can miss. [SRC-0067]

## Key Points

- mHDX-MS infers opening-energy distributions from hydrogen-deuterium exchange rates measured across many proteins in pooled mass-spectrometry experiments. [SRC-0067]
- Global unfolding stability and local opening stability are related but partially uncoupled; domains with similar global stability can have different distributions of low-energy partially open states. [SRC-0067]
- Opening cooperativity summarizes whether a domain has many residues with high opening energies relative to other domains with similar global stability and simple structural covariates. [SRC-0067]
- Low opening cooperativity can correspond to entire unstable secondary-structure elements, which matters for interpreting dynamics, design, aggregation risk, immunogenicity, and simulation benchmarks. [SRC-0067]
- Large energy-landscape datasets can support feature analysis and machine-learning-guided design, but SRC-0067 found that cooperativity remained much harder to predict than global stability. [SRC-0067]

## Evidence

- SRC-0067 analyzed 5,778 protein domains and identified 3,590 measurably stable domains by mHDX-MS.
- SRC-0067 reports agreement between mHDX-MS and HDX NMR for 13 domains, and correlation between mHDX-MS and cDNA-display global-stability measurements across thousands of domains.
- SRC-0067 experimentally tested designed double-mutant libraries and found multiple designed variants that improved both opening cooperativity and global stability.

## Links

- [[wiki/sources/SRC-0067-protein-energy-landscape-discovery-analysis-design]]
- [[wiki/concepts/protein-force-field-benchmark-datasets]]

## Caveats

- Intact-protein mHDX-MS provides opening-energy distributions but does not by itself map each inferred rate to a residue position. [SRC-0067]
- The inferred energies depend on HDX model assumptions and require careful quality filtering. [SRC-0067]
- Current models trained on these data explain only a limited fraction of opening-cooperativity variance, so this remains a measurement-led rather than prediction-solved problem. [SRC-0067]

## Open Questions

- How should mHDX-MS-derived opening energies be turned into quantitative benchmarks for protein ensemble generators or molecular simulations?
- Which protein families, sizes, and experimental conditions can be profiled with comparable throughput and accuracy?
