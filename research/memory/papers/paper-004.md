# Paper 004: JEDEC LPDDR6 Standard (JESD209-6) — July 2025

**Source ID**: 15, 16, 17, 18  
**Source Title**: JEDEC Releases New LPDDR6 Standard; Samsung LPDDR6 10.7 Gbps; SK Hynix 14.4 Gbps LPDDR6  
**URLs**:  
- https://www.jedec.org/news/pressreleases/jedec%C2%AE-releases-new-lpddr6-standard-enhance-mobile-and-ai-memory-performance  
- https://www.trendforce.com/news/2025/11/10/news-samsung-lpddr6-memory-specs-unveiled-10-7gbps-speed-on-12nm-reportedly-eyes-14-gbps/  
**Date**: 2025-07-09 (JEDEC publication); products announced Nov 2025 – Jan 2026  
**Tags**: LPDDR6, JEDEC, mobile, AI-edge, JESD209-6

---

## One-Sentence Claim
JEDEC published the LPDDR6 standard (JESD209-6) on July 9, 2025, defining 10,667 MT/s to 14,400 MT/s rates with dual sub-channel architecture, on-die ECC, and dynamic voltage scaling — the first DDR6-era standard to be finalized, ahead of DDR6 itself.

## Methodology Summary
JEDEC's JC-42 committee finalized JESD209-6 after multi-year development. Samsung demonstrated 10.7 Gbps LPDDR6 on a 12nm process with 21% energy efficiency improvement over LPDDR5X. SK Hynix presented 16Gb LPDDR6 at 14.4 Gbps on its 1c process at ISSCC 2026. Samsung sent LPDDR6X samples to Qualcomm for SoC validation.

## Quantitative Results
- Base data rate range: 10,667 MT/s to 14,400 MT/s (equivalent to 10.7 Gbps to 14.4 Gbps per pin)
- Device density: 4 Gb to 64 Gb per die
- Architecture: dual sub-channel, 12 DQ lines per sub-channel
- Access granularity: 32 bytes
- Samsung implementation: 10.7 Gbps on 12nm, 21% better energy efficiency vs LPDDR5X
- SK Hynix: 16 Gb at 14.4 Gbps on 1c process
- Power: lower VDD2 supply vs LPDDR5; DVFSL reduces voltage at low frequency
- Security: CA parity, MBIST, programmable link protection, on-die ECC

## Stated Limitations
- Samsung targets 10.7 Gbps initially; 14 Gbps is a future target not yet in production
- No explicit latency improvements stated vs LPDDR5X
- Standard was just finalized; ecosystem validation (Qualcomm, MediaTek SoC qualification) ongoing

## Inferred Limitations
- Mobile adoption depends on SoC integration validation by Qualcomm and MediaTek — typically 12-18 months from standard publication to shipping devices
- 64 Gb density represents theoretical ceiling; practical products likely 16-32 Gb per die in 2026
- Power savings may not hold in sustained high-bandwidth scenarios where sub-channel activation is high

## Architectural Significance
LPDDR6 is architecturally significant as it extends the LPDDR family into the AI-edge era with native PIM roadmap support (JEDEC also previewed LPDDR6-PIM). The dual sub-channel with 12 DQ lines represents a structural change from LPDDR5's 16 DQ per channel, optimized for mixed-workload access patterns. The 14,400 MT/s ceiling matches enterprise CXL expectations for low-power tiers.

## Cross-Paper Connections
- LPDDR6-PIM collaboration between Samsung and SK Hynix (paper-014) builds on this standard
- SOCAMM2 form factor (paper-013) uses LPDDR5X today but will transition to LPDDR6
- DDR6 standard (paper-015) is the desktop/server counterpart; LPDDR6 was standardized first
- SK Hynix presented LPDDR6 alongside GDDR7 and HBM4 at ISSCC 2026 (paper-007 ecosystem)

## Theme Tags
LPDDR6, JEDEC, JESD209-6, mobile, AI-edge, dual-sub-channel, on-die-ECC, PIM-roadmap
