# paper-011: Fan-Out Wafer Level Packaging (FOWLP) — Market Dynamics and Panel Migration

**Tags:** FOWLP, fan-out, panel-level-packaging, FO-PLP, advanced-packaging
**Date Range:** 2025-Q4 – 2026-Q2
**Source IDs:** 19, 20, 46, 47

---

## Summary

Fan-Out Wafer Level Packaging (FOWLP) provides a chip-first, RDL-last approach that eliminates the package substrate entirely, reducing form factor and improving electrical performance. The market was valued at $4.33B in 2025 with projected growth to $10.12B by 2033. NVIDIA accelerated GB200 migration to panel-level fan-out packaging (FO-PLP) to ease CoWoS constraints.

## Technical Details

**FOWLP Technology:**
- Chip-first approach: dies are placed face-down in a mold compound, then RDL layers are patterned on top
- RDL line/space: 5/5 μm (standard FOWLP) to 2/2 μm (advanced FOWLP)
- No package substrate required; I/O balls (BGA) directly on RDL
- Typical package thickness: 0.5–1.2 mm (vs. 1.5–2 mm for flip-chip BGA)

**Fan-Out Panel Level Packaging (FO-PLP):**
- Scales from 300 mm wafer to 515×510 mm rectangular panels (Samsung/ASE) or 600×600 mm (future)
- Panel format: 40% better substrate utilization vs. wafer format for multi-die designs
- Cost reduction: potential 30–40% vs. FOWLP on wafers at scale
- Challenge: die placement accuracy on large panels (warpage, overlay errors)

**2025–2026 Key Events:**
- NVIDIA: Accelerated GB200 migration to panel-level FO for overflow capacity (pulled forward from 2026 to 2025)
- ASE: Invested $200M in 310×310 mm panels for AI chips (July 2025)
- Deca + Arizona State University: First FO-WLP R&D facility in North America announced
- TSMC CoPoS (Chip-on-Panel-on-Substrate): Pilot line completing June 2026; mass production 2028–2029

**Market Breakdown:**
- 2025 market: $4.33B; growing at 11.2% CAGR to $10.12B by 2033
- AI and 5G applications are dominant growth drivers
- PLP market: $0.35B in 2025 → $1.37B by 2031 at 25.58% CAGR

## Key Findings

1. NVIDIA's CoWoS demand overflow creating real adoption of FO-PLP as a viable alternative for mid-tier AI chips.
2. Panel-level packaging delivers 40% better die yield per batch for multi-die layouts vs. wafer-level.
3. Warpage control on panels >500 mm remains the primary technical barrier for high-density products.
4. TSMC's CoPoS pilot completion June 2026 will be a critical data point for panel-level viability at the leading edge.
5. Advanced RDL on panels is approaching 2/2 μm line/space, comparable to package substrates.

## Implications

FO-PLP threatens the ABF organic substrate market for mid-range and mainstream AI chips. As panel processing matures, the cost advantage over silicon interposer-based solutions (CoWoS, H-Cube) could reshape the supply chain for AI chips that don't require the extreme density of hybrid bonding.
