# Paper 015: AMD MI400 CDNA5 Architecture and 2026 Roadmap

**Source ID**: src-026, src-040  
**Tier**: 3 (Industry Analysis)  
**Date**: 2025-12-01  
**URL**: https://www.guru3d.com/story/amd-instinct-mi400-launches-in-2026-with-cdna-5-architecture/

---

## One-Sentence Claim
AMD Instinct MI400 series (CDNA5, H2 2026) doubles MI350's compute to 40 PFLOPs FP4, upgrades to 432GB HBM4 at 19.6 TB/s bandwidth, introduces a new 300 GB/s scale-out link, and uses CoWoS-L packaging — targeting a 10x performance frontier model improvement to compete with NVIDIA Rubin.

## Methodology Summary
AMD confirmed MI400 roadmap at MI350 launch (June 2025) and subsequent investor events. Specifications disclosed progressively: HBM4 capacity and bandwidth at June 2025 launch event, full product lineup (MI455X, MI430X) at later announcements. Wccftech and Tweaktown coverage from official AMD disclosures. AMD also confirmed MI500 series for 2027.

## Quantitative Results
- **Target launch**: H2 2026
- **Architecture**: CDNA5
- **Compute (FP4)**: 40 PFLOPs (2x MI350's 9.2 PFLOPs per GPU, scaled to system)
- **Compute (FP8)**: 20 PFLOPs
- **Memory**: 432GB HBM4 (up from MI350X's 288GB HBM3E)
- **Memory bandwidth**: 19.6 TB/s (up from MI350X's 8 TB/s — 2.45x improvement)
- **Scale-out link**: 300 GB/s (new, vs. MI350's 7x Gen4 links at 1,075 GBps aggregate)
- **Packaging**: CoWoS-L (replacing MI350's CoWoS-S approach)
- **MI455X**: Training/cloud focus
- **MI430X**: HPC/government focus with native FP64 processing units
- **MI500 timeline**: 2027 with "1000x" performance claim over time
- **Process**: Expected TSMC 3nm or 2nm derivative for CDNA5

## Stated Limitations
- MI400 specifications are vendor projections; final products may differ
- HBM4 supply constraints could delay or reduce MI400 availability
- 19.6 TB/s bandwidth requires 12-14 HBM4 stacks — large package footprint
- "1000x" MI500 claim is multi-generational, not single-generation

## Inferred Limitations
- 19.6 TB/s MI400 vs. estimated 3+ TB/s per stack × 8-12 stacks for Rubin suggests competitive parity rather than clear AMD lead
- CDNA5 software stack (ROCm 8?) needs to mature concurrently with hardware launch
- CoWoS-L availability for 432GB HBM4 packages requires TSMC capacity beyond what's allocated for MI350/GB300
- MI430X FP64 capability for HPC may limit peak FP4/FP8 performance vs. MI455X

## Architectural Significance
MI400 is AMD's response to NVIDIA's Rubin scheduled for the same H2 2026 window. The 2.45x bandwidth improvement (8 → 19.6 TB/s) would be the largest generational memory bandwidth jump in AMD Instinct history and would directly address the memory bottleneck identified in src-034. The 300 GB/s scale-out link is a new architectural addition, improving MI400 multi-node scaling beyond the existing Infinity Fabric approach. The CoWoS-L transition from CoWoS-S reflects a packaging architecture upgrade AMD needs to accommodate the larger HBM4 package footprint. If delivered, MI400 would represent AMD's strongest challenge to NVIDIA datacenter GPU dominance.

## Cross-Paper Connections
- src-007 (HBM4) covers the memory technology MI400 depends on
- src-002 (MI350X) establishes the baseline MI400 improves upon
- src-006 (Rubin) covers the NVIDIA competitor targeting same H2 2026 window
- src-025 (TSMC CoWoS) explains packaging constraints on MI400 ramp
- src-040 (AMD roadmap) provides broader context including MI500 in 2027

## Theme Tags
`MI400`, `CDNA5`, `HBM4`, `AMD-Instinct`, `roadmap`, `2026`, `scale-out`, `CoWoS-L`, `FP4`, `competitive-analysis`
