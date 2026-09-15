# RpiCam project-goal summaries

Source ID: SRC-0089

This immutable source record captures the durable content of two project-goal summaries supplied directly by the user. It records intent, historical claims, proposed architecture, hardware details, and roadmap context; it is not a snapshot of the current RpiCam repository.

## Ultimate goal and artistic thesis

- Build a portable, battery-powered, standalone experimental digital camera and programmable imaging laboratory from low-level components: Adafruit Feather RP2350 with 8 MB PSRAM/HSTX, OV7670, ST7789, microSD, physical controls, battery, and enclosure.
- Make acquisition, digital representation, timing, memory, transformation, and output directly accessible.
- Treat the internal digital representation and electrical signal as artistic media. Prioritize unconventional artifacts, distortions, feedback, temporal effects, and deliberate corruption rather than conventional image quality.

## Intended baseline pipeline

- OV7670 8-bit parallel data plus PCLK/HREF/VSYNC -> RP2350 GPIO -> PIO RX FIFO -> DMA -> SRAM/PSRAM frame buffers -> programmable transformation -> ST7789 and/or USB/microSD.
- SCCB over hardware I2C configures the sensor separately from pixel acquisition.
- QVGA RGB565 is 320 x 240 x 2 = 153,600 bytes and maps conveniently to the display and low-level manipulation.
- PIO and DMA should perform deterministic byte acquisition without per-byte CPU servicing. The CPU remains available for sensor configuration, frame management, transformations, UI, storage/display, and glitch-control timing.
- HSTX may be explored for low-CPU display output.

## Experimental layers

1. Software manipulation of RGB565 pixels, channels, scanlines, full frames, and frame history. Candidate operations include shifting, reordering, duplication, deletion, sorting, accumulation, blending, feedback, controlled corruption, and stateful or temporal transforms.
2. Hardware-level digital circuit bending inserted into D0-D7 before RP2350 capture, intended to generate distinctive effects electrically rather than merely as post-processing.

Proposed hardware glitch logic uses 74LVC4066 bilateral switches to connect or disconnect selected bus bits and 74LVC86 XOR gates to conditionally invert bits. RP2350-generated control signals could synchronize glitches to VSYNC/HREF/PCLK, selected rows, pixels or regions, periodic or pseudorandom patterns, and potentiometer or user inputs. Intended effects include color shifts or removal, quantization, clipping, posterization, bands, and patterned discontinuities.

## Physical interface and memory intent

- Intended controls include shutter, mode/navigation buttons, switches, potentiometers, and glitch enable/intensity/position/frequency controls.
- ADC resistor ladders or I/O expanders may conserve GPIO.
- PSRAM is unnecessary for one QVGA frame but strategically important for multiple/history buffers, temporal accumulation, delayed feedback, alternate/intermediate frames, regional processing, and double/triple buffering.

## User-reported historical milestones

The summaries report these milestones as having been achieved historically: OV7670 PID 0x76 and VER 0x73; SCCB, XCLK, sync and data bring-up; exact 640-byte lines; eight consecutive lines; complete 240-line/153,600-byte frame captures; deterministic color bars; and changing optical frames.

These are user-provided historical claims and are not, by themselves, evidence of current repository behavior.

## Development strategy and roadmap

The proposed sequence is to validate sensor control/timing/capture independently, perform host visual validation, add display, add storage, add physical controls, add hardware glitch logic, synchronize artistic control, and complete standalone integration.

The summaries describe USB frame export or host-side visual development as current and TFT/microSD as future work. This chronology must not override later repository evidence: the current inspected firmware already implements SPI0 ST7789 preview and SPI1/FatFs BMP storage, but no USB frame protocol. Transformations, PSRAM use, physical controls, hardware glitch circuitry, and battery/enclosure integration remain goals.

## User-reported hardware details

The summaries additionally report PWDN tied to GND, RESET tied to 3.3 V, local sensor decoupling, and two parallel 10 kOhm PCLK pull-down resistors. These details are user-reported and are not necessarily verified by the current repository source.
