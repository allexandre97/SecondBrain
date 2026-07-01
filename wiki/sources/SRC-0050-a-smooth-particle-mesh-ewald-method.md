---
type: source
status: active
created: 2026-06-30
updated: 2026-06-30
source_id: SRC-0050
display_title: "A Smooth Particle Mesh Ewald Method"
short_title: "Smooth Particle Mesh Ewald"
authors:
  - Ulrich Essmann
  - Lalith Perera
  - Max L. Berkowitz
  - Tom Darden
  - Hsing Lee
  - Lee G. Pedersen
year: 1995
venue: "Journal of Chemical Physics"
doi: "10.1063/1.470117"
aliases:
  - "SRC-0050"
  - "Smooth Particle Mesh Ewald"
  - "A Smooth Particle Mesh Ewald Method"
source_path: raw/sources/SRC-0050-a-smooth-particle-mesh-ewald-method.pdf
original_filename: "8577_1_online.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 95f9181cd3fd4ea0891729ba18b0d7bc868925b66189f3d08ab75752debac520
areas:
  - research
categories:
  - research/molecular-simulation/molecular-dynamics
tags:
  - PME
  - Ewald-summation
  - electrostatics
  - B-splines
related:
  - "[[wiki/concepts/particle-mesh-ewald-and-long-range-electrostatics]]"
sources:
  - SRC-0050
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: math-standard
metadata_review_status: reviewed
citation_match_status: partial
cqt_review_status: linked
---

# A Smooth Particle Mesh Ewald Method

Source ID: `SRC-0050`

## Raw source

- Repository path: `raw/sources/SRC-0050-a-smooth-particle-mesh-ewald-method.pdf`
- Open raw source: [raw/sources/SRC-0050-a-smooth-particle-mesh-ewald-method.pdf](../../raw/sources/SRC-0050-a-smooth-particle-mesh-ewald-method.pdf)

## Summary

Essmann et al. reformulate particle mesh Ewald using B-spline interpolation of structure factors. Smooth PME gives analytic gradients, efficient virial tensor calculation, and controllable accuracy with $N \log N$ scaling, making Ewald electrostatics practical for large biomolecular simulations. [SRC-0050]

## Key Points

- The method replaces Lagrange interpolation in earlier PME formulations with cardinal B-spline interpolation. [SRC-0050]
- B-splines make potential and forces smooth functions of particle positions at any chosen accuracy level. [SRC-0050]
- The method naturally handles general unit cells through fractional coordinates. [SRC-0050]
- The same structure-factor view extends to lattice sums for related pair potentials such as dispersion interactions. [SRC-0050]
- The paper reports that PME can reach arbitrary accuracy independent of system size at cost $N \log N$. [SRC-0050, abstract]

## Key equations

Electrostatic structure factor: [SRC-0050, eq. 2.2]

$$
S(m) =
\sum_{j=1}^{N}
q_j \exp\left(2\pi i\, m \cdot r_j\right).
$$

Ewald energy split: [SRC-0050, section II]

$$
E = E_{\mathrm{dir}} + E_{\mathrm{rec}} + E_{\mathrm{corr}}.
$$

Reciprocal-space energy has the form: [SRC-0050, eq. 2.4]

$$
E_{\mathrm{rec}}
=
\frac{1}{2\pi V}
\sum_{m\ne 0}
\frac{\exp(-\pi^2 m^2/\beta^2)}{m^2}
S(m)S(-m).
$$

## Variable glossary

- $S(m)$: electrostatic structure factor for reciprocal vector $m$. [SRC-0050, eq. 2.2]
- $q_j$: charge on atom $j$. [SRC-0050, eq. 2.2]
- $V$: unit-cell volume. [SRC-0050, eq. 2.4]
- $\beta$: Ewald splitting parameter. [SRC-0050]
- $E_{\mathrm{dir}}$, $E_{\mathrm{rec}}$, $E_{\mathrm{corr}}$: direct, reciprocal, and correction energy terms. [SRC-0050]

## Equation inventory

| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |
| Structure factor | Eq. (2.2) | Key equations | Encodes charge distribution in reciprocal space | $S(m)$, $q_j$, $r_j$ | Target approximated by B-spline gridding |
| Ewald split | Section II | Key equations | Splits electrostatics into direct, reciprocal, correction terms | $E_{\mathrm{dir}}$, $E_{\mathrm{rec}}$, $E_{\mathrm{corr}}$ | Architecture of PME computation |
| Reciprocal energy | Eq. (2.4) | Key equations | Long-range reciprocal contribution | $m$, $\beta$, $V$, $S(m)$ | FFT-accelerated term |
| B-spline approximation | Sections III-IV | Mathematical gaps | Smooth gridding/interpolation of structure factors | B-splines, grid indices | Full implementation formulas omitted |

## Limitations

- The source is a foundational method paper; modern MD codes use many later optimizations and variants. [SRC-0050]
- The wiki does not reproduce the complete B-spline recursion or all accuracy/timing tables. [SRC-0050]

## Mathematical gaps

- Full B-spline interpolation formulas, force derivations, virial tensor derivations, and dispersion PME details remain in the raw source.

## Links

- [[wiki/concepts/particle-mesh-ewald-and-long-range-electrostatics]]

## Claims

- [[wiki/claims/CLM-0027-ewald-pme-family-choices-trade-accuracy-smoothness-and-cost]]

## Questions

- [[wiki/questions/md-virial-pressure-implementation-for-autodiff-and-many-body-potentials]]

## Tensions

- [[wiki/tensions/TEN-0012-exact-electrostatics-and-neighbor-accounting-vs-practical-gpu-performance]]

## Citation links

- Citation review status: partial. Bibliographic metadata was checked from the PDF first page; this page is a cited local target of SRC-0054.

## Ingestion QA

### Retrieval questions checked

- What is smooth PME?
- Why are B-splines used?
- What is the role of the structure factor?
- What scaling does the method claim?
- How does it affect forces and virials?
- What formulas are omitted from the wiki?

### Coverage decision

Complete at `coverage_profile: math-standard`. The page records the central Ewald split, structure-factor formula, method contribution, and implementation gaps.
