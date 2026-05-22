# paper-011: Google Ironwood TPU v7 — 9.6 Tbps ICI and Multi-Die Architecture

**Tags:** chip-to-chip  
**Date:** 2025  
**Source:** Google Cloud Blog / ServeTheHome Hot Chips 2025  
**URL:** https://cloud.google.com/blog/products/compute/inside-the-ironwood-tpu-codesigned-ai-stack

---

## Summary

Google's Ironwood (TPU v7) is the first Google TPU with a multi-chiplet architecture — two compute dies per chip — and introduces the highest per-chip inter-chip interconnect bandwidth of any Google TPU generation, at 9.6 Tbps. A 9,216-chip Ironwood superpod scales to 1.77 PB of shared HBM.

## Key ICI Specifications

| Parameter | Trillium (v6) | Ironwood (v7) |
|---|---|---|
| ICI links | 6 | 4 |
| ICI aggregate bandwidth | ~4.8 Tbps | **9.6 Tbps** |
| Per-chip bandwidth | 600 GB/s | **1.2 TB/s** |
| Topology | 3D Torus | 3D Torus (enhanced) |
| Memory type | HBM2e | HBM3+ |
| Chiplet architecture | No | Yes — 2 compute dies |

## Multi-Die Architecture (Hot Chips 2025)

Ironwood marks Google's first transition from monolithic TPU die to multi-chiplet design:
- Two Ironwood compute chiplets per chip
- Die-to-die interconnect within package (likely UCIe-compatible or proprietary)
- Enables scaling beyond single reticle limits
- Hot Chips 2025 presentation highlighted UCIe optical I/O retimer chiplet possibilities for future generations

## Superpod Architecture

| Scale | Configuration | Total HBM |
|---|---|---|
| 1 chip | 2 compute dies | ~192 GB |
| 1 cube | 64 chips | ~12 TB |
| Superpod | 9,216 chips | **1.77 PB** |

The 3D Torus topology provides:
- All-to-all connectivity within a cube via direct ICI links
- Cube-to-cube connectivity through pod-level switching infrastructure
- "Functions as a unified supercomputer" at superpod scale

## ICI Technical Details

ICI bandwidth of 9.6 Tbps:
- 4 links × 2.4 Tbps per link
- Bidirectional (1.2 TB/s = 9.6 Tbps / 8 bits per byte)
- Short-reach die-to-die connections within and between chips
- Latency target: single-digit nanoseconds for within-cube communication

## Comparison: Custom TPU vs GPU Scale-Up BW

| Chip | Scale-Up BW | Memory BW | Pod Scale |
|---|---|---|---|
| Ironwood v7 | 1.2 TB/s ICI | ~8 TB/s | 9,216 chips |
| GB200 | 1.8 TB/s NVLink | ~8 TB/s HBM3e | 576 GPUs |
| Rubin (2026) | 3.6 TB/s NVLink | 13 TB/s HBM4 | TBD |

## Strategic Observations

- Ironwood's superpod architecture (9,216 chips) dramatically outscales NVSwitch's 576-GPU domain
- The 1.77 PB shared HBM across a superpod enables inference model serving that would require dozens of NVL72 racks otherwise
- Google's move to multi-die Ironwood mirrors AMD and Intel's chiplet strategies, driven by reticle limit constraints
- Future generations likely to incorporate photonic I/O for inter-cube scaling
