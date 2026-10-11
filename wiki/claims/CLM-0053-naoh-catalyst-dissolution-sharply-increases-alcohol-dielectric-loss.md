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
  - biodiesel
  - transesterification
  - microwave-dielectric-heating
  - dielectric-loss
  - sodium-hydroxide-catalyst
  - ionic-conduction
related:
  - "[[wiki/sources/SRC-0094-investigation-of-microwave-dielectric-properties-of-biodiesel-components]]"
sources:
  - SRC-0094
sensitivity: public
encryption: none
---

# NaOH Catalyst Dissolution Sharply Increases Alcohol Dielectric Loss, With a Stronger Effect in Methanol

## Claim

Dissolving a very small amount of NaOH catalyst (0.18 wt% relative to oil) into ethanol or methanol decreases the solvent's dielectric constant ($\varepsilon'$) but sharply increases its dielectric loss factor ($\varepsilon''$) via ionic conduction, and changes the shape of $\varepsilon''(f)$ from a peaked curve (pure alcohol) to a monotonic asymptotic decrease. The effect is substantially larger for methanol-NaOH than for ethanol-NaOH across the measured frequency range (280 MHz-4.5 GHz) and all tested temperatures (30-75 °C), implying faster microwave heating for methanol-catalyst mixtures at matched NaOH loading. [SRC-0094, §3.3]

## Scope

Local to this single source. The result is specific to soybean-oil-derived transesterification solvent ratios (ethanol:NaOH at 0.066 g NaOH per 19.3 mL ethanol; methanol:NaOH at 0.091 g NaOH per 10.235 mL methanol), to NaOH as the catalyst, and to the 280 MHz-4.5 GHz / 30-75 °C measurement window. Other catalysts (e.g., KOH, acid catalysts), other NaOH concentrations, and frequencies outside this window are not covered. [SRC-0094, §2]

## Evidence

- At 915 MHz and 30 °C, $\varepsilon''$ rises from 7.57±0.25 (pure ethanol) to 11.04±0.09 (ethanol+NaOH), and from 6.55±0.16 (pure methanol) to 27.12±0.32 (methanol+NaOH) — a much larger relative and absolute increase for methanol. [SRC-0094, Table 2]
- $\varepsilon'$ decreases with NaOH addition at most temperatures (e.g., ethanol 30 °C: 15.85±0.18 pure vs. 13.57±0.28 with NaOH at 915 MHz), attributed to ion solvation reducing the alcohol's own dipolar polarization rather than adding free dipoles. [SRC-0094, §3.3.1]
- For pure alcohols, $\varepsilon''$ vs. frequency shows a peak (ethanol peak near 1000 MHz at 30 °C; methanol peak 3000-4000 MHz at 30 °C); after NaOH addition, $\varepsilon''$ instead decreases monotonically and asymptotically with frequency, consistent with added ionic conduction dominating over dipolar relaxation. [SRC-0094, Fig. 2b-c, Fig. 4b-c]
- Loss tangent (tan $\delta$) at 915 MHz is higher for methanol-catalyst than ethanol-catalyst mixtures across temperatures (Table 2), and the paper notes higher loss tangent values generally yield higher microwave heating rates. [SRC-0094, §3.3.2, Table 2]

## Caveats

- Only one catalyst (NaOH) and one concentration regime (set by the biodiesel-relevant oil:alcohol:catalyst ratios used) were tested; the claim does not establish how the effect scales with catalyst identity or concentration beyond this regime. [SRC-0094, §2]
- The mechanism (ion solvation reducing $\varepsilon'$; ionic conduction raising $\varepsilon''$) is the authors' interpretation, supported by comparison to general electrolyte-solution theory (Hasted and Roderick, 1958) rather than by a separate mechanistic measurement in this paper. [SRC-0094, §3.3.1]
- Dielectric loss (and hence predicted microwave heating rate) is only one factor in actual reactor heating performance; the paper does not independently verify heating rate or reaction outcome from these dielectric measurements alone. [SRC-0094, §4]

## Links

- [[wiki/sources/SRC-0094-investigation-of-microwave-dielectric-properties-of-biodiesel-components]]
