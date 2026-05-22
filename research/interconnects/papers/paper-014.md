# paper-014: AWS Trainium3 UltraServer — NeuronLink Scale-Up Interconnect

**Tags:** chip-to-chip  
**Date:** 2025-12  
**Source:** AWS / HPCwire  
**URL:** https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/

---

## Summary

AWS launched Trainium3 UltraServers in December 2025, delivering a proprietary NeuronLinkv4 interconnect that doubles inter-chip bandwidth compared to Trainium2. The UltraServer configuration scales to 144 Trainium3 chips with 706 TB/s aggregate memory bandwidth — a unique custom-silicon approach to AI training infrastructure.

## Trainium3 Chip Specifications

| Parameter | Trainium2 | Trainium3 |
|---|---|---|
| FP8 compute | ~1.0 PFLOPS | 2.52 PFLOPS |
| Memory | 96 GB HBM2e | 144 GB HBM3e |
| Memory bandwidth | ~2.9 TB/s | 4.9 TB/s |
| NeuronLink | v3 | v4 |
| PCIe lanes (NeuronLink) | ~100 | 160 (144 active + 16 redundant) |

## NeuronLinkv4 Interconnect

| Parameter | Value |
|---|---|
| Technology | PCIe-based NeuronLink |
| Total PCIe lanes | 160 per chip |
| Active lanes | 144 |
| Redundant lanes | 16 (fault tolerance) |
| Medium | Backplane + board-to-board |
| Bandwidth improvement | 2x vs Trainium2 (NeuronLinkv3) |

NeuronLinkv4 uses PCIe lanes as the physical fabric, avoiding custom SerDes development. This approach:
- Leverages PCIe ecosystem silicon reliability
- Trades ultimate bandwidth for broad compatibility and lower development risk
- Enables cost-effective scale-out beyond what NVIDIA's NVLink price point allows

## Trn3 UltraServer Configuration

| Parameter | Value |
|---|---|
| Max chips per UltraServer | 144 Trainium3 |
| Aggregate HBM3e | 20.7 TB |
| Aggregate memory bandwidth | **706 TB/s** |
| Aggregate FP8 compute | 362 PFLOPS |
| Interconnect fabric | NeuronSwitch-v1 (all-to-all) |

The **NeuronSwitch-v1** provides all-to-all fabric connectivity across all 144 chips, enabling efficient AllReduce-class collective operations required for LLM training.

## Trainium4 (Upcoming)

AWS teased Trainium4 at the December 2025 announcement:
- 6x FP4 throughput improvement vs Trainium3
- 3x FP8 performance
- 4x more memory bandwidth
- Estimated availability: 2026–2027

## Competitive Context

| System | GPU Count | Aggregate Mem BW | Fabric |
|---|---|---|---|
| NVIDIA GB200 NVL72 | 72 GPUs | ~576 TB/s | NVLink 5 |
| AMD 8-GPU node | 8 GPUs | ~72 TB/s | IF4 |
| Trainium3 UltraServer | 144 chips | **706 TB/s** | NeuronLinkv4 |

The 706 TB/s aggregate memory bandwidth from 144 Trainium3 chips exceeds the GB200 NVL72's ~576 TB/s, though per-chip compute density favors NVIDIA.

## Strategic Observations

- AWS's PCIe-based NeuronLink trades per-link bandwidth for ecosystem cost benefits — a deliberate decision reflecting AWS's need to deploy at scale economically
- The 144-chip UltraServer footprint (vs 72 GPUs in NVL72) enables denser training clusters with lower per-chip cost
- Trainium4's 4x memory bandwidth target suggests convergence with HBM4-class performance
- AWS custom silicon strategy reduces dependence on NVIDIA pricing leverage
