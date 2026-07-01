---
type: claim
status: active
created: 2026-07-01
updated: 2026-07-01
claim_status: supported
claim_scope: implementation
areas:
  - research
categories:
  - research/molecular-simulation/free-energy
tags:
  - claim
  - solvation-free-energy
  - decoupling
  - LAMMPS
related:
  - "[[wiki/concepts/solvation-free-energy-decoupling-in-lammps]]"
  - "[[wiki/questions/md-free-energy-decoupling-implementation-validation]]"
sources:
  - SRC-0047
sensitivity: public
encryption: none
---

# Decoupling Implementations Must Preserve Intramolecular Solute Terms

## Claim

Alchemical decoupling implementations must preserve solute intramolecular interactions while staging solute-environment interactions; in LAMMPS charge scaling needs an overlay correction to avoid unintentionally scaling intramolecular Coulomb energy. [SRC-0047]

## Evidence

- SRC-0047 distinguishes decoupling from annihilation by retaining intramolecular solute interactions while modulating interactions with the surrounding solution. [SRC-0047]
- In LAMMPS, scaling solute charges stages long-range solute-solvent electrostatics but also scales solute intramolecular Coulomb terms. [SRC-0047]
- The overlay correction adds the missing intramolecular Coulomb energy and is expressed by the factor $(1-\lambda_q^2)$ over intramolecular charge pairs. [SRC-0047, eq. 7]

## Implementation Use

For Molly/Enzyme/MD work, treat "scale charge" as an implementation operation whose side effects must be audited against the intended alchemical Hamiltonian. The reusable pattern is to identify any internal terms affected by a convenient global operation and add an explicit compensating term if the target thermodynamic path requires them to remain fixed. [SRC-0047]

## Caveats

The source demonstrates the correction for two hydration examples and thermodynamic integration; broader estimator and system coverage remains an implementation-validation question. [SRC-0047]

## Links

- [[wiki/sources/SRC-0047-performing-solvation-free-energy-calculations-in-lammps-using]]
- [[wiki/concepts/solvation-free-energy-decoupling-in-lammps]]
- [[wiki/questions/md-free-energy-decoupling-implementation-validation]]
