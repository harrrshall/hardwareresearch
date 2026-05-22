# Paper 006: UCIe 3.0 Specification — Doubling Chiplet Interconnect Bandwidth

**Source ID:** 19, 20  
**Authors:** UCIe Consortium  
**Venue:** UCIe Consortium Release / Semiwiki  
**Date:** August 2025  
**Tags:** yield (packaging ecosystem quality)  
**URL:** https://www.uciexpress.org/post/ucie-3-0-specification-redefining-chiplet-interconnects

## Abstract / Summary

The UCIe Consortium released the UCIe 3.0 specification on August 5, 2025, representing the fourth major revision of the open chiplet interconnect standard. UCIe 3.0 doubles peak link speed from 32 GT/s (UCIe 2.0) to 48 and 64 GT/s, while adding runtime power management, manageability features, and support for streaming protocols critical for AI chiplet configurations.

## Key Technical Data

- **Release date:** August 5, 2025
- **Peak link speed:** 48 GT/s and 64 GT/s (vs. 32 GT/s in UCIe 2.0)
- **Bandwidth improvement:** ~2x over UCIe 2.0
- **New features:** Continuous transmission (Raw Mode), runtime recalibration, L2 Optimization
- **Raw Mode application:** Uninterrupted data flow for SoC-to-DSP chiplet connections
- **Power efficiency:** Idle power reduction via sideband optimization
- **Version history:** 1.0 (2022) → 1.1 (2023) → 2.0 (Aug 2024) → 3.0 (Aug 2025)
- **Process compatibility:** Node-agnostic; works across TSMC N2, Intel 18A, Samsung SF2

## Key Findings

1. UCIe 3.0's 64 GT/s link speed approaches on-package interconnect performance necessary for AI accelerators with 100+ TB/s aggregate bandwidth requirements.
2. Runtime recalibration enables adaptive link tuning during chip operation — critical for thermal variation in 3D AI stacks.
3. Raw Mode support enables low-latency chiplet communication for time-sensitive AI inference pipelines.
4. UCIe 3.0 is foundry-neutral, but aligns with TSMC CoWoS-L and Intel EMIB physical implementations.
5. 2025-2026 industry focus is on pre-silicon and post-silicon UCIe verification for first products using 3.0.

## Relevance to Research Window (2025-11-22 to 2026-05-22)

UCIe 3.0 released August 2025 (just before window start); first product implementations and verification activities fall within the window. ISSCC 2026 (Feb 2026) featured UCIe-related chiplet integration papers.
