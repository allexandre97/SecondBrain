---
type: source
status: active
created: 2026-10-01
updated: 2026-10-01
source_id: SRC-0096
display_title: "Traceable Measurements of the Static Permittivity of Dielectric Reference Liquids Over the Temperature Range 5-50 °C"
short_title: "Gregory & Clarke NPL Static Permittivity Reference Liquids"
aliases:
  - "SRC-0096"
  - "Gregory and Clarke 2005"
  - "Traceable measurements of the static permittivity of dielectric reference liquids over the temperature range 5-50 C"
source_path: raw/sources/SRC-0096-traceable-measurements-of-the-static-permittivity-of-dielectric.pdf
imported_path: raw/sources/SRC-0096-traceable-measurements-of-the-static-permittivity-of-dielectric.pdf
original_filename: "Gregory_2005_Meas._Sci._Technol._16_1506.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: cf76e5e077faf968bb650e0131ca10f2f149cf90acfee87b5221d3a30072a030
authors:
  - "A P Gregory"
  - "R N Clarke"
author_entities: []
year: 2005
venue: "Measurement Science and Technology, 16, 1506-1516"
doi: "10.1088/0957-0233/16/7/013"
arxiv:
metadata_review_status: reviewed
areas:
  - research
categories:
  - research/experimental-benchmarking
tags:
  - scientific-paper
  - dielectric-permittivity
  - static-permittivity
  - reference-liquids
  - admittance-cell
  - metrology
  - traceability
  - water
  - methanol
  - ethanol
  - cyclohexane
  - temperature-dependence
related: []
sources:
  - SRC-0096
cites_sources: []
citation_match_status: reviewed
cqt_review_status: linked
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: math-standard
peer_review_status: peer-reviewed
---

# Traceable Measurements of the Static Permittivity of Dielectric Reference Liquids Over the Temperature Range 5-50 °C

Source ID: `SRC-0096`

## Raw source

- Repository path: `raw/sources/SRC-0096-traceable-measurements-of-the-static-permittivity-of-dielectric.pdf`
- Open raw source: [raw/sources/SRC-0096-traceable-measurements-of-the-static-permittivity-of-dielectric.pdf](../../raw/sources/SRC-0096-traceable-measurements-of-the-static-permittivity-of-dielectric.pdf)

## Summary

Gregory and Clarke (National Physical Laboratory, UK) report traceable measurements of the "static" permittivity ($\varepsilon'$ in the 0.1-1.0 MHz band, where no frequency dependence is observed for these liquids) of eight polar liquids (acetone, butan-1-ol, dimethyl sulphoxide, ethanediol, ethanol, methanol, propan-1-ol, water) and two non-polar liquids (cyclohexane, 1 cS silicone oil) over 5-50 °C, using a shielded, micrometer-driven, variable-separation parallel-plate admittance cell with four-terminal-pair impedance-analyser capacitance measurement. [SRC-0096, abstract] The paper documents the measurement apparatus, an extrapolation procedure for determining the cell's effective micrometer zero-error (and hence electrode separation) from reciprocal-capacitance data, and a detailed uncertainty budget, then compares the new results against prior published values for methanol, cyclohexane and water. [SRC-0096, §§2-6]

The measurements are intended to support the use of these liquids as calibration/check references for RF and microwave dielectric probes and admittance/coaxial-line instruments, and as components of tissue-equivalent liquids for specific-absorption-rate (SAR) measurement. [SRC-0096, Introduction] This is a "static" (near-DC, 0.1-1.0 MHz) companion to the same authors' RF/microwave (30 MHz-5 GHz) measurements on the same liquids, described in a separate paper (ref. [8]) and combined into a single reference-liquid tables report (ref. [6], NPL Report CETM 33, 2001) that is cited elsewhere in SecondBrain (see Links below). [SRC-0096, Introduction, §7]

## Key points

- The admittance cell is a shielded, two-terminal, parallel-plate design (40 mm diameter gold-flashed brass disc electrodes) with a precision 100 mm-barrel micrometer (0.0005 mm resolution) for electrode-separation adjustment, temperature-controlled water circulation around the shield/lower electrode and active air-based temperature control of the (thermally decoupled) upper electrode assembly, enabling operation over 5-50 °C. [SRC-0096, §2, Fig. 1]
- Capacitance is measured with a Hewlett-Packard HP4194A impedance analyser via four-terminal-pair connections, which is practically unaffected by stray/guard capacitances at low frequencies, unlike simple two-terminal measurement. [SRC-0096, §2]
- Because the cell's effective electrode separation changes with temperature (brass has non-negligible thermal expansion) and the upper electrode cannot be held at exactly the same temperature as the lower one in the absence of a liquid sample, the authors use a linear extrapolation of reciprocal capacitance vs. micrometer reading (at 9 micrometer positions from 2.75 down to 0.75 mm gap, in 0.25 mm steps) to determine an "effective" micrometer zero-error $Z$ for both the empty (air) cell and the liquid-filled cell at each temperature, from which the change in cell length between air and liquid measurements is derived and corrected for. [SRC-0096, §3, Fig. 3, Fig. 4]
- Static permittivity is obtained from a weighted average of capacitance-ratio results (liquid/air) across a frequency sub-band (typically 200 kHz-750 kHz or up to 1 MHz) and micrometer positions down to 0.75 mm gap, excluding the smallest gaps (electrode non-parallelism/fringing nonlinearity) and frequencies below ~100-150 kHz (electrode-polarization effects) and, for the highest-permittivity liquid (water), effects of lead inductance at 1 MHz. [SRC-0096, §4.1, Fig. 4, Fig. 5]
- New results for methanol (full 5-50 °C set, Table 3), cyclohexane (Table 4) and deionized water (Table 5) agree with independent literature values (Kienitz and Marsh 1981; Jordan et al; NPL 1990; Cunningham et al; Kaatze 1989) within the reported combined uncertainties at every compared temperature. [SRC-0096, §5, Tables 3-5]
- New static-permittivity results at 20 °C, 25 °C and 30 °C for the remaining six liquids (acetone, butan-1-ol, dimethyl sulphoxide, ethanediol, ethanol, propan-1-ol, 1 cS silicone oil) are reported in Tables 6-8, without an independent literature comparison in this paper. [SRC-0096, §5, Tables 6-8]
- A detailed, GUM/UKAS-M3003-based uncertainty budget is given, dominated (for methanol) by the type-A (repeatability) component from repeated-experiment spread, zero-error correction, and impedance-analyser linearity, with temperature uncertainty depending on how far the measurement temperature is from the cell's actively-controlled range; further largely negligible contributions (electrode thermal expansion, liquid contamination, cable inductance, residual electrode polarization, stray capacitance, and finite-frequency departure from the DC/static limit) are itemized separately. [SRC-0096, §6, Tables 9-10]

## Methods and evidence

The core measurement principle (shielded two-terminal admittance cell) relates total measured capacitance $C_t$ to the real relative permittivity $\varepsilon'$ of the liquid filling the cell via Eq. 1 below; for a parallel-plate cell the dominant vacuum geometric capacitance term is given by Eq. 2. Because the cell is only calibrated via a capacitance ratio between liquid-filled and air-filled measurements at the same (or a correctable) electrode separation, the absolute accuracy of the impedance analyser's capacitance reading is not critical — only its *linearity* (ratio accuracy) matters, which the authors verify separately using calibrated standard capacitors and small-footprint "Sufflex" capacitors swept from 1 kHz to 1 MHz. [SRC-0096, §4.1]

Lead/cable inductance between the impedance analyser and the cell (~42 nH total) causes the apparent measured capacitance $C_{app}$ to depart from the true capacitance $C$ at high frequency, following Eq. 3; this effect is largest for water (the highest-permittivity, hence highest-capacitance, liquid measured) and is corrected numerically. [SRC-0096, §2, Eq. 3] Electrode polarization is identified as a competing low-frequency effect (large for water and other polar/ionic-leaning liquids), motivating the choice of a working frequency sub-band (roughly 100-150 kHz to 750 kHz-1 MHz) in which neither inductive nor polarization effects are significant, demonstrated experimentally for methanol in Table 1. [SRC-0096, §2, Table 1]

The zero-error extrapolation procedure (Fig. 4) performs, independently at each frequency, a weighted least-squares fit of reciprocal capacitance against micrometer reading for both the air-filled and liquid-filled cell, extracts an "effective" zero-error $Z$ from each fit's intercept/gradient ratio, averages across frequencies, computes the change in cell length $\Delta$ between the air and liquid conditions, applies $\Delta$ to correct the air-measurement reciprocal capacitances, and only then takes the capacitance ratio at each micrometer position and frequency to obtain the liquid permittivity, which is finally averaged (weighted by frequency and micrometer-position weighting factors) to a single result. [SRC-0096, §3, Fig. 3, Fig. 4] Measurements at the smallest electrode gaps are given zero weight because fringing capacitance becomes non-reciprocal in $d$ there (observed as nonlinearity in Fig. 3's reciprocal-capacitance plot below ~0.75 mm gap). [SRC-0096, §3]

Validation: methanol, cyclohexane and water were chosen partly because independent, well-established literature values exist (IUPAC-recommended data for cyclohexane and water via Kienitz and Marsh 1981 and Kaatze 1989); agreement with these at every compared temperature (Tables 3-5) is used to build confidence in the cell and procedure before reporting new, less-independently-verified results for the other seven liquids (Tables 6-8). Cyclohexane and water were measured despite lying outside the cell's nominal design range of $\varepsilon' \approx 5$-40 specifically as an out-of-range confidence check. [SRC-0096, §5, §7]

## Key equations

Shielded two-terminal admittance-cell capacitance relation: total measured capacitance as a function of electrode separation $d$. [SRC-0096, eq. 1, p. 1507]

$$
C_t(d) = \varepsilon' C_g(d) + \varepsilon' C_f(d) + C_s
$$

Vacuum geometric capacitance of a parallel-plate cell, as printed in the source. [SRC-0096, eq. 2, p. 1507]

$$
C_g(d) = \varepsilon_0 \varepsilon' A / d
$$

Apparent capacitance measured in the presence of lead/cable inductance $L$ at measurement frequency $f$, relative to the true capacitance $C$. [SRC-0096, eq. 3, p. 1508]

$$
C_{app} = \frac{C}{1 - 4\pi^2 f^2 L C}
$$

### Variable glossary

- $C_t(d)$: total measured capacitance of the admittance cell at electrode separation $d$.
- $\varepsilon'$: real part of the relative permittivity of the liquid (or air) filling the cell; this is the "static" permittivity reported throughout the paper.
- $C_g(d)$: geometric (dominant, $1/d$) capacitance term between the electrodes.
- $C_f(d)$: fringing-field capacitance at the electrode edges; left as an unspecified function of $d$ since the method does not require its value.
- $C_s$: constant stray capacitance in parallel with the electrode system; made negligible by shielding.
- $A$: electrode area; $d$: electrode (plate) separation; $\varepsilon_0$: permittivity of free space.
- $C_{app}$, $C$: apparent (inductance-affected) and true capacitance at frequency $f$; $L$: total lead/cable inductance (~42 nH in this setup).
- $M$: micrometer reading (mm); $Z$: "effective" micrometer zero-error (mm), such that true electrode separation $d = M - Z$.
- $R_{k,i}$: reciprocal measured capacitance at frequency index $k$ and micrometer-position index $i$ (air or sample, per the superscript used in Fig. 4).
- $G_k$, $I_k$: gradient and intercept of the weighted linear fit of $R_{k,i}$ vs. $M_i$ at frequency $f_k$ (used to compute $Z_k = -I_k/G_k$).
- $\Delta$: change in effective cell length between the air and sample measurement conditions, $\Delta = \bar{Z}^{\text{air}} - \bar{Z}^{\text{sample}}$.
- $W^{\text{mic}}$, $W^{\text{freq}}$: micrometer-position and frequency weighting factors used in averaging.

### Equation inventory

| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |
| Admittance-cell capacitance relation | SRC-0096, eq. 1, p. 1507 | This page | Relates total measured capacitance to liquid permittivity for a shielded two-terminal cell. | $C_t$, $\varepsilon'$, $C_g$, $C_f$, $C_s$, $d$ | Defines the physical basis for extracting $\varepsilon'$ from a capacitance ratio (liquid vs. air) at matched electrode separation. |
| Parallel-plate geometric capacitance | SRC-0096, eq. 2, p. 1507 | This page | Gives the dominant (geometric) capacitance term for a parallel-plate cell. | $C_g$, $\varepsilon_0$, $\varepsilon'$, $A$, $d$ | As printed, this equation duplicates the $\varepsilon'$ factor already present in eq. 1 (see Mathematical gaps); use eq. 1 as the authoritative relation. |
| Lead-inductance capacitance correction | SRC-0096, eq. 3, p. 1508 | This page | Corrects apparent capacitance for cable/lead inductance at a given frequency. | $C_{app}$, $C$, $f$, $L$ | Needed to reconstruct true capacitance from raw impedance-analyser readings above ~100 kHz for high-permittivity liquids (notably water). |

### Mathematical gaps

- Eq. 2 as printed, $C_g(d) = \varepsilon_0\varepsilon' A/d$, includes a factor of $\varepsilon'$, even though the surrounding text defines $C_g$ as "the **vacuum** 'geometric' capacitance between the electrodes" and eq. 1 already carries $\varepsilon'$ as a separate multiplying factor ($\varepsilon' C_g(d) + \varepsilon' C_f(d) + C_s$). This was independently re-verified against two separate 350-400 dpi renders of page 1507 (printed exactly as $C_g(d)=\varepsilon_0\varepsilon' A/d$ both times); it is reproduced here exactly as printed rather than silently corrected. It is most plausibly a typesetting/editing error in the original publication (the vacuum geometric capacitance of a parallel-plate capacitor is conventionally $C_g(d) = \varepsilon_0 A/d$, without $\varepsilon'$), but this is not stated or corrected anywhere in the source itself, and no errata were found. The paper's actual computational procedure (Fig. 4, stages 1-6) does not use eq. 2 directly — it works from measured reciprocal capacitances and a capacitance *ratio* between sample and air measurements — so this apparent inconsistency does not propagate into the reported numerical results.
- The full weighted-least-squares and weighted-averaging formulas shown graphically in Fig. 4 (stages 1-6) are reproduced here in symbolic form via the variable glossary and equation-inventory description above, but the exact summation formulas as typeset in the figure (e.g., $R^{air}_{k,i} = G_k^{air}M_i + I_k^{air}$, and the two weighted-average formulas for $\bar Z$ and the final $\bar\varepsilon'_i$) are not reproduced as separate display equations, since they are a flowchart annotation rather than a numbered equation and are fully paraphrased in the Methods and evidence section above.

## Data tables

Full numeric transcription of all ten tables in the paper. Tables 3-8 report static-permittivity measurement results (and literature comparisons); Tables 1, 2, 9 and 10 report supporting capacitance/uncertainty data for the methanol worked example. All values were independently re-verified a second time against 350-400 dpi page renders of the original table pages; no value was found illegible, and the only anomaly found was the eq. 2 inconsistency recorded above (a printed-equation issue, not a table-transcription issue). No numeric table value itself was found to be anomalous or inconsistent.

### Measurement conditions (for reuse)

- Instrument: shielded, two-terminal, variable-electrode-separation parallel-plate admittance cell (40 mm diameter gold-flashed brass disc electrodes), derived from the 1930s Hartshorn and Ward NPL design, with capacitance measured via a Hewlett-Packard HP4194A impedance analyser using four-terminal-pair connections (instrument averaging set to 128, integration time "medium"). [SRC-0096, §2]
- Electrode-separation control: a precision 100 mm-barrel micrometer with 0.0005 mm resolution; typical working micrometer positions correspond to electrode gaps $d$ from 2.75 to 0.75 mm in 0.25 mm steps (9 positions), with gaps below 0.75 mm excluded from the permittivity calculation because of fringing-capacitance nonlinearity. [SRC-0096, §3]
- Calibration/traceability: impedance-analyser linearity verified against capacitance standards calibrated traceably to international standards (1 kHz-1 MHz) and against small "Sufflex" capacitors swept across the full measurement band; linearity uncertainty taken conservatively as the manufacturer's specification, $\pm 0.0003 \times \varepsilon'$. The method itself requires only capacitance *ratios* (sample/air), not absolute capacitance accuracy. [SRC-0096, §4.1]
- Temperature control and measurement: water circulated through the shield/lower-electrode duct from a temperature-controlled bath; the thermally-isolated upper electrode assembly actively temperature-controlled via heated/cooled compressed air from a vortex tube. Calibrated 1 mm-diameter platinum-resistance thermometers at both electrodes (removed immediately before each capacitance measurement to avoid affecting the admittance reading, then re-inserted to confirm final temperature). Measurements taken only when both thermometers read within $\pm 0.02$ °C of the target temperature; achieved operating range 5-50 °C. [SRC-0096, §2, §3, §6]
- Frequency range used for the reported "static" permittivity: 0.1-1.0 MHz nominally, narrowed in practice to a sub-band (typically 200 kHz-750 kHz, up to 1 MHz for some liquids) that avoids both low-frequency electrode-polarization effects and high-frequency lead-inductance effects; frequencies below ~100-150 kHz are excluded from the final weighted average. [SRC-0096, §2, §4.1, Table 1]
- Sample handling: "all samples were taken from newly opened bottles of high-purity grade liquids which were obtained from chemical suppliers" (no specific purity/grade percentages or supplier names given in the main text); first and last measurements of each experiment session were made at 20 °C and compared to check for temperature-drift or air-bubble artifacts; most liquids were measured in three separate experiments spanning the full temperature range, giving six independent weighted-average results at the common 20 °C point (used to estimate type-A uncertainty, Fig. 7). [SRC-0096, §3, §4.2, §6]
- Reported precision/uncertainty: NPL results are quoted at coverage factor $k=2$ (approximately 95% confidence); uncertainties in brackets in Tables 3-8 include an additional temperature-measurement-uncertainty contribution ($\pm 0.1$ °C for 10-35 °C, $\pm 0.2$ °C at 5 °C and 40-50 °C). A full dominant-contribution uncertainty budget for methanol is tabulated in Table 9 (type-A repeatability, zero-error correction, impedance-analyser linearity, temperature); further largely-negligible contributions are tabulated in Table 10 (electrode thermal expansion, liquid contamination, cable inductance, residual electrode polarization, stray capacitance, and the small systematic offset between "static" ε′ and the true DC limit for liquids with low-frequency Debye relaxation, e.g. butan-1-ol at 10 °C). [SRC-0096, §6, Tables 9-10]
- Full per-temperature data for all ten liquids (beyond the 20/25/30 °C summaries in Tables 6-8) are stated to be available in a separate NPL report [SRC-0096, ref. 6], not reproduced in this paper or ingested here.

### Table 1 - Measured apparent capacitance of a methanol sample over a wide frequency band at fixed electrode separation [SRC-0096, Table 1]

Demonstrates the frequency sub-band (100 kHz-1 MHz) in which electrode-polarization (low-frequency) and lead-inductance (high-frequency, ~10 MHz) effects are both insignificant.

| Frequency | $C$ (pF) |
| --- | --- |
| 100 Hz | 15 460.0 |
| 200 Hz | 4 540.0 |
| 500 Hz | 1 145.0 |
| 1 kHz | 572.5 |
| 10 kHz | 363.8 |
| 100 kHz | 360.20 |
| 200 kHz | 360.28 |
| 500 kHz | 360.07 |
| 1 MHz | 360.06 |
| 10 MHz | 360.30 |

### Table 2 - A complete set of methanol measurements at 20 °C [SRC-0096, Table 2]

Measured permittivity as a function of micrometer reading $M$ (mm) and frequency. The final result ($\varepsilon' = 33.62$ for this particular experiment) is a weighted average of the 200 kHz-750 kHz data at micrometer readings from 7.75 mm upwards; the "effective" zero error $Z$ = 6.82 mm (subtract from $M$ to get the inter-electrode separation).

| $M$ (mm) | 100 kHz | 150 kHz | 200 kHz | 250 kHz | 500 kHz | 750 kHz | 1 MHz |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 7.25 | 33.895 | 33.841 | 33.809 | 33.740 | 33.734 | 33.729 | 33.742 |
| 7.50 | 33.680 | 33.641 | 33.623 | 33.579 | 33.577 | 33.580 | 33.590 |
| 7.75 | 33.711 | 33.684 | 33.667 | 33.634 | 33.641 | 33.639 | 33.655 |
| 8.00 | 33.649 | 33.626 | 33.621 | 33.593 | 33.598 | 33.608 | 33.619 |
| 8.25 | 33.673 | 33.646 | 33.626 | 33.614 | 33.618 | 33.628 | 33.649 |
| 8.50 | 33.682 | 33.663 | 33.637 | 33.614 | 33.629 | 33.636 | 33.657 |
| 8.75 | 33.681 | 33.657 | 33.636 | 33.616 | 33.627 | 33.633 | 33.650 |
| 9.00 | 33.668 | 33.646 | 33.623 | 33.604 | 33.612 | 33.619 | 33.638 |
| 9.25 | 33.682 | 33.655 | 33.643 | 33.616 | 33.623 | 33.629 | 33.648 |
| 9.50 | 33.682 | 33.659 | 33.644 | 33.617 | 33.623 | 33.627 | 33.640 |

### Table 3 - Comparison of the measured static permittivity of methanol with literature values [SRC-0096, Table 3]

NPL data given at coverage factor $k=2$ (~95% confidence); figures in brackets include the temperature-measurement contribution (note (a), per Table 8 caption). Literature uncertainties: (b) quoted at 95% confidence; (c) assumed to correspond to one standard deviation.

| Temperature (°C) | $\varepsilon'$ (NPL) | $\pm$ [a] | $\varepsilon'$ (published) | $\pm$ | Reference |
| --- | --- | --- | --- | --- | --- |
| 5 | 36.86 | 0.06 (0.07) | | | |
| 10 | 35.74 | 0.06 (0.06) | 35.70 | 0.03 [c] | Kienitz and Marsh [29] |
| 15 | 34.68 | 0.06 (0.06) | | | |
| 20 | 33.64 | 0.06 (0.06) | 34.8 | 0.5 [b] | Jordan et al [30] |
| 20 | | | 33.66 | 0.03 [c] | Kienitz and Marsh [29] |
| 20 | | | 33.65 | 0.1 [b] | NPL 1990 [31] |
| 25 | 32.66 | 0.06 (0.06) | 32.62 | 0.03 [c] | Cunningham [32] |
| 25 | | | 32.66 | 0.02 [c] | Kienitz and Marsh [29] |
| 25 | | | 32.65 | 0.1 [b] | NPL 1990 [31] |
| 30 | 31.69 | 0.06 (0.06) | 31.70 | 0.1 [b] | NPL 1990 [31] |
| 35 | 30.78 | 0.06 (0.06) | | | |
| 40 | 29.85 | 0.06 (0.07) | 29.86 | 0.05 [c] | Kienitz and Marsh [29] |
| 45 | 28.95 | 0.06 (0.07) | | | |
| 50 | 28.19 | 0.06 (0.07) | | | |

### Table 4 - Comparison of the measured static permittivity of cyclohexane with literature values [SRC-0096, Table 4]

| Temperature (°C) | $\varepsilon'$ (NPL) | $\pm$ [a] | $\varepsilon'$ (Kienitz and Marsh [29]) | $\pm$ [c] |
| --- | --- | --- | --- | --- |
| 10 | 2.040 | 0.002 (0.002) | 2.039 | 0.0015 |
| 20 | 2.024 | 0.002 (0.002) | 2.024 | 0.001 |
| 30 | 2.008 | 0.002 (0.002) | 2.008 | 0.001 |
| 40 | 1.992 | 0.002 (0.002) | 1.992 | 0.001 |
| 50 | 1.975 | 0.002 (0.002) | 1.976 | 0.001 |

### Table 5 - Comparison of the measured static permittivity of deionized water with literature values [SRC-0096, Table 5]

The admittance cell used is noted by the authors as "not of optimum design for measuring water," so these are described as a useful check on cell operation rather than the primary intended use case.

| Temperature (°C) | $\varepsilon'$ (NPL) | $\pm$ [a] | $\varepsilon'$ (Kaatze et al [33]) | $\pm$ [c] | $\varepsilon'$ (Kienitz and Marsh [29]) | $\pm$ [c] |
| --- | --- | --- | --- | --- | --- | --- |
| 10 | 84.04 | 0.20 (0.20) | 83.92 | 0.20 | 83.91 | 0.07 |
| 20 | 80.29 | 0.20 (0.20) | 80.21 | 0.20 | 80.16 | 0.05 |
| 30 | 76.68 | 0.20 (0.20) | 76.56 | 0.20 | 76.57 | 0.05 |
| 40 | 73.31 | 0.20 (0.21) | 73.18 | 0.20 | 73.16 | 0.04 |
| 50 | 69.99 | 0.20 (0.21) | 69.89 | 0.20 | 69.90 | 0.04 |

### Table 6 - New results for the static permittivity of other liquids at 20 °C [SRC-0096, Table 6]

| Liquid | $\varepsilon'$ | $\pm$ [a] |
| --- | --- | --- |
| Acetone | 21.13 | 0.04 (0.04) |
| Butan-1-ol | 18.19 | 0.04 (0.04) |
| Dimethyl sulphoxide | 47.13 | 0.06 (0.06) |
| Ethanediol | 41.89 | 0.06 (0.06) |
| Ethanol | 25.16 | 0.04 (0.04) |
| Propan-1-ol | 21.15 | 0.04 (0.04) |
| Silicone oil (1 cS) | 2.307 | 0.002 (0.002) |

### Table 7 - New results for the static permittivity of other liquids at 25 °C [SRC-0096, Table 7]

| Liquid | $\varepsilon'$ | $\pm$ [a] |
| --- | --- | --- |
| Acetone | 20.59 | 0.04 (0.04) |
| Butan-1-ol | 17.53 | 0.04 (0.04) |
| Dimethyl sulphoxide | 46.49 | 0.06 (0.06) |
| Ethanediol | 40.75 | 0.06 (0.06) |
| Ethanol | 24.43 | 0.04 (0.04) |
| Propan-1-ol | 20.42 | 0.04 (0.04) |
| Silicone oil (1 cS) | 2.294 | 0.002 (0.002) |

### Table 8 - New results for the static permittivity of other liquids at 30 °C [SRC-0096, Table 8]

Key: (a) NPL data are given at coverage factor $k=2$ (~95% confidence); figures in brackets include the temperature contribution. (b) Quoted at 95% confidence level. (c) Assumed to correspond to one standard deviation. [This key applies to Tables 3-8 and is printed in full only under Table 8.]

| Liquid | $\varepsilon'$ | $\pm$ [a] |
| --- | --- | --- |
| Acetone | 20.10 | 0.04 (0.04) |
| Butan-1-ol | 16.89 | 0.04 (0.04) |
| Dimethyl sulphoxide | 45.86 | 0.06 (0.06) |
| Ethanediol | 39.66 | 0.06 (0.06) |
| Ethanol | 23.64 | 0.04 (0.04) |
| Propan-1-ol | 19.75 | 0.04 (0.04) |
| Silicone oil (1 cS) | 2.279 | 0.002 (0.002) |

### Table 9 - Estimated dominant standard uncertainty contributions for methanol [SRC-0096, Table 9]

| Contribution | Standard uncertainty of input quantity | Standard uncertainty of permittivity |
| --- | --- | --- |
| Type-A from figure 7 | | $\pm 0.02$ |
| Zero-error correction | Approximately $\pm 0.0005$ mm | $\pm 0.01$ |
| Impedance analyser linearity | $\pm 0.0003 \times \varepsilon'$ | $\pm 0.01$ |
| Temperature (a) | $\pm 0.05$ °C | $\pm 0.01$ |
| Temperature (b) | $\pm 0.1$ °C | $\pm 0.02$ |

(a) For 10-35 °C. (b) For 5 and 40-50 °C.

### Table 10 - Sources of uncertainty estimated in most cases to be negligible in magnitude [SRC-0096, Table 10]

| Uncertainty contribution | Comment |
| --- | --- |
| Uncertainty in electrode expansion correction | Dependent on linear expansion coefficient. Since the grade of brass is unspecified the standard uncertainty is taken to be 10% of the permittivity correction for expansion. For water at 50 °C the standard uncertainty is estimated to be $\pm 0.007$. This contribution is smaller for measurements at lower temperatures and on other liquids. |
| Contamination of liquid during experiment | Considered to be taken into account in the spread of figure 7, since this contains data from initial and final measurements in experiments which lasted a whole day. |
| Cable inductance | Standard uncertainty less than 0.001 for methanol. |
| Electrode polarization | A low-frequency effect which shows strong frequency dependence and increases for small electrode gaps. Data below a chosen frequency (typically 150 kHz) is excluded in the calculation of the averaged result. Any residual effect is taken to be represented in the type A uncertainty. |
| Stray capacitance | Careful shielding used to minimize fields around the outside of the cell. If there were a stray-capacitance effect, it would be most significant at largest gaps, but there is no evidence of this, e.g. in figure 3. It is estimated that $C_s < 0.003$ pF. |
| Change in $\varepsilon'$ from DC | For the worst case, butan-1-ol at 10 °C (which has a Debye relaxation frequency of only 170 MHz), the change in $\varepsilon'$ is approx. $-0.0004$. |

### Figures with data not captured in the tables

- Fig. 1: labeled exploded-view mechanical drawing of the admittance cell (not a data figure). [SRC-0096, Fig. 1]
- Fig. 2: schematic of the electrical connections between the impedance-analyser terminals and the cell (not a data figure). [SRC-0096, Fig. 2]
- Fig. 3: reciprocal cell capacitance vs. micrometer reading for the air-filled cell, used to determine the effective zero-error $Z$ by extrapolation to zero reciprocal capacitance; no per-point numeric table is given (Table 1/2 give related but distinct capacitance/permittivity data). [SRC-0096, Fig. 3]
- Fig. 4: flowchart of the six-stage calculation procedure from reciprocal-capacitance data to final averaged permittivity (reproduced in prose in Methods and evidence above, and as a Mathematical gap note); not a data figure. [SRC-0096, Fig. 4]
- Fig. 5: residual capacitance (measured minus average) vs. frequency for the air-filled cell at 11 different electrode separations (3.18 mm down to 0.43 mm), used to assess impedance-analyser digitization artifacts; curve values are not tabulated. [SRC-0096, Fig. 5]
- Fig. 6: measured methanol permittivity at 20 °C vs. effective electrode spacing, for the same frequencies tabulated in Table 2 (same underlying data as Table 2, shown graphically). [SRC-0096, Fig. 6]
- Fig. 7: standard deviation of six repeated 20 °C permittivity results vs. measured static permittivity, for all ten liquids (~60 total results); used as the basis for the type-A uncertainty estimate (Table 9); per-liquid numeric values are not tabulated, only the scatter plot. [SRC-0096, Fig. 7]

## Limitations and caveats

- The admittance cell was designed for liquids with permittivity in the range $\varepsilon' \approx 5$-40; cyclohexane ($\varepsilon' \approx 2$) and water ($\varepsilon' \approx 70$-85) lie outside this design range and are explicitly described as "not of optimum design" cases included only as a confidence check, though their results still agree with literature within uncertainty. [SRC-0096, §5, Table 5]
- "Static" permittivity here specifically means the real part of $\varepsilon'$ measured at 0.1-1.0 MHz; the paper notes this is indistinguishable, within measurement precision, from the true DC/zero-frequency limit for all liquids studied except in the worst case identified (butan-1-ol at 10 °C, where the estimated DC-vs-static difference is only $\approx -0.0004$, i.e. negligible at the reported precision). [SRC-0096, §6, Table 10]
- New results for acetone, butan-1-ol, dimethyl sulphoxide, ethanediol, ethanol, propan-1-ol and silicone oil (Tables 6-8) are not independently cross-checked against literature in this paper (unlike methanol, cyclohexane and water), so their accuracy rests on the validated cell/method rather than an external agreement check specific to those liquids. [SRC-0096, §5]
- Eq. 2 as printed is internally inconsistent with eq. 1's stated definition of $C_g$ (see Mathematical gaps); this does not affect the numerical results, which are derived from capacitance ratios rather than from eq. 2 directly, but it is an unresolved typesetting/editing issue in the published paper.
- Full per-temperature data tables for all ten liquids are stated to reside in a separate NPL report (ref. [6], CETM 33, 2001), not included in or ingested from this journal paper; this paper gives only the 5-50 °C set for methanol/cyclohexane/water (Tables 3-5) and 20/25/30 °C summaries for the rest (Tables 6-8).
- Sample purity/grade and supplier identity are described only generically ("newly opened bottles of high-purity grade liquids...from chemical suppliers"); no CAS numbers, purity percentages, or supplier names are given. [SRC-0096, §4.2]
- Dimethyl sulphoxide is explicitly flagged by the authors as strongly hygroscopic, with permittivity measurably increasing on atmospheric exposure within a short time; users of this reference value are cautioned accordingly, though the paper does not quantify how much of an exposure-time effect, if any, affected its own DMSO measurements. [SRC-0096, §4.2]

## Open questions

- Whether the apparent $\varepsilon'$ duplication in eq. 2 is a simple typesetting error (most likely) or reflects some non-standard definition of $C_g$ used only in this paper is not resolved from the text alone; no errata for this article were located. [Synthesis, not stated in the source]
- The paper does not state how closely the new Tables 6-8 results (acetone, butan-1-ol, DMSO, ethanediol, ethanol, propan-1-ol, silicone oil) agree with other published values, since no literature comparison is given for these liquids in this paper; whether such a comparison exists in the companion NPL report (ref. [6]) is not addressed here. [SRC-0096, §5]

## Cross-source comparison with other SecondBrain dielectric-permittivity sources

[[wiki/sources/SRC-0094-investigation-of-microwave-dielectric-properties-of-biodiesel-components]] measures ethanol and methanol permittivity at 280 MHz-4.5 GHz (30-75 °C), and [[wiki/sources/SRC-0095-temperature-dependent-complex-dielectric-permittivity-a-simple-measurement]] measures water, methanol, and ethanol permittivity near 1.85-2.45 GHz (with the alcohols showing non-monotonic $\varepsilon'(T)$, per [[wiki/claims/CLM-0054-alcohols-show-non-monotonic-dielectric-permittivity-temperature-dependence]]). SRC-0096 measures the same three liquids' permittivity at 0.1-1.0 MHz ("static," i.e. effectively the zero-frequency/non-dispersive limit). Because water, methanol and ethanol are all known to exhibit Debye-type dielectric relaxation with relaxation frequencies in the GHz range at room temperature (water ≈17 GHz, lower alcohols somewhat lower), SRC-0096's static values are expected to sit above the microwave-frequency $\varepsilon'$ values reported in SRC-0094/SRC-0095 by an amount that grows with frequency and depends on each liquid's specific relaxation time — this is a known dispersion effect, not a measurement disagreement. [Synthesis, not stated in any single source]

A direct numeric comparison was not performed here because it would require fitting each liquid's full Debye (or non-Debye) relaxation spectrum, which none of the three sources individually provides for a consistent liquid/temperature combination (SRC-0096 reports only the static limit; SRC-0094 reports only two fixed frequencies per liquid-temperature point; SRC-0095 reports regressed curve-fit parameters at design frequencies near 1.85-2.45 GHz, not multi-frequency sweeps). No tension page is warranted, since the three sources do not report values at overlapping frequencies that could be checked against each other's stated uncertainties; the relationship between them is complementary (reference zero-frequency limit vs. two microwave operating-point measurements) rather than contradictory.

## Links

No existing SecondBrain source, concept, entity, claim, question, or tension page previously addressed traceable static (near-DC) permittivity metrology, admittance-cell measurement technique, or NPL dielectric-reference-liquid data; the topical connection is to the two already-ingested microwave-frequency dielectric-permittivity sources below, via shared measured liquids (methanol, ethanol, water) and the shared observable (real relative permittivity $\varepsilon'$), not via any bibliographic citation.

- [[wiki/sources/SRC-0094-investigation-of-microwave-dielectric-properties-of-biodiesel-components]]
- [[wiki/sources/SRC-0095-temperature-dependent-complex-dielectric-permittivity-a-simple-measurement]]

## Metadata notes

- Authors: A P Gregory and R N Clarke, Enabling Metrology Division, National Physical Laboratory (NPL), Hampton Road, Teddington, Middlesex, UK. Measurement Science and Technology 16, 1506-1516 (2005). DOI `10.1088/0957-0233/16/7/013`. Received 21 February 2005, final form 13 May 2005, published online 15 June 2005.
- Citation check: inspected SRC-0096's own reference list (35 references, mostly dielectric-measurement-technique and reference-liquid-property literature from the 1930s-2000s) — none of it overlaps with any already-ingested SecondBrain source (SRC-0094's 2013 biodiesel paper and SRC-0095's 2023 bireentrant-cavity paper both postdate SRC-0096, so they cannot be cited by it, and were confirmed absent from its reference list by name/keyword search).
- Citation check (reverse direction): SRC-0094 was searched for any mention of "Gregory" and none was found. SRC-0095 cites (ref. 57) "Gregory, A P & Clarke, R N, Tables of the complex permittivity of dielectric reference liquids at frequencies up to 5 GHz, National Physical Laboratory Report CETM 33" — this is the companion NPL report (ref. [6] within SRC-0096 itself) that tabulates the full combined static-and-RF/microwave reference-liquid dataset produced by the same two authors, not the SRC-0096 journal article under ingestion here. Per the citation-matching rule (title/author/year must match; a different document by the same authors is not a confirmed link), this is recorded as a related-but-distinct reference rather than a `cites_sources` entry for SRC-0096. A corresponding note has been added to SRC-0095's "Metadata notes" section for symmetry, without altering SRC-0095's `cites_sources` field.
- Categorization: filed under `research/experimental-benchmarking`, consistent with the user's stated purpose of building an experimental dielectric-property benchmarking collection and matching the category already used for SRC-0094 and SRC-0095.
- No author entity pages were created; neither author appears elsewhere in SecondBrain.

## Ingestion QA

### Retrieval questions checked

- What is the central contribution? Traceable, uncertainty-quantified "static" (0.1-1.0 MHz) permittivity measurements for ten candidate dielectric reference liquids over 5-50 °C, using a shielded variable-separation admittance cell, validated against independent literature for three of the ten liquids. [SRC-0096, abstract, §7]
- What problem does it address? The lack of published dielectric reference-liquid data with clear traceability and well-documented uncertainty analysis, needed to calibrate and check RF/microwave dielectric-measurement instruments (including coaxial probes used for tissue-equivalent/SAR work). [SRC-0096, Introduction]
- What methods were used? A micrometer-driven, variable-electrode-separation, shielded parallel-plate admittance cell with four-terminal-pair impedance-analyser capacitance measurement; a reciprocal-capacitance extrapolation procedure to track and correct for thermal changes in electrode separation; weighted averaging across frequency and micrometer position to obtain a single permittivity value per liquid/temperature. [SRC-0096, §2-4]
- What are the key quantitative results? Methanol, cyclohexane and water results (Tables 3-5) agree with independent literature at every compared temperature within combined uncertainty; new results for acetone, butan-1-ol, DMSO, ethanediol, ethanol, propan-1-ol and silicone oil are given at 20/25/30 °C (Tables 6-8) without an independent check in this paper. [SRC-0096, Tables 3-8]
- What are the limitations? Cyclohexane and water lie outside the cell's intended $\varepsilon'$ design range; DMSO is hygroscopic and time-sensitive; eq. 2 contains an apparent typesetting inconsistency; full per-temperature data for all ten liquids are only available in a separate, non-ingested NPL report. [SRC-0096, §5-6]
- What should not be overgeneralized? The reported uncertainties and agreement apply specifically to the "static" (0.1-1.0 MHz) regime; these values should not be assumed to equal permittivity at RF/microwave frequencies for liquids with relaxation frequencies in or below that range (see Cross-source comparison section). [Synthesis, not stated in the source]
- Does this connect to existing SecondBrain content? Yes, topically to SRC-0094 and SRC-0095 via shared liquids (methanol, ethanol, water) and the shared permittivity observable, but not via any bibliographic citation in either direction. [SRC-0096; Synthesis]

### Coverage decision

Complete at `coverage_profile: math-standard`. All three numbered equations, their variable definitions (including the flagged eq. 2 inconsistency), the apparatus, zero-error-extrapolation and uncertainty-budget methodology, full numeric transcriptions of all ten tables (independently re-verified against 350-400 dpi page renders), the measurement/reuse conditions, untabulated figures, limitations, open questions, and a cross-source comparison with SRC-0094/SRC-0095 are represented. No claim or tension page was created: the central finding (literature agreement within stated uncertainty) is not itself debatable or contested, and no genuine disagreement beyond stated uncertainty was found against either prior literature or the other two SecondBrain dielectric sources.

### Known gaps

- Full per-temperature data for all ten liquids (beyond the 5-50 °C set for methanol/cyclohexane/water and the 20/25/30 °C summaries for the rest) reside in a separate NPL report (ref. [6], CETM 33, 2001) that has not been ingested.
- The companion RF/microwave (30 MHz-5 GHz) measurement paper on the same ten liquids (ref. [8] in SRC-0096) has not been ingested; it would be the natural next step for any future close dispersion comparison with SRC-0094/SRC-0095's microwave-frequency data.
- The apparent $\varepsilon'$-duplication in printed eq. 2 is recorded as a likely source-side typesetting error but is not independently resolved (e.g., via an erratum).
