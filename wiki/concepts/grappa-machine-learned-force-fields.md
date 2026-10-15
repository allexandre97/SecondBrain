---
type: concept
status: active
created: 2026-10-12
updated: 2026-10-12
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/machine-learning/molecular-modeling
  - research/machine-learning/scientific-modeling
tags:
  - grappa
  - force-fields
  - graph-neural-networks
  - nonbonded-parameters
  - partial-charges
  - lennard-jones
related:
  - "[[wiki/concepts/espaloma-machine-learned-mm-force-fields]]"
  - "[[wiki/concepts/automated-force-field-training]]"
  - "[[wiki/concepts/garnet-force-field]]"
  - "[[wiki/concepts/double-exponential-potential]]"
  - "[[wiki/claims/CLM-0057-grappa-fullff-jointly-learns-nonbonded-parameters-without-degrading-bonded-accuracy]]"
  - "[[wiki/claims/CLM-0058-grappa-matches-or-exceeds-espaloma-accuracy-at-mm-cost-and-extends-to-new-chemistries]]"
  - "[[wiki/sources/SRC-0098-graph-nets-partial-charge-prediction]]"
sources:
  - SRC-0101
  - SRC-0102
sensitivity: public
encryption: none
---

# Grappa Machine-Learned Force Fields

## Summary

Grappa is a family of graph-attention models that predict classical molecular-mechanics (MM) force-field parameters from molecular topology. `grappa-bonded` (Seute, Hartmann, Stühmer & Gräter, Chemical Science 2025, doi `10.1039/d4sc05465b`, [[wiki/sources/SRC-0102-grappa-a-machine-learned-molecular-mechanics-force-field|SRC-0102]]) predicts bonded parameters (bond, angle, dihedral, improper) using a shared graph-attention encoder followed by four "symmetric transformer" heads, while using externally assigned nonbonded (partial-charge and Lennard-Jones) parameters, achieving state-of-the-art bonded-parameter accuracy at the same computational cost as traditional MM. `grappa-fullFF` (SRC-0101) extends the same shared encoder architecture with two additional heads so that nonbonded parameters are predicted and trained jointly and consistently with the bonded parameters, directly from quantum-mechanical (QM) energies and forces, without relying on any externally assigned nonbonded parameters. [SRC-0102] [SRC-0101]

## Key Points

- Both Grappa variants share a graph-attention encoder (4 layers, GAT-style local attention) that produces atom embeddings, from which per-interaction-type "symmetric transformer" heads read out bond, angle, dihedral (torsion), and improper-dihedral parameters. Each head adds a permutation-invariant positional encoding and sums an MLP over the relevant symmetry group so the predicted parameters respect the required invariances (e.g. $\xi^{(\mathrm{bond})}_{ij}=\xi^{(\mathrm{bond})}_{ji}$); impropers are not invariant under all permutations that fix the central atom, so Grappa predicts two force constants per improper and combines them to restore invariance. [SRC-0102]
- `grappa-bonded`'s only input features are atomic number, ring/loop membership, node degree, and the partial charge received from whichever nonbonded scheme it is paired with — no hand-crafted hybridization or aromaticity features — which the paper argues is what makes the architecture both accurate and easy to extend to new chemistries. [SRC-0102]
- On the Espaloma-0.3 benchmark (17,427 molecules, >1,000,000 conformations of small molecules, peptides, and RNA), `grappa-bonded` matches or exceeds Espaloma-0.3's energy/force accuracy and substantially exceeds traditional force fields GAFF-2.11, ff99SB-ILDN/ff14SB, and RNA.OL3, while being retrainable to stay consistent with different nonbonded schemes (AM1-BCC, ff99SB, CHARMM36) at closely matched accuracy. [[wiki/claims/CLM-0058-grappa-matches-or-exceeds-espaloma-accuracy-at-mm-cost-and-extends-to-new-chemistries]]
- `grappa-bonded` extends to peptide radicals (a chemistry absent from its original training data) with a modest purpose-built dataset, without degrading accuracy on the original Espaloma-derived test sets, and reproduces downstream experimental/MD observables: protein backbone *J*-couplings (better agreement with experiment than Espaloma-0.3 and Amber ff14SB), chignolin folding free energy, ubiquitin stability over 200 ns, and stability of a one-million-atom virus (STMV) simulation at ~101 timesteps/second on a single A100 GPU. [SRC-0102]
- `grappa-bonded` reproduces the diagonal $\alpha_R$-helix basin shape and $\alpha$-helix/$\beta$-sheet transition region of Amber ff19SB's relaxed backbone-dihedral free-energy landscape *without* requiring ff19SB's residue-specific CMAP correction maps, by jointly tuning dihedral, angle, and neighboring-term parameters together rather than fitting each bonded term separately — an advantage the authors attribute to learning all bonded parameters jointly, as in both Grappa and Espaloma, rather than separately as in conventional force-field fitting. [SRC-0102]
- `grappa-fullFF` adds two heads on top of the unchanged `grappa-bonded` bonded-parameter heads: an antisymmetric bond-charge-flux head for partial charges, and a Tkatchenko-Scheffler van der Waals (TS-vdW) volume-ratio head for Lennard-Jones parameters. [SRC-0101]
- The partial-charge head predicts charge *flux* $w_{ij}$ transferred between bonded atom pairs at each message-passing refinement step, antisymmetric under atom-index permutation ($w_{ij} = -w_{ji}$), so total molecular charge is conserved by construction. This follows the classical Bond-Charge Increment (BCI) idea (Halgren's MMFF94), not charge equilibration (QEq). It is a distinct mechanism from the electronegativity/hardness QEq solve used by Espaloma and by the graph-net charge model of Wang et al.; see [[wiki/concepts/espaloma-machine-learned-mm-force-fields]] and [[wiki/sources/SRC-0098-graph-nets-partial-charge-prediction]] for the QEq alternative. [SRC-0101] [SRC-0098]
- The Lennard-Jones head predicts a per-atom effective/free atomic-volume ratio $v_i$, which is mapped to $\sigma$ and $\epsilon$ through the physically motivated TS-vdW relation $\sigma \propto v_i^{1/7}$, $\epsilon \propto C_6^{\mathrm{eff}}/\sigma^6$, rather than predicting $\sigma,\epsilon$ directly. [SRC-0101]
- Because QM energies and forces alone cannot uniquely determine how total energy splits between bonded and nonbonded contributions ("energy degeneracy"), `grappa-fullFF` adds two physics-informed regularization losses, evaluated on the subset of conformers with available QM electron densities: an electrostatic-potential (ESP) loss matching predicted-charge ESP to the QM reference ESP, and a volume-ratio loss matching predicted $v_i$ to MBIS-partitioned reference ratios. Partial charges are deliberately *not* supervised directly against reference atomic charges in the main model. [SRC-0101]
- `grappa-fullFF` is trained and evaluated on the DES-monomer, dipeptide, and PubChem subsets of SPICE with OMol25 QM energies/forces (ωB97M-V/def2-TZVPD), the same filtering used for Espaloma and `grappa-bonded` comparisons (10,240 unique molecules, ~441,000 conformers; a 14,600-conformer subset has usable electron densities for the ESP/volume-ratio losses). [SRC-0101]
- `grappa-fullFF` matches `grappa-bonded`'s state-of-the-art geometry-optimization accuracy on the OpenFF Industry Benchmark and reproduces the alanine-dipeptide Ramachandran free-energy surface about twice as accurately as espaloma-0.3.2, despite training only on gas-phase monomers (not on explicit-solvent configurations). [[wiki/claims/CLM-0057-grappa-fullff-jointly-learns-nonbonded-parameters-without-degrading-bonded-accuracy]]
- Garnet (a separate graph-neural-network force field) also jointly trains bonded and nonbonded parameters including water, but uses a different nonbonded functional form (a double-exponential potential) and a broader training signal including condensed-phase and protein NMR data, rather than Grappa's TS-vdW/ESP-regularized Lennard-Jones-and-charge-flux approach. [[wiki/concepts/garnet-force-field]] [[wiki/concepts/double-exponential-potential]] [SRC-0101]

## Evidence

See the full result tables transcribed in the respective source pages: `grappa-bonded`'s Espaloma-benchmark, radical-extensibility, nonbonded-scheme-ablation, finetuning, and bootstrapped-uncertainty tables in [[wiki/sources/SRC-0102-grappa-a-machine-learned-molecular-mechanics-force-field]]; `grappa-fullFF`'s ESP/dipole accuracy, geometry-optimization benchmark, Ramachandran free-energy divergence, and regularization-ablation tables in [[wiki/sources/SRC-0101-learning-consistent-molecular-mechanics-force-fields-from-first]].

## Links

- [[wiki/sources/SRC-0102-grappa-a-machine-learned-molecular-mechanics-force-field]]
- [[wiki/sources/SRC-0101-learning-consistent-molecular-mechanics-force-fields-from-first]]
- [[wiki/concepts/espaloma-machine-learned-mm-force-fields]]
- [[wiki/concepts/automated-force-field-training]]
- [[wiki/concepts/garnet-force-field]]
- [[wiki/concepts/double-exponential-potential]]
- [[wiki/sources/SRC-0098-graph-nets-partial-charge-prediction]]
- [[wiki/claims/CLM-0057-grappa-fullff-jointly-learns-nonbonded-parameters-without-degrading-bonded-accuracy]]
- [[wiki/claims/CLM-0058-grappa-matches-or-exceeds-espaloma-accuracy-at-mm-cost-and-extends-to-new-chemistries]]

## Caveats

- `grappa-bonded` predicts only bonded parameters; its own accuracy is partly contingent on the quality of whichever externally assigned nonbonded scheme it is paired with. This limitation is what motivated `grappa-fullFF`. [SRC-0102] [SRC-0101]
- `grappa-fullFF`'s nonbonded regularization requires QM electron-density data (for ESP and MBIS volume-ratio references) in addition to energies and forces, which is a more expensive data requirement than energy/force-only training. [SRC-0101]
- Efficiency comparisons of Grappa against E(3)-equivariant models (Allegro) use published numbers from different studies and hardware configurations rather than a matched, controlled benchmark. [SRC-0102]

## Open Questions

- Does extending `grappa-fullFF` training to explicit-solvent or other condensed-phase configurations further close the small remaining Ramachandran-FES gap relative to `grappa-bonded` plus empirical nonbonded parameters? [SRC-0101, Discussion]
- How would the antisymmetric bond-charge-flux charge model compare to QEq-style charge models under larger conformational or environmental polarization changes? [SRC-0101]
