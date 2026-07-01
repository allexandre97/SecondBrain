---
type: source
status: active
created: 2026-06-30
updated: 2026-06-30
source_id: SRC-0047
display_title: "Performing Solvation Free Energy Calculations in LAMMPS Using the Decoupling Approach"
short_title: "LAMMPS Solvation Free Energy"
authors:
  - Vikram Khanna
  - Jacob I. Monroe
  - Michael F. Doherty
  - Baron Peters
year: 2020
venue: "Journal of Computer-Aided Molecular Design"
doi: "10.1007/s10822-020-00303-3"
aliases:
  - "SRC-0047"
  - "LAMMPS Solvation Free Energy"
  - "Performing Solvation Free Energy Calculations in LAMMPS Using the Decoupling Approach"
source_path: raw/sources/SRC-0047-performing-solvation-free-energy-calculations-in-lammps-using.pdf
original_filename: "s10822-020-00303-3.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 09ec0c00f1e71123b58eefdeb3a0ebb71a9dfe37ba9ed8fddaf8aacc92f74bb3
areas:
  - research
categories:
  - research/molecular-simulation/free-energy
tags:
  - solvation-free-energy
  - LAMMPS
  - thermodynamic-integration
  - decoupling
related:
  - "[[wiki/concepts/free-energy-estimation]]"
  - "[[wiki/concepts/solvation-free-energy-decoupling-in-lammps]]"
sources:
  - SRC-0047
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: math-standard
metadata_review_status: reviewed
citation_match_status: partial
cqt_review_status: linked
---

# Performing Solvation Free Energy Calculations in LAMMPS Using the Decoupling Approach

Source ID: `SRC-0047`

## Raw source

- Repository path: `raw/sources/SRC-0047-performing-solvation-free-energy-calculations-in-lammps-using.pdf`
- Open raw source: [raw/sources/SRC-0047-performing-solvation-free-energy-calculations-in-lammps-using.pdf](../../raw/sources/SRC-0047-performing-solvation-free-energy-calculations-in-lammps-using.pdf)

## Summary

This paper introduces a way to perform solvation free energy calculations in LAMMPS using the decoupling route without modifying LAMMPS source code. The key implementation step is an overlay correction that compensates for intramolecular Coulomb scaling when solute charges are scaled to stage solute-solvent electrostatics. [SRC-0047]

## Key Points

- In decoupling, solute-solvent interactions are turned off or on while the solute's intramolecular interactions remain preserved. [SRC-0047]
- The challenge in LAMMPS is that scaling solute charges to control long-range solute-solvent electrostatics also scales intramolecular solute electrostatics. [SRC-0047]
- The paper's main contribution is an overlay potential that restores the solute's intramolecular Coulomb energy while using scaled charges for the staged electrostatic calculation. [SRC-0047, eqs. 5-8]
- The method was tested on ethanol and biphenyl hydration free energies and compared against GROMACS decoupling calculations. [SRC-0047]
- Reported total dimensionless solvation free energies agree across LAMMPS, GROMACS, and FreeSolv within the stated uncertainty for the two examples. [SRC-0047, table 2]
- The authors state that the overlay correction should also work with other free-energy estimators such as BAR, although the paper implements thermodynamic integration. [SRC-0047, conclusions]

## Key equations

**Thermodynamic integration, source Eqs. (1)-(2) [SRC-0047]:**

$$
\Delta G_{(i)\to(j)}
=
\int_{\lambda=0}^{\lambda=1}
\left\langle \frac{dU}{d\lambda} \right\rangle_\lambda d\lambda.
$$

For LJ or Coulomb staging:

$$
\Delta G_{\mathrm{solv}}^i
=
\int_{\lambda_i=0}^{\lambda_i=1}
\left\langle \frac{dU}{d\lambda_i} \right\rangle_{\lambda_i} d\lambda_i,
\qquad i \in \{\mathrm{LJ},\mathrm{coul}\}.
$$

**Overlay correction, source Eq. (7) [SRC-0047]:**

$$
\begin{aligned}
U_{\mathrm{coul}}^{\mathrm{overlay}}(r_{ij};\lambda_q)
&=
U_{\mathrm{coul}}^{\mathrm{intra}}(r_{ij})
-
U_{\mathrm{coul}}^{\mathrm{intra,scaled}}(r_{ij};\lambda_q) \\
&=
\sum_{i<j} (1-\lambda_q^2) k \frac{q_i q_j}{r_{ij}} \\
&=
\frac{1-\lambda_q^2}{\lambda_q^2}
U_{\mathrm{coul}}^{\mathrm{intra,scaled}}(r_{ij};\lambda_q).
\end{aligned}
$$

with $\lambda_{\mathrm{coul}}=(1-\lambda_q^2)/\lambda_q^2$ for the soft Coulomb overlay term. [SRC-0047, eqs. 7-8]

## Variable glossary

- $A$: solute whose interactions with solution are staged. [SRC-0047]
- $B$: solution phase around the solute. [SRC-0047]
- $\lambda_{\mathrm{LJ}}$: coupling parameter for solute-solution Lennard-Jones interactions. [SRC-0047]
- $\lambda_q$: charge-scaling parameter applied to solute charges. [SRC-0047]
- $\lambda_{\mathrm{coul}}$: user-supplied LAMMPS overlay scaling parameter. [SRC-0047, eq. 8]
- $q_i$: atomic charge on solute atom $i$. [SRC-0047]
- $r_{ij}$: pair distance. [SRC-0047]
- $k$: Coulomb prefactor $1/(4\pi\epsilon)$. [SRC-0047, eq. 5]

## Equation inventory

| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |
| Thermodynamic integration | Eqs. (1)-(2) | Key equations | Computes staged free-energy changes | $U$, $\lambda_i$ | Core numerical estimator |
| LAMMPS soft-core LJ | Eq. (3) | Mathematical gaps | Stages LJ interactions | $\lambda_{ij}$, $\epsilon$, $\sigma_{ij}$ | Omitted because OCR made formula unreliable |
| Pairwise lambda assignment | Eq. (4) | Mathematical gaps | Sets solute-solvent versus solute-solute LJ scaling | $\lambda_{ij}$, $\lambda_{\mathrm{LJ}}$ | Omitted as a simple case rule |
| Intramolecular Coulomb energies | Eqs. (5)-(6) | Key equations | Shows charge scaling distorts intramolecular energy | $\lambda_q$, $q_i$, $q_j$ | Identifies implementation problem |
| Overlay correction | Eq. (7) | Key equations | Restores original intramolecular Coulomb energy | $\lambda_q$, $U^{\mathrm{intra}}$ | Main LAMMPS implementation contribution |
| Soft Coulomb overlay | Eq. (8) | Key equations | Implements correction through `coul/cut/soft` overlay | $\lambda_{\mathrm{coul}}$, $\lambda_q$ | Directly actionable in LAMMPS |

## Limitations

- The validation examples are only ethanol and biphenyl, so the paper tests the implementation mechanism rather than broad chemical generality. [SRC-0047]
- The paper uses thermodynamic integration for simplicity; other estimators are argued to be compatible but not demonstrated. [SRC-0047, conclusions]
- The source does not claim that LAMMPS and GROMACS settings are identical in every implementation detail; it reports close agreement under matched practical protocols. [SRC-0047]

## Mathematical gaps

- The wiki omits the full LAMMPS soft-core Lennard-Jones formula because the PDF extraction garbled the nested powers; consult source Eq. (3) for exact implementation.
- The wiki does not reproduce the full quadrature schedule or every simulation parameter, but records the central overlay equations.

## Links

- [[wiki/concepts/free-energy-estimation]]
- [[wiki/concepts/solvation-free-energy-decoupling-in-lammps]]

## Claims

- [[wiki/claims/CLM-0023-decoupling-implementations-must-preserve-intramolecular-solute-terms]]

## Questions

- [[wiki/questions/md-free-energy-decoupling-implementation-validation]]

## Citation links

- Citation review status: partial. Bibliographic metadata was checked from the PDF first page and metadata; local MD-implementation cluster citation links were not promoted without direct bibliography evidence.

## Ingestion QA

### Retrieval questions checked

- What problem prevents straightforward decoupling calculations in LAMMPS?
- How does the overlay correction preserve solute intramolecular Coulomb interactions?
- Which equations define the thermodynamic integration estimator and overlay correction?
- Which test molecules were used?
- How did LAMMPS compare with GROMACS and FreeSolv?
- What validation boundaries remain?

### Coverage decision

Complete at `coverage_profile: math-standard`. The page captures the central implementation problem, equations, validation examples, limitations, and mathematical gaps.

### Known gaps

- Exact LAMMPS input snippets and the full soft-core LJ expression remain in the raw source.
