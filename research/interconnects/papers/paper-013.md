# paper-013: HBM4 Memory Interconnect — 2 TB/s per Stack in 2026 AI Accelerators

**Tags:** chip-to-chip  
**Date:** 2026  
**Source:** Samsung, Micron, OSCOO, Electronic Design  
**URL:** https://www.oscoo.com/news/hbm4-the-memory-revolution-in-the-age-of-ai-computing/

---

## Summary

HBM4 entered mass production in early 2026, with Samsung (February 2026) and Micron (Q1 2026) leading shipments. HBM4 doubles the interface width to 2,048 bits and achieves 2–3.3 TB/s per stack bandwidth, directly enabling AMD MI400 and NVIDIA Rubin performance targets.

## HBM Generation Comparison

| Generation | Interface | Speed/pin | BW/stack | Capacity | Volume |
|---|---|---|---|---|---|
| HBM2e | 1024-bit | 3.6 Gbps | 460 GB/s | 24 GB | 2022 |
| HBM3 | 1024-bit | 6.4 Gbps | 819 GB/s | 24 GB | 2023 |
| HBM3e | 1024-bit | 9.8 Gbps | 1.18 TB/s | 36–48 GB | 2024 |
| HBM4 | 2048-bit | 8.0+ Gbps | 2.0+ TB/s | 36–48 GB | 2026 |
| HBM4 (Samsung) | 2048-bit | 11.7 Gbps | 3.3 TB/s | varies | Feb 2026 |

## HBM4 Technical Innovations

### Interface Width Doubling
- 2,048-bit interface (vs 1,024-bit in HBM3/3e)
- Achieves higher bandwidth at lower per-pin speeds, reducing signal integrity challenges

### Active Base Die
- HBM4 uses an **active logic base die** vs passive interposer in HBM3e
- Logic base die handles address decoding, power management, error correction
- Enables higher density and better thermal management

### New Packaging Requirements
- Requires wider silicon interposer routings (TSMC CoWoS-L or CoWoS-S upgrades)
- Intel EMIB-T with TSVs also supports HBM4 routing density
- SK Hynix 16-Hi HBM4 (48 GB/stack) planned for 2026

## AI Accelerator Adoption Timeline

| Platform | HBM Type | BW/GPU | Volume |
|---|---|---|---|
| NVIDIA GB200/GB300 | HBM3e | ~8 TB/s | 2025 |
| AMD MI350X | HBM3e | ~9 TB/s | 2025 |
| NVIDIA Rubin | HBM4 | 13 TB/s | H2 2026 |
| AMD MI400 | HBM4 | 19.6 TB/s | 2026 |

## Memory Wall Problem

LLM inference KV caches for trillion-parameter models require:
- 80–120+ GB per GPU (exceeding current HBM3e capacity)
- Bandwidth >10 TB/s for real-time token generation
- HBM4 + CXL memory pooling is the combined solution trajectory

## Supply Chain Context

- TSMC CoWoS capacity bottleneck (2025): CoWoS growing at 80% CAGR but demand still outpaces
- NVIDIA secured >70% of TSMC CoWoS capacity in 2025
- Samsung and SK Hynix competing for HBM4 supply contracts with NVIDIA and AMD

## Strategic Observations

- AMD's MI400 leads on memory bandwidth (19.6 TB/s) vs NVIDIA Rubin (13 TB/s) — a reversal from NVLink's scale-up bandwidth advantage
- The active base die in HBM4 enables logic at the memory stack, potentially enabling compute-near-memory for certain operations
- HBM4 packaging requirements make advanced packaging (CoWoS, EMIB) a competitive moat for foundries
