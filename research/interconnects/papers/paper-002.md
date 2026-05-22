# paper-002: NVLink 5.0 and NVSwitch in GB200 NVL72 — Rack-Scale GPU Interconnect

**Tags:** NVLink, chip-to-chip  
**Date:** 2025  
**Source:** NVIDIA Official / NADDOD Blog  
**URL:** https://www.nvidia.com/en-us/data-center/gb200-nvl72/

---

## Summary

NVLink 5.0 powers the NVIDIA GB200 NVL72 rack-scale system, delivering the highest total GPU-to-GPU bandwidth ever deployed in a production system. The NVL72 connects 72 Blackwell GPUs into a single non-blocking all-to-all fabric through nine NVLink switch trays, each housing two NVSwitch chips.

## Key Technical Specifications

| Parameter | Value |
|---|---|
| NVLink generation | 5th generation |
| Per-GPU bandwidth | 1,800 GB/s (1.8 TB/s) |
| NVLink links per GPU | 18 links |
| Per-link bandwidth | 100 GB/s bidirectional |
| NVL72 aggregate bandwidth | 130 TB/s |
| Scale to 576 GPUs | 1 PB/s non-blocking |
| NVSwitch SHARP support | Yes — in-network reductions + multicast |

## Architecture Details

The NVL72 is composed of:
- **18 compute trays**: each containing 4 GB200 GPUs + 2 Grace CPUs
- **9 switch trays**: each containing 2 NVLink Switch chips with 144 NVLink ports total
- **No direct GPU-to-GPU links** within a compute tray — all traffic routes through external NVSwitch fabric

This full-mesh external switching architecture ensures every GPU pair can communicate at full 3.6 TB/s aggregate (1.8 TB/s each direction). The approach maximizes uniformity: from a high-speed NVLink perspective, all 72 cards are equivalent.

## NVSwitch Features

- **SHARP (Scalable Hierarchical Aggregation and Reduction Protocol)**: In-network reductions reduce GPU idle time during AllReduce operations
- **Multicast acceleration**: Supports efficient broadcast patterns in distributed training
- **ConnectX-8 NICs**: 800 Gbps XDR InfiniBand for inter-rack scale-out (from mid-2025 deployments)

## Deployment Context

- Microsoft Azure deployed the first supercomputer-scale NVL72 system in October 2025: 4,608 NVIDIA GB300 GPUs linked via NVLink 5
- Stargate project deployed 64,000 GB200 systems beginning March 2025, interconnected by 800 Gbps InfiniBand

## Strategic Observations

- NVIDIA's decision to route all traffic through external NVSwitch eliminates within-tray locality — a deliberate simplification that enables software-transparent scaling
- The 576-GPU non-blocking domain at 1 PB/s represents an unprecedented scale for a single coherent interconnect domain
- Power density for the switch layer requires dedicated cooling; NVLink 6 switch chips require liquid cooling
