---
type: source
status: active
created: 2026-06-30
updated: 2026-07-01
source_id: SRC-0012
display_title: "Multistate Reweighting and Configuration Mapping"
short_title: "MBAR with Configuration Mapping"
aliases:
  - "SRC-0012"
  - "MBAR with Configuration Mapping"
  - "Multistate Reweighting and Configuration Mapping"
source_path: raw/sources/SRC-0012-multistate-reweighting-and-configuration-mapping-together-accelerate-thermodynamic.pdf
imported_path: raw/sources/SRC-0012-multistate-reweighting-and-configuration-mapping-together-accelerate-thermodynamic.pdf
original_filename: "154108_1_online.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 03ec626dc3dc092e1e7c155f69e36e10691ca8f9cc06ea8426ef86491a1b85e2
authors:
  - "Himanshu Paliwal"
  - "Michael R. Shirts"
author_entities:
  - "[[wiki/entities/authors/michael-r-shirts]]"
year: 2013
venue: "Journal of Chemical Physics"
doi: "10.1063/1.4801332"
arxiv:
metadata_review_status: reviewed
areas:
  - research
categories:
  - research/molecular-simulation/free-energy
  - research/statistics/monte-carlo
tags:
  - mbar
  - configuration-mapping
  - reweighting
  - phase-space-overlap
  - math-heavy
related:
  - "[[wiki/concepts/mbar-with-configuration-mapping]]"
  - "[[wiki/concepts/free-energy-estimation]]"
  - "[[wiki/concepts/relative-binding-free-energy-benchmarking]]"
sources:
  - SRC-0012
cites_sources:
  - SRC-0023
citation_match_status: reviewed
cqt_review_status: linked
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: math-standard
---

# Multistate Reweighting and Configuration Mapping

Source ID: `SRC-0012`

## Raw source

- Repository path: `raw/sources/SRC-0012-multistate-reweighting-and-configuration-mapping-together-accelerate-thermodynamic.pdf`
- Open raw source: [raw/sources/SRC-0012-multistate-reweighting-and-configuration-mapping-together-accelerate-thermodynamic.pdf](../../raw/sources/SRC-0012-multistate-reweighting-and-configuration-mapping-together-accelerate-thermodynamic.pdf)

## Summary

This 2013 Journal of Chemical Physics paper combines MBAR with invertible configuration mappings to estimate free energies and other thermodynamic differences between states with poor or zero direct phase-space overlap. The key mathematical step is to evaluate MBAR on mapped, or "warped", reduced potentials that include the mapping Jacobian. [SRC-0012]

The paper demonstrates the method on truncated harmonic oscillators, rigid water model transformations, and solvated dipoles with different equilibrium bond lengths. It reports efficiency gains from orders of magnitude to five orders of magnitude in favorable cases. [SRC-0012]

## Key Points

- Standard reweighting methods require overlap between sampled configurations and target-state configurations; with zero overlap, no amount of sampling gives an unbiased free-energy difference. [SRC-0012, introduction]
- If an invertible, bijective mapping exists between phase spaces, samples can be transformed before evaluating reduced potentials. [SRC-0012, section II]
- The mapping Jacobian must be included in the reduced potential. [SRC-0012, eq. 1]
- Once warped reduced energies are computed, the standard MBAR self-consistent equations apply. [SRC-0012, eq. 2]
- The method is exact for the paper's truncated harmonic oscillator mapping, requiring no samples to estimate the free-energy difference once the exact map is known. [SRC-0012]
- Applications to rigid water models and dipoles show major efficiency gains but also show that benefits depend on mapping quality and observable type. [SRC-0012]

## Key equations

Warped reduced energy: [SRC-0012, eq. 1]

$$
u_{ij}^{w}(x_j)=u_i(T_{ji}(x_j))-\log|J_{ji}(x_j)|.
$$

MBAR with warped reduced energies: [SRC-0012, eq. 2]

$$
f_i=-\log\sum_{j=1}^{K}\sum_{n=1}^{N_j}
\frac{\exp[-u_{ij}^{w}(x_{jn})]}
{\sum_{k=1}^{K}N_k\exp[f_k-u_{kj}^{w}(x_{jn})]}.
$$

Harmonic mapping via reference state: [SRC-0012, eq. 3]

$$
T_i(x_i)=\frac{x_i-\mu_i}{\sigma_i},
\qquad
T_{ij}(x_i)=\frac{x_i-\mu_i}{\sigma_i}\sigma_j+\mu_j.
$$

Jacobian for the harmonic map: [SRC-0012, eq. 4]

$$
J_{ij}=\frac{\sigma_j}{\sigma_i},\qquad J_{ji}=\frac{\sigma_i}{\sigma_j}.
$$

## Equation inventory

| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |
| Warped reduced energy, eq. (1) | SRC-0012 section II | This page; [[wiki/concepts/mbar-with-configuration-mapping]] | Adds mapping and Jacobian to target-state reduced energy. | $u_i$, $T_{ji}$, $J_{ji}$ | Core mapped reweighting quantity. |
| MBAR with mapping, eq. (2) | SRC-0012 section II | This page; [[wiki/concepts/mbar-with-configuration-mapping]] | Uses warped energies in MBAR. | $f_i$, $u_{ij}^{w}$, $N_k$ | Free-energy estimator. |
| Reference-state map, eq. (3) | SRC-0012 section III.A | This page | Constructs pairwise maps through reference coordinates. | $T_i$, $T_{ij}$, $\mu_i$, $\sigma_i$ | Toy-model mapping. |
| Jacobian, eq. (4) | SRC-0012 section III.A | This page | Gives map volume factor. | $J_{ij}$, $\sigma_i$ | Required correction. |
| Harmonic warped energy, eq. (5) | SRC-0012 section III.A | This page | Applies map and Jacobian to oscillator. | $u_{ij}^{w}$, $K_i$ | Exact toy result. |
| Thermodynamic cycles, eqs. (6)-(7) | SRC-0012 water results | This page | Validate water-model transformations. | $\Delta G$, $\Delta H$, $\Delta S$ | Consistency checks. |
| Efficiency ratio, eq. (8) | SRC-0012 results | This page | Compares samples needed with and without mapping. | $N_{\mathrm{no\ mapping}}$, $N_{\mathrm{mapping}}$ | Efficiency claim. |

## Mathematical structure

The method assumes phase spaces $\Omega_i$ and $\Omega_j$ can be connected by an invertible map $T_{ij}:\Omega_i\to\Omega_j$. Instead of evaluating state $i$ on an impossible or irrelevant configuration from state $j$, the sample is first pulled back through $T_{ji}$. The Jacobian corrects the transformed measure. [SRC-0012, section II]

## Evidence

The truncated harmonic oscillator example has zero direct overlap but an exact mapping; the mapping estimator recovers the free energy exactly. [SRC-0012]

For SPC/E, TIP3P, and TIP4P water transformations, mapped MBAR gives thermodynamic-cycle-consistent free energies, enthalpies, and entropies and much lower uncertainty for some quantities than standard decoupling. [SRC-0012]

For solvated dipoles with different equilibrium bond lengths, MBAR with mapping requires 3-300 times fewer samples for comparable precision in the reported tests. [SRC-0012]

## Limitations and Caveats

- The limiting requirement is constructing an appropriate invertible mapping. [SRC-0012]
- Mapping improves overlap but does not guarantee equal gains for all observables; enthalpy of vaporization did not benefit as much as free energies and entropies in the water-model example. [SRC-0012]
- The examples are selected transformations where mappings are natural; broader molecular transformations may require nontrivial mapping design. [SRC-0012]

## Links

- [[wiki/concepts/mbar-with-configuration-mapping]]
- [[wiki/concepts/free-energy-estimation]]
- [[wiki/concepts/relative-binding-free-energy-benchmarking]]

## Claims

- [[wiki/claims/CLM-0005-configuration-mapping-extends-mbar]] - Invertible mappings can extend MBAR by transforming samples and including Jacobian-corrected warped reduced energies. [SRC-0012]
- [[wiki/claims/CLM-0004-mbar-is-optimal-but-overlap-limited]] - Mapped MBAR keeps MBAR's fixed-sample estimator structure while addressing raw-overlap failure modes. [SRC-0012] [SRC-0023]

## Questions

- [[wiki/questions/overlap-support-diagnostics-for-free-energy-estimators]] - How should raw and mapped overlap be diagnosed before trusting a mapped MBAR estimate? [SRC-0012]

## Tensions

- [[wiki/tensions/TEN-0004-configuration-mapping-overlap-gain-vs-support-risk]] - Mapping can create useful warped overlap, but a map still needs support and observable-specific validation. [SRC-0012]

## Open Questions

- Which chemically useful transformations admit simple invertible mappings that preserve enough Boltzmann overlap for mapped MBAR to be practical? [SRC-0012]

## Citation links

- `SRC-0023`: The references list M. Shirts and J. Chodera, Journal of Chemical Physics 129, 124105 (2008), which matches the ingested original MBAR source by author, venue, year, and article identifier. [SRC-0012]
- Citation review is complete for the currently ingested free-energy/adaptive-sampling cluster; it is not a full bibliography extraction.

## Metadata notes

- This paper is not part of the OPES main/SI bundle and was ingested as a separate source.

## Mathematical gaps

- The appendix proof and all water-model mapping details are summarized rather than fully reproduced.

## Ingestion QA

### Retrieval questions checked

- What problem does configuration mapping solve for MBAR?
- What is the warped reduced energy?
- Why is the Jacobian necessary?
- How does the mapped MBAR equation relate to standard MBAR?
- What examples validate the method?
- What efficiency gains are reported?
- What is the main limitation?

### Coverage decision

Complete at `coverage_profile: math-standard`. [SRC-0012]

### Known gaps

- Full appendix proof and exact molecular mapping recipes remain in the source PDF.
