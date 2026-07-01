---
type: source
status: active
created: 2026-06-30
updated: 2026-06-30
source_id: SRC-0014
display_title: "Reparameterizing a Lipid Force Field Using SAXS"
short_title: "Lipid Force Field SAXS Reparameterization"
aliases:
  - "SRC-0014"
  - "Lipid Force Field SAXS Reparameterization"
  - "Reparameterizing a Lipid Force Field Using SAXS"
source_path: raw/sources/SRC-0014-lipid-force-field-saxs-reparameterization.pdf
imported_path: raw/sources/SRC-0014-lipid-force-field-saxs-reparameterization.pdf
original_filename: "reparameterizing-a-lipid-force-field-using-small-angle-x-ray-scattering-to-improve-predictions-of-multicomponent.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 020e1bbd727d71df5e9e25c9ba1c8b1c0376980ed65a7bfed097493b298c11eb
authors:
  - "Omar N. A. Demerdash"
  - "Micholas Dean Smith"
  - "Lee-Ping Wang"
  - "Sai Venkatesh Pingali"
  - "Joshua O. Aggrey"
author_entities: []
year: 2026
venue: "Journal of Physical Chemistry B"
doi: "10.1021/acs.jpcb.5c08658"
arxiv:
metadata_review_status: reviewed
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/biomolecules/lipids
tags:
  - forcebalance
  - lipid-force-field
  - saxs
  - charmm36
  - math-heavy
related:
  - "[[wiki/sources/SRC-0015-lipid-force-field-saxs-reparameterization-supporting-information]]"
  - "[[wiki/concepts/force-field-training-from-experimental-observables]]"
  - "[[wiki/concepts/automated-force-field-training]]"
sources:
  - SRC-0014
cites_sources:
  - SRC-0025
citation_match_status: reviewed
cqt_review_status: linked
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: math-standard
---

# Reparameterizing a Lipid Force Field Using SAXS

Source ID: `SRC-0014`

## Raw source

- Repository path: `raw/sources/SRC-0014-lipid-force-field-saxs-reparameterization.pdf`
- Open raw source: [raw/sources/SRC-0014-lipid-force-field-saxs-reparameterization.pdf](../../raw/sources/SRC-0014-lipid-force-field-saxs-reparameterization.pdf)
## Source bundle

Main paper for SRC-0015, the supporting information. [SRC-0014] [SRC-0015]

## Summary

This 2026 JPCB paper uses ForceBalance-SAS to tune selected CHARMM36 lipid Lennard-Jones parameters against SAXS intensities for a mixed POPE/POPG membrane, then tests whether those parameters transfer to organic-solvent stress and pure-lipid membrane properties. [SRC-0014]

The key result is that SAXS fitting can improve the training system and some validation observables, but the authors explicitly diagnose transferability limits and argue that SAXS alone may be insufficient without complementary SANS information. [SRC-0014]

## Key Points

- The training observable is a condensed-phase SAXS profile, not quantum chemistry or a small set of scalar membrane observables. [SRC-0014]
- The optimized parameters are restricted mainly to Lennard-Jones $\sigma$ and $\epsilon$ terms for selected lipid atom groups. [SRC-0014]
- ForceBalance-SAS alternates MD simulation, SAXS calculation, objective/gradient evaluation, and trust-radius optimization. [SRC-0014]
- The paper reports about 10.0-fold and 7.5-fold reductions in $\chi^2$ for membranes under 1-butanol and THF stress, respectively, after tuning. [SRC-0014]
- The tuned force field improves membrane thickness predictions for pure lipid systems, but not all transfer tests pass. [SRC-0014]
- The authors identify missing contrast information as a limitation and specifically point to the need for SANS in addition to SAXS. [SRC-0014]

## Key equations

ForceBalance-SAS minimizes a discrepancy between experimental and calculated scattering intensities. In abstract form:

$$
\chi^2(\lambda)=\sum_i
\left[
\frac{I_{\mathrm{calc}}(q_i;\lambda)-I_{\mathrm{exp}}(q_i)}
{\sigma_i}
\right]^2,
$$

where $\lambda$ denotes force-field parameters. [SRC-0014]

The calculated SAXS amplitudes are linearly rescaled before comparison:

$$
I_{\mathrm{fit}}(q_i)=a I_{\mathrm{raw,calc}}(q_i)+b.
$$

[SRC-0014]

For an ensemble observable $A$, the force-field derivative includes a covariance-like response term:

$$
\frac{\partial \langle A\rangle_{\lambda}}{\partial \lambda}
=
\left\langle \frac{\partial A}{\partial \lambda}\right\rangle_{\lambda}
-\beta\,\mathrm{Cov}_{\lambda}
\left(A,\frac{\partial U}{\partial \lambda}\right).
$$

[SRC-0014]

## Equation inventory

| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |
| SAXS residual | SRC-0014 Methods | This page; [[wiki/concepts/force-field-training-from-experimental-observables]] | Fits calculated SAXS to experiment. | $q_i$, $I_{\mathrm{calc}}$, $I_{\mathrm{exp}}$, $\lambda$ | Objective function. |
| Linear intensity rescaling | SRC-0014 Methods | This page | Aligns calculated and experimental intensity amplitudes. | $a$, $b$, $I_{\mathrm{raw,calc}}$ | Preprocessing before residuals. |
| Observable response derivative | SRC-0014 Methods | This page | Gives parameter gradients for ensemble averages. | $A$, $U$, $\beta$, $\lambda$ | Gradient-based fitting. |

## Evidence

The final model is assessed on solvent-stressed membrane SAXS and on pure POPE/POPG membrane thickness and area-per-lipid observables. [SRC-0014]

The paper reports that individual optimization trials can fall into rugged local landscapes and that some head- or tail-only parameter optimizations fail transfer tests. [SRC-0014]

## Limitations and Caveats

- A single SAXS profile does not uniquely identify all membrane structural features relevant to transferability. [SRC-0014]
- The optimized parameter set is local to the chosen CHARMM36 functional form and the selected atom groups. [SRC-0014]
- The paper treats missing polarization, charge transfer, and damping effects as possible limits of classical pairwise-additive reparameterization. [SRC-0014]

## Links

- [[wiki/sources/SRC-0015-lipid-force-field-saxs-reparameterization-supporting-information]]
- [[wiki/concepts/force-field-training-from-experimental-observables]]
- [[wiki/concepts/automated-force-field-training]]
- [[wiki/questions/force-field-training-validation-scope]]
- [[wiki/claims/CLM-0009-observable-fitting-needs-held-out-validation]]
- [[wiki/claims/CLM-0012-forcebalance-reduces-manual-fitting-noise]]
- [[wiki/tensions/TEN-0006-observable-fitting-gain-vs-transferability-tradeoff]]

## Claims

- [[wiki/claims/CLM-0009-observable-fitting-needs-held-out-validation]] - SAXS-driven lipid fitting needs held-out systems and observables before transferability is trusted. [SRC-0014]
- [[wiki/claims/CLM-0012-forcebalance-reduces-manual-fitting-noise]] - ForceBalance-SAS makes optimization systematic, but the fitted target still bounds transferability. [SRC-0014] [SRC-0025]

## Questions

- [[wiki/questions/force-field-training-validation-scope]] - What held-out validation is enough before treating a fitted force field as transferable? [SRC-0014]

## Tensions

- [[wiki/tensions/TEN-0006-observable-fitting-gain-vs-transferability-tradeoff]] - SAXS fitting improves targeted behavior but does not remove transferability limits. [SRC-0014]

## Citation links

- `SRC-0025`: The references list Wang, Martinez, and Pande, "Building Force Fields," as the original ForceBalance method used by ForceBalance-SAS. This matches the ingested ForceBalance source. [SRC-0014]

## Open Questions

- What combination of SAXS, SANS, and scalar membrane properties is sufficient to constrain transferable lipid parameters? [SRC-0014]

## Mathematical gaps

- The wiki records the objective, rescaling, and response-gradient structure, but not every ForceBalance trust-radius implementation detail.

## Ingestion QA

### Retrieval questions checked

- What observables were used for lipid force-field reparameterization?
- What parameters were optimized?
- How does ForceBalance-SAS use scattering intensities?
- What validation systems were used?
- What transferability limitations were reported?

### Coverage decision

Complete at `coverage_profile: math-standard`. [SRC-0014]

### Known gaps

- Full numerical parameter tables are left in the source and supporting information rather than reproduced in the wiki.
