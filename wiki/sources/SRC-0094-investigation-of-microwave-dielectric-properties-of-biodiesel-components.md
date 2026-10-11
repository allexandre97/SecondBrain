---
type: source
status: active
created: 2026-10-01
updated: 2026-10-01
source_id: SRC-0094
display_title: "Investigation of Microwave Dielectric Properties of Biodiesel Components"
short_title: "Muley & Boldor Biodiesel Dielectric Properties"
aliases:
  - "SRC-0094"
  - "Muley and Boldor 2013"
  - "Investigation of Microwave Dielectric Properties of Biodiesel Components"
source_path: raw/sources/SRC-0094-investigation-of-microwave-dielectric-properties-of-biodiesel-components.pdf
imported_path: raw/sources/SRC-0094-investigation-of-microwave-dielectric-properties-of-biodiesel-components.pdf
original_filename: "1-s2.0-S0960852412015106-main.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 9208e26d66c45171bf47060496c9c0e486a0c89b2c0de10f0a01c950a3663fbb
authors:
  - "Pranjali D. Muley"
  - "Dorin Boldor"
author_entities: []
year: 2013
venue: "Bioresource Technology, 127, 165-174"
doi: "10.1016/j.biortech.2012.10.008"
arxiv:
metadata_review_status: reviewed
areas:
  - research
categories:
  - research/experimental-benchmarking
tags:
  - scientific-paper
  - biodiesel
  - transesterification
  - microwave-dielectric-heating
  - dielectric-constant
  - dielectric-loss
  - soybean-oil
  - ethanol
  - methanol
  - sodium-hydroxide-catalyst
related: []
sources:
  - SRC-0094
cites_sources: []
citation_match_status: reviewed
cqt_review_status: linked
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: math-standard
peer_review_status: peer-reviewed
---

# Investigation of Microwave Dielectric Properties of Biodiesel Components

Source ID: `SRC-0094`

## Raw source

- Repository path: `raw/sources/SRC-0094-investigation-of-microwave-dielectric-properties-of-biodiesel-components.pdf`
- Open raw source: [raw/sources/SRC-0094-investigation-of-microwave-dielectric-properties-of-biodiesel-components.pdf](../../raw/sources/SRC-0094-investigation-of-microwave-dielectric-properties-of-biodiesel-components.pdf)

## Summary

Muley and Boldor measure the complex dielectric permittivity ($\varepsilon' - j\varepsilon''$) of soybean oil, ethanol, methanol, and sodium hydroxide (NaOH)-catalyst mixtures, and of oil-alcohol-catalyst blends simulating a transesterification reaction, across 280 MHz-4.5 GHz and at 30/45/60/75 °C. [SRC-0094, abstract] The motivation is to supply dielectric-property data needed to design and optimize a microwave-assisted continuous-flow biodiesel (transesterification) process, since dielectric properties govern microwave field distribution, heating rate, and absorbed power. [SRC-0094, §1]

Two heating scenarios are compared: (1) oil mixed with the alcohol-catalyst solution at room temperature, then jointly heated to the target temperature (undergoing some reaction during heating), versus (2) oil and the alcohol-catalyst solution heated separately to the target temperature and mixed only immediately before measurement (minimal reaction). [SRC-0094, §2]

## Key points

- Soybean oil's dielectric constant ($\varepsilon'$) is low (2.8-3.2) and essentially unchanged by frequency and temperature; its dielectric loss ($\varepsilon''$) is negligible (max. 0.366 at 468 MHz) and decreases slightly with frequency. [SRC-0094, §3.1]
- Ethanol and methanol (both polar) show $\varepsilon'$ decreasing with frequency; methanol has higher $\varepsilon'$ than ethanol at a given frequency and temperature (methanol 18-31 vs. ethanol 6-21 over the measured range). $\varepsilon''$ peaks at a frequency that shifts higher as temperature increases (ethanol peak near 1000 MHz at 30 °C; methanol peak between 3000-4000 MHz at 30 °C). [SRC-0094, §3.2]
- Relaxation frequency (from $d\varepsilon''/df$) increases sharply with temperature: ethanol goes from 1005.6 MHz at 30 °C to 3749 MHz at 75 °C; methanol from 3463 MHz at 30 °C to 5830 MHz at 60 °C (not measured at 75 °C, above methanol's 68 °C boiling point). Derived viscosities from these relaxation frequencies agree closely with standard literature values for ethanol but diverge somewhat for methanol. [SRC-0094, §3.2.2, Table 1]
- Adding a very small amount of NaOH catalyst (0.18% by weight of oil; 0.066 g in 19.3 mL ethanol, or 0.091 g in 10.235 mL methanol) has a disproportionately large effect: $\varepsilon'$ decreases compared to pure alcohol, but $\varepsilon''$ increases substantially and its frequency dependence changes from a peaked curve (pure alcohol) to a monotonic asymptotic decrease, attributed to ionic conduction from the dissolved Na+/OH- ions. [SRC-0094, §3.3]
- Methanol+NaOH shows a much larger $\varepsilon''$ increase than ethanol+NaOH throughout the frequency range, implying methanol-catalyst mixtures would absorb microwave energy and heat faster than ethanol-catalyst mixtures at the same NaOH loading. [SRC-0094, §3.3.2, §4]
- For oil-alcohol-catalyst mixtures (modeling the reacting system), scenario 1 (mixed before heating, more reaction progress) gives higher $\varepsilon'$ and generally higher $\varepsilon''$ than scenario 2 (heated separately, then mixed, minimal reaction) at a given temperature, because unreacted ethanol/methanol and reaction intermediates (mono/diglycerides) are more polar than the biodiesel (fatty acid ester) product. [SRC-0094, §3.4]
- At FCC-allocated industrial/scientific/medical microwave frequencies (915 MHz and 2450 MHz), the paper tabulates $\varepsilon'$, $\varepsilon''$, and loss tangent for every pure component and mixture at each temperature (Tables 2-3), intended as direct design input since practical microwave systems are typically built only for these two frequencies. [SRC-0094, §3.3.1, §3.4.1, Tables 2-3]
- The authors recommend an operating frequency between 915 and 2450 MHz as a practical compromise, since it is impractical to build a variable-frequency system that tracks the material's temperature-dependent dielectric response. [SRC-0094, §3.2.2]

## Methods and evidence

Dielectric properties were measured with an Agilent ENA E5071C vector network analyzer and an Agilent 85070E open-ended coaxial slim-form probe kit (201-point frequency sweep, 280 MHz-4.5 GHz), calibrated at 25 °C with the 3-point (short-circuit/air/water) method. [SRC-0094, §2] Soybean oil (grocery-store), 200-proof ACS-grade ethanol and methanol, and anhydrous NaOH flakes were used; NaOH was fully dissolved in ethanol or methanol (0.18 wt% relative to oil) before mixing. Oil:ethanol ratio was 1:9 and oil:methanol ratio was 1:5 (by volume, following Kanitkar et al. 2011), both well above the 1:3 stoichiometric oil:alcohol ratio, so substantial unreacted alcohol remains at equilibrium (the paper calculates 6.0 mol unreacted ethanol remaining for the 1:9 oil:ethanol ratio). [SRC-0094, §2, §3.4.2] Measurements were triplicated, averaged, and reported with standard deviations (Excel 2010); plots were produced in SigmaPlot 10. [SRC-0094, §2]

Two mixing/heating protocols (scenario 1: mix oil with alcohol-catalyst solution at room temperature, then heat jointly; scenario 2: heat oil and alcohol-catalyst solution separately to target temperature, then mix immediately before measurement) were used to bound the dielectric behavior of the reacting mixture between "early reaction" and "minimal reaction" states. [SRC-0094, §2, §3.4]

## Key equations

Complex permittivity is defined as: [SRC-0094, eq. 1]

$$
\varepsilon = \varepsilon' - j\varepsilon''
$$

Relaxation time $\tau$ is related to solvent viscosity $\mu$, molecular gyration radius $r$, and absolute temperature $\mathrm{Temp}$ via: [SRC-0094, eq. 2]

$$
\tau = \frac{4\pi r^3 \mu}{k_b\, \mathrm{Temp}}
$$

Microwave power absorbed per unit volume depends on conductivity $\sigma$ (or equivalently on $\varepsilon''$), frequency $f$, and electric field intensity $E$: [SRC-0094, eq. 3]

$$
P_{\mathrm{abs}} = \sigma E^2 = 2\pi f \varepsilon_0 \varepsilon'' E^2
$$

### Variable glossary

- $\varepsilon'$: dielectric constant (energy storage); $\varepsilon''$: dielectric loss factor (thermal/heat conversion).
- $\tau$: relaxation time (s); $r$: molecular gyration radius (m); $\mu$: solvent viscosity (Pa·s); $k_b$: Boltzmann constant.
- $P_{\mathrm{abs}}$: absorbed microwave power density (W/m$^3$); $\sigma$: conductivity (S/m); $f$: frequency (Hz); $\varepsilon_0$: vacuum permittivity; $E$: electric field intensity (V/m).

### Equation inventory

| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |
| Complex permittivity | SRC-0094, eq. 1, p. 166 | This page | Defines $\varepsilon'$/$\varepsilon''$ decomposition used throughout. | $\varepsilon$, $\varepsilon'$, $\varepsilon''$ | Basic definition for interpreting all reported data. |
| Relaxation time from viscosity | SRC-0094, eq. 2, p. 166 | This page | Links measured relaxation frequency to solvent viscosity. | $\tau$, $r$, $\mu$, $\mathrm{Temp}$, $k_b$ | Used to cross-check derived viscosities against literature (Table 1). |
| Absorbed microwave power | SRC-0094, eq. 3, p. 166 | This page | Links $\varepsilon''$ to volumetric microwave heating rate. | $P_{\mathrm{abs}}$, $\sigma$, $f$, $\varepsilon_0$, $\varepsilon''$, $E$ | Central design equation for sizing/optimizing microwave reactors from the measured $\varepsilon''$ tables. |

No further mathematical structure (e.g., mixing-rule derivations) is reproduced; the paper explicitly declines to apply standard dielectric mixing rules (Bruggeman, Landau-Lifshitz-Looyenga, etc.) to this reacting multicomponent system because too many time-varying parameters (composition, density, temperature) would need to be tracked. [SRC-0094, §1]

## Data tables

Full numeric transcription of the paper's three summary tables, for reuse as experimental benchmark data. Values and uncertainties are transcribed exactly as printed; `-NA-` reproduces the paper's own marker for values not measured (methanol was not measured at 75 °C because it is above methanol's 68 °C boiling point). Values were verified by independently re-reading high-resolution renders of each table page a second time after first transcription; no digit remained illegible. Two likely source-side anomalies were found and are reported as printed rather than silently corrected (see notes under each table).

### Measurement conditions (for reuse)

- Instrument: Agilent ENA E5071C vector network analyzer with an Agilent 85070E dielectric probe kit, slim-form open-ended coaxial probe method. [SRC-0094, §2]
- Frequency grid: 201-point sweep from 280 MHz to 4.5 GHz; the paper does not state whether point spacing is linear or logarithmic. [SRC-0094, §2]
- Calibration: 3-point method (short-circuit, air, water), performed at 25 °C. [SRC-0094, §2]
- Temperature control: constant-temperature water bath at nominal set points 30, 45, 60, 75 °C; methanol-containing samples (pure methanol, methanol+NaOH, oil+methanol+NaOH) were only measured up to 60 °C because methanol boils at 68 °C. [SRC-0094, §2]
- Replication and reported precision: each sample was measured in triplicate; all tabulated values are the triplicate mean ± standard deviation. Data were processed in Excel 2010 and plotted in SigmaPlot 10. Table 1's relaxation frequencies are derived quantities (the frequency at which $d\varepsilon''/df$ is extremal, Fig. 3), not direct instrument readings. [SRC-0094, §2, §3.2.2]
- Sample composition: oil = soybean oil (grocery-store, uncharacterized fatty-acid profile); ethanol and methanol = 200-proof, ACS grade; catalyst = anhydrous NaOH flakes, 0.18 wt% relative to the oil, fully dissolved in the alcohol before mixing with oil (0.066 g NaOH in 19.3 mL ethanol; 0.091 g NaOH in 10.235 mL methanol). Oil:ethanol volume ratio 1:9; oil:methanol volume ratio 1:5 (both above the 1:3 stoichiometric oil:alcohol ratio). Scenario 1 = oil mixed with the alcohol-catalyst solution at room temperature, then heated together to the target temperature (more reaction progress); Scenario 2 = oil and the alcohol-catalyst solution heated separately to the target temperature, then mixed immediately before measurement (minimal reaction progress). [SRC-0094, §2, §3.4]

### Table 1 - Relaxation time and viscosity of ethanol and methanol at different temperatures [SRC-0094, Table 1]

Ethanol: molecular radius $r = 4.8\times10^{-10}$ m. Methanol: $r = 2.65\times10^{-10}$ m. Relaxation frequency and time are derived from the first derivative of $\varepsilon''$ with respect to frequency (Fig. 3); viscosity is back-calculated from the relaxation time via eq. 2 and compared with standard literature viscosity.

| Solvent | Temperature (K) | Relaxation frequency (MHz) | Relaxation time (s) | Viscosity, this study (cP) | Viscosity, literature (cP) |
| --- | --- | --- | --- | --- | --- |
| Ethanol | 303.15 | 1005.6 | $1.58\times10^{-10}$ | 0.2 | 0.1 |
| Ethanol | 318.15 | 1540 | $1.03\times10^{-10}$ | 0.1 | 0.09 |
| Ethanol | 333.15 | 2378 | $6.69\times10^{-11}$ | 0.13 | 0.06 |
| Ethanol | 348.15 | 3749 | $4.24\times10^{-11}$ | 0.08 | 0.05 |
| Methanol | 303.15 | 3463 | $4.59\times10^{-10}$ | 0.013 | 0.05 |
| Methanol | 318.15 | 4231 | $3.76\times10^{-10}$ | 0.012 | 0.04 |
| Methanol | 333.15 | 5830 | $2.73\times10^{-10}$ | 0.01 | 0.03 |
| Methanol | 348.15 | -NA- | -NA- | -NA- | -NA- |

### Table 2 - Dielectric constant and dielectric loss of pure components and alcohol+NaOH mixtures at 915 and 2450 MHz [SRC-0094, Table 2]

$\varepsilon'$ = dielectric constant, $\varepsilon''$ = dielectric loss, Tan $\delta$ = loss tangent ($\varepsilon''/\varepsilon'$). "Ethanol + NaOH" and "Methanol + NaOH" are the alcohol-catalyst solutions (no oil). All values are mean ± standard deviation of triplicate measurements.

| Component | Temperature | $\varepsilon'$ (915 MHz) | $\varepsilon''$ (915 MHz) | Tan $\delta$ (915 MHz) | $\varepsilon'$ (2450 MHz) | $\varepsilon''$ (2450 MHz) | Tan $\delta$ (2450 MHz) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Soybean oil | 30 °C | 2.90 ± 0.01 | 0.23 ± 0.0001 | 0.079 | 2.86 ± 0.03 | 0.10 ± 0.003 | 0.035 |
| Soybean oil | 45 °C | 2.97 ± 0.01 | 0.28 ± 0.006 | 0.096 | 2.85 ± 0.02 | 0.14 ± 0.003 | 0.052 |
| Soybean oil | 60 °C | 2.99 ± 0.03 | 0.28 ± 0.007 | 0.094 | 2.95 ± 0.04 | 0.14 ± 0.007 | 0.049 |
| Soybean oil | 75 °C | 2.85 ± 0.21 | 0.21 ± 0.01 | 0.075 | 2.81 ± 0.05 | 0.11 ± 0.009 | 0.040 |
| Ethanol | 30 °C | 15.85 ± 0.18 | 9.54 ± 0.11 | 0.602 | 8.21 ± 0.11 | 6.83 ± 0.08 | 0.831 |
| Ethanol | 45 °C | 17.68 ± 0.14 | 7.57 ± 0.25 | 0.428 | 10.02 ± 0.02 | 7.63 ± 0.03 | 0.762 |
| Ethanol | 60 °C | 18.22 ± 0.04 | 5.06 ± 0.06 | 0.278 | 13.01 ± 0.05 | 7.32 ± 0.02 | 0.562 |
| Ethanol | 75 °C | 18.35 ± 0.05 | 3.63 ± 0.07 | 0.198 | 14.98 ± 0.04 | 6.20 ± 0.08 | 0.413 |
| Methanol | 30 °C | 29.51 ± 0.14 | 6.55 ± 0.16 | 0.222 | 23.03 ± 0.04 | 11.56 ± 0.13 | 0.502 |
| Methanol | 45 °C | 28.34 ± 0.26 | 4.63 ± 0.22 | 0.163 | 24.33 ± 0.03 | 9.13 ± 0.02 | 0.375 |
| Methanol | 60 °C | 26.84 ± 0.39 | 3.30 ± 0.10 | 0.123 | 24.25 ± 0.04 | 6.95 ± 0.02 | 0.286 |
| Methanol | 75 °C | -NA- | -NA- | -NA- | -NA- | -NA- | -NA- |
| Ethanol + NaOH | 30 °C | 13.57 ± 0.28 | 11.04 ± 0.09 | 0.814 | 7.03 ± 0.08 | 6.95 ± 0.11 | 0.988 |
| Ethanol + NaOH | 45 °C | 15.76 ± 0.27 | 10.25 ± 0.25 | 0.650 | 8.97 ± 0.03 | 7.96 ± 0.27 | 0.888 |
| Ethanol + NaOH | 60 °C | 16.50 ± 0.01 | 8.41 ± 0.06 | 0.509 | 11.39 ± 0.03 | 8.06 ± 0.02 | 0.707 |
| Ethanol + NaOH | 75 °C | 16.32 ± 0.08 | 6.92 ± 0.048 | 0.424 | 13.04 ± 0.06 | 6.89 ± 005 [sic] | 0.528 |
| Methanol + NaOH | 30 °C | 23.34 ± 0.15 | 27.12 ± 0.32 | 1.162 | 17.99 ± 0.05 | 16.24 ± 0.002 | 0.903 |
| Methanol + NaOH | 45 °C | 21.84 ± 0.03 | 30.42 ± 0.48 | 1.392 | 19.10 ± 0.12 | 16.32 ± 0.07 | 0.854 |
| Methanol + NaOH | 60 °C | 20.80 ± 0.03 | 34.18 ± 0.21 | 1.643 | 19.22 ± 0.01 | 16.74 ± 0.02 | 0.871 |
| Methanol + NaOH | 75 °C | -NA- | -NA- | -NA- | -NA- | -NA- | -NA- |

`[sic]` note: the printed uncertainty on Ethanol+NaOH's $\varepsilon''$ at 2450 MHz, 75 °C reads "± 005" with no decimal point in the original table; it is almost certainly a typesetting omission for "± 0.05" (consistent with the magnitude of neighboring uncertainties in that column), but is transcribed exactly as printed rather than silently corrected.

### Table 3 - Dielectric constant and dielectric loss of oil-alcohol-catalyst mixtures at 915 and 2450 MHz, Scenarios 1 and 2 [SRC-0094, Table 3]

No Tan $\delta$ column is given in this table. Scenario 1 = mixed before heating (more reaction progress); Scenario 2 = heated separately then mixed (minimal reaction progress). Methanol-containing mixtures have no 75 °C row (methanol not measured above 60 °C, as in Table 2).

| Component | Temperature (°C) | $\varepsilon'$ (915 MHz) | $\varepsilon''$ (915 MHz) | $\varepsilon'$ (2450 MHz) | $\varepsilon''$ (2450 MHz) |
| --- | --- | --- | --- | --- | --- |
| Oil + EtOH − NaOH, Scenario 1 | 30 | 15.78 ± 0.13 | 11.55 ± 0.09 | 8.38 ± 0.07 | 7.65 ± 0.09 |
| Oil + EtOH − NaOH, Scenario 1 | 45 | 12.23 ± 1.64 | 6.90 ± 1.56 | 6.98 ± 0.07 | 5.70 ± 0.1 |
| Oil + EtOH − NaOH, Scenario 1 | 60 | 11.19 ± 0.01 | 3.38 ± 0.03 | 8.47 ± 0.04 | 3.93 ± 0.03 |
| Oil + EtOH − NaOH, Scenario 1 | 75 | 8.13 ± 0.33 | 1.58 ± 0.18 | 7.94 ± 0.18 | 2.77 ± 0.02 |
| Oil + EtOH − NaOH, Scenario 2 | 30 | 9.13 ± 0.17 | 5.00 ± 0.23 | 5.72 ± 0.08 | 3.46 ± 0.01 |
| Oil + EtOH − NaOH, Scenario 2 | 45 | 5.61 ± 0.09 | 1.97 ± 0.05 | 4.47 ± 0.06 | 1.75 ± 0.02 |
| Oil + EtOH − NaOH, Scenario 2 | 60 | 5.88 ± 0.05 | 0.94 ± 0.01 | 5.25 ± 0.03 | 1.08 ± 0.01 |
| Oil + EtOH − NaOH, Scenario 2 | 75 | 6.20 ± 0.007 | 0.72 ± 0.02 | 5.61 ± 0.02 | 0.85 ± 0.01 |
| Oil + MeOH + NaOH, Scenario 1 | 30 | 18.61 ± 0.08 | 21.03 ± 0.18 [see note] | 21.03 ± 0.05 [see note] | 12.38 ± 0.03 |
| Oil + MeOH + NaOH, Scenario 1 | 45 | 19.84 ± 2.3 | 26.40 ± 4.32 [see note] | 26.40 ± 0.24 [see note] | 14.28 ± 0.24 |
| Oil + MeOH + NaOH, Scenario 1 | 60 | 10.55 ± 0.56 | 19.43 ± 2.0 [see note] | 19.43 ± 0.75 [see note] | 9.43 ± 0.99 |
| Oil + MeOH + NaOH, Scenario 2 | 30 | 11.11 ± 0.16 | 12.05 ± 0.39 | 8.81 ± 0.17 | 6.75 ± 0.1 |
| Oil + MeOH + NaOH, Scenario 2 | 45 | 15.64 ± 0.19 | 22.43 ± 0.91 | 13.34 ± 0.33 | 11.69 ± 0.41 |
| Oil + MeOH + NaOH, Scenario 2 | 60 | 14.38 ± 0.09 | 22.75 ± 0.02 | 12.65 ± 0.9 | 10.97 ± 0.1 |

`[see note]` anomaly: as printed, every "Oil + MeOH + NaOH, Scenario 1" row has an identical numeric value (differing only in its ± uncertainty) for $\varepsilon''$ at 915 MHz and $\varepsilon'$ at 2450 MHz (21.03 at 30 °C, 26.40 at 45 °C, 19.43 at 60 °C). This pattern appears in none of the other 13 rows of Table 3 (including the otherwise-parallel "Scenario 2" rows for the same mixture), which strongly suggests a column-alignment or copy-paste error in the original published table rather than a genuine physical coincidence. The values are transcribed exactly as printed; this is recorded as a likely source-data error rather than corrected, since the correct original value cannot be recovered from the paper alone.

### Figures with data not captured in the tables

The following figures show continuous dielectric-property curves across the full 280 MHz-4.5 GHz sweep, at temperatures and intermediate frequencies beyond the two frequencies (915, 2450 MHz) tabulated above. Curve values were not digitized; only the figures' existence and content are recorded here:

- Fig. 1: $\varepsilon'$ and $\varepsilon''$ of soybean oil vs. frequency at 30 and 75 °C (caption notes the 45/60 °C curves essentially overlap the ones shown). [SRC-0094, Fig. 1]
- Fig. 2: (a) $\varepsilon'$ of methanol and ethanol vs. frequency at 30/45/60/75 °C (ethanol) and 30/45/60 °C (methanol); (b) $\varepsilon''$ of ethanol vs. frequency at 30/45/60/75 °C; (c) $\varepsilon''$ of methanol vs. frequency at 30/45/60 °C. [SRC-0094, Fig. 2]
- Fig. 3: first derivative $d\varepsilon''/df$ vs. frequency for (a) ethanol (30/45/60/75 °C) and (b) methanol (30/45/60 °C) — the curves used to locate the relaxation frequencies reported in Table 1. [SRC-0094, Fig. 3]
- Fig. 4: (a) $\varepsilon'$ of ethanol+NaOH and methanol+NaOH vs. frequency at 30/45/60/75 °C (ethanol) and 30/45/60 °C (methanol); (b) $\varepsilon''$ of ethanol+NaOH vs. frequency; (c) $\varepsilon''$ of methanol+NaOH vs. frequency (note different y-axis scales between (b) and (c)). [SRC-0094, Fig. 4]
- Fig. 5: oil+ethanol+NaOH mixture vs. frequency: (a) $\varepsilon'$ Scenario 1; (b) $\varepsilon'$ Scenario 2; (c) $\varepsilon''$ Scenario 1; (d) $\varepsilon''$ Scenario 2; all at 30/45/60/75 °C. [SRC-0094, Fig. 5]
- Fig. 6: oil+methanol+NaOH mixture vs. frequency: (a) $\varepsilon'$ Scenario 1; (b) $\varepsilon'$ Scenario 2; (c) $\varepsilon''$ Scenario 1; (d) $\varepsilon''$ Scenario 2; all at 30/45/60 °C. [SRC-0094, Fig. 6]

## Limitations and caveats

- All mixtures are used as static proxies for different points along the transesterification reaction extent; no in-situ reaction extent (e.g., FAME conversion) was measured alongside the dielectric data, so the mapping from "scenario 1 vs. scenario 2" to actual conversion is qualitative. [SRC-0094, §2, §3.4]
- Methanol could not be measured at 75 °C because its boiling point (68 °C) is below that temperature. [SRC-0094, §2]
- The probe/instrument combination only supports frequencies above 200 MHz, so the lower-frequency behavior reported in some cited literature (down to $10^{-5}$ MHz) could not be directly compared across the full range. [SRC-0094, §3.1.1]
- The paper notes its measured relaxation-time-derived viscosity for methanol diverges from standard literature values, while ethanol's agrees closely; no explanation beyond general measurement uncertainty is offered. [SRC-0094, §3.2.2, Table 1]
- Soybean oil batches were purchased from a local grocery store (not a controlled/characterized feedstock), and compositional variability (fatty acid profile) is cited as a factor affecting $\varepsilon'$ in other literature but not independently verified here. [SRC-0094, §3.1.1]

## Open questions

- The paper does not report how closely its oil-alcohol-catalyst dielectric proxies track actual, independently measured FAME conversion over time; this would be needed to use the dielectric data as a real-time reaction-progress indicator rather than only as an a priori design input. [Synthesis, not stated in the source]
- Whether the same qualitative catalyst-driven $\varepsilon''$ increase (ionic conduction) holds for other common biodiesel catalysts (e.g., KOH, acid catalysts) is not addressed; only NaOH was tested. [SRC-0094, §2]

## Links

No existing SecondBrain concept, entity, claim, question, or tension pages address biodiesel production, transesterification, or microwave dielectric heating; this is the first source in that domain. [Synthesis, not stated in the source]

- [[wiki/claims/CLM-0053-naoh-catalyst-dissolution-sharply-increases-alcohol-dielectric-loss]]

## Metadata notes

- The article identifies Pranjali D. Muley and Dorin Boldor (LSU Agricultural Center / LSU Biological and Agricultural Engineering); Bioresource Technology 127 (2013) 165-174; DOI `10.1016/j.biortech.2012.10.008`. Received 25 June 2012, accepted 6 October 2012, available online 17 October 2012; journal issue dated 2013.
- The bibliography was inspected; none of its ~30 references matched an already-ingested SecondBrain source (the cited literature is specific to dielectric/biodiesel engineering, e.g. Kanitkar et al. 2011, Sorichetti 2011, Terigar et al. 2010, and does not overlap with SecondBrain's existing molecular-simulation/force-field or water-structure source set).
- Categorization: filed under `research/experimental-benchmarking`. This source is being ingested specifically to collect experimental dielectric-property data for benchmarking, so this category is the intended fit, not a fallback.
- No author entity pages were created for Muley or Boldor; neither appears elsewhere in SecondBrain, and this is their only ingested paper.

## Ingestion QA

### Retrieval questions checked

- What is the central contribution? A temperature- and frequency-resolved dielectric-property dataset (280 MHz-4.5 GHz, 30-75 °C) for soybean oil, ethanol, methanol, NaOH-catalyst solutions, and oil-alcohol-catalyst mixtures, intended for microwave-assisted biodiesel reactor design. [SRC-0094, abstract]
- What problem does it address? Lack of dielectric data needed to model/optimize microwave heating of the specific, complex, reacting precursor mixtures used in biodiesel transesterification. [SRC-0094, §1]
- What methods were used? Open-ended coaxial probe + vector network analyzer measurements, triplicated, at four temperatures and two oil-alcohol-catalyst mixing/heating protocols. [SRC-0094, §2]
- What are the key quantitative results? Oil: $\varepsilon'\approx2.8-3.2$, negligible $\varepsilon''$. Ethanol/methanol: $\varepsilon'$ 6-31 decreasing with frequency; methanol relaxation frequency (3463-5830 MHz) much higher than ethanol's (1005.6-3749 MHz). NaOH addition sharply raises $\varepsilon''$, especially for methanol. See Tables 1-3 for full values. [SRC-0094, §3, Tables 1-3]
- What are the limitations? Static reaction-extent proxies rather than in-situ conversion tracking; methanol not measured at 75 °C; only NaOH catalyst tested; grocery-store oil feedstock. [SRC-0094, §2-3]
- What should not be overgeneralized? Results are specific to soybean oil, ethanol/methanol, and NaOH at the stated concentrations and oil:alcohol ratios (1:9, 1:5); other feedstocks, alcohols, or catalysts are not covered. [SRC-0094]
- Does this connect to existing SecondBrain content? No direct connection found; this introduces biodiesel/microwave-dielectric-heating as a new, currently isolated topic area. [Synthesis, not stated in the source]

### Coverage decision

Complete at `coverage_profile: math-standard`. All three equations, the central experimental findings (oil, alcohols, alcohol-catalyst, and oil-alcohol-catalyst mixtures under both heating scenarios), full numeric transcriptions of Tables 1-3, the measurement conditions needed to reuse the data, the figures' untabulated curve content, limitations, and open questions are represented.

### Known gaps

- Figs. 1-6 show continuous dielectric-property curves across the full 280 MHz-4.5 GHz sweep and additional temperatures beyond the two frequencies (915, 2450 MHz) tabulated in Tables 2-3; these curves were not digitized (see "Figures with data not captured in the tables").
- Two likely source-side anomalies were found while transcribing and are preserved as printed rather than corrected: a missing decimal point in Table 2's Ethanol+NaOH, 75 °C, 2450 MHz $\varepsilon''$ uncertainty ("± 005"), and an apparent column-duplication error across all three "Oil + MeOH + NaOH, Scenario 1" rows in Table 3 (see notes under each table).
- No source bundle (e.g., supplementary data) was provided; the article is ingested alone.
