---
type: source
status: active
created: 2026-09-14
updated: 2026-09-14
source_id: SRC-0089
display_title: "RpiCam Project-Goal Summaries"
short_title: "RpiCam Goals"
aliases:
  - "SRC-0089"
  - "RpiCam goals"
  - "RpiCam roadmap"
source_path: raw/sources/SRC-0089-rpicam-project-goal-summaries.md
imported_path: raw/sources/SRC-0089-rpicam-project-goal-summaries.md
original_filename: "Two user-provided RpiCam project-goal summaries"
original_path_note: "Supplied directly in the wiki-update request; no external file path."
authors: []
author_entities: []
year:
venue:
doi:
arxiv:
metadata_review_status: not-applicable
areas:
  - research
  - work
categories:
  - research/scientific-computing
tags:
  - embedded-systems
  - experimental-camera
  - artistic-imaging
  - rp2350
  - ov7670
  - circuit-bending
  - roadmap
related:
  - "[[wiki/sources/SRC-0088-rpicam-repository]]"
  - "[[wiki/concepts/rpicam-embedded-camera-firmware]]"
  - "[[wiki/tensions/TEN-0019-rpicam-firmware-host-tool-protocol-drift]]"
sources:
  - SRC-0089
cites_sources: []
citation_match_status: reviewed
cqt_review_status: linked
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: deep
source_bundle: rpicam-repository
bundle_role: supplement
---
# RpiCam Project-Goal Summaries

Source ID: `SRC-0089`

## Raw source

- Repository path: `raw/sources/SRC-0089-rpicam-project-goal-summaries.md`
- Open raw source: [raw/sources/SRC-0089-rpicam-project-goal-summaries.md](../../raw/sources/SRC-0089-rpicam-project-goal-summaries.md)

## Provenance and interpretation boundary

This source records two summaries supplied directly by the user as project-intent and roadmap context. It is authoritative for the user's stated goals, proposed architecture, and user-reported history, but not for the current RpiCam implementation. Current implementation facts come from the later static repository inspection in [[wiki/sources/SRC-0088-rpicam-repository]]. Where the summaries' chronology conflicts with observed code, SRC-0088 governs present behavior and the discrepancy is preserved rather than silently reconciled. [SRC-0089]

## Overall goal and artistic thesis

The ultimate goal is a portable, battery-powered, standalone experimental digital camera and programmable imaging laboratory built from low-level components: an Adafruit Feather RP2350 with 8 MB PSRAM/HSTX, OV7670 sensor, ST7789 display, microSD storage, physical controls, battery, and enclosure. [SRC-0089]

The artistic aim is to expose acquisition, digital representation, timing, memory, transformation, and output as directly controllable media. The internal digital representation and electrical signal are themselves artistic material; unconventional artifacts, distortion, feedback, temporal effects, and deliberate corruption take priority over conventional image quality. [SRC-0089]

## Intended baseline architecture

The intended pipeline is OV7670 8-bit data plus PCLK/HREF/VSYNC -> RP2350 GPIO -> PIO RX FIFO -> DMA -> SRAM or PSRAM frame buffers -> programmable transformation -> ST7789 and/or USB/microSD. SCCB over hardware I2C configures the sensor separately. QVGA RGB565 is a convenient baseline because $320 \times 240 \times 2 = 153{,}600$ bytes maps directly to the display and supports low-level manipulation. [SRC-0089]

PIO and DMA are intended to acquire bytes deterministically without per-byte CPU servicing. The CPU can then handle sensor configuration, frame management, transformations, user interaction, storage/display, and timing of glitch controls. HSTX is a possible future route to lower-CPU display output; it is not the current display implementation, which uses SPI0. [SRC-0089; SRC-0088, `RpiCam.c`]

## Complementary experimental layers

### Software transformation

Planned software operations act on RGB565 pixels, channels, scanlines, whole frames, and frame history. Candidate operations include shifts, reordering, duplication, deletion, sorting, accumulation/blending, feedback, controlled corruption, and stateful or temporal transforms. [SRC-0089]

### Hardware digital circuit bending

A complementary layer would alter D0-D7 electrically before RP2350 capture rather than reproducing every effect in post-processing. Proposed logic uses 74LVC4066 bilateral switches to connect or disconnect selected bits and 74LVC86 XOR gates to conditionally invert them. RP2350 control signals could synchronize interventions to VSYNC/HREF/PCLK, selected rows/pixels/regions, periodic or pseudorandom patterns, and potentiometer or other user inputs. Intended effects include color shifts or removal, quantization, clipping, posterization, bands, and patterned discontinuities. [SRC-0089]

## Physical controls and memory strategy

The intended interface includes shutter and mode/navigation buttons, switches, potentiometers, and controls for glitch enable, intensity, position, and frequency. ADC resistor ladders or I/O expanders may reduce GPIO demand. [SRC-0089]

One QVGA frame does not require PSRAM, but PSRAM is strategically important for multiple/history buffers, temporal accumulation, delayed feedback, alternate or intermediate frames, regional processing, and double/triple buffering. Current firmware instead holds two frames in internal SRAM and does not use PSRAM. [SRC-0089; SRC-0088, `RpiCam.c`]

## User-reported historical milestones

The summaries report successful OV7670 PID `0x76` and VER `0x73` reads; SCCB, XCLK, sync, and data bring-up; exact 640-byte scanlines; eight consecutive lines; complete 240-line/153,600-byte captures; deterministic color bars; and changing optical frames. These are historical claims supplied by the user and were not independently corroborated during this ingestion unless they overlap with static current-repository facts. [SRC-0089]

## Roadmap and current-state reconciliation

The proposed development sequence is independent validation of sensor control/timing/capture, host visual validation, display, storage, physical controls, hardware glitch logic, synchronized artistic control, and finally standalone integration. [SRC-0089]

The summaries describe USB frame export or host visual development as current and TFT/microSD as future work. Later repository evidence changes that status: current `RpiCam.c` implements capture, SPI0 ST7789 preview, and SPI1/FatFs BMP storage, while the old USB frame protocol is absent and retained host tooling has drifted. Transformations, PSRAM usage, physical controls, hardware glitch circuitry, and battery/enclosure integration remain future goals. [SRC-0089; SRC-0088, `RpiCam.c`, `recv_frame.py`, `live_view.py`]

## Additional user-reported hardware details

PWDN is reported tied to GND, RESET tied to 3.3 V, local sensor decoupling is reported present, and PCLK is reported to have two parallel 10 kOhm pull-down resistors. These details supplement the wiring already recorded in SRC-0088 but remain user-reported rather than current-source-verified. [SRC-0089]

## Limitations and caveats

- The source is a goal/history summary, not an immutable project snapshot or electrical verification report. [SRC-0089]
- Proposed parts, controls, effects, HSTX output, PSRAM use, battery power, and enclosure details are intent, not implemented features unless SRC-0088 separately says otherwise. [SRC-0089; SRC-0088]
- Historical milestones and supplemental wiring details should be verified against dated artifacts or hardware before being treated as current facts. [SRC-0089]

## Tensions

- [[wiki/tensions/TEN-0019-rpicam-firmware-host-tool-protocol-drift]]

## Links

- [[wiki/sources/SRC-0088-rpicam-repository]]
- [[wiki/concepts/rpicam-embedded-camera-firmware]]

## Ingestion QA

### Retrieval questions checked

- What is the ultimate RpiCam project goal and artistic thesis?
- What intended pipeline divides work among SCCB/I2C, PIO, DMA, CPU, frame memory, and outputs?
- What software and electrical glitch layers are proposed?
- Why is PSRAM strategically useful even though one QVGA frame fits without it?
- Which milestones and wiring details are only user-reported historical claims?
- Which roadmap stages are already implemented according to SRC-0088?
- Which features remain future intent?
- Why must HSTX and USB frame export not be described as current behavior?

### Coverage decision

Coverage is complete for the durable goal, artistic, architecture, hardware-experiment, interface, memory, historical, wiring, and roadmap context supplied by the user. [SRC-0089]

### Known gaps

- The two original summaries were supplied through the request rather than as separately imported files, so this source preserves their requested durable content as one consolidated source record.
- Historical milestones and supplemental wiring details lack dated test logs or current hardware corroboration.
