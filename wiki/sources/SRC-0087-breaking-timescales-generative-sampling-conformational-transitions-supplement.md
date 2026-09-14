---
type: source
status: active
created: 2026-09-14
updated: 2026-09-14
source_id: SRC-0087
display_title: "Supplementary Information for Breaking timescales with generative sampling of conformational transitions"
short_title: "Gen-COMPAS Supplement"
aliases:
  - "SRC-0087"
  - "Gen-COMPAS Supplement"
  - "Breaking Timescales Supplement"
source_path: raw/sources/SRC-0087-breaking-timescales-generative-sampling-conformational-transitions-supplement.pdf
imported_path: raw/sources/SRC-0087-breaking-timescales-generative-sampling-conformational-transitions-supplement.pdf
original_filename: "41586_2026_11025_MOESM1_ESM.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 5457d9f087c76836626603df402960d9bc2cb40b7bc49dc7561ff9489c21f598
authors:
  - "Chenyu Tang"
  - "Mayank Prakash Pandey"
  - "Cheng Giuseppe Chen"
  - "Alberto Megías"
  - "François Dehez"
  - "Christophe Chipot"
author_entities: []
year: 2026
venue: "Nature supplementary information"
doi: "10.1038/s41586-026-11025-1"
arxiv:
metadata_review_status: reviewed
source_bundle: breaking-timescales-generative-sampling-conformational-transitions-2026
bundle_role: supplement
areas:
  - research
categories:
  - research/adaptive-sampling
  - research/molecular-simulation/free-energy
  - research/molecular-simulation/molecular-dynamics
  - research/machine-learning/molecular-modeling
  - research/biomolecules/proteins
tags:
  - Gen-COMPAS
  - supplementary-information
  - diffusion-model
  - committor
  - RiteWeight
  - targeted-molecular-dynamics
  - uncertainty-quantification
  - reproducibility
related:
  - "[[wiki/sources/SRC-0086-breaking-timescales-generative-sampling-conformational-transitions]]"
  - "[[wiki/concepts/generative-committor-guided-path-sampling]]"
  - "[[wiki/concepts/enhanced-sampling-validation]]"
  - "[[wiki/claims/CLM-0043-generated-transition-proposals-require-dynamical-validation]]"
  - "[[wiki/questions/QST-0009-scalable-independent-validation-of-learned-committors]]"
sources:
  - SRC-0086
  - SRC-0087
cites_sources: []
citation_match_status: partial
cqt_review_status: linked
sensitivity: public
encryption: none
ingestion_status: partial
coverage_profile: math-deep
peer_review_status: supplementary-material
---

# Supplementary Information for Breaking Timescales with Generative Sampling of Conformational Transitions

Source ID: `SRC-0087`

## Raw source

- Repository path: `raw/sources/SRC-0087-breaking-timescales-generative-sampling-conformational-transitions-supplement.pdf`
- Open raw source: [raw/sources/SRC-0087-breaking-timescales-generative-sampling-conformational-transitions-supplement.pdf](../../raw/sources/SRC-0087-breaking-timescales-generative-sampling-conformational-transitions-supplement.pdf)
- Main source: [[wiki/sources/SRC-0086-breaking-timescales-generative-sampling-conformational-transitions]]

## Summary

The supplement is the implementation and validation companion to the Gen-COMPAS paper. It provides Algorithm S1, the denoising diffusion probabilistic model (DDPM), graph architecture, transition-state and path construction, RiteWeight free-energy reconstruction, convergence and uncertainty diagnostics, direct committor validation, TMD sensitivity and reproducibility tests, four additional molecular applications, per-system parameters, and estimated GPU costs. [SRC-0087]

## Algorithmic recursion

Algorithm S1 iterates over cumulative datasets $D_k$ and RiteWeight weights $W_k$: [SRC-0087, Algorithm S1, pp. S10–S11]

1. Initialize $D_0$ from 1–2 ns unbiased trajectories in $A$ and $B$.
2. Train the initial DDPM, generate intermediates, cluster them, and refine representative targets by bidirectional TMD.
3. Launch unbiased trajectories from refined configurations and compute $D_1,W_1$ with RiteWeight.
4. At iteration $k\ge1$, train the DDPM and committor $q_k$ on $D_k,W_k$.
5. Select $T_k=\{x_i:q_k(x_i)\approx1/2\}$, refine with TMD, and launch new unbiased trajectories.
6. Accumulate

$$
D_{k+1}=D_k\cup\Delta D_k,
\qquad
W_{k+1}=W_k\cup\Delta W_k,
$$

then repeat until the diagnostics stop changing within the chosen criteria.

## DDPM equations

The forward transition kernel is [SRC-0087, Eq. S1, p. S12]

$$
p(x_t\mid x_{t-1})
=
\mathcal N\!\left(x_t;\sqrt{1-\beta_t}\,x_{t-1},\beta_t I\right),
$$

where $\beta_t$ is the variance schedule and $\bar\alpha_t=\prod_{s=1}^{t}(1-\beta_s)$. Coordinates are centred before noise is applied. The clean-coordinate prediction is trained with [SRC-0087, Eq. S5, p. S13]

$$
\mathcal L(\theta)
=
\mathbb E_{t,x_0,\epsilon}
\left[
\left\|
f_\theta\!\left(\sqrt{\bar\alpha_t}x_0+\sqrt{1-\bar\alpha_t}\epsilon,t\right)-x_0
\right\|_2^2
\right].
$$

The denoising network combines a static covalent graph with a dynamic $k$-nearest-neighbour graph, SchNet-style atom messages, and residue-level multi-head attention. Protein and ligand coordinates are denoised jointly. [SRC-0087, Eqs. S6–S9, pp. S13–S14]

## Transition-state and path construction

The transition-state ensemble is approximated by generated structures in a neighbourhood

$$
q\in\left(\frac12-\epsilon,\frac12+\epsilon\right),
\qquad 2\epsilon<1,
$$

followed by TMD refinement. Candidate transition paths are constructed from representative transition-state structures by following the learned committor gradient and clustering the resulting committor-consistent paths. [SRC-0087, pp. S14–S15]

## RiteWeight free-energy reconstruction

Gen-COMPAS trajectories begin from non-equilibrium ensembles near TMD endpoints or the separatrix, so their frames cannot be pooled as equilibrium samples. RiteWeight repeatedly randomizes a clustering of configuration space, estimates the stationary probabilities of its weighted transition matrix, and updates fragment weights. [SRC-0087, pp. S15–S16]

For random clustering iteration $k$,

$$
\pi^{(k)}=\pi^{(k)}T^{(k)},
\qquad
\sum_i\pi_i^{(k)}=1.
$$

The weighted density along a post-selected CV $\xi$ and corresponding free energy are [SRC-0087, Eqs. S11–S12, p. S16]

$$
P(\xi)\propto\sum_{x\in D}w(x)\,\delta\!\left(\xi(x)-\xi\right),
$$

$$
F(\xi)=-k_BT\ln P(\xi)+C.
$$

The source emphasizes that global accuracy still depends on trajectory connectivity and sampling coverage. [SRC-0087, p. S16]

## Validation and uncertainty

- **Transition-region coverage:** Compare consecutive $k$-nearest-neighbour RMSD distributions using order-one Wasserstein distance; the reported threshold is 1.0. [SRC-0087, Eq. S13 and Table S1, p. S17]
- **Free-energy uncertainty:** Resample whole trajectories, not individual frames, and rebuild weighted FELs for bootstrap replicates. [SRC-0087, Eqs. S14–S15, p. S18]
- **Free-energy accumulation:** Compare partial-data FELs with the full available-data estimate using a masked RMSE over sufficiently populated bins. [SRC-0087, Eqs. S16–S17, pp. S18–S19]
- **Direct shooting:** For a structure, estimate

$$
q_{\mathrm{sample}}=\frac{n_B}{n_A+n_B},
$$

where unresolved finite-time shots are excluded from the denominator. [SRC-0087, Eq. S18, p. S22]
- **Committor ensembles:** Eight independently trained VCNs provide mean prediction and between-model standard deviation. [SRC-0087, Eqs. S24–S27, p. S31]
- **TMD consistency:** Compare endpoint committors from the $A$-to-target and $B$-to-target trajectories using predicted and, where feasible, directly sampled committors. [SRC-0087, Eqs. S19–S20, pp. S22–S23]

For Trp-cage, independent aimless shooting retained 91 structures for which more than half of 20 trajectories committed within 50 ns; predicted and sampled committors gave $r=0.898$ and $R^2=0.806$. A separate test evaluated frames from one independent DESRES trajectory with predicted $q\in[0.45,0.55]$: the mean prediction was 0.4998 and the observed forward first-arrival fraction was 0.5335 with a reported 95% Wilson interval of 0.5118–0.5552. No new shooting trajectories were launched for those 2,028 frames, and temporal correlation or overlapping forward continuations mean they should not be read as 2,028 statistically independent trials. [SRC-0087, pp. S26–S30]

For NANMA, TMD-extracted structures at predicted $q\approx0.1,0.3,0.5,0.7,0.9$ gave sampled means 0.174, 0.359, 0.485, 0.617, and 0.799; pointwise predicted-versus-sampled agreement had $r=0.848$. Evaluation along a separate 460,000-step unbiased trajectory yielded correlation 0.9999668. [SRC-0087, pp. S22–S25]

## Equation inventory

| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |
| Algorithm S1 | pp. S10–S11 | [[wiki/sources/SRC-0087-breaking-timescales-generative-sampling-conformational-transitions-supplement#Algorithmic recursion]] | Defines the end-to-end iterative loop. | $A$, $B$, $D_k$, $W_k$, $q_k$, $T_k$ | Primary workflow specification. |
| DDPM forward and reverse processes, S1–S5 | pp. S12–S13 | [[wiki/sources/SRC-0087-breaking-timescales-generative-sampling-conformational-transitions-supplement#DDPM equations]] | Defines coordinate noising, denoising, and training. | $x_t$, $\beta_t$, $\alpha_t$, $\bar\alpha_t$, $\theta$, $\epsilon$ | Core generated-target implementation; S2–S3 require notation review. |
| GNN architecture, S6–S9 | pp. S13–S14 | [[wiki/sources/SRC-0087-breaking-timescales-generative-sampling-conformational-transitions-supplement#DDPM equations]] | Combines atom/residue features and predicts clean coordinates. | $h_i$, $d_{ij}$, $G_{k\mathrm{NN}}$, $G_{\mathrm{bonds}}$ | Defines covalent/dynamic neighbours, SchNet messages, and attention. |
| RiteWeight stationary equation, S10 | p. S15 | [[wiki/sources/SRC-0087-breaking-timescales-generative-sampling-conformational-transitions-supplement#RiteWeight free-energy reconstruction]] | Reconstructs stationary cluster weights. | $T^{(k)}$, $\pi^{(k)}$ | Basis of trajectory-fragment reweighting. |
| Weighted density and FEL, S11–S12 | p. S16 | [[wiki/sources/SRC-0087-breaking-timescales-generative-sampling-conformational-transitions-supplement#RiteWeight free-energy reconstruction]] | Converts converged frame weights to projected free energies. | $w(x)$, $\xi$, $P(\xi)$, $F(\xi)$ | Produces reported FELs in post-selected CVs. |
| Structural coverage, S13 | p. S17 | [[wiki/sources/SRC-0087-breaking-timescales-generative-sampling-conformational-transitions-supplement#Validation and uncertainty]] | Measures iteration-to-iteration TSE change. | $W_1$, $P_\ell$, $d_i^{(\ell)}$ | Stopping diagnostic with empirical threshold 1.0. |
| Bootstrap and FEL degradation, S14–S17 | pp. S18–S19 | [[wiki/sources/SRC-0087-breaking-timescales-generative-sampling-conformational-transitions-supplement#Validation and uncertainty]] | Quantifies trajectory-level uncertainty and accumulation stability. | $T_i$, $w(x)$, $F_f$, masked RMSE | Avoids frame-level resampling and distinguishes partial-data stability. |
| Direct committor and TMD consistency, S18–S23 | pp. S22–S30 | [[wiki/sources/SRC-0087-breaking-timescales-generative-sampling-conformational-transitions-supplement#Validation and uncertainty]] | Tests learned $q$ and bidirectional refinement against unbiased dynamics. | $n_A$, $n_B$, $q_{\mathrm{pred}}$, $q_{\mathrm{sample}}$, $\delta q$ | Strongest direct validation, applied to NANMA and Trp-cage. |
| Ensemble uncertainty, S24–S27 | p. S31 | [[wiki/sources/SRC-0087-breaking-timescales-generative-sampling-conformational-transitions-supplement#Validation and uncertainty]] | Estimates epistemic disagreement among VCNs. | $q_i(x)$, $\bar q(x)$, $\sigma_q(x)$ | Cheaper diagnostic for systems where direct shooting is prohibitive. |

## Variable glossary

- $D_k,W_k$: Cumulative trajectory frames and RiteWeight weights at iteration $k$. [SRC-0087, Algorithm S1]
- $x_t$: Coordinates at DDPM diffusion step $t$; $x_0$ denotes clean coordinates. [SRC-0087, Eqs. S1–S5]
- $\beta_t$, $\alpha_t$, $\bar\alpha_t$: Diffusion variance, one-step retention, and cumulative schedule. [SRC-0087, pp. S12–S13]
- $f_\theta$: Network predicting clean centred coordinates from a noised configuration. [SRC-0087, Eq. S5]
- $q_k(x)$: Iteration-$k$ committor prediction. [SRC-0087, Algorithm S1]
- $\epsilon$: TSE-selection half-width around $q=1/2$; elsewhere the source also uses epsilon-like notation for Gaussian diffusion noise. [SRC-0087, pp. S12–S14]
- $T^{(k)},\pi^{(k)}$: Random-clustering transition matrix and stationary probabilities in RiteWeight iteration $k$. [SRC-0087, Eq. S10]
- $w(x)$: Reconstructed stationary weight of configuration $x$. [SRC-0087, Eq. S11]
- $\xi$: Interpretable CV chosen after sampling for projection. [SRC-0087, Eqs. S11–S12]
- $n_A,n_B$: Resolved shooting trajectories first reaching $A$ or $B$. [SRC-0087, Eq. S18]
- $\sigma_q(x)$: Across-network standard deviation used as an epistemic uncertainty proxy. [SRC-0087, Eq. S26]

## Implementation parameters

- Shared DDPM settings include a cosine schedule, 200 diffusion steps, hidden dimension 128, node features 64, 16 neighbours, four SchNet layers, four attention heads, time embedding 128, learning rate $10^{-4}$, and weight decay $10^{-6}$. [SRC-0087, Table S3, p. S37]
- TMD durations are 10 ps for NANMA and trialanine and 100 ps for larger systems; unbiased shots are 100 ps for the toy systems, 1 ns for Trp-cage, and 2 ns for larger systems. [SRC-0087, Table S4, p. S37]
- VCNs have four hidden layers, 500 maximum epochs, patience 20, and learning rate $10^{-4}$; lag times range from 100 fs for toy systems to 4 ps for the larger systems. [SRC-0087, Table S5, p. S38]
- The recommended generative-noise range is approximately 0–50 initially and 0–2 after transition data accumulate; these are empirical settings rather than universal constants. [SRC-0087, p. S33]
- A 20-combination Trp-cage TMD scan and five independent full workflows tested steering sensitivity; the weakest force constant sampled transition states less effectively but remained qualitatively consistent. Table S4 reports 100 ps TMD for Trp-cage, whereas Fig. S17 labels the reproducibility runs as 1 ns per TMD trajectory despite saying three runs used manuscript parameters; the supplement does not reconcile this tenfold discrepancy. [SRC-0087, pp. S33–S35, S37]
- Estimated total costs for the listed non-toy systems range from 192.49 GPU-hours for apo AAC to 666.71 GPU-hours for nAChR, measured on eight NVIDIA L40S GPUs. These estimates combine benchmarked stages and are not direct evidence of equal-error wall-clock speedup over conventional MD. [SRC-0087, Table S6, p. S38]

## Proof and dependency map

No theorem proof is supplied. The mathematical structure supports four linked implementation layers: DDPM proposal generation (S1–S9), committor-guided TSE/TPE construction (S14–S15), stationary reconstruction by RiteWeight (S10–S12), and validation through structural-distance, bootstrap, shooting, ensemble, and TMD-consistency diagnostics (S13–S27). Failure in an earlier layer can propagate: geometrically poor proposals stress TMD; inadequate trajectory connectivity limits RiteWeight; incomplete transition coverage biases the VCN; and model-ensemble agreement cannot exclude shared systematic error. [SRC-0087, pp. S12–S35]

## Supplement-specific evidence

- Adds NANMA, trialanine, ribose-binding protein, and $V_o$ results that are not detailed in the main article. For $V_o$, the principal barrier is about 5–6 kcal mol$^{-1}$ versus about 8 kcal mol$^{-1}$ in the cited conventional study, while $\Delta G_{AB}<1$ kcal mol$^{-1}$ in both; basin M3 differs by about 5 kcal mol$^{-1}$. [SRC-0087, pp. S2–S9]
- Gives direct-shooting committor tests for NANMA and Trp-cage, including finite-time censoring rules and confidence intervals. [SRC-0087, pp. S22–S30]
- Reports convergence tables, FEL degradation curves, independent Trp-cage repeats, TMD sensitivity, architecture settings, and estimated hardware costs. [SRC-0087, pp. S17–S21, S33–S38]

## Limitations and mathematical gaps

- The DDPM notation on p. S12 has several unresolved issues. Equation S2 prints $x_t=\sqrt{\bar\alpha_t}x_{t-1}+\sqrt{1-\bar\alpha_t}\epsilon$ although $\bar\alpha_t$ is cumulative; Eq. S3 writes the reverse joint distribution as conditioned on $x_0$; the text gives $\Sigma_\theta=\sigma_t I$ while $\sigma_t^2=\beta_t$, mixing covariance and standard-deviation conventions; and Eq. S4's posterior coefficient differs from the standard $x_0$-prediction form. Implementations should check the released code or derive the kernel rather than silently correcting the source. [SRC-0087, Eqs. S2–S4, p. S12]
- The eight-network standard deviation diagnoses model disagreement, not shared model bias. [SRC-0087, p. S31]
- Larger-system free-energy degradation curves do not all establish a strict global plateau; the source advises caution for absolute differences between weakly connected basins. [SRC-0087, pp. S18–S21]
- Direct shooting is not scaled to the largest applications because it is considered computationally prohibitive. [SRC-0087, p. S31]
- The wiki records central equations and dependencies but omits full expanded architecture equations, every system-specific CV definition, and every table entry.

## Claims, questions, and links

- [[wiki/claims/CLM-0043-generated-transition-proposals-require-dynamical-validation]]
- [[wiki/questions/QST-0009-scalable-independent-validation-of-learned-committors]]
- [[wiki/tensions/TEN-0016-internal-convergence-vs-external-free-energy-correctness]]
- [[wiki/concepts/generative-committor-guided-path-sampling]]
- [[wiki/concepts/enhanced-sampling-validation]]

## Citation links

- The 33-item supplement bibliography was checked for conservative matches to existing source pages; none was confirmed strongly enough to add to `cites_sources`.
- Citation review remains partial because references were not fully normalized against external identifiers.

## Ingestion QA

### Retrieval questions checked

- What exact recursion defines one Gen-COMPAS iteration?
- How is the DDPM trained, and what graph architecture does it use?
- How does RiteWeight reconstruct free energies from non-equilibrium-started trajectories?
- Which diagnostics assess transition-region coverage, FEL stability, committor validity, and TMD consistency?
- What direct quantitative validation is reported for Trp-cage?
- Which settings are shared across systems, and which are system-dependent?
- What does the supplement report about TMD sensitivity and run-to-run reproducibility?
- What implementation ambiguities or validation gaps remain?

### Coverage decision

Broad `math-deep` coverage as the supplement page. It captures Algorithm S1, the central DDPM and RiteWeight equations, equation dependencies, validation estimators, direct-shooting results, variable definitions, implementation parameters, mathematical ambiguities, and bundle-level limitations. Formal `ingestion_status` remains `partial` because repository-wide validation is blocked by the pre-existing missing frontmatter in `wiki/answers/garnet-nonbonded-contact-cleanup.md`, and Eqs. S2–S4 plus the Trp-cage TMD duration contain unresolved source-level inconsistencies.

### Known gaps

- Repository-wide validation does not pass because of the pre-existing unrelated missing-frontmatter error above; validation passes when that file is temporarily excluded.
- Exact code state is not fixed by a commit or release tag in the source.
- Full parameter tables, every figure, and all projected FEL values remain in the raw PDF.
- External references, code, and source data were not ingested.
