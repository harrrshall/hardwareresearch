# paper-009: AMD Infinity Fabric 4 and MI350 Series Interconnect Architecture

**Tags:** chip-to-chip  
**Date:** 2025  
**Source:** AMD, Hot Chips 2025, SemiAnalysis  
**URL:** https://www.amd.com/en/blogs/2025/engineering-the-future-of-ai.html

---

## Summary

AMD's MI350 series (2025) adopts 4th Generation Infinity Fabric with a fully redesigned interconnect topology providing 5.5 TB/s bi-sectional bandwidth and 1,075 GB/s GPU-to-GPU aggregate bandwidth. The MI400 (2026) will scale to 19.6 TB/s using HBM4 and is expected to incorporate UALink-based scale-up connectivity.

## Infinity Fabric Generations

| Generation | Product | Bandwidth |
|---|---|---|
| Gen 1–2 | MI50/MI100 | 100–200 GB/s |
| Gen 3 | MI200, MI250 | 800 GB/s |
| Gen 3 (enhanced) | MI300X | 896 GB/s |
| Gen 4 | MI350, MI355X | 1,075 GB/s GPU-GPU |

## MI350/MI355X Interconnect Specifications

| Parameter | Value |
|---|---|
| Scale-up links | 7 × Gen4 Infinity Fabric links |
| GPU-to-GPU bandwidth | 1,075 GB/s bidirectional aggregate |
| Die interconnect (AP) | Infinity Fabric Advanced Package |
| AP bi-sectional bandwidth | **5.5 TB/s** |
| Host interface | PCIe 5.0 via embedded switch |

### Architecture Notes
- Fewer dies vs MI300X allows wider Infinity Fabric AP bus between I/O chiplets → lower operating voltage → lower energy per bit
- CDNA 4 architecture: TSMC 3nm, 185 billion transistors
- 288 GB HBM3e memory; 19.6 TB/s target for MI400 with HBM4

## Hot Chips 2025 Presentation

AMD presented Infinity Fabric improvements at Hot Chips 2025 (August 2025), highlighting:
- Redesigned topology for MI350 reducing per-bit energy at the same bandwidth
- Advanced Package interconnect with 5.5 TB/s connecting two chiplet complexes
- Compatibility with future UALink integration

## MI400 (2026) Preview

From SemiAnalysis and AMD roadmap leaks:
| Parameter | MI350X | MI400 |
|---|---|---|
| Process | 3nm CDNA 4 | 3nm CDNA 5 (est.) |
| FP4 performance | ~30 PFLOPS | 40 PFLOPS |
| HBM type | HBM3e | HBM4 |
| Memory | 288 GB | 432 GB |
| Memory BW | ~9 TB/s | 19.6 TB/s |
| Scale-out per GPU | ~200 GB/s | 300 GB/s |

## Comparison: AMD vs NVIDIA Scale-Up Bandwidth (2025)

| GPU | Scale-Up BW | Memory BW | Process |
|---|---|---|---|
| GB200 | 1,800 GB/s (NVLink 5) | ~8 TB/s (HBM3e) | TSMC 4nm |
| MI350X | 1,075 GB/s (IF4) | ~9 TB/s (HBM3e) | TSMC 3nm |
| Rubin (2026) | 3,600 GB/s (NVLink 6) | 13 TB/s (HBM4) | TSMC 3nm |
| MI400 (2026) | TBD (UALink?) | 19.6 TB/s (HBM4) | TSMC 3nm |

## Strategic Observations

- AMD's MI400 HBM4 memory bandwidth (19.6 TB/s) will significantly exceed NVIDIA Rubin's 13 TB/s in this dimension
- Infinity Fabric 4 Gen's AP interconnect at 5.5 TB/s positions AMD to benefit from chiplet disaggregation at very high internal bandwidth
- UALink adoption by AMD in MI400/MI500 would establish AMD as the reference implementer of the open scale-up standard
