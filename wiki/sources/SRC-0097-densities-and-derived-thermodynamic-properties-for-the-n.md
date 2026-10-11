---
type: source
status: active
created: 2026-10-01
updated: 2026-10-01
source_id: SRC-0097
display_title: "Densities and Derived Thermodynamic Properties for the (n-Heptane + n-Octane), (n-Heptane + Ethanol) and (n-Octane + Ethanol) Systems at High Pressures"
short_title: "Abdussalam et al. High-Pressure Alkane/Ethanol Densities"
aliases:
  - "SRC-0097"
  - "Abdussalam et al. 2016"
  - "Densities and derived thermodynamic properties for the (n-heptane + n-octane), (n-heptane + ethanol) and (n-octane + ethanol) systems at high pressures"
source_path: raw/sources/SRC-0097-densities-and-derived-thermodynamic-properties-for-the-n.pdf
imported_path: raw/sources/SRC-0097-densities-and-derived-thermodynamic-properties-for-the-n.pdf
original_filename: "1-s2.0-S0021961416300428-main.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 6cac8714c0c2908a06b13a1cf809465b41c6fa641b40381058093840e2fa2f28
authors:
  - "Ali A. Abdussalam"
  - "Gorica R. Ivaniš"
  - "Ivona R. Radović"
  - "Mirjana Lj. Kijevčanin"
author_entities: []
year: 2016
venue: "Journal of Chemical Thermodynamics, 100, 89-99"
doi: "10.1016/j.jct.2016.04.014"
arxiv:
metadata_review_status: reviewed
areas:
  - research
categories:
  - research/experimental-benchmarking
tags:
  - scientific-paper
  - density
  - high-pressure
  - excess-molar-volume
  - isothermal-compressibility
  - isobaric-thermal-expansion-coefficient
  - tammann-tait-equation
  - equation-of-state
  - n-heptane
  - n-octane
  - ethanol
  - binary-mixtures
  - vibrating-tube-densimeter
related: []
sources:
  - SRC-0097
cites_sources: []
citation_match_status: reviewed
cqt_review_status: linked
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: math-standard
peer_review_status: peer-reviewed
---

# Densities and Derived Thermodynamic Properties for the (n-Heptane + n-Octane), (n-Heptane + Ethanol) and (n-Octane + Ethanol) Systems at High Pressures

Source ID: `SRC-0097`

## Raw source

- Repository path: `raw/sources/SRC-0097-densities-and-derived-thermodynamic-properties-for-the-n.pdf`
- Open raw source: [raw/sources/SRC-0097-densities-and-derived-thermodynamic-properties-for-the-n.pdf](../../raw/sources/SRC-0097-densities-and-derived-thermodynamic-properties-for-the-n.pdf)

## Summary

Abdussalam, Ivaniš, Radović and Kijevčanin (University of Belgrade) report experimental liquid densities for pure n-heptane, n-octane and ethanol at (288.15-413.15) K and (0.1-60) MPa, and for the three binary mixtures n-heptane + n-octane, n-heptane + ethanol and n-octane + ethanol (each at three mole fractions near 0.25/0.50/0.75) at (293.15-373.15) K and (0.1-40) MPa, using an Anton Paar DMA HP density cell coupled to a DMA 5000 vibrating-tube densimeter. [SRC-0097, Abstract, §2] Densities were fitted with a modified Tammann-Tait equation of state, and the fit was used to derive excess molar volumes, isothermal compressibilities and isobaric thermal expansion coefficients. [SRC-0097, Abstract, §3.2-3.3]

The pure-compound densities agree with multiple independent literature sources within 0.012-0.215% (absolute average percentage deviation, AAD) depending on the reference and liquid; the n-octane + ethanol system had not previously been measured at high pressure, so it is the paper's principal new dataset, while the n-heptane + ethanol and n-heptane + n-octane measurements extend the literature's temperature/pressure coverage. [SRC-0097, Introduction, §3.1] Both alcohol-containing mixtures show positive excess molar volumes, attributed to the disruption of ethanol's self-associated hydrogen-bonded network on mixing with the non-polar alkanes, while n-heptane + n-octane is close to ideal. [SRC-0097, §3.1, §3.3]

## Methods and evidence

Pure-compound and mixture densities were measured with an Anton Paar DMA HP high-pressure density cell coupled to an Anton Paar DMA 5000 vibrating-tube densimeter (oscillation-period method), the same apparatus described in the authors' earlier work. [SRC-0097, §2.2] Temperature was controlled by an integrated Peltier thermostat (stability ±0.05 K); pressure was set and controlled with a High Pressure Equipment Co. (HiP) model 50-6-15 generator using acetone as the hydraulic fluid and measured with a WIKA S-10 transducer. [SRC-0097, §2.2] The densimeter was calibrated using the procedure of Comuñas et al. [ref. 16], and a viscosity-induced density correction (<0.02 kg·m⁻³, from correspondence with the instrument manufacturer, Anton Paar) was applied. [SRC-0097, §2.2]

Densities were fitted to a modified Tammann-Tait equation of state (Eqs. 1-4) as a function of temperature and pressure, with fit quality assessed by the absolute average percentage deviation (AAD, Eq. 5) and the standard deviation $\sigma$ (Eq. 6). [SRC-0097, §3.2] From the fitted equation, the authors derive closed-form expressions for isothermal compressibility $\kappa_T$ (Eqs. 8-9) and isobaric thermal expansion coefficient $\alpha_p$ (Eqs. 10-14), and compute excess molar volume $V^E$ directly from measured mixture and pure-component densities (Eq. 7). [SRC-0097, §3.2-3.3]

Pure-compound densities (Table 3) are compared against multiple independent literature datasets using AAD and maximum percentage deviation (MxD) metrics (Fig. 1); binary-mixture densities (Tables 4-6) are compared, where literature data existed, via interpolation to the present temperatures/pressures (Fig. 2). No independent literature comparison exists for the newly measured n-octane + ethanol system density values themselves (only at atmospheric pressure, against two literature sources, see Limitations). [SRC-0097, §3.1]

## Key equations

Modified Tammann-Tait equation of state for density as a function of temperature $T$ and pressure $p$. [SRC-0097, Eq. 1]

$$
\rho(T,p) = \frac{\rho^{\text{ref}}(T)}{1 - C(T)\ln\!\left(\dfrac{B(T)+p}{B(T)+p^{\text{ref}}}\right)}
$$

Temperature-dependent parameters of Eq. 1, each a quadratic polynomial in $T$ with fitted coefficients $a_i$, $b_i$, $c_i$ ($i=0,1,2$). [SRC-0097, Eqs. 2-4]

$$
\rho^{\text{ref}}(T) = \sum_{i=0}^{2} a_i T^i
\qquad
B(T) = \sum_{i=0}^{2} b_i T^i
\qquad
C(T) = \sum_{i=0}^{2} c_i T^i
$$

Fit-quality metrics: absolute average percentage deviation (Eq. 5) and standard deviation (Eq. 6), where $\rho^{\exp}$ is the experimental density, $\rho^{\text{cal}}$ is the value from Eq. 1, $N$ is the number of experimental points and $m$ is the number of optimized parameters. [SRC-0097, Eqs. 5-6]

$$
AAD = \frac{100}{N}\sum_{i=1}^{N}\left|\frac{\rho_i^{\exp}-\rho_i^{\text{cal}}}{\rho_i^{\exp}}\right|
\qquad
\sigma = \sqrt{\frac{\sum_{i=1}^{N}(\rho_i^{\exp}-\rho_i^{\text{cal}})^2}{N-m}}
$$

Excess molar volume of a mixture, from measured mixture density $\rho$ and pure-component densities $\rho_i$. [SRC-0097, Eq. 7]

$$
V^E = \sum_{i=1}^{n} x_i M_i \left[\frac{1}{\rho} - \frac{1}{\rho_i}\right]
$$

Isothermal compressibility, defined thermodynamically (Eq. 8) and then obtained in closed form by substituting Eq. 1 (Eq. 9). [SRC-0097, Eqs. 8-9]

$$
\kappa_T = \frac{1}{\rho}\left(\frac{\partial \rho}{\partial p}\right)_T
\qquad\qquad
\kappa_T = \frac{C(T)}{(B(T)+p)\left(1 - C(T)\ln\dfrac{B(T)+p}{B(T)+p^{\text{ref}}}\right)}
$$

Isobaric thermal expansion coefficient, defined thermodynamically (Eq. 10) and then obtained in closed form by combining Eqs. 1 and 10 (Eq. 11), using the temperature derivatives $\rho^{\text{ref}\prime}(T)$, $B'(T)$, $C'(T)$ of $\rho^{\text{ref}}$, $B$, $C$ (Eqs. 12-14). [SRC-0097, Eqs. 10-14]

$$
\alpha_p = \frac{1}{\rho}\left(\frac{\partial p}{\partial T}\right)_\rho \left(\frac{\partial p}{\partial \rho}\right)_T^{-1} = -\frac{1}{\rho}\left(\frac{\partial \rho}{\partial T}\right)_p
$$

$$
\alpha_p = \frac{-\dfrac{\rho^{\text{ref}\prime}(T)}{\rho^{\text{ref}}(T)} - \dfrac{C(T)\,\dfrac{B'(T)(p^{\text{ref}}-p)}{(B(T)+p)(B(T)+p^{\text{ref}})} + C'(T)\ln\dfrac{B(T)+p}{B(T)+p^{\text{ref}}}}{1 - C(T)\ln\dfrac{B(T)+p}{B(T)+p^{\text{ref}}}}}{1}
$$

$$
\rho^{\text{ref}\prime} = \sum_{i=0}^{2} i\,a_i T^{i-1}
\qquad
B' = \sum_{i=0}^{2} i\,b_i T^{i-1}
\qquad
C' = \sum_{i=0}^{2} i\,c_i T^{i-1}
$$

### Variable glossary

- $\rho(T,p)$: density at temperature $T$, pressure $p$; $\rho^{\text{ref}}(T)$: density at the reference pressure $p^{\text{ref}}=0.1$ MPa.
- $B(T)$, $C(T)$: temperature-dependent Tammann-Tait parameters, each nominally $\sum_{i=0}^2 (\cdot)_i T^i$.
- $a_i$, $b_i$, $c_i$ ($i=0,1,2$): fitted polynomial coefficients for $\rho^{\text{ref}}$, $B$, $C$ respectively (tabulated in Tables 7-8). In this paper $C$ is treated as temperature-independent, so only $c_0$ is fitted/reported (no $c_1$, $c_2$); see Mathematical gaps.
- $AAD$: absolute average percentage deviation between experimental and correlated densities; $\sigma$: standard deviation of the fit; $N$: number of experimental data points; $m$: number of optimized parameters.
- $V^E$: excess molar volume of a mixture; $x_i$: mole fraction of component $i$; $M_i$: molecular weight of component $i$; $\rho$: measured mixture density; $\rho_i$: measured density of pure component $i$ at the same $T,p$.
- $\kappa_T$: isothermal compressibility; $\alpha_p$: isobaric thermal expansion coefficient.
- $\rho^{\text{ref}\prime}(T)$, $B'(T)$, $C'(T)$: first derivatives with respect to $T$ of $\rho^{\text{ref}}$, $B$, $C$.
- $MxD$: maximum percentage deviation between experimental and literature densities, used alongside AAD for literature comparisons (text only, not a numbered equation). [SRC-0097, §3.1]

### Equation inventory

| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |
| Modified Tammann-Tait EOS | SRC-0097, Eq. 1, p. 93 | This page | Correlates density with $T$ and $p$ from a reference-pressure density curve and two fitted parameters. | $\rho$, $\rho^{\text{ref}}$, $B$, $C$, $p$, $p^{\text{ref}}$ | Reconstructs $\rho(T,p)$ for the pure compounds (Table 7) or any tabulated mixture composition (Table 8) over the fitted $T,p$ range. |
| Quadratic-in-$T$ parameters | SRC-0097, Eqs. 2-4, p. 93 | This page | Defines $\rho^{\text{ref}}(T)$, $B(T)$, $C(T)$ from fitted coefficients. | $a_i$, $b_i$, $c_i$ | Supplies the three functions needed to evaluate Eq. 1; note $C(T)=c_0$ (constant) as actually fitted. |
| AAD / $\sigma$ fit metrics | SRC-0097, Eqs. 5-6, pp. 93-94 | This page | Quantifies agreement between fitted and experimental densities. | $\rho^{\exp}$, $\rho^{\text{cal}}$, $N$, $m$ | Reported per-compound/mixture in Tables 7-8; usable to judge whether the fit is adequate for a given reuse. |
| Excess molar volume | SRC-0097, Eq. 7, p. 95 | This page | Computes $V^E$ directly from measured densities (not from the EOS fit). | $x_i$, $M_i$, $\rho$, $\rho_i$ | Needed to reproduce Fig. 4 values; no $V^E$ numeric table is given in the main paper (see Known gaps). |
| Isothermal compressibility | SRC-0097, Eqs. 8-9, p. 95 | This page | Analytic $\kappa_T(T,p)$ from the EOS fit. | $\kappa_T$, $B(T)$, $C(T)$, $p$, $p^{\text{ref}}$ | Can be evaluated directly from Table 7/8 parameters without digitizing Figs. 5-7. |
| Isobaric thermal expansion coefficient | SRC-0097, Eqs. 10-14, p. 96 | This page | Analytic $\alpha_p(T,p)$ from the EOS fit and its $T$-derivatives. | $\alpha_p$, $\rho^{\text{ref}\prime}$, $B'$, $C'$, $p$, $p^{\text{ref}}$ | Can likewise be evaluated directly from Table 7/8 parameters; requires $a_i,b_i,c_i$ and their derivatives. |

### Mathematical gaps

- The paper states "In our case the parameter $C$ is treated as temperature independent" [SRC-0097, §3.2], yet Eq. 4 is printed in the same general quadratic form as Eqs. 2-3. Tables 7 and 8 confirm the practical consequence: only a single $c_0$ (labelled "$c_0$" in Table 7 and "$c$" in Table 8) is fitted and reported for each compound/mixture, with no $c_1$ or $c_2$ values given. This is recorded as a modeling simplification explicit in the text, not a transcription gap.
- Eq. 11 ($\alpha_p$) is reproduced here exactly as laid out in the source (a single fraction whose numerator is itself a fraction containing $\rho^{\text{ref}\prime}/\rho^{\text{ref}}$ and a second nested fraction, independently re-verified against a 300 dpi render of page 96); no simplification was applied.
- Tables S1-S4 (isothermal compressibility and isobaric thermal expansion coefficient of the pure compounds, and the same two derived properties tabulated numerically for the binary mixtures) are referenced in-text [SRC-0097, §3.3] as residing in the online Supplementary Information, which is not included in the ingested PDF; see Known gaps.

## Data tables

All eight numbered tables from the main paper are transcribed in full below. Tables 1, 2, 3, 4, 5 and 6 report measured values (chemicals/purity, pure-compound literature comparison, and full pure-compound/mixture density grids). Tables 7 and 8 report Tammann-Tait equation-of-state **fit parameters**, not directly measured quantities; use them with the model equations above. All values were independently re-verified a second time against 300 dpi renders of the original table pages (pp. 90-91-92-94-95-97 of the journal, PDF pages 2-4, 6-7, 9); no value was found illegible or anomalous, and the two renders agreed exactly with the first-pass extraction in every case.

### Measurement conditions (for reuse)

- Instrument: Anton Paar DMA HP high-pressure density-measuring cell coupled with an Anton Paar DMA 5000 vibrating-tube densimeter; the oscillation period $\tau$ of the U-tube was read to seven significant digits with a digital counter, transferred from DMA HP to DMA 5000 via S-BUS interfaces, and logged to a PC via the APSoft-Print Excel add-in. [SRC-0097, §2.2]
- Calibration: densimeter calibrated by the procedure of Comuñas et al. [ref. 16], detailed in the authors' earlier work [ref. 3]; the influence of sample viscosity on density was estimated from information obtained in personal correspondence with the instrument supplier (Anton Paar) and found to be <0.02 kg·m⁻³. [SRC-0097, §2.2]
- Temperature control: integrated Peltier thermostat, stability within ±0.05 K at each selected temperature. [SRC-0097, §2.2]
- Pressure control: pressure generator model 50-6-15 (High Pressure Equipment Co., HiP) with acetone as the hydraulic fluid [ref. 3]; pressure measured with a WIKA S-10 transducer (Alexander Wiegand GmbH & Co.). The maximum of the sum of deviation and expanded measurement uncertainty is ±0.1815% across the full pressure range. [SRC-0097, §2.2]
- Conditions studied: pure compounds at (288.15-413.15) K and (0.1-60) MPa; binary mixtures at (293.15-373.15) K and (0.1-40) MPa, at three mole fractions per system (approx. 0.25, 0.50, 0.75). [SRC-0097, §2.2, §3.1]
- Sample purity/preparation: n-heptane (Sigma-Aldrich, CAS 142-82-5, mass-fraction purity ≥0.99), n-octane (Merck, CAS 111-65-9, ≥0.99), ethanol (Merck, CAS 64-17-5, ≥0.999); used as received without further purification, degassed prior to measurement (Table 1). Mixtures prepared gravimetrically with a Mettler AG 204 balance (precision $1\times10^{-7}$ kg); mole-fraction uncertainty less than $\pm1\times10^{-4}$. [SRC-0097, §2.1, §2.2]
- Reported precision/uncertainty: expanded uncertainty with 0.95 level of confidence ($k=2$) in reported densities is $U(\rho)=1.7$ kg·m⁻³ for (288.15-363.15) K and $U(\rho)=2.7$ kg·m⁻³ for (373.15-413.15) K (Tables 3-6 footnote a); $U(T)=0.1$ K (Tables 3-6 footnote b); $U(p)=0.05$ MPa (Tables 3-6 footnote c); $U(x)=2\times10^{-4}$ for mixture mole fractions (Tables 4-6 footnote d). Table 2 (atmospheric-pressure comparison) instead reports $u(T)=0.01$ K and $u(p)=5\%$ as standard uncertainties and $U(\rho)=0.08$ kg·m⁻³ as an expanded (0.95) uncertainty — a different, tighter uncertainty budget than Tables 3-6, as printed. Excess molar volume was calculated with average uncertainty $\pm4\times10^{-6}$ m³·kmol⁻¹. [SRC-0097, §2.2, Table 2 footnotes, Tables 3-6 footnotes]

### Table 1 - Chemicals used in this work [SRC-0097, Table 1]

| Chemical name | CAS | Supplier | Purity mass fraction |
| --- | --- | --- | --- |
| n-Heptane | 142-82-5 | Sigma-Aldrich | ≥0.99 |
| n-Octane | 111-65-9 | Merck | ≥0.99 |
| Ethanol | 64-17-5 | Merck | ≥0.999 |

### Table 2 - Comparison of the measured and literature densities of the pure compounds at atmospheric pressure ($p^c=0.101$ MPa) [SRC-0097, Table 2]

Both density columns are printed in the source as "Exp."; the left is this work's measurement, the right is the literature value with its bracketed reference number(s). $u(T)=0.01$ K (standard uncertainty); $U(\rho)=0.08$ kg·m⁻³ (expanded, 0.95 confidence); $u(p)=5\%$ (standard uncertainty).

| Component | $T^a$/K | $\rho^b$/kg·m⁻³ — this work (Exp.) | $\rho^b$/kg·m⁻³ — literature (Exp.) [ref.] |
| --- | --- | --- | --- |
| n-Heptane | 288.15 | 688.33 | 687.92 [13] |
| n-Heptane | 293.15 | 684.11 | 683.9 [10]; 683.67 [13] |
| n-Heptane | 298.15 | 679.87 | 679.48 [13] |
| n-Heptane | 303.15 | 675.60 | 675.1 [10]; 675.15 [13] |
| n-Heptane | 308.15 | 671.31 | 670.86 [13] |
| n-Heptane | 313.15 | 667.00 | 666.4 [10]; 666.5 [13] |
| n-Octane | 293.15 | 702.58 | 702.56 [13]; 702.55 [14] |
| n-Octane | 303.15 | 694.48 | 694.48 [13]; 694.44 [14] |
| n-Octane | 313.15 | 686.32 | 686.29 [13]; 686.22 [14] |
| n-Octane | 323.15 | 678.09 | 678.00 [13]; 677.90 [14] |
| Ethanol | 303.15 | 780.83 | 781.1 [10], 780.9 [15] |
| Ethanol | 313.15 | 772.10 | 772.3 [10], 772.1 [15] |
| Ethanol | 323.15 | 763.22 | 763.1 [10], 763.3 [15] |

### Table 3 - Experimental densities of pure compounds at various pressures, $p$, and temperatures, $T$ [SRC-0097, Table 3]

$U(\rho)=1.7$ kg·m⁻³ (288.15 K ≤ T ≤ 363.15 K) and $2.7$ kg·m⁻³ (373.15 K ≤ T ≤ 413.15 K); $U(T)=0.1$ K; $U(p)=0.05$ MPa (all expanded, 0.95 confidence). Blank cells mean no value is reported at that $p,T$ combination (consistent with the liquid being above its normal boiling point at 0.1 MPa and that temperature; this inference is synthesis, not stated in the source).

**n-Heptane, $\rho$/kg·m⁻³, $T$/K = 288.15-323.15**

| $p$/MPa | 288.15 | 293.15 | 298.15 | 303.15 | 308.15 | 313.15 | 318.15 | 323.15 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.1 | 688.4 | 684.2 | 679.9 | 675.7 | 671.4 | 667.1 | 662.7 | 658.3 |
| 1 | 689.2 | 685.0 | 680.7 | 676.5 | 672.2 | 668.0 | 663.6 | 659.3 |
| 5 | 692.5 | 688.4 | 684.3 | 680.2 | 676.0 | 672.0 | 667.7 | 663.5 |
| 10 | 696.5 | 692.6 | 688.6 | 684.6 | 680.6 | 676.7 | 672.6 | 668.6 |
| 15 | 700.4 | 696.5 | 692.7 | 688.9 | 685.0 | 681.2 | 677.3 | 673.4 |
| 20 | 704.1 | 700.4 | 696.6 | 693.0 | 689.2 | 685.5 | 681.8 | 678.0 |
| 25 | 707.7 | 704.0 | 700.4 | 696.8 | 693.2 | 689.6 | 686.0 | 682.4 |
| 30 | 711.1 | 707.5 | 704.0 | 700.5 | 697.0 | 693.5 | 690.0 | 686.5 |
| 35 | 714.3 | 710.9 | 707.4 | 704.0 | 700.6 | 697.2 | 693.8 | 690.4 |
| 40 | 717.4 | 714.0 | 710.7 | 707.4 | 704.0 | 700.7 | 697.4 | 694.1 |
| 45 | 720.3 | 717.0 | 713.8 | 710.5 | 707.2 | 704.0 | 700.7 | 697.5 |
| 50 | 723.1 | 719.9 | 716.7 | 713.5 | 710.3 | 707.1 | 703.9 | 700.7 |
| 55 | 725.8 | 722.5 | 719.4 | 716.2 | 713.1 | 709.9 | 706.8 | 703.7 |
| 60 | 728.2 | 725.1 | 721.9 | 718.8 | 715.7 | 712.6 | 709.5 | 706.4 |

**n-Heptane, $\rho$/kg·m⁻³, $T$/K = 328.15-413.15**

| $p$/MPa | 328.15 | 333.15 | 343.15 | 353.15 | 363.15 | 373.15 | 393.15 | 413.15 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.1 | 653.9 | 649.5 | 640.5 | 631.3 | 621.9 | | | |
| 1 | 654.9 | 650.6 | 641.6 | 632.5 | 623.2 | 614.2 | 594.6 | 574.1 |
| 5 | 659.3 | 655.1 | 646.5 | 637.8 | 628.9 | 620.2 | 601.7 | 582.3 |
| 10 | 664.5 | 660.5 | 652.3 | 644.0 | 635.6 | 627.4 | 610.0 | 592.0 |
| 15 | 669.5 | 665.7 | 657.8 | 649.9 | 641.9 | 634.1 | 617.8 | 600.9 |
| 20 | 674.3 | 670.6 | 663.1 | 655.5 | 647.9 | 640.4 | 625.0 | 609.2 |
| 25 | 678.8 | 675.2 | 668.0 | 660.7 | 653.4 | 646.3 | 631.7 | 616.9 |
| 30 | 683.0 | 679.6 | 672.6 | 665.6 | 658.6 | 651.8 | 637.9 | 623.9 |
| 35 | 687.0 | 683.7 | 676.9 | 670.2 | 663.5 | 656.9 | 643.6 | 630.2 |
| 40 | 690.8 | 687.5 | 681.0 | 674.4 | 667.9 | 661.5 | 648.7 | 635.9 |
| 45 | 694.3 | 691.1 | 684.7 | 678.3 | 672.0 | 665.8 | 653.3 | 640.9 |
| 50 | 697.6 | 694.4 | 688.1 | 681.9 | 675.7 | 669.6 | 657.4 | 645.2 |
| 55 | 700.6 | 697.4 | 691.3 | 685.1 | 679.0 | 673.1 | 660.9 | 648.9 |
| 60 | 703.3 | 700.2 | 694.1 | 688.0 | 681.9 | 676.1 | 663.9 | 651.9 |

**n-Octane, $\rho$/kg·m⁻³, $T$/K = 288.15-323.15**

| $p$/MPa | 288.15 | 293.15 | 298.15 | 303.15 | 308.15 | 313.15 | 318.15 | 323.15 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.1 | 706.5 | 702.5 | 698.5 | 694.4 | 690.4 | 686.3 | 682.2 | 678.0 |
| 1 | 707.2 | 703.2 | 699.2 | 695.2 | 691.2 | 687.1 | 683.0 | 678.9 |
| 5 | 710.3 | 706.4 | 702.5 | 698.6 | 694.7 | 690.8 | 686.8 | 682.8 |
| 10 | 714.1 | 710.3 | 706.5 | 702.7 | 698.9 | 695.1 | 691.3 | 687.4 |
| 15 | 717.7 | 714.0 | 710.3 | 706.7 | 703.0 | 699.3 | 695.6 | 691.9 |
| 20 | 721.2 | 717.6 | 714.0 | 710.5 | 706.9 | 703.3 | 699.7 | 696.1 |
| 25 | 724.5 | 721.0 | 717.6 | 714.1 | 710.6 | 707.2 | 703.6 | 700.2 |
| 30 | 727.7 | 724.3 | 720.9 | 717.5 | 714.2 | 710.8 | 707.4 | 704.0 |
| 35 | 730.8 | 727.5 | 724.1 | 720.9 | 717.5 | 714.3 | 711.0 | 707.7 |
| 40 | 733.7 | 730.5 | 727.2 | 724.0 | 720.8 | 717.6 | 714.3 | 711.1 |
| 45 | 736.5 | 733.3 | 730.1 | 727.0 | 723.8 | 720.7 | 717.5 | 714.4 |
| 50 | 739.2 | 736.0 | 732.9 | 729.8 | 726.7 | 723.6 | 720.5 | 717.4 |
| 55 | 741.7 | 738.6 | 735.5 | 732.5 | 729.4 | 726.3 | 723.3 | 720.3 |
| 60 | 744.1 | 741.0 | 738.0 | 735.0 | 731.9 | 728.9 | 725.9 | 722.9 |

**n-Octane, $\rho$/kg·m⁻³, $T$/K = 328.15-413.15**

| $p$/MPa | 328.15 | 333.15 | 343.15 | 353.15 | 363.15 | 373.15 | 393.15 | 413.15 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.1 | 673.8 | 669.7 | 661.2 | 652.6 | 643.8 | 634.7 | 616.3 | |
| 1 | 674.7 | 670.6 | 662.2 | 653.7 | 645.0 | 636.3 | 618.1 | 599.3 |
| 5 | 678.7 | 674.8 | 666.6 | 658.4 | 650.1 | 641.8 | 624.3 | 606.6 |
| 10 | 683.5 | 679.7 | 671.9 | 664.1 | 656.1 | 648.2 | 631.8 | 615.1 |
| 15 | 688.1 | 684.5 | 677.0 | 669.4 | 661.9 | 654.4 | 638.8 | 623.1 |
| 20 | 692.5 | 689.0 | 681.8 | 674.5 | 667.3 | 660.1 | 645.3 | 630.6 |
| 25 | 696.7 | 693.2 | 686.3 | 679.3 | 672.4 | 665.5 | 651.5 | 637.4 |
| 30 | 700.7 | 697.3 | 690.6 | 683.9 | 677.2 | 670.6 | 657.1 | 643.8 |
| 35 | 704.4 | 701.1 | 694.6 | 688.1 | 681.6 | 675.3 | 662.3 | 649.6 |
| 40 | 707.9 | 704.7 | 698.4 | 692.1 | 685.8 | 679.6 | 667.1 | 654.8 |
| 45 | 711.3 | 708.1 | 701.9 | 695.7 | 689.6 | 683.6 | 671.4 | 659.5 |
| 50 | 714.4 | 711.3 | 705.2 | 699.1 | 693.1 | 687.3 | 675.3 | 663.6 |
| 55 | 717.3 | 714.2 | 708.2 | 702.3 | 696.3 | 690.5 | 678.8 | 667.2 |
| 60 | 719.9 | 716.9 | 711.0 | 705.1 | 699.2 | 693.5 | 681.8 | 670.2 |

**Ethanol, $\rho$/kg·m⁻³, $T$/K = 288.15-323.15**

| $p$/MPa | 288.15 | 293.15 | 298.15 | 303.15 | 308.15 | 313.15 | 318.15 | 323.15 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.1 | 793.7 | 789.4 | 785.2 | 780.9 | 776.5 | 772.1 | 767.7 | 763.2 |
| 1 | 794.4 | 790.2 | 785.9 | 781.6 | 777.3 | 773.0 | 768.5 | 764.1 |
| 5 | 797.6 | 793.5 | 789.3 | 785.1 | 780.9 | 776.6 | 772.3 | 768.0 |
| 10 | 801.5 | 797.4 | 793.4 | 789.3 | 785.2 | 781.0 | 776.8 | 772.6 |
| 15 | 805.3 | 801.3 | 797.3 | 793.3 | 789.3 | 785.3 | 781.2 | 777.1 |
| 20 | 808.9 | 805.0 | 801.1 | 797.2 | 793.3 | 789.4 | 785.4 | 781.4 |
| 25 | 812.4 | 808.6 | 804.8 | 801.0 | 797.1 | 793.3 | 789.4 | 785.5 |
| 30 | 815.7 | 812.0 | 808.3 | 804.6 | 800.8 | 797.0 | 793.2 | 789.4 |
| 35 | 819.0 | 815.3 | 811.7 | 808.0 | 804.3 | 800.6 | 796.9 | 793.2 |
| 40 | 822.1 | 818.5 | 814.9 | 811.3 | 807.7 | 804.1 | 800.4 | 796.8 |
| 45 | 825.1 | 821.5 | 818.0 | 814.5 | 810.9 | 807.4 | 803.8 | 800.2 |
| 50 | 828.0 | 824.5 | 821.0 | 817.5 | 814.0 | 810.5 | 806.9 | 803.4 |
| 55 | 830.7 | 827.2 | 823.8 | 820.3 | 816.9 | 813.4 | 809.9 | 806.5 |
| 60 | 833.3 | 829.9 | 826.5 | 823.1 | 819.6 | 816.2 | 812.8 | 809.3 |

**Ethanol, $\rho$/kg·m⁻³, $T$/K = 328.15-413.15**

| $p$/MPa | 328.15 | 333.15 | 343.15 | 353.15 | 363.15 | 373.15 | 393.15 | 413.15 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.1 | 758.7 | 754.1 | 744.6 | | | | | |
| 1 | 759.6 | 755.0 | 745.6 | 736.0 | 725.9 | 715.3 | 692.2 | 666.3 |
| 5 | 763.6 | 759.1 | 750.0 | 740.6 | 730.8 | 720.6 | 698.4 | 673.6 |
| 10 | 768.3 | 764.0 | 755.2 | 746.2 | 736.7 | 727.0 | 705.8 | 682.3 |
| 15 | 772.9 | 768.8 | 760.2 | 751.5 | 742.4 | 733.0 | 712.8 | 690.5 |
| 20 | 777.3 | 773.3 | 765.0 | 756.5 | 747.7 | 738.7 | 719.4 | 698.1 |
| 25 | 781.6 | 777.6 | 769.6 | 761.3 | 752.8 | 744.2 | 725.6 | 705.3 |
| 30 | 785.6 | 781.7 | 773.9 | 765.9 | 757.7 | 749.3 | 731.4 | 712.0 |
| 35 | 789.5 | 785.7 | 778.0 | 770.2 | 762.2 | 754.1 | 736.8 | 718.2 |
| 40 | 793.1 | 789.4 | 781.9 | 774.3 | 766.5 | 758.6 | 741.8 | 723.8 |
| 45 | 796.6 | 792.9 | 785.6 | 778.1 | 770.5 | 762.8 | 746.4 | 729.0 |
| 50 | 799.9 | 796.3 | 789.1 | 781.7 | 774.3 | 766.7 | 750.7 | 733.7 |
| 55 | 803.0 | 799.4 | 792.3 | 785.1 | 777.7 | 770.2 | 754.5 | 737.9 |
| 60 | 805.9 | 802.4 | 795.3 | 788.2 | 780.9 | 773.5 | 757.9 | 741.5 |

### Table 4 - Experimental densities, $\rho$, for the binary mixture n-heptane (1) + n-octane (2) for different mole fractions, $x$, at pressure, $p$, and temperature, $T$ [SRC-0097, Table 4]

$U(\rho)=1.7$ kg·m⁻³ (288.15-363.15 K), $2.7$ kg·m⁻³ (373.15-413.15 K); $U(T)=0.1$ K; $U(p)=0.05$ MPa; $U(x)=2\times10^{-4}$ (all expanded, 0.95 confidence).

**$x_1 = 0.2500$**

| $p$/MPa | 293.15 | 303.15 | 313.15 | 323.15 | 333.15 | 353.15 | 373.15 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.1 | 698.22 [sic] | 690.1 | 681.8 | 673.4 | 664.9 | 647.5 | |
| 0.5 | 698.6 | 690.4 | 682.2 | 673.8 | 665.4 | 648.1 | 630.3 |
| 5 | 702.4 | 694.5 | 686.5 | 678.5 | 670.4 | 653.9 | 637.1 |
| 10 | 706.4 | 698.8 | 691.1 | 683.4 | 675.6 | 659.9 | 644.1 |
| 15 | 710.2 | 702.8 | 695.4 | 687.9 | 680.4 | 665.4 | 650.3 |
| 20 | 713.8 | 706.6 | 699.4 | 692.1 | 684.9 | 670.5 | 656.0 |
| 25 | 717.2 | 710.2 | 703.2 | 696.1 | 689.2 | 675.2 | 661.2 |
| 30 | 720.4 | 713.6 | 706.8 | 699.9 | 693.2 | 679.6 | 666.1 |
| 35 | 723.6 | 716.9 | 710.2 | 703.6 | 696.9 | 683.7 | 670.7 |
| 40 | 726.6 | 720.1 | 713.5 | 707.0 | 700.6 | 687.7 | 675.1 |

`[sic]` note: the value at $x_1=0.2500$, 0.1 MPa, 293.15 K is printed as "698.22", with two decimals where every other density in Tables 3-6 has one. It is transcribed as printed. It is most likely a typesetting slip for 698.2, which is consistent with the 0.5 MPa value of 698.6, but this cannot be confirmed from the paper.

**$x_1 = 0.5002$**

| $p$/MPa | 293.15 | 303.15 | 313.15 | 323.15 | 333.15 | 353.15 | 373.15 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.1 | 693.9 | 685.6 | 677.3 | 668.7 | 660.2 | 642.5 | |
| 0.5 | 694.3 | 686.0 | 677.7 | 669.2 | 660.6 | 643.1 | 625.0 |
| 5 | 698.1 | 690.2 | 682.1 | 674.0 | 665.8 | 649.1 | 632.0 |
| 10 | 702.2 | 694.5 | 686.8 | 678.9 | 671.1 | 655.2 | 639.2 |
| 15 | 706.0 | 698.6 | 691.1 | 683.6 | 676.0 | 660.8 | 645.6 |
| 20 | 709.7 | 702.5 | 695.2 | 687.9 | 680.6 | 666.0 | 651.4 |
| 25 | 713.2 | 706.1 | 699.1 | 692.0 | 684.9 | 670.8 | 656.7 |
| 30 | 716.5 | 709.6 | 702.7 | 695.8 | 689.0 | 675.3 | 661.7 |
| 35 | 719.6 | 712.9 | 706.2 | 699.5 | 692.8 | 679.5 | 666.3 |
| 40 | 722.7 | 716.1 | 709.6 | 703.0 | 696.5 | 683.6 | 670.8 |

**$x_1 = 0.7502$**

| $p$/MPa | 293.15 | 303.15 | 313.15 | 323.15 | 333.15 | 353.15 | 373.15 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.1 | 689.0 | 680.7 | 672.2 | 663.5 | 654.8 | 636.9 | |
| 0.5 | 689.4 | 681.0 | 672.6 | 664.0 | 655.3 | 637.4 | 619.0 |
| 5 | 693.4 | 685.3 | 677.2 | 668.9 | 660.6 | 643.6 | 626.3 |
| 10 | 697.5 | 689.7 | 681.9 | 674.0 | 666.0 | 649.9 | 633.6 |
| 15 | 701.4 | 693.9 | 686.3 | 678.7 | 671.1 | 655.7 | 640.2 |
| 20 | 705.1 | 697.8 | 690.5 | 683.1 | 675.8 | 661.0 | 646.2 |
| 25 | 708.7 | 701.6 | 694.4 | 687.3 | 680.2 | 665.9 | 651.7 |
| 30 | 712.0 | 705.1 | 698.1 | 691.2 | 684.3 | 670.4 | 656.7 |
| 35 | 715.2 | 708.5 | 701.7 | 694.9 | 688.2 | 674.7 | 661.5 |
| 40 | 718.4 | 711.7 | 705.1 | 698.5 | 692.0 | 678.9 | 666.0 |

### Table 5 - Experimental densities, $\rho$, for the binary mixture n-heptane (1) + ethanol (2) for different mole fractions, $x$, at pressure, $p$, and temperature, $T$ [SRC-0097, Table 5]

Same uncertainty footnotes as Table 4.

**$x_1 = 0.2505$**

| $p$/MPa | 293.15 | 303.15 | 313.15 | 323.15 | 333.15 | 353.15 | 373.15 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.1 | 737.7 | 728.9 | 719.9 | 710.6 | 701.1 | | |
| 0.5 | 738.1 | 729.3 | 720.3 | 711.1 | 701.6 | 681.4 | 659.3 |
| 5 | 742.1 | 733.6 | 725.0 | 716.1 | 706.9 | 687.7 | 666.9 |
| 10 | 746.4 | 738.2 | 729.8 | 721.2 | 712.5 | 694.1 | 674.5 |
| 15 | 750.4 | 742.4 | 734.3 | 726.1 | 717.6 | 700.0 | 681.4 |
| 20 | 754.3 | 746.5 | 738.6 | 730.6 | 722.4 | 705.5 | 687.6 |
| 25 | 757.9 | 750.3 | 742.6 | 734.8 | 726.9 | 710.5 | 693.3 |
| 30 | 761.4 | 754.0 | 746.5 | 738.9 | 731.2 | 715.3 | 698.6 |
| 35 | 764.7 | 757.5 | 750.1 | 742.7 | 735.2 | 719.7 | 703.6 |
| 40 | 768.0 | 760.8 | 753.7 | 746.4 | 739.1 | 724.0 | 708.4 |

**$x_1 = 0.5004$**

| $p$/MPa | 293.15 | 303.15 | 313.15 | 323.15 | 333.15 | 353.15 | 373.15 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.1 | 711.0 | 702.1 | 693.0 | 683.6 | 674.0 | | |
| 0.5 | 711.3 | 702.5 | 693.4 | 684.1 | 674.5 | 654.2 | 632.2 |
| 5 | 715.4 | 706.9 | 698.2 | 689.2 | 680.0 | 660.8 | 640.2 |
| 10 | 719.8 | 711.5 | 703.1 | 694.5 | 685.7 | 667.5 | 648.1 |
| 15 | 723.8 | 715.8 | 707.7 | 699.4 | 691.0 | 673.6 | 655.3 |
| 20 | 727.7 | 719.9 | 712.0 | 704.0 | 695.9 | 679.1 | 661.7 |
| 25 | 731.3 | 723.8 | 716.1 | 708.4 | 700.5 | 684.3 | 667.5 |
| 30 | 734.8 | 727.4 | 720.0 | 712.4 | 704.8 | 689.1 | 672.9 |
| 35 | 738.1 | 730.9 | 723.7 | 716.3 | 708.9 | 693.7 | 678.0 |
| 40 | 741.4 | 734.3 | 727.2 | 720.1 | 712.8 | 698.1 | 682.9 |

**$x_1 = 0.7501$**

| $p$/MPa | 293.15 | 303.15 | 313.15 | 323.15 | 333.15 | 353.15 | 373.15 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.1 | 694.3 | 685.4 | 676.4 | 667.2 | 657.7 | | |
| 0.5 | 694.6 | 685.8 | 676.9 | 667.6 | 658.2 | 638.4 | 617.2 |
| 5 | 698.7 | 690.3 | 681.6 | 672.8 | 663.8 | 645.1 | 625.3 |
| 10 | 703.0 | 694.9 | 686.6 | 678.1 | 669.6 | 651.8 | 633.3 |
| 15 | 707.1 | 699.2 | 691.2 | 683.0 | 674.9 | 657.9 | 640.4 |
| 20 | 710.9 | 703.3 | 695.5 | 687.7 | 679.8 | 663.5 | 646.8 |
| 25 | 714.6 | 707.1 | 699.6 | 692.0 | 684.3 | 668.6 | 652.6 |
| 30 | 718.0 | 710.8 | 703.4 | 696.0 | 688.6 | 673.4 | 658.0 |
| 35 | 721.4 | 714.3 | 707.1 | 699.9 | 692.7 | 678.0 | 663.0 |
| 40 | 724.6 | 717.6 | 710.6 | 703.6 | 696.6 | 682.3 | 667.9 |

### Table 6 - Experimental densities, $\rho$, for the binary mixture n-octane (1) + ethanol (2) for different mole fractions, $x$, at pressure, $p$, and temperature, $T$ [SRC-0097, Table 6]

Same uncertainty footnotes as Table 4.

**$x_1 = 0.2492$**

| $p$/MPa | 293.15 | 303.15 | 313.15 | 323.15 | 333.15 | 353.15 | 373.15 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.1 | 743.9 | 735.3 | 726.5 | 717.4 | 708.2 | | |
| 0.5 | 744.3 | 735.7 | 726.9 | 717.9 | 708.6 | 689.0 | 667.6 |
| 5 | 748.2 | 739.8 | 731.3 | 722.6 | 713.7 | 695.0 | 674.8 |
| 10 | 752.3 | 744.2 | 736.0 | 727.6 | 719.1 | 701.1 | 682.0 |
| 15 | 756.2 | 748.3 | 740.4 | 732.2 | 724.0 | 706.8 | 688.6 |
| 20 | 759.9 | 752.2 | 744.5 | 736.6 | 728.6 | 712.0 | 694.6 |
| 25 | 763.4 | 755.9 | 748.4 | 740.7 | 733.0 | 716.9 | 700.1 |
| 30 | 766.8 | 759.5 | 752.1 | 744.6 | 737.1 | 721.5 | 705.2 |
| 35 | 770.0 | 762.9 | 755.7 | 748.4 | 741.0 | 725.8 | 710.0 |
| 40 | 773.2 | 766.2 | 759.1 | 752.0 | 744.8 | 730.0 | 714.6 |

**$x_1 = 0.4999$**

| $p$/MPa | 293.15 | 303.15 | 313.15 | 323.15 | 333.15 | 353.15 | 373.15 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.1 | 722.3 | 713.7 | 705.0 | 696.0 | 686.8 | | |
| 0.5 | 722.6 | 714.1 | 705.4 | 696.4 | 687.3 | 667.9 | 647.2 |
| 5 | 726.5 | 718.3 | 709.8 | 701.2 | 692.4 | 674.0 | 654.4 |
| 10 | 730.6 | 722.6 | 714.5 | 706.1 | 697.7 | 680.2 | 661.7 |
| 15 | 734.4 | 726.7 | 718.8 | 710.8 | 702.7 | 685.8 | 668.3 |
| 20 | 738.1 | 730.6 | 722.9 | 715.1 | 707.3 | 691.1 | 674.3 |
| 25 | 741.6 | 734.2 | 726.8 | 719.2 | 711.6 | 695.9 | 679.8 |
| 30 | 744.9 | 737.7 | 730.5 | 723.1 | 715.7 | 700.5 | 684.9 |
| 35 | 748.1 | 741.1 | 734.0 | 726.8 | 719.6 | 704.8 | 689.7 |
| 40 | 751.2 | 744.3 | 737.4 | 730.4 | 723.4 | 709.0 | 694.3 |

**$x_1 = 0.7503$**

| $p$/MPa | 293.15 | 303.15 | 313.15 | 323.15 | 333.15 | 353.15 | 373.15 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.1 | 709.6 | 701.2 | 692.6 | 683.8 | 674.8 | | |
| 0.5 | 709.9 | 701.5 | 693.0 | 684.2 | 675.3 | 656.6 | 637.0 |
| 5 | 713.7 | 705.6 | 697.4 | 688.9 | 680.4 | 662.6 | 644.1 |
| 10 | 717.7 | 709.9 | 702.0 | 693.8 | 685.6 | 668.7 | 651.2 |
| 15 | 721.5 | 713.9 | 706.3 | 698.4 | 690.5 | 674.3 | 657.7 |
| 20 | 725.1 | 717.8 | 710.3 | 702.7 | 695.1 | 679.5 | 663.6 |
| 25 | 728.6 | 721.4 | 714.1 | 706.8 | 699.3 | 684.3 | 669.0 |
| 30 | 731.9 | 724.9 | 717.8 | 710.6 | 703.4 | 688.7 | 674.0 |
| 35 | 735.0 | 728.2 | 721.2 | 714.2 | 707.2 | 693.0 | 678.7 |
| 40 | 738.1 | 731.4 | 724.6 | 717.8 | 710.9 | 697.1 | 683.2 |

### Table 7 - Adjusted parameters of Eqs. (1)-(4), standard deviation $\sigma$, and average percentage deviation AAD, for the pure compounds [SRC-0097, Table 7]

**Tammann-Tait equation-of-state fit parameters** (not directly measured values); use with Eqs. 1-6 above. $C(T)$ is fitted as the single constant $c_0$ (no $c_1$, $c_2$).

| Parameter | n-Heptane | n-Octane | Ethanol |
| --- | --- | --- | --- |
| $a_0$/kg·m⁻³ | 871.86 | 875.98 | 952.55 |
| $a_1$/kg·m⁻³·K⁻¹ | −0.44006 | −0.39170 | −0.26716 |
| $a_2$/kg·m⁻³·K⁻² | $-6.8295\times10^{-4}$ | $-6.8294\times10^{-4}$ | $-9.8674\times10^{-4}$ |
| $b_0$/MPa | 364.98 | 376.90 | 521.31 |
| $b_1$/MPa·K⁻¹ | −1.4465 | −1.4388 | −2.0143 |
| $b_2$/MPa·K⁻² | $1.4864\times10^{-3}$ | $1.4222\times10^{-3}$ | $2.1155\times10^{-3}$ |
| $c_0$ | 0.090856 | 0.091360 | 0.11571 |
| $\sigma$/kg·m⁻³ | 0.464 | 0.343 | 1.143 |
| AAD/% | 0.044 | 0.032 | 0.075 |

### Table 8 - Adjusted parameters of Eqs. (1)-(4), standard deviation $\sigma$, and average percentage deviation AAD, for the binary mixtures [SRC-0097, Table 8]

**Tammann-Tait equation-of-state fit parameters** (not directly measured values); use with Eqs. 1-6 above. $C(T)$ is fitted as the single constant $c$ per mixture composition.

| Parameter | n-Hept.(1)+n-Oct., $x_1$=0.2500 | $x_1$=0.5002 | $x_1$=0.7502 | n-Hept.(1)+EtOH, $x_1$=0.2505 | $x_1$=0.5004 | $x_1$=0.7501 | n-Oct.(1)+EtOH, $x_1$=0.2492 | $x_1$=0.4999 | $x_1$=0.7503 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $a_0$/kg·m⁻³ | 886.86 | 881.92 | 874.49 | 858.601 | 835.52 | 837.22 | 868.53 | 853.178 | 859.71 |
| $a_1$/kg·m⁻³·K⁻¹ | −0.47668 | −0.46306 | −0.43618 | 0.031042 | 0.015346 | −0.11263 | −0.012068 | −0.057854 | −0.19781 |
| $a_2$/kg·m⁻³·K⁻² | $-5.6905\times10^{-4}$ | $-6.0833\times10^{-4}$ | $-6.7036\times10^{-4}$ | $-1.5131\times10^{-3}$ | $-1.5024\times10^{-3}$ | $-1.2798\times10^{-3}$ | $-1.4095\times10^{-3}$ | $-1.3262\times10^{-3}$ | $-1.0726\times10^{-3}$ |
| $b_0$/MPa | 330.45 | 342.71 | 343.22 | 366.94 | 362.02 | 353.74 | 361.14 | 361.06 | 336.83 |
| $b_1$/MPa·K⁻¹ | −1.2758 | −1.3482 | −1.359 | −1.4233 | −1.4373 | −1.4117 | −1.3741 | −1.4022 | −1.2815 |
| $b_2$/MPa·K⁻² | $1.2751\times10^{-3}$ | $1.3768\times10^{-3}$ | $1.3930\times10^{-3}$ | $1.4250\times10^{-3}$ | $1.4653\times10^{-3}$ | $1.4457\times10^{-3}$ | $1.3480\times10^{-3}$ | $1.4003\times10^{-3}$ | $1.2440\times10^{-3}$ |
| $c$ | 0.082865 | 0.084243 | 0.085089 | 0.089459 | 0.0875 | 0.086668 | 0.088070 | 0.085702 | 0.084095 |
| $\sigma$/kg·m⁻³ | 0.202 | 0.206 | 0.210 | 0.304 | 0.278 | 0.266 | 0.281 | 0.237 | 0.214 |
| AAD/% | 0.012 | 0.012 | 0.014 | 0.022 | 0.020 | 0.019 | 0.020 | 0.017 | 0.014 |

### Figures with data not captured in the tables

- Fig. 1 (a-d): measured-vs-literature percentage density deviation ($100\cdot(\rho^{\text{cal}}/\rho^{\exp}-1)$) vs. pressure for n-heptane (two panels, against different literature sets), n-octane, and ethanol, each against several named literature datasets; underlying per-point deviations are not tabulated beyond the AAD/MxD summary values quoted in the running text (§3.1). [SRC-0097, Fig. 1]
- Fig. 2 (a-c): measured-vs-literature percentage density deviation vs. mole fraction $x_1$ for the three binary systems, against literature data available only at atmospheric pressure for certain temperatures; not tabulated beyond the AAD values quoted in §3.1. [SRC-0097, Fig. 2]
- Fig. 3 (a-c): experimental density vs. mole fraction $x_1$ for the three binary systems at 5 MPa and 35 MPa, for isotherms 293.15 K, 313.15 K and 353.15 K; the same underlying density values are a subset of Tables 4-6 at those specific $(p,T)$ combinations, shown here only graphically for visual trend comparison. [SRC-0097, Fig. 3]
- Fig. 4 (a,b): excess molar volume $V^E$ vs. pressure for the equimolar n-heptane+ethanol and n-octane+ethanol mixtures, at seven isotherms (293.15 to 373.15 K); $V^E$ values themselves are not given as a numeric table in the main paper (only the defining Eq. 7 and this figure), so cannot be read off exactly without digitizing the plot. [SRC-0097, Fig. 4]
- Fig. 5, 6, 7 (a,b each): isothermal compressibility $\kappa_T$ and isobaric thermal expansion coefficient $\alpha_p$ vs. mole fraction $x_1$, at 293.15 K and 323.15 K, for four isobars (0.1, 10, 25, 40 MPa), for the n-heptane+n-octane, n-heptane+ethanol, and n-octane+ethanol systems respectively; the underlying numeric values are stated to reside in Supplementary Tables S3 ($\kappa_T$) and S4 ($\alpha_p$), not included in this PDF (see Known gaps). [SRC-0097, Figs. 5-7]

## Limitations and caveats

- Binary-mixture measurements span a narrower range — (293.15-373.15) K and (0.1-40) MPa — than the pure-compound measurements, (288.15-413.15) K and (0.1-60) MPa. [SRC-0097, §2.2]
- No independent literature density comparison is reported for the n-octane + ethanol system beyond two atmospheric-pressure interpolated comparisons (Estrada-Baltazar et al., AAD=0.080%; Orge et al., AAD=0.053%, both at 293.15-323.15 K); this is explicitly the system "that has not been analyzed in the literature" at high pressure, so most of Table 6 has no independent cross-check in this paper. [SRC-0097, Introduction, §3.1]
- The paper's own stated model simplification — treating $C(T)$ as temperature-independent (a single constant per compound/mixture, Tables 7-8) rather than the general quadratic form implied by Eq. 4 — narrows the EOS's flexibility relative to what Eqs. 1-4 suggest at face value; see Mathematical gaps. [SRC-0097, §3.2]
- Excess molar volume, isothermal compressibility and isobaric thermal expansion coefficient are presented in the main paper only as defining equations (Eqs. 7-14) and comparison/trend figures (Figs. 4-7); the corresponding numeric data tables (Tables S1-S4) and additional plots (Figs. S1-S6) are in the online Supplementary Information, not included in the ingested PDF. [SRC-0097, §3.1, §3.3, Appendix A]
- Sample purity is reported only as a minimum mass-fraction bound (≥0.99 or ≥0.999) with CAS numbers and suppliers (Table 1); no chromatographic trace-impurity breakdown is given. [SRC-0097, §2.1, Table 1]
- The paper predicts (but does not measure) that pure ethanol's isobaric thermal expansion coefficient $\alpha_p$ isotherms would cross at "very high pressures," by analogy with other alcohols reported elsewhere [ref. 38]; this extrapolation is not tested within the paper's own (288.15-413.15 K, 0.1-60 MPa) measurement range. [SRC-0097, §3.3]

## Open questions

- Whether the full per-temperature/per-pressure Supplementary Tables S1-S4 (pure-compound $\kappa_T$, $\alpha_p$; mixture $\kappa_T$, $\alpha_p$) agree with values computed directly from the Tammann-Tait fit parameters in Tables 7-8 via Eqs. 8-14 is not checked here, since the supplementary file was not available in the ingested PDF. [SRC-0097, §3.3; Synthesis]
- Whether this high-pressure PVT and excess-volume dataset has been used (by this or another group) as a force-field or equation-of-state benchmark/validation target for n-heptane, n-octane, ethanol or their mixtures is not addressed in the paper and is not yet tracked elsewhere in SecondBrain. [Synthesis, not stated in the source]

## Cross-source comparison with other SecondBrain sources

No comparable-conditions overlap exists with [[wiki/sources/SRC-0094-investigation-of-microwave-dielectric-properties-of-biodiesel-components]], [[wiki/sources/SRC-0095-temperature-dependent-complex-dielectric-permittivity-a-simple-measurement]] or [[wiki/sources/SRC-0096-traceable-measurements-of-the-static-permittivity-of-dielectric]]: those three sources measure dielectric permittivity ($\varepsilon'$, $\varepsilon''$) of ethanol (among other liquids) at atmospheric pressure, while SRC-0097 measures density ($\rho$) of ethanol and its alkane mixtures at (0.1-60) MPa; the two observable classes (dielectric permittivity vs. density/PVT) are not directly comparable, and no source reports the other's observable at matching conditions. Ethanol is the one liquid common to all four sources, but as a different physical property in each case. No tension page is warranted.

SRC-0097's own bibliography (39 references, all on liquid density, viscosity, excess-volume or vibrating-tube-densimeter calibration literature for alkanes/alcohols) was checked for mentions of "Gregory", "Clarke", "dielectric" or "permittivity" and none were found; SRC-0097 does not cite any already-ingested SecondBrain source. In the reverse direction, SRC-0094 (2013) and SRC-0096 (2005) both predate SRC-0097 (2016) and cannot cite it; SRC-0095 (2023, postdates SRC-0097) was checked for "Abdussalam", "Kijevčanin", "Ivaniš" and "Radović" and none were found in its reference list. No citation link exists in either direction.

## Links

- [[wiki/sources/SRC-0094-investigation-of-microwave-dielectric-properties-of-biodiesel-components]] (shared liquid, ethanol; different observable, no citation link)
- [[wiki/sources/SRC-0095-temperature-dependent-complex-dielectric-permittivity-a-simple-measurement]] (shared liquid, ethanol; different observable, no citation link)
- [[wiki/sources/SRC-0096-traceable-measurements-of-the-static-permittivity-of-dielectric]] (shared liquid, ethanol; different observable, no citation link)
- [[wiki/claims/CLM-0056-ethanol-alkane-mixing-gives-positive-excess-volume-from-hydrogen-bond-disruption]]

## Metadata notes

- Authors: Ali A. Abdussalam, Gorica R. Ivaniš, Ivona R. Radović, Mirjana Lj. Kijevčanin, Faculty of Technology and Metallurgy, University of Belgrade, Serbia. Journal of Chemical Thermodynamics 100, 89-99 (2016). DOI `10.1016/j.jct.2016.04.014`. Received 12 November 2015, revised 5 April 2016, accepted 17 April 2016, published online 19 April 2016.
- Citation check: inspected SRC-0097's own 39-reference list (density/viscosity/excess-volume/calibration literature for n-alkanes and alcohols, 1980-2015) — no overlap found with any already-ingested SecondBrain source, including no match for "Gregory", "Clarke", or any dielectric-permittivity terminology.
- Citation check (reverse direction): SRC-0094 (2013) and SRC-0096 (2005) predate this 2016 paper and cannot cite it. SRC-0095 (2023) was searched for the authors' surnames ("Abdussalam", "Kijevčanin", "Ivaniš", "Radović"); none were found in its reference list.
- Categorization: filed under `research/experimental-benchmarking` only, matching the user's stated purpose of building an experimental-data benchmarking collection (here, PVT/density data potentially usable for force-field or equation-of-state validation of n-heptane, n-octane and ethanol, rather than dielectric data as in SRC-0094/0095/0096).
- No author entity pages were created; none of the four authors appear elsewhere in SecondBrain.
- Supplementary Information (Tables S1-S4, Figs. S1-S6) referenced at `http://dx.doi.org/10.1016/j.jct.2016.04.014` was not available in the provided PDF and was not separately retrieved; see Known gaps.

## Ingestion QA

### Retrieval questions checked

- What is the central contribution? High-pressure liquid densities for pure n-heptane, n-octane and ethanol, and for their three binary mixtures (n-octane + ethanol newly measured at high pressure), fitted with a modified Tammann-Tait equation of state and used to derive excess molar volume, isothermal compressibility and isobaric thermal expansion coefficient. [SRC-0097, Abstract]
- What problem does it address? Filling gaps in high-pressure PVT literature for these gasoline/biofuel-relevant alkane + ethanol systems, in particular providing the first high-pressure density data for n-octane + ethanol. [SRC-0097, Introduction]
- What methods were used? Anton Paar DMA HP/DMA 5000 vibrating-tube densimetry at controlled temperature (Peltier, ±0.05 K) and pressure (HiP generator + WIKA transducer), with gravimetric mixture preparation and a modified Tammann-Tait EOS regression. [SRC-0097, §2.2, §3.2]
- What are the key quantitative results? Pure-compound densities agree with literature within 0.012-0.215% AAD depending on reference/liquid (Table 2-3, Fig. 1); binary-mixture EOS fits have AAD ≤0.022% (Table 8); both alcohol-containing mixtures show positive excess molar volume, increasing with temperature and decreasing (then leveling off) with pressure (Fig. 4), while n-heptane + n-octane is nearly ideal. [SRC-0097, §3.1, §3.3]
- What are the limitations? Narrower $T,p$ range for mixtures than pure compounds; no independent literature check for most of the new n-octane + ethanol data; $C(T)$ fitted as a constant despite Eq. 4's general quadratic form; derived-property numeric tables (S1-S4) are in an unretrieved Supplementary Information. [SRC-0097, §2.2, §3.1-3.3]
- What should not be overgeneralized? The Tammann-Tait fit parameters (Tables 7-8) are valid only within each compound/mixture's measured $T,p$ range and should not be extrapolated (e.g., to predict the ethanol $\alpha_p$-crossing pressure the authors themselves describe as outside their own measured range). [SRC-0097, §3.3; Synthesis]
- Does this connect to existing SecondBrain content? Topically to SRC-0094/SRC-0095/SRC-0096 only via the shared liquid ethanol, not via a shared observable or any bibliographic citation; the hydrogen-bond-disruption interpretation of its positive excess volumes connects conceptually (not citationally) to [[wiki/claims/CLM-0051-xray-diffraction-alcohol-oh-hydrogen-bond-geometry]] and [[wiki/claims/CLM-0052-neutron-md-liquid-ethanol-winding-hydrogen-bonded-chains]]. [SRC-0097; Synthesis]

### Coverage decision

Complete at `coverage_profile: math-standard`. All 14 numbered equations and their variable definitions (including the flagged $C(T)$-constant simplification), the apparatus/calibration/uncertainty methodology, full numeric transcription of all eight main-paper tables (independently re-verified against 300 dpi page renders), the measurement/reuse conditions, untabulated figures, limitations, open questions, and a cross-source comparison with SRC-0094/SRC-0095/SRC-0096 are represented. One claim page was added ([[wiki/claims/CLM-0056-ethanol-alkane-mixing-gives-positive-excess-volume-from-hydrogen-bond-disruption]]) connecting this paper's positive-excess-volume result to SecondBrain's existing alcohol hydrogen-bonding claims. No tension page was created: no genuine disagreement was found against literature cited in the paper or against any other SecondBrain source (no shared observable at matching conditions exists with SRC-0094/0095/0096).

### Known gaps

- Supplementary Tables S1-S4 (pure-compound $\kappa_T$/$\alpha_p$; mixture $\kappa_T$/$\alpha_p$ numeric values) and Figs. S1-S6 are referenced by the paper but were not present in the ingested PDF and have not been retrieved or ingested.
- No numeric $V^E$ table exists in the main paper itself (only Eq. 7 and Fig. 4); exact excess-molar-volume values at specific $(T,p,x)$ points would need to be computed from Tables 4-6 via Eq. 7, or read from Fig. 4/Supplementary Fig. S3.
- Whether this dataset has already been used as a molecular-dynamics force-field or equation-of-state validation target (by this group or others) is not addressed in the paper and has not been checked against any force-field literature.
