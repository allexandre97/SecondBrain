---
type: source
status: active
created: 2026-07-01
updated: 2026-07-01
source_id: SRC-0065
display_title: "MACE-MDP: A Foundation Model for Molecular Dipole Moments and Polarizabilities"
short_title: "MACE-MDP"
aliases:
  - "SRC-0065"
  - "MACE-MDP"
  - "MACE-MDP: A Foundation Model for Molecular Dipole Moments and Polarizabilities"
source_path: raw/sources/SRC-0065-mace-mdp-molecular-dipole-moments-polarizabilities.pdf
imported_path: raw/sources/SRC-0065-mace-mdp-molecular-dipole-moments-polarizabilities.pdf
original_filename: "chemrxiv.15000716_v1.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 7374fa7effc4df9c0dfd08239f0db423a58670e1c08fc93121ec26a35ae55757
areas:
  - research
categories:
  - research/machine-learning/molecular-modeling
  - research/molecular-simulation/datasets
  - research/molecular-simulation/force-fields
  - research/experimental-benchmarking
tags:
  - preprint
  - MACE
  - MACE-MDP
  - SPICE-alpha
  - dipole-moments
  - polarizabilities
  - vibrational-spectroscopy
related:
  - "[[wiki/concepts/molecular-response-property-foundation-models]]"
  - "[[wiki/concepts/machine-learning-potential-datasets]]"
  - "[[wiki/concepts/machine-learned-interatomic-potential-foundation-models]]"
sources:
  - SRC-0065
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: standard
peer_review_status: not-peer-reviewed
---

# MACE-MDP: A Foundation Model for Molecular Dipole Moments and Polarizabilities

Source ID: `SRC-0065`

## Raw source

- Repository path: `raw/sources/SRC-0065-mace-mdp-molecular-dipole-moments-polarizabilities.pdf`
- Open raw source: [raw/sources/SRC-0065-mace-mdp-molecular-dipole-moments-polarizabilities.pdf](../../raw/sources/SRC-0065-mace-mdp-molecular-dipole-moments-polarizabilities.pdf)

## Status note

This is a ChemRxiv preprint posted on 2026-03-09 under CC-BY 4.0 and explicitly marked as not peer reviewed. Treat its data and conclusions as preliminary until peer-reviewed or otherwise independently validated. [SRC-0065]

The user-provided path pointed to a missing `Fibres/` subdirectory; the matching filename was found and ingested from the parent `Papers/` directory. The absolute path is intentionally omitted from wiki metadata. [SRC-0065]

## Summary

Gonnheimer, Reuter, Kapil, and Margraf introduce MACE-MDP, a MACE-based foundation model for predicting molecular dipole moments and fully anisotropic polarizability tensors. The work extends SPICE into SPICE-alpha by adding first-principles polarizabilities, trains an equivariant model for joint dipole/polarizability prediction, and evaluates zero-shot vibrational spectroscopy workflows for gas-phase molecules, non-covalent trimers, and molecular-crystal Raman spectra. [SRC-0065]

## Key Points

- The motivation is that many foundation-scale MLIPs predict potential-energy surfaces, energies, and forces, but not electronic response properties needed for IR, Raman, dielectric, and field-driven applications. [SRC-0065]
- SPICE-alpha augments SPICE v2.0 with molecular polarizabilities computed at the omegaB97M-D3(BJ)/def2-TZVPPD level for organic molecules, dimers, and solvated complexes. [SRC-0065]
- MACE-MDP is trained on roughly 1.5 million neutral organic structures from SPICE-alpha using a 90/5/5 split and predicts total dipole moments plus full polarizability tensors. [SRC-0065]
- The MACE-mu-alpha architecture modifies the MACE readout to produce charge-like scalar terms, local dipoles, isotropic polarizability terms, and anisotropic rank-2 polarizability terms. [SRC-0065]
- Test-set errors are reported as RMSE 0.017 e Angstrom for dipoles, 0.017 e Angstrom squared per volt for diagonal polarizability elements, and 0.012 e Angstrom squared per volt for off-diagonal polarizability elements. [SRC-0065]
- When combined with molecular MLIPs, MACE-MDP predicts harmonic Raman and IR spectra for the IR-R-7193 dataset with high match scores, especially using MACE-OFF23(L). [SRC-0065]
- On non-covalent molecular trimers, Raman-spectrum errors are reported to be driven mostly by the underlying MLIP's force/frequency errors rather than by polarizability prediction alone. [SRC-0065]
- For aspirin and paracetamol crystal polymorphs, MACE-MDP combined with fine-tuned MACE potentials gives encouraging anharmonic Raman spectra, including clear paracetamol polymorph identification, while aspirin remains harder because polymorph spectral differences are subtle. [SRC-0065]

## Limitations and Caveats

- The source is a preprint and has not been peer reviewed. [SRC-0065]
- Training uses neutral organic systems; the paper excludes open-shell IR-R-7193 systems from spectral analysis because the models were trained on closed-shell systems. [SRC-0065]
- Molecular-crystal performance is limited by the underlying potential-energy surface and by missing molecular-crystal response-property data in training. [SRC-0065]
- Non-covalent trimer Raman spectra have lower match scores than isolated molecules because small force errors can shift soft intermolecular vibrational modes. [SRC-0065]
- The paper argues the polarizability model transfers from monomers/dimers to trimers, but further weakly interacting-system data or fine-tuning may improve difficult cases. [SRC-0065]

## Links

- [[wiki/concepts/molecular-response-property-foundation-models]]
- [[wiki/concepts/machine-learning-potential-datasets]]
- [[wiki/concepts/machine-learned-interatomic-potential-foundation-models]]
- [[wiki/sources/SRC-0044-spice-a-dataset-of-drug-like-molecules-and]]

## Metadata notes

- DOI shown by the source: `10.26434/chemrxiv.15000716/v1`.
- Code/data availability in the source points to Zenodo for SPICE-alpha, IR-R-7193, and R-3B69; a GitHub repository for MACE-MDP; and the MACE package implementation as `AtomicDieletricMACE`. [SRC-0065]

## Ingestion QA

### Retrieval questions checked

- What does MACE-MDP predict?
- What problem does it address relative to foundation MLIPs?
- What is SPICE-alpha?
- How does the MACE-mu-alpha readout represent dipoles and polarizabilities?
- What benchmarks are used for gas-phase molecules, trimers, and crystals?
- What limitations affect non-covalent trimers and molecular crystals?
- Is the source peer reviewed?
- What claims should not be overgeneralized?

### Coverage decision

Complete at `coverage_profile: standard`. The page captures the source status, dataset/model contribution, architectural idea, benchmark scope, validation results, limitations, and links to durable dataset and foundation-model concepts.

### Known gaps

- The wiki does not reproduce the full mathematical derivation, supporting information, all benchmark tables, or code/data URLs beyond a summary.
- Exact SI details for MACE-mu-alpha and anharmonic Raman setup are summarized only at a high level.
