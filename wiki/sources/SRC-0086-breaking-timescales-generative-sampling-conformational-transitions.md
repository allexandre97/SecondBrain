---
type: source
status: active
created: 2026-09-14
updated: 2026-09-14
source_id: SRC-0086
display_title: "Breaking timescales with generative sampling of conformational transitions"
short_title: "Gen-COMPAS"
aliases:
  - "SRC-0086"
  - "Gen-COMPAS"
  - "Breaking Timescales"
source_path: raw/sources/SRC-0086-breaking-timescales-generative-sampling-conformational-transitions.pdf
imported_path: raw/sources/SRC-0086-breaking-timescales-generative-sampling-conformational-transitions.pdf
original_filename: "s41586-026-11025-1.pdf"
original_path_note: "Original local path omitted from wiki metadata."
sha256: 042d002e51b8411af736e966fb84238088e08be12da9e2e1ddbdd5f8a6e5fbe5
authors:
  - "Chenyu Tang"
  - "Mayank Prakash Pandey"
  - "Cheng Giuseppe Chen"
  - "Alberto Megías"
  - "François Dehez"
  - "Christophe Chipot"
author_entities: []
year: 2026
venue: "Nature"
doi: "10.1038/s41586-026-11025-1"
arxiv:
metadata_review_status: reviewed
source_bundle: breaking-timescales-generative-sampling-conformational-transitions-2026
bundle_role: main
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
  - generative-sampling
  - committor
  - transition-path-sampling
  - diffusion-model
  - targeted-molecular-dynamics
  - RiteWeight
  - rare-events
related:
  - "[[wiki/sources/SRC-0087-breaking-timescales-generative-sampling-conformational-transitions-supplement]]"
  - "[[wiki/concepts/generative-committor-guided-path-sampling]]"
  - "[[wiki/concepts/adaptive-enhanced-sampling]]"
  - "[[wiki/concepts/enhanced-sampling-validation]]"
  - "[[wiki/concepts/free-energy-estimation]]"
  - "[[wiki/concepts/boltzmann-generators-equilibrium-sampling]]"
  - "[[wiki/claims/CLM-0043-generated-transition-proposals-require-dynamical-validation]]"
  - "[[wiki/questions/QST-0009-scalable-independent-validation-of-learned-committors]]"
  - "[[wiki/tensions/TEN-0016-internal-convergence-vs-external-free-energy-correctness]]"
sources:
  - SRC-0086
  - SRC-0087
cites_sources:
  - SRC-0041
  - SRC-0074
citation_match_status: partial
cqt_review_status: linked
sensitivity: public
encryption: none
ingestion_status: partial
coverage_profile: math-standard
peer_review_status: peer-reviewed
---

# Breaking Timescales with Generative Sampling of Conformational Transitions

Source ID: `SRC-0086`

## Raw source

- Repository path: `raw/sources/SRC-0086-breaking-timescales-generative-sampling-conformational-transitions.pdf`
- Open raw source: [raw/sources/SRC-0086-breaking-timescales-generative-sampling-conformational-transitions.pdf](../../raw/sources/SRC-0086-breaking-timescales-generative-sampling-conformational-transitions.pdf)
- Supplement: [[wiki/sources/SRC-0087-breaking-timescales-generative-sampling-conformational-transitions-supplement]]

## Summary

Tang et al. introduce Gen-COMPAS, an iterative rare-transition exploration workflow that combines a system-specific denoising diffusion model, bidirectional targeted molecular dynamics (TMD), short unbiased shooting trajectories, a variational committor network (VCN), and RiteWeight trajectory reweighting. It starts from endpoint structures and basin definitions without requiring low-dimensional collective variables (CVs) to drive proposal or committor learning; interpretable CVs are selected afterward for projection. Generated structures are proposal targets rather than equilibrium samples or final transition states. [SRC-0086, pp. 1–3, 7–8] [SRC-0087, Algorithm S1]

The paper demonstrates the workflow on systems from small peptides to Trp-cage, ribose-binding protein, mitochondrial ADP/ATP carrier (AAC), V-ATPase $V_o$, and muscle nicotinic acetylcholine receptor (nAChR). The authors explicitly frame the method as exploratory: pathway-level and local free-energy organization can be informative, but global equilibrium convergence and complete pathway discovery are not established for every complex system. [SRC-0086, pp. 3–6]

## Core workflow

1. Run short unbiased simulations from metastable basins $A$ and $B$ and train a diffusion model. [SRC-0086, p. 2]
2. Generate intermediate structures; cluster them in the first iteration, when no committor model exists. [SRC-0086, p. 2]
3. Refine each target by TMD launched independently from both endpoints. [SRC-0086, pp. 2, 8]
4. Remove the bias and launch unbiased trajectories from the refined configurations. TMD data are excluded from kinetic and thermodynamic estimators. [SRC-0086, pp. 2, 7–8]
5. Reweight the short unbiased trajectory ensemble with RiteWeight, train the VCN, and select new proposals near $q=1/2$. [SRC-0086, pp. 2, 7] [SRC-0087, pp. S10–S16]
6. Iterate until structural, committor, TMD-consistency, and free-energy diagnostics stabilize within reported uncertainty. [SRC-0086, p. 7] [SRC-0087, pp. S16–S35]

The contribution is the feedback-loop organization of established diffusion, committor-learning, TMD, path-construction, and reweighting components rather than invention of each component independently. [SRC-0086, p. 7]

## Evidence and applications

| System | Main evidence | Scope |
| --- | --- | --- |
| NANMA and trialanine | Recovered established small-peptide landscapes and pathways. For NANMA targets with predicted $q\approx0.1,0.3,0.5,0.7,0.9$, direct shooting gave means 0.174, 0.359, 0.485, 0.617, and 0.799; pointwise TMD-extracted agreement had $r=0.848$, and comparison along a 460,000-step unbiased trajectory gave correlation 0.9999668. [SRC-0087, pp. S2–S4, S22–S25] | Small vacuum benchmarks; the unbiased-trajectory correlation is not a large-system validation. |
| Trp-cage | Recovered two folding routes and semi-quantitative agreement with a 208.8 $\mu$s DESRES trajectory using 594 ns aggregate unbiased MD. Independent aimless shooting gave $r=0.898$, $R^2=0.806$ over 91 retained structures. [SRC-0086, p. 4] [SRC-0087, pp. S26–S30] | The roughly 350-fold figure compares trajectory budgets, not wall-clock time or equal-error efficiency. |
| Ribose-binding protein | Identified stepwise induced-fit and simultaneous binding/folding routes. [SRC-0087, pp. S5–S6] | Mechanistic agreement is mainly qualitative; no direct shooting benchmark is reported. |
| Holo and apo AAC | Holo AAC followed a segmented $C\rightarrow O\rightarrow M$ route with apparent barriers of about 2.5 and 2 kcal mol$^{-1}$; apo AAC lacked the occluded basin and had an approximately 10 kcal mol$^{-1}$ $C$–$M$ barrier. [SRC-0086, pp. 4–5] | The $O$ state was prepared before the segmented $C$–$O$ and $O$–$M$ calculations, so this test did not discover $O$ de novo from only $C$ and $M$. [SRC-0086, p. 9] |
| V-ATPase $V_o$ | Resolved a five-basin rotary sequence and rotor–stator contact rearrangements. The principal barrier was about 5–6 kcal mol$^{-1}$ versus about 8 kcal mol$^{-1}$ in the cited conventional study, with $\Delta G_{AB}<1$ kcal mol$^{-1}$ in both. [SRC-0087, pp. S7–S9] | Basin M3 lay near A here but about 5 kcal mol$^{-1}$ above A in the comparison. Projection degeneracy or multiple channels are proposed explanations, not independently established causes. |
| Muscle nAChR | Recovered an asymmetric unliganded-to-mono-liganded-to-di-liganded route and a pore-pre-active intermediate consistent with PDB 9E3G. [SRC-0086, p. 5] | The finite system always contains two explicit ACh molecules, and no 1 M correction was applied; reported basin differences are not standard binding free energies. |

## Mathematical structure

The committor is the probability that dynamics initiated from $x_0$ reaches $B$ before $A$: [SRC-0086, Eq. 1, p. 7]

$$
q(x_0)=\mathbb{P}\!\left(\tau_B(x_0)<\tau_A(x_0)\right),
$$

with $q=0$ in $A$, $q=1$ in $B$, and the $q=1/2$ separatrix used to identify the transition-state ensemble.

The VCN minimizes a lagged correlation/flux functional: [SRC-0086, Eq. 2, p. 7]

$$
J_{AB}[q;\tau]=\frac{C[q;\tau]}{\tau},
\qquad
C[q;\tau]=\frac{1}{2}\left\langle\left(q(\tau)-q(0)\right)^2\right\rangle.
$$

The VCN imposes the basin values explicitly and learns only the interior mapping: [SRC-0086, Eq. 3, p. 7]

$$
q_\omega(z)=
\begin{cases}
0, & z\in A, \\
F_\omega(z), & z\in(A\cup B)^c, \\
1, & z\in B.
\end{cases}
$$

Its unconstrained objective is $\mathcal L_{\mathrm{VCN}}[q_\omega]=2C[q_\omega;\tau]$; adding boundary-continuity penalties gives [SRC-0086, Eqs. 4–5, pp. 7–8]

$$
\mathcal L[q_\omega]
=
2C[q_\omega;\tau]
+
\lambda\left(
\left.F_\omega(z)^2\right|_{z\in A}
+
\left.\left(F_\omega(z)-1\right)^2\right|_{z\in B}
\right),
$$

and a final sigmoid bounds predictions in $[0,1]$.

TMD uses an RMSD restraint with a linearly decreasing target: [SRC-0086, Eqs. 6–7, p. 8]

$$
V_{\mathrm{TMD}}(t)
=
\frac{k_{\mathrm{TMD}}}{2N}
\left(\operatorname{RMSD}(t)-\operatorname{RMSD}^{*}(t)\right)^2,
$$

$$
\operatorname{RMSD}^{*}(t)
=
\operatorname{RMSD}(0)\left(1-\frac{t}{t_f}\right).
$$

## Equation inventory

| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |
| Committor definition, Eq. 1 | Main p. 7 | [[wiki/sources/SRC-0086-breaking-timescales-generative-sampling-conformational-transitions#Mathematical structure]] | Defines first-arrival probability and the separatrix. | $q$, $x_0$, $A$, $B$, $\tau_A$, $\tau_B$ | Target learned by the VCN and used to select transition-region structures. |
| VCN functional and boundary loss, Eqs. 2–5 | Main pp. 7–8 | [[wiki/sources/SRC-0086-breaking-timescales-generative-sampling-conformational-transitions#Mathematical structure]] | Learns a bounded committor from lagged trajectories. | $C$, $J_{AB}$, $q_\omega$, $F_\omega$, $z$, $\lambda$, $\tau$ | Defines the model objective and endpoint constraints. |
| TMD potential and schedule, Eqs. 6–7 | Main p. 8 | [[wiki/sources/SRC-0086-breaking-timescales-generative-sampling-conformational-transitions#Mathematical structure]] | Refines generated targets from both endpoint basins. | $V_{\mathrm{TMD}}$, $k_{\mathrm{TMD}}$, $N$, $t_f$ | Determines steering strength and duration; must be validated for structural plausibility. |
| DDPM, RiteWeight, convergence, and shooting equations | Supplement pp. S12–S31 | [[wiki/sources/SRC-0087-breaking-timescales-generative-sampling-conformational-transitions-supplement#Equation inventory]] | Supplies the full generative, reweighting, and validation mathematics. | See supplement glossary. | Essential for implementation and validation. |

## Variable glossary

- $A,B$: Reactant and product metastable basins. [SRC-0086, p. 7]
- $x_0$: Initial molecular configuration. [SRC-0086, Eq. 1]
- $q(x)$: Probability of reaching $B$ before $A$; $q=1/2$ identifies the separatrix. [SRC-0086, pp. 2, 7]
- $\tau_S$: First hitting time of basin $S$; $\tau$ without a subscript also denotes the VCN lag. [SRC-0086, Eqs. 1–2]
- $z\in\mathbb R^{3N-6}$: Z-matrix internal-coordinate representation of selected atoms, excluding rigid translation and rotation. [SRC-0086, p. 8]
- $\omega$: VCN parameters; $F_\omega$ is its unconstrained interior mapping. [SRC-0086, Eqs. 3–5]
- $\lambda$: Boundary-loss coefficient in the VCN objective. [SRC-0086, Eq. 5]
- $k_{\mathrm{TMD}}$, $N$, $t_f$: TMD force constant, selected-atom count, and steering duration. [SRC-0086, Eqs. 6–7]

## Proof and dependency map

The paper contains no formal theorem proof. Its technical dependency chain is empirical and algorithmic: endpoint trajectories train the DDPM; DDPM proposals are made physically accessible by bidirectional TMD; unbiased shooting supplies dynamical data; lagged data train the VCN; $q\approx1/2$ focuses subsequent sampling; RiteWeight reconstructs stationary weights; and structural, committor, TMD, bootstrap, and external-reference checks assess the result. [SRC-0086, pp. 2, 7–8] [SRC-0087, pp. S10–S35]

## Limitations and validation boundaries

- Gen-COMPAS is exploratory and does not replace converged equilibrium sampling or transition-path sampling. [SRC-0086, pp. 3, 6]
- Endpoint structures, basin definitions, atom selection, force field, model expressivity, and transition-region coverage remain consequential priors despite the absence of predefined low-dimensional sampling CVs. [SRC-0086, pp. 2–3, 7–8]
- Generated structures become evidence only after TMD refinement and unbiased dynamical validation. [SRC-0086, pp. 2–3, 7]
- Pathways disconnected from the supplied basins or missed by the proposal/refinement loop can remain undiscovered. [SRC-0086, pp. 3, 7]
- Bootstrap stability and agreement with the full available dataset do not establish globally converged equilibrium free energies. [SRC-0086, pp. 3, 6] [SRC-0087, pp. S18–S21]
- Direct shooting validation is strong for NANMA and Trp-cage but was considered prohibitively expensive for the larger systems, where the paper uses internal and ensemble diagnostics instead. [SRC-0087, pp. S22–S31]
- The main text's statement that reactive trajectories cross intermediate committor values monotonically is not established by a proof in the bundle and should not be generalized without separate review. [SRC-0086, p. 7]

## Claims

- [[wiki/claims/CLM-0043-generated-transition-proposals-require-dynamical-validation]]
- Gen-COMPAS combines system-specific generative proposals, explicit-Hamiltonian refinement, committor selection, and trajectory reweighting into an iterative transition-region exploration loop. [SRC-0086, pp. 2, 7] [SRC-0087, Algorithm S1]
- In the reported Trp-cage test, the learned committor agreed with independent aimless shooting at $r=0.898$ and $R^2=0.806$ over 91 retained structures. [SRC-0087, pp. S26–S27]

## Questions and tensions

- [[wiki/questions/QST-0009-scalable-independent-validation-of-learned-committors]]
- [[wiki/tensions/TEN-0016-internal-convergence-vs-external-free-energy-correctness]]
- The approximately 350-fold Trp-cage trajectory-budget reduction is not demonstrated as an equal-error or wall-clock speedup. [SRC-0086, p. 4] [SRC-0087, Table S6]
- The AAC presentation of endpoint-driven discovery is qualified by the preconstructed $O$ state and separate $C$–$O$ and $O$–$M$ committors. [SRC-0086, p. 9]

## Citation links

- Confirmed title match: the paper cites *Convergence is not correctness: context-dependent performance of enhanced-sampling methods across biological complexity*, ingested as SRC-0074. [SRC-0086, ref. 3]
- Confirmed title match: the paper cites *Boltzmann generators: sampling equilibrium states of many-body systems with deep learning*, ingested as SRC-0041. [SRC-0086, ref. 19]
- Citation review is partial; references were checked conservatively for already-ingested exact-title matches, not fully normalized.

## Code and data

- The paper names `https://github.com/Tangcyu/Gen-COMPAS` as the open-source package and says it includes a command-line interface, graphical interface, configurations, and representative inputs. No release tag or commit is fixed in the PDF. [SRC-0086, p. 10]
- Source data are stated to accompany the paper. External code and data were not ingested. [SRC-0086, p. 10]

## Metadata notes

- The PDF displays `Published online: xx xx xxxx`; no exact online publication date was inferred. [SRC-0086, p. 1]
- The source is a 2026 peer-reviewed Nature article accepted on 11 August 2026. [SRC-0086, p. 1]
- The supplement is required for Algorithm S1, full DDPM and RiteWeight details, numerical settings, GPU-cost estimates, and direct committor validation. [SRC-0087]

## Mathematical gaps

- Full DDPM, RiteWeight, convergence, and validation equations are represented on the supplement page rather than duplicated here. [SRC-0087]
- The wiki does not reproduce every model-architecture equation, system-specific CV definition, hyperparameter, or projected landscape.
- Apparent notation issues in supplementary Eqs. S2–S4 are preserved as an implementation-review gap on the supplement page rather than silently corrected. [SRC-0087, p. S12]

## Ingestion QA

### Retrieval questions checked

- What is Gen-COMPAS's central contribution, and which components does it combine?
- Which inputs remain required despite not using predefined low-dimensional sampling CVs?
- Are generated structures equilibrium samples or final transition states?
- How is the committor defined, learned, and used to select a transition-state ensemble?
- How are free-energy landscapes estimated from trajectories started outside equilibrium?
- What quantitative evidence supports the Trp-cage committor and sampling claim?
- Which applications lack direct committor-shooting validation?
- Was the AAC occluded state discovered de novo from only the $C$ and $M$ endpoints?
- Are the nAChR apparent free energies standard binding free energies?
- Are the reported free-energy landscapes globally equilibrium-converged?

### Coverage decision

Broad `math-standard` coverage as the main page of a `math-deep` bundle. This page captures the central contribution, main equations, applications, quantitative evidence, limitations, semantic links, citations, and retrieval questions; SRC-0087 supplies the detailed algorithm, estimators, validation equations, parameters, and implementation caveats. Formal `ingestion_status` remains `partial` because repository-wide validation is blocked by the pre-existing missing frontmatter in `wiki/answers/garnet-nonbonded-contact-cleanup.md`, and the supplement preserves unresolved mathematical and protocol inconsistencies.

### Known gaps

- Repository-wide validation does not pass because of the pre-existing unrelated missing-frontmatter error above; validation passes when that file is temporarily excluded.
- External source data, GitHub code, and cited works other than already-ingested exact matches were not ingested.
- Direct committor validation was not reported for the largest heterogeneous systems.
- Global equilibrium convergence and exhaustive pathway coverage remain explicitly unestablished.
- Final publication date, volume, issue, and page range are absent from the requested PDF.
