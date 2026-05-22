# Paper 009: imec IGZO 2T0C Capacitorless 3D DRAM — IEDM 2025

**Source ID**: 34, 35  
**Source Title**: imec Disrupting DRAM Roadmap: Capacitorless IGZO DRAM Technology; IEDM 2025 Detailed Report  
**URLs**:  
- https://www.imec-int.com/en/articles/disrupting-dram-roadmap-capacitor-less-igzo-dram-technology  
- https://www.viksnewsletter.com/p/2025-international-electron-devices  
**Date**: 2025-12 (IEDM 2025, San Francisco)  
**Tags**: IEDM2025, IGZO, 3D-DRAM, capacitorless, imec, oxide-semiconductor

---

## One-Sentence Claim
imec presented its 2T0C (two-transistor, zero-capacitor) IGZO DRAM technology at IEDM 2025, demonstrating sub-100nm patterning via reactive ion etch, 1.2V operation at 5-year lifetime reliability (95°C), and integration into a vertical 3D DRAM architecture as a viable capacitor-free pathway.

## Methodology Summary
imec developed a DRAM bit cell using two IGZO (indium-gallium-zinc-oxide) thin-film transistors without a storage capacitor, relying instead on the high resistivity of IGZO to retain charge. The key process innovation is using reactive ion etch (RIE) instead of the traditional ion beam etch (IBE) for patterning the active module, enabling sub-100nm pattern dimensions with minimal damage. 5nm thin IGZO channels are conformally deposited via atomic layer deposition (ALD). The reliability metric of Vov=1.2V for 5-year lifetime at 95°C was demonstrated.

## Quantitative Results
- Bit cell type: 2T0C (two thin-film IGZO transistors, zero capacitor)
- Channel material: IGZO (indium-gallium-zinc-oxide), 5nm thickness via ALD
- Patterning: sub-100nm via RIE (improved over IBE baseline)
- Operating voltage: 1.2V overdrive for 5-year lifetime at 95°C
- Patterning damage reduction vs IBE: quantified improvement (specific dB values proprietary)
- Density potential: stacking multiple layers enables 8-16x density over planar DRAM

## Stated Limitations
- PBTI (positive bias temperature instability) reliability remains a concern; hydrogen anneal partially mitigates
- No capacitor means charge retention depends on IGZO OFF-current — temperature sensitivity is higher than conventional DRAM
- Sub-threshold swing and ON/OFF ratio targets for production-level reliability not yet met
- Technology is on the DRAM roadmap as a "long-term option" (Yole 2024), not near-term production

## Inferred Limitations
- IGZO deposition uniformity at ALD for 5nm channels across high-aspect-ratio 3D structures is extremely challenging at wafer scale
- The 2T0C architecture uses 2x the transistors of a 1T1C DRAM cell, potentially negating density gains unless vertical stacking compensates
- IGZO is an amorphous material; crystallinity control affects carrier mobility and hence device performance

## Architectural Significance
2T0C IGZO DRAM represents a fundamental departure from 60 years of capacitor-based DRAM technology. If manufacturable at scale, it eliminates the capacitor scaling challenge that now limits DRAM bit cell area reduction below ~10nm half-pitch. The ability to deposit IGZO conformally via ALD enables true 3D monolithic DRAM stacking on top of CMOS logic dies, potentially enabling DRAM-on-logic integration without TSVs — a revolutionary packaging paradigm.

## Cross-Paper Connections
- Directly competes with conventional HBM4 (papers 001-003) if it enables DRAM-on-logic at lower cost
- Kioxia's oxide-semiconductor 3D DRAM (paper-010) presented at same IEDM 2025 conference
- 3D DRAM density targets (8-16x) would theoretically exceed HBM4 stack capacities
- Near-memory computing (paper-016) benefits directly from monolithic DRAM-on-logic enabled by 2T0C

## Theme Tags
IGZO, 3D-DRAM, imec, capacitorless, 2T0C, IEDM2025, ALD, oxide-semiconductor, reliability
