---
type: concept
status: active
created: 2026-06-29
updated: 2026-09-07
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
tags:
  - nonbonded-potentials
  - molecular-dynamics
related:
  - "[[wiki/concepts/garnet-force-field]]"
sources:
  - SRC-0003
  - SRC-0090
sensitivity: public
encryption: none
---

# Double Exponential Potential

## Summary

The double exponential potential is the non-bonded potential used by Garnet as an alternative to Lennard-Jones interactions. [SRC-0003] Its published-version functional form is [SRC-0090, Methods]

$$
V(r;\sigma,\epsilon,a,b)
=
\epsilon\left(
\frac{b\,e^{a}}{a-b}\exp\left[-a\frac{r}{r_m}\right]
-\frac{a\,e^{b}}{a-b}\exp\left[-b\frac{r}{r_m}\right]
\right),
\qquad r_m=2^{1/6}\sigma,
$$

where $\sigma$ and $\epsilon$ are per-atom parameters and $a$, $b$ are trained global parameters (fitted to $a=12.2$, $b=4.33$). [SRC-0090, Methods]

## Key Points

- In SRC-0003, Lennard-Jones training became unstable when simulations were introduced during training, for example when fitting condensed-phase properties. [SRC-0003]
- The double exponential potential trained effectively and is described as flexible for intermolecular interactions because it uses exponential repulsion and a flexible attractive term. [SRC-0003]
- The potential adds global parameters beyond atom-level sigma and epsilon values; the fitted Garnet values are $\alpha = 12.2$ and $\beta = 4.33$. [SRC-0003, section "The Garnet force field"]
- It remains practical in OpenMM through custom forces, with the revised manuscript reporting a 15--20% slowdown relative to Lennard-Jones. [SRC-0003, section "The Garnet force field"]
- Good trainability does not imply fully accurate condensed-phase behavior: Garnet tends to overestimate density and enthalpy of vapourisation on the revised 12-molecule test, suggesting overly strong attractive intermolecular interactions. [SRC-0003, section "Small molecule benchmark"]
- The authors do not claim Lennard-Jones is generally unstable; the claim is specific to their automated training pipeline. [SRC-0003]
- Future functional-form work could explore other bonded and non-bonded terms, soft-core potentials, polarization, and charge flux. [SRC-0003]

## Links

- [[wiki/sources/SRC-0003-training-a-force-field-from-scratch]]
- [[wiki/sources/SRC-0090-training-force-field-proteins-small-molecules]]
- [[wiki/concepts/garnet-force-field]]
- [[wiki/concepts/automated-force-field-training]]
