---
type: claim
status: active
created: 2026-07-01
updated: 2026-07-30
claim_status: limited
claim_scope: cross-source
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/experimental-benchmarking
tags:
  - claim
  - force-field-training
  - validation
related:
  - "[[wiki/concepts/force-field-training-from-experimental-observables]]"
  - "[[wiki/concepts/automated-force-field-training]]"
  - "[[wiki/questions/force-field-training-validation-scope]]"
  - "[[wiki/tensions/TEN-0006-observable-fitting-gain-vs-transferability-tradeoff]]"
sources:
  - SRC-0014
  - SRC-0021
  - SRC-0025
  - SRC-0026
sensitivity: public
encryption: none
---

# Observable-Fitted Force Fields Need Held-Out Validation

## Claim

Force-field parameters fitted to selected observables need held-out observables and systems before their transferability should be trusted. [SRC-0014] [SRC-0021] [SRC-0025] [SRC-0026]

## Scope

This claim covers experimental-observable force-field fitting in the scoped cluster, including water-property, SAXS-driven lipid, and host-guest binding-data fitting. It does not say observable fitting is unreliable; it says validation must be broader than the training objective. [SRC-0014] [SRC-0021] [SRC-0025] [SRC-0026]

## Evidence

- SRC-0014 fits lipid Lennard-Jones parameters to SAXS profiles and then tests organic-solvent stress and pure-lipid membrane properties, finding useful improvements but also transferability limits. [SRC-0014]
- SRC-0021 fits OBC2 GB cavity radii to host-guest binding free energies and validates against host-guest test systems, protein-ligand binding, and hydration free energies; the hydration-free-energy results reveal a tradeoff. [SRC-0021]
- SRC-0025/SRC-0026 fit thermodynamic properties and ab initio cluster data, then test O-O radial structure, self-diffusion, and viscosity outside the fitting objective. The low-temperature TIP3P-FB density error also exposes a functional-form limit. [SRC-0025] [SRC-0026]

## Caveats

- Held-out validation can diagnose a problem without identifying whether the force-field form, sampling, forward model, or experimental uncertainty caused it. [SRC-0021]
- Supporting-information pages provide important audit detail on which properties were actually held out. [SRC-0015] [SRC-0022] [SRC-0026]

## Links

- [[wiki/sources/SRC-0014-lipid-force-field-saxs-reparameterization]]
- [[wiki/sources/SRC-0021-tuning-potential-functions-host-guest-binding-data]]
- [[wiki/sources/SRC-0025-building-force-fields-automatic-systematic-reproducible-approach]]
- [[wiki/sources/SRC-0026-building-force-fields-forcebalance-supporting-information]]
- [[wiki/concepts/tip3p-fb-and-tip4p-fb-water-models]]
- [[wiki/concepts/force-field-training-from-experimental-observables]]
- [[wiki/questions/force-field-training-validation-scope]]
- [[wiki/tensions/TEN-0006-observable-fitting-gain-vs-transferability-tradeoff]]
