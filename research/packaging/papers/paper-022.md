# paper-022: Monolithic 3D IC and Sequential Process — Stanford/SkyWater 3D Chip Demonstration

**Tags:** monolithic-3D, 3D-IC, sequential, research, US-foundry, advanced-packaging
**Date Range:** 2025-Q4 – 2026-Q1
**Source IDs:** 64

---

## Summary

A collaborative team from Stanford, Carnegie Mellon, UPenn, and MIT demonstrated the first monolithic 3D integrated circuit manufactured at a commercial US foundry (SkyWater Technology) in late 2025. The chip integrates carbon nanotube (CNT) transistors for logic and resistive RAM in upper tiers, stacked on conventional CMOS in a single continuous fabrication process — reporting 4x performance improvement over equivalent 2D designs.

## Technical Details

**Monolithic 3D vs. Chiplet 3D:**
| Property | Chiplet 3D (Die Stacking) | Monolithic 3D |
|---|---|---|
| Inter-tier via pitch | 2–100 μm (TSV/hybrid bond) | < 100 nm (MIV) |
| Tier-to-tier process | Post-fab bonding | Sequential wafer fabrication |
| Thermal budget | No constraint (room temp bond) | < 400°C (protect lower tiers) |
| Inter-tier bandwidth | 1–100 M/mm² | >100 M/mm² (approaching on-chip density) |
| Yield | Independent die yield | Single integrated process yield |

**Stanford/SkyWater Demonstration:**
- Upper tier: Carbon Nanotube FETs (CNFETs) for logic
- Lower tier: Conventional CMOS (Si transistors)
- Inter-tier vias: < 100 nm pitch Monolithic Inter-tier Vias (MIVs)
- Memory tier: Resistive RAM (RRAM) integrated in upper back-end layers
- Performance gain: 4x vs. 2D equivalent (claimed)
- Energy-delay product improvement: potential 1000x in future optimized implementations

**Alternative Approach (Beijing Qingwei, 2025):**
- Reconfigurable logic wafer bonded face-to-face with memory wafer
- Hybrid bonding for inter-tier connections
- Data transfer width limited only by bonding area (not I/O pins)

## Key Findings

1. First US foundry production of monolithic 3D with CNT + CMOS is a major milestone for domestic advanced manufacturing.
2. MIV density at < 100 nm pitch is 90–900x denser than hybrid bonding (2–9 μm), enabling near on-chip interconnect density between tiers.
3. Low-thermal-budget process (< 400°C) for upper tiers is the critical enabler — protects underlying CMOS from thermal damage.
4. CNT transistors offer unique properties for upper-tier logic: high carrier mobility, air-stable n-type and p-type variants, sub-1nm body thickness.
5. 4x performance gain is attributed to ~zero-latency inter-tier memory access and 3D routing topologies that reduce average wire length.

## Implications

Monolithic 3D is still pre-production but represents the endpoint of the roadmap: when MIVs approach metal layer density, 3D integration becomes indistinguishable from monolithic chip design. CNT-based upper tiers combined with Si CMOS lower tiers could yield energy-efficiency gains of 10–100x for AI inference workloads dominated by memory access.
