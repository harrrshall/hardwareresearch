# Paper 002: Samsung HBM4 — 36GB 12-Hi at 3.3 TB/s (ISSCC 2026)

**Source ID**: 5, 6, 8  
**Source Title**: Samsung 36GB HBM4 Delivers 3.3 TB/s Bandwidth; Samsung Begins HBM4 Mass Production; ISSCC 2026 Analysis  
**URLs**:  
- https://windowsreport.com/samsungs-hbm4-delivers-3-3-tb-s-bandwidth-production-ramps-up/  
- https://videocardz.com/newz/samsung-begins-hbm4-mass-production-and-customer-shipments-up-to-3-3-tb-s-per-stack  
- https://newsletter.semianalysis.com/p/isscc-2026-nvidia-and-broadcom-cpo  
**Date**: 2026-02 (ISSCC 2026, February 15–19, San Francisco)  
**Tags**: HBM4, Samsung, ISSCC2026, bandwidth, 3D-stacking, base-die

---

## One-Sentence Claim
Samsung's 12-Hi 36GB HBM4, presented at ISSCC 2026, achieves 3.3 TB/s bandwidth using 13 Gbps per pin on a 2,048-bit interface, built on 1c DRAM dies and an SF4 logic base die, representing a 37.5% improvement over Samsung's initial HBM4 variant.

## Methodology Summary
Samsung used its own 1c (6th-generation 10nm-class) DRAM core die process for the memory layers and its SF4 (Samsung Foundry 4nm-class) node for the logic base die. The 12-Hi stack maintains 36 GB total capacity with 2,048 I/O pins. Samsung presented detailed circuit-level results at the IEEE ISSCC 2026 conference in February 2026.

## Quantitative Results
- Configuration: 12-Hi, 36 GB
- I/O pins: 2,048
- Speed: 13 Gbps per pin (operating), vs. JEDEC HBM4 spec of 8 GT/s minimum
- Bandwidth: 3.3 TB/s per stack (initial Samsung HBM4 was 2.4 TB/s → 37.5% improvement)
- Power efficiency improvement: 40% vs HBM3E
- Thermal resistance improvement: 10% vs HBM3E
- Heat dissipation improvement: 30% vs HBM3E
- Base die: SF4 (Samsung Foundry 4nm-class)
- DRAM process: 1c (6th-gen 10nm-class)

## Stated Limitations
- 12-Hi configuration limits maximum stack capacity to 36 GB vs. SK Hynix's 16-Hi at 48 GB
- SF4 base die is manufactured on Samsung's own foundry, which has faced yield challenges
- Samsung entered HBM4 mass production later than SK Hynix

## Inferred Limitations
- Samsung's in-house SF4 base die fabrication faces foundry yield competition from TSMC
- The thermal improvement (10% resistance, 30% dissipation) suggests thermal management remains a binding constraint at high pin counts
- 2,048 IO at 13 Gbps implies 26.624 TB/s of total raw signaling per stack, requiring exceptional signal integrity design

## Architectural Significance
Samsung's choice to use its SF4 foundry node for the HBM4 base die is strategically significant — it provides cost and supply chain independence from TSMC but requires Samsung Foundry's 4nm technology to mature. The 13 Gbps pin speed exceeds the JEDEC 8 GT/s minimum by 62.5%, showing that actual product shipping specs are decoupled from the conservative JEDEC floor. The 40% power efficiency gain is critical for reducing data center power budgets.

## Cross-Paper Connections
- Competes directly with SK Hynix HBM4 (paper-001) which uses TSMC 12nm base die
- Samsung supplies Google TPU HBM (60%+ TPU v5 supply) and NVIDIA Vera Rubin HBM4
- NVIDIA Vera Rubin (paper-007) lists Samsung as one of three qualified HBM4 suppliers
- HBM4E roadmap (paper-017) will extend Samsung's 36 GB 12-Hi to 48 GB 16-Hi at 4 TB/s
- Samsung's 1c DRAM process also used for LPDDR6 (paper-004) and GDDR7 products

## Theme Tags
HBM4, Samsung, ISSCC2026, bandwidth, 3.3TB/s, base-die, SF4, 1c-node, thermal
