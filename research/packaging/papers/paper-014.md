# paper-014: Broadcom 3.5D XDSiP Packaging — World's First 2nm Custom AI SoC in Production

**Tags:** 3.5D, Broadcom, SoIC, CoWoS, AI, chiplet, heterogeneous-integration
**Date Range:** 2026-Q1 – 2026-Q2
**Source IDs:** 54

---

## Summary

Broadcom introduced its 3.5D XDSiP (eXtreme Density System in Package) technology, delivered its first 2nm custom AI SoC to Fujitsu in February 2026, and has five 3.5D products in development. The platform combines TSMC SoIC (3D face-to-face stacking) with CoWoS (2.5D integration), delivering 7x higher die-to-die signal density, 10x lower interface power, and reduced latency through 6,000 mm² silicon integration.

## Technical Details

**XDSiP Architecture:**
- 3D SoIC F2F stacking: compute dies stacked face-to-face using TSMC SoIC process
- 2.5D CoWoS integration: stacked chiplet complex placed on CoWoS organic interposer
- 3D HCB (Hybrid Chip Bridge): Broadcom-proprietary bridge for die-to-die interface optimization

**Performance Claims vs. Traditional Packaging:**
| Metric | Traditional 2.5D | XDSiP 3.5D |
|---|---|---|
| Die-to-die signal density | Baseline | 7x higher |
| Die-to-die power | Baseline | 10x lower |
| Package silicon area | ~3,000 mm² | 6,000 mm² |
| Integration level | Single tier | Two tiers (3D) |

**First Product:**
- Customer: Fujitsu
- Process: TSMC 2nm (N2)
- Packaging: 3.5D XDSiP
- Delivery: February 2026 (first samples)
- Mass production: February 2026 onset

**AI Revenue Context:**
- Broadcom AI revenue Q3 2025: $5.2B (63% YoY growth)
- Custom ASIC segment leading AI packaging demand
- 5+ 3.5D products in development pipeline

## Key Findings

1. Broadcom's 3.5D XDSiP is the first commercially shipped 3.5D (3D+2.5D hybrid) product at 2nm node.
2. 10x die-to-die power reduction validates that eliminating bump parasitics through SoIC F2F bonding has profound energy efficiency impact.
3. 7x die-to-die signal density enables previously impractical disaggregation of large monolithic AI SoC blocks.
4. The 6,000 mm² package size matches the NVIDIA B200 CoWoS-L package, confirming this is the new normal for flagship AI silicon.
5. Fujitsu as first customer signals enterprise HPC / supercomputer market as early 3.5D adopter.

## Implications

XDSiP establishes Broadcom as a credible competitor to AMD and NVIDIA in AI silicon, leveraging packaging innovation rather than leading-edge process alone. The 10x power reduction in die-to-die interfaces directly reduces total chip power — at AI accelerator scale, this could mean 20–30W savings per GPU.
