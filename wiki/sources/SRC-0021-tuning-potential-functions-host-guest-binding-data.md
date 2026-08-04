---
type: source
status: active
created: 2026-06-30
updated: 2026-08-04
source_id: SRC-0021
display_title: "Tuning Potential Functions to Host-Guest Binding Data"
short_title: "Host-Guest Potential Tuning"
aliases:
  - "SRC-0021"
  - "Host-Guest Potential Tuning"
  - "Tuning Potential Functions to Host-Guest Binding Data"
source_path: raw/sources/SRC-0021-tuning-potential-functions-host-guest-binding-data.pdf
imported_path: raw/sources/SRC-0021-tuning-potential-functions-host-guest-binding-data.pdf
original_filename: "tuning-potential-functions-to-host-guest-binding-data.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 8cb7671c2b32e1eebe95ae82226b329bb451c6f173c9e1584edbb54a52606f57
authors:
  - "Jeffry Setiadi"
  - "Simon Boothroyd"
  - "David R. Slochower"
  - "David L. Dotson"
  - "Matthew W. Thompson"
  - "Jeffrey R. Wagner"
  - "Lee-Ping Wang"
  - "Michael K. Gilson"
author_entities: []
year: 2024
venue: "Journal of Chemical Theory and Computation"
doi: "10.1021/acs.jctc.3c01050"
arxiv:
metadata_review_status: reviewed
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/computational-drug-discovery
  - research/molecular-simulation/free-energy
  - research/biomolecules/proteins
  - research/experimental-benchmarking
tags:
  - host-guest
  - binding-free-energy
  - forcebalance
  - openff-evaluator
  - implicit-solvent
  - math-heavy
related:
  - "[[wiki/sources/SRC-0022-tuning-potential-functions-host-guest-binding-data-supporting-information]]"
  - "[[wiki/concepts/force-field-training-from-experimental-observables]]"
  - "[[wiki/concepts/relative-binding-free-energy-benchmarking]]"
sources:
  - SRC-0021
cites_sources:
  - SRC-0025
citation_match_status: reviewed
cqt_review_status: linked
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: math-standard
source_bundle: tuning-potential-functions-host-guest-binding-2024
bundle_role: main
---

# Tuning Potential Functions to Host-Guest Binding Data

Source ID: `SRC-0021`

## Raw source

- Repository path: `raw/sources/SRC-0021-tuning-potential-functions-host-guest-binding-data.pdf`
- Open raw source: [raw/sources/SRC-0021-tuning-potential-functions-host-guest-binding-data.pdf](../../raw/sources/SRC-0021-tuning-potential-functions-host-guest-binding-data.pdf)
## Source bundle

Main paper in the `tuning-potential-functions-host-guest-binding-2024` bundle. [[wiki/sources/SRC-0022-tuning-potential-functions-host-guest-binding-data-supporting-information|SRC-0022]] supplies the complete benchmark tables, restraint definitions, parameter trajectories, timing comparison, and prior-width analysis. [SRC-0021] [SRC-0022]

## Metadata notes

- The requested `ct3c01050.pdf` has DOI `10.1021/acs.jctc.3c01050` and the same article content as the existing repository copy, but a different SHA256 because the requested copy includes later download-time modifications. It was therefore deduplicated to `SRC-0021` rather than imported as a new source. [SRC-0021]
- Requested-file SHA256 checked on 2026-08-04: `3fdaaf072c38d7f1df863b4455d6b0363e19d4ed3e08881f65cac4fa92c469e2`.

## Summary

This 2024 JCTC paper extends OpenFF Evaluator and ForceBalance to train potential-function parameters against host-guest absolute binding free energies. [SRC-0021]

As a proof of principle, the authors optimize OBC2 generalized Born cavity radii on 36 host-guest systems, test on 90 additional host-guest systems, and evaluate transfer to 59 protein-ligand systems and hydration free energies. [SRC-0021]

## Key Points

- The paper argues that host-guest complexes are simpler binding models than protein-ligand systems and can isolate force-field errors more cleanly. [SRC-0021]
- The infrastructure computes host-guest ABFEs and gradients with respect to force-field parameters, then passes them to ForceBalance. [SRC-0021]
- The initial application optimizes OBC2 GB cavity radii, not a full molecular mechanics force field. [SRC-0021]
- Refitting improves both training and host-guest test performance and shows encouraging transfer to protein-ligand ABFEs. [SRC-0021]
- The optimized radii are smaller than baseline radii and lead to excessively favorable hydration free energies, exposing a binding/HFE tradeoff. [SRC-0021]
- OBC2 implicit solvent in OpenMM gives about a 10-fold speedup relative to corresponding explicit-solvent ABFE calculations in this study. [SRC-0021]
- The fitted H and N radii become physically suspect: H falls from 1.20 to 0.707 Angstrom and N from 1.55 to 0.533 Angstrom, while O rises from 1.50 to 1.632 Angstrom. [SRC-0021, Table 1]

## Key equations

OBC/GB electrostatic self energy, source Eq. (1A):

$$
G_{\mathrm{GB}}^{\mathrm{self}}
=\frac{1}{2}
\left(\frac{1}{\epsilon_{\mathrm{solute}}}-\frac{1}{\epsilon_{\mathrm{solvent}}}\right)
\sum_i \frac{q_i^2}{R_i}.
$$

[SRC-0021, Eq. 1A]

Binding-free-energy parameter gradient, source Eq. (5):

$$
\frac{\partial \Delta G_b}{\partial \theta}
=
\left\langle\frac{\partial U}{\partial\theta}\right\rangle_{\mathrm{bound}}
-
\left\langle\frac{\partial U}{\partial\theta}\right\rangle_{\mathrm{free}}.
$$

[SRC-0021, Eq. 5]

Central finite-difference energy derivative, source Eq. (6):

$$
\frac{\partial U}{\partial\theta}
\approx
\frac{U(\theta+h)-U(\theta-h)}{2h}.
$$

The implementation uses $h=10^{-4}\theta$ for the fitted cavity radius. [SRC-0021, Eq. 6]

Gradient for multiple poses, source Eq. (7):

$$
\frac{\partial \Delta G_b}{\partial \theta}
=
\sum_{k=1}^{N_b}
p_k
\frac{\partial \Delta G_{b,k}}{\partial \theta},
\quad
p_k=
\frac{\exp[-\beta\Delta G_{b,k}]}
{\sum_l\exp[-\beta\Delta G_{b,l}]}.
$$

[SRC-0021, Eq. 7]

ForceBalance objective:

$$
\mathcal L(\theta)
=
\sum_i
\left[
\frac{y_i(\theta)-y_i^{\mathrm{exp}}}{\sigma_i}
\right]^2
+
\sum_j
\left[
\frac{\theta_j-\theta_{j,0}}{\sigma_{\theta,j}}
\right]^2.
$$

[SRC-0021, Eq. 8]

Two-pose cyclodextrin binding free energy, source Eq. (9):

$$
\Delta G_b
=-RT\ln\left[
e^{-\Delta G_p/(RT)}+e^{-\Delta G_s/(RT)}
\right].
$$

[SRC-0021, Eq. 9]

## Equation inventory

| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |
| GB self energy, Eq. (1A) | SRC-0021, Eq. (1A), p. 241 | This page | Defines one optimized implicit-solvent energy component. | $q_i$, $R_i$, $\epsilon$ | Shows direct dependence on fitted radii. |
| ABFE gradient, Eq. (5) | SRC-0021, Eq. (5), p. 241 | This page | Expresses the property gradient as bound/free ensemble averages. | $U$, $\theta$ | Connects ABFE estimates to ForceBalance. |
| Central difference, Eq. (6) | SRC-0021, Eq. (6), p. 242 | This page | Estimates energy derivatives after parameter perturbation. | $U$, $\theta$, $h$ | Defines the implemented numerical gradient. |
| Multi-pose gradient, Eq. (7) | SRC-0021, Eq. (7), p. 242 | This page | Boltzmann-weights gradients over binding poses. | $p_k$, $\Delta G_{b,k}$, $\theta$ | Required for asymmetric cyclodextrin hosts. |
| ForceBalance objective, Eq. (8) | SRC-0021, Eq. (8), p. 242 | This page; [[wiki/concepts/force-field-training-from-experimental-observables]] | Fits physical properties with parameter priors. | $y_m$, $\theta_i$, $\sigma_i$ | Core regularized optimization objective. |
| Two-pose free energy, Eq. (9) | SRC-0021, Eq. (9), p. 242 | This page | Combines primary- and secondary-face cyclodextrin poses. | $\Delta G_p$, $\Delta G_s$, $R$, $T$ | Prevents selecting only one pose. |

## Variable glossary

- $U$: total potential energy used in the endpoint-gradient construction.
- $\theta$: optimized force-field parameter; here, an OBC2 GB cavity radius.
- $\Delta G_b$: standard absolute binding free energy.
- $p_k$: Boltzmann probability assigned to binding pose $k$.
- $R_i$ and $q_i$: effective Born radius and partial charge of atom $i$.
- $\sigma_i$: prior width controlling the L2 penalty on parameter displacement; the production fit uses 0.5 Angstrom.
- $d_n$: property residual scale; the binding target uses 1 kcal/mol.

## Algorithm and protocol map

1. Curate 126 aqueous cyclodextrin, cucurbituril, and octa-acid complexes; select six complexes per host for a balanced 36-system training set and reserve 90 systems for testing. [SRC-0021, section 2.5]
2. Compute host-guest ABFEs with attach-pull-release, Boresch-style restraints, thermodynamic integration, and two binding poses for cyclodextrins. [SRC-0021, section 2.2]
3. Re-evaluate endpoint energies at perturbed radii, combine pose gradients, and pass predictions and gradients through OpenFF Evaluator to ForceBalance. [SRC-0021, Eqs. 5-8]
4. Optimize five radii with a Gauss-Newton approximation and L2 prior, then independently recalculate the held-out host-guest set. [SRC-0021, sections 2.1 and 3.2]
5. Test cross-system transfer on 59 protein-ligand ABFEs, 100 neutral-molecule hydration free energies, and 100 ns unrestrained simulations of four apo proteins. [SRC-0021, sections 2.3-2.5 and 3.3-3.4]

## Evidence

The dataset includes 126 host-guest complexes, with 36 selected for training and 90 held out for host-guest testing. [SRC-0021]

- Training-set RMSE falls from 21.0 to 2.9 kcal/mol, although $R^2$ decreases from 0.7 to 0.6; test-set RMSE falls from 19.5 to 2.1 kcal/mol while $R^2$ rises from 0.5 to 0.8. [SRC-0021, section 3.2] [SRC-0022, Tables S4-S5]
- Across 59 protein-ligand systems, RMSE falls from 7.4 to 2.4 kcal/mol with ff14SB/Sage and from 6.4 to 2.0 kcal/mol with ff14SB/GAFF2, but correlation is roughly halved. [SRC-0021, section 3.3] [SRC-0022, Table S10]
- On 100 neutral FreeSolv molecules, hydration RMSE worsens from 2.11 to 19.12 kcal/mol and $R^2$ from 0.79 to 0.35; rank correlation remains similar, showing a large calibration failure rather than total loss of ordering. [SRC-0021, section 3.4] [SRC-0022, Table S13]
- The supporting information adds complete ABFE and HFE tables, per-host and per-protein statistics, timing comparisons, parameter trajectories, and prior-width sensitivity. [SRC-0022]

## Limitations and Caveats

- The proof-of-principle fit improves binding but worsens hydration free energies, indicating that refitting one parameter class against one observable class can create property tradeoffs. [SRC-0021]
- The optimized radii are specific to OBC2 GBSA and should not be treated as generally transferable classical force-field parameters. [SRC-0021]
- Host-guest complexes reduce but do not eliminate modeling ambiguities such as restraints, protonation, and host flexibility. [SRC-0021]
- The protein-ligand calculations use a separate double-decoupling workflow outside OpenFF Evaluator, so they validate the fitted radii but not an end-to-end Evaluator protein-ligand implementation. [SRC-0021, section 2.3]
- The 100 ns apo-protein checks preserve tertiary folds but show greater 2-4 Angstrom RMSD and helix flexibility with the fitted radii; this is not evidence of general protein-dynamics fidelity. [SRC-0021, section 3.3]

## Links

- [[wiki/sources/SRC-0022-tuning-potential-functions-host-guest-binding-data-supporting-information]]
- [[wiki/concepts/force-field-training-from-experimental-observables]]
- [[wiki/concepts/relative-binding-free-energy-benchmarking]]
- [[wiki/questions/force-field-training-validation-scope]]
- [[wiki/claims/CLM-0009-observable-fitting-needs-held-out-validation]]
- [[wiki/claims/CLM-0012-forcebalance-reduces-manual-fitting-noise]]
- [[wiki/tensions/TEN-0006-observable-fitting-gain-vs-transferability-tradeoff]]

## Claims

- [[wiki/claims/CLM-0009-observable-fitting-needs-held-out-validation]] - Host-guest binding-data fitting needs held-out observables because binding gains can coexist with hydration-free-energy degradation. [SRC-0021]
- [[wiki/claims/CLM-0012-forcebalance-reduces-manual-fitting-noise]] - ForceBalance-Evaluator makes the optimization reproducible but cannot remove target-selection limits. [SRC-0021] [SRC-0025]

## Questions

- [[wiki/questions/force-field-training-validation-scope]] - What held-out systems and observables are enough for force-field transfer claims? [SRC-0021]

## Tensions

- [[wiki/tensions/TEN-0006-observable-fitting-gain-vs-transferability-tradeoff]] - Host-guest binding improvements trade off against hydration free energies in this fit. [SRC-0021]

## Citation links

- `SRC-0025`: The references list Wang, Martinez, and Pande, "Building Force Fields," as the ForceBalance method used in the optimization workflow. This matches the ingested ForceBalance source. [SRC-0021]

## Open Questions

- What additional GB model terms or training observables are required to fit both binding free energies and hydration free energies? [SRC-0021]

## Mathematical gaps

- The cross term, surface-area term, effective-distance kernel, OBC radius transform, and soft-core alchemical attenuation equations remain in the raw paper; the inventory captures the equations most central to optimization and implementation flow. [SRC-0021, Eqs. 1B-4 and 10A-10E]
- No theorem or long proof is presented. The appendix derivation of the two-pose combination is summarized by source Eq. (9), not reproduced step by step. [SRC-0021, Appendix]

## Ingestion QA

### Retrieval questions checked

- Why use host-guest binding data for training?
- What framework was extended?
- Which parameters were optimized?
- How are binding free-energy gradients passed to ForceBalance?
- What transfer and failure modes were reported?
- How large are the held-out host-guest, protein-ligand, and hydration effects?
- Why do the optimized nitrogen and hydrogen radii improve binding while harming hydration and protein flexibility?

### Coverage decision

Complete at `coverage_profile: math-standard` for the deduplicated main/SI bundle. The page preserves the main optimization equations, parameter meanings, algorithm flow, quantitative validation, and the functional-form limitation. [SRC-0021] [SRC-0022]

### Known gaps

- Full benchmark rows and every restraint/window parameter remain in SRC-0022 rather than being duplicated here.
- External repositories, benchmark structures, and raw simulation trajectories referenced by the paper were not part of the requested bundle and were not ingested.
