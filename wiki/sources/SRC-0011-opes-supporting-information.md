---
type: source
status: active
created: 2026-06-30
updated: 2026-06-30
source_id: SRC-0011
display_title: "Supporting Information for Rethinking Metadynamics"
short_title: "OPES Supporting Information"
aliases:
  - "SRC-0011"
  - "OPES Supporting Information"
  - "Supporting Information for Rethinking Metadynamics"
source_path: raw/sources/SRC-0011-supporting-information-for-rethinking-metadynamics-from-bias-potentials.pdf
imported_path: raw/sources/SRC-0011-supporting-information-for-rethinking-metadynamics-from-bias-potentials.pdf
original_filename: "jz0c00497_si_001.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 84c972bea49a526039f324e7b7da438cae152e0b05f0698f0c142cb7c4d6c052
areas:
  - research
categories:
  - research/adaptive-sampling
  - research/molecular-simulation/free-energy
tags:
  - opes
  - supporting-information
  - kernel-compression
  - metadynamics
  - math-heavy
related:
  - "[[sources/SRC-0010-rethinking-metadynamics-opes]]"
  - "[[concepts/on-the-fly-probability-enhanced-sampling]]"
sources:
  - SRC-0011
  - SRC-0010
sensitivity: public
encryption: none
source_bundle: opes-rethinking-metadynamics
bundle_role: supplement
ingestion_status: complete
coverage_profile: math-standard
---

# Supporting Information for Rethinking Metadynamics

Source ID: `SRC-0011`

## Raw source

- Repository path: `raw/sources/SRC-0011-supporting-information-for-rethinking-metadynamics-from-bias-potentials.pdf`
- Local relative link: [Open raw source](../../raw/sources/SRC-0011-supporting-information-for-rethinking-metadynamics-from-bias-potentials.pdf)

## Source bundle

This is the supporting information for [[sources/SRC-0010-rethinking-metadynamics-opes]]. [SRC-0010] [SRC-0011]

## Summary

The supporting information gives OPES implementation details, especially kernel compression, bandwidth rescaling, normalization-factor estimation, the barrier parameter, reweighting behavior, and extended results on model systems and alanine peptides. [SRC-0011]

## Key Points

- OPES compresses Gaussian kernels on the fly instead of storing a full grid or every deposited kernel. [SRC-0011]
- New kernels are merged into existing kernels when the Mahalanobis distance is below a threshold, with $d_t=1$ suggested as a useful default. [SRC-0011]
- The compressed-kernel representation avoids predefining the explored collective-variable region and is more natural for higher-dimensional CV spaces than grids. [SRC-0011]
- Bandwidths shrink using the main-text formula and an effective sample size; kernel heights are adjusted consistently. [SRC-0011, eqs. S6-S8]
- The barrier parameter sets a practical bias cap and can also set the bias factor $\gamma$ and regularization parameter $\epsilon$. [SRC-0011]
- Extended examples compare OPES and metadynamics on a suboptimal double well, alanine dipeptide, and alanine tetrapeptide. [SRC-0011]

## Key equations

Diagonal Gaussian kernel: [SRC-0011, eq. S1]

$$
G(s,s^0)=h\exp\left[-\frac{1}{2}\sum_i\left(\frac{s_i-s_i^0}{\sigma_i}\right)^2\right].
$$

Mahalanobis distance for compression: [SRC-0011, eq. S2]

$$
d(s^0,G)=\sqrt{\sum_i\left(\frac{s_i-s_i^0}{\sigma_i}\right)^2}.
$$

Kernel merge rule: [SRC-0011, eqs. S3-S5]

$$
h=h_1+h_2,\qquad
s^0=h^{-1}(h_1s_1+h_2s_2).
$$

Bandwidth and effective sample size: [SRC-0011, eqs. S6-S7]

$$
\sigma_i^{(n)}=\sigma_i^{(0)}\left[N_{\mathrm{eff}}^{(n)}(d+2)/4\right]^{-1/(d+4)},
\qquad
N_{\mathrm{eff}}^{(n)}=\frac{\left(\sum_k^n w_k\right)^2}{\sum_k^n w_k^2}.
$$

Barrier-parameter bias cap: [SRC-0011, eq. S10]

$$
\min_s V_n(s)=-\Delta E.
$$

## Equation inventory

| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |
| Gaussian kernel, eq. S1 | SRC-0011 Algorithmic details | This page | Defines compressed probability kernels. | $G$, $h$, $s$, $\sigma$ | Bias representation. |
| Mahalanobis distance, eq. S2 | SRC-0011 Algorithmic details | This page | Tests whether to merge a new kernel. | $d$, $s^0$, $G$ | Compression criterion. |
| Merge rules, eqs. S3-S5 | SRC-0011 Algorithmic details | This page | Combines two Gaussian kernels. | $h$, $s^0$, $\sigma$ | Kernel compression. |
| Bandwidth rescaling, eq. S6 | SRC-0011 Bandwidth rescaling | This page; [[concepts/on-the-fly-probability-enhanced-sampling]] | Shrinks bandwidth. | $N_{\mathrm{eff}}$, $d$ | Resolution schedule. |
| Effective sample size, eq. S7 | SRC-0011 Bandwidth rescaling | This page | Quantifies weighted sample information. | $w_k$ | Stable early updates. |
| Normalization estimate, eq. S9 | SRC-0011 Normalization factor | [[concepts/on-the-fly-probability-enhanced-sampling]] | Estimates $Z_n$ from compressed kernels. | $Z_n$, $G$, $S$ | Explored-region normalization. |
| Barrier cap, eq. S10 | SRC-0011 Barrier parameter | This page | Sets maximum bias depth. | $\Delta E$, $V_n$ | User parameter meaning. |

## Algorithmic recursions

For each new kernel, OPES computes the minimum Mahalanobis distance to existing compressed kernels. If the distance is below the threshold, the new kernel is merged with the nearest kernel and the merge check repeats recursively; otherwise the new kernel is added. [SRC-0011]

## Evidence

The supplement reports extended model-system and alanine-peptide results, including robustness of OPES reweighting to initial transients and high-dimensional alanine tetrapeptide exploration. [SRC-0011]

## Limitations and Caveats

- Kernel compression reduces cost but introduces a coarsening threshold; higher thresholds can reduce kernel count at the cost of coarser probability estimates. [SRC-0011]
- Computational cost scales roughly with the number of compressed kernels; neighbor-list acceleration is identified as future work. [SRC-0011]

## Links

- [[sources/SRC-0010-rethinking-metadynamics-opes]]
- [[concepts/on-the-fly-probability-enhanced-sampling]]

## Open Questions

- How should compression threshold and bandwidth schedules be tuned for very high-dimensional CV spaces beyond the tested examples? [SRC-0011]

## Metadata notes

- Bundle role was inferred from the title page: "SUPPORTING INFORMATION Rethinking Metadynamics...".

## Mathematical gaps

- The wiki records the implementation-critical formulas but not all figures or simulation parameter tables.

## Ingestion QA

### Retrieval questions checked

- Which main paper does this support?
- How does kernel compression work?
- What does $d_t$ control?
- How are bandwidths rescaled?
- How is effective sample size defined?
- What does the barrier parameter do?
- What examples are extended in the supplement?

### Coverage decision

Complete at `coverage_profile: math-standard` as the supplement component of the OPES source bundle. [SRC-0011]

### Known gaps

- Full figure-level comparisons and all input files remain external to the wiki.
