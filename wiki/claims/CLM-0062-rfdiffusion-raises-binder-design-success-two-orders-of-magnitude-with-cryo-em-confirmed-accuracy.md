---
type: claim
status: active
created: 2026-10-12
updated: 2026-10-12
claim_status: supported
claim_scope: validation
areas:
  - research
categories:
  - research/biomolecules/proteins
  - research/machine-learning/molecular-modeling
  - research/experimental-benchmarking
tags:
  - claim
  - protein-design
  - diffusion-model
  - binder-design
  - validation
related:
  - "[[wiki/concepts/rfdiffusion-diffusion-based-de-novo-protein-design]]"
sources:
  - SRC-0104
sensitivity: public
encryption: none
---

# RFdiffusion Raises Binder-Design Success Two Orders of Magnitude, With Cryo-EM-Confirmed Atomic Accuracy

## Claim

RFdiffusion, fine-tuned on protein-complex structures and conditioned on target "interface hotspot" residues, combined with AlphaFold2 (AF2)-based confidence filtering, raises experimental de novo protein-binder design success rates by roughly two orders of magnitude over a prior physics-based (Rosetta) target-structure-only binder-design method on the same targets, identifying nanomolar-affinity binders from fewer than 100 designs per target where the prior method required screening thousands; the atomic-level accuracy of a resulting design was independently confirmed by a 2.9 Å cryo-EM structure matching the design model to 0.63 Å backbone RMSD. [SRC-0104]

## Evidence

- Across five targets (influenza HA, IL-7Rα, PD-L1, InsR, TrkA), single-point biolayer interferometry (BLI) screening at 10 μM gave an overall experimental hit rate (≥ 50% of positive-control response) of ~19%, with binders identified for every target from fewer than 100 designs tested per target, versus the prior Rosetta-based method's reliance on screening many thousands of designs per campaign on the same four shared targets (IL-7Rα, InsR, PD-L1, TrkA). [SRC-0104, p. 1097]
- The authors estimate what the Rosetta-based campaigns' success rates would have been had AF2 filtering been applied retrospectively: HA 0%, IL-7Rα 2.2%, InsR 5.5%, PD-L1 3.7%, TrkA 1.5% — all below RFdiffusion's observed rates — and attribute roughly one order of magnitude of the overall improvement to RFdiffusion itself and the second order of magnitude to AF2-based filtering. [SRC-0104, p. 1097, Fig. 6b]
- Several designed binders reached nanomolar affinity with no further experimental optimization, e.g. ~30 nM for HA and IL-7Rα hits (BLI titration). [SRC-0104, p. 1097]
- The highest-affinity influenza-HA binder (HA_20, Kd = 28 nM by BLI) was solved in complex with Iowa/43 HA by cryo-EM: a C3-symmetric, 2.9 Å reconstruction showed full occupancy of all three HA stem epitopes, with the resulting structure matching the RFdiffusion design model to 0.63 Å backbone RMSD over the complex (0.6 Å over the binder alone); the designed interface's side-chain contacts were markedly different from the nearest structural homolog in the PDB. [SRC-0104, p. 1098]

## Implementation Use

For target-conditioned de novo protein-binder design pipelines, this result supports: (1) fine-tuning a backbone-generation diffusion model on protein-complex structures with an explicit "interface hotspot" conditioning feature to steer binders toward a specific site on the target, rather than relying on unconditional generation plus post hoc filtering; and (2) pairing generative backbone design with AF2-based interface/monomer confidence filtering before experimental testing, which the authors attribute roughly half of the total success-rate improvement to on its own. The practical implication is that high-affinity binders to a new target can plausibly be identified by screening on the order of tens to ~100 designs, rather than thousands, for target sites resembling those tested here. [SRC-0104]

## Caveats

- The two-orders-of-magnitude comparison is made against one specific prior method (a Rosetta-based, target-structure-only pipeline) on specific targets; it is not a comparison against all possible alternative binder-design approaches. [SRC-0104, p. 1097]
- All five targeted sites are described by the authors as "non-polar sites"; they explicitly state further studies are needed to assess success rates on more polar target sites and on targets without known native binding partners, so the magnitude of improvement should not be assumed to generalize to such cases. [SRC-0104, p. 1098]
- Binder specificity (vs. off-target or proteome-wide binding) was assessed for only a subset of designs (six IL-7Rα binders, via competition BLI against one validated positive control); the authors explicitly flag that "further work is required to fully characterize proteome-wide specificity." [SRC-0104, p. 1098]
- The reported 19% hit rate is noted by the authors as a conservative estimate, since some designs that showed binding lacked sufficient material to be screened at the full 10 μM concentration. [SRC-0104, p. 1097]
- The cryo-EM confirmation (0.63 Å RMSD) is reported for a single designed complex (HA_20/HA), not as a systematic structural-validation statistic across all designed binders. [SRC-0104, p. 1098]

## Links

- [[wiki/sources/SRC-0104-de-novo-design-of-protein-structure-and-function]]
- [[wiki/concepts/rfdiffusion-diffusion-based-de-novo-protein-design]]
- [[wiki/claims/CLM-0061-rfdiffusion-self-conditioning-and-mse-loss-are-necessary-for-design-quality]]
