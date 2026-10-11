---
type: source
status: active
created: 2026-10-01
updated: 2026-10-01
source_id: SRC-0093
display_title: "The Structure of Liquid Ethanol: A Neutron Diffraction and Molecular Dynamics Study"
short_title: "Benmore & Loh Liquid Ethanol Neutron Diffraction"
aliases:
  - "SRC-0093"
  - "Benmore and Loh 2000"
  - "The Structure of Liquid Ethanol: A Neutron Diffraction and Molecular Dynamics Study"
source_path: raw/sources/SRC-0093-the-structure-of-liquid-ethanol-a-neutron-diffraction.pdf
imported_path: raw/sources/SRC-0093-the-structure-of-liquid-ethanol-a-neutron-diffraction.pdf
original_filename: "5877_1_online.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: c601353b3f2e54b109ee107548653bc26e636877a6999d849695c6db2d098047
authors:
  - "Chris J. Benmore"
  - "Yen L. Loh"
author_entities: []
year: 2000
venue: "Journal of Chemical Physics, 112(13), 5877-5883"
doi: "10.1063/1.481160"
arxiv:
metadata_review_status: reviewed
areas:
  - research
categories:
  - research/experimental-benchmarking
  - research/molecular-simulation/force-fields
tags:
  - scientific-paper
  - neutron-diffraction
  - hydrogen-bonding
  - ethanol
  - liquid-structure
  - radial-distribution-function
  - molecular-dynamics
  - isotopic-substitution
  - opls
related:
  - "[[wiki/sources/SRC-0092-hydrogen-bonding-in-liquid-methanol-and-ethanol-determined]]"
  - "[[wiki/claims/CLM-0051-xray-diffraction-alcohol-oh-hydrogen-bond-geometry]]"
  - "[[wiki/claims/CLM-0052-neutron-md-liquid-ethanol-winding-hydrogen-bonded-chains]]"
  - "[[wiki/concepts/tolerance-normalized-multi-observable-losses]]"
  - "[[wiki/answers/ffrefine-current-implementation-status]]"
  - "[[wiki/claims/CLM-0009-observable-fitting-needs-held-out-validation]]"
sources:
  - SRC-0093
cites_sources:
  - SRC-0092
citation_match_status: reviewed
cqt_review_status: linked
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: math-standard
peer_review_status: peer-reviewed
---

# The Structure of Liquid Ethanol: A Neutron Diffraction and Molecular Dynamics Study

Source ID: `SRC-0093`

## Raw source

- Repository path: `raw/sources/SRC-0093-the-structure-of-liquid-ethanol-a-neutron-diffraction.pdf`
- Open raw source: [raw/sources/SRC-0093-the-structure-of-liquid-ethanol-a-neutron-diffraction.pdf](../../raw/sources/SRC-0093-the-structure-of-liquid-ethanol-a-neutron-diffraction.pdf)

## Summary

Benmore and Loh (ISIS Facility, Rutherford Appleton Laboratory; Cavendish Laboratory, Cambridge) report a comprehensive neutron scattering (H/D isotopic substitution) study of pure liquid ethanol at room temperature (22±1 °C), using the SANDALS diffractometer at the ISIS pulsed neutron facility. [SRC-0093, Abstract, §III.B] Of the 21 possible partial structure factors for ethanol's six distinct atom types, they directly measure 6 hydrogen-hydrogen intermolecular partial structure factors and extract 4 composite structure factors ($H_{XH1}$, $H_{XH2}$, $H_{XH3}$, $H_{XX}$) describing hydroxyl-, methylene-, and methyl-hydrogen correlations and carbon/oxygen ("nonhydrogen", $XX$) correlations. [SRC-0093, Abstract, §I, Eqs. 4-5] The neutron data are compared against classical molecular dynamics (MD) simulations using Jorgensen's OPLS potential in both a four-site (united-atom methyl/methylene) and nine-site (all-atom) representation. [SRC-0093, §IV] Agreement between the measured and simulated structure factors and radial distribution functions is generally good, and both experiment and simulation support a picture in which hydrogen bonding dominates the intermolecular structure of liquid ethanol, consistent with disordered, winding hydrogen-bonded chains rather than closed hexamer or tetramer clusters. [SRC-0093, Abstract, §VI]

The paper explicitly compares its neutron-derived intermolecular $XX$ (carbon/oxygen) composite structure factor against the x-ray intermolecular structure factor of Narten and Habenschuss [SRC-0092] (their Ref. 8), finding that beyond $Q>5\ \text{Å}^{-1}$, where both functions are dominated by the O–O partial, the neutron and x-ray data have practically the same shape. [SRC-0093, §V.B, Fig. 5] This is a direct experimental cross-check between the two sources: SRC-0092's x-ray intermolecular structure function for ethanol and this paper's independently measured neutron composite structure function agree in the Q-range where both are dominated by oxygen-oxygen correlations.

This is a single, non-bundled, 7-page experimental/simulation paper with no appendices or supplementary data supplied.

## Key points

- Twelve isotopically distinct ethanol samples were measured: fully protonated CH₃CH₂OH; four specifically deuterated samples CH₃CD₂OH, CH₃CH₂OD, CH₃CD₂OD, CD₃CD₂OD; and seven 50:50 mixtures of these, chosen to maximize scattering-length contrast for specific H/D substitutions. [SRC-0093, §III.B]
- Notation used throughout: H1 = hydroxyl hydrogen, H2 = methylene (CH₂) hydrogen, H3 = methyl (CH₃) hydrogen; C1 = carbon nearest oxygen, C2 = methyl carbon. [SRC-0093, §III.C]
- First- and second-order H/D difference methods (Eqs. 2-3) isolate partial structure factors for a single substituted atom/group; six hydrogen-hydrogen partial structure factors and four nonhydrogen-weighted composite functions were obtained this way. [SRC-0093, §III.A, Eqs. 2-3]
- Data reduction used the ATLAS package with a constraint that $H_{HH}(Q)$, $H_{XH}(Q)$, and $H_{XX}(Q)$ match MD-predicted $H(0)$ values (to correct for inaccuracies in nuclear-recoil correction at low $Q$ for hydrogenous samples on a pulsed source), and Soper's minimum-noise Fourier inversion technique to reduce Fourier transform artifacts. [SRC-0093, §III.C]
- MD used 125 semiflexible ethanol molecules in a 23 Å cubic box, DL_POLY 2.0, Hoover-Nosé NVT thermostat at $T=300$ K, density $0.7873\ \text{g/cm}^3$, 100 ps runs in 0.002 ps steps. Two models were simulated: a four-site model (Jorgensen's OPLS, LJ sites on O-O/C-C/O-C only, charges on C1/O/H1, single C-O dihedral potential) and a nine-site model (all methyl/methylene hydrogens included with zero charges, harmonic bonds and valence angles, two dihedral potentials for both C-O and C-C internal rotation, from Gao et al. ab initio 6-31G calculations). [SRC-0093, §IV, Tables I-II, Fig. 3]
- The measured intramolecular OH bond length in the liquid, $r=0.97(1)$ Å ($\sigma=0.09$), is longer than the gas-phase value ($0.945(2)$ Å), consistent with hydrogen bonding; the methyl/methylene hydrogens are, on average, oriented in the eclipsed configuration found in the crystal structure. [SRC-0093, §V.A, Table III]
- The four-site model agrees very well with the measured $H_{XX}(Q)$ neutron data; the nine-site model's high-$Q$ oscillations are shifted to higher $Q$, corresponding to an ~0.08 Å shift in the first peak of $g_{OO}(r)$ between the two models, attributed to the different dihedral potentials controlling internal rotation (single C-O dihedral vs. two C-O/C-C dihedrals). [SRC-0093, §V.B]
- Integrated coordination numbers from the intermolecular radial distribution functions: the hydroxyl hydrogen is surrounded by $2.0\pm0.2$ hydroxyl hydrogen atoms within 3.0 Å; the oxygen is surrounded by $0.95\pm0.3$ hydroxyl hydrogen atoms within 2.1 Å and $2.0\pm0.2$ oxygen atoms within 3.0 Å. [SRC-0093, §V.B, Fig. 6]
- The $g_{XX}(r)$ composite neutron intermolecular function is directly compared against Narten and Habenschuss's x-ray intermolecular structure factor (via Eq. 6, weighting the simulation results with x-ray form factors); agreement is good beyond $Q>5\ \text{Å}^{-1}$ where O–O correlations dominate both functions, with differences at lower $Q$ attributed to electron form-factor variation. [SRC-0093, §V.B, Fig. 5]
- Comparing the measured nearest-neighbor $g_{H1H1}(r)$ peak against three cluster models proposed by Sarkar and Joarder (U-shaped open chain, tetramer closed chain, hexamer closed chain), the U-shaped open-chain model agrees well in peak position and area, while the closed-chain tetramer and hexamer models do not; this is consistent with the MD winding hydrogen-bonded chain picture rather than Sarkar and Joarder's proposed hexamer clusters. [SRC-0093, §V.B, Fig. 7(a)]
- Comparing ethanol to methanol (via Yamaguchi et al.), the $g_{H1H1}(r)$ coordination number is the same within experimental error, but at a slightly shorter distance in ethanol (2.28 Å) than methanol (2.42 Å); two additional peaks at 3.3 and 4.4 Å in the ethanol curve are reproduced by the MD winding-chain model and correspond to the repeat H1···H1···H1 distance along the chain. [SRC-0093, §V.B, Fig. 7(b)]

## Methods and evidence

Neutron diffraction used the H/D substitution technique on 12 isotopically distinct liquid ethanol samples (SANDALS diffractometer, ISIS pulsed neutron source), measured at $22\pm1\ ^\circ\text{C}$ in 1 mm-wall titanium-zirconium "null scattering" containers; samples were $\geq 99.7\%$ purity from Aldrich/Hayman. [SRC-0093, §III.B] First- and second-order isotopic differences isolate single-site and site-pair partial structure factors (Eqs. 2-3); the measured $H_{XH}(Q)$ and $H_{XX}(Q)$ composite functions still contain residual intramolecular hydrogen contributions, which were fitted and subtracted using Eq. 7 after Fourier transformation to real space. [SRC-0093, §III.C, §V.A]

MD simulation used Jorgensen's OPLS intermolecular potentials in four-site and nine-site representations, fit against the earlier gas-phase and liquid-phase geometry references used in the field (see Table III for a cross-comparison of crystal, Jorgensen gas-phase, prior neutron, and this paper's liquid intramolecular bond lengths). [SRC-0093, §IV] Simulated structure factors and radial distribution functions were compared directly against the neutron data (Fig. 2, Fig. 6) and, via appropriate form-factor weighting (Eq. 6), against Narten and Habenschuss's x-ray data (Fig. 5). [SRC-0093, §V.B]

## Mathematical structure

The site-site radial distribution functions $g_{\alpha\beta}(r)$ are related to the measured $Q$-space partial structure factors $H_{\alpha\beta}(Q)$ by a standard Fourier-transform pair (Eq. 1). Measured total structure factors for H/D-substituted samples are combined via first-order (single-site) and second-order (site-pair) isotopic difference equations (Eqs. 2-3) to isolate partial structure factors involving a specific hydrogen site. Because full isotopic separation of all hydrogen sites is not experimentally possible, the measured composite functions $H_{XH1}(Q)$, $H_{XH2}(Q)$, $H_{XH3}(Q)$ (Eq. 4) and $H_{XX}(Q)$ (Eq. 5) are weighted sums of several underlying partial structure factors, with weights determined by the relevant neutron scattering lengths. The intramolecular contribution to these composite functions is modeled as a Gaussian-rms-deviation-damped sinc-like function of $Q$ (Eq. 7) and subtracted to leave the intermolecular (structural) signal. Equation 6 defines an analogous x-ray structure factor, weighted by atomic form factors $f_\alpha(Q)$ instead of neutron scattering lengths, used to compare MD and neutron results directly against published x-ray diffraction data.

## Key equations

Site-site structure factor / radial distribution function Fourier pair: [SRC-0093, Eq. 1, p. 5878]

$$
H_{\alpha\beta}(Q) = 4\pi\rho \int r^2\,[g_{\alpha\beta}(r)-1]\,\frac{\sin Qr}{Qr}\,dr.
$$

First-order isotopic difference (isolates the hydroxyl-hydrogen environment): [SRC-0093, Eq. 2, p. 5878]

$$
H_{XH_1}(Q) = A\cdot[F_{CH_3CH_2OH}(Q) - F_{CH_3CH_2OD}(Q)].
$$

Second-order isotopic difference (isolates hydroxyl-hydroxyl hydrogen partial structure factor): [SRC-0093, Eq. 3, p. 5878]

$$
H_{H_1H_1}(Q) = B\cdot[2F_{CH_3CH_2OM}(Q) - F_{CH_3CH_2OH}(Q) - F_{CH_3CH_2OD}(Q)],
$$

where $M$ is a 50:50 mixture of $\text{CH}_3\text{CH}_2\text{OH}$ and $\text{CH}_3\text{CH}_2\text{OD}$, and $A$, $B$ are normalization constants.

Nonhydrogen ($XX$) composite structure function: [SRC-0093, Eq. 5, p. 5879]

$$
H_{XX}(Q) = 0.0924\,H_{OO}(Q) + 0.212\,H_{C1O}(Q) + 0.121\,H_{C1C1}(Q) + 0.212\,H_{C2O}(Q) + 0.242\,H_{C2C1}(Q) + 0.121\,H_{C2C2}(Q).
$$

Analogous x-ray structure factor, used for comparison against Narten and Habenschuss's x-ray data: [SRC-0093, Eq. 6, p. 5880]

$$
H_{\text{x-ray}}(Q) = \left(\sum (2-\delta_{\alpha\beta})\,f_\alpha(Q) f_\beta(Q)\, H_{\alpha\beta}(Q)\right)\left(\sum f_\alpha(Q)\right)^{-2},
$$

where $f_\alpha$ is the x-ray atomic form factor for site $\alpha$.

Intramolecular term subtracted from the composite $XH$/$XX$ functions: [SRC-0093, Eq. 7, p. 5880]

$$
H_{\alpha\beta}^{\text{intra}}(Q) = \sum \frac{\sin Qr_{\alpha\beta}}{\sin Qr_{\alpha\beta}}\, e^{-Q^2\sigma^2/2},
$$

where $r_{\alpha\beta}$ is the average intramolecular separation of atom types $\alpha$ and $\beta$, and $\sigma$ is the standard deviation of that distance. **Transcription note:** the denominator is printed in the source exactly as shown ("$\sin Qr_{\alpha\beta}$"), identical to the numerator; this is almost certainly a typesetting error in the original journal PDF, since the standard sinc-damped form used throughout this literature (and consistent with the paper's own description of the term as a damped sine) is $\sin(Qr_{\alpha\beta})/(Qr_{\alpha\beta})$. Rendering the page at high resolution confirms the printed denominator really is $\sin Qr_{\alpha\beta}$ (not a text-extraction artefact). The intended form is corroborated by the paper's own Eq. 1, which uses $\sin Qr/(Qr)$, and by its Ref. 8 (SRC-0092, Eq. 3), which models the same intramolecular term as $j_0(kr_{\alpha\gamma})\exp(-l_{\alpha\gamma}^2k^2/2)$ with $j_0(x)=\sin x/x$. Recorded as printed rather than silently corrected; see Mathematical gaps.

## Equation inventory

| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |
| Site-site Fourier pair | SRC-0093, Eq. 1, p. 5878 | This page, Key equations | Relates measured $Q$-space partial structure factors to real-space $g_{\alpha\beta}(r)$. | $H_{\alpha\beta}(Q)$, $g_{\alpha\beta}(r)$, $\rho$ | Standard liquid-diffraction Fourier-transform relation, reusable for any site-site RDF/structure-factor comparison. |
| First-order isotopic difference | SRC-0093, Eq. 2, p. 5878 | This page, Key equations | Isolates a single substituted hydrogen site's structural environment. | $H_{XH_1}(Q)$, $F$, $A$ | Defines the H/D substitution method applied across all 12 samples. |
| Second-order isotopic difference | SRC-0093, Eq. 3, p. 5878 | This page, Key equations | Isolates a hydrogen-hydrogen partial structure factor (e.g. H1-H1). | $H_{H_1H_1}(Q)$, $B$, $M$ | Core of the six measured H-H partial structure factors. |
| Composite $XH$ functions | SRC-0093, Eq. 4, p. 5879 | Not reproduced in full; see Implementation notes | Expresses measured $H_{XH1}$, $H_{XH2}$, $H_{XH3}$ as weighted sums of partials. | Site-pair weighting coefficients (0.153-0.943 range) | Needed to decompose composite functions into underlying site-site partials. |
| Composite $XX$ function | SRC-0093, Eq. 5, p. 5879 | This page, Key equations | Expresses measured nonhydrogen composite structure factor as a weighted sum of C/O partials. | $H_{XX}(Q)$, weighting coefficients | Basis for the direct neutron/x-ray comparison (Fig. 5). |
| X-ray analogue structure factor | SRC-0093, Eq. 6, p. 5880 | This page, Key equations | Converts simulated (or neutron) site-site functions into an x-ray-comparable structure factor. | $H_{\text{x-ray}}(Q)$, $f_\alpha(Q)$ | Used to overlay MD and neutron results on Narten and Habenschuss's x-ray data [SRC-0092]. |
| Intramolecular damping term | SRC-0093, Eq. 7, p. 5880 | This page, Key equations | Models/subtracts the intramolecular contribution to composite $XH$/$XX$ functions. | $H^{\text{intra}}_{\alpha\beta}(Q)$, $r_{\alpha\beta}$, $\sigma$ | Needed to isolate intermolecular (structural) signal; printed form likely contains a typesetting error (see above). |

## Implementation notes

- Eq. 4's full three-line weighted sums for $H_{XH1}(Q)$, $H_{XH2}(Q)$, $H_{XH3}(Q)$ (coefficients 0.153-0.943, including intramolecular H1H2/H1H3/H2H1/H2H3 cross terms) were inspected but not fully transcribed here; see the source PDF, p. 5879, if the individual coefficients are needed for reanalysis.
- Table I (Lennard-Jones parameters: O-O $\varepsilon=0.170$ kcal/mol, $\sigma=3.07$ Å; C1-C1 $\varepsilon=0.110$, $\sigma=3.98$; C2-C2 $\varepsilon=0.180$, $\sigma=3.86$; O-C1 $\varepsilon=0.137$, $\sigma=3.50$; O-C2 $\varepsilon=0.175$, $\sigma=3.44$; C1-C2 $\varepsilon=0.141$, $\sigma=3.92$) and Table II (dihedral potentials $V_0$-$V_3$ for four-site H-O-C1-C2 and nine-site H-O-C1-C2/O-C1-C2-H2 torsions) give a complete, reusable four-site and partial nine-site OPLS-style ethanol force field specification. [SRC-0093, Tables I-II]
- Partial charges for the four-site model are shown schematically in Fig. 3 ($q_{H1}=+0.435$, $q_O=-0.700$, $q_{C1}=+0.265$, all other sites zero); exact numeric values for the nine-site model's bond/angle force constants are given in the text ($350\ \text{kcal mol}^{-1}\text{Å}^{-2}$ bonds, $150\ \text{kcal mol}^{-1}\text{rad}^{-2}$ angles) but full nine-site charge/LJ parameters beyond "zero charge on nonhydrogen-bonded H" were not separately tabulated in the paper. [SRC-0093, §IV, Fig. 3]
- Table III (bond lengths: crystal, Jorgensen gas-phase, prior neutron liquid data of Montague et al., this paper's neutron liquid data) and Table IV (bond angles, same comparison set) are useful cross-study intramolecular-geometry reference tables but were not fully digitized row-by-row here.

## Mathematical gaps

- Eq. 7's denominator is printed identically to its numerator ("$\sin Qr_{\alpha\beta}/\sin Qr_{\alpha\beta}$"); this is recorded as a likely source-level typesetting error rather than corrected. The intended form $\sin(Qr_{\alpha\beta})/(Qr_{\alpha\beta})$ is strongly corroborated by the paper's Eq. 1 and by the identical Gaussian-damped $j_0$ form in SRC-0092, Eq. 3, but no erratum was checked (see Key equations, transcription note).
- Eq. 4's full coefficient set for the three $XH$ composite functions was not transcribed in full (see Implementation notes).
- Table III's compressibility-extrapolation and minimum-noise Fourier inversion procedures reference external methods (Soper, Ref. 19; Soper and Luzar, Ref. 13) not reproduced in detail here.
- Numerical tabulations of the measured structure factors and radial distribution functions themselves (analogous to SRC-0092's Table III) are not included in the PDF as a separate data table and were not digitized.

## Claims

- [[wiki/claims/CLM-0051-xray-diffraction-alcohol-oh-hydrogen-bond-geometry]] - this paper's neutron/MD results for ethanol are a complementary, independent measurement technique probing a closely related structural question (hydroxyl hydrogen-bonding geometry) to SRC-0092's x-ray result; the two sources are not merged into one claim because they use different techniques, report different specific quantities (H1-H1 distance and coordination vs. OH···OH distance and coordination), and this paper's claim additionally concerns chain topology and force-field validation.
- [[wiki/claims/CLM-0052-neutron-md-liquid-ethanol-winding-hydrogen-bonded-chains]]

## Links

- [[wiki/sources/SRC-0092-hydrogen-bonding-in-liquid-methanol-and-ethanol-determined]] - This paper directly cites and quantitatively compares against Narten and Habenschuss's x-ray intermolecular structure factor for ethanol (their Ref. 8); see Fig. 5 and Eq. 6. Confirmed exact match: same authors, same year (1984), same venue (J. Chem. Phys. 80, 3387), same DOI family as already recorded in SRC-0092's metadata.
- [[wiki/concepts/tolerance-normalized-multi-observable-losses]] - Like SRC-0092, this paper's structure factors and radial distribution functions are the kind of experimental structural observable a future alcohol force-field training or validation target family would draw on; it additionally supplies a complete, directly reusable four-site OPLS-style ethanol force field (Tables I-II) as a comparison baseline. FFRefine does not currently use this data.
- [[wiki/answers/ffrefine-current-implementation-status]] - FFRefine's ethanol-solvation experiment currently trains on solvation free energy (and an optional, currently disabled density target), not structural RDF targets or the OPLS four-/nine-site potentials described here; this source is a candidate experimental and force-field reference if ethanol structural validation is added later.
- [[wiki/claims/CLM-0009-observable-fitting-needs-held-out-validation]] - General precedent (for water models) that RDF-type structural observables are natural held-out validation targets distinct from thermodynamic fitting targets; this source supplies both the experimental RDF-type reference data and a concrete alternative/baseline force field for ethanol.

## Metadata notes

- Bibliographic details confirmed directly from the PDF: Chris J. Benmore (ISIS Facility, CLRC Rutherford Appleton Laboratory, Chilton, Oxon) and Yen L. Loh (Cavendish Laboratory, Cambridge University); received 15 November 1999, accepted 5 January 2000; published as a Research Article dated 1 April 2000 in J. Chem. Phys. 112(13), 5877-5883; DOI `10.1063/1.481160`.
- The references (21 total) were inspected for context. Reference 8 ("A. H. Narten and A. Habenschuss, J. Chem. Phys. 80, 3387 (1984)") is an exact author/year/venue match to the already-ingested [[wiki/sources/SRC-0092-hydrogen-bonding-in-liquid-methanol-and-ethanol-determined]] (J. Chem. Phys. 80(7), 3387-3391, 1984); this is recorded in `cites_sources`. The paper also explicitly compares its own results against Narten's x-ray data (Fig. 5), so this is both a bibliographic citation and a direct quantitative cross-check between the two sources. The remaining 20 references were cross-checked by author, year, and venue against every ingested SecondBrain source page (2026-10-01); none matched, so `citation_match_status` is `reviewed`.
- No supplementary material or data files accompanied the PDF; this is treated as a single, non-bundled source.

## Ingestion QA

### Retrieval questions checked

- What is the central contribution? A comprehensive H/D-substitution neutron diffraction study of liquid ethanol, directly measuring 10 of 21 possible partial/composite structure factors and comparing them to four-site and nine-site OPLS molecular dynamics simulations, confirming that hydrogen bonding dominates the liquid's intermolecular structure via disordered winding chains. [SRC-0093, Abstract]
- What problem does it address? Previous x-ray and neutron studies of liquid ethanol (including SRC-0092) could not isolate all the hydrogen-hydrogen partial structure factors needed to fully characterize the hydrogen-bonding network; H/D isotopic substitution provides that resolution. [SRC-0093, §I-§II]
- What methods were used? Neutron diffraction with H/D isotopic substitution on 12 samples (SANDALS, ISIS); first/second-order isotopic difference analysis; MD simulation with Jorgensen's OPLS potential in four-site and nine-site representations (DL_POLY). [SRC-0093, §III-IV]
- What is the key evidence? Good agreement between measured and simulated $H_{\alpha\beta}(Q)$ structure factors (Fig. 2) and intermolecular radial distribution functions (Fig. 6); direct agreement with Narten and Habenschuss's x-ray intermolecular structure factor beyond $Q>5\ \text{Å}^{-1}$ (Fig. 5); better agreement of the nearest-neighbor $g_{H1H1}(r)$ peak with a U-shaped open-chain model than with proposed hexamer/tetramer closed-chain models. [SRC-0093, §V, Figs. 2, 5-7]
- What are the key numerical results? Liquid-state OH bond length $0.97(1)$ Å vs. gas-phase $0.945(2)$ Å; hydroxyl-hydrogen coordination $2.0\pm0.2$ within 3.0 Å; oxygen coordination $0.95\pm0.3$ hydroxyl H within 2.1 Å and $2.0\pm0.2$ O within 3.0 Å; $g_{H1H1}(r)$ first-peak position 2.28 Å in ethanol vs. 2.42 Å in methanol. [SRC-0093, Table III, §V.B]
- What are the limitations? Results are an average, time/ensemble-averaged structure; the nine-site and four-site MD models disagree with each other and with experiment on specific peak positions (0.07-0.16 Å shifts), attributed to differences in the dihedral potentials used; the $g_{XX}(r)$ function includes broad intramolecular hydrogen-hydrogen contributions that may introduce systematic errors. [SRC-0093, §V.A-B]
- What should not be overgeneralized? Agreement with a winding-chain picture over closed hexamer/tetramer clusters is based on nearest-neighbor peak comparison only; the authors note closed-chain hexamer clusters could still survive in small quantities, and whether/how the liquid structure transitions toward clusters at higher pressure/temperature (as seen for supercritical methanol) remains an open question the authors flag as future work, not resolved here. [SRC-0093, §V.B, §VI]
- Does this connect to current SecondBrain force-field work? Not directly used by any current project; it is a candidate experimental structural reference and a ready-made four-site/partial nine-site OPLS ethanol force field, analogous to existing water RDF validation practice and complementary to SRC-0092. [Synthesis, not stated in the source]

### Coverage decision

Complete at `coverage_profile: math-standard`. The paper's methodology, central equations, numerical results (Tables I-IV, key figures), interpretation, limitations, and the direct cross-reference to SRC-0092 are represented; Eq. 4's full coefficient set and the raw numerical structure-factor/RDF tabulations are summarized rather than digitized in full.

### Known gaps

- Eq. 4's complete three-equation coefficient set (for $H_{XH1}$, $H_{XH2}$, $H_{XH3}$) was not transcribed in full.
- Eq. 7's printed denominator appears to contain a typesetting error in the source PDF; recorded as printed, not corrected (see Mathematical gaps).
- Raw numerical structure-factor and radial-distribution-function data (underlying Figs. 2, 4, 6) are not available as machine-readable tables in the PDF and were not digitized.
- Only 1 of 21 references (Ref. 8, matching SRC-0092) was confirmed against already-ingested SecondBrain sources; the remaining 20 were not exhaustively cross-checked.
