# paper-023: Advanced Packaging Yield and Reliability — Known-Good Die, Warpage, and Lifetime Testing

**Tags:** yield, reliability, advanced-packaging, KGD, warpage, ECTC
**Date Range:** 2025-Q1 – 2025-Q4
**Source IDs:** 36, 40

---

## Summary

Yield and reliability of advanced packages remain critical barriers to cost competitiveness. ECTC 2025 (IEEE 75th, Dallas) featured 400 technical papers across 36 sessions, with significant focus on yield improvement through known-good die (KGD) selection, warpage control for large packages, and long-term reliability of hybrid bonded interconnects. The 2025 TechInsights Advanced Packaging Outlook identifies capacity limitations and yield challenges as the two primary industry constraints.

## Technical Details

**Yield by Technology (2025 Estimates):**
| Technology | Assembly Yield | Notes |
|---|---|---|
| Mature flip-chip (FCBGA) | 98–99% | High-volume, well-established |
| CoWoS-S (standard) | 95–97% | TSMC mature process |
| CoWoS-L (new) | 90–93% | Larger package, more integration points |
| SoIC-X 6 μm hybrid bonding | 88–92% | Early HVM, improving |
| 3D stacked multi-chiplet | 82–88% | Aggregate of per-die yields |
| HBM4 12-Hi stack | 90–93% | KGD selection critical |

**Known-Good Die (KGD) Testing:**
- Wafer-level burn-in and functional testing before singulation
- Cost: $50–200 per die depending on test complexity
- Yield improvement: Reduces assembled package defect rate from 10–15% (no KGD) to 2–3%
- Required for any 3D package with > 4 dies to achieve economic viability

**Warpage Challenges:**
- Large packages (> 2,000 mm²) are susceptible to warpage during reflow (above glass transition Tg of organic substrate)
- CoWoS-L package warpage: target < 100 μm across 6,000 mm² package
- Warpage at reflow peak (260°C): up to 300–400 μm for non-optimized designs
- Mitigation: stiffeners, thermoset mold compounds, substrate core material optimization

**Hybrid Bonding Reliability:**
- Cu-Cu bonds pass JEDEC moisture sensitivity level (MSL) 1 test
- 1,000-cycle thermal shock (-55°C to +125°C): < 1% resistance increase at 6 μm pitch
- Primary failure mode at < 5 μm pitch: Cu oxidation during pre-bond surface preparation

## Key Findings

1. ECTC 2025 was the largest electronics packaging conference in its 75-year history — 400 papers, 2,000+ attendees from 20+ countries.
2. KGD testing economics become compelling above 6-chiplet assemblies; critical for 12-chiplet MI300X economics.
3. Warpage is now the primary physical design constraint for packages > 4,000 mm².
4. Hybrid bonding reliability at 6 μm has passed standard qualification thresholds — production confidence is established.
5. Advanced packaging defect density per unit area is ~10x higher than monolithic SoC at equivalent technology node.

## Implications

Yield and reliability considerations add 15–25% to advanced packaging cost beyond raw process cost. As chiplet count per package grows (AMD MI300X: 12 dies; Intel roadmap: 16 compute + 24 HBM), cumulative yield becomes the economic constraint. The industry is converging on KGD + wafer-level pre-qualification as the standard protocol for heterogeneous integration.
