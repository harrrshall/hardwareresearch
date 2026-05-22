# Paper 001: SK Hynix HBM4 — 16-Hi 48GB at 11.7 Gbps / 2 TB/s

**Source ID**: 3, 4  
**Source Title**: SK Hynix Completes Development of Next-Gen HBM4; SK Hynix Shows 16-Layer 48GB at CES 2026  
**URLs**:  
- https://www.tomshardware.com/pc-components/dram/sk-hynix-completes-development-of-hbm4-2-048-bit-interface-and-10-gt-s-speeds-promised  
- https://www.techpowerup.com/344834/sk-hynix-shows-16-layer-48-gb-hbm4-memory-modules-at-ces-2026  
**Date**: 2025-11 / 2026-01  
**Tags**: HBM4, SK-Hynix, 3D-stacking, bandwidth, AI-accelerator

---

## One-Sentence Claim
SK Hynix's HBM4 doubles the memory interface width to 2,048 bits and achieves 10–11.7 Gbps per pin, yielding up to 2 TB/s bandwidth per stack from 16-Hi 48GB configurations at CES 2026.

## Methodology Summary
SK Hynix utilized TSMC's 12nm logic process for the HBM4 base die, enabling a 32-channel architecture. The DRAM die layers use their proprietary 1c-nm (1-gamma equivalent) process. The 16-Hi stack uses thermal compression bonding (TCB) as the current primary interconnect method.

## Quantitative Results
- Interface width: 2,048 bits (doubled from HBM3E's 1,024 bits)
- Data transfer rate: 10 GT/s (JEDEC spec), achieved 11.7 Gbps in demonstrations
- Bandwidth per stack: 2 TB/s (16-Hi), 1.28 TB/s baseline (12-Hi standard)
- Capacity: 48 GB (16-Hi), 36 GB (12-Hi initial production)
- Power efficiency improvement: >40% vs HBM3E at equivalent bandwidth
- Number of independent channels: 32 (doubled from 16 in HBM3E)
- Base die fabrication: TSMC 12nm process

## Stated Limitations
- 16-Hi stacking increases thermal resistance and requires advanced cooling solutions
- TCB (Thermal Compression Bonding) is current process; hybrid bonding planned for HBM4E
- TSMC 12nm base die is fabricated externally, adding supply chain complexity
- Physical height of 16-Hi stack may require modified socket and PCB designs

## Inferred Limitations
- At 11.7 Gbps per pin, signal integrity across 2,048 bits is a significant engineering challenge
- 16-layer stacking yields and defect rates are not publicly disclosed
- Thermal management at >450W GPU power envelopes with dense HBM4 stacks is unsolved at scale
- Transition from 12-Hi (2025) to 16-Hi (2026) production introduces yield risks

## Architectural Significance
The doubling of the HBM interface width from 1,024 to 2,048 bits is the most significant architectural change to HBM since the standard's introduction in 2015. This change, combined with the shift to 32 independent channels, directly addresses the bandwidth wall confronting large transformer model inference. The base die logic process separation (TSMC 12nm vs. in-house DRAM for DRAM stacks) enables co-optimization of I/O circuits independently of DRAM process.

## Cross-Paper Connections
- Directly enables NVIDIA Vera Rubin NVL72 (paper-007) which requires 288 GB HBM4 per GPU
- AMD MI400 (paper-008) uses same HBM4 generation but 12 stacks vs Vera Rubin's 8
- Competes with Samsung's 36GB HBM4 (paper-002) which achieves 3.3 TB/s via higher pin speed
- Hybrid bonding adoption (paper-012) will be required for HBM4E to extend to 4 TB/s
- SOCAMM2 (paper-013) is the complementary LPDDR solution for CPU-side memory in same AI platforms

## Theme Tags
HBM4, SK-Hynix, 3D-stacking, bandwidth, AI-accelerator, 16-Hi, base-die, TSMC-12nm
