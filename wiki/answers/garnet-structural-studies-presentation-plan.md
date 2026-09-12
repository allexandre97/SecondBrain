---
type: answer
status: active
created: 2026-09-07
updated: 2026-09-11
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
tags:
  - presentation
related:
  - "[[wiki/sources/SRC-0003-training-a-force-field-from-scratch]]"
sources:
  - SRC-0003
sensitivity: internal
encryption: none
---

# Garnet Structural Studies presentation preparation

## Animation backgrounds unified — 11 September 2026

All nine Blender animations in `/ssd/Blender/Garnet_Presentation` now render against `#F7F5F2` from the project's `background_color.txt`. The update includes all camera-bearing scenes and improved contrast for standalone text, mesh equations and plot curves. White lettering inside dark parameter panels is retained. Molecular lighting and animation curves are preserved; force-field/message-passing schematic scenes use Standard display conversion, matching discrete typing, to keep antialiased text readable. Other molecular scenes retain AgX.

Original files and per-file reports are in `Documents/Garnet_Presentation/assets/background_update/`, alongside revised copies, scripts and representative renders. Comparisons verified frame ranges and object/data animation curves for every scene/object in all nine files. Background samples round to RGB (247,245,242). Existing movies were not rerendered. Original MolecularNodes sidecars remain unchanged; the installed plugin reports pre-existing unpickle errors for three static-scene sidecars, although their saved geometry renders. No scientific claims or source records were changed.

## Preparation artifact

The user requested a route plan for preparing the Structural Studies colloquium PowerPoint and talk. The working document is `Documents/Garnet_Presentation/route_plan.md` (relative to the user home directory). The current abstract is `title_and_abstract.md` in the same project directory.

The plan records confirmed talk constraints and covers building the narrative, selecting and checking figures, drafting slides and speaker notes, transferring them into online PowerPoint, rehearsing, preparing questions, and adapting a separate later LMB talk. The Structural Studies colloquium is on **17 September 2026**, with **20 minutes speaking plus questions**. There is no slide limit or required template; slides use **16:9** for a large projector. The current title and abstract are final. Backbone v1 now contains 15 core slide records budgeted at 19 minutes, with one minute of delivery margin, and three backup records. PowerPoint construction and timed rehearsal remain outstanding. The later LMB internal symposium's exact date and speaking allowance remain unconfirmed.

## Scientific basis

The planned narrative introduces simulation and force fields before learned parameter assignment and training. Representative evidence will cover small molecules, folded proteins, intrinsically disordered proteins and relative binding free energies. Source locators are Figure 1A, Figure 2 and Table 1, Figure 3, Figure 4B–C, and Figure 6 of the revised manuscript. The framing emphasises automated development while preserving validation limitations. [SRC-0003, Results and Discussion]

Keep the colloquium focused on Garnet, with no main-talk time allocated to FFRefine. Reserve FFRefine for possible inclusion as a preliminary extension in the later LMB internal symposium, subject to its speaking allowance and verified source material. FFRefine is not the main focus; this plan makes no new FFRefine result claims.

## Editorial direction confirmed on 7 September 2026

The user requested a visually pleasing presentation, a brief discussion of alternative models, an audience-specific explanation of J-couplings, and consistent citation of other studies. These directions are reflected in the local route_plan.md, general_directions.md and AGENTS.md; the final title and abstract remain unchanged.

- Plan an editable Morph sequence from manual atom assignment/tuning to learned chemical environments and automatic parameter assignment. Preserve visual continuity and readable static slides for PDF export; test transition support in the actual PowerPoint setup. Use shapes or placeholders, never generative AI figures.
- Explicitly position Garnet as a classical molecular mechanics force field with learned parameters. The local route plan now includes a short, sourced comparison of machine learning interatomic potentials, coarse-graining and polarisability, with benefits and limitations and no universal ranking. Keep this within the 20-minute talk; retain detail in backup. Garnet's interaction terms and parameter assignment are described in SRC-0003, Figure 1A and Methods “Potential functional forms”. [SRC-0003]
- Prefer Figure 3C for explaining torsion-dependent three-bond J-couplings through a Karplus relationship and averaging the predicted couplings over simulation frames. Skip a general NMR introduction. Figure 3B instead concerns hydrogen-bond-mediated couplings. Preserve GB3's training status, the error metric and forward-model caveats in notes. [SRC-0003, Figure 3 and Methods “Protein benchmark”]
- Place original-study citations on slides supporting external claims or adapting others' visuals; keep full references and claim-specific source locations in notes. Resolve unchecked citations before presentation. Initial comparison references are linked in route_plan.md: Kovács et al. (2025), MACE-OFF, DOI 10.1021/jacs.4c07099; Souza et al. (2021), Martini 3, DOI 10.1038/s41592-021-01098-3; Shi et al. (2013), AMOEBA, DOI 10.1021/ct4003702. These were consulted for presentation planning, without ingesting new wiki sources.

## Backbone v1 and assets

The user authorised the next drafting step on 7 September 2026. Working originals are under `Documents/Garnet_Presentation/` relative to the user home directory:

- `structural_studies_slide_draft.md`: master narrative, 15-slide timing table, shared visual direction, three-state Morph storyboard and online PowerPoint transfer instructions.
- `slides/structural_studies/S01.md` through `S15.md`: one editable record per core slide, each with on-slide content, visual specification, speaker notes, transition, animation and full references. Total planned speaking time is 1,140 seconds; these are estimates, not rehearsal measurements.
- `slides/structural_studies/B01.md` through `B03.md`: backup records for from-scratch/model choices, complete protein couplings and full binding metrics.
- `figure_manifest.md`: manuscript page/panel identifiers, source version/hash, caption summaries, axes, uncertainty, crop coordinates and scientific boundaries.
- `presentation_references.md`: reference ledger; full references also appear in individual slide records.
- `assets/originals/`: five supplied figure PDFs preserved as original copies. `assets/selected/`: four main-slide crops and two full backup figures rendered directly from the PDFs. No scientific data were redrawn or generated.

The selected results are Figure 2A’s Structure subplot (small-molecule geometry), Figure 3C’s BPTI subplot (couplings beyond the GB3 training system), Figure 4B (IDP dimensions), and the complete Figure 6A (all eight binding targets and weighted error). Full Figure 3C and Figure 6 are retained for questions. Figure 1A supplies the checked reference for the editable method sequence. Original figure PDFs were visually compared against manuscript pages 4, 6, 9, 10 and 13, and the four output crops were inspected. [SRC-0003, Figures 1–4 and 6]

The BPTI crop requires restoration of the original coupling-category legend in PowerPoint. Notes preserve the 99.9% confidence intervals for the coupling comparison, IDP limitations, training/test distinctions and differences between binding protocols. These are backbone records and insertion assets; there is no completed PowerPoint deck yet. [SRC-0003, Figures 3–4 and 6 and associated Methods]

One source ambiguity was raised with the user: the prose and Figure 6 caption disagree on whether exactly 16 ligands meets the ranking-metric eligibility rule. The backup avoids asserting that boundary; the main RMSE panel is unaffected. Numerical Karplus-curve construction is deferred until a coupling-specific calibration is chosen; the current explanation is a schematic mapping. [SRC-0003, relative binding free energy Results and Figure 6 caption; Methods “Protein benchmark”]

## Reviewed edits and PowerPoint handoff

On 7 September 2026 the user asked for review of their edits and exact instructions for the ChatGPT add-in. The reviewed local records retain an off-white background, section progress guide, full Garnet author citation, direct speaking transitions, parameter-knob analogy and requested molecular imagery. The core estimate remains 19 minutes plus one minute of margin.

The review qualified the suggestion that an MLIP is automatically more accurate and that improvement only requires better data/training: results remain benchmark-specific and the interaction model can also limit accuracy. Optional discussion of alternative samplers was kept out of the one-minute core opening. [SRC-0003, small-molecule validation and Discussion]

`Documents/Garnet_Presentation/powerpoint_handoff/README.md` now gives the exact build prompt and transfer steps. `powerpoint_handoff/upload/` contains `01_build_brief.txt` (all 18 records, design, notes, sources and manifest) and nine PNG images. `powerpoint_handoff.zip` is a convenience archive to extract before supplying the individual files. It does not include environment files or the full source repository. This package is a snapshot to refresh after further slide edits.

Two existing molecular overlays from Figure 2C were inspected and added for S09, with explicit quantum-reference/Garnet colour labels and selected-example status. The supplied method figure was rendered for portable reference. Requested protein/IDP/protein–ligand videos remain named placeholders because no verified trajectories were supplied. [SRC-0003, Figures 1 and 2C]

The handoff asks the add-in to build all 15 core slides and three backups, keep native text and shapes editable, insert supplied plots intact, retain citations and notes, and report unsupported operations. Attachment, speaker-note and Morph capabilities are treated conditionally for the actual installation; official workflow reference: https://learn.chatgpt.com/use-cases/generate-slide-decks. No PowerPoint deck has been built or uploaded by this agent.

## Provenance and status

Planning decisions derive from the user's request, constraints confirmed on 7 September 2026 (ten days before the colloquium), and the presentation project's general_directions.md and title_and_abstract.md. The constraints are reflected in general_directions.md, route_plan.md and AGENTS.md; the final title_and_abstract.md remains unchanged. Scientific figure locators were checked against the revised 44-page SRC-0003 manuscript. The first slide backbone and figure selection/extraction are prepared. PowerPoint construction, conceptual schematic building, animation checks and timed rehearsal remain future work. No durable scientific claims or raw sources were changed.

## First deck review — 8 September 2026

The user supplied `ss_coloquia.pptx`, `report_summary.md.txt`, molecular movies and frame directories in the presentation workspace. Inspection of slide XML, all notes and LibreOffice renders found 18 slides in 16:9, nine embedded PNGs, and no embedded movies or standard animation/transition elements. The narrative and scientific caveats are largely preserved. Typography and scientific figure labels need projector checks; the molecular-interaction, message-passing, training-loop and J-coupling schematics require further construction. These are observations about the supplied draft, not new scientific results.

The durable local review is `Documents/Garnet_Presentation/deck_review.md`; `media_storyboard.md` records the asset inventory and a rotation → still → topology-derived graph → learned descriptions → parameters sequence. The candidate still is `Frames/Caffeine/0300.png`, with adjacency from `structures/caffeine.pdb`. The user referred to aspirin, but the supplied movie/frames/structure identify caffeine; the user subsequently confirmed caffeine (8 September 2026). The user subsequently confirmed both BPTI and α-synuclein movies as Garnet molecular dynamics, each representing 600 trajectory frames spanning 300 ns. Their exact identity with plotted benchmark runs is not established or required for illustrative use. Camera rotation must not be presented as simulated internal motion. The original deck is unchanged; media integration, diagram revision, actual PowerPoint playback checks and timed rehearsal remain outstanding.

This update supersedes earlier statements that no deck or molecular media had been supplied. The initial add-in handoff remains a historical snapshot. The review and storyboard are reflected here without copying bulky media into the wiki or adding new source ingestions.

## Revision bundle and confirmed media

On 8 September 2026 the user confirmed caffeine and the protein-movie provenance above and requested a second handoff. `Documents/Garnet_Presentation/powerpoint_revision_handoff.zip` contains a self-contained revision brief, historical content/citation reference, the unchanged first deck, nine scientific images, three movies, three static fallbacks and two molecular structure files. Its README and prompt direct the presentation session to revise the existing deck, repair explanatory diagrams/readability, integrate media and report unsupported operations. Local slide records, route plan, backbone, figure manifest and project brief reflect these confirmations. `deck_review.md` and `media_storyboard.md` are updated. The bundle has 20 upload files and passed ZIP integrity validation. No new scientific results or raw sources were added.

## Molecular stills and J-coupling illustration refinement

On 8 September 2026 the user deferred replacing stills with videos and requested real molecular representations on S03/S05/S06. They supplied `assets/jcoupling_60fps.mp4`, `Frames/JCoupling/` (300 PNGs) and an alanine-dipeptide PDB. The local `molecular_visual_revision.md` records the review and annotation specification: alanine dipeptide for force-field terms and the coupling example; caffeine with topology-derived overlays for environments, graph neighbourhoods and schematic learned descriptions. Four J-coupling frames were inspected; 0100 is a provisional still candidate, while 0200 has clipping/occlusion. The exact highlighted quartet awaits operator confirmation. Treat the user-described torsion sweep as illustrative, not an equilibrium MD ensemble to average.

The supplied deck is byte-identical to the deck in the second handoff; its previous visual review remains applicable. The received report still includes obsolete requests for supplied protein media. Local slide records, backbone, brief, route plan, figure manifest, media storyboard and review now link the refinement. The deck and report remain unchanged. The existing second-handoff ZIP is a historical snapshot and does not contain this new asset or the instruction to defer video insertion. These are project-review observations, with no new paper-result claims or raw-source ingestion.

## Corrected supplied deck/report

The user subsequently corrected the report to `report_summary.txt.txt` and supplied a new approximately 4.3 MB `ss_coloquia.pptx`. The prior unchanged-deck finding applied to the earlier file, not this revision. The new deck has 18 slides and 12 PNGs, including actual caffeine and protein stills, neighbourhood diagrams and schematic embeddings. Targeted XML/text inspection and new LibreOffice renders confirm these improvements. The latest correction in local `deck_review.md` and `molecular_visual_revision.md` records remaining issues: molecule/graph correspondence and local-subgraph labelling; S07 prediction/reference comparisons and feedback connections; S10 Karplus-before-predicted-J ordering; S12 poster/caption overlap; and the still text-only binding schematic. Video insertion remains deferred. Current received files are preserved; presentation-environment rendering is untested.

## Blender animation handoff — 9 September 2026

The user requested a prompt for a separate Codex agent to prepare a caffeine → graph → assigned-parameters animation through Blender MCP. Local `Documents/Garnet_Presentation/blender_caffeine_animation_prompt.md` contains the complete scene-building handoff. The selected oxygen is O8, with C7 one bond away and C6/N9 two bonds away, checked against the supplied caffeine PDB. The prompt uses symbolic vector packets and two message-passing rounds, then separates atom and multi-atom parameter assignment. The manuscript confirms two GraphSAGE layers, conformation-independent inputs, and molecule-wide charge constraints; the animation must not imply raw second-shell information crosses two bonds in one layer or that all final parameters are purely local. [SRC-0003, Methods “Neural network architecture”, Figure 1A]

The handoff requests a roughly 24-second 1080p/60 fps editable scene, preview frames, a lightweight preview and rendering instructions. Full-quality rendering is deferred. Local media/storyboard notes now reflect O8 as the animation focus, superseding the prior C7 example for this asset. No Blender scene was modified during prompt preparation.

## Editable Blender animation delivered — 9 September 2026

Final timing check: current master `caffeine_message_passing_v11.blend` is 31 seconds (1860 frames at 60 fps). Endpoint-copy motion now starts at 1399, after the bond pulses settle at 1397; subsequent bonded beats shift by 60 frames. The message-passing rounds and two-second final hold are unchanged. Updated representative stills and 372-frame lightweight preview; v10 preserved. This avoids competing attention cues without changing the scientific sequence.

Bond-attention revision: current master `caffeine_message_passing_v10.blend` adds a thicker saturated cyan-to-amber highlight on the C7–O8 bond and two synchronised pulses of the stroke and endpoint rings (peaks 1349/1381, settled 1397). Gradient endpoints match the ring colours; intermediate hues are selection styling, not model contributions. Peak/rest rendered stills were inspected. The editable script and lightweight preview are updated; v9 remains preserved.

Projector-colour revision: current master `caffeine_message_passing_v9.blend` uses more saturated dedicated emission materials for the four embedding-origin colours, with brightness adjusted to retain visibility against black. The consistent per-atom colour mapping, 30-second duration and molecular element colours are retained. Rendered stills and preview were refreshed; actual projector playback remains untested. Earlier v8 is preserved.

Embedding-colour revision: current master `caffeine_message_passing_v8.blend` consistently tracks selected individual atoms: O8 amber, C7 cyan, C6 violet, N9 burgundy. Initial messages retain sender colours; O8's first update combines amber/cyan, while C7's update and O8's second update contain all four origins. Copies into bond mixing preserve their source palettes, and the bond embedding retains the same origin accents. Spheres keep element colours; other glyphs remain muted grey. These colours are schematic context provenance, not actual vector components or weights. Updated stage renders and sender/copy material matches were checked; the 30-second preview was refreshed, preserving v7.

Arrow revision: current master `caffeine_message_passing_v7.blend` adds a downward amber arrowhead on the existing Parameter assignment → Atom interactions connection. The arrow shares the line's reveal timing; the 30-second duration and bonded branch are unchanged. Updated stills and preview were generated, preserving v6.

Bond-specific revision: current master `caffeine_message_passing_v6.blend` extends the scene to 30 seconds (1800 frames at 60 frames per second). The revised branch highlights the actual C7–O8 bond, copies exactly its two endpoint embeddings into labelled C/O slots, moves both through “Learned mixing”, emits one distinct “Bond embedding” vector, then assigns bond length/stiffness parameters. “Both atom orders” summarises the order-independent construction: apply the same network to both concatenation orders and sum its outputs. The visual is schematic, not a raw average of input vectors. [SRC-0003, Methods “Neural network architecture”, lines 443–450 in the local manuscript] Bond-input, mixing, output and final stills plus arrival samples were inspected; the preview is now 30 seconds. Earlier v5 remains preserved.

Parameter-card contrast revision: current master `caffeine_message_passing_v5.blend` uses bright white card titles/body text, pale-gold interaction symbols and darker card backgrounds, as requested by the user. The parameter still and affected preview frames were refreshed; v4 is preserved.

Contrast revision: the current master is now `caffeine_message_passing_v4.blend`. The user requested more readable element labels; O/C/N lettering was enlarged from 0.23 to 0.27 Blender units and given white fill with editable black outlines. Representative stills and the lightweight preview were refreshed. Earlier master v3 is preserved.

The requested scene was subsequently built through Blender MCP (Blender 5.1.0). Current master: `Documents/Garnet_Presentation/assets/caffeine_message_passing/caffeine_message_passing_v3.blend`; select scene `Caffeine_Message_Passing_v2`. Its `README.md` records the scientific caveats, source locators, timing, editing and exact rendering instructions. `build_v2.py` is the reproducible native-object build script. The original caffeine source scene and pre-existing animation files were preserved.

The master is 1920 × 1080, 60 frames per second, frames 1–1440 (24 seconds), with seven stage markers: molecule, graph, first round, second round, learned description, parameter assignment and final hold. The supplied PDB was checked: 24 atoms, 25 unique covalent edges, O8 adjacent only to C7 and exact second shell C6/N9. Native graph geometry retains the molecule and rings. First-round sender states are kept separate from updated descriptions; C7 passes aggregated context to O8 only in round two. Atom-interaction and multi-atom bonded-parameter routes are separate. Bars are symbolic, only selected layer updates are animated, and charges are omitted because their assignment includes a molecule-wide constraint. Scientific basis: Figure 1A and Methods “Neural network architecture”, including the Espaloma lineage cited there. [SRC-0003]

Six representative 1080p stills are in `stills_v2/`; the silent lightweight preview is `preview_v2/caffeine_message_passing_preview.mp4` (960 × 540, 12 frames per second, 24 seconds). Source/reference views, all six stages, arrival-adjacent frames and parameter-route frames were inspected. A description-strip/bond overlap, card contrast and low-sample denoising artefacts were corrected. Final Cycles settings are 96 samples, denoising off, PNG output, without depth-of-field or motion blur. Full-quality animation rendering and actual PowerPoint/projector playback remain outstanding; this scene depicts parameter assignment by an already-trained model, not training or molecular dynamics. No new source was ingested or scientific result added.

## Classical force-field terms animation handoff — 9 September 2026

After completion of the embedding animation, the user requested a separate caffeine animation explaining Garnet's classical force-field terms. Local `Documents/Garnet_Presentation/blender_force_field_terms_prompt.md` is the implementation handoff for a GPT-6 Astra low agent using Blender MCP and MolecularNodes. It specifies a 26-second sequence using C7–O8 for harmonic bond stretching, O8–C7–C6 for harmonic angle bending, C5–N13–C14–H22 for a proper torsion about N13–C14, and two caffeine molecules for representative intermolecular contacts. Atom selections were checked against the supplied PDB topology.

The handoff uses the manuscript's harmonic bond, harmonic angle, cosine torsion, Coulomb and Garnet double-exponential equations. Internal motion, contact lines and the caffeine-pair arrangement are explicitly schematic; they must not be presented as molecular dynamics, an energy-minimised dimer or caffeine hydrogen bonding. MolecularNodes supplies the complete molecular representations, with editable native overlays for annotations and a limited fallback for selected-atom deformation. Full-quality rendering remains deferred. [SRC-0003, Methods “Potential functional forms”]

The revised handoff adds a live signed response plot driven by each molecular coordinate rather than by time. The bond force and angle restoring torque cross zero linearly at equilibrium, the illustrative torsional torque is periodic, and the qualitative intermolecular radial force progresses from short-range repulsion through a zero crossing into attraction before tending to zero. Convenient dimensionless scaling is allowed, but the shapes and signs must remain mathematically consistent. These are explanatory curves, not caffeine-specific Garnet predictions. Each coordinate sweep leaves its completed curve visible for narration; the sequence is now approximately 30 seconds.


## Classical force-field terms animation delivered — 9 September 2026

Current editable asset: `Documents/Garnet_Presentation/assets/caffeine_force_field_terms/caffeine_force_field_terms_v08.blend`. This supersedes the force-field handoff's earlier 26-second estimate: the built sequence is 30 seconds, 1800 frames at 60 fps, with molecule 0–3 s, bond 3–9 s, angle 9–15 s, torsion 15–23 s, and intermolecular nonbonded interactions 23–30 s. The embedding-animation v11 master is unchanged.

Built through Blender MCP with Blender 5.1.0 and MolecularNodes 4.5.12. Both complete molecules retain editable MolecularNodes ball-and-stick representations. Upstream Geometry Nodes move O8 for C7–O8 stretching and O8–C7–C6 bending, and rotate H22–H24 around N13–C14 for the C5–N13–C14–H22 proper torsion. PDB element mapping, 24 atoms and 25 CONECT edges were verified. Evaluated geometry checks confirm constant angle-demo bond length, rigid methyl rotation and source-pose resets. Live native curve/text plots share the motion progress; the final graph explicitly illustrates the DE contribution, not a calculated total caffeine-dimer force. Source equations checked against local LaTeX Methods “Potential functional forms” and SRC-0003 printed pages 19–20.

Deliverables include `build_caffeine_ff_v08.py` (also embedded), `README.md`, five 1920×1080 stills in `stills_v08/`, a 30-second 960×540/10 fps movie `preview_v08.mp4`, sampled frames in `preview_v08/`, and `verification_v08.json`. Representative extrema, zero crossings, torsion states, contact geometry, equations and resets were inspected. Repaired inherited text render visibility and clarified the angle restoring arrow. The scene is schematic, motion exaggerated: not MD, Garnet training, a minimised dimer or hydrogen bonding. Final settings: Cycles 96 samples, denoising, 1920×1080/60 fps, PNG RGB, black world, no blur. Full-quality animation rendering and projector playback remain deferred. No new scientific result or source was added. [SRC-0003]


### Force-field motion amplification — v09

Current asset is `caffeine_force_field_terms_v09.blend`: bond motion doubled to ±16% and angle motion doubled to ±20°, with synchronized molecular geometry and overlays. Same 30-second timing. User requested a fast edit without renders or checks; v08 preview/stills remain unchanged and do not depict this revision. Builder `build_caffeine_ff_v09.py` is saved and embedded.


## Animation integration handoff — 10 September 2026

Local deliverables: `Documents/Garnet_Presentation/powerpoint_animation_handoff_2026-09-10.zip` and its editable folder, including README/paste prompt, consolidated AGENT_BRIEF.txt, slide revision brief, media cues, 19 original PNG stills with source mapping, seven recommended MP4s plus two alternate speeds, unchanged baseline deck/report, manuscript/figure references and review evidence. The task is another agent handoff; the PowerPoint itself was not edited. This brief supersedes older missing-media and still-only instructions.

Reviewed the supplied revised 18-slide deck using XML/text and a new LibreOffice render. Priorities remain the S07 prediction/reference comparisons, S10 Karplus-before-coupling ordering, and media sizing/static export. New force-field frames show potential-energy curves, superseding older force/torque documentation. The completed message-passing illustration uses O8, with one- and two-bond contexts before atom/bond parameter assignment; source for the model interpretation: SRC-0003 Figure 1A and Methods “Neural network architecture”. [SRC-0003]

User confirmations, 10 September 2026: J-coupling illustration highlights the hydrogens bonded to amide N and Cα, identifying HN–N–Cα–Hα and ³J(HN,Hα); it is still not established as an equilibrium MD trajectory. The free-energy movie is TYK2 with a ligand from the dataset used in the Garnet paper, a 5 ns simulation using the default OpenFE protocol. No run-specific force field, ligand-pair ID or exact linkage to the plotted TYK2 statistic was provided. The handoff pairs the bound-pocket movie with an editable bound/solvent comparison; method basis: SRC-0003 Methods “Relative binding free energy benchmark”, printed pp. 24–25. [SRC-0003; user media provenance, 10 September 2026]

All nine MP4s passed full decoding and are silent 1280×720 H.264/yuv420p. The 24/30/60 fps free-energy encodes have 1,005 frames and durations 41.875/33.5/16.75 seconds; the recommended 24 fps version is narrated inside S13’s existing two-minute allowance. Source stills are 1920×1080. ZIP integrity and byte-for-byte copies of input movies, selected stills and baseline deck/report were checked. Microsoft 365 playback, Morph, endpoint matching and venue readability remain untested. The 19-minute core speaking budget plus one-minute margin is retained.

## Discrete atom typing animation — 11 September 2026

Opening consistency revision: copied the exact molecular and camera actions from `/ssd/Blender/Garnet_Presentation/caffeine_message_passing.blend`. The complete molecule holds through frame 181, then hydrogens/bonds shrink away through frame 341 with the original camera easing. All 74 molecular objects match at every frame 1–341 (zero transform difference), with later holds also checked. The animation remains 20 seconds and retains the off-white background. `before_opening_morph.blend` preserves the previous discrete-typing file; the reference is unchanged.

The user requested a traditional atom-typing counterpart to the open Garnet message-passing animation and approved a 20-second atom-and-bond example using illustrative categories. The new editable file is `/ssd/Blender/Garnet_Presentation/caffeine_discrete_atom_typing.blend`; supporting assets are in `Documents/Garnet_Presentation/assets/caffeine_discrete_atom_typing/` (relative to the user's home). The folder includes the builder, narration/source notes, validation results, eight full-resolution stills and a 960×540/12 fps preview. A recovery copy preserves the original open scene and its unsaved edits; the original message-passing file is unchanged.

The new active scene is `Caffeine_Discrete_Atom_Typing`, 1920×1080, 60 fps, frames 1–1200. It retains caffeine's coordinates and connectivity, selects O8 and C7, assigns fixed carbonyl category badges, and animates copies into atom and paired-type parameter tables. Outputs are symbolic size/strength and bond length/stiffness. The final hold mentions angle/torsion type combinations. Categories are illustrative, not actual GAFF/Amber identifiers; parameter fitting, partial-charge assignment and molecular dynamics are not depicted. Background comes from the user-specified `background_color.txt`, sRGB `#F7F5F2`, verified as RGB (247, 245, 242) in the render.

Scientific provenance is recorded in the artifact README and embedded Blender notes: Wang et al., *J. Comput. Chem.* 25, 1157–1174 (2004), DOI https://doi.org/10.1002/jcc.20035, abstract (finite atom types and automatic application); OpenMM User Guide 7.7, “Creating Force Fields,” §6.1 and §6.2 (types/classes, template matching and parameter lookup). Garnet context was checked against SRC-0003, Introduction pp. 1–2 and Figure 1A. These are references for a schematic, not new results or source ingestion. [SRC-0003]

Focused checks preserve all 24 atoms and 25 bonds, verify lookup-event visibility, and inspect text bounds at 240 sampled frames. Stage and motion renders were reviewed. Actual PowerPoint/projector playback remains untested. The wiki validator has a pre-existing failure: missing YAML frontmatter in `wiki/answers/garnet-nonbonded-contact-cleanup.md`; that unrelated page was left untouched.
