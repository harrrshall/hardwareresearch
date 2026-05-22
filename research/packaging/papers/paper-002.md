# paper-002: TSMC SoIC 3D Stacking Roadmap — Pitch Scaling from 9 μm to 3 μm (2025–2027)

**Tags:** SoIC, TSMC, 3D-stacking, hybrid-bonding, pitch
**Date Range:** 2025-Q4 – 2026-Q1
**Source IDs:** 8, 9, 10, 11, 12

---

## Summary

TSMC's System-on-Integrated-Chips (SoIC) platform is the company's flagship 3D stacking technology, enabling face-to-face or face-to-back die integration using hybrid bonding (bumpless). As of early 2026, TSMC has achieved 6 μm pitch in high-volume manufacturing, with a roadmap to 3 μm by 2027 and 4.5 μm in regular production by 2029.

## Technical Details

**SoIC Variants:**
- **SoIC-X (bumpless, face-to-face):** Uses direct Cu-to-Cu hybrid bonding at 6 μm pitch in HVM as of 2026. Over 1 million interconnects per mm². Eliminates solder bumps entirely.
- **SoIC-P (bump-based):** Uses micro-bumps between dies. F2B configuration in 2025 at 25 μm pitch (N3 top / N4 bottom); F2F at 16 μm pitch planned 2027 (N2 top / N3 bottom).
- **SoIC-mH (Molding Horizontal):** Horizontal mold compound for heat spreading. Used in Apple M5 series (late 2025 / early 2026) to disaggregate CPU and GPU chiplets while managing hotspots.

**Pitch Roadmap:**
| Year | Technology | Pitch |
|------|-----------|-------|
| 2025 | SoIC-X HVM | 9 μm |
| 2026 | SoIC-X HVM | 6 μm |
| 2027 | SoIC-X target | 3 μm |
| 2027 | SoIC-P F2F | 16 μm |
| 2029 | SoIC-X target | 4.5 μm (stable production) |

## Key Findings

1. At 6 μm pitch, SoIC-X achieves >1 M interconnects/mm², compared to ~4,000/mm² for flip-chip microbumps.
2. Apple M5 used SoIC-mH to stack CPU and GPU for M5 Pro/Max, reducing die area penalty vs. monolithic designs.
3. TSMC expects 30+ SoIC designs in production by 2026–2027 across diverse customer portfolios.
4. Fujitsu's Monaka CPU (future server) will utilize SoIC face-to-face stacking.
5. AMD MI300X leverages SoIC at 9 μm TSV pitch for compute-on-IO die stacking.

## Implications

SoIC at sub-5 μm pitch could partially displace HBM for memory-on-logic stacking in select applications. The technology enables 3D chiplet integration without the overhead of individual bump structures, dramatically increasing interconnect density while lowering latency and energy per bit to sub-0.05 pJ/b targets.
