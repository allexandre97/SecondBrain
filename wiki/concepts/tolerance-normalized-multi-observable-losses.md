---
type: concept
status: active
created: 2026-07-21
updated: 2026-07-28
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/scientific-computing
tags:
  - force-field-optimization
  - multi-objective-optimization
  - loss-functions
  - observable-targets
related:
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
  - "[[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]]"
  - "[[wiki/claims/CLM-0010-reweighting-fine-tuning-depends-on-support]]"
  - "[[wiki/answers/ffrefine-current-implementation-status]]"
sources:
  - SRC-0018
sensitivity: public
encryption: none
---

# Tolerance-Normalized Multi-Observable Losses

## Summary

When force-field training combines observables with different units, numerical scales, or target counts, raw squared errors do not define a meaningful balance: changing units can change the optimizer even when the physical problem is unchanged. Each scalar target should instead be expressed through a dimensionless residual

$$
r_i = \frac{y_i(\theta)-y_i^{\mathrm{ref}}}{\tau_i},
$$

where $\tau_i>0$ is an engineering tolerance for that target. SRC-0018 uses this tolerance-normalized target representation to combine thermodynamic and observable losses. [SRC-0018]

For collections such as density values and radial-distribution-function bins, a hierarchical weighted mean prevents the family with more scalar targets from dominating merely because it has more entries:

$$
L_f = \frac{\sum_{i\in f} w_i r_i^2}{\sum_{i\in f} w_i},
\qquad
L = \frac{\sum_f \alpha_f L_f}{\sum_f \alpha_f}.
$$

Here $w_i$ sets importance within a target family and $\alpha_f$ sets importance between families. The hierarchical family aggregation is an FFRefine implementation refinement of SRC-0018's tolerance-normalized target layer, not a separate claim from the source.

## Interpretation

- The tolerance $\tau_i$ defines what one unit of error means for target $i$ and makes the residual dimensionless.
- The within-family weight $w_i$ expresses scientific priority without changing units. For an RDF, it can emphasize structurally important peak bins.
- The family coefficient $\alpha_f$ balances quantities such as density and the complete RDF independently of the number of temperatures, pair types, or histogram bins.
- If only one family is enabled, normalization over present families gives that family the full objective. Missing families do not require dummy targets or special loss branches.

The gradient of the MSE-like objective contains the expected inverse-square tolerance scaling:

$$
\nabla_\theta L_f
=
\frac{2}{\sum_{i\in f}w_i}
\sum_{i\in f}
w_i\frac{y_i-y_i^{\mathrm{ref}}}{\tau_i^2}
\nabla_\theta y_i.
$$

Consequently, rescaling an observable, its reference, its tolerance, and its observable gradient by the same unit-conversion factor leaves both the loss and the parameter gradient unchanged.

## Implementation consequences

An optimizer-facing target should retain the prediction, reference, tolerance, family, within-family weight, and family coefficient. History should record raw errors and normalized residuals as well as base and effective weights, because only the normalized quantities are comparable across target types.

For water-temperature fitting, the current FFRefine implementation uses density, RDF, and dielectric target families. RDF peak weights are assigned by first shell, second shell, and tail regions within each pair type, then family coefficients control density-versus-RDF-versus-dielectric influence. Equal family coefficients therefore mean equal family influence, not equal influence per scalar bin; the current water script gives RDF a larger family coefficient than density or dielectric. Split validation is a separate policy: density and RDF split checks are enabled, while dielectric split checks are present in the source but commented out as of the 2026-07-28 audit.

Tolerance-normalized losses should not automatically be called chi-squared objectives. That probabilistic interpretation requires tolerances to be justified as observation standard deviations; engineering accuracy tolerances provide scale and priority but do not by themselves define a likelihood.

## Links

- [[wiki/concepts/awh-replay-force-field-optimization]]
- [[wiki/answers/tss-mbar-replay-force-field-optimization-route-plan]]
- [[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]

