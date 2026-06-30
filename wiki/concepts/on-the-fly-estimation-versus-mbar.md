---
type: concept
status: active
created: 2026-06-29
updated: 2026-06-29
areas:
  - research
categories:
  - research/statistics/monte-carlo
  - research/molecular-simulation/free-energy
tags:
  - on-the-fly-estimation
  - mbar
  - asymptotic-variance
  - math-heavy
related:
  - "[[sources/SRC-0005-times-square-sampling-free-energy]]"
  - "[[sources/SRC-0006-times-square-sampling-supplement]]"
  - "[[concepts/times-square-sampling]]"
  - "[[concepts/free-energy-estimation]]"
  - "[[concepts/adaptive-enhanced-sampling]]"
  - "[[questions/tss-generalization-scope]]"
sources:
  - SRC-0005
  - SRC-0006
sensitivity: public
encryption: none
---

# On-the-Fly Estimation Versus the Multistate Bennett Acceptance Ratio

## Summary

SRC-0005 argues that on-the-fly free energy estimation can sometimes achieve lower asymptotic variance than the multistate Bennett acceptance ratio estimator because the sampler can use current estimates while generating future samples. [SRC-0005]

## Key Points

- MBAR is a maximum-likelihood estimator used after samples are available; in chemical physics it is commonly used for free energy estimation across multiple states. [SRC-0005, introduction]
- TSS updates estimates during sampling, so estimate information changes the future distribution of samples. [SRC-0005, section 2.2.3]
- The paper calls this variance-reducing feedback self-adjustment. [SRC-0005, section 2.2.3]
- The supplement proves a general variance comparison under stated assumptions using overlap matrices and asymptotic covariance expressions. [SRC-0006, section 4.5]
- The claim does not mean MBAR is generally inferior; it applies to settings where sample generation itself can exploit adaptive estimate information. [SRC-0005, proposition 3] [SRC-0006, section 4.5]

## Core equations

TSS asymptotic covariance under the independent-sample setup is identified with an overlap matrix expression in the supplement. [SRC-0006, sections 4.1 and 4.5]

$$
\Sigma_{TSS}=O.
$$

The MBAR covariance is expressed as: [SRC-0006, section 4.2]

$$
\Sigma_{MBAR}=(\Pi-\Pi O\Pi)^+ - \Pi^{-1}.
$$

The variance of a free-energy difference is evaluated by a quadratic form: [SRC-0006, section 4.5]

$$
Var(F_j-F_i)=(e_j-e_i)^T\Sigma(e_j-e_i).
$$

The theorem's comparison target is positive semidefiniteness of the difference: [SRC-0006, section 4.5]

$$
(e_j-e_i)^T(\Sigma_{MBAR}-\Sigma_{TSS})(e_j-e_i) \ge 0.
$$

## Variable glossary

- `MBAR`: multistate Bennett acceptance ratio estimator, treated as a maximum-likelihood estimator in the source. [SRC-0005, introduction]
- $\Sigma_{TSS}$: asymptotic covariance of TSS free-energy difference estimates under the theorem setup. [SRC-0006, section 4]
- $\Sigma_{MBAR}$: asymptotic covariance of the MBAR estimator. [SRC-0006, section 4.2]
- $O$: overlap matrix between distributions. [SRC-0006, section 4.5]
- $\Pi$: diagonal matrix of sampling proportions. [SRC-0006, section 4.2]
- $\nu$: number of repeated sampler moves per estimator update interval in self-adjustment examples. [SRC-0005, section 2.2.3] [SRC-0006, section 10.2.3]

## Derivation sketch

The supplement derives covariance formulas for stochastic approximation and maximum likelihood estimation, specializes them to TSS and MBAR, and then proves the covariance difference has the required nonnegative quadratic form for free-energy differences when the overlap matrix is irreducible and the sampling assumptions hold. [SRC-0006, sections 4.1-4.5]

The intuition is not that post-processing has become worse. Instead, TSS changes the sampling process itself: future samples are drawn from a distribution influenced by current free-energy estimates, and that information is unavailable to MBAR when it receives a fixed sample set after the fact. [SRC-0005, section 2.2.3]

## Implementation consequences

- Repeating rung moves between global estimator updates can capture much of the variance benefit when rung moves are cheap and communication is expensive. [SRC-0005, section 4.3] [SRC-0006, section 10.2.3]
- The supplement's high-frequency kernel breaks one long MD interval into $\nu$ smaller pieces followed by intermediate rung moves while keeping the estimator-update interval fixed. [SRC-0006, eqs. 10.1-10.2]

## Caveats

- The variance theorem assumes independent samples from the relevant distributions and an irreducible overlap matrix; practical Markov-chain and MD samples are correlated. [SRC-0006, section 4.5]
- The source's MBAR comparison is a bounded mathematical claim, not a blanket replacement argument. [SRC-0005, proposition 3]
- The supplement's molecular-dynamics example is supportive evidence for self-adjustment but not broad benchmarking across applications. [SRC-0006, section 10.2.3]

## Evidence

- Proposition 3 in SRC-0005 states that, under its setup with independent samples from the adaptive target used by TSS, the asymptotic variance of a free energy difference is smaller than that of MBAR. [SRC-0005, proposition 3]
- The supplement proves the result as Theorem 4.1 and gives the covariance algebra. [SRC-0006, section 4.5]
- The numerical sections show that increasing the number of sampler moves per estimator update can reduce errors, consistent with the self-adjustment argument. [SRC-0005, section 4.3] [SRC-0006, section 10.2.3]

## Links

- [[sources/SRC-0005-times-square-sampling-free-energy]]
- [[sources/SRC-0006-times-square-sampling-supplement]]
- [[concepts/times-square-sampling]]
- [[concepts/free-energy-estimation]]
- [[concepts/adaptive-enhanced-sampling]]
- [[questions/tss-generalization-scope]]

## Open Questions

- Which other maximum-likelihood-style estimators can be improved by making the sampling process adaptive rather than only changing the post-processing estimator? [SRC-0005]
