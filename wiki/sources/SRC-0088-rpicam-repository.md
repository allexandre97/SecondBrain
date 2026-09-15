---
type: source
status: active
created: 2026-09-14
updated: 2026-09-14
source_id: SRC-0088
display_title: "RpiCam Firmware Repository"
short_title: "RpiCam"
aliases:
  - "SRC-0088"
  - "RpiCam"
  - "RpiCam repository"
original_filename: "RpiCam repository working tree"
original_path_note: "Authoritative local repository path omitted from wiki metadata; paths below are relative to its root."
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
  - rp2350
  - ov7670
  - st7789
  - microSD
  - rgb565
  - pico-sdk
related:
  - "[[wiki/concepts/rpicam-embedded-camera-firmware]]"
  - "[[wiki/sources/SRC-0089-rpicam-project-goal-summaries]]"
  - "[[wiki/tensions/TEN-0019-rpicam-firmware-host-tool-protocol-drift]]"
sources:
  - SRC-0088
cites_sources: []
citation_match_status: reviewed
cqt_review_status: linked
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: deep
source_bundle: rpicam-repository
bundle_role: main
---
# RpiCam Firmware Repository

Source ID: `SRC-0088`

## Source scope and provenance

This source is an in-place inspection of the current RpiCam working tree. File locators below are relative to the authoritative repository root supplied with the ingestion request. Ignored generated output (`build/`, frame dumps, images, bytecode and PDFs) was excluded from architectural interpretation. Vendored FatFs was inspected only where its configuration or integration affected current behavior. No RpiCam files were modified. [SRC-0088]

Primary implementation evidence:

- `RpiCam.c` — firmware architecture, peripheral assignments, camera setup, capture, preview, storage and command dispatch.
- `camera.pio` — pixel sampling state machine and comments about its expected C configuration.
- `sd_spi.c`, `sd_spi.h`, `third_party/fatfs/source/ffconf.h` — custom SPI block driver and FatFs constraints.
- `CMakeLists.txt`, `pico_sdk_import.cmake` — board, SDK and firmware build integration.
- `pinout.txt` — wiring record, checked against firmware constants.
- `recv_frame.py`, `live_view.py`, `environment.yml` — host-side workflow and protocol assumptions.
- `AGENTS.md`, `.gitignore` — repository guidance and evidence that Markdown documentation, build output and captured frames are ignored.

No immutable raw repository snapshot or Git revision identifier was imported. The source therefore records the implementation observed during this ingestion, not an automatically updating mirror. [SRC-0088]

## Summary

RpiCam is bare-metal Pico SDK firmware targeting an Adafruit Feather RP2350. It configures an OV7670 for 320×240 RGB565, captures each 640-byte scan line through a PIO state machine and byte-wide DMA, and stores complete frames in two 153,600-byte buffers. Core 1 captures into the double buffers while core 0 sends ready frames to a 320×240 landscape ST7789 over SPI0. A separate custom SPI1 SD block driver backs FatFs and saves individual top-down 16-bit RGB565 BMP files. USB CDC currently serves as a textual command console, not a frame transport. [SRC-0088; `RpiCam.c`, `camera.pio`, `sd_spi.c`]

## Architecture and data flow

1. Startup initializes USB stdio, SCCB/I²C and camera pins, TFT bus state and microSD mounting; then starts the camera XCLK, recovers the I²C bus, programs the OV7670, initializes PIO/DMA and immediately enters TFT preview. [SRC-0088; `RpiCam.c` `main`]
2. The OV7670 is reset and programmed for QVGA RGB565. A reference ISP/AWB table is applied, followed by empirically tuned capture timing including a documented +18-pixel horizontal shift intended to suppress fixed left-edge artifacts. [SRC-0088; `RpiCam.c` `ov7670_*_seq`]
3. Frame synchronization is driven by VSYNC. For each of 240 lines, firmware resets the PIO state machine/FIFOs and DMA channel, configures an 8-bit DMA transfer of 640 bytes, waits for HREF low, then starts DMA and PIO. Each line has a 100 ms DMA timeout; frame-start synchronization has a 1 s timeout. [SRC-0088; `RpiCam.c` `wait_for_frame_start`, `capture_full_frame_into`]
4. Preview uses two full-frame buffers and two inter-core queues. Core 1 captures into a free buffer and queues it as ready; core 0 writes ready frames to the TFT and returns the buffer. This is double-buffered multicore capture/display, but it is not USB streaming. [SRC-0088; `RpiCam.c` `stream_capture_worker`, `preview_frames_tft`]
5. A still request stops preview capture, captures into `framebuf`, writes an `IMG0001.BMP`-style temporary file, syncs/closes it, and renames it atomically to the final name before preview is restarted. RGB565 bytes are swapped per pixel because the camera/TFT path is big-endian while BMP pixel words are little-endian. [SRC-0088; `RpiCam.c` `save_still_to_sd`, `write_frame_bmp`]

## Hardware mapping

The implementation and `pinout.txt` agree on the following current mapping. [SRC-0088; `RpiCam.c`, `pinout.txt`]

| Function | Peripheral / pins |
| --- | --- |
| OV7670 control | I²C1/SCCB: SDA GPIO2, SCL GPIO3; 10 kHz |
| OV7670 clock/sync | XCLK GPIO10 from PWM; HREF GPIO0; VSYNC GPIO1; PCLK GPIO4 |
| OV7670 data | D0…D7 on consecutive GPIO22…GPIO29 |
| ST7789 | SPI0: CS GPIO5, SCK GPIO6, MOSI GPIO7, reset GPIO9, DC GPIO11, backlight GPIO20; 24 MHz |
| microSD | SPI1: MISO GPIO12, CS GPIO13, SCK GPIO14, MOSI GPIO15; 400 kHz initialization then 12 MHz |

Important wiring constraints are that camera data must remain consecutive for `in pins, 8`; the PIO program directly waits on absolute GPIO0 and GPIO4; SD uses SPI1 rather than sharing TFT SPI0; SD D0/SO maps to the HSTX breakout label D2+/GPIO12; and GPIO8 should be avoided on Feather variants carrying PSRAM. [SRC-0088; `camera.pio`, `pinout.txt`]

## Firmware behavior and interface

The current command set exposed by `print_help` and handled by `main` is: [SRC-0088; `RpiCam.c` `print_help`, `main`]

| Command | Current behavior |
| --- | --- |
| `h` | Print help. |
| `s` | Save one BMP still to microSD; during preview, capture is stopped and restarted around the save. |
| `L` | Start the TFT live preview. |
| `q`, `Q`, or Escape | Stop an active preview; outside preview they have no additional action. |

Startup enters preview automatically after successful camera initialization, so command-console availability is normally reached only after preview is stopped. `stdio_set_translate_crlf(..., false)` remains configured, but the current firmware sends no binary frame envelope or payload over USB. [SRC-0088; `RpiCam.c` `main`, `preview_frames_tft`]

## microSD and BMP constraints

- Storage uses a project-specific SPI-mode SD driver implementing single-sector reads/writes (`CMD17`/`CMD24`) and SD v1/v2 initialization, with FatFs providing the filesystem layer. [SRC-0088; `sd_spi.c`]
- Card detect is disabled, there is one volume, 512-byte sectors, no exFAT, no long filenames, no re-entrancy, and no real-time clock timestamps. The fallback FatFs date is configured to 2026-01-01. [SRC-0088; `RpiCam.c`, `third_party/fatfs/source/ffconf.h`]
- Filenames are limited to `IMG0001.BMP` through `IMG9999.BMP`. Existing names are scanned at mount; a temporary `.TMP` file is used during each write. [SRC-0088; `RpiCam.c`]
- BMP output is 320×240, 16-bit BI_BITFIELDS RGB565, top-down, and 153,666 bytes including the 66-byte header. [SRC-0088; `RpiCam.c`]

## Build and runtime workflow

- Firmware is built with CMake and Pico SDK 2.2.0 for `PICO_BOARD=adafruit_feather_rp2350`. The target compiles `RpiCam.c`, `sd_spi.c` and vendored `ff.c`, generates `camera.pio.h`, enables USB stdio, disables UART stdio, and emits the Pico extra outputs such as UF2. [SRC-0088; `CMakeLists.txt`]
- Expected commands are `cmake -B build -S .` and `cmake --build build`, followed by flashing the UF2 and testing on the wired hardware. No automated tests exist. [SRC-0088; `AGENTS.md`, `CMakeLists.txt`]
- `environment.yml` creates a Python 3.10 `rpicam` environment with pyserial, NumPy and OpenCV for the host scripts. Those scripts are not currently compatible with the firmware protocol, so their documented run commands are historical unless the USB protocol is restored or the tools are updated. [SRC-0088; `environment.yml`, `recv_frame.py`, `live_view.py`, `RpiCam.c`]

## Current inconsistencies and limitations

### Host tools versus firmware

Both Python programs wait for `FRAME_BEGIN width height RGB565 nbytes checksum` and `FRAME_END checksum` records around a binary USB payload. `recv_frame.py` requests a frame with `e`; `live_view.py` requests with `e` or starts continuous streaming with `S`, and it sends many register-tuning commands. None of the frame-envelope strings, frame payload writes, `e`/`S` handlers, checksum code, or tuning-command handlers is present in current `RpiCam.c`. The firmware instead exposes only `h`, `s`, `L` and `q`. The host utilities and the corresponding `AGENTS.md` usage claims are therefore stale/incompatible with the current implementation. [SRC-0088; `recv_frame.py`, `live_view.py`, `RpiCam.c`, `AGENTS.md`]

### PIO comments versus C configuration

`camera.pio` says the input shift is right and DMA transfers “640 words.” Current C explicitly configures shift-left (`sm_config_set_in_shift(..., false, true, 8)`), uses `DMA_SIZE_8`, and requests `LINE_BYTES = 640` transfers. The executable PIO instructions remain consistent with byte sampling, but these comments describe an older configuration and should not be used as the current contract. [SRC-0088; `camera.pio`, `RpiCam.c` `init_pio_capture`, `capture_full_frame_into`]

### Validation and operational limits

- No automated build, unit, integration or hardware test suite is present. Architecture was established by static source inspection; camera timing, image quality, SD-card compatibility, preview frame rate and electrical behavior were not independently exercised during ingestion. [SRC-0088; `AGENTS.md`]
- The two frame buffers consume 307,200 bytes before other static/runtime memory. This is intentional for multicore double buffering but is a major RAM constraint for future features. [SRC-0088; `RpiCam.c`]
- Capture resets/configures PIO and DMA for every line and busy-waits on VSYNC/HREF and queue availability. This tightly couples operation to current signal polarity/timing and can occupy both cores continuously during preview. [SRC-0088; `RpiCam.c`, `camera.pio`]
- The OV7670 tuning table and +18-pixel window shift are empirical; provenance and validation conditions are not documented beyond source comments. [SRC-0088; `RpiCam.c`]
- The repository guidance says Markdown and PDFs are ignored, so `AGENTS.md` and `pinout.txt` can describe important behavior without necessarily being tracked as authoritative versioned documentation. Current C and PIO implementation should take precedence where they disagree. [SRC-0088; `.gitignore`, `AGENTS.md`, `pinout.txt`]

## Tensions

- [[wiki/tensions/TEN-0019-rpicam-firmware-host-tool-protocol-drift]]

## Links

- [[wiki/concepts/rpicam-embedded-camera-firmware]]
- [[wiki/sources/SRC-0089-rpicam-project-goal-summaries]] — user-stated goals, historical milestones, intended architecture, and roadmap; not evidence of current implementation.

## Ingestion QA

### Retrieval questions checked

- What board, camera, display and storage interfaces does RpiCam use?
- How does a frame move from OV7670 pins through PIO/DMA to the ST7789?
- What are the exact current GPIO assignments?
- What commands does the current firmware implement?
- How are still images named, encoded and safely written?
- How is firmware built and what must be tested on hardware?
- Are `recv_frame.py` and `live_view.py` usable with current firmware?
- Which `camera.pio` comments are stale relative to C?
- What are the principal memory, timing, filesystem and validation constraints?

### Coverage decision

Coverage is complete for the requested static architecture, hardware mapping, current firmware behavior, build/runtime workflow, constraints and source-visible inconsistencies. [SRC-0088]

### Known gaps

- No Git commit/revision or clean/dirty state could be recorded, so “current” refers to the files observed during ingestion.
- No firmware build, flash, camera/display test or microSD write was performed.
- Generated build artifacts and captured frames were intentionally not treated as authoritative evidence.
