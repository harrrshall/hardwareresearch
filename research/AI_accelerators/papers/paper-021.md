# paper-021: HBM Memory Supercycle — Supply Crisis and HBM4 Transition

**Tags:** transformer-accelerator  
**Date:** 2025–2026  
**Source:** Tom's Hardware, TrendForce, Introl Blog  
**URL:** https://www.tomshardware.com/tech-industry/artificial-intelligence/samsung-and-sk-hynix-warn-ai-driven-memory-shortages-could-last-until-2027-and-beyond

---

## Summary

The AI compute buildout has triggered a structural HBM memory shortage that both Samsung and SK Hynix warn will persist until 2027 or beyond. Prices surged 171.8% year-over-year in late 2025, with a further 20% increase locked in for 2026 supply contracts. The industry is simultaneously transitioning from HBM3E to HBM4.

## The HBM Crisis

### Demand Drivers
- NVIDIA Blackwell B200/H200: 180 GB HBM3e per GPU
- AMD MI355X: 288 GB HBM3E per GPU
- Google TPU v7 Ironwood: 192 GB HBM3e per chip
- AWS Trainium3: 144 GB HBM3e per chip
- Each new generation requires more HBM per accelerator

### Supply Constraints
- HBM manufacturing requires separate DRAM wafers + Through-Silicon Via (TSV) stacking
- TSV stacking is complex, lower yield than planar DRAM
- Samsung and SK Hynix reallocating up to 40% of advanced wafer capacity to HBM
- This creates commodity DRAM shortage for PC/server/smartphone markets

### Pricing Impact
- Late 2025: +171.8% YoY HBM price surge
- 2026 supply contracts: +20% over 2025 prices
- Goldman Sachs: most severe memory shortage in 15 years
- DRAM supply-demand gap (2026): 4.9% (vs 3.3% projection six months prior)

### Manufacturer Response
| Manufacturer | Investment | Target |
|-------------|------------|--------|
| Samsung | 465.4B KRW in Xi'an (2025, +67.5% YoY) | HBM3E + HBM4 ramp |
| SK Hynix | 581.1B KRW in Wuxi; 440.6B KRW in Dalian | HBM3E dominance |
| Micron | HBM3E entering production | Late entrant |

## HBM Technology Roadmap

### HBM3E (Current Standard, 2024–2026)
- Per stack: up to 36 GB capacity
- Per-stack bandwidth: ~1.2 TB/s
- Used in: B200, H200, MI350X, Trainium3, Ironwood

### HBM4 (Emerging, 2026+)
- NVIDIA Rubin R100: 288 GB HBM4, 22 TB/s per GPU
- Per-stack bandwidth increase: ~50% over HBM3E
- Logic base die: more intelligent memory subsystem
- Samsung began HBM4 shipments (first batches) in May 2026

### HBM4E (Future, 2027+)
- SK Hynix reportedly lagging vs Samsung on HBM4 qualification
- Projected bandwidth: ~2 TB/s per stack
- Critical for post-Rubin NVIDIA architecture

## System Implications

The memory shortage has cascading effects:
1. **AI chip production bottlenecked by HBM availability** — not fab capacity
2. **Price elasticity limited** — hyperscalers must buy regardless of cost
3. **Commodity DRAM shortage** ripples into consumer electronics
4. **HBM4 transition** accelerates to create competitive differentiation

## Market Share in HBM (2025)
- SK Hynix: ~55% of HBM market (dominant in HBM3E premium)
- Samsung: ~35% of HBM market (catching up on HBM4)
- Micron: ~10% (growing)

## Significance

The HBM memory supercycle is a structural constraint on AI infrastructure expansion. The shortage lasting until 2027–2030 means that accelerator performance improvements from better compute (Rubin, Ironwood) may be hampered by memory supply. This is driving exploration of alternative memory architectures (CXL, PIM, on-chip SRAM) as ways to reduce HBM dependency per inference operation.
