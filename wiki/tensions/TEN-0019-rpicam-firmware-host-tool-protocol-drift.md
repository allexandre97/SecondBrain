---
type: tension
status: active
created: 2026-09-14
updated: 2026-09-14
tension_status: active
areas:
  - research
  - work
categories:
  - research/scientific-computing
tags:
  - tension
  - protocol-drift
  - stale-tooling
  - usb-cdc
related:
  - "[[wiki/concepts/rpicam-embedded-camera-firmware]]"
  - "[[wiki/sources/SRC-0088-rpicam-repository]]"
  - "[[wiki/sources/SRC-0089-rpicam-project-goal-summaries]]"
related_claims: []
related_questions: []
sources:
  - SRC-0088
  - SRC-0089
sensitivity: public
encryption: none
---
# RpiCam Firmware–Host Tool Protocol Drift

## Tension

The current RpiCam firmware implements local TFT preview and microSD still capture with commands `h`, `s`, `L` and `q`, while the retained Python host tools and user-provided historical roadmap context describe USB host frame validation or export that no longer exists in the firmware. [SRC-0088; SRC-0089; `RpiCam.c`, `recv_frame.py`, `live_view.py`]

## Positions

- `RpiCam.c` contains no `FRAME_BEGIN`/`FRAME_END` framing, checksum generation, USB frame-payload path, `e` one-frame command, `S` stream command, or host-driven sensor tuning handlers. Its “stream” functions are an internal multicore capture-to-TFT pipeline. [SRC-0088; `RpiCam.c`]
- `recv_frame.py` sends `e` and blocks waiting for checksummed frame envelopes. `live_view.py` sends `S` or repeated `e` commands and exposes many register-tuning commands. The repository guidance still presents both scripts as runnable against the device. [SRC-0088; `recv_frame.py`, `live_view.py`, `AGENTS.md`]
- `camera.pio` comments similarly retain older transfer assumptions: shift-right and “640 words,” versus current shift-left, 8-bit DMA and 640 byte transfers in C. [SRC-0088; `camera.pio`, `RpiCam.c`]
- The project-goal summaries preserve a historical sequence in which host visual validation/USB export precedes display and storage, and describe TFT/microSD as future work. Current repository evidence shows that capture, SPI0 TFT preview, and SPI1/FatFs BMP storage are implemented while USB frame export is absent. The summaries remain authoritative for intent and history, not present implementation. [SRC-0089; SRC-0088]

## Why it matters

A developer following the host-tool documentation will receive timeouts or “Unknown command” responses rather than frames, and a developer following the PIO comments may incorrectly change byte alignment or DMA width. Future changes must first choose which interface is authoritative: restore a versioned USB protocol or remove/update the stale tools and comments around the local preview/storage design. [SRC-0088]

## Resolution status

Active. SRC-0088 and current firmware remain authoritative for present behavior; SRC-0089 preserves goals and historical claims. The project has not yet decided whether to restore a versioned USB protocol or explicitly retire/update the stale host tools and PIO commentary. [SRC-0088; SRC-0089]

## Links

- [[wiki/sources/SRC-0088-rpicam-repository]]
- [[wiki/sources/SRC-0089-rpicam-project-goal-summaries]]
- [[wiki/concepts/rpicam-embedded-camera-firmware]]
