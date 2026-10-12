---
type: answer
status: active
created: 2026-10-04
updated: 2026-10-11
question: "How did FFRefine's two deciding water campaigns develop past their first snapshot (2026-10-04): what happened when weighted sum's epoch-27 worker was killed by an out-of-memory condition, what does ConFIG's continuing run through checkpoint 33 show about conflict-driven exclusion, and what did six production rescue extensions reveal about weaknesses in the extend-or-exclude policy?"
answer_status: answered
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/machine-learning/scientific-modeling
  - research/scientific-computing
tags:
  - ffrefine
  - config
  - multi-objective-optimization
  - direction-gate
  - gradient-conflict
  - natural-gradient
  - replay-reweighting
  - calibration
  - resource-management
related:
  - "[[wiki/answers/ffrefine-direction-gates-and-production-policy]]"
  - "[[wiki/answers/ffrefine-current-implementation-status]]"
  - "[[wiki/tensions/TEN-0020-config-family-exclusion-versus-untreated-drift]]"
  - "[[wiki/questions/QST-0011-config-versus-weighted-sum-under-calibrated-direction-gates]]"
  - "[[wiki/questions/QST-0012-persistent-replay-prediction-optimism-for-one-family]]"
  - "[[wiki/questions/QST-0013-step-length-policy-after-family-exclusion]]"
  - "[[wiki/questions/QST-0015-rdf-density-dielectric-pareto-front-for-this-water-parameterisation]]"
  - "[[wiki/claims/CLM-0044-config-must-exclude-directionally-unreliable-families]]"
  - "[[wiki/claims/CLM-0048-family-weight-renormalisation-changes-natural-gradient-step-length]]"
  - "[[wiki/claims/CLM-0049-few-block-pseudo-value-covariance-understates-promise-null]]"
  - "[[wiki/claims/CLM-0050-retesting-a-failed-gate-after-extension-needs-alpha-spending]]"
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
  - "[[wiki/concepts/tolerance-normalized-multi-observable-losses]]"
  - "[[wiki/concepts/conflict-free-pinn-training]]"
  - "[[wiki/answers/adding-config-optimiser-to-ffrefine]]"
  - "[[wiki/answers/ffrefine-loss-gate-diagnostic-policy]]"
  - "[[wiki/answers/ffrefine-improved-gates-water-run-lessons]]"
sources:
  - SRC-0018
  - SRC-0036
sensitivity: public
encryption: none
wiki_pages_used:
  - "[[wiki/answers/ffrefine-direction-gates-and-production-policy]]"
  - "[[wiki/answers/ffrefine-current-implementation-status]]"
  - "[[wiki/tensions/TEN-0020-config-family-exclusion-versus-untreated-drift]]"
  - "[[wiki/questions/QST-0011-config-versus-weighted-sum-under-calibrated-direction-gates]]"
  - "[[wiki/questions/QST-0012-persistent-replay-prediction-optimism-for-one-family]]"
  - "[[wiki/questions/QST-0013-step-length-policy-after-family-exclusion]]"
  - "[[wiki/claims/CLM-0044-config-must-exclude-directionally-unreliable-families]]"
  - "[[wiki/claims/CLM-0048-family-weight-renormalisation-changes-natural-gradient-step-length]]"
  - "[[wiki/claims/CLM-0050-retesting-a-failed-gate-after-extension-needs-alpha-spending]]"
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
  - "[[wiki/concepts/tolerance-normalized-multi-observable-losses]]"
raw_sources_consulted: []
wiki_pages_updated:
  - "[[wiki/tensions/TEN-0020-config-family-exclusion-versus-untreated-drift]]"
  - "[[wiki/questions/QST-0011-config-versus-weighted-sum-under-calibrated-direction-gates]]"
  - "[[wiki/questions/QST-0012-persistent-replay-prediction-optimism-for-one-family]]"
  - "[[wiki/questions/QST-0013-step-length-policy-after-family-exclusion]]"
  - "[[wiki/questions/QST-0015-rdf-density-dielectric-pareto-front-for-this-water-parameterisation]]"
  - "[[wiki/claims/CLM-0044-config-must-exclude-directionally-unreliable-families]]"
  - "[[wiki/claims/CLM-0050-retesting-a-failed-gate-after-extension-needs-alpha-spending]]"
  - "[[wiki/answers/ffrefine-direction-gates-and-production-policy]]"
  - "[[wiki/answers/ffrefine-current-implementation-status]]"
  - "[[wiki/concepts/awh-replay-force-field-optimization]]"
project_evidence:
  - "FFRefine water run 20260930-132911 (weighted sum, rdf/density/dielectric, weights 1/2/10): no longer running. Its epoch-27 worker was killed by the kernel out-of-memory killer at the first replay proposal of epoch 27. Last completed checkpoint 26 (wall time 107.9 h through 26 epochs); last available aggregate fresh total-loss measurement is checkpoint 25 (1.376)"
  - "FFRefine water run 20260930-132851 (ConFIG, same families and weights): still running. Snapshot taken 2026-10-05 through checkpoint 33 (112.7 h); epoch 34 in progress"
  - "Six production rescue extensions observed across both campaigns (CF epochs 27, 29, 32; WS epochs 26, 27) plus the first snapshot's single rescue (CF 27, now superseded by this fuller account); one (WS 27) was cut short by the out-of-memory crash before its chain ran"
  - "Out-of-memory crash evidence: worker RSS versus archive frame count, node memory co-scheduling, and monitoring that reported the killed worker as exiting with code 0"
  - "Earlier context already recorded in [[wiki/answers/ffrefine-direction-gates-and-production-policy]] and [[wiki/tensions/TEN-0020-config-family-exclusion-versus-untreated-drift]]: legacy half-archive-gate run 20260924-204914 and shadow campaign 20260928-220040"
scope: snapshot
currency: current
as_of: 2026-10-05
---

# ConFIG-Versus-Weighted-Sum Water Campaign: Weighted Sum's Crash and ConFIG's Continuing Regression

## Short answer

**Status as of 2026-10-05.** Weighted sum (`20260930-132911`) is no longer running: its epoch-27 worker was killed by the Linux kernel's out-of-memory (OOM) killer at the first replay proposal of epoch 27. Its last completed checkpoint is 26 (107.9 h); its last available fresh total-loss measurement is checkpoint 25 (1.376). ConFIG (`20260930-132851`) is still running; this snapshot runs through checkpoint 33 (112.7 h), with epoch 34 in progress.

Where the first snapshot (2026-10-04, through weighted-sum epoch 23 and ConFIG epoch 27) found weighted sum ahead and ConFIG regressing after a four-epoch dielectric exclusion (with its first rescue just bought), this update changes the picture:

1. **Weighted sum plateaued, then stopped on an infrastructure failure, not a scientific one.** Through checkpoint 25 its fresh loss was still falling, but slowly (about -0.03/epoch, versus -0.08/epoch earlier) as density sat excluded for five consecutive epochs (23-27) with a noise-level own gradient, consistent with (not proof of) a constrained optimum. The run never reached a worse state before it was killed.
2. **ConFIG's exclusion pattern became a genuine, unrecovering cycle, not a sawtooth.** After its best of 1.82 at checkpoint 22, its fresh loss rose to 3.41 (checkpoint 26), dipped to 2.74 after the rescue (checkpoint 27), then seesawed up to 5.05 by checkpoint 32, driven by density and dielectric alternately being excluded and then returning to find the other family had pushed the objective uphill. **INFERENCE, explicitly a judgement call and not a measured result:** under the current policy this run is unlikely to recover; what the project had treated as an accepted sawtooth around a descending trend has become a cycle with net ascent, strengthening the case for a full-objective guard that is not limited to the currently included families.
3. **All three families now conflict pairwise under ConFIG**, not only dielectric against the other two as in the first snapshot; the whitened rdf-density cosine, previously mildly positive, turned negative (-0.31 to -0.77) over epochs 29-34.
4. **Weighted sum showed a second step-length failure mode.** With density excluded, the earlier KL-capped two-cycle (oscillating sign at the cap) vanished, but the chains began to crawl instead: every chain ran to the 21-proposal limit with a shrinking, well-calibrated but barely-progressing step. The same run has now exhibited both failure modes.
5. **Six production rescue extensions have now been exercised (one cut short by the crash), exposing generic weaknesses in the extend-or-exclude policy** beyond the statistical biases already recorded: the pass-probability model scores only the stage a family failed, not later stages it might still fail; weighted sum's rescue statistic can make a family at its own constrained optimum look rescuable; the measured production-cost fraction is inflated by slow or crawling epochs; and the policy has no memory-cost term at all. Full account in [[wiki/answers/ffrefine-direction-gates-and-production-policy]].
6. **Replay's miscalibration for an excluded family is not consistently signed.** Earlier, replay under-predicted dielectric's rise by about 2x when it was excluded; here, replay over-predicted density's rise by over 50% when density was excluded instead (predicted +2.14/+2.27, realised +1.32/+1.70).
7. **The out-of-memory crash is a reusable infrastructure lesson, not specific to this campaign.** Replay-worker memory grows roughly linearly with archive length (about 11 MB resident memory per frame here); a rescue extension lengthens the archive and therefore raises peak memory, which the current extend-or-exclude policy does not account for at all.

All of this is FFRefine project evidence; ConFIG itself comes from SRC-0036 and the replay/AWH machinery from SRC-0018. See [[wiki/answers/ffrefine-direction-gates-and-production-policy]] for the direction-gate and extend-or-exclude mechanism, which is not re-derived here, and for the fuller rescue-policy-flaw analysis.

## Detailed answer

### Setup (shared by both runs, unchanged from the first snapshot)

A rigid-geometry, QEq-charge water model with ten latent parameters (Lennard-Jones sigma/epsilon for O and H, a double-exponential repulsion alpha/beta, QEq electronegativity and hardness for H and O). Three tolerance-normalized target families ([[wiki/concepts/tolerance-normalized-multi-observable-losses]]): RDF (O-O/H-O/H-H, 456 bins), density over 14-41 degrees C, and the static dielectric constant over 15-40 degrees C, with family weights rdf 1, density 2, dielectric 10. Sampling used Times Square Sampling (TSS, 28 states spanning 14-41 degrees C) with a 50 ns frozen-bias production archive per checkpoint (about 10,001 frames) and no cross-epoch pooling ([[wiki/concepts/awh-replay-force-field-optimization]]). MBAR-replay optimisation used damped natural-gradient steps (learning rate 1) KL-capped at 0.1, with a chain stopping at an archive-support boundary or after 21 proposals, momentum 0, and loss gates diagnostic rather than blocking ([[wiki/answers/ffrefine-loss-gate-diagnostic-policy]]); step family weights were renormalised over the included families at every proposal ([[wiki/claims/CLM-0048-family-weight-renormalisation-changes-natural-gradient-step-length]]). Per-checkpoint direction gates used $B=8$ time-ordered jackknife blocks, $\alpha=0.05$, and the cross-fitted promise test described in [[wiki/answers/ffrefine-direction-gates-and-production-policy]], paired with its extend-or-exclude production policy. The two runs are identical except for the aggregation.

### Weighted sum: plateau, lockout, and an infrastructure death (measured)

Fresh total loss at checkpoints 22-25: 1.484, 1.465, 1.385, 1.376. Paired consecutive-checkpoint significance tests for the transitions ending at 23, 24, 25 were -0.019, -0.080, -0.009, all "inconclusive"; the run was plateauing at roughly -0.03/epoch, markedly slower than the -0.08/epoch average reported for the earlier, steeper epochs in the first snapshot.

Density was excluded `:degrades_total` in five consecutive epochs (23-27), holding about 54% of the loss throughout. Its own size statistic stayed at noise level (z 1.2-1.9) and its own per-family fresh loss stayed flat at 0.71-0.75, consistent with a genuine constrained optimum rather than a conflict-suppressed signal; its thermal-slope residual has been stuck at about -22 g/L over the 27 degree C range since about checkpoint 10. A persistent-exclusion warning fired for density at epoch 26, suggesting about 272 ns of production (5.4x the 50 ns used) — a prescription that, unlike the earlier dielectric case, is plausibly appropriate here, because density's exclusion looks noise/optimum-driven rather than conflict-driven (see [[wiki/tensions/TEN-0020-config-family-exclusion-versus-untreated-drift]] for the contrast).

With density excluded, the two-cycle oscillation recorded in the first snapshot vanished: the step-to-step cosine returned to +1.0 and the path/displacement ratio to 1.0. But the chains began to **crawl** instead: every chain used its full 21-proposal budget, with median step KL falling from about 0.0020 to 0.0008 across these epochs and a predicted gain of only 0.03-0.06 per chain. Epochs still took about 285 minutes, because FFRefine's per-epoch replay cost is dominated by the number of proposals attempted, not by how far they collectively move. **This single run has now shown two distinct step-length failure modes**: a bounded two-cycle at the KL cap while the stiff density family is included, and a crawl of many tiny, individually well-calibrated but barely-progressing proposals once it is excluded. See [[wiki/questions/QST-0013-step-length-policy-after-family-exclusion]].

Physical state at checkpoint 26 (the run's last completed checkpoint): density mean -0.3 g/L (essentially matched), thermal-slope residual -22.0 g/L (unresolved, as above); dielectric residual +2.2...+0.4 across 15-40 degrees C (converged); rdf RMS O-O/H-O/H-H 0.130/0.073/0.086.

**The crash.** At epoch 27, density's exclusion was rescued (see the rescue section below); the post-rescue gate passed. The worker that would have run epoch 27's replay chain was then killed by the kernel's OOM killer at its first replay proposal. No chain-level outcome exists for epoch 27: do not read any result beyond "the gate passed" for that epoch. Full account of the crash itself is below.

### ConFIG: all three families now conflict pairwise, with net ascent (measured, with one explicit inference)

Fresh total loss at checkpoints 27-32: 2.74, 4.01, 3.12, 3.90, 4.99, 5.05 (the run's best remains 1.82, at checkpoint 22). Checkpoint 33's aggregate fresh total loss was not available to this write-back; only its physical breakdown is reported below. Paired consecutive-checkpoint significance tests for the transitions 26->27 through 31->32: -0.68 (a statistically confident decrease), +1.27 (a statistically confident **increase**), -0.88 (confident decrease), +0.78 (confident increase), +1.10 (confident increase), +0.06 (inconclusive). All of these are report-only: FFRefine's loss gates are diagnostic, not blocking, by default ([[wiki/answers/ffrefine-loss-gate-diagnostic-policy]]), so three statistically confident rises in six epochs did not stop or alter the campaign.

Per-family fresh losses at checkpoints 27-32 — density: 0.34, 1.66, 0.54, 0.29, 1.98, 0.71; dielectric: 2.09, 2.05, 2.30, 3.33, 2.74, 4.08. RDF continued to improve over the same window (0.308 to 0.265). Density and dielectric are **seesawing with a net ascent**: density was excluded as `:uncertain` at epochs 28 and 31 (size z 1.4 and 0.46, both sitting near its own optimum). Chain 28 (density excluded) predicted density +2.14, dielectric -0.53, full objective +1.60 (realised density +1.32); chain 31 predicted density +2.27, dielectric -0.87, full objective +1.39 (realised density +1.70). **Both chains ran despite replay's own prediction of a full-objective rise of about 1.4-1.6**, because the loss gates are diagnostic and score only the included families — the same structural gap already identified in the first snapshot's regression mechanism, now repeating with larger, more confident numbers. Density then returned each time with a very easy promise test (t 37-41, reflecting how far it had been pushed from its optimum), while dielectric's angle to the three-family ConFIG step widened to 81-88 degrees and its own cross-fitted promise went negative at several points (t -3.04 at epoch 29, -0.19 at 30, 0.48 at 32, 0.89 at 33, -1.04 at 34). Dielectric was itself excluded at epochs 29, 30, 32 and 33, and the dielectric-excluded chains raised dielectric by +1.03 (chain 30) and +1.34 (chain 32).

**All three families now conflict pairwise**, not only dielectric against the other two as in the first snapshot. Whitened gradient cosines: rdf-density moved from +0.05 to +0.17 earlier in the run to -0.31 to -0.77 over epochs 29-34 (new); rdf-dielectric -0.18 to -0.77 (as before); density-dielectric -0.17 to -0.54 (as before, unchanged from the first snapshot).

Physical state at checkpoint 33: density mean -5.3 g/L, with transient spikes to -9 to -10 g/L at checkpoints 29 and 32; thermal-slope residual -12.1 g/L (still better than the start and than weighted sum's locked-in -22.0, and still improving); dielectric residual +41.9...+33.0 across 15-40 degrees C, back to roughly its checkpoint-5 level; rdf RMS O-O/H-O/H-H 0.081/0.047/0.057, still the best of the three metrics and still slowly improving.

**INFERENCE, explicitly the parent agent's own judgement, not a measured result or an established claim:** under the current policy, this ConFIG run is unlikely to recover. [[wiki/tensions/TEN-0020-config-family-exclusion-versus-untreated-drift]]'s earlier framing — exclusion as an accepted, bounded sawtooth around a descending trend — no longer matches what is happening once every family conflicts with every other: exclusion has become a cycle with net ascent across the whole objective. This strengthens, but does not by itself prove, the case for a full-objective guard that is not limited to the currently included families (one of the candidate remedies already recorded in the first snapshot and in [[wiki/tensions/TEN-0020-config-family-exclusion-versus-untreated-drift]]).

### Rescue policy, now exercised six times (measured)

The extend-or-exclude policy bought six rescue extensions across both campaigns, one more than the single first-snapshot data point:

| Run, epoch | Family | Failed stage | Statistic (pre-rescue) | $\kappa^*$ | $P(\kappa^*)$ | EV | Post-rescue statistic: predicted vs realised | Outcome |
|---|---|---|---|---|---|---|---|---|
| CF 27 | dielectric | promise | $t=2.18$ vs $m_0=2.26$ | 1.44 | 0.57 | positive | $t$: 2.62 predicted, 2.67 realised | passed, included (chain ran; this is the first snapshot's rescue) |
| CF 29 | dielectric | size (`uncertain`) | $z=1.26$ vs 1.84 | 1.17 | — | +0.002 | size $z$: 1.69 predicted, 1.97 realised (size passed) | size passed, then **failed promise** ($t=-3.04$); wasted |
| CF 32 | dielectric | size (`uncertain`) | $z=1.52$ | 1.11 | — | 0.13 | size $z$: 1.89 predicted, 2.67 realised (size passed) | size passed, then **failed promise** ($t=0.48$); wasted |
| WS 26 | density | total-$t$-with-family-restored | $t=2.19$ vs $m_0=2.64$ | 1.62 | 0.57 | 0.079 | $t$: 2.79 predicted, 1.40 realised | **failed**; epoch took 444 min against about 285 |
| WS 27 | density | total-$t$-with-family-restored | $z=2.46$ | 1.73 | 0.78 | 0.25 | gate: 2.73 threshold vs 2.84 realised | gate **passed**, then the worker was killed (OOM); no chain-level outcome |

(WS 26 and WS 27 also report the family's full-objective loss share, $c_\mathrm{ex}=0.54$, and measured cost fractions $\rho=0.275$ and $\rho=0.18$ respectively, both well below ConFIG's measured $\rho\approx0.48$; see the flaw analysis below.)

Of the five rescues with a resolved outcome: one led to a chain that actually ran and included the family (CF 27); three were wasted — the extension was bought and the targeted statistic passed, but the family then failed a later stage or the predicted benefit did not materialise (CF 29, CF 32, WS 26); and one (WS 27) was cut short by the out-of-memory crash immediately after its gate passed, so no chain-level outcome exists for it.

**Prediction accuracy.** Across the resolved rescues, the conditional prediction model showed the directional biases already recorded in [[wiki/claims/CLM-0050-retesting-a-failed-gate-after-extension-needs-alpha-spending]] plus one new one: size predictions still undershot (CF 29: 1.69 predicted vs 1.97 realised; CF 32: 1.89 vs 2.67), consistent with a just-failed statistic being biased low; the one promise-based prediction was accurate (CF 27: 2.62 vs 2.67); and weighted sum's total-based prediction **overshot badly** (WS 26: 2.79 predicted vs only 1.40 realised) — a failure mode this statistic had not previously been exercised against in a deciding campaign.

**Generic flaws exposed (reasoned from this evidence; analysis, untested, not yet adopted):**

- **(a)** The pass-probability model only scores the stage a family actually failed, not stages that come after it. Under ConFIG, a size-filter rescue can pass the size test and then fail the later promise test because of a genuine inter-family conflict (CF 29, CF 32): the rescue "succeeds" by its own statistic and still contributes nothing.
- **(b)** Under weighted sum, the rescue statistic is the total's $t$ with the family restored, not the family's own debiased size statistic. The policy's intended protection against rescuing a family that is simply sitting at its own constrained optimum relies on that family's own size statistic (a family with $z\le0$ or negligible is never rescuable) — a protection that never engages under weighted sum's total-based statistic. A family at a genuine optimum with a large loss share (density, 54% here) can therefore look rescuable (WS 26, WS 27) even though, physically, there is nothing to rescue.
- **(c)** The measured production-cost fraction $\rho$ is relative to the *epoch's own* wall time, so a slow or crawling epoch inflates the denominator and makes further extensions look artificially cheap: weighted sum's measured $\rho$ fell to 0.18-0.28 during the crawl regime, against about 0.48 for ConFIG's faster epochs in the same window.
- **(d)** The rescue model has no memory-cost term at all. See the out-of-memory account below.

This flaw analysis is recorded in full, alongside the policy's other implementation lessons, in [[wiki/answers/ffrefine-direction-gates-and-production-policy]]; it is not duplicated at length here.

### The out-of-memory crash (measured, reusable implementation lesson)

A FFRefine replay worker's resident memory grows roughly linearly with the number of archive frames it holds: about 11 MB of resident memory per frame in this setup, of which about 6 MB was live garbage-collector (GC) heap — resident memory ran about 3x the live heap, suggesting (not established) that the GC let a large amount of garbage accumulate before reclaiming it, or that much of the resident memory sits outside the GC heap. A normal 10,001-frame (50 ns) epoch peaked at 205-260 GB resident memory. Rescue extensions added 40-70 GB more: a 14,440-frame archive (CF epoch 27's rescue) peaked at about 290 GB; a 16,211-frame archive (WS epoch 26's rescue) peaked at about 311 GB.

The WS epoch-27 worker, extended to 17,282 frames by a 36 ns rescue, was killed by the kernel at about 307 GB of anonymous resident memory at its very first replay proposal, while the other campaign's worker held about 210 GB on the same node at the same time. The two campaigns' *ordinary* peaks already summed to roughly the node's total memory; they had survived up to that point only because their peaks had not previously coincided — the rescue extension was what pushed the combined total over the edge.

The run's own monitoring had reported the killed worker as having "exited with code 0". A kernel signal kill leaves the Julia process's exit code at 0 with `success() == false`; the terminating signal is recorded separately (`termsignal`), but the monitoring message printed only the exit code, so from the monitoring log alone this looked like a clean, intentional exit rather than a crash.

**Generic lesson for FFRefine (not literature-derived, stated independently of this specific campaign):** the extend-or-exclude production policy currently has no memory term at all (flaw (d) above), even though a rescue's whole purpose is to lengthen the archive, which is exactly what raises peak memory. Candidate remedies, untested: cap the rescue multiplier $\kappa$ by predicted frame count times measured bytes-per-frame against an explicit memory budget; bound the worker's heap (for example, a garbage-collector heap-size hint) so a runaway worker fails predictably instead of growing without limit; avoid co-scheduling campaigns whose ordinary peak memory can coincide on one node; and report a worker's terminating signal, not only its exit code, since an OOM kill is otherwise indistinguishable from a clean exit in monitoring output. What specifically accounts for the roughly 6 MB of live heap per frame has not been profiled; this is recorded as an open question, not a resolved cause. A short, cross-referenced version of this lesson is also recorded in [[wiki/answers/ffrefine-current-implementation-status]] as a general implementation note, independent of this specific campaign.

### Replay calibration (measured, including a sign flip)

RDF's replay predictions remain persistently optimistic by about 5% in both runs, with cumulative calibration $z$ continuing to grow (now 6.1 for ConFIG, 4.7 for weighted sum, up from 5.9/4.5 at the first snapshot) — significant mainly because rdf's own standard error is tiny, not because the absolute bias is large.

In ConFIG, when density was excluded (chains 28 and 31), replay **over-predicted** density's rise (predicted +2.14 and +2.27; realised +1.32 and +1.70). This is the opposite sign from density's own earlier persistent optimism (where replay under-predicted density's improvement; see [[wiki/questions/QST-0012-persistent-replay-prediction-optimism-for-one-family]]) and from the earlier roughly 2x under-prediction of dielectric's rise in the first snapshot's chains 23-26. So the direction of replay's miscalibration for a currently excluded family is not stable across episodes or even across families within the same run: sometimes optimistic, sometimes pessimistic. This weakens any simple one-directional correction (for example, "always discount an excluded family's predicted rise") as a fix for the regression-mechanism gap described above.

### Gate health (measured)

Across roughly 60 completed epochs total (26 weighted sum, 33-34 ConFIG), no promise-drift blocks occurred, and the equilibration cut and survival-ratio statistics described in the first snapshot remain in their earlier ranges. The combined gates and extend-or-exclude policy have now bought six rescue extensions (five resolved, one cut short by the crash) across these epochs, up from the single rescue recorded at the first snapshot — still a large reduction from the 13 extensions in 22 epochs the legacy half-archive gate spent (`20260924-204914`; see [[wiki/answers/ffrefine-improved-gates-water-run-lessons]]), but enough rescues now to show the generic policy flaws above rather than only their statistical biases.

## Practical lessons

- **Weighted sum's remaining failure mode is wall time, not direction.** Once the stiff, conflicting family is excluded for a genuine (noise-level) reason, the KL-capped step stops oscillating but starts crawling: every proposal is well calibrated but tiny, so wall time is spent without proportional progress.
- **ConFIG's exclusion pattern can turn from a bounded sawtooth into a net-ascending cycle once every family conflicts with every other.** This is a qualitatively different regime from the single-family, intermittent exclusion recorded earlier, and the project's "do not guard against cycling" decision — already contradicted once by a four-epoch single-family exclusion — is strained further by a multi-family cycle with no sign of returning to its earlier (better) state. (Explicitly flagged as the parent's inference, not a measured fact.)
- **A statistically confident per-epoch regression is not itself a defence if the gate scoring it is diagnostic, not blocking.** Three of ConFIG's six checkpoint-to-checkpoint transitions in this window were confident rises, not merely "inconclusive" slow drift, and none of them stopped or altered the campaign.
- **A rescue's pass-probability model should score every downstream stage a family must still clear, not only the stage it currently failed**, and a weighted-sum rescue statistic built from the total should not be treated as evidence that the individual family itself needs more data, since it bypasses the policy's own "already at its optimum" protection.
- **A production-cost fraction measured relative to the current epoch's own wall time is not a stable unit once that wall time itself becomes pathological** (crawling or oscillating); it can make further extensions look cheaper than they are in absolute terms.
- **A sampling-archive extension policy that does not budget memory can crash a worker outright**, and a signal-killed worker can be indistinguishable from a clean exit in ordinary monitoring output unless the terminating signal itself is surfaced.
- **Replay's prediction bias for an excluded family can flip sign across episodes and across families**, so no single-direction correction (always discount, always inflate) is likely to fix the underlying regression-detection gap on its own.

## Key equations

No new equations; the direction-gate and extend-or-exclude mathematics used by both campaigns are given in [[wiki/answers/ffrefine-direction-gates-and-production-policy]] and are not repeated here. The memory-growth relationship above (resident memory roughly linear in archive frame count) is reported as an approximate empirical rate, not a derived formula.

## Sources used

- SRC-0036 for ConFIG itself; SRC-0018 for the AWH/replay/frozen-bias machinery underlying the sampling and optimisation loop. Every numeric result in this note is FFRefine project evidence from the two named campaigns, listed in this page's frontmatter.

## Wiki pages used

- [[wiki/answers/ffrefine-direction-gates-and-production-policy]]
- [[wiki/answers/ffrefine-current-implementation-status]]
- [[wiki/tensions/TEN-0020-config-family-exclusion-versus-untreated-drift]]
- [[wiki/questions/QST-0011-config-versus-weighted-sum-under-calibrated-direction-gates]]
- [[wiki/questions/QST-0012-persistent-replay-prediction-optimism-for-one-family]]
- [[wiki/questions/QST-0013-step-length-policy-after-family-exclusion]]
- [[wiki/claims/CLM-0044-config-must-exclude-directionally-unreliable-families]]
- [[wiki/claims/CLM-0048-family-weight-renormalisation-changes-natural-gradient-step-length]]
- [[wiki/claims/CLM-0050-retesting-a-failed-gate-after-extension-needs-alpha-spending]]
- [[wiki/concepts/awh-replay-force-field-optimization]]
- [[wiki/concepts/tolerance-normalized-multi-observable-losses]]

## Wiki updates made

- Rewrote this answer note with the weighted-sum crash, ConFIG's continuation through checkpoint 33, six rescue extensions, and the out-of-memory lesson.
- Updated [[wiki/tensions/TEN-0020-config-family-exclusion-versus-untreated-drift]] with the net-ascent, all-pairwise-conflict evidence (inference flagged) and refreshed its resolution status.
- Updated [[wiki/questions/QST-0011-config-versus-weighted-sum-under-calibrated-direction-gates]] with the crash/continuation status.
- Updated [[wiki/questions/QST-0012-persistent-replay-prediction-optimism-for-one-family]] with the calibration sign-flip evidence.
- Updated [[wiki/questions/QST-0013-step-length-policy-after-family-exclusion]] with the crawl-regime evidence (both step-length failure modes now observed in one run).
- Updated [[wiki/questions/QST-0015-rdf-density-dielectric-pareto-front-for-this-water-parameterisation]] with the all-pairwise-conflict evidence.
- Updated [[wiki/claims/CLM-0044-config-must-exclude-directionally-unreliable-families]] with the multi-family conflict evidence.
- Updated [[wiki/answers/ffrefine-direction-gates-and-production-policy]] with the six-rescue evidence and the generic rescue-policy flaws (a)-(d).
- Updated [[wiki/answers/ffrefine-current-implementation-status]] with a generic, cross-referenced out-of-memory implementation note.
- Added a cross-reference in [[wiki/claims/CLM-0050-retesting-a-failed-gate-after-extension-needs-alpha-spending]] noting that production rescues are now observed.

## Remaining gaps

- **Weighted sum's run ended on an infrastructure failure, not a scientific terminus.** Its last measured state (checkpoint 25/26) was still slowly improving; whether it would have continued to improve, plateaued, or eventually hit its own pathology cannot be known from this run.
- **ConFIG is still running (epoch 34 in progress).** The "unlikely to recover" judgement above is this write-back's own inference from the trend so far, not a measured terminal state; a future update could show recovery, a `:noise_floor` stop, or continued regression.
- Single seed per aggregation; see the first snapshot's note on run-to-run noise at identical initial parameters.
- The rdf/density-thermal-expansion/dielectric trade-off remains inference, not established; the new all-pairwise-conflict evidence strengthens but does not prove it. See [[wiki/questions/QST-0015-rdf-density-dielectric-pareto-front-for-this-water-parameterisation]].
- All candidate remedies (full-objective guard, conflict-aware removal, memory-budgeted rescues, GC heap bounds, signal reporting) are untested design options, not implemented or evaluated.
- What specifically accounts for the measured ~6 MB of live GC heap per archive frame has not been profiled.
- Whether co-scheduling campaigns with a shared memory budget is a general FFRefine operational constraint, or specific to this pair of runs sharing one node, is not established from a single coincidence.
