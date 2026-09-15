---
type: concept
status: active
created: 2026-09-14
updated: 2026-09-14
areas:
  - research
  - work
categories:
  - research/scientific-computing
tags:
  - embedded-systems
  - camera
  - rp2350
  - ov7670
  - st7789
  - microSD
  - artistic-imaging
  - circuit-bending
  - roadmap
related:
  - "[[wiki/sources/SRC-0089-rpicam-project-goal-summaries]]"
  - "[[wiki/tensions/TEN-0019-rpicam-firmware-host-tool-protocol-drift]]"
sources:
  - SRC-0088
  - SRC-0089
sensitivity: public
encryption: none
---
# RpiCam Embedded Camera Firmware

## Summary

RpiCam is an RP2350 embedded camera pipeline whose current authoritative behavior is local OV7670 capture, ST7789 preview and microSD BMP still storage. Camera pixels are acquired as QVGA RGB565 using PIO plus DMA; two full-frame buffers connect a core-1 capture worker to core-0 TFT output. USB CDC is currently a text command console rather than a frame-streaming transport. [SRC-0088; `RpiCam.c`]

The broader user-stated goal is a portable, battery-powered, standalone experimental digital camera and programmable imaging laboratory. Its artistic thesis treats acquisition, digital representation, electrical signals, timing, memory, transformation, and output as accessible media for artifacts, distortion, feedback, temporal effects, and deliberate corruption rather than optimizing only for conventional image quality. This intent is not evidence of current implementation. [SRC-0089]

## Current architecture

- **Sensor/control:** OV7670 on SCCB-compatible I²C1, with PWM-generated XCLK and discrete HREF/VSYNC/PCLK inputs. The sensor is configured for 320×240 RGB565 using a large reference ISP/AWB table and empirically shifted capture window. [SRC-0088; `RpiCam.c`]
- **Capture:** PIO0 state machine 0 samples eight consecutive data GPIOs on PCLK rising edges while HREF is high. DMA reads the RX FIFO as 8-bit transfers, 640 bytes per line and 240 lines per frame. [SRC-0088; `camera.pio`, `RpiCam.c`]
- **Preview:** two 153,600-byte buffers and free/ready queues decouple capture on core 1 from blocking SPI0 writes to a landscape 320×240 ST7789 on core 0. [SRC-0088; `RpiCam.c`]
- **Still storage:** preview is paused, one frame is captured, converted from big-endian camera/TFT byte order to little-endian BMP pixel words, and written through FatFs and a custom SPI1 SD block driver. [SRC-0088; `RpiCam.c`, `sd_spi.c`]

## Intended experimental architecture

The goal pipeline is OV7670 D0-D7 plus PCLK/HREF/VSYNC -> RP2350 GPIO -> PIO RX FIFO -> DMA -> SRAM/PSRAM frame buffers -> programmable transformation -> ST7789 and/or USB/microSD. SCCB over hardware I2C configures the sensor independently. QVGA RGB565 is $320 \times 240 \times 2 = 153{,}600$ bytes, making it convenient for direct display and low-level manipulation. PIO/DMA own deterministic byte acquisition; the CPU remains available for sensor setup, frame management, transformation, UI, output, and glitch-control timing. [SRC-0089]

Two complementary experimentation layers are intended: [SRC-0089]

1. **Software transforms:** pixel/channel/scanline/frame/history operations including shifting, reordering, duplication, deletion, sorting, accumulation, blending, feedback, controlled corruption, and stateful or temporal transforms.
2. **Electrical transforms before capture:** 74LVC4066 switches would disconnect selected D0-D7 bits and 74LVC86 XOR gates would conditionally invert them. RP2350 controls could synchronize effects to VSYNC/HREF/PCLK, rows/pixels/regions, periodic or pseudorandom patterns, and user inputs, producing color shifts/removal, quantization, clipping, posterization, bands, and patterned discontinuities.

The intended physical interface includes shutter and navigation buttons, switches, potentiometers, and glitch enable/intensity/position/frequency controls; ADC resistor ladders or I/O expanders may conserve GPIO. [SRC-0089]

## Memory and output intent versus implementation

A single QVGA frame does not require PSRAM. PSRAM matters strategically for frame history, accumulation, delayed feedback, alternate/intermediate frames, regional processing, and double/triple buffering. Current code instead uses two internal-SRAM frames and does not use PSRAM. HSTX may be explored for lower-CPU display output, but current display output is SPI0. [SRC-0089; SRC-0088, `RpiCam.c`]

## Current interface

The implemented firmware commands are `h` (help), `s` (save still), `L` (start TFT preview), and `q`/`Q`/Escape (stop preview). Startup automatically starts preview after successful camera initialization. [SRC-0088; `RpiCam.c`]

The repository's Python receivers describe a different, older interface based on `FRAME_BEGIN`/`FRAME_END`, `e` single-frame requests, `S` continuous streaming and numerous tuning controls. That interface is absent from current firmware. [SRC-0088; `recv_frame.py`, `live_view.py`, `RpiCam.c`]

## Hardware invariants

- D0…D7 must occupy consecutive GPIO22…GPIO29 because PIO samples eight pins from the configured input base. [SRC-0088; `RpiCam.c`, `camera.pio`]
- HREF and PCLK are embedded as absolute GPIO0 and GPIO4 waits in the PIO program; changing only C constants is insufficient. [SRC-0088; `camera.pio`]
- TFT remains on SPI0 while microSD uses SPI1 GPIO12…GPIO15; this avoids bus/pin sharing. [SRC-0088; `RpiCam.c`, `pinout.txt`]
- The HSTX breakout lane names are not SD signal names: SD D0/SO is connected to D2+/GPIO12. GPIO8 should be avoided where the Feather board includes PSRAM. [SRC-0088; `pinout.txt`]

## Historical claims and roadmap status

The user-provided summaries report OV7670 PID `0x76`/VER `0x73`, SCCB/XCLK/sync/data bring-up, exact 640-byte lines, eight consecutive lines, complete 240-line/153,600-byte captures, deterministic color bars, and changing optical frames. They also report PWDN tied to GND, RESET tied to 3.3 V, local sensor decoupling, and two parallel 10 kOhm PCLK pull-downs. These are user-reported historical or hardware claims, not current-source-verified facts unless SRC-0088 independently corroborates them. [SRC-0089]

The intended development sequence is sensor control/timing/capture validation -> host visual validation -> display -> storage -> physical controls -> hardware glitch logic -> synchronized artistic control -> standalone integration. Current repository inspection places capture, SPI0 ST7789 preview, and SPI1/FatFs BMP storage in the implemented column. USB frame export appears removed or regressed relative to retained tools. Transformations, PSRAM use, physical controls, glitch circuitry, battery power, and enclosure integration remain roadmap items. [SRC-0089; SRC-0088]

## Constraints and maintenance guidance

- Treat `RpiCam.c` as authoritative for command behavior and PIO/DMA configuration. `camera.pio` comments and host-tool documentation contain known historical assumptions. [SRC-0088]
- Two frame buffers reserve 307,200 bytes, making RAM budget a first-order constraint. [SRC-0088; `RpiCam.c`]
- FatFs is deliberately minimal: one 512-byte-sector volume, 8.3 filenames, no exFAT, no RTC timestamps and no re-entrancy. [SRC-0088; `third_party/fatfs/source/ffconf.h`]
- Hardware timing and image behavior cannot be established by a successful build alone. Meaningful validation requires flashing and checking frame dimensions, alignment, color order, capture stability, TFT preview and microSD writes on the actual wiring. [SRC-0088; `AGENTS.md`]

## Links

- [[wiki/sources/SRC-0088-rpicam-repository]] — current implementation snapshot.
- [[wiki/sources/SRC-0089-rpicam-project-goal-summaries]] — user-stated goals, history, intended architecture, and roadmap.
- [[wiki/tensions/TEN-0019-rpicam-firmware-host-tool-protocol-drift]]

## Open Questions

- Should USB frame transport be restored in firmware, or should the Python tools be retired/reworked around the local TFT/microSD design? [SRC-0088]
- Under which board clock and attached OV7670 module was the empirical +18-pixel shift validated? [SRC-0088]
- What sustained preview frame rate and SD-card compatibility have been measured on current hardware? [SRC-0088]
- Should USB frame export be restored for host visual development, or should host validation use a different interface? [SRC-0088; SRC-0089]
- Which software transforms, electrical glitch topology, physical controls, and PSRAM buffering strategy should form the first experimental milestone? [SRC-0089]
- Can the user-reported historical milestones and supplemental wiring details be tied to dated logs, schematics, or current hardware verification? [SRC-0089]
