# Paper 004: NVLink 5.0 and NVLink Fusion Ecosystem

**Source ID**: src-006, src-022, src-023, src-043  
**Tier**: 3/4 (Industry Analysis + Vendor Disclosure)  
**Date**: 2025-05-19 (NVLink Fusion), 2025-09-18 (Intel deal)  
**URL**: https://www.nvidia.com/en-us/data-center/nvlink-fusion/

---

## One-Sentence Claim
NVLink 5.0 doubles GPU interconnect bandwidth to 1,800 GB/s per GPU for Blackwell, while NVLink Fusion (Computex 2025) opens NVLink connectivity to third-party CPUs and ASICs via a chiplet licensing model — with NVLink 6.0 at 3,600 GB/s already announced for Rubin (2026).

## Methodology Summary
NVIDIA published technical specifications for NVLink 5.0 with Blackwell product launches. NVLink Fusion was announced at Computex 2025. The Intel partnership was announced separately in September 2025. Bandwidth figures are from NVIDIA official documentation and validated by NVLink Switch hardware deployed in NVL72 systems. NVLink 6.0 figures announced at CES 2026 for Rubin platform.

## Quantitative Results
- **NVLink 5.0 per-GPU bandwidth**: 1,800 GB/s bidirectional (18 links × 100 GB/s each)
- **vs. NVLink 4.0 (Hopper)**: 2x improvement (from 900 GB/s)
- **vs. PCIe Gen5**: >14x more bandwidth
- **GB200 NVL72 system bandwidth**: 130 TB/s aggregate
- **Max NVLink 5.0 domain**: 576 GPUs in non-blocking fabric
- **NVLink 6.0 (Rubin)**: 3,600 GB/s per GPU (2x over 5.0)
- **Vera Rubin NVL72 rack bandwidth**: 260 TB/s (2x over GB200 NVL72's 130 TB/s)
- **NVLink C2C (GB10)**: 600 GB/s bidirectional chip-to-chip
- **NVLink Fusion chiplet**: Implements NVLink 5 for integration into third-party designs
- **Intel $5B investment**: NVIDIA invests $5B in Intel; Intel commits to NVLink for x86-CPU NVL72-style racks
- **Marvell investment**: NVIDIA invests $2B in Marvell for NVLink Fusion partnership

## Stated Limitations
- NVLink Fusion does not license the full NVLink IP; third parties must integrate NVIDIA's chiplet
- Intel and AMD are explicitly not NVLink Fusion partners; they back UALink instead
- NVLink's 576-GPU domain, while large, is smaller than UALink's 1,024-accelerator spec
- Scale-out (between racks) still relies on InfiniBand or Ethernet, not NVLink

## Inferred Limitations
- NVLink chiplet integration requirement means third-party designs cannot build NVLink without NVIDIA's IP/supply
- Intel's NVLink commitment while also backing UALink suggests hedging rather than full commitment
- UALink hardware availability expected late 2026, giving NVLink Fusion an 18+ month head start
- High bandwidth comes with high pin counts and complex power delivery to the NVLink fabric

## Architectural Significance
NVLink 5.0 at 1.8 TB/s represents the architectural backbone that makes the NVL72 rack behave as a single 1.4 exaflops compute device. Without NVLink bandwidth exceeding HBM bandwidth, all-to-all communication patterns for trillion-parameter models would be bandwidth-bottlenecked at the interconnect. NVLink Fusion's ecosystem strategy is a significant competitive moat expansion: by allowing third-party CPU makers (Fujitsu, Qualcomm, and now Intel) to attach via NVLink, NVIDIA extends its ecosystem without fully opening the standard. The 2x per-generation NVLink bandwidth doubling tracks with memory bandwidth doubling, maintaining the interconnect-to-HBM balance.

## Cross-Paper Connections
- src-009 (Rubin GPU) covers NVLink 6.0 doubling to 3,600 GB/s
- src-024 (UALink 1.0) covers the open-standard competitive response
- src-001 (GB200 performance) relies on NVLink 5.0 for rack-scale coherency
- src-027 (Vera CPU) covers NVLink C2C integration in the Vera Rubin superchip

## Theme Tags
`NVLink`, `NVLink-5.0`, `NVLink-Fusion`, `interconnect`, `GPU-interconnect`, `bandwidth`, `ecosystem`, `UALink`, `scale-up`
