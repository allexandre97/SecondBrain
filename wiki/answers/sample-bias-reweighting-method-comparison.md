---
type: answer
status: active
created: 2026-07-01
updated: 2026-07-02
question: "How do TSS, AWH, OPES, MBAR, LaDyBUGS, and Boltzmann generators differ in how they use samples, biasing, reweighting, and validation diagnostics?"
answer_status: answered
areas:
  - research
categories:
  - research/molecular-simulation/free-energy
  - research/adaptive-sampling
  - research/statistics/monte-carlo
  - research/machine-learning/molecular-modeling
tags:
  - free-energy-estimation
  - adaptive-sampling
  - reweighting
  - biasing
  - mbar
  - boltzmann-generators
related:
  - "[[wiki/concepts/free-energy-estimation]]"
  - "[[wiki/concepts/adaptive-enhanced-sampling]]"
  - "[[wiki/concepts/times-square-sampling]]"
  - "[[wiki/concepts/accelerated-weight-histogram-method]]"
  - "[[wiki/concepts/on-the-fly-probability-enhanced-sampling]]"
  - "[[wiki/concepts/multistate-bennett-acceptance-ratio]]"
  - "[[wiki/concepts/mbar-with-configuration-mapping]]"
  - "[[wiki/concepts/lambda-dynamics-with-bias-updated-gibbs-sampling]]"
  - "[[wiki/concepts/boltzmann-generators-equilibrium-sampling]]"
  - "[[wiki/questions/overlap-support-diagnostics-for-free-energy-estimators]]"
  - "[[wiki/questions/adaptive-estimators-vs-fixed-sample-estimators]]"
  - "[[wiki/tensions/TEN-0005-on-the-fly-bias-adaptation-vs-postprocessing-diagnostics]]"
sources:
  - SRC-0005
  - SRC-0006
  - SRC-0007
  - SRC-0008
  - SRC-0009
  - SRC-0010
  - SRC-0011
  - SRC-0012
  - SRC-0013
  - SRC-0023
  - SRC-0037
  - SRC-0039
  - SRC-0041
sensitivity: public
encryption: none
wiki_pages_used:
  - "[[wiki/index]]"
  - "[[wiki/concepts/free-energy-estimation]]"
  - "[[wiki/concepts/adaptive-enhanced-sampling]]"
  - "[[wiki/concepts/times-square-sampling]]"
  - "[[wiki/concepts/accelerated-weight-histogram-method]]"
  - "[[wiki/concepts/on-the-fly-probability-enhanced-sampling]]"
  - "[[wiki/concepts/multistate-bennett-acceptance-ratio]]"
  - "[[wiki/concepts/on-the-fly-estimation-versus-mbar]]"
  - "[[wiki/concepts/mbar-with-configuration-mapping]]"
  - "[[wiki/concepts/lambda-dynamics-with-bias-updated-gibbs-sampling]]"
  - "[[wiki/concepts/boltzmann-generators-equilibrium-sampling]]"
  - "[[wiki/concepts/transferable-and-scalable-boltzmann-generators]]"
  - "[[wiki/claims/CLM-0001-tss-self-adjustment-can-lower-variance]]"
  - "[[wiki/claims/CLM-0004-mbar-is-optimal-but-overlap-limited]]"
  - "[[wiki/claims/CLM-0006-opes-reconstructs-probability-to-derive-bias]]"
  - "[[wiki/claims/CLM-0007-awh-updates-bias-from-conditional-histograms]]"
  - "[[wiki/claims/CLM-0008-ladybugs-couples-gibbs-sampling-with-fastmbar-bias-updates]]"
  - "[[wiki/claims/CLM-0016-boltzmann-generators-need-overlap-and-reweighting-support]]"
  - "[[wiki/questions/overlap-support-diagnostics-for-free-energy-estimators]]"
  - "[[wiki/questions/adaptive-estimators-vs-fixed-sample-estimators]]"
  - "[[wiki/tensions/TEN-0001-tss-variance-advantage-vs-mbar-generalization]]"
  - "[[wiki/tensions/TEN-0005-on-the-fly-bias-adaptation-vs-postprocessing-diagnostics]]"
  - "[[wiki/tensions/TEN-0009-boltzmann-generator-one-shot-sampling-vs-overlap-risk]]"
  - "[[wiki/dashboards/source-citation-links]]"
  - "[[wiki/entities/authors/jack-lidmar]]"
  - "[[wiki/entities/authors/michael-r-shirts]]"
raw_sources_consulted: []
wiki_pages_updated: []
graph_neighborhoods_used:
  - "tools/query_graph.py --start wiki/answers/sample-bias-reweighting-method-comparison --depth 2 --types source,concept,claim,question,tension,entity"
  - "tools/query_graph.py --start wiki/concepts/free-energy-estimation --depth 1 --types source,concept,claim,question,tension,entity"
  - "tools/query_graph.py --source-id SRC-0005"
  - "tools/query_graph.py --source-id SRC-0013"
  - "tools/query_graph.py --source-id SRC-0041"
---

# Sample, Bias, Reweighting, and Diagnostics Across Free-Energy Methods

## Short answer

The main split is between methods that adapt the simulation while samples are being generated, methods that reweight a fixed sample set after generation, and methods that learn a generator whose samples are later importance-weighted. TSS, AWH, OPES, and LaDyBUGS all use samples on the fly to change future sampling, but they update different objects: TSS updates free-energy and allocation estimates over rungs, AWH updates a free-energy bias from conditional weight histograms, OPES updates a collective-variable probability estimate and derived bias, and LaDyBUGS updates discrete alchemical-state biases with FastMBAR feedback. [SRC-0005] [SRC-0007] [SRC-0010] [SRC-0013]

MBAR is different: it is primarily a postprocessing estimator that takes samples from multiple equilibrium states and reweights them through cross-state reduced potentials. [SRC-0023] Boltzmann generators are different again: they train an exact-density generative proposal, then use importance weights to recover unbiased equilibrium estimates when generated samples overlap the target Boltzmann distribution. [SRC-0041] [SRC-0037] [SRC-0039]

Their validation diagnostics differ accordingly. Adaptive methods need diagnostics that account for the adaptation history and whether learned biases created useful overlap; MBAR needs overlap, decorrelation, cross-potential, and uncertainty diagnostics on a fixed sample set; Boltzmann generators need effective-sample-size and missed-state diagnostics because a low-energy generator can still omit important modes. [SRC-0006] [SRC-0023] [SRC-0037] [SRC-0039]

## Detailed answer

| Method | How samples are used | What biasing does | How reweighting enters | Validation diagnostics |
| --- | --- | --- | --- | --- |
| TSS | Samples are generated in a simulated-tempering-style extended space over configurations and rungs; conditional rung probabilities drive stochastic-approximation updates during the run. [SRC-0005, sections 2.1-2.2] | Biasing is a control mechanism for rung allocation: current free-energy estimates and visit-control tilts decide where future effort goes, and windowing localizes large rung spaces. [SRC-0005, section 3.1] [SRC-0006, sections 6-7] | Reweighting is built into the estimator through conditional probabilities across rungs, but TSS is not mainly an offline reweighting method; its distinctive feature is that current estimates affect future sampling. [SRC-0005, section 2.2.3] [SRC-0006, section 4.5] | Check whether the theoretical overlap-matrix assumptions are plausible for correlated MD, whether visit control/windowing distort the intended allocation, and whether epoch or jackknife estimates expose unstable adaptation. The TSS variance advantage is a scoped claim, not a blanket MBAR replacement. [SRC-0006, section 4.5] [[wiki/claims/CLM-0001-tss-self-adjustment-can-lower-variance]] [[wiki/tensions/TEN-0001-tss-variance-advantage-vs-mbar-generalization]] |
| AWH | Each sampled configuration contributes fractional conditional probabilities to many parameter values, not just a count at the visited parameter. [SRC-0007, eq. 5] [SRC-0009, eq. 3] | Biasing learns free-energy weights so the sampled parameter marginal approaches a chosen target distribution. [SRC-0008, section II.A] [SRC-0009, eq. 5] | Reweighting appears as conditional weights and histogram-based free-energy updates; final estimates still depend on overlap between conditionally likely parameter states. [SRC-0007, section II] [SRC-0009] | Inspect conditional overlap, reaction-coordinate or pathway coverage, uncertainty estimates, and agreement across independent runs; a smooth learned bias is not enough if conditionally adjacent states have poor support. [[wiki/claims/CLM-0007-awh-updates-bias-from-conditional-histograms]] [[wiki/questions/overlap-support-diagnostics-for-free-energy-estimators]] |
| OPES | Samples in collective-variable space are accumulated into a weighted kernel density estimate of the unbiased CV probability. [SRC-0010, eq. 5] | Biasing is derived from the ratio of the estimated CV probability to a target CV distribution, with regularization to bound the bias. [SRC-0010, eqs. 4 and 8] | Reweighting enters through the weighted probability reconstruction and through interpreting biased CV samples back in terms of the underlying distribution; it remains limited by CV choice and target choice. [SRC-0010] [SRC-0011] | Validate the chosen collective variables and target distribution, monitor kernel compression or bandwidth behavior, and check whether reweighted estimates remain stable under the OPES regularization choices. [[wiki/claims/CLM-0006-opes-reconstructs-probability-to-derive-bias]] [[wiki/tensions/TEN-0005-on-the-fly-bias-adaptation-vs-postprocessing-diagnostics]] |
| MBAR | Samples are collected first from multiple equilibrium states; MBAR then uses all retained samples and all cross-state reduced potentials. [SRC-0023] | MBAR itself does not prescribe an adaptive bias; any bias belongs to the sampling protocol that produced the samples. [SRC-0023] | Reweighting is the central operation: MBAR solves coupled normalization-constant equations and assigns weights for free-energy differences, expectations, and uncertainties. [SRC-0023] Configuration mapping extends this by warping samples before MBAR when raw overlap is poor. [SRC-0012] | Check decorrelation/subsampling, cross-state reduced-potential availability, phase-space overlap, covariance or uncertainty estimates, and sensitivity to configuration mappings. [[wiki/claims/CLM-0004-mbar-is-optimal-but-overlap-limited]] [[wiki/questions/overlap-support-diagnostics-for-free-energy-estimators]] |
| LaDyBUGS | Samples alternate between short MD at a discrete alchemical state and Gibbs updates of the state conditional on the current coordinates. [SRC-0013] | Biases are updated during production to keep many ligand alchemical states sampled in one simulation. [SRC-0013, eqs. 1 and 4] | FastMBAR periodically estimates free-energy differences and feeds those estimates into the next bias update; the method therefore combines adaptive biasing with MBAR-style reweighting. [SRC-0013] | Validate both sides of the loop: coordinate sampling within short MD segments and lambda-state support for FastMBAR. Ligand grouping and conditional-state overlap become diagnostics, not just implementation details. [[wiki/claims/CLM-0008-ladybugs-couples-gibbs-sampling-with-fastmbar-bias-updates]] [[wiki/tensions/TEN-0005-on-the-fly-bias-adaptation-vs-postprocessing-diagnostics]] |
| Boltzmann generators | Samples are generated by an exact-density normalizing-flow-like model rather than by a Markov chain alone. [SRC-0041] | Training uses energy and entropy/Jacobian terms, and sometimes examples, to make the generator proposal resemble the target distribution. [SRC-0041] | Importance reweighting is essential for unbiased observables and free energies; effective sample size and missing-state risk determine whether the generated proposal is usable. [SRC-0041] [SRC-0037] [SRC-0039] | Check exact generated densities, importance-weight variance, effective sample size, state coverage, and missed metastable states. Transfer or scaling claims remain incomplete without those support diagnostics. [[wiki/claims/CLM-0016-boltzmann-generators-need-overlap-and-reweighting-support]] [[wiki/tensions/TEN-0009-boltzmann-generator-one-shot-sampling-vs-overlap-risk]] |

The practical interpretation is:

- Use TSS, AWH, OPES, or LaDyBUGS when the sampling process itself should adapt from information learned during the run.
- Use MBAR when the main problem is statistically efficient analysis of samples already drawn from multiple states, assuming adequate overlap.
- Use Boltzmann generators when the goal is amortized direct proposal generation, with reweighting as the statistical correction rather than as an afterthought.

TSS and MBAR make the contrast especially clear. MBAR receives a fixed sample set and estimates free energies afterward, whereas TSS lets current free-energy estimates shape the distribution of future samples. The TSS source bundle proves a bounded variance comparison under its assumptions, but the wiki records this as a limited claim rather than a general replacement for MBAR. [SRC-0005, proposition 3] [SRC-0006, section 4.5]

## Key equations

The methods share a common normalization problem but attach weights at different points in the workflow. MBAR solves self-consistent equations over fixed cross-evaluated samples. [SRC-0023] AWH accumulates conditional weights over parameter values. [SRC-0009, eq. 3] OPES builds a weighted KDE of collective-variable probability. [SRC-0010, eq. 5] Boltzmann generators use importance weights from generated proposal density to target Boltzmann density. [SRC-0037]

## Graph-guided acceptance-test notes

Graph traversal from this answer note recovered the expected concept neighborhood: TSS, AWH, OPES, MBAR, configuration-mapped MBAR, LaDyBUGS, Boltzmann generators, and general free-energy estimation. Traversal also surfaced the reusable claims about TSS variance scope, MBAR overlap limits, AWH conditional histograms, OPES probability reconstruction, LaDyBUGS FastMBAR feedback, and Boltzmann-generator overlap support.

The question and tension neighborhood was useful for the diagnostic layer: overlap/support diagnostics, adaptive-estimator versus fixed-sample comparison, TSS-versus-MBAR generalization, on-the-fly bias adaptation versus postprocessing diagnostics, and one-shot generator sampling versus overlap risk. Citation-link traversal showed strong local links among the ingested TSS, AWH, MBAR, LaDyBUGS, and Boltzmann-generator sources; author/entity traversal surfaced Jack Lidmar for the AWH cluster and Michael R. Shirts for the MBAR cluster.

## Sources used

- SRC-0005 and SRC-0006 for TSS on-the-fly stochastic approximation, visit control, windowing, and the bounded TSS-versus-MBAR variance claim.
- SRC-0007, SRC-0008, and SRC-0009 for AWH conditional weight histograms, free-energy bias updates, and target parameter distributions.
- SRC-0010 and SRC-0011 for OPES probability reconstruction, target distributions, regularization, and kernel compression.
- SRC-0012 and SRC-0023 for MBAR and the configuration-mapping extension.
- SRC-0013 for LaDyBUGS Gibbs sampling, dynamic biases, and FastMBAR feedback.
- SRC-0037, SRC-0039, and SRC-0041 for Boltzmann-generator exact-density proposals, importance reweighting, effective sample size, transfer, and scaling limits.

## Wiki pages used

- [[wiki/concepts/free-energy-estimation]]
- [[wiki/concepts/adaptive-enhanced-sampling]]
- [[wiki/concepts/times-square-sampling]]
- [[wiki/concepts/accelerated-weight-histogram-method]]
- [[wiki/concepts/on-the-fly-probability-enhanced-sampling]]
- [[wiki/concepts/multistate-bennett-acceptance-ratio]]
- [[wiki/concepts/on-the-fly-estimation-versus-mbar]]
- [[wiki/concepts/mbar-with-configuration-mapping]]
- [[wiki/concepts/lambda-dynamics-with-bias-updated-gibbs-sampling]]
- [[wiki/concepts/boltzmann-generators-equilibrium-sampling]]
- [[wiki/concepts/transferable-and-scalable-boltzmann-generators]]
- [[wiki/claims/CLM-0001-tss-self-adjustment-can-lower-variance]]
- [[wiki/claims/CLM-0004-mbar-is-optimal-but-overlap-limited]]
- [[wiki/claims/CLM-0006-opes-reconstructs-probability-to-derive-bias]]
- [[wiki/claims/CLM-0007-awh-updates-bias-from-conditional-histograms]]
- [[wiki/claims/CLM-0008-ladybugs-couples-gibbs-sampling-with-fastmbar-bias-updates]]
- [[wiki/claims/CLM-0016-boltzmann-generators-need-overlap-and-reweighting-support]]
- [[wiki/questions/overlap-support-diagnostics-for-free-energy-estimators]]
- [[wiki/questions/adaptive-estimators-vs-fixed-sample-estimators]]
- [[wiki/tensions/TEN-0001-tss-variance-advantage-vs-mbar-generalization]]
- [[wiki/tensions/TEN-0005-on-the-fly-bias-adaptation-vs-postprocessing-diagnostics]]
- [[wiki/tensions/TEN-0009-boltzmann-generator-one-shot-sampling-vs-overlap-risk]]
- [[wiki/dashboards/source-citation-links]]
- [[wiki/entities/authors/jack-lidmar]]
- [[wiki/entities/authors/michael-r-shirts]]

## Wiki updates made

- Updated this answer note to include validation diagnostics and graph-traversal provenance.
- No durable concept, source, claim, question, tension, citation, or author pages needed changes.

## Remaining gaps

- The wiki does not contain a single benchmark that compares all six methods on the same system.
- The comparison is therefore mechanistic and workflow-oriented, not a performance ranking.
