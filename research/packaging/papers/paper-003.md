# paper-003: Hybrid Bonding Physics and Process — From 10 μm to Sub-Micron Pitch

**Tags:** hybrid-bonding, direct-bonding, interconnect, imec, pitch, copper
**Date Range:** 2025-Q1 – 2026-Q1
**Source IDs:** 13, 14, 15, 16, 17, 18, 48, 49

---

## Summary

Hybrid bonding (Cu/dielectric direct bonding) has become the defining advanced packaging process for 3D integration below 10 μm pitch. Unlike conventional flip-chip micro-bumps that require solder joints and 40 μm+ pitch, hybrid bonding joins Cu pads and SiO₂/SiCN dielectric surfaces simultaneously at room temperature (then annealed), enabling interconnect pitches below 1 μm in research settings and 2 μm in die-to-wafer (D2W) demonstrations.

## Technical Details

**Process Flow:**
1. Chemical mechanical planarization (CMP) to achieve surface roughness < 0.3 nm Ra
2. Plasma activation of bonding surfaces (SiO₂ or SiCN dielectric)
3. Room-temperature pre-bonding via van der Waals forces
4. Anneal (200–400°C) to form covalent Si-O-Si bonds + Cu-Cu diffusion bonds
5. Cu expansion during anneal fills any recess gap (~5–10 nm)

**Pitch Achievements:**
| Organization | Configuration | Pitch | Year |
|---|---|---|---|
| imec | W2W hybrid bonding | 400 nm | IEDM 2023 |
| imec | W2W hybrid bonding | 250 nm (feasibility) | VLSI 2025 |
| imec | D2W Cu/SiCN | 2 μm | 2025 |
| TSMC SoIC-X | D2W HVM | 6 μm | 2026 |
| AMD MI300X | SoIC via TSMC | 9 μm TSV pitch | 2024–2025 |

**Overlay Requirement:**
- imec D2W demonstration: < 350 nm overlay error at 2 μm pitch
- Through-dielectric vias (TDV) at 120 nm pitch demonstrated on wafer backside

## Key Findings

1. Copper grain structure engineering is critical for yield: columnar grain structure reduces void formation during anneal at >300°C.
2. Yole Group projects hybrid bonding equipment market to grow at 21% CAGR from 2025–2030.
3. IEEE Hybrid Bonding Symposium 2025 (imec-hosted) highlighted sub-2 μm as the current industry frontier.
4. NanoIC/imec released first-ever fine-pitch RDL and D2W hybrid bonding PDKs in March 2026, opening broader access to the process.
5. Sub-micrometer bonding enables CMOS 2.0 compute architectures with functional tier stacking within a single SoC.

## Implications

Hybrid bonding at 2–6 μm pitch delivers >100x the interconnect density of flip-chip. This fundamentally alters memory subsystem design — instead of relying on HBM stacked beside the processor, hybrid-bonded SRAM or DRAM can be stacked directly atop logic, reducing latency from ~100 ns (HBM off-chip) to < 5 ns.
