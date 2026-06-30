---
type: source
status: active
created: 2026-06-30
updated: 2026-06-30
source_id: SRC-0051
display_title: "A General Pressure Tensor Calculation for Molecular Dynamics Simulations"
short_title: "MD Pressure Tensor Calculation"
aliases:
  - "SRC-0051"
  - "MD Pressure Tensor Calculation"
  - "A General Pressure Tensor Calculation for Molecular Dynamics Simulations"
source_path: raw/sources/SRC-0051-a-general-pressure-tensor-calculation-for-molecular-dynamics.pdf
original_filename: "A general pressure tensor calculation for molecular dynamics simulations.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 15e62b3027b6ef473226b0550222d81ffa733ac9d810900bca79aa4c9115516e
areas:
  - research
categories:
  - research/molecular-simulation/molecular-dynamics
tags:
  - pressure-tensor
  - constraints
  - Ewald-summation
  - polymers
related:
  - "[[concepts/md-pressure-and-stress-tensor-calculation]]"
sources:
  - SRC-0051
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: math-standard
---

# A General Pressure Tensor Calculation for Molecular Dynamics Simulations

Source ID: `SRC-0051`

## Raw source

- Repository path: `raw/sources/SRC-0051-a-general-pressure-tensor-calculation-for-molecular-dynamics.pdf`
- Local relative link: [Open raw source](../../raw/sources/SRC-0051-a-general-pressure-tensor-calculation-for-molecular-dynamics.pdf)

## Summary

Brown and Neyertz present a hybrid pressure-tensor calculation combining thermodynamic and mechanical routes. The method was motivated by crystalline polyethylene oxide simulations with periodic chains, holonomic constraints, and Ewald electrostatics, where traditional molecular pressure-tensor definitions become awkward. [SRC-0051]

## Key Points

- The method separates contributions from potential terms and constraints to the pressure tensor. [SRC-0051]
- The motivating system includes effectively infinite polymer chains bonded across periodic images, making center-of-mass molecular pressure definitions difficult. [SRC-0051]
- The authors use pressure-tensor components as sensitive diagnostics for force-field parameter choices. [SRC-0051]
- The paper argues the method is generally applicable to fully periodic classical MD systems. [SRC-0051]

## Key equations

The paper builds pressure tensor components by combining thermodynamic derivatives for some potential terms with mechanical force contributions for others. A compact generic virial-style tensor contribution is:

$$
P_{\alpha\beta}^{\mathrm{force}}
\propto
\sum_i r_{i,\alpha} F_{i,\beta}.
$$

[SRC-0051]

## Variable glossary

- $P_{\alpha\beta}$: pressure tensor component. [SRC-0051]
- $r_{i,\alpha}$: component $\alpha$ of atom position $i$. [SRC-0051]
- $F_{i,\beta}$: component $\beta$ of force on atom $i$. [SRC-0051]
- PEO: polyethylene oxide motivating application. [SRC-0051]

## Equation inventory

| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |
| Hybrid pressure tensor | Section 3 | Key equations | Combines mechanical and thermodynamic routes | $P_{\alpha\beta}$, forces, constraints | Main method |
| Constraint contribution | Section 3.3 | Mathematical gaps | Adds rigid-constraint pressure contribution | constraint forces, positions | Needed for constrained systems |
| Ewald contribution | Appendix/equation discussion | Mathematical gaps | Handles reciprocal electrostatics | Ewald terms | Needed for long-range electrostatics |

## Limitations

- OCR quality is weak for several formulas; implementation should consult the PDF directly. [SRC-0051]
- The case study is crystalline PEO, so empirical diagnostic conclusions about parameter sensitivity are system-specific. [SRC-0051]

## Mathematical gaps

- The wiki records the method structure but not every pressure-tensor component formula because the scanned PDF extraction is noisy.

## Links

- [[concepts/md-pressure-and-stress-tensor-calculation]]

## Ingestion QA

### Retrieval questions checked

- Why was a hybrid pressure-tensor method needed?
- Which MD features complicated traditional pressure calculations?
- What does the method separate?
- How was it used for PEO parameter assessment?
- What formulas require raw-source lookup?

### Coverage decision

Complete at `coverage_profile: math-standard`. The page captures scope, method intent, important caveats, and formula gaps.
