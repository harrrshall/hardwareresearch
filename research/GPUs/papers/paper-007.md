# Paper 007: HBM Memory Evolution — HBM3E to HBM4

**Source ID**: src-011, src-044  
**Tier**: 3 (Industry Analysis + Technical Blog)  
**Date**: 2026-02-01, 2026-04-24  
**URL**: https://www.spheron.network/blog/hbm3e-vs-hbm4-vs-hbm4e-llm-inference-guide/

---

## One-Sentence Claim
HBM4, specified by JEDEC in April 2025 with a doubled 2,048-bit I/O interface delivering 1.5+ TB/s per stack and capacities up to 64GB, will first appear in NVIDIA Rubin and AMD MI400 (both H2 2026), while HBM3E remains the production standard through mid-2026 in H200, B200, and MI350X deployments.

## Methodology Summary
Analysis based on JEDEC HBM4 specification release (April 2025), vendor product announcements, and Siemens EDA IC design guide for HBM4 packaging. Deployment timelines from NVIDIA Rubin and AMD MI400 official announcements. HBM3E current performance from deployed systems (H200 at 4.8 TB/s per GPU, B200 at 8 TB/s per GPU, MI350X at 8 TB/s per GPU).

## Quantitative Results
**HBM3E (current standard)**:
- Per-stack bandwidth: up to 1.2 TB/s
- I/O width: 1,024 bits per stack
- Per-pin speed: up to 9.8 Gb/s
- Deployed: H200 (141GB, 4.8 TB/s total), B200 (192GB, 8 TB/s total), MI350X (288GB, 8 TB/s total), MI325X (256GB, 6 TB/s total)

**HBM4 (2026 generation)**:
- JEDEC spec finalized: April 2025
- Per-stack bandwidth: 1.5+ TB/s
- I/O width: 2,048 bits per stack (doubled from HBM3E)
- Per-pin speed: up to 8 Gb/s (same, but wider interface)
- Stack height: 4–16 dies
- Die density: 24Gb or 32Gb, up to 64GB per stack
- First deployments: NVIDIA Rubin R100 H2 2026, AMD MI400 H2 2026
- AMD MI400 target: 432GB HBM4, 19.6 TB/s total bandwidth
- Micron HBM4 modules: 36GB, 2.3x bandwidth improvement over prior gen

**HBM4E (future)**:
- Projected 2027-2028
- Per-pin rates targeting 10+ Gb/s
- No GPU vendor announcements as of May 2026

## Stated Limitations
- HBM4 supply concentrated at SK Hynix and Samsung; volume ramp critical to GPU availability
- Broader I/O interface increases package complexity and CoWoS interposer area
- Higher bandwidth creates new thermal management challenges for memory stacks
- No GPU product shipping HBM4 as of May 2026; first products H2 2026

## Inferred Limitations
- 19.6 TB/s total bandwidth target (AMD MI400) requires 12-14 HBM4 stacks, expanding package footprint
- HBM4's 64GB max stack capacity lags DRAM improvements, remaining a capacity constraint for very large models
- Double I/O width means larger TSV array in the base logic die, increasing die complexity and power
- Early HBM4 yields and availability likely constrained through 2026, limiting Rubin/MI400 ramp speed

## Architectural Significance
The HBM3E-to-HBM4 transition is the most significant memory bandwidth step in GPU history. Doubling the per-stack I/O from 1,024 to 2,048 bits enables bandwidth scaling without increasing per-pin speed — a more reliable engineering path. For LLM inference, which is fundamentally memory-bandwidth-bound (per src-034), this bandwidth doubling directly translates to inference throughput improvements for memory-bound decode phases. AMD MI400's 19.6 TB/s target vs MI350X's 8 TB/s represents a 2.45x improvement — larger than any prior generational bandwidth jump. The JEDEC standardization (April 2025) is critical: it ensures multi-vendor sourcing (SK Hynix, Samsung, Micron) unlike proprietary alternatives.

## Cross-Paper Connections
- src-006 (Rubin GPU) covers the first GPU platform deploying HBM4
- src-026 (MI400 roadmap) specifies AMD's HBM4 capacity targets
- src-034 (memory bandwidth bottleneck) explains why HBM4 is critical for LLM performance
- src-025 (TSMC CoWoS capacity) shows how interposer capacity constrains HBM deployment

## Theme Tags
`HBM3e`, `HBM4`, `memory-bandwidth`, `GPU-memory`, `JEDEC`, `memory-hierarchy`, `capacity`, `SK-Hynix`, `Micron`, `Samsung`
