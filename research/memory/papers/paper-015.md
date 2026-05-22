# Paper 015: DDR6 Standard — JEDEC Timeline and Industry Roadmap

**Source ID**: 38, 39  
**Source Title**: DDR6 Explained: Speeds, Architecture & Release Date; Samsung/Micron/SK Hynix DDR6 Plans  
**URLs**:  
- https://intuitionlabs.ai/articles/ddr6-explained-speed-architecture  
- https://www.guru3d.com/story/samsung-micron-sk-hynix-ddr6-development-plans-arrives-in-2027-with-s-speeds/  
**Date**: 2025-12  
**Tags**: DDR6, JEDEC, timeline, specifications, 2027

---

## One-Sentence Claim
JEDEC's DDR6 specification is expected to be formally published in Q4 2025–Q1 2026, with enterprise server modules in late 2025–2026 and consumer desktop deployment in 2027, targeting 8,800–17,600 MT/s speeds from all three major DRAM vendors.

## Methodology Summary
Based on industry reports of JEDEC committee progress. LPDDR6 was published first (July 2025, JESD209-6), with DDR6 JESD79-6 following. Platform validation by Intel and AMD planned for 2026. Consumer DDR6 modules delayed from previously expected late 2025 to 2027.

## Quantitative Results
- Speed range: 8,800 MT/s (DDR6-8800) to 17,600 MT/s (DDR6-17600) per JEDEC spec
- JEDEC ratification: Q4 2025–Q1 2026
- Enterprise server priority access: 2026
- Consumer commercial deployment: 2027
- Comparison: DDR5 tops out at ~8,800 MT/s (OC); DDR6 baseline matches DDR5 OC ceiling
- LPDDR6 published first (July 2025) as first DDR6-era standard

## Stated Limitations
- Consumer DDR6 availability pushed to 2027, later than previously expected
- Platform validation by CPU vendors (Intel, AMD) required before commercial rollout
- DDR6 channel width and other architectural changes may require PCB layout changes

## Inferred Limitations
- DDR6 at 17,600 MT/s represents a theoretical ceiling; first products will likely start at 8,800-12,800 MT/s
- Server adoption will be slower than mobile due to certification requirements; HBM4 dominates server memory bandwidth regardless
- Memory controller complexity increases with DDR6's advanced signaling (PAM4 potential)

## Architectural Significance
DDR6 is the mainstream desktop/laptop successor to DDR5 and is significant for workstations, client AI PCs, and non-HBM server segments. The fact that LPDDR6 was standardized before DDR6 reflects the industry's prioritization of mobile/AI-PC as the leading-edge market. DDR6's 17,600 MT/s ceiling represents a ~2x improvement over current DDR5-8800, which is important for CPU-bound AI inference on consumer hardware.

## Cross-Paper Connections
- LPDDR6 (paper-004) was standardized first in July 2025; DDR6 follows
- DDR6 on Intel/AMD platforms will use the TSMC N2 SRAM advances (paper-006) in memory controllers
- For data center AI, HBM4 (papers 001-003) remains the relevant memory standard; DDR6 fills the CPU-attached tier

## Theme Tags
DDR6, JEDEC, JESD79-6, timeline, 17600MT/s, consumer, enterprise, 2027
