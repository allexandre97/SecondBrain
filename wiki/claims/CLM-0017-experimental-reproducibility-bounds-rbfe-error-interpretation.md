---
type: claim
status: active
created: 2026-07-01
updated: 2026-07-01
claim_status: limited
claim_scope: cross-source
areas:
  - research
categories:
  - research/molecular-simulation/free-energy
  - research/computational-drug-discovery
  - research/experimental-benchmarking
tags:
  - claim
  - rbfe
  - experimental-reproducibility
  - benchmarking
related:
  - "[[wiki/concepts/relative-binding-free-energy-benchmarking]]"
  - "[[wiki/questions/rbfe-benchmark-prospective-use-scope]]"
sources:
  - SRC-0045
  - SRC-0046
  - SRC-0061
sensitivity: public
encryption: none
---

# Experimental Reproducibility Bounds RBFE Error Interpretation

## Claim

RBFE benchmark error cannot be interpreted without experimental reproducibility and assay heterogeneity, because experimental relative-affinity data impose an error floor and can make physically reasonable predictions look wrong. [SRC-0046] [SRC-0061]

## Scope

This claim applies to protein-ligand RBFE and FEP benchmark interpretation, especially when comparing simulation predictions against heterogeneous assay-derived affinities. It does not claim that all experimental disagreement is experimental noise. [SRC-0046]

## Evidence

- SRC-0046 estimates experimental relative-affinity reproducibility and compares it with FEP+ benchmark accuracy, framing experimental repeatability as a practical upper bound on interpretable FEP accuracy. [SRC-0046, table 3]
- SRC-0046 notes that assay measurements can differ substantially, so benchmark errors mix simulation error with experimental reproducibility limits. [SRC-0046]
- SRC-0061 treats assay-limit data and private benchmark assay heterogeneity as part of why blinded active-project benchmark interpretation is harder than public curated benchmarking. [SRC-0061, sections 3.2 and 4.2]
- SRC-0045 reports the same public/private contrast in the earlier OpenFE benchmark preprint. [SRC-0045]

## Caveats

- Experimental reproducibility is not a permission to ignore simulation failures; it is a required context for deciding which discrepancies are scientifically meaningful. [SRC-0046] [SRC-0061]

## Links

- [[wiki/sources/SRC-0046-the-maximal-and-current-accuracy-of-rigorous-protein]]
- [[wiki/sources/SRC-0061-openfe-rbfe-benchmark-journal-version]]
- [[wiki/concepts/relative-binding-free-energy-benchmarking]]
- [[wiki/questions/rbfe-benchmark-prospective-use-scope]]
