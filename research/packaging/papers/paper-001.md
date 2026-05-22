# paper-001: TSMC CoWoS Capacity Expansion — From 35K to 130K Wafers/Month (2024–2026)

**Tags:** CoWoS, TSMC, capacity-expansion, AI, interposer
**Date Range:** 2025-Q4 – 2026-Q2
**Source IDs:** 2, 3, 6, 7

---

## Summary

TSMC's Chip-on-Wafer-on-Substrate (CoWoS) platform has undergone the most aggressive capacity ramp in advanced packaging history. Starting from ~35,000 wafers/month in late 2024, TSMC nearly doubled output to 75,000 wafers/month by end of 2025, with confirmed targets of 120,000–130,000 wafers/month by December 2026 — approximately a 4x increase in under two years.

## Technical Details

**CoWoS-S (Silicon Interposer):**
- Uses a monolithic silicon interposer with Through-Silicon Vias (TSVs)
- Interposer pitch: ~55 μm micro-bump pitch between die and interposer
- Limited to 1–2 reticle sizes (~858 mm²/reticle)
- Used in NVIDIA H100 (5.5-reticle equivalent interposer area)

**CoWoS-L (Local Silicon Interconnect):**
- Uses an organic substrate with embedded Local Silicon Interconnect (LSI) bridges
- Overcomes reticle-size limitation; enables packages up to 5.5–8 reticle sizes currently
- Used in NVIDIA B200 Blackwell: two logic dies + 8 × HBM3e stacks on a single package
- Package size: ~6,000 mm² die area
- Die-to-die bandwidth via LSI bridge: up to 5.76 TB/s aggregate

**Roadmap:**
- Current: 5.5-reticle CoWoS production
- 2027: 8-reticle CoWoS
- 2028: 14-reticle CoWoS (enables 24 HBM5e stacks)
- 2029: 24 HBM stacks target with ~48x compute vs. 2025 baseline

## Key Findings

1. TSMC committed $56 billion in 2026 capex partly to double CoWoS output for NVIDIA's Rubin GPU era.
2. CoWoS wafer ASP is reportedly approaching 7nm wafer pricing, making it a significant profit driver.
3. Despite massive expansion, CoWoS capacity is sold out through 2026; NVIDIA holds priority allocation.
4. CoPoS (Chip-on-Panel-on-Substrate) pilot line completes June 2026; mass production planned 2028–2029.
5. AI wafer demand grew 11x from 2022 to 2026 — CoWoS is the critical enabler.

## Implications

The CoWoS constraint is the single largest bottleneck for AI hardware deployment. The 4x capacity increase will ease but not eliminate the shortage. TSMC's transition toward panel-level formats (CoPoS) signals longer-term effort to break the substrate area cost barrier.
