---
type: question
status: active
created: 2026-08-05
updated: 2026-08-05
question_status: open
areas:
  - research
categories:
  - research/molecular-simulation/molecular-dynamics
tags:
  - question
  - dielectric-constant
  - reaction-field
  - Ewald-summation
  - finite-size-effects
related:
  - "[[wiki/concepts/dipole-moment-fluctuation-dielectric-constant]]"
  - "[[wiki/concepts/particle-mesh-ewald-and-long-range-electrostatics]]"
sources:
  - SRC-0075
sensitivity: public
encryption: none
---

# Reaction-Field Versus Ewald Dielectric Limit

## Question

Why did the reaction-field and Ewald-geometry estimates of the dielectric constant differ for the highly polar Stockmayer system, and how do the two estimates converge with particle number and summation accuracy?

## Evidence and current position

For $N=256$, reaction-field calculations gave approximately $\varepsilon=65$–$66$, whereas the cited Ewald results were lower and showed a weaker, non-monotonic size dependence. Neumann identifies finite-size dependence and possible distortions from approximate Ewald-sum evaluation as unresolved explanations, while noting that reaction-field and Ewald-with-reaction-field should agree in the thermodynamic limit. [SRC-0075, pp. 852–856]

The paper is evidence for a validation requirement, not a resolution: compare multiple system sizes, exact and approximate long-range treatments, and the same fluctuation convention before interpreting a dielectric constant.

## Links

- [[wiki/sources/SRC-0075-dipole-moment-fluctuation-formulas-in-computer-simulations-of]]
- [[wiki/tensions/TEN-0017-reaction-field-consistency-versus-ewald-finite-size-behavior]]
- [[wiki/concepts/dipole-moment-fluctuation-dielectric-constant]]
