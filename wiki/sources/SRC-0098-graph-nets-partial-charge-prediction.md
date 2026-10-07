---
type: source
status: active
created: 2026-10-07
updated: 2026-10-07
source_id: SRC-0098
display_title: "Graph Nets for Partial Charge Prediction"
short_title: "Graph Nets for Partial Charge Prediction"
aliases:
  - "SRC-0098"
  - "Graph Nets for Partial Charge Prediction"
  - "Wang et al. 2019 charge equilibration"
source_path: raw/sources/SRC-0098-graph-nets-partial-charge-prediction.pdf
imported_path: raw/sources/SRC-0098-graph-nets-partial-charge-prediction.pdf
original_filename: "wang2019.pdf"
original_path_note: "Original local path omitted from wiki metadata. File downloaded directly from arXiv (https://arxiv.org/pdf/1909.07903); the original filename is a generic working name, not a publisher filename."
sha256: 232430544399509a2ea1f22ecbf6f38fb00c44046c8ed63935582c4055d3d759
authors:
  - "Yuanqing Wang"
  - "Josh Fass"
  - "Chaya D. Stern"
  - "Kun Luo"
  - "John D. Chodera"
author_entities:
  - "[[wiki/entities/authors/john-d-chodera]]"
year: 2019
venue: "arXiv preprint (physics.comp-ph), marked 'Preprint. Under review.'"
doi:
arxiv: "1909.07903"
metadata_review_status: reviewed
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/machine-learning/molecular-modeling
tags:
  - partial-charges
  - charge-equilibration
  - electronegativity
  - hardness
  - graph-neural-networks
  - espaloma
related:
  - "[[wiki/sources/SRC-0072-machine-learned-molecular-mechanics-force-fields-from-large]]"
  - "[[wiki/sources/SRC-0073-supplementary-material-for-machine-learned-molecular-mechanics-force]]"
  - "[[wiki/sources/SRC-0016-fine-tuning-mm-force-fields-to-experimental-free-energies]]"
  - "[[wiki/concepts/espaloma-machine-learned-mm-force-fields]]"
  - "[[wiki/concepts/free-energy-reweighting-for-force-field-fine-tuning]]"
  - "[[wiki/answers/qeq-per-type-electronegativity-hardness-redundancy]]"
sources:
  - SRC-0098
cites_sources: []
citation_match_status: reviewed
cqt_review_status: none-needed
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: math-deep
---

# Graph Nets for Partial Charge Prediction

Source ID: `SRC-0098`

## Raw source

- Repository path: `raw/sources/SRC-0098-graph-nets-partial-charge-prediction.pdf`
- Open raw source: [raw/sources/SRC-0098-graph-nets-partial-charge-prediction.pdf](../../raw/sources/SRC-0098-graph-nets-partial-charge-prediction.pdf)

## Summary

Wang, Fass, Stern, Luo, and Chodera present a Graph Net (full-block, Battaglia-style) architecture that predicts atomic partial charges from molecular topology alone (no conformation dependence), trained to reproduce DFT-derived reference charges from a curated ChEMBL subset (Bleiziffer et al.). The central contribution for later force-field work is not the graph architecture itself but §2.4: a differentiable, exact way to enforce the net-molecular-charge constraint by having the network predict per-atom electronegativity and hardness instead of charges directly, then solving a quadratic charge-equilibration (QEq) problem in closed form via a single Lagrange multiplier. This QEq layer is geometry-independent (no pairwise Coulomb coupling between atoms) and is the method later adopted, citing this paper directly, by Espaloma's charge model (SRC-0072, SRC-0073) and by one-shot espaloma charge fine-tuning (SRC-0016). [SRC-0098]

## Key Points

- Problem: a per-atom charge predictor must satisfy $\sum_i \hat q_i = Q$, the known total molecular charge (Eq. 12). Two naive fixes were tried and rejected: (1) no explicit constraint, letting the model "learn" it (RMSE $\approx 0.280\,e$); (2) redistributing any excess/deficit charge evenly across all atoms, following Bleiziffer et al. [2018]. Neither gave satisfactory results with this model. [SRC-0098]
- Adopted fix (credited to Gilson, Gilson & Potter, 2003, *J. Chem. Inf. Comput. Sci.* 43(6):1982–1997, doi `10.1021/ci034148o`, not separately ingested in this wiki): instead of predicting charges directly, the network predicts the first and second partial derivatives of the potential energy with respect to each atom's charge, i.e. an electronegativity $e_i = \partial E/\partial q_i$ and a hardness $s_i = \partial^2E/\partial q_i^2$ (Eq. 13). [SRC-0098]
- Charges are then obtained by minimizing the second-order Taylor expansion of the charge-dependent energy, $\sum_i (e_i q_i + \tfrac12 s_i q_i^2)$, subject to the net-charge constraint (Eq. 14). This optimization has no cross-atom Coulomb term and no geometric/conformational dependence; it is purely a per-atom quadratic program coupled only through the single linear constraint. [SRC-0098]
- The constrained minimization has an exact closed form via one Lagrange multiplier (Eq. 15), so the charge layer is differentiable end-to-end and its Jacobian/Hessian are "trivially easy to calculate." [SRC-0098]
- Trained against DFT reference charges (dielectric $\epsilon=4$) for 350,259 molecules from ChEMBL curated by Bleiziffer et al., with an 80:20 train/test split and 5-fold cross-validated hyperparameter search. Overall held-out RMSE $\approx 0.0223\,e$ ($R^2 \approx 0.9936$), reported as roughly within the DFT-vs-AM1-BCC discrepancy and about 500x faster than AM1-BCC to evaluate (~0.03 s/molecule). No positive correlation was observed between error and molecule size (up to 63 atoms). [SRC-0098]
- The broader architecture (§2.1–2.3) is a standard full-block Graph Net: one-hot element features initialize node attributes, bond order initializes edge attributes, and rounds of edge-update / edge-to-node-aggregate / node-update / (optionally global-update) message passing produce the final per-atom $\{\hat e_i,\hat s_i\}$ read out after $T$ rounds. [SRC-0098]

## Core equations

### Net-charge constraint

$$
\sum_i \hat q_i = \sum_i q_i = Q
\tag{12}
$$

where $Q$ is the total (signed) molecular charge. [SRC-0098]

### Electronegativity and hardness as energy derivatives

$$
e_i \equiv \frac{\partial E}{\partial q_i}, \qquad
s_i \equiv \frac{\partial^2 E}{\partial q_i^2}.
\tag{13}
$$

[SRC-0098]

### Constrained QEq minimization

$$
\{\hat q_i\} = \operatorname*{arg\,min}_{q_i}
\sum_i \left( \hat e_i q_i + \tfrac12 \hat s_i q_i^2 \right)
\quad \text{subject to Eq. 12.}
\tag{14}
$$

[SRC-0098]

### Closed-form solution

$$
\hat q_i = -e_i s_i^{-1} + s_i^{-1}\,
\frac{Q + \sum_j e_j s_j^{-1}}{\sum_j s_j^{-1}}.
\tag{15}
$$

[SRC-0098]

### Graph Net architecture (summary; not the paper's main contribution for charge-equilibration purposes)

$$
\mathcal G = \{\mathcal V, \mathcal E, \mathcal U\}
\tag{1}
$$

Node/edge/global initialization (one-hot element features through a feedforward net for nodes; bond order through a feedforward net for edges; zeros for the global attribute) (Eqs. 2–3); message passing per round $t$:

$$
e_k^{(t+1)} = \phi^e\!\left(e_k^{(t)}, \textstyle\sum_{i\in\mathcal N_k^e} v_i, u^{(t)}\right), \quad
\bar e_i^{(t+1)} = \rho^{e\to v}(E_i^{(t+1)}), \quad
v_i^{(t+1)} = \phi^v\!\left(\bar e_i^{(t+1)}, v_i^{(t)}, u^{(t)}\right),
\tag{4–6}
$$

$$
\bar e^{(t+1)} = \rho^{e\to u}(E^{(t+1)}), \quad
\bar v^{(t+1)} = \rho^{v\to u}(V^{(t)}), \quad
u^{(t+1)} = \phi^u\!\left(\bar e^{(t+1)}, \bar v^{(t+1)}, u^{(t)}\right),
\tag{7–9}
$$

readout after $T$ rounds, $\hat y = f^r(\{\{v^{(t)},e^{(t)},u^{(t)}\}, t=1,\dots,T\})$ (Eq. 10), and a batching rule that concatenates small molecular graphs' adjacency matrices into a block-diagonal batch (Eq. 11). [SRC-0098]

## Derivation sketch (Eq. 14 $\to$ Eq. 15)

Form the Lagrangian for Eq. 14 with multiplier $\lambda$ for the single constraint $\sum_i q_i = Q$:

$$
\mathcal L(q,\lambda) = \sum_i \left(e_i q_i + \tfrac12 s_i q_i^2\right) - \lambda\left(\sum_i q_i - Q\right).
$$

Stationarity in $q_i$ gives $e_i + s_i q_i - \lambda = 0$, i.e. $q_i = (\lambda - e_i)/s_i$. Substituting into the constraint, $\sum_i (\lambda - e_i)/s_i = Q$, gives $\lambda = \left(Q + \sum_i e_i/s_i\right) / \sum_i (1/s_i)$. Substituting back reproduces Eq. 15. Because each $s_i>0$ (hardness) is implicitly treated as positive, the objective is strictly convex and the single linear constraint has full row rank, so this stationary point is the unique global minimizer. The paper does not spell out this convexity/uniqueness argument explicitly; it is a direct, low-risk completion of the stated derivation. [SRC-0098]

## Equation inventory

| Equation / label | Source location | Wiki location | Purpose | Variables | Implementation relevance |
| --- | --- | --- | --- | --- | --- |
| Net-charge constraint | §2.4, Eq. 12 | This page, "Core equations" | States the constraint any charge model must satisfy. | $\hat q_i$, $Q$ | Defines correctness criterion for any charge-equilibration layer. |
| Electronegativity/hardness definitions | §2.4, Eq. 13 | This page | Defines the predicted quantities as energy derivatives, following Gilson et al. 2003. | $e_i$, $s_i$, $E$ | Explains why a network predicts two scalars per atom instead of one charge. |
| Constrained QEq objective | §2.4, Eq. 14 | This page | States the quadratic program solved for charges. | $\hat e_i$, $\hat s_i$, $q_i$ | The exact optimization implemented downstream (e.g. Espaloma, FFRefine). |
| Closed-form QEq solution | §2.4, Eq. 15 | This page; derivation sketch | Analytic Lagrange-multiplier solution, differentiable end-to-end. | $e_i$, $s_i$, $Q$ | Directly reusable formula; the single-species special case of more general multi-constraint QEq systems (cf. [SRC-0016]). |
| Graph Net message passing | §2.2, Eqs. 4–9 | This page, architecture summary | Defines how per-atom $\{\hat e_i,\hat s_i\}$ are produced from molecular topology. | $v_i$, $e_k$, $u$, $\phi^\bullet$, $\rho^\bullet$ | Context for how electronegativity/hardness are made transferable across molecules; not reused verbatim by later QEq-only applications that use fixed per-type coefficients instead of a GNN. |

## Mathematical gaps

- The paper does not prove convexity/uniqueness of the Eq. 14 solution explicitly; the wiki's derivation sketch above fills this gap as a direct, low-risk completion, not as content verified against the paper's own text.
- The paper does not discuss the rank or redundancy of the $\{e_i,s_i\}\to q_i$ map when $e_i,s_i$ are not independently predicted per atom but are instead looked up from a small shared set of per-type (rather than per-atom, network-predicted) coefficients. That question is outside this paper's scope (its $e_i,s_i$ are always per-atom GNN outputs) and is addressed as a separate, project-grounded synthesis in [[wiki/answers/qeq-per-type-electronegativity-hardness-redundancy]].

## Evidence

- Held-out test RMSE $\approx 0.0223\,e$ overall ($R^2\approx0.9936$) across 299,811 held-out atoms; per-element RMSE ranges from about $0.013\,e$ (H) to $0.195\,e$ (I, only 105 samples, large uncertainty). [SRC-0098]
- No explicit no-constraint baseline RMSE other than the reported $\approx 0.280\,e$ figure; no separate ablation RMSE is reported for the "redistribute excess charge evenly" baseline beyond the qualitative statement that it was also unsatisfactory. [SRC-0098]
- Reported ~500x speed-up versus AM1-BCC, with per-molecule inference around 0.03 s. [SRC-0098]

## Limitations and Caveats

- Reference charges (DFT, $\epsilon=4$, Bleiziffer et al. curated ChEMBL subset) are themselves conformation-dependent in principle, though the paper argues the lowest-energy conformation used is deterministic given the topology; the authors note they are moving toward AM1-BCC ELF10 references, which are built to be conformation-independent. [SRC-0098]
- The dataset's largest molecule has 63 atoms; scalability beyond that size is inferred from the absence of a size-error trend within this range, not demonstrated on larger systems. [SRC-0098]
- Elements with few samples (I: 105, Cl: 1215, Br: 572) have much higher RMSE and wide confidence intervals; per-element accuracy should not be treated as uniform. [SRC-0098]
- The paper's own comparison is restricted to a Random Forest baseline (Bleiziffer et al.) and to AM1-BCC on runtime; it does not benchmark against other QEq-style or GNN charge models. [SRC-0098]

## Links

- [[wiki/sources/SRC-0072-machine-learned-molecular-mechanics-force-fields-from-large]]
- [[wiki/sources/SRC-0073-supplementary-material-for-machine-learned-molecular-mechanics-force]]
- [[wiki/sources/SRC-0016-fine-tuning-mm-force-fields-to-experimental-free-energies]]
- [[wiki/concepts/espaloma-machine-learned-mm-force-fields]]
- [[wiki/concepts/free-energy-reweighting-for-force-field-fine-tuning]]
- [[wiki/answers/qeq-per-type-electronegativity-hardness-redundancy]]
- [[wiki/answers/ffrefine-paper-methods-knowledge-base]]

## Citation links

- This paper's own charge-equilibration trick (§2.4) is explicitly credited to Gilson, Gilson & Potter, *J. Chem. Inf. Comput. Sci.* 43(6):1982–1997 (2003), doi `10.1021/ci034148o` (reference [6] in the source). This source is not separately ingested in this wiki; cite it by DOI rather than by a wiki source ID until it is ingested.
- Reference charges and part of the dataset are credited to Bleiziffer, Schaller & Riniker, *J. Chem. Inf. Model.* 58(3):579–590 (2018), doi `10.1021/acs.jcim.7b00663` (reference [2]). Not separately ingested.
- Confirmed downstream citation (checked against the SRC-0072 raw PDF text, 2026-10-07): espaloma-0.3's main text cites this paper (its reference 68, arXiv `190907903`) by name ("following the protocol of Wang et al.68 we predict the electronegativity and hardness of atoms used in a charge equilibration67") immediately alongside its reference 67, which is the same Gilson 2003 paper cited above. [SRC-0072]
- Confirmed context match (not line-by-line verified against the SRC-0016 raw PDF): SRC-0016's charge-equilibration equation ($\mathbf q^*=\arg\min \sum_i e_i^*q_i + \tfrac12 s_i^*q_i^2$ subject to $\sum_i q_i=Q$) is the same functional form as Eq. 14 here and is used for espaloma charge fine-tuning, consistent with SRC-0016 reusing the Espaloma/Wang et al. charge-equilibration layer rather than re-deriving it.

## Open Questions

- The paper does not address what happens to the expressiveness of the $\{e_i,s_i\}\to q_i$ map when electronegativity and hardness are not independent per-atom network outputs but are instead shared, looked-up coefficients per atom type (the setting relevant to non-GNN force-field refinement). See [[wiki/answers/qeq-per-type-electronegativity-hardness-redundancy]] for a project-grounded answer to this question.
- It is not established in this source whether hardness $s_i$ carries distinguishable information from electronegativity $e_i$ when both are fit to the same charge targets without any out-of-sample transfer test; the paper's own training always transfers to new molecules (via the GNN), so this question does not arise in its own setting.

## Ingestion QA

### Retrieval questions checked

- What problem does this paper solve, and why does the net-charge constraint matter?
- What two naive constraint-handling approaches were tried, and why were they rejected?
- What is the Gilson-et-al.-derived trick, and what do electronegativity and hardness mean here?
- What is the exact closed-form charge solution, and how is it derived?
- What accuracy and speed were achieved, and against what reference?
- What are the main limitations (element coverage, molecule size, reference-charge dependence)?
- Which later sources cite this paper's charge-equilibration method, and for what purpose?

### Coverage decision

Complete at `coverage_profile: math-deep`. This short paper's full charge-equilibration derivation (§2.4, Eqs. 12–15) is reproduced with a derivation sketch and equation inventory; the surrounding Graph Net architecture (§2.1–2.3) is summarized at a level sufficient for context and retrieval without reproducing every architectural variant, since it is not the aspect reused by the force-field-refinement sources this page links to.

### Known gaps

- The Graph Net propagation/readout details (choice of specific $\phi$/$\rho$ functions, hyperparameters, training losses beyond charge RMSE) are summarized rather than fully reproduced, since they are not required for understanding or reusing the charge-equilibration layer.
- Figure 1 (predicted-vs-true scatter plot) is described qualitatively (per-element RMSE table reproduced) rather than reproduced as an image.
