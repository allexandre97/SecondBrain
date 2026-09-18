---
type: source
status: active
created: 2026-09-18
updated: 2026-09-18
source_id: SRC-0090
display_title: "Training a force field for proteins and small molecules from scratch"
short_title: "Garnet Force Field (Chemical Science)"
aliases:
  - "SRC-0090"
  - "Garnet Chemical Science"
  - "Training a Force Field from Scratch"
source_path: raw/sources/SRC-0090-training-force-field-proteins-small-molecules.pdf
imported_path: raw/sources/SRC-0090-training-force-field-proteins-small-molecules.pdf
original_filename: "d6sc02874h.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: e61a6ff6d62ef579f284015b8861dd324b9df272c77b715f09d37f4541b195da
authors:
  - "Alexandre Blanco-González"
  - "Thea K. Schulze"
  - "Evianne Rovers"
  - "Joe G. Greener"
author_entities: []
year: 2026
venue: "Chemical Science"
doi: "10.1039/D6SC02874H"
arxiv:
metadata_review_status: reviewed
source_bundle: garnet-training-force-field-from-scratch-2026
bundle_role: main
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/machine-learning/molecular-modeling
  - research/biomolecules/proteins
  - research/machine-learning/scientific-modeling
  - research/experimental-benchmarking
  - research/molecular-simulation/free-energy
tags:
  - garnet
  - molecular-dynamics
  - graph-neural-networks
  - force-fields
  - double-exponential-potential
  - rbfe
  - continuous-atom-typing
related:
  - "[[wiki/sources/SRC-0091-training-force-field-proteins-small-molecules-supplement]]"
  - "[[wiki/sources/SRC-0003-training-a-force-field-from-scratch]]"
  - "[[wiki/concepts/garnet-force-field]]"
  - "[[wiki/concepts/double-exponential-potential]]"
  - "[[wiki/concepts/automated-force-field-training]]"
  - "[[wiki/concepts/relative-binding-free-energy-benchmarking]]"
  - "[[wiki/claims/CLM-0002-garnet-automates-parameter-assignment]]"
  - "[[wiki/questions/garnet-validation-scope]]"
  - "[[wiki/tensions/TEN-0002-garnet-broad-coverage-vs-validation-gaps]]"
sources:
  - SRC-0090
cites_sources:
  - SRC-0016
  - SRC-0021
  - SRC-0023
  - SRC-0025
  - SRC-0043
  - SRC-0044
  - SRC-0046
  - SRC-0061
  - SRC-0072
citation_match_status: partial
cqt_review_status: linked
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: math-standard
peer_review_status: peer-reviewed
---

# Training a Force Field for Proteins and Small Molecules from Scratch

Source ID: `SRC-0090`

## Raw source

- Repository path: `raw/sources/SRC-0090-training-force-field-proteins-small-molecules.pdf`
- Open raw source: [raw/sources/SRC-0090-training-force-field-proteins-small-molecules.pdf](../../raw/sources/SRC-0090-training-force-field-proteins-small-molecules.pdf)
- Supplement: [[wiki/sources/SRC-0091-training-force-field-proteins-small-molecules-supplement]]
- Preprint: [[wiki/sources/SRC-0003-training-a-force-field-from-scratch]]

## Summary

This is the peer-reviewed Chemical Science version of the Garnet paper, published 17 September 2026 under a CC-BY 4.0 licence. It presents Garnet, a graph neural network that assigns all molecular mechanics force-field parameters (bonds, angles, proper and improper torsions, charges, and non-bonded terms) for supported molecules using continuous atom typing from molecular topology, without reusing legacy force-field parameters. Training combined quantum mechanical data (SPICE, Espaloma, GEMS, MACE-OFF), condensed-phase properties (enthalpy of vaporisation and mixing), and GB3 protein NMR data via ensemble reweighting, with water parameters trained from scratch rather than imported from an existing model. The authors report performance comparable to established force fields on small molecules, folded proteins, protein complexes, and disordered proteins, and similar results to popular approaches on relative binding free energy (RBFE) predictions, while showing that the double exponential non-bonded potential is a trainable and accurate alternative to Lennard-Jones. [SRC-0090]

## Key points

- Garnet predicts parameters from continuous atom types; it does not rely on human-assigned atom types. [SRC-0090]
- Training was from scratch; the only dependence on existing force fields is via GAFF/TIP3P and Amber14SB/TIP3P trajectories used for the first five epochs to provide conformations before the training force field was stable enough to generate its own. [SRC-0090, Methods]
- Lennard-Jones became unstable to train once simulations entered the pipeline; the double exponential potential trained effectively and runs about 15--20% slower than Lennard-Jones in OpenMM. [SRC-0090]
- Fitted double-exponential global parameters are $a=12.2$ and $b=4.33$, with a 1--4 electrostatic scaling factor of 0.57. [SRC-0090, section "The Garnet force field"]
- On the SPICE held-out subsets, Garnet's force and potential-energy-difference errors are lower than Espaloma 0.4.0 and much lower than OpenFF 2.2.1, though still much higher than MACE-OFF23. [SRC-0090, Table 1]
- On the 12-molecule condensed-phase test set, Garnet overestimates density and enthalpy of vapourisation relative to OpenFF 2.2.1 (ΔHv RMSE 4.29 vs 2.63 kcal mol$^{-1}$; density RMSE 0.13 vs 0.041 g mL$^{-1}$), consistent with overly strong attractive intermolecular interactions. The three molecules whose ΔHv was seen during training are predicted better. [SRC-0090, section "Small molecule benchmark"] [SRC-0091, Table 3]
- Folded proteins GB3, BPTI, HEWL, and ubiquitin remained stable over 5 μs; four protein complexes stayed intact; four IDPs were over-compacted relative to a99SB-disp, though less so than Amber14SB. [SRC-0090, section "Protein benchmark"]
- The Garnet water model gives bulk properties similar to TIP3P, but its dielectric constant is too large because the charges are over-polarised (SPICE MBIS gives oxygen an average charge of $-0.97$ versus $-0.83$ in TIP3P). [SRC-0090, section "Protein benchmark"]
- On 8 of 58 OpenFE benchmark systems, Garnet's RBFE RMSE was 1.66 kcal mol$^{-1}$ (95% CI 1.33--1.89), compared to 1.50 for OpenFE and 1.15 for FEP+. A net-charge-change transformation caused a large cmet failure. [SRC-0090, section "Relative binding free energy benchmark"] [SRC-0091, Table 4]
- Buffered 14-7 also trained to similar loss as the double exponential; Lennard-Jones 6-9 trained with a higher intermolecular force loss; Morse, Buckingham, and Waldman--Hagler combination rules did not train or failed. [SRC-0090, section "Different functional forms"]

## Mathematical structure

### Charge prediction

Two atom features are electronegativity $e_i$ and hardness $s_i$, with $E$ the potential energy and $q_i$ the partial charge: [SRC-0090, Methods]

$$
f_1=e_i=\frac{\partial E}{\partial q_i},\qquad f_2=s_i=\frac{\partial^2 E}{\partial q_i^2}.
$$

Partial charges follow Espaloma's scheme, where $Q$ is the total charge of the molecule containing atom $i$: [SRC-0090, Methods]

$$
q_i = -e_i s_i^{-1} + s_i^{-1}\frac{Q + \sum_j e_j s_j^{-1}}{\sum_j s_j^{-1}}.
$$

### Harmonic bond and angle

$$
V(r;k_b,r_0)=\frac{k_b}{2}(r-r_0)^2,\qquad
V(\theta;k_a,\theta_0)=\frac{k_a}{2}(\theta-\theta_0)^2,
$$

with $k_b=f_1+f_2$ and $r_0=(f_1 b_1+f_2 b_2)/(f_1+f_2)$ using bounds $b_1=0.5$ Å and $b_2=3$ Å; angles use the same form with $b_1=0°$ and $b_2=180°$. [SRC-0090, Methods]

### Cosine torsion

For proper and improper torsions with periodicity $n$, parameters $k_n$ and phases $\phi_{s,n}$ (phases are fixed, not trained): [SRC-0090, Methods]

$$
V(\phi;k_n,\phi_{s,n})=\sum_{n=1}^{N}k_n\left(1+\cos(n\phi-\phi_{s,n})\right).
$$

### Double exponential potential

$$
V(r;\sigma,\epsilon,a,b)
=
\epsilon\left(
\frac{b\,e^{a}}{a-b}\exp\left[-a\frac{r}{r_m}\right]
-\frac{a\,e^{b}}{a-b}\exp\left[-b\frac{r}{r_m}\right]
\right),
\qquad r_m=2^{1/6}\sigma.
$$

$\sigma$ ranges over $0.05$--$0.5$ nm and $\epsilon$ over $0.02$--$1.5$ kJ mol$^{-1}$; $a$ and $b$ are trained global parameters (fitted to $12.2$ and $4.33$). [SRC-0090, Methods]

### Alternative non-bonded potentials

Lennard-Jones (failed to train): [SRC-0090, Methods]

$$
V(r;\sigma,\epsilon)=4\epsilon\left[\left(\frac{\sigma}{r}\right)^{12}-\left(\frac{\sigma}{r}\right)^6\right].
$$

Lennard-Jones 6-9: [SRC-0090, Methods]

$$
V(r;\sigma,\epsilon)=\frac{27}{4}\epsilon\left[\left(\frac{\sigma}{r}\right)^{9}-\left(\frac{\sigma}{r}\right)^{6}\right].
$$

Buffered 14-7, with $\rho=r/r_m$ and $r_m=2^{1/6}\sigma$: [SRC-0090, Methods]

$$
V(r;\sigma,\epsilon,\delta,\gamma)
=
\epsilon\left(\frac{1+\delta}{\rho+\delta}\right)^{7}
\left(\frac{1+\gamma}{\rho^{7}+\gamma}-2\right).
$$

Combination rules: Lorentz--Berthelot $\sigma_{ij}=\tfrac{\sigma_i+\sigma_j}{2}$, $\epsilon_{ij}=\sqrt{\epsilon_i\epsilon_j}$; geometric $\sigma_{ij}=\sqrt{\sigma_i\sigma_j}$, $\epsilon_{ij}=\sqrt{\epsilon_i\epsilon_j}$. [SRC-0090, Methods]

Urey--Bradley angle potential (trained but no improvement): [SRC-0090, Methods]

$$
V(\theta,r;k_a,\theta_0,k_u,r_0)=\frac{k_a}{2}(\theta-\theta_0)^2+\frac{k_u}{2}(r-r_0)^2.
$$

### Soft-core double exponential (RBFE)

For alchemical atoms at intermediate $0<\lambda<1$, with $a_s=(1.1+\lambda(a-1.1))$ and $b_s=(1+\lambda(b-1))$: [SRC-0090, Methods]

$$
V(r;\sigma,\epsilon,a,b,\lambda)
=
\lambda\epsilon\left(
\frac{b_s e^{a_s}}{a_s-b_s}\exp\left[-a_s\frac{r}{r_m}\right]
-\frac{a_s e^{b_s}}{a_s-b_s}\exp\left[-b_s\frac{r}{r_m}\right]
\right).
$$

### Ensemble reweighting gradient

Gradients of a trajectory-dependent loss $L(x)$ with respect to parameters $\lambda$, when the trajectory was generated with a different potential $\tilde U$: [SRC-0090, Methods]

$$
\frac{d\langle L(x)\rangle}{d\lambda}
=
-\beta\frac{\tilde Z}{Z}
\left\langle L(x)D(x;\lambda)\frac{\partial U(x;\lambda)}{\partial\lambda}\right\rangle
-\beta\frac{\tilde Z}{Z}
\left\langle L(x)D(x;\lambda)\right\rangle
\left\langle\frac{\partial U(x;\lambda)}{\partial\lambda}D(x;\lambda)\right\rangle,
$$

with $D(x;\lambda)=e^{-\beta(U(x;\lambda)-\tilde U(x))}$ and $\tilde Z/Z=1/\langle D(x;\lambda)\rangle_{\sim}$. The paper notes the actual code differed from this equation because of a mistake noticed after training. [SRC-0090, Methods]

### Karplus J-coupling

$^3J$ coupling uses $J(\theta)=A\cos^2(\theta+\Delta)+B\cos(\theta+\Delta)+C$ with $A=7.97$, $B=-1.26$, $C=0.63$, $\Delta=60°$; hydrogen-bond-mediated coupling uses $J_{HB}(R,\theta,\phi)=\exp[-k(R-R_0)]\left[(A\cos^2\phi+B\cos\phi+C)\sin^2\theta+D\cos^2\theta\right]$. [SRC-0090, Methods]

### Conformer energy deviation (DDE)

$$
\mathrm{DDE}_i=(E^{\mathrm{FF}}_i-E^{\mathrm{FF}}_{\min})-(E^{\mathrm{QM}}_i-E^{\mathrm{QM}}_{\min}).
$$

[SRC-0090, Methods]

## Equation inventory

| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |
| Charge prediction, $e_i,s_i,q_i$ | Methods | [[wiki/concepts/garnet-force-field]] | Derives charges from electronegativity/hardness. | $e_i$, $s_i$, $q_i$, $Q$ | Charge readout head; defines over-polarisation source. |
| Double exponential potential | Methods | [[wiki/concepts/double-exponential-potential]] | Non-bonded potential replacing LJ. | $r$, $\sigma$, $\epsilon$, $a$, $b$ | Custom OpenMM force; 15--20% slower than LJ. |
| Soft-core double exponential | Methods | this page | Alchemical states for RBFE. | $a_s$, $b_s$, $\lambda$ | OpenFE protocol modification. |
| Ensemble reweighting gradient | Methods | [[wiki/concepts/free-energy-reweighting-for-force-field-fine-tuning]] | Gradients through NMR/condensed-phase observables. | $D$, $\tilde Z/Z$, $\beta$ | Core of simulation-observable training. |
| Karplus couplings | Methods | this page | NMR J-coupling and H-bond couplings. | $A,B,C,\Delta$ | Loss target for GB3. |
| DDE | Methods | this page | Conformer relative-energy ranking. | $E^{\mathrm{FF}},E^{\mathrm{QM}}$ | Small-molecule benchmark metric. |

## Limitations and validation boundaries

- The small-molecule condensed-phase benchmark uses only 12 test molecules; Garnet's ΔHv and density errors are larger than OpenFF 2.2.1, indicating too-strong attractive intermolecular interactions. [SRC-0090]
- Charges are over-polarised because they were fit to gas-phase MBIS partial charges; this inflates the water dielectric constant and distorts dipole magnitude and orientation. [SRC-0090]
- Good GB3 performance may reflect overfitting, since GB3 was used during training. [SRC-0090]
- IDPs are over-compacted relative to the specialist a99SB-disp force field; it is unclear whether this stems from GB3 NMR training or from training on DFT data. [SRC-0090]
- RBFE coverage is 8 of 58 public benchmark systems; a net-charge-change transformation caused a large cmet failure (pairwise RMSE 8.26 kcal mol$^{-1}$, Kendall's $\tau$ $-0.11$). [SRC-0090] [SRC-0091, Table 4]
- Planar aromatic rings occasionally deviate from planarity during simulation. [SRC-0090]
- Supported elements (SPICE set) are listed but performance is not validated for all of them. [SRC-0090, Methods]
- Results should not be overgeneralised to universal coverage across all biomolecular species. [SRC-0090]

## Claims, questions, and tensions

- [[wiki/claims/CLM-0002-garnet-automates-parameter-assignment]]
- [[wiki/questions/garnet-validation-scope]]
- [[wiki/tensions/TEN-0002-garnet-broad-coverage-vs-validation-gaps]]

## Citation links

- [[wiki/sources/SRC-0061-openfe-rbfe-benchmark-journal-version]] - cited as the OpenFE large-scale RBFE benchmark. [SRC-0090, ref. 15]
- [[wiki/sources/SRC-0072-machine-learned-molecular-mechanics-force-fields-from-large]] - cited as the espaloma-0.3 study. [SRC-0090, ref. 16]
- [[wiki/sources/SRC-0025-building-force-fields-automatic-systematic-reproducible-approach]] - cited as the ForceBalance force-field construction approach. [SRC-0090, ref. 26]
- [[wiki/sources/SRC-0044-spice-a-dataset-of-drug-like-molecules-and]] - cited as the SPICE quantum-chemical dataset. [SRC-0090, ref. 40]
- [[wiki/sources/SRC-0046-the-maximal-and-current-accuracy-of-rigorous-protein]] - cited as the FEP+ accuracy benchmark. [SRC-0090, ref. 56]
- [[wiki/sources/SRC-0021-tuning-potential-functions-host-guest-binding-data]] and [[wiki/sources/SRC-0016-fine-tuning-mm-force-fields-to-experimental-free-energies]] - cited for fitting force fields to experimental free-energy data. [SRC-0090, refs. 66--67]
- [[wiki/sources/SRC-0023-statistically-optimal-analysis-multiple-equilibrium-states-mbar]] - cited for multistate Bennett acceptance ratio. [SRC-0090, ref. 68]
- [[wiki/sources/SRC-0043-structure-based-experimental-datasets-for-benchmarking-protein-simulation]] - cited for protein force-field benchmark data. [SRC-0090, ref. 75]
- Citation review is partial: only strong title/DOI matches against already-ingested sources were recorded.

## Code and data

- Garnet force field, training scripts, validation scripts, and data: `https://github.com/greener-group/garnet` (permissive licence).
- Modified RBFE protocol: `https://github.com/greener-group/openfe`.
- Molly.jl: `https://github.com/JuliaMolSim/Molly.jl`.
- The model is trained in Julia (Molly.jl, Enzyme.jl, Zygote.jl) and converted to PyTorch for inference in the OpenFF/OpenMM ecosystems. [SRC-0090, Methods]

## Metadata notes

- Received 7 April 2026; accepted 6 September 2026; published 17 September 2026. [SRC-0090]
- Published by the Royal Society of Chemistry under CC-BY 4.0. Corresponding author Joe G. Greener, MRC Laboratory of Molecular Biology, Cambridge, UK; Alexandre Blanco-González and Thea K. Schulze contributed equally. [SRC-0090]
- This is the peer-reviewed journal version of the arXiv preprint ingested as [[wiki/sources/SRC-0003-training-a-force-field-from-scratch]]. The scientific content is largely shared; this source adds the final DOI, venue, licence, author-contribution statement, and the supplementary information.

## Ingestion QA

### Retrieval questions checked

- What is Garnet and what does the paper contribute?
- Which training data and signals are used?
- Why is the double exponential potential used instead of Lennard-Jones?
- How are charges predicted, and what causes their over-polarisation?
- Which benchmark families are reported, and what do they show?
- What are the quantitative RBFE results and the cmet failure?
- What condensed-phase small-molecule results are reported?
- What limitations and validation boundaries are stated?
- How does this source relate to the arXiv preprint SRC-0003?

### Coverage decision

`math-standard`. The source page captures the central contribution, key equations (charge, bond/angle/torsion, non-bonded functional forms, soft-core, ensemble reweighting, Karplus, DDE), benchmark results, limitations, citation links, and the preprint relationship. Detailed numerical tables remain in the raw source and are partly summarised on the supplement page.

### Known gaps

- Full SPICE Table 1 numeric values and per-motif enrichment tables remain in the raw source / supplement.
- The ensemble reweighting code discrepancy noted in the paper is preserved as a caveat, not resolved.
- RBFE results are summarised at benchmark-family level, not per-ligand-pair.
- The preprint SRC-0003 already holds extensive cross-linked concept coverage; this page adds the published-version provenance and the equations not otherwise represented.
