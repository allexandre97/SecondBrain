---
type: source
status: active
created: 2026-10-01
updated: 2026-10-01
source_id: SRC-0092
display_title: "Hydrogen Bonding in Liquid Methanol and Ethanol Determined by X-Ray Diffraction"
short_title: "Narten & Habenschuss Methanol/Ethanol X-Ray Diffraction"
aliases:
  - "SRC-0092"
  - "Narten and Habenschuss 1984"
  - "Hydrogen Bonding in Liquid Methanol and Ethanol Determined by X-Ray Diffraction"
source_path: raw/sources/SRC-0092-hydrogen-bonding-in-liquid-methanol-and-ethanol-determined.pdf
imported_path: raw/sources/SRC-0092-hydrogen-bonding-in-liquid-methanol-and-ethanol-determined.pdf
original_filename: "3387_1_online.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 4aa7a564d96152a3503c82e5e690aca458ee53c1ebd11707e23eade8b02f73ab
authors:
  - "A. H. Narten"
  - "A. Habenschuss"
author_entities: []
year: 1984
venue: "Journal of Chemical Physics, 80(7), 3387-3391"
doi: "10.1063/1.447093"
arxiv:
metadata_review_status: reviewed
areas:
  - research
categories:
  - research/experimental-benchmarking
  - research/molecular-simulation/force-fields
tags:
  - scientific-paper
  - x-ray-diffraction
  - hydrogen-bonding
  - methanol
  - ethanol
  - liquid-structure
  - radial-distribution-function
  - alcohols
related:
  - "[[wiki/concepts/tolerance-normalized-multi-observable-losses]]"
  - "[[wiki/answers/ffrefine-current-implementation-status]]"
  - "[[wiki/claims/CLM-0009-observable-fitting-needs-held-out-validation]]"
  - "[[wiki/sources/SRC-0093-the-structure-of-liquid-ethanol-a-neutron-diffraction]]"
  - "[[wiki/claims/CLM-0052-neutron-md-liquid-ethanol-winding-hydrogen-bonded-chains]]"
sources:
  - SRC-0092
cites_sources: []
citation_match_status: reviewed
cqt_review_status: linked
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: math-standard
peer_review_status: peer-reviewed
---

# Hydrogen Bonding in Liquid Methanol and Ethanol Determined by X-Ray Diffraction

Source ID: `SRC-0092`

## Raw source

- Repository path: `raw/sources/SRC-0092-hydrogen-bonding-in-liquid-methanol-and-ethanol-determined.pdf`
- Open raw source: [raw/sources/SRC-0092-hydrogen-bonding-in-liquid-methanol-and-ethanol-determined.pdf](../../raw/sources/SRC-0092-hydrogen-bonding-in-liquid-methanol-and-ethanol-determined.pdf)

## Summary

Narten and Habenschuss (Oak Ridge National Laboratory / Oak Ridge Associated Universities) report x-ray diffraction measurements of liquid methanol and ethanol at 20 °C and atmospheric pressure, covering scattering vectors $0.3<k<16\ \text{Å}^{-1}$. [SRC-0092, abstract, §II] They decompose the measured total structure function into intramolecular and intermolecular (distinct) parts, fit the intramolecular part to obtain bond geometry, and Fourier-invert the intermolecular part to obtain radial distribution functions. The central finding is a well-resolved intermolecular peak near 2.8 Å in the distinct radial distribution function $G_d(r)$, attributed to hydrogen-bonded hydroxyl groups, with an average coordination number near 1.8 OH···OH neighbors per hydroxyl group. [SRC-0092, §§III-IV] The authors interpret this as evidence that methanol and ethanol molecules associate into hydrogen-bonded chains rather than rings or a fully disordered liquid, while noting that this is an average, instantaneous-fluctuation-smoothed picture. [SRC-0092, §IV]

This is a short, self-contained experimental structural-chemistry paper (6 pages, one bundle, no appendices or supplementary material supplied).

## Key points

- Site number densities and isothermal compressibilities used in data reduction: methanol $\rho=0.02976\ \text{Å}^{-3}$, $\beta_T=1.21\times10^{-10}\ \text{Pa}^{-1}$; ethanol $\rho=0.03096\ \text{Å}^{-3}$, $\beta_T=1.11\times10^{-9}\ \text{Pa}^{-1}$. [SRC-0092, Table I]
- Intramolecular distances and rms deviations fitted from the large-$k$ structure function: C-O $r=1.437(2)$ Å, $l=0.064(2)$ Å; C-C $r=1.540(3)$ Å, $l=0.042(5)$ Å; non-bonded C···O (ethanol) $r=2.472(4)$ Å, $l=0.056(5)$ Å. [SRC-0092, Table II] The –OH, –CH₂–, and –CH₃ groups were each treated as a single scattering site; the C-O parameters were obtained from methanol data and then used to analyze ethanol's C-C and C···O parameters.
- The distinct structure function $H_d(k)$ (Table III, tabulated for $k=0$ to 16 Å⁻¹ for both liquids) was extrapolated to $H_d(0)$ using the isothermal compressibility, then Fourier-inverted to the radial distribution function $G_d(r)$ (Fig. 4).
- The intermolecular peak near 2.8 Å in $G_d(r)$ is absent in alkanes and is ascribed specifically to hydrogen-bonded hydroxyl groups; it is nearly completely resolved from other intermolecular contributions. [SRC-0092, §IV]
- Fitted hydrogen-bond parameters (Table IV): methanol $n=1.77(7)$ neighbors, $r=2.798(6)$ Å, $l=0.142(6)$ Å; ethanol $n=1.81(9)$ neighbors, $r=2.808(8)$ Å, $l=0.113(7)$ Å, obtained by least-squares fitting the large-$k$ part of $H_d(k)$ with coordination number as an additional parameter.
- Small-angle x-ray scattering studies (cited, not reproduced here) show $S(k\to0)$ for several alcohols matches the value computed from isothermal compressibility, supporting that large-scale density fluctuations are ordinary liquid-density fluctuations rather than evidence of large persistent clusters. [SRC-0092, §IV, ref. 26]
- The paper explicitly frames its results as an average structure: local, instantaneous configurations deviate substantially from the mean, and the inferred correlations (chain formation) are expected to extend only a few molecular diameters. [SRC-0092, §IV]

## Methods and evidence

X-ray diffraction used reflection geometry with monochromatic Mo $K_\alpha$ radiation ($\lambda=0.7107$ Å) over $0.3<k<16\ \text{Å}^{-1}$, with statistical errors kept below $\pm0.003$ in the structure functions. Standard corrections were applied for background, absorption, polarization, incoherent scattering, monochromator discrimination, and multiple scattering. [SRC-0092, §II] Methanol and ethanol were obtained from Aldrich Chemical Co. at >99 wt % purity. [SRC-0092, §II]

The total structure function $H(k)=H_m(k)+H_d(k)$ was decomposed into a molecular (intramolecular) part $H_m(k)$, modeled from intramolecular site-site distances with Gaussian rms-deviation damping, and a distinct (intermolecular) part $H_d(k)=H(k)-H_m(k)$. [SRC-0092, Eqs. 1-3] Fourier inversion of $H_d(k)$ (after compressibility-based extrapolation to $k=0$) gives the intermolecular radial distribution function $G_d(r)$. [SRC-0092, Eqs. 4-6]

## Mathematical structure

The normalized total structure function is $H(k)=M(k)[S(k)-S_s(k)]$, where $M(k)=[n^{-1}\sum_\alpha f_\alpha(k)]^{-2}$ normalizes by the mean scattering factor per site, $S(k)$ is the measured coherent scattering function, and $S_s(k)$ is the self-scattering from independent sites. [SRC-0092, Eqs. 1-2] The molecular structure function sums intramolecular site-pair contributions damped by a Gaussian rms-deviation factor; the distinct structure function sums intermolecular partial structure factors $a_{\alpha\gamma}(k)=\rho\hat h_{\alpha\gamma}(k)$, themselves the Fourier transform of intermolecular site-site pair correlation functions $h_{\alpha\gamma}(r)=g_{\alpha\gamma}(r)-1$. Fourier inversion of $H_d(k)$ yields a radial distribution function that is a weighted sum of site-site distribution functions modified by scattering-factor products, useful mainly for locating dominant site-site correlation peaks rather than resolving individual site-site functions. [SRC-0092, Eqs. 4-6]

## Key equations

Total structure function: [SRC-0092, Eq. 1]

$$
H(k) = H_m(k) + H_d(k) = M(k)\,[S(k) - S_s(k)].
$$

Normalization factor: [SRC-0092, Eq. 2]

$$
M(k) = \left[n^{-1}\sum_\alpha f_\alpha(k)\right]^{-2}.
$$

Molecular (intramolecular) structure function: [SRC-0092, Eq. 3]

$$
H_m(k) = M(k)\, n^{-1} \sum_\alpha \sum_{\gamma\neq\alpha} f_\alpha(k) f_\gamma(k)\, j_0(k r_{\alpha\gamma}) \exp\!\left(-l_{\alpha\gamma}^2 k^2 / 2\right).
$$

Distinct structure function in terms of partial structure functions: [SRC-0092, Eq. 4]

$$
H_d(k) = M(k) \sum_\alpha \sum_{\gamma \neq \alpha} f_\alpha(k) f_\gamma(k)\, a_{\alpha\gamma}(k).
$$

Partial structure function: [SRC-0092, Eq. 5]

$$
\hat h_{\alpha\gamma}(k) = 4\pi \int_0^\infty r^2\, h_{\alpha\gamma}(r)\, j_0(kr)\, dr, \qquad a_{\alpha\gamma}(k) = \rho\, \hat h_{\alpha\gamma}(k).
$$

Radial distribution function from Fourier inversion: [SRC-0092, Eq. 6]

$$
G_d(r) = 1 + (2\pi^2 \rho r)^{-1} \int_0^\infty k\, H_d(k) \sin(kr)\, dk.
$$

## Variable glossary

- $k = (4\pi/\lambda)\sin\theta$: scattering vector magnitude, with $\lambda$ the x-ray wavelength and $2\theta$ the scattering angle.
- $f_\alpha(k)$: x-ray scattering factor for site $\alpha$ (–OH, –CH₂–, or –CH₃ treated as a single site).
- $S(k)$, $S_s(k)$: measured coherent scattering function and independent-site self-scattering.
- $r_{\alpha\gamma}$, $l_{\alpha\gamma}$: intramolecular site-pair distance and its rms deviation.
- $\rho$: bulk site number density.
- $g_{\alpha\gamma}(r)$, $h_{\alpha\gamma}(r)$: intermolecular site-site pair correlation function and its deviation from unity.
- $j_0(x) = x^{-1}\sin x$: zeroth-order spherical Bessel function.
- $n$: average coordination number of hydrogen-bonded OH···OH neighbors per hydroxyl group (Table IV).

## Equation inventory

| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |
| Total structure function | SRC-0092, Eq. 1, p. 3388 | This page, Key equations | Defines the measured, normalized total structure function. | $H(k)$, $M(k)$, $S(k)$, $S_s(k)$ | Starting point for any reanalysis of the raw diffraction data. |
| Normalization factor | SRC-0092, Eq. 2, p. 3388 | This page, Key equations | Normalizes by mean per-site scattering factor. | $M(k)$, $f_\alpha(k)$ | Needed to reproduce normalized intensities. |
| Molecular structure function | SRC-0092, Eq. 3, p. 3388 | This page, Key equations | Models intramolecular contribution from bond geometry. | $H_m(k)$, $r_{\alpha\gamma}$, $l_{\alpha\gamma}$ | Basis for the fitted C-O/C-C/C···O bond parameters (Table II). |
| Distinct structure function | SRC-0092, Eq. 4, p. 3389 | This page, Key equations | Expresses the intermolecular part via partial structure functions. | $H_d(k)$, $a_{\alpha\gamma}(k)$ | Links reciprocal-space data to intermolecular pair correlations. |
| Partial structure function | SRC-0092, Eq. 5, p. 3389 | This page, Key equations | Fourier transform relating $h_{\alpha\gamma}(r)$ and $a_{\alpha\gamma}(k)$ | $\hat h_{\alpha\gamma}(k)$, $\rho$ | Standard liquid-structure Fourier-transform relation. |
| Radial distribution function | SRC-0092, Eq. 6, p. 3389 | This page, Key equations | Fourier-inverts $H_d(k)$ to real-space $G_d(r)$. | $G_d(r)$, $H_d(k)$ | Produces the 2.8 Å hydrogen-bond peak used as the central result. |

## Implementation notes

- Table III gives the full tabulated $H(k)$ and $H_d(k)$ for both methanol and ethanol at $k=0.0$ to $16.0\ \text{Å}^{-1}$ in steps of 0.1 Å⁻¹; this could in principle be digitized as a reciprocal-space structural reference target, but was not transcribed in full here (see Known gaps).
- The hydrogen-bond fit (Table IV) used the large-$k$ portion of $H_d(k)$ with coordination number as a free parameter; the reported coordination numbers (1.77-1.81) and bond distance (2.80-2.81 Å) are fit outputs, not direct measurements of a single geometric distance.
- The paper's own intramolecular bond-length and rms-deviation values (Table II) were obtained sequentially (C-O from methanol, then C-C and C···O from ethanol using the fixed C-O value), so the ethanol intramolecular parameters are conditional on the methanol fit.

## Mathematical gaps

- The compressibility-based extrapolation procedure for $H_d(k\to0)$ is referenced to an earlier paper (ref. 23) and not reproduced in full here.
- Table III's full numerical $H(k)$/$H_d(k)$ listings (all $k$ values, both liquids) are summarized but not digitized into the wiki as machine-readable data.

## Claims

- [[wiki/claims/CLM-0051-xray-diffraction-alcohol-oh-hydrogen-bond-geometry]]

## Links

- [[wiki/concepts/tolerance-normalized-multi-observable-losses]] - This paper's tabulated structure functions and radial distribution functions are the kind of experimental structural observable (analogous to water's O-O/H-O/H-H RDFs) that a future alcohol force-field training or validation target family would draw on; FFRefine does not currently use this data.
- [[wiki/answers/ffrefine-current-implementation-status]] - FFRefine's ethanol-solvation experiment currently trains on solvation free energy (and an optional, currently disabled density target), not structural RDF targets; this source is a candidate experimental reference if ethanol structural validation is added later.
- [[wiki/claims/CLM-0009-observable-fitting-needs-held-out-validation]] - General precedent (for water models) that RDF-type structural observables are natural held-out validation targets distinct from thermodynamic fitting targets; this source supplies the analogous experimental reference geometry for methanol and ethanol.
- [[wiki/sources/SRC-0093-the-structure-of-liquid-ethanol-a-neutron-diffraction]] - A later (2000) neutron-diffraction/MD study of liquid ethanol cites this source as its Ref. 8 and directly compares its neutron-derived intermolecular $XX$ structure factor against this source's x-ray intermolecular structure factor, finding good agreement for $Q>5\ \text{Å}^{-1}$ where both are dominated by O-O correlations. Confirmed citation match (exact author/year/venue match).
- [[wiki/claims/CLM-0052-neutron-md-liquid-ethanol-winding-hydrogen-bonded-chains]] - Complementary claim from the citing neutron-diffraction/MD source; broadly consistent hydroxyl coordination picture for ethanol, measured by a different technique and specific site pairs.

## Metadata notes

- Bibliographic details confirmed directly from the PDF: A. H. Narten (Chemistry Division, Oak Ridge National Laboratory) and A. Habenschuss (University Programs Division, Oak Ridge Associated Universities); received 25 October 1983, accepted 7 December 1983; J. Chem. Phys. 80(7), 3387-3391 (1 April 1984); DOI `10.1063/1.447093`.
- The work was sponsored by the US DOE Division of Materials Sciences under contracts W-7405-eng-26 (Union Carbide Corp.) and DE-AC05-76OR00033 (Oak Ridge Associated Universities).
- The references (26 total) were inspected for context. All 26 were cross-checked by author, year, and venue against every ingested SecondBrain source page (2026-10-01); the only earlier-dated ingested source, SRC-0075 (Neumann 1983), is not cited. No matches, so `cites_sources` is left empty and `citation_match_status` is `reviewed`.
- No supplementary material or data files accompanied the PDF; this is treated as a single, non-bundled source.

## Ingestion QA

### Retrieval questions checked

- What is the central contribution? X-ray-diffraction-derived evidence that liquid methanol and ethanol hydroxyl groups have ~1.8 hydrogen-bonded OH···OH neighbors at 2.8 Å, supporting a chain-like (not ring-like) average liquid structure. [SRC-0092, §IV]
- What problem does it address? Direct experimental characterization of intermolecular hydrogen-bonding structure in liquid alcohols, complementing earlier neutron-diffraction and statistical-mechanical modeling work. [SRC-0092, §I]
- What methods were used? X-ray diffraction at 20 °C with Mo $K_\alpha$ radiation; least-squares fitting of intramolecular structure function parameters; Fourier inversion of the intermolecular structure function to a radial distribution function; compressibility-based low-$k$ extrapolation. [SRC-0092, §§II-III]
- What is the key evidence? A well-resolved ~2.8 Å peak in $G_d(r)$ for both liquids, absent in alkanes, fit by a Gaussian with coordination number ≈1.8. [SRC-0092, Fig. 4, Table IV]
- What are the key numerical results? Methanol: $n=1.77(7)$, $r=2.798(6)$ Å; ethanol: $n=1.81(9)$, $r=2.808(8)$ Å; intramolecular C-O $1.437(2)$ Å, C-C $1.540(3)$ Å, C···O $2.472(4)$ Å. [SRC-0092, Tables II, IV]
- What are the limitations? Results describe an average liquid structure; local/instantaneous configurations deviate substantially; coordination number and bond distance come from a model fit to the large-$k$ structure function rather than a direct real-space measurement; only pure liquids at 20 °C and atmospheric pressure are studied (no mixtures, temperatures, or pressures). [SRC-0092, §IV]
- What should not be overgeneralized? The chain-formation interpretation is a plausible structural picture consistent with the data, not a uniquely proven topology; the paper itself notes that further experimental or statistical-mechanical modeling would be needed to fully define alcohol intermolecular structure. [SRC-0092, §IV]
- Does this connect to current SecondBrain force-field work? Not directly used by any current project; it is a candidate experimental structural reference for a possible future alcohol RDF validation target, analogous to existing water RDF validation practice. [Synthesis, not stated in the source]

### Coverage decision

Complete at `coverage_profile: math-standard`. The paper's methodology, central equations, numerical results (Tables I-IV), interpretation, and limitations are represented; the full $k$-resolved structure-function tables (Table III) are summarized rather than digitized in full.

### Known gaps

- Table III's complete numerical structure-function listings (161 $k$ points per liquid) are not transcribed as machine-readable data; only their role and key features are recorded.
- No citation match to an already-ingested SecondBrain source was found or forced.
