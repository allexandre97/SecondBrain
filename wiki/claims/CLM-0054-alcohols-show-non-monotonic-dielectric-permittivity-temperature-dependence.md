---
type: claim
status: active
created: 2026-10-01
updated: 2026-10-01
claim_status: supported
claim_scope: local
areas:
  - research
categories:
  - research/experimental-benchmarking
tags:
  - claim
  - dielectric-permittivity
  - dielectric-constant
  - dielectric-loss
  - alcohols
  - temperature-dependence
  - microwave-dielectric-heating
related:
  - "[[wiki/sources/SRC-0095-temperature-dependent-complex-dielectric-permittivity-a-simple-measurement]]"
sources:
  - SRC-0095
sensitivity: public
encryption: none
---

# Alcohols Show Non-Monotonic Dielectric Permittivity-Temperature Dependence, Unlike Water and Non-Alcohol Organic Solvents

## Claim

Across a benchtop measurement spanning water, nine non-alcohol organic solvents, and four alcohols near 2.45 GHz, water and the non-alcohol organics show a monotonic decrease in both dielectric constant ($\varepsilon'$) and dielectric loss factor ($\varepsilon''$) as temperature increases (well fit by a simple three-parameter exponential decay). Alcohols (ethanol, methanol, isopropanol, 2-pentanol) instead show $\varepsilon'$ and $\varepsilon''$ both rising with temperature to a maximum and then falling, a qualitatively different, non-monotonic behavior that requires a six-parameter modified lognormal fit rather than a simple exponential. [SRC-0095, §"Dielectric permittivity of alcohols", §"Conclusions"]

## Scope

Local to this single source's measured solvent set (water; MIBK, THF, γ-valeractone/valerolactone, DMSO, DMF, ethyl acetate, acetonitrile, 2-methyl-THF, acetone; ethanol, methanol, isopropanol, 2-pentanol), measured near 2.45 GHz (1.5-2.6 GHz reflectometer range) at temperatures up to each solvent's $T_{\mathrm{MAX}}$ (chosen to keep vapor pressure ≤7 bar). The claim does not establish how general the alcohol-vs-non-alcohol distinction is beyond these specific compounds, nor whether it holds at other frequencies. [SRC-0095, Methods, Tables 1-2]

## Evidence

- Non-alcohol organics (Table 1): all nine solvents and water fit $\varepsilon = A_1\cdot\exp(-A_2 T) + A_3$ with standard error <3% for both $\varepsilon'$ and $\varepsilon''$; $A_2$ is negative in every row, giving monotonic decay. [SRC-0095, Table 1]
- Alcohols (Table 2, Fig. 7): ethanol and isopropanol example curves (Fig. 7a-b) visibly rise from room temperature to a peak (ethanol $\varepsilon'$ peak ≈15 near 50 °C; isopropanol $\varepsilon'$ peak ≈11.5 near 60-70 °C) before falling; all four alcohols require the six-parameter lognormal fit (Eq. 2) with standard error <3.5%. [SRC-0095, Fig. 7, Table 2]
- The paper explicitly states this reversal ("alcohols seemingly share a separate behavior") as a qualitative departure from the monotonic water/non-alcohol-organic trend, and from the paper's own simpler exponential model, which was retained only for the monotonic class. [SRC-0095, Conclusions]

## Caveats

- The underlying raw per-temperature data points for both solvent classes are not in the ingested PDF (they are stated to be in Supplementary Figs. S3-S5); this claim rests on the fitted curve shapes and fit-parameter behavior reported in the main text, not independently re-derived from raw points. [SRC-0095, Tables 1-2]
- No mechanistic explanation is offered in the paper for why alcohols specifically show the reversal (e.g., hydrogen-bonding network reorganization with temperature is plausible but not discussed in this source). [SRC-0095]
- Prior literature is cited only generally (refs. 35, 60) as establishing that alcohol permittivity is nonmonotonic in temperature; this paper's contribution is the quantitative fit and the direct water/organic-solvent comparison, not the qualitative observation itself. [SRC-0095, §"Dielectric permittivity of alcohols"]

## Links

- [[wiki/sources/SRC-0095-temperature-dependent-complex-dielectric-permittivity-a-simple-measurement]]
