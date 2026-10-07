---
type: answer
status: active
created: 2026-10-07
updated: 2026-10-07
question: "When charge-equilibration (QEq) electronegativity and hardness coefficients are shared per atom type (looked up) instead of predicted per atom by a network, is the hardness parameter redundant, and when does it matter?"
answer_status: answered
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/machine-learning/molecular-modeling
tags:
  - charge-equilibration
  - electronegativity
  - hardness
  - identifiability
  - force-field-optimization
  - fisher-information
  - espaloma
related:
  - "[[wiki/sources/SRC-0098-graph-nets-partial-charge-prediction]]"
  - "[[wiki/sources/SRC-0072-machine-learned-molecular-mechanics-force-fields-from-large]]"
  - "[[wiki/sources/SRC-0016-fine-tuning-mm-force-fields-to-experimental-free-energies]]"
  - "[[wiki/concepts/espaloma-machine-learned-mm-force-fields]]"
  - "[[wiki/concepts/free-energy-reweighting-for-force-field-fine-tuning]]"
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
  - "[[wiki/answers/ffrefine-paper-methods-knowledge-base]]"
  - "[[wiki/answers/training-initially-disabled-lennard-jones-parameters]]"
sources:
  - SRC-0098
  - SRC-0072
  - SRC-0073
  - SRC-0016
sensitivity: public
encryption: none
wiki_pages_used:
  - "[[wiki/answers/ffrefine-paper-methods-knowledge-base]]"
  - "[[wiki/concepts/espaloma-machine-learned-mm-force-fields]]"
  - "[[wiki/concepts/free-energy-reweighting-for-force-field-fine-tuning]]"
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
  - "[[wiki/answers/training-initially-disabled-lennard-jones-parameters]]"
raw_sources_consulted:
  - "SRC-0098 (raw PDF, read in full this session)"
  - "SRC-0072 (raw PDF, checked around the charge-equilibration sentence and its reference list this session)"
wiki_pages_updated:
  - "[[wiki/sources/SRC-0098-graph-nets-partial-charge-prediction]]"
  - "[[wiki/sources/SRC-0072-machine-learned-molecular-mechanics-force-fields-from-large]]"
  - "[[wiki/concepts/espaloma-machine-learned-mm-force-fields]]"
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
  - "[[wiki/answers/training-initially-disabled-lennard-jones-parameters]]"
  - "[[wiki/index]]"
  - "[[wiki/log]]"
project_evidence:
  - "FFRefine (coding-project) session, reported 2026-10-07: per-type QEq redundancy, zero-charge-seed multiplicative-bound failure, and the supervised-vs-reweighting training contrast, observed while reusing FFRefine's multiplicity-weighted QEq implementation for force-field refinement. The derivations in this note were independently re-derived and checked during this SecondBrain write-back against FFRefine's already-recorded QEq KKT system in [[wiki/answers/ffrefine-paper-methods-knowledge-base]]; the FFRefine project's own Julia code was not inspected directly by this write-back."
---

# When Is a Per-Type QEq Hardness Coefficient Redundant?

## Short answer

The charge-equilibration (QEq) trick used by Wang et al. ([[wiki/sources/SRC-0098-graph-nets-partial-charge-prediction]]) and by Espaloma ([[wiki/sources/SRC-0072-machine-learned-molecular-mechanics-force-fields-from-large]]) predicts a per-atom electronegativity $e_i$ and hardness $s_i$ and solves a constrained quadratic program for charges. That functional form generalizes directly to force-field refinement where $e$ and $s$ are not per-atom network outputs but a small set of shared, per-atom-type (looked-up) coefficients reused across possibly many species with their own net-charge constraints — this is exactly the multiplicity-weighted QEq system already recorded in [[wiki/answers/ffrefine-paper-methods-knowledge-base]].

Within that per-type setting, **hardness is redundant with electronegativity for any single fixed fitting problem**: for any target charge vector $q^\*$ satisfying all configured constraints, the choice $e=-q^\*$, $h=\mathbf 1$ (uniform hardness), and zero Lagrange multipliers already reaches $q^\*$ exactly, and because the QEq energy is strictly convex this is the *unique* minimizer. The map from $(e,h)$ to charges therefore has the same achievable image, and the same differential rank, whether or not $h$ is allowed to vary at all. Concretely, for $p$ shared charge parameters and $r$ independent net-charge constraints, the combined $(e,h)$-Jacobian has rank exactly $p-r$ — the dimension of the feasible charge subspace — and every hardness-direction Jacobian column is literally a scalar multiple ($q_k$) of the corresponding electronegativity-direction column, so $h$ contributes no column that is not already spanned by $e$. For a two-type water model with one net-charge constraint ($p=2$, $r=1$), only one combination of the four coefficients $(e_O,e_H,s_O,s_H)$ changes the charges at all.

Two gauge (null) directions follow directly: a uniform additive shift of every $e_t$ by the same constant is exactly absorbed by an equal shift of every constraint's Lagrange multiplier, and a joint positive rescaling of $(e,h,\lambda)$ by any $\alpha>0$ leaves the charges unchanged. So, within one fixed fit, $e$ and $h$ are not independently meaningful "physical" electronegativities and hardnesses; they are effective coefficients defined only up to this gauge.

**Consequence for optimization:** because the loss, any charge-space prior, and the reduced potential depend on $(e,h)$ only through the charges $q(e,h)$, the chain rule sends every null direction of the $(e,h)\to q$ Jacobian to a null direction of the loss gradient and of the Gauss–Newton/Fisher metric built from it. A per-type QEq block of a Fisher or Gauss–Newton matrix is therefore structurally singular along these directions — not merely poorly conditioned — and needs a treatment that tolerates or removes a hard zero eigenvalue block (e.g. Tikhonov-damped modal gain or exclusion of non-positive eigenvalues, as already used in [[wiki/answers/ffrefine-paper-methods-knowledge-base]]'s optimizer step), not just generic regularization.

**When hardness does matter:** the redundancy proof is specific to one fixed constraint structure (fixed set of species/molecules used in the fit). The *same* shared per-type coefficients, applied to a molecule with a different net-charge grouping or type multiplicity, generally produce different charges depending on $h$ even though $h$ was completely unconstrained by the original fit. Hardness is therefore a real, meaningful degree of freedom exactly when coefficients are expected to transfer to molecular environments outside the fitting set — which is the setting Wang et al.'s graph net and Espaloma are actually built for (per-atom $e_i,s_i$ generated by a network trained across very many distinct molecules), and is not the setting of fitting a handful of shared per-type coefficients to a small, fixed set of training species.

## Detailed answer

### Setup: the per-type QEq system this reuses

[[wiki/answers/ffrefine-paper-methods-knowledge-base]] already records the multiplicity-weighted, constrained QEq energy used when a shared charge parameter $q_j$ ($j=1,\dots,p$, one per atom type / shared descriptor) can appear with multiplicity $A_{gj}$ in several net-charge constraint groups $g=1,\dots,r$ (e.g. one group per solute molecule in a solvated system):

$$
E(\mathbf q) = \sum_{j=1}^p m_j\left(e_jq_j+\tfrac12 h_jq_j^2\right),
\qquad
A\mathbf q=\mathbf Q,
\qquad
m_j=\sum_g A_{gj},
\qquad
D=\operatorname{diag}(m_1,\dots,m_p).
$$

This is the direct multi-species, multi-multiplicity generalization of Eq. 14 in [[wiki/sources/SRC-0098-graph-nets-partial-charge-prediction]]; for one species with unit multiplicities it reduces exactly to Wang et al.'s single-constraint problem, and the single-multiplier solution reduces to their Eq. 15.

With $H=\operatorname{diag}(\mathbf h)$, $\overline A=AD^{-1}$, $R=H^{-1}$, $G=AR\overline A^T$, the stationarity system (already derived in that page) is

$$
D(\mathbf e+H\mathbf q)=A^T\boldsymbol\lambda,
\qquad
G\boldsymbol\lambda=\mathbf Q+AR\mathbf e,
\qquad
\mathbf q=R(\overline A^T\boldsymbol\lambda-\mathbf e).
$$

This setup assumes $r=\operatorname{rank}(A)$, i.e. the constraint rows are independent (no redundant net-charge constraints), and $h_j>0$ for every used type, so $D$ and $H$ are positive diagonal and $G$ is invertible.

### Proof 1: electronegativity alone reaches every feasible charge vector

Fix any charge vector $\mathbf q^\*$ with $A\mathbf q^\*=\mathbf Q$ (i.e. any charge assignment that already satisfies every configured net-charge constraint). Set

$$
\mathbf e=-\mathbf q^\*,
\qquad
\mathbf h=\mathbf 1,
\qquad
\boldsymbol\lambda=\mathbf 0.
$$

Then $D(\mathbf e+H\mathbf q^\*) = D(-\mathbf q^\*+\mathbf q^\*) = \mathbf 0 = A^T\mathbf 0$, so the stationarity condition holds, and $A\mathbf q^\*=\mathbf Q$ holds by assumption. With $h_j=1>0$ for all $j$, $E(\mathbf q)$ is strictly convex (its Hessian is $D\succ0$), and $\{\mathbf q:A\mathbf q=\mathbf Q\}$ is a nonempty affine subspace, so this stationary point is the *unique* global minimizer: $\mathbf q(\mathbf e,\mathbf h)=\mathbf q^\*$.

Because this works for every feasible $\mathbf q^\*$, the map $\mathbf e\mapsto\mathbf q(\mathbf e,\mathbf 1)$ (hardness fixed at any positive constant vector) is already onto the entire feasible subspace $\{\mathbf q:A\mathbf q=\mathbf Q\}$. Varying $\mathbf h$ cannot reach anything outside that subspace either (the constraint $A\mathbf q=\mathbf Q$ holds for every $\mathbf h$), so hardness adds no new reachable charge vectors.

### Proof 2: the hardness Jacobian is pointwise proportional to the electronegativity Jacobian

Differentiating the stationarity system (as in [[wiki/answers/ffrefine-paper-methods-knowledge-base]]'s "Analytic QEq Jacobian" section) gives, for a perturbation of electronegativity alone,

$$
\frac{\partial\mathbf q}{\partial e_k}=M\,\mathbf u_k,
\qquad
M:=H^{-1}\!\left(\overline A^TG^{-1}AH^{-1}-I\right),
$$

where $\mathbf u_k$ is the $k$-th coordinate vector. Differentiating with respect to $h_k$ instead (holding $\mathbf e$ fixed) and simplifying using $AH^{-1}\overline A^TG^{-1}=I_r$ (by definition of $G$) gives the identity

$$
\boxed{
\frac{\partial\mathbf q}{\partial h_k}=q_k\,\frac{\partial\mathbf q}{\partial e_k}.
}
$$

Every hardness-direction Jacobian column is exactly the corresponding electronegativity-direction column scaled by the current charge value $q_k$. Stacking all $2p$ columns, the combined $(\mathbf e,\mathbf h)\to\mathbf q$ Jacobian therefore has the same column space, and the same rank, as the $p$-column electronegativity-only Jacobian $M$.

Separately, $AM=A H^{-1}\overline A^TG^{-1}AH^{-1}-AH^{-1}=GG^{-1}AH^{-1}-AH^{-1}=0$, so every column of $M$ lies in $\ker A$, a $(p-r)$-dimensional space, giving $\operatorname{rank}(M)\le p-r$. Combined with Proof 1 (the map $\mathbf e\mapsto\mathbf q$ is affine in $\mathbf e$ for fixed $\mathbf h$, and is onto the $(p-r)$-dimensional feasible affine subspace), the rank is exactly $p-r$. For a two-type water model with one net-charge constraint, $p-r=2-1=1$: only one combination of the four coefficients $(e_O,e_H,h_O,h_H)$ changes the charges; the other three directions are exactly inert.

### Two explicit gauge (null) directions

- **Uniform shift of electronegativity.** Since $m_j=\sum_gA_{gj}=(A^T\mathbf 1_r)_j$ by definition of $m_j$, we have $D\mathbf 1_p=A^T\mathbf 1_r$. Shifting every $e_j\to e_j+c$ changes the stationarity condition by $cD\mathbf 1_p=cA^T\mathbf 1_r=A^T(c\mathbf 1_r)$, which is exactly compensated by shifting every constraint's multiplier $\lambda_g\to\lambda_g+c$. The charges are unchanged; a uniform electronegativity shift is absorbed by the Lagrange multipliers.
- **Joint rescaling.** Replacing $(\mathbf e,\mathbf h,\boldsymbol\lambda)\to(\alpha\mathbf e,\alpha\mathbf h,\alpha\boldsymbol\lambda)$ for any $\alpha>0$ scales the stationarity condition by $\alpha$ and leaves $\mathbf q=R(\overline A^T\boldsymbol\lambda-\mathbf e)=(\alpha H)^{-1}(\overline A^T(\alpha\boldsymbol\lambda)-\alpha\mathbf e)$ exactly unchanged. $\mathbf e$ and $\mathbf h$ are therefore only meaningful up to a common positive scale, not as independently calibrated physical electronegativities/hardnesses.

### Consequence for optimization

Any scalar quantity that depends on $(\mathbf e,\mathbf h)$ only through $\mathbf q(\mathbf e,\mathbf h)$ — the per-type QEq loss, a charge-space prior, or an ensemble-observable loss computed from the resulting partial charges — has, by the chain rule, a gradient and a Gauss–Newton/Fisher metric whose null space contains every null direction of the $(\mathbf e,\mathbf h)\to\mathbf q$ Jacobian identified above. The per-type QEq block of such a Fisher matrix is therefore **structurally singular**, not merely ill-conditioned: at least $p+r$ of the $2p$ coefficient directions (the $p-(p-r)=r$-dimensional residual electronegativity gauge plus the full $p$-dimensional hardness block) carry exactly zero first-order signal for any loss built only from the resulting charges. A Tikhonov-damped modal gain ($\lambda_j/(\lambda_j^2+\gamma^2)$, as already used in [[wiki/answers/ffrefine-paper-methods-knowledge-base]]'s optimizer step) or exclusion of non-positive/negligible eigenvalues is required to keep a natural-gradient or trust-region step well defined; ordinary ridge damping that assumes a merely ill-conditioned (not singular) metric understates the problem.

### When hardness is not redundant: transfer beyond the fitting set

The redundancy proof is specific to one fixed constraint matrix $A$ — i.e. one fixed collection of species and type multiplicities used in a given fit. It does **not** say that $\mathbf h$ is irrelevant to predictions on a molecule outside that fit. If the same shared per-type $(\mathbf e,\mathbf h)$ are applied to a new molecule with a different constraint matrix $A'$ (different atoms, different per-type multiplicities), the resulting charges $\mathbf q'=R(\overline{A'}^T\boldsymbol\lambda'-\mathbf e)$ depend on $\mathbf h$ explicitly through $R=H^{-1}$ and through $G'=A'RH^{-1}\overline{A'}^T$-style terms specific to $A'$ — terms that did not appear, or appeared differently, for the original $A$. A value of $\mathbf h$ that was entirely unconstrained by the training fit (any positive vector gave an equally good fit) can therefore still change predictions on unseen molecules.

This is exactly why hardness is a meaningful, trained quantity in [[wiki/sources/SRC-0098-graph-nets-partial-charge-prediction]] and in Espaloma ([[wiki/sources/SRC-0072-machine-learned-molecular-mechanics-force-fields-from-large]], [[wiki/sources/SRC-0073-supplementary-material-for-machine-learned-molecular-mechanics-force]]): there, $e_i,s_i$ are per-atom outputs of a graph net trained by supervised regression against DFT- or AM1-BCC-ELF10-derived reference charges across hundreds of thousands of distinct molecules, so the training signal constrains how $(e_i,s_i)$ must behave across many different constraint structures $A'$ simultaneously, breaking the single-$A$ gauge freedom. It is also why [[wiki/sources/SRC-0016-fine-tuning-mm-force-fields-to-experimental-free-energies]]'s low-rank electronegativity/hardness fine-tuning remains well posed: it perturbs a pretrained, already-transferable espaloma charge model rather than fitting $(\mathbf e,\mathbf h)$ from a cold start on one fixed constraint structure.

By contrast, a force-field refinement that fits a *small, fixed* set of per-type QEq coefficients to a *small, fixed* set of training species (the per-type, non-GNN setting analyzed above, as used e.g. by FFRefine) has no charge-space transfer signal at all during that fit: its loss comes only from ensemble observables or free energies evaluated on the same species used to define $A$. Within that fit, hardness is pure gauge and should be expected to show up as exact or near-exact zero eigenvalues in an empirical Fisher or Gauss–Newton metric, not as a weak but nonzero direction.

### Practical caveat: relative bounds fail at a zero charge seed

A common way to keep a QEq electronegativity coefficient local during optimization is an epoch-local relative (multiplicative) trust-region window, e.g. $e_t\in[e_t^{(0)}(1-f),\,e_t^{(0)}(1+f)]$ around the current value $e_t^{(0)}=-q_t^{(0)}$. If an atom type starts with exactly zero charge, $q_t^{(0)}=0$ gives $e_t^{(0)}=0$, and the multiplicative window collapses to the single point $\{0\}$: the optimizer can never move that type's electronegativity away from zero. This is the same structural failure mode as the zero-amplitude Lennard-Jones case already recorded in [[wiki/answers/training-initially-disabled-lennard-jones-parameters]] — a relative/multiplicative bound degenerates exactly where the underlying physical quantity passes through zero. The practical fix is the same in kind: use an additive (absolute) trust-region window for coefficients that can start at or pass through zero, reserving multiplicative windows for coefficients bounded away from zero.

## Key equations

Multiplicity-weighted QEq energy and constraint (already recorded in [[wiki/answers/ffrefine-paper-methods-knowledge-base]]):

$$
E(\mathbf q)=\sum_{j=1}^pm_j\left(e_jq_j+\tfrac12h_jq_j^2\right),
\qquad
A\mathbf q=\mathbf Q.
$$

Redundancy witness: for any feasible $\mathbf q^\*$,

$$
\mathbf e=-\mathbf q^\*,\quad\mathbf h=\mathbf 1,\quad\boldsymbol\lambda=\mathbf 0
\quad\Longrightarrow\quad
\mathbf q(\mathbf e,\mathbf h)=\mathbf q^\*.
$$

Hardness-Jacobian identity (new, derived in this note):

$$
\frac{\partial\mathbf q}{\partial h_k}=q_k\,\frac{\partial\mathbf q}{\partial e_k},
\qquad
\operatorname{rank}\!\left[\frac{\partial\mathbf q}{\partial\mathbf e}\ \Big|\ \frac{\partial\mathbf q}{\partial\mathbf h}\right]=p-r.
$$

Gauge directions (new, derived in this note):

$$
\mathbf e\to\mathbf e+c\mathbf 1_p,\ \boldsymbol\lambda\to\boldsymbol\lambda+c\mathbf 1_r
\quad\text{(uniform shift, since }D\mathbf 1_p=A^T\mathbf 1_r\text{)},
\qquad
(\mathbf e,\mathbf h,\boldsymbol\lambda)\to\alpha(\mathbf e,\mathbf h,\boldsymbol\lambda),\ \alpha>0
\quad\text{(common rescaling).}
$$

Wang et al.'s single-species, unit-multiplicity special case ([SRC-0098], Eq. 15):

$$
\hat q_i=-e_is_i^{-1}+s_i^{-1}\frac{Q+\sum_je_js_j^{-1}}{\sum_js_j^{-1}}.
$$

## Sources used

- [[wiki/sources/SRC-0098-graph-nets-partial-charge-prediction]] — origin of the electronegativity/hardness QEq trick and its closed-form solution (Eqs. 12–15), credited there to Gilson, Gilson & Potter (2003, doi `10.1021/ci034148o`, not separately ingested). [SRC-0098]
- [[wiki/sources/SRC-0072-machine-learned-molecular-mechanics-force-fields-from-large]] and [[wiki/sources/SRC-0073-supplementary-material-for-machine-learned-molecular-mechanics-force]] — Espaloma's per-atom, GNN-predicted, supervised-trained instantiation of the same functional form, confirmed by direct text match to cite SRC-0098 (reference 68) and Gilson 2003 (reference 67) together. [SRC-0072] [SRC-0073]
- [[wiki/sources/SRC-0016-fine-tuning-mm-force-fields-to-experimental-free-energies]] — reuses the same constrained-minimization form (its own Eq. "QEq constrained minimization") to fine-tune a pretrained, already-transferable espaloma charge model via low-rank perturbations, rather than fitting coefficients from a cold start. [SRC-0016]

## Wiki pages used

- [[wiki/answers/ffrefine-paper-methods-knowledge-base]] — already-recorded multiplicity-weighted QEq KKT system, analytic Jacobian, and the Fisher/optimizer treatments (Tikhonov damping, hard eigenvalue cutting) that this note's redundancy result feeds into.
- [[wiki/concepts/espaloma-machine-learned-mm-force-fields]] — Espaloma context, now cross-linked to this note.
- [[wiki/concepts/free-energy-reweighting-for-force-field-fine-tuning]] and [[wiki/concepts/awh-replay-force-field-optimization]] — the force-field-refinement setting (training charges through ensemble observables/free energies rather than direct charge supervision) in which this redundancy matters operationally.
- [[wiki/answers/training-initially-disabled-lennard-jones-parameters]] — the analogous relative-bound-at-zero failure mode for Lennard-Jones amplitude, used above for the practical electronegativity-seed caveat.

## Wiki updates made

- Created this answer note.
- Created [[wiki/sources/SRC-0098-graph-nets-partial-charge-prediction]] (new source).
- Updated [[wiki/sources/SRC-0072-machine-learned-molecular-mechanics-force-fields-from-large]]: added `cites_sources: SRC-0098`, a confirmed citation-link note, and filled in the previously-recorded charge-equilibration gap.
- Updated [[wiki/concepts/espaloma-machine-learned-mm-force-fields]]: added two Key Points on the QEq charge model and its per-type-refinement generalization, with links.
- Updated [[wiki/concepts/awh-replay-force-field-optimization]]: added a dated implementation-lesson paragraph pointing to this note.
- Updated [[wiki/answers/training-initially-disabled-lennard-jones-parameters]]: added a cross-link to this note.
- Updated `wiki/index.md` and `wiki/log.md`.

## Remaining gaps

- Gilson, Gilson & Potter (2003, doi `10.1021/ci034148o`) and Bleiziffer, Schaller & Riniker (2018, doi `10.1021/acs.jcim.7b00663`) are cited by [[wiki/sources/SRC-0098-graph-nets-partial-charge-prediction]] but are not separately ingested; the original electronegativity-equalization derivation and the DFT reference-charge dataset construction are therefore known only at the level of SRC-0098's own description.
- This note's hardness-Jacobian identity and gauge-direction derivations were produced and checked during this SecondBrain write-back using FFRefine's already-recorded QEq system; they were not re-verified against FFRefine's own Julia implementation or against finite-difference checks in the project repository during this write-back.
- The claim that hardness becomes identifiable "once multiple distinct constraint structures share the same coefficients" is stated qualitatively; it is not accompanied by a quantitative identifiability bound (e.g. how many distinct $A'$ structures, or how much cross-species variation, are needed before the Fisher block for $\mathbf h$ becomes well-conditioned rather than merely non-singular).
