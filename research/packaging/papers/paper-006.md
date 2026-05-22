# paper-006: HBM4 Packaging Architecture — 12-Hi, 16-Hi Stacking and 2 TB/s per Stack

**Tags:** HBM4, 3D-stacking, memory, JEDEC, SK-Hynix, Samsung, Micron
**Date Range:** 2025-Q2 – 2026-Q2
**Source IDs:** 43, 44, 45, 58

---

## Summary

JEDEC released the official HBM4 specification in April 2025, establishing a new memory architecture with doubled interface width (2048-bit), up to 2.8 TB/s per stack, and 12- to 16-layer die stacks. SK Hynix and Samsung completed 12-Hi pilot runs by late 2025, with Micron entering mass production of 12-Hi HBM4 (36 GB, >2.8 TB/s) in Q1 2026.

## Technical Details

**JEDEC HBM4 Specification (April 2025):**
| Parameter | HBM3e | HBM4 |
|---|---|---|
| Interface width (bits) | 1024 | 2048 |
| Transfer speed (Gb/s/pin) | 9.6 | 8.0 (base) |
| Peak bandwidth/stack | ~1.2 TB/s | 2.0–2.8 TB/s |
| Stack height | Up to 12-Hi | 4–16 Hi |
| Die density | 24 Gb | 24 or 32 Gb |
| Max capacity/stack | 36 GB (12-Hi) | 48 GB (16-Hi) |
| Package thickness | 720 μm | 775 μm (relaxed) |

**Manufacturing:**
- JEDEC relaxed package thickness to 775 μm to enable 12-Hi and future 16-Hi stacks
- Stacking process: MR-MUF (Mass Reflow-Molded Underfill) for SK Hynix; TC-NCF (Thermocompression Non-Conductive Film) alternatives
- 16-Hi may require transition to hybrid bonding for pitch reduction; still under evaluation
- TSV pitch: ~55 μm vertical interconnect

**Supply Landscape:**
- SK Hynix: 12-Hi HBM4 in H2 2025; 16-Hi (48 GB) planned 2026; $13B packaging plant approved Jan 2026
- Samsung: 12-Hi pilot completed late 2025; 4 μm-pitch hybrid bonding for HBM stacking enabled 2026
- Micron: 36 GB 12-Hi HBM4 in mass production Q1 2026; >2.8 TB/s bandwidth per stack

## Key Findings

1. HBM4 doubles bandwidth/stack vs. HBM3e (2 TB/s vs. ~1 TB/s) through 2x interface width, not speed increase.
2. SK Hynix is building a $13B HBM packaging plant — the world's largest — targeting 2027 completion; already configured for HBM4E and HBM5.
3. NVIDIA's Rubin GPU (2026) is expected to adopt HBM4 12-Hi with 8 stacks per GPU.
4. SK Hynix, Samsung, and Micron are all competing for NVIDIA Rubin HBM4 supply contracts.
5. 16-Hi HBM4 (called HBM4E) will offer 48 GB/stack at ~3+ TB/s.

## Implications

HBM4 with 2 TB/s/stack and 8 stacks per GPU delivers ~16 TB/s aggregate memory bandwidth — sufficient for trillion-parameter AI model inference without memory bandwidth bottleneck, at least until model sizes grow further. The $13B SK Hynix plant signals memory packaging is now a capital-intensive strategic asset comparable to logic wafer fabs.
