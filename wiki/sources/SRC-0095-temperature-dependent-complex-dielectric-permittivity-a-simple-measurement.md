---
type: source
status: active
created: 2026-10-01
updated: 2026-10-01
source_id: SRC-0095
display_title: "Temperature-Dependent Complex Dielectric Permittivity: A Simple Measurement Strategy for Liquid-Phase Samples"
short_title: "Baker-Fales et al. Benchtop Dielectric Permittivity Measurement"
aliases:
  - "SRC-0095"
  - "Baker-Fales et al. 2023"
  - "Temperature-Dependent Complex Dielectric Permittivity: A Simple Measurement Strategy for Liquid-Phase Samples"
source_path: raw/sources/SRC-0095-temperature-dependent-complex-dielectric-permittivity-a-simple-measurement.pdf
imported_path: raw/sources/SRC-0095-temperature-dependent-complex-dielectric-permittivity-a-simple-measurement.pdf
original_filename: "s41598-023-45049-8.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 820b7a4f1c8b5fd0779b8ef9d091f284b61f3a518c37f569a542c4b674c75783
authors:
  - "Montgomery Baker-Fales"
  - "José D. Gutiérrez-Cano"
  - "José M. Catalá-Civera"
  - "Dionisios G. Vlachos"
author_entities: []
year: 2023
venue: "Scientific Reports, 13, 18171"
doi: "10.1038/s41598-023-45049-8"
arxiv:
metadata_review_status: reviewed
areas:
  - research
categories:
  - research/experimental-benchmarking
tags:
  - scientific-paper
  - dielectric-permittivity
  - dielectric-constant
  - dielectric-loss
  - microwave-dielectric-heating
  - water
  - alcohols
  - hydrochloric-acid
  - temperature-dependence
  - benchtop-measurement
related: []
sources:
  - SRC-0095
cites_sources: []
citation_match_status: reviewed
cqt_review_status: linked
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: math-standard
peer_review_status: peer-reviewed
---

# Temperature-Dependent Complex Dielectric Permittivity: A Simple Measurement Strategy for Liquid-Phase Samples

Source ID: `SRC-0095`

## Raw source

- Repository path: `raw/sources/SRC-0095-temperature-dependent-complex-dielectric-permittivity-a-simple-measurement.pdf`
- Open raw source: [raw/sources/SRC-0095-temperature-dependent-complex-dielectric-permittivity-a-simple-measurement.pdf](../../raw/sources/SRC-0095-temperature-dependent-complex-dielectric-permittivity-a-simple-measurement.pdf)

## Summary

Baker-Fales et al. present a benchtop method for measuring the temperature-dependent complex dielectric permittivity ($\varepsilon' - j\varepsilon''$) of liquid samples near the 2.45 GHz industrial/scientific/medical (ISM) microwave frequency, up to vapor pressures of 7 bar. [SRC-0095, abstract] The method extends a previously published standalone bireentrant-cavity dielectric measurement kit (Gutiérrez-Cano et al. 2020) with larger, pressure- and temperature-capable alumina or quartz vials, avoiding the need for a full vector network analyzer, a dedicated temperature controller, a high-pressure coaxial adapter, or calibration against reference materials. [SRC-0095, Methods] The motivation is the general lack of accessible temperature/pressure-resolved dielectric datasets needed to design and simulate microwave-heated chemical reactors. [SRC-0095, Introduction]

The method is validated against literature values for water (20-160 °C, compared to Kaatze's 1989 Debye model at 1.85 GHz) and for the room-temperature dielectric constant of a range of organic solvents, alcohols, and water (parity against refs. 49-59, average 5.8% relative error, $\varepsilon'$ range approximately 1-100). [SRC-0095, Results] The paper then reports new temperature-dependent permittivity data for nine non-alcohol organic solvents, four alcohols, and six aqueous hydrochloric acid solutions (pH 1.0-2.5, plus pure water), fitting each dataset to either a three-parameter exponential (non-alcohol organics) or a six-parameter modified lognormal function (alcohols, HCl solutions), and tabulates the regressed fit parameters rather than the raw per-temperature readings (the raw series are referred to Supplementary Figs. S3-S5, which are not part of this PDF). [SRC-0095, Results, Tables 1-3]

## Key points

- Water and the nine non-alcohol organic solvents tested show a monotonic decrease in both $\varepsilon'$ and $\varepsilon''$ with increasing temperature, well fit (standard error <3%) by the three-parameter exponential $\varepsilon = A_1 \cdot \exp(-A_2 T) + A_3$ (Eq. 1). [SRC-0095, §"Dielectric permittivity of non-alcohol organic solvents", Table 1]
- The four alcohols tested (ethanol, methanol, isopropanol, 2-pentanol) show a qualitatively different, non-monotonic temperature dependence: $\varepsilon'$ and $\varepsilon''$ both rise with temperature to a maximum and then fall, requiring a six-parameter modified lognormal fit (Eq. 2, standard error <3.5%). [SRC-0095, §"Dielectric permittivity of alcohols", Fig. 7, Table 2]
- Aqueous HCl solutions (pH 7 down to pH 1, i.e., pure water through increasing acid strength) show $\varepsilon'$ dropping less steeply with temperature as pH decreases, until at pH 1 $\varepsilon'$ actually increases with temperature; $\varepsilon''$ increases monotonically with HCl addition even at room temperature, and the decrease of $\varepsilon''$ with temperature becomes less prominent until, at pH 2 and below (pH 1.6, 1.3, 1.0), $\varepsilon''$ instead increases with temperature. The authors state this reversal of the temperature trend by ionic strength has not been previously reported. [SRC-0095, §"Dielectric permittivity of aqueous hydrochloric acid solutions", Fig. 8]
- The measurement apparatus is a single-post bireentrant microwave cavity (CNC-machined aluminum, ±5 µm precision) operating with a tailor-made MW reflectometer over 1.5-2.6 GHz, requiring no calibration against reference materials (unlike cavity perturbation methods); dielectric properties are extracted from the measured resonant frequency and quality factor via an electromagnetic mode-matching/circuit model. [SRC-0095, Methods]
- Samples are held in sealed alumina (or, for atmospheric-pressure comparison, quartz) vials rated to 7 bar, heated externally on a hot plate, then transferred into the cavity and measured continuously as the vial cools, with an internal silica-clad optical fiber providing continuous temperature readout. [SRC-0095, Methods, Fig. 3]
- Compared to the most similar prior traceable high-pressure/high-temperature system (Dimitrakis et al. 2009), this setup trades traceability for simplicity (no VNA, HPLC pump, dedicated temperature controller, or custom high-pressure coaxial adapter) and lower apparent experimental variance, attributed partly to a seal placement that avoids geometric changes to the cell on pressurization; all data in this paper were collected in a single day. [SRC-0095, Results]

## Methods and evidence

The cavity's electromagnetic model (mode-matching/circuit analysis, extending Gutiérrez-Cano et al. 2020) relates the complex resonant frequency (resonant frequency + quality factor) of the loaded cavity to the sample's complex permittivity, without requiring calibration against reference materials. [SRC-0095, Methods] An upgraded pressure-temperature-dielectric (PTD) vessel was designed around larger quartz or alumina vials (replacing the original setup's small Pyrex tubes, whose permittivity is itself strongly temperature-dependent) to allow pressurized, high-temperature operation while keeping a single resonant mode across the reflectometer's 1.5-2.6 GHz range; an EM/MATLAB model was used to choose vial/cavity dimensions (Fig. 1) that still achieve roughly a 600 MHz maximum frequency shift for $\varepsilon'$ from 1 to 100, comparable to the original Pyrex-tube version. [SRC-0095, Methods, Figs. 1-2] The internal vial diameter is held to ±20 µm of the modeled nominal value to keep $\varepsilon'$ uncertainty within 2% and $\varepsilon''$ uncertainty within 5%. [SRC-0095, Methods]

Validation used (1) water permittivity measured from 20-160 °C at 1.85 GHz compared to Kaatze's (1989) Debye-model values (close agreement over the reference's full 20-60 °C range), and (2) room-temperature $\varepsilon'$ for a range of non-alcohol organic solvents, alcohols, and water compared to literature values from 11 separate sources (refs. 49-59), yielding 5.8% average relative error across $\varepsilon'\approx1$-100. [SRC-0095, Results, Figs. 4-5] Quartz and alumina vials give nearly identical measurements (Fig. S2, not in this PDF), but alumina was used for all reported temperature-dependent data because of its superior pressure resistance (reliable to 7 bar). [SRC-0095, Results]

## Key equations

Non-alcohol organic solvents (water, the nine solvents in Table 1): a three-parameter exponential describes $\varepsilon'(T)$ and $\varepsilon''(T)$ independently: [SRC-0095, eq. 1, p. 5]

$$
\varepsilon = A_1 \cdot \exp(-A_2 \cdot T) + A_3
$$

Alcohols and HCl solutions: a six-parameter modified lognormal function captures the non-monotonic rise-then-fall behavior: [SRC-0095, eq. 2, p. 6]

$$
\varepsilon = \frac{B_2}{B_1 + T} \cdot \frac{B_3}{\sigma\sqrt{2\pi}} \cdot \exp\left(-\frac{\left(\ln\left(\frac{B_1+T}{B_2}\right) - \mu\right)^2}{2\sigma^2}\right) + B_4
$$

### Variable glossary

- $\varepsilon$: either the dielectric constant ($\varepsilon'$) or loss factor ($\varepsilon''$), fitted independently with its own parameter set.
- $T$: measured temperature, °C.
- $A_1, A_2, A_3$: regressed exponential-fit parameters (Eq. 1, Table 1).
- $B_1, B_2, B_3, B_4$: regressed lognormal-fit scale/offset parameters (Eq. 2, Tables 2-3).
- $\sigma, \mu$: traditional lognormal shape and location parameters (Eq. 2, Tables 2-3).
- Error: standard error of the fit relative to the mean, reported as a percentage, for each parameter set.
- $T_{\mathrm{MAX}}$: maximum temperature (°C) measured for that solvent/solution, chosen to keep vapor pressure within the vessel's 7 bar limit.

### Equation inventory

| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |
| Exponential permittivity fit | SRC-0095, eq. 1, p. 5 | This page | Empirical model for monotonically decreasing $\varepsilon'(T)$, $\varepsilon''(T)$ in water and non-alcohol organic solvents. | $\varepsilon$, $A_1$, $A_2$, $A_3$, $T$ | Lets Table 1's fit parameters reconstruct $\varepsilon'(T)$/$\varepsilon''(T)$ curves for any listed solvent without digitizing the original data points. |
| Modified lognormal permittivity fit | SRC-0095, eq. 2, p. 6 | This page | Empirical model for non-monotonic (rise-then-fall) $\varepsilon'(T)$, $\varepsilon''(T)$ in alcohols and HCl solutions. | $\varepsilon$, $B_1$-$B_4$, $\sigma$, $\mu$, $T$ | Lets Tables 2-3's fit parameters reconstruct the corresponding curves; $B_1$-$B_4$ generalize the lognormal beyond its standard $\sigma$/$\mu$ parameterization via x-/y-axis stretching and offset. |

No further mathematical structure (e.g., the underlying EM mode-matching/circuit-analysis derivation for the cavity itself) is reproduced here; that derivation is presented in full in the cited prior work (Gutiérrez-Cano et al. 2020, ref. 39), which is not ingested as a SecondBrain source. [SRC-0095, Methods]

## Data tables

Full numeric transcription of the paper's three tables. These tables report regressed curve-fit parameters (Eq. 1 or Eq. 2 above), not raw per-temperature instrument readings; the underlying raw temperature-series data points are stated to be listed in Supplementary Figs. S3-S5 and Table S1, which are referenced by the paper but are not included in this PDF (the ingested file is the 10-page main article only). Every value below was independently re-verified against a 350-dpi render of its source page after first transcription; no digit was found illegible, and no transcription anomaly was found (unlike SRC-0094, this paper's three tables showed no internal inconsistency on re-check).

### Measurement conditions (for reuse)

- Instrument: benchtop standalone dielectric measurement kit based on a single-post bireentrant microwave cavity (CNC-machined aluminum, ±5 µm machining precision), with a tailor-made MW reflectometer (no full-featured VNA) operating 1.5-2.6 GHz; extends the device and EM mode-matching/circuit-analysis method of Gutiérrez-Cano et al. (2020, ref. 39). [SRC-0095, Methods]
- Target frequency: measurements are made near the 2.45 GHz ISM band (the same microwave frequency tabulated as one of two design frequencies in [[wiki/sources/SRC-0094-investigation-of-microwave-dielectric-properties-of-biodiesel-components]]'s Tables 2-3). [SRC-0095, abstract, Methods]
- Calibration: none required against reference materials; permittivity is derived directly from the cavity's measured resonant frequency and quality factor via the EM numerical model, unlike cavity perturbation methods (CPM) which require reference-material calibration. Internal vial diameter is held to ±20 µm of the modeled nominal value to bound $\varepsilon'$ uncertainty to 2% and $\varepsilon''$ uncertainty to 5%. [SRC-0095, Methods]
- Sample vessel: pressure-temperature-dielectric (PTD) vessel; alumina vials (quartz also usable but limited to near-atmospheric pressure) with a flanged top sealed by an o-ring, a threaded assembly for pressure containment, and a silica-clad optical-fiber temperature sensor sealed in with soft ETFE ferrules; rated for reliable use up to 7 bar. [SRC-0095, Methods, Fig. 3]
- Temperature/pressure protocol: the sealed vial is heated to a predetermined temperature on an external heating block, then transferred into the measurement cavity; permittivity-temperature data points are collected continuously as the vial cools, so the internal pressure at each recorded point reflects the solvent's own vapor pressure at that temperature (not an externally imposed constant pressure). The paper cites evidence that this does not measurably affect alcohol permittivity over 1-60 bar (Dimitrakis et al. 2009). [SRC-0095, Methods]
- Per-solvent temperature range ($T_{\mathrm{MAX}}$, Tables 1-3) was chosen individually to keep vapor pressure within the 7 bar vessel limit; methanol's $T_{\mathrm{MAX}}$ (111.5 °C) is far above its normal boiling point (64.7 °C) because the sealed, pressurized vessel suppresses boiling. [SRC-0095, Tables 1-2]
- Reported precision: no explicit replicate count or triplicate averaging is stated (contrast with SRC-0094's explicit triplicate-mean ± SD protocol); instead, each solvent/solution's continuous cooling-curve dataset is fit to Eq. 1 or Eq. 2, and the tabulated "Error" column is the fit's standard error relative to the mean (<3% for Eq. 1 fits, <3.5% for alcohol Eq. 2 fits, <4% for HCl Eq. 2 fits). [SRC-0095, Tables 1-3, Results]
- Sample identity: specific purity/grade/supplier information for the nine organic solvents, four alcohols, and HCl solutions is not given in the main text (it may be in the Supplementary Information, not included in this PDF). [SRC-0095]

### Table 1 - Regressed parameters for non-alcohol organic solvents fitted to Eq. (1) [SRC-0095, Table 1]

$A_1$, $A_2$, $A_3$: fit parameters (Eq. 1); Error: standard error relative to the mean; $T_{\mathrm{MAX}}$: maximum temperature measured (°C).

| Solvent | $A_1$ ($\varepsilon'$) | $A_2$ ($\varepsilon'$) | $A_3$ ($\varepsilon'$) | Error ($\varepsilon'$) | $A_1$ ($\varepsilon''$) | $A_2$ ($\varepsilon''$) | $A_3$ ($\varepsilon''$) | Error ($\varepsilon''$) | $T_{\mathrm{MAX}}$ (°C) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MIBK | 12.801 | −0.003555 | 0.000 | 0.5% | 1.908 | −0.015495 | 0.095 | 1.9% | 165.4 |
| Tetrahydrofuran | 7.089 | −0.003233 | 0.326 | 0.3% | 0.219 | −0.012762 | 0.025 | 1.0% | 135.4 |
| γ-Valeractone | 35.766 | −0.001980 | 0.000 | 1.9% | 12.924 | −0.017054 | 1.041 | 2.6% | 185.3 |
| DMSO | 48.082 | −0.002262 | 0.000 | 0.9% | 14.008 | −0.019674 | 1.223 | 1.4% | 179.0 |
| Dimethylformamide | 29.870 | −0.005903 | 9.803 | 0.3% | 5.954 | −0.017535 | 0.481 | 1.7% | 186.6 |
| Ethyl acetate | 3.537 | −0.005128 | 2.484 | 0.1% | 0.299 | −0.017324 | 0.042 | 0.9% | 111.8 |
| Acetonitrile | 33.160 | −0.004736 | 5.434 | 0.2% | 1.737 | −0.014391 | 0.207 | 0.6% | 133.8 |
| 2 m-THF | 4.642 | −0.004662 | 1.673 | 0.2% | 0.289 | −0.014894 | 0.024 | 0.8% | 145.2 |
| Acetone | 22.997 | −0.004106 | −0.936 | 0.3% | 1.036 | −0.013575 | 0.059 | 0.8% | 115.4 |

Note: "γ-Valeractone" and "2 m-THF" are transcribed exactly as printed in the table (the paper's body text and Fig. 6 caption area otherwise use "γ-Valerolactone" [ref. 55] and "2-methyltetrahydrofuran" [ref. 52] for the same compounds; the table header abbreviations are reproduced as-is rather than expanded).

### Table 2 - Regressed parameters for alcohols fitted to Eq. (2) [SRC-0095, Table 2]

$B_1$-$B_4$, $\sigma$, $\mu$: fit parameters (Eq. 2); Error: standard error relative to the mean; $T_{\mathrm{MAX}}$: maximum temperature measured (°C). Reported separately for dielectric constant ($\varepsilon'$) and loss factor ($\varepsilon''$).

**Dielectric constant $\varepsilon'$ [-]**

| Solvent | $B_1$ | $B_2$ | $B_3$ | $B_4$ | $\sigma$ | $\mu$ | Error | $T_{\mathrm{MAX}}$ (°C) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Ethanol | 112.82 | 169.75 | 6.846 | 5.167 | 0.23079 | 0.25746 | 0.6% | 140.0 |
| Methanol | 17.572 | 195.77 | 36.847 | 0.8127 | 1.01634 | 0.00305 | 0.2% | 111.5 |
| Isopropanol | 89.533 | 137.39 | 4.275 | 3.681 | 0.20388 | 0.35941 | 0.8% | 133.0 |
| 2-Pentanol | 27.006 | 108.26 | 3.239 | 3.102 | 0.33902 | 0.30006 | 1.1% | 172.1 |

**Loss factor $\varepsilon''$ [-]**

| Solvent | $B_1$ | $B_2$ | $B_3$ | $B_4$ | $\sigma$ | $\mu$ | Error | $T_{\mathrm{MAX}}$ (°C) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Ethanol | 177.08 | 193.78 | 4.516 | 0.106 | 0.17261 | 0.17374 | 1.0% | 140.0 |
| Methanol | 315.885 | 754.41 | 2645.101 | 0.0000 | 0.53719 | −2.59687 | 0.8% | 111.5 |
| Isopropanol | 561.926 | 324.10 | 1.352 | 0.317 | 0.05364 | 0.65545 | 2.6% | 133.0 |
| 2-Pentanol | 313.805 | 288.81 | 0.752 | 0.109 | 0.08754 | 0.27231 | 3.4% | 172.1 |

### Table 3 - Regressed parameters for HCl solutions fitted to Eq. (2) [SRC-0095, Table 3]

Same parameter meanings as Table 2. "Solution" rows are pure water and five HCl solutions of decreasing pH (increasing acid strength): pH 2.5, 2.0, 1.6, 1.3, 1.0.

**Dielectric constant $\varepsilon'$ [-]**

| Solution | $B_1$ | $B_2$ | $B_3$ | $B_4$ | $\sigma$ | $\mu$ | Error | $T_{\mathrm{MAX}}$ (°C) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Water | 328.07 | 440.42 | 50.052 | 20.425 | 0.4137 | −0.35783 | 0.3% | 161.5 |
| pH 2.5 | 100.153 | 251.06 | 133.19 | 0.4520 | 1.1311 | 0.00290 | 0.2% | 165.4 |
| pH 2.0 | 257.88 | 527.20 | 64.293 | 4.604 | 0.6550 | −0.63567 | 0.3% | 164.0 |
| pH 1.6 | 254.28 | 437.25 | 103.07 | −4.812 | 0.7801 | −0.32871 | 0.2% | 162.1 |
| pH 1.3 | 170.802 | 93.591 | 22.15 | 61.793 | 0.2754 | 0.61419 | 0.2% | 161.3 |
| pH 1.0 | 3.389 | 100.943 | −7.424 | 76.750 | 0.7132 | 0.21673 | 0.1% | 163.3 |

**Loss factor $\varepsilon''$ [-]**

| Solution | $B_1$ | $B_2$ | $B_3$ | $B_4$ | $\sigma$ | $\mu$ | Error | $T_{\mathrm{MAX}}$ (°C) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Water | 76.014 | 84.415 | 61.390 | 0.24264 | 0.8689 | −1.1598 | 3.0% | 161.5 |
| pH 2.5 | 37.13 | 10,586.3 | 2630.04 | 2.4934 | 13.5644 | −58.4632 | 1.1% | 165.4 |
| pH 2.0 | 5.0850 | 253.13 | −37.596 | 23.493 | 1.6017 | 0.9550 | 0.7% | 164.0 |
| pH 1.6 | 49.807 | 765.6 | −177.51 | 93.607 | 1.8130 | 0.9576 | 0.3% | 162.1 |
| pH 1.3 | −0.12798 | 246.07 | 15.783 | 20.938 | 0.7880 | 0.2661 | 0.4% | 161.3 |
| pH 1.0 | −0.12801 | 218.71 | 8.8847 | 26.337 | 0.9260 | 0.2853 | 0.3% | 163.3 |

Note: pH 2.5's loss-factor fit parameters ($B_2=10{,}586.3$, $B_3=2630.04$, $\sigma=13.5644$, $\mu=-58.4632$) are far outside the range of any other row in Tables 2-3; they are transcribed exactly as printed and verified twice against the high-resolution render (see verification note below). The paper reports this fit's standard error as only 1.1%, so the large parameter magnitudes are plausibly an artifact of this particular fit's parameterization (e.g., a near-degenerate combination of $B_2$, $B_3$, $\sigma$, $\mu$ in the lognormal form) rather than a transcription error, but this is not independently confirmed from the paper alone.

### Figures with data not captured in the tables

The following figures show measured or literature-comparison data not reproduced as exact numeric tables in this PDF; curve/point values were not digitized, only the figures' existence and content are recorded:

- Fig. 2: frequency-shift contour maps for the designed bireentrant cavity loaded with quartz (a) or alumina (b) tubes, as a function of material $\varepsilon'$ and $\varepsilon''$, with resonant-frequency contours at 0.1 GHz increments; this is cavity calibration/design data (simulated response), not a measured material property. [SRC-0095, Fig. 2]
- Fig. 4: measured temperature-dependent $\varepsilon'$ and $\varepsilon''$ of water at 1.85 GHz from 20-160 °C, overlaid with Kaatze's (1989) Debye-model values up to 60 °C, used as the method's primary temperature validation. [SRC-0095, Fig. 4]
- Fig. 5: parity plot of measured vs. literature room-temperature $\varepsilon'$ for non-alcohol organics, alcohols, and water (literature values from refs. 49-59), log-log scale, $\varepsilon'\approx1$-100; no per-point numeric table is given. [SRC-0095, Fig. 5]
- Fig. 6: example temperature-dependent $\varepsilon'$/$\varepsilon''$ curves (with Eq. 1 fit overlays) for MIBK (a) and ethyl acetate (b); the full set of non-alcohol-organic raw data points is stated to be in Supplementary Figs. S3-S4 (not in this PDF) — only the Table 1 fit parameters are available here. [SRC-0095, Fig. 6]
- Fig. 7: example temperature-dependent $\varepsilon'$/$\varepsilon''$ curves (with Eq. 2 fit overlays) for ethanol (a) and isopropanol (b); the full alcohol raw dataset is stated to be in Supplementary Fig. S5 (not in this PDF) — only the Table 2 fit parameters are available here. [SRC-0095, Fig. 7]
- Fig. 8: temperature-dependent $\varepsilon'$ (a) and $\varepsilon''$ (b) curves for water and five HCl solutions (pH 1.0, 1.3, 1.6, 2.0, 2.5); no raw per-point table or supplementary figure is referenced for this dataset in the main text — only the Table 3 fit parameters are available. [SRC-0095, Fig. 8]

## Limitations and caveats

- The tabulated data (Tables 1-3) are regressed curve-fit parameters, not raw measured values; reconstructing a predicted $\varepsilon'(T)$ or $\varepsilon''(T)$ at a specific temperature requires evaluating Eq. 1 or Eq. 2 with the tabulated parameters, introducing the fit's own standard error (up to 4% for HCl $\varepsilon''$ fits) in addition to any underlying measurement uncertainty. [SRC-0095, Tables 1-3]
- The method is explicitly non-traceable (unlike the Dimitrakis et al. 2009 VNA-based reference system) and is limited to a moderate maximum pressure (~7 bar), which bounds the accessible temperature range for each liquid. [SRC-0095, Results]
- Measurements are taken while the heated, sealed vial cools rather than under externally controlled, fixed pressure at each temperature; pressure at each point equals the sample's own vapor pressure at that temperature. The paper argues (citing Dimitrakis et al. 2009) that this does not measurably affect alcohol permittivity for 1-60 bar, but this was not independently re-verified for the specific solvents in this paper. [SRC-0095, Methods]
- No replicate count, averaging protocol, or sample purity/grade information is given in the main text for any of the 9 organic solvents, 4 alcohols, or 6 HCl solutions; this level of detail may exist only in the Supplementary Information, which is not part of the ingested PDF. [SRC-0095]
- Literature comparison for solvents at elevated temperature (beyond the room-temperature parity check, Fig. 5) could not be performed because the authors found no literature data at matching frequency and temperature. [SRC-0095, Results]
- The pH-2.5 HCl loss-factor fit (Table 3) has fit-parameter magnitudes far outside the range of every other row in Tables 2-3, despite a low (1.1%) reported fit error; this is recorded as a known oddity rather than resolved (see Table 3 note above).

## Open questions

- Whether the lognormal-fit parameters for alcohols and HCl solutions (Tables 2-3) are stable/identifiable (i.e., not strongly correlated or near-degenerate) is not discussed; the very large pH-2.5 $\varepsilon''$ fit parameters suggest at least one fit may be poorly conditioned despite a low reported error. [Synthesis, not stated in the source]
- The paper's own stated novel finding — that ionic strength (HCl concentration) can reverse the sign of $d\varepsilon''/dT$ — is not given a mechanistic explanation beyond the general observation; whether this generalizes to other strong-acid or ionic-strength systems is not addressed. [SRC-0095, Results]

## Links

No existing SecondBrain concept, entity, claim, question, or tension page addresses dielectric permittivity measurement methodology, water/alcohol/HCl dielectric behavior, or microwave cavity instrumentation; [[wiki/sources/SRC-0094-investigation-of-microwave-dielectric-properties-of-biodiesel-components]] is the only existing source sharing this topic area (same measured observable, complex dielectric permittivity $\varepsilon'-j\varepsilon''$, and the same 2.45 GHz ISM design frequency), though the two papers use unrelated instruments (open-ended coaxial probe + VNA vs. a resonant bireentrant cavity + reflectometer) and study different materials (biodiesel precursors vs. water/alcohols/HCl). [Synthesis, not stated in either source]

- [[wiki/sources/SRC-0094-investigation-of-microwave-dielectric-properties-of-biodiesel-components]]
- [[wiki/sources/SRC-0096-traceable-measurements-of-the-static-permittivity-of-dielectric]]
- [[wiki/claims/CLM-0054-alcohols-show-non-monotonic-dielectric-permittivity-temperature-dependence]]
- [[wiki/claims/CLM-0055-hcl-ionic-strength-reverses-loss-factor-temperature-trend]]

## Metadata notes

- The article identifies Montgomery Baker-Fales and Dionisios G. Vlachos (University of Delaware, Department of Chemical and Biomolecular Engineering; RAPID Manufacturing Institute / Delaware Energy Institute), and José D. Gutiérrez-Cano and José M. Catalá-Civera (Institute of Information and Communication Technologies (ITACA), Universitat Politècnica de València); Scientific Reports 13, 18171 (2023); DOI `10.1038/s41598-023-45049-8`. Received 8 July 2023, accepted 15 October 2023, published online 24 October 2023. Open access (CC BY 4.0).
- Supplementary Information exists online (Figs. S1-S5, Table S1) but is not part of the ingested 10-page PDF (confirmed via `pdfinfo`: 10 pages); its contents (raw per-temperature datasets, vial dimensions, quartz-vs-alumina comparison, literature-source table) are referenced but not transcribed here. If the Supplementary Information is later supplied, it should be ingested as a separate `SRC-XXXX` bundle member with `bundle_role: supplement`, linked back to this page.
- Bibliography (60 references) was inspected; it is specific to microwave reactor engineering, cavity/EM measurement methods, and individual solvent property references (e.g., Kaatze 1989, Dimitrakis et al. 2009, Gutiérrez-Cano et al. 2020), and does not overlap with any already-ingested SecondBrain source, including [[wiki/sources/SRC-0094-investigation-of-microwave-dielectric-properties-of-biodiesel-components]] (not cited) or the alcohol-structure diffraction papers SRC-0092/SRC-0093 (not cited; different subfield).
- Reference 57 of this paper's bibliography ("Gregory, A P & Clarke, R N. Tables of the complex permittivity of dielectric reference liquids at frequencies up to 5 GHz; NPL") is a companion NPL report (CETM 33, 2001) by the same two authors as [[wiki/sources/SRC-0096-traceable-measurements-of-the-static-permittivity-of-dielectric]], not the SRC-0096 journal article itself (which is cited as ref. [6] within SRC-0096's own bibliography). Per the citation-matching convention (title/author/year must match the specific document), this is recorded as a related-but-distinct reference rather than a `cites_sources` entry. SRC-0096 and this paper both report water, methanol and ethanol permittivity, at 0.1-1.0 MHz ("static" limit) versus ~1.85-2.45 GHz respectively; see SRC-0096's "Cross-source comparison" section for why a direct numeric comparison was not performed.
- Categorization: filed under `research/experimental-benchmarking`, matching the user's stated purpose of collecting experimental dielectric-property data for benchmarking (same rationale as SRC-0094).
- No author entity pages were created; none of the four authors appears elsewhere in SecondBrain.

## Ingestion QA

### Retrieval questions checked

- What is the central contribution? A simplified, non-traceable benchtop method (bireentrant cavity + reflectometer + pressurized alumina/quartz vial) for measuring temperature-dependent complex dielectric permittivity of liquids near 2.45 GHz up to 7 bar, plus new permittivity datasets (as curve-fit parameters) for water, alcohols, non-alcohol organics, and HCl solutions. [SRC-0095, abstract]
- What problem does it address? The scarcity of accessible temperature/pressure-resolved liquid dielectric datasets needed for microwave reactor design and simulation, given that existing traceable high-T/P systems require uncommon lab equipment. [SRC-0095, Introduction]
- What methods were used? A single-post bireentrant MW cavity with EM mode-matching/circuit model (no reference-material calibration needed), alumina/quartz PTD vessels sealed to 7 bar with optical-fiber temperature sensing, heated externally and measured while cooling. [SRC-0095, Methods]
- What are the key quantitative results? Non-alcohol organics (9 solvents) fit an exponential decay in $\varepsilon'$, $\varepsilon''$ vs. T (Table 1); alcohols (4) and HCl solutions (6, incl. water) show non-monotonic rise-then-fall behavior fit by a 6-parameter lognormal (Tables 2-3); water/room-T solvent validation shows close agreement with literature (5.8% average error for room-T $\varepsilon'$). [SRC-0095, Tables 1-3, Results]
- What are the limitations? Non-traceable method, ≤7 bar pressure ceiling, tabulated values are fit parameters (not raw data, which are in an unincluded Supplementary Information), no stated replicate/purity protocol in the main text, and one HCl fit (pH 2.5, $\varepsilon''$) has unusually large parameter magnitudes. [SRC-0095, Results, Tables 1-3]
- What should not be overgeneralized? The specific fit parameters are tied to each named solvent/solution and its measured $T_{\mathrm{MAX}}$; the HCl results are specific to the stated pH values (1.0-2.5) and should not be extrapolated to arbitrary acid concentrations or other electrolytes without further validation. [SRC-0095]
- Does this connect to existing SecondBrain content? Yes, topically, to [[wiki/sources/SRC-0094-investigation-of-microwave-dielectric-properties-of-biodiesel-components]] (same dielectric-permittivity observable and 2.45 GHz design frequency), though via a different instrument and different materials; no bibliographic citation link exists between the two papers. [Synthesis, not stated in either source]

### Coverage decision

Complete at `coverage_profile: math-standard`. Both equations (Eq. 1, Eq. 2), their variable definitions, the central experimental findings for all three solvent classes (non-alcohol organics, alcohols, HCl solutions), full numeric transcriptions of Tables 1-3 (independently re-verified against 350-dpi page renders), the measurement/reuse conditions, the untabulated figures, limitations, and open questions are represented.

### Known gaps

- The paper's raw per-temperature dielectric data points (as opposed to the regressed fit parameters reported in Tables 1-3) are stated to reside in Supplementary Figs. S3-S5 and Table S1, which are not part of the ingested PDF and so could not be transcribed or verified.
- The pH 2.5 HCl loss-factor fit's unusually large parameter magnitudes (Table 3) are recorded as a known oddity; the paper gives no discussion of fit conditioning or parameter correlation that would resolve whether this reflects a genuine feature of the data or a fit artifact.
- No source bundle (e.g., the Supplementary Information) was available for ingestion; the article is ingested alone.
