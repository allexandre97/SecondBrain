---
type: claim
status: active
created: 2026-07-02
updated: 2026-07-02
claim_status: supported
claim_scope: interpretation
areas:
  - research
categories:
  - research/biomolecules/proteins
  - research/experimental-benchmarking
tags:
  - claim
  - missense-variants
  - protein-stability
  - clinical-variants
related:
  - "[[wiki/concepts/human-domainome-variant-stability-mapping]]"
sources:
  - SRC-0071
sensitivity: public
encryption: none
---

# Stability Explains Many but Not All Missense Effects

## Claim

Protein destabilization explains a large fraction of pathogenic missense effects, but stability is not a universal mechanism: many clinically or evolutionarily important variants affect function through binding, active sites, allostery, localization, aggregation, gain of function, or full-length context. [SRC-0071]

## Evidence

- SRC-0071 estimates that about 60% of pathogenic missense variants reduce protein stability. [SRC-0071]
- The contribution of stability varies across proteins, diseases, structural classes, and inheritance modes, with particularly strong contribution in recessive disorders. [SRC-0071]
- Residual analysis after fitting abundance-stability effects to ESM1v evolutionary-fitness predictions enriches for annotated functional sites, indicating non-stability functional effects. [SRC-0071]
- The discussion explicitly identifies isolated-domain context and non-abundance traits such as binding, localization, aggregation, and allostery as remaining measurement needs. [SRC-0071]

## Implementation Use

For clinical variant interpretation or model benchmarking, treat stability data as a major mechanistic feature rather than a complete label. Variant-effect workflows should keep separate evidence channels for stability, molecular function, interaction interfaces, regulatory context, and disease mechanism. [SRC-0071]

## Links

- [[wiki/sources/SRC-0071-site-saturation-mutagenesis-of-500-human-protein-domains]]
- [[wiki/concepts/human-domainome-variant-stability-mapping]]
