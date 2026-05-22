# paper-009: Die-to-Die Bandwidth Density — UCIe 2.0 and Beyond 20 Tbps/mm

**Tags:** UCIe, chiplet, bandwidth, die-to-die, heterogeneous-integration
**Date Range:** 2025-Q1 – 2026-Q2
**Source IDs:** 27, 28, 41, 42, 66

---

## Summary

The UCIe (Universal Chiplet Interconnect Express) standard has become the dominant open standard for die-to-die communication in chiplet packages. UCIe 2.0 (2025) introduces a manageability layer, 64 Gbps PHY speed target, and optical interconnect options. Alphawave Semi's Gen3 UCIe IP achieves >20 Tbps/mm bandwidth density; ISSCC 2026 demonstrated implementations reaching 17.9 Tb/s/mm² in 3D packages.

## Technical Details

**UCIe 1.x vs. 2.0:**
| Feature | UCIe 1.0/1.1 | UCIe 2.0 |
|---|---|---|
| PHY speed | 16 / 32 Gbps | 64 Gbps |
| Bandwidth density (advanced) | 188–1,350 GB/s/mm² | Target >4 TB/s/mm² (3D) |
| Optical die-to-die | No | Yes (optional) |
| Manageability layer | No | Yes (dedicated control plane) |
| Security features | Basic | Enhanced |

**Demonstrated Implementations (2025–2026):**
- Alphawave Semi Gen3 UCIe at 64 Gbps: >20 Tbps/mm bandwidth density
- Marvell ultra-high bandwidth: >50 Tbps/mm at <0.1 pJ/bit (die-to-die)
- ISSCC 2026 paper: 17.9 Tb/s/mm² at 16 Gb/s PAM-4 in 5/6nm FinFET on 9 μm pitch 3D package, 10.24 Tb/s aggregate bandwidth
- UCIe-3D (3D bonded variant): 4 TB/s/mm² at 9 μm bump pitch

**Competing Standards:**
- BOW (Bunch of Wires) v1.0 released January 2025: BoW Memory and BoW Flexi variants
- AIB (Advanced Interface Bus): Intel proprietary, widely licensed
- UCIe Consortium: 120+ members as of 2025

**Optical UCIe:**
- World's first UCIe optical interconnect chiplet: unveiled OFC 2025, achieves 8 Tbps bandwidth
- NVIDIA Quantum-X (H2 2025): 1.6T silicon photonics CPO chip

## Key Findings

1. UCIe 2.0's 64 Gbps PHY enables >20 Tbps/mm bandwidth density, reducing the bandwidth gap between die-to-die and on-chip interconnects.
2. Power efficiency targets: from 0.25 pJ/b (current) to <0.05 pJ/b (future UCIe 3D).
3. Intel's "Chiplet Alliance" (March 2025) aims at interoperable and secure chiplet implementation standards beyond UCIe's protocol layer.
4. Optical UCIe at 8 Tbps per chiplet represents a 100x leap over electrical die-to-die in raw bandwidth capacity.
5. UCIe 3.0 roadmap is already being drafted, targeting sub-1 pJ/b at 128 Gbps PHY.

## Implications

The convergence of hybrid bonding (density) and UCIe 2.0 (standardized high-speed protocol) enables a true open chiplet marketplace — any chiplet from any foundry can interoperate in a single package. This is the foundation of the "chiplet economy," threatening monolithic SoC designs at the high end.
