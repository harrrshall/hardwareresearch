# paper-001: UCIe 3.0 Specification — 64 GT/s Chiplet Interconnect for AI Era

**Tags:** UCIe, chip-to-chip  
**Date:** 2025-08-05  
**Source:** UCIe Consortium / BusinessWire  
**URL:** https://www.uciexpress.org/post/ucie-3-0-specification-redefining-chiplet-interconnects

---

## Summary

The UCIe Consortium officially released version 3.0 of the Universal Chiplet Interconnect Express specification on August 5, 2025, timed to coincide with the Flash Memory Summit (FMS 2025). UCIe 3.0 represents the third major revision since the standard's launch in March 2022 and delivers the highest data rates in the standard's history.

## Key Technical Specifications

| Parameter | UCIe 2.0 | UCIe 3.0 |
|---|---|---|
| UCIe-S data rate | 32 GT/s | 48 GT/s |
| UCIe-A data rate | 32 GT/s | 64 GT/s |
| Sideband reach | ~50 mm | up to 100 mm |
| Backward compatibility | UCIe 1.x | UCIe 1.x, 2.0 |

## New Features

- **Runtime recalibration**: Improves power efficiency during operation; links recalibrate without full retraining
- **Early firmware download**: Increases system responsiveness during boot and resets
- **Priority sideband packets**: Enables time-critical management operations to bypass queued data
- **Extended sideband reach (100 mm)**: Supports more flexible System-in-Package (SiP) topologies
- **Full backward compatibility** with UCIe 1.0, 1.1, and 2.0

## Architectural Context

UCIe defines both a die-to-die physical layer (package and advanced variants) and a protocol stack supporting PCIe and CXL traffic over the same link. UCIe-S targets standard organic substrate packaging (bump pitch ~130 µm), while UCIe-A targets advanced packaging (bump pitch <55 µm) such as TSMC CoWoS or Intel EMIB, enabling the higher 64 GT/s rate.

## Industry Impact

The UCIe 3.0 specification directly addresses demands from AI accelerator disaggregation, where chipmakers need to combine compute, memory, and I/O dies from multiple sources at maximum bandwidth. The adoption of this standard is expected to accelerate the chiplet ecosystem by enabling multi-vendor integration at wire-level speeds.

## Strategic Observations

- UCIe is now in its third revision within three years, indicating rapid ecosystem pressure
- The 100 mm sideband reach enables multi-chiplet packages that span a full reticle-sized substrate
- AI workloads requiring ever-larger effective die sizes are the primary demand signal
