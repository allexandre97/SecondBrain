---
type: source
status: active
created: 2026-06-30
updated: 2026-06-30
source_id: SRC-0054
display_title: "Accelerating Molecular Dynamics Simulations Using Fast Ewald Summation with Prolates"
short_title: "Fast Ewald Summation with Prolates"
aliases:
  - "SRC-0054"
  - "Fast Ewald Summation with Prolates"
  - "Accelerating Molecular Dynamics Simulations Using Fast Ewald Summation with Prolates"
source_path: raw/sources/SRC-0054-accelerating-molecular-dynamics-simulations-using-fast-ewald-summation.pdf
original_filename: "s41467-026-73232-8_reference.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: fe6f5299ca0c0fca07c7b3fafe6a5bd0ee084be344f6cde89a9b45c0c6b135f9
areas:
  - research
categories:
  - research/molecular-simulation/molecular-dynamics
  - research/high-performance-computing
tags:
  - Ewald-summation
  - PME
  - PSWF
  - LAMMPS
  - GROMACS
related:
  - "[[concepts/particle-mesh-ewald-and-long-range-electrostatics]]"
sources:
  - SRC-0054
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: math-standard
---

# Accelerating Molecular Dynamics Simulations Using Fast Ewald Summation with Prolates

Source ID: `SRC-0054`

## Raw source

- Repository path: `raw/sources/SRC-0054-accelerating-molecular-dynamics-simulations-using-fast-ewald-summation.pdf`
- Local relative link: [Open raw source](../../raw/sources/SRC-0054-accelerating-molecular-dynamics-simulations-using-fast-ewald-summation.pdf)

## Summary

This 2026 Nature Communications article-in-press introduces ESP, Ewald summation with prolate spheroidal wave functions, for accelerating long-range Coulomb calculations in MD. ESP replaces the conventional Gaussian splitting/gridding kernel with PSWF-based kernels to reduce Fourier grid size, communication, and particle-grid work. [SRC-0054]

## Key Points

- Long-range Coulomb interactions remain a major cost in MD even with PME/PPPM because FFT-based methods require global communication. [SRC-0054]
- ESP uses radial kernels derived from prolate spheroidal wave functions for Ewald splitting and Cartesian-product PSWFs for spreading/interpolation. [SRC-0054]
- The method is integrated into LAMMPS and GROMACS for comparison with PPPM/PME baselines. [SRC-0054]
- At error tolerances $10^{-3}$ to $10^{-4}$, the abstract reports roughly 3-fold acceleration of electrostatics and 2.5-fold MD speedup at about $10^3$ cores. [SRC-0054, abstract]
- At tolerance $10^{-5}$, the abstract reports about 10-fold far-field electrostatics speedup and 5-fold MD simulation speedup. [SRC-0054, abstract]
- The discussion notes that realistic low-accuracy MD speedups with shorter Coulomb cutoffs require extending ESP to Lennard-Jones dispersion, because current packages still cut off van der Waals interactions at the same radius. [SRC-0054, discussion]

## Key equations

The source remains within the Ewald split family:

$$
E = E_{\mathrm{real}} + E_{\mathrm{Fourier}} + E_{\mathrm{self/correction}}.
$$

Its main mathematical change is the replacement of Gaussian localization by PSWF-derived kernels that improve frequency localization. [SRC-0054]

## Variable glossary

- ESP: Ewald summation with prolates. [SRC-0054]
- PSWF: prolate spheroidal wave function. [SRC-0054]
- PME/PPPM: FFT-based Ewald variants used as baselines. [SRC-0054]
- $r_c$: Coulomb cutoff radius. [SRC-0054]

## Equation inventory

| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |
| Ewald split | Introduction/methods | Key equations | Separates real and Fourier terms | $E_{\mathrm{real}}$, $E_{\mathrm{Fourier}}$ | Shared structure with PME/PPPM |
| PSWF kernel construction | Methods | Mathematical gaps | Replaces Gaussian/B-spline kernels | PSWF coefficients, grid spacing | Core ESP implementation |
| Error tolerance benchmarks | Results | Key Points | Relates speedup to accuracy | tolerances $10^{-3}$-$10^{-5}$ | Performance/accuracy tradeoff |

## Limitations

- The manuscript is marked article-in-press and unedited, so final publication details may change. [SRC-0054]
- Reported CPU-cluster benchmarks establish baselines; GPU-specific optimization is described as preliminary or ongoing. [SRC-0054, discussion]
- Low-accuracy full-MD acceleration is limited until Lennard-Jones/dispersion handling is also adapted for shorter cutoffs. [SRC-0054, discussion]

## Mathematical gaps

- PSWF kernel derivations, coefficient construction, detailed error analysis, and implementation parameters remain in the raw source.

## Links

- [[concepts/particle-mesh-ewald-and-long-range-electrostatics]]

## Ingestion QA

### Retrieval questions checked

- What is ESP?
- What part of PME/PPPM does it replace?
- What speedups are reported at different tolerances?
- Which MD packages include prototype integrations?
- Why does low-accuracy full-MD speedup need Lennard-Jones extension?
- What details may change because this is article-in-press?

### Coverage decision

Complete at `coverage_profile: math-standard`. The page captures method idea, reported performance, limitations, and derivation gaps.
