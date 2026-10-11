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
  - dielectric-loss
  - hydrochloric-acid
  - ionic-strength
  - temperature-dependence
related:
  - "[[wiki/sources/SRC-0095-temperature-dependent-complex-dielectric-permittivity-a-simple-measurement]]"
sources:
  - SRC-0095
sensitivity: public
encryption: none
---

# Increasing HCl Concentration Reverses the Sign of the Dielectric Loss Factor's Temperature Dependence

## Claim

For pure water, the dielectric loss factor ($\varepsilon''$) decreases monotonically with increasing temperature. As HCl is added (decreasing pH from 7 toward 1), this temperature dependence weakens and then reverses: at pH 2 and below (pH 2.0, 1.6, 1.3, 1.0 in this dataset), $\varepsilon''$ instead increases with increasing temperature. HCl addition also monotonically raises $\varepsilon''$ at every fixed temperature, including room temperature. The dielectric constant ($\varepsilon'$) shows an analogous, weaker effect: its decrease with temperature becomes less steep as pH drops, and at pH 1 it reverses to an increase with temperature. The authors state that this ionic-strength-driven reversal of the temperature trend had not been previously reported. [SRC-0095, §"Dielectric permittivity of aqueous hydrochloric acid solutions"]

## Scope

Local to this single source's measured HCl concentration range (pH 7 [pure water] down to pH 1.0, discrete steps at pH 2.5, 2.0, 1.6, 1.3, 1.0) and temperature range (up to each solution's $T_{\mathrm{MAX}}$, 161.3-165.4 °C across the six solutions), measured near 2.45 GHz. The claim is specific to HCl and is not shown to generalize to other acids, bases, or salts. [SRC-0095, Methods, Table 3]

## Evidence

- Fig. 8b shows $\varepsilon''$ vs. temperature for water and five HCl concentrations: the water and weak-HCl (pH 2.5) curves decrease with temperature; pH 2.0 is roughly flat; pH 1.6, 1.3, and 1.0 curves increase with temperature. [SRC-0095, Fig. 8b]
- All six $\varepsilon''(T)$ datasets (water + 5 HCl concentrations) are fit by the same six-parameter lognormal form (Eq. 2) used for alcohols, with standard error <4% in every case (Table 3), indicating the reversal is a reproducible, well-fit trend rather than a single noisy outlier. [SRC-0095, Table 3]
- $\varepsilon'$ shows the weaker, same-direction effect: at pH 1 only, $\varepsilon'$ increases with temperature instead of decreasing (Fig. 8a); at room temperature, $\varepsilon'$ decreases slightly as pH is lowered. [SRC-0095, Fig. 8a]
- The paper explicitly flags this as a new observation: "This behavior in which ionic concentration changes the temperature effect on permittivity has not been previously reported to our knowledge." [SRC-0095, §"Dielectric permittivity of aqueous hydrochloric acid solutions"]

## Caveats

- No mechanistic explanation is given beyond the general statement that ionic concentration changes the temperature-permittivity relationship; the role of ionic conduction vs. ion-water structural effects is not separated out. [SRC-0095]
- The underlying raw per-temperature $\varepsilon'(T)$/$\varepsilon''(T)$ data points are not available in this PDF (no supplementary figure is even cited for this dataset in the main text); the claim rests on the plotted curves in Fig. 8 and the Table 3 fit parameters. [SRC-0095, Fig. 8, Table 3]
- The pH 2.5 loss-factor fit (Table 3) has markedly larger parameter magnitudes than any other row in the paper's fit tables; while its reported standard error is low (1.1%), this raises some question about fit robustness at the lower end of the tested HCl concentration range. [SRC-0095, Table 3]
- Pure water's own small-magnitude $\varepsilon''$ decrease (Table 3's "Water" row) sits at one end of a continuum rather than being a qualitatively distinct reference state; the claim describes a continuous trend across pH, not a sharp threshold effect, except insofar as pH 2.0 is the approximate crossover point in the reported data. [SRC-0095, Fig. 8b]

## Links

- [[wiki/sources/SRC-0095-temperature-dependent-complex-dielectric-permittivity-a-simple-measurement]]
