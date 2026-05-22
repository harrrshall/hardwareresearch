# Paper 017: NVIDIA Quantum-X800 InfiniBand Switch Platform — 800G XDR Specifications

**Tags:** AI-cluster, network-topology
**Source:** NVIDIA Networking, NADDOD, Converge Digest
**Date:** 2025
**Relevance:** High

## Platform Overview

The NVIDIA Quantum-X800 is the XDR (Extended Data Rate) generation of InfiniBand switches, providing 800 Gb/s per port — double the NDR (400G) generation. It leverages 200 Gb/s per lane SerDes technology.

## NVIDIA Quantum-X800 Q3400-RA Specifications

| Parameter | Value |
|-----------|-------|
| Port speed | 800 Gb/s per port |
| Total ports | 144 × 800G (OSFP connectors) |
| Aggregate switching bandwidth | 115.2 Tb/s |
| Form factor | 4U |
| Cooling | Air-cooled |
| SerDes technology | 200 Gb/s per lane (4 lanes per port) |
| In-network computing | SHARP v4 |
| Routing | Adaptive routing engine |
| Congestion control | Telemetry-based |
| Unified Fabric Manager | Dedicated port supported |

## Q3200 Compact Variant

| Parameter | Value |
|-----------|-------|
| Configuration | 2 independent switches in 2U |
| Ports per switch | 36 × 800G |
| Total (2 switches) | 72 × 800G |
| Use case | Smaller-scale deployments |

## Scaling Capability

Using two-level fat-tree topology with Q3400-RA:
- **Maximum non-blocking cluster size:** 10,368 × ConnectX-8 NICs
- **GPU cluster equivalent:** ~10,368 dual-port nodes = ~20,736 GPUs
- **Hop count:** 2 (leaf-spine two-level fat-tree)

## SHARP v4 In-Network Computing

SHARP (Scalable Hierarchical Aggregation and Reduction Protocol) v4 performs collective operations (AllReduce, AllGather, Barrier) directly on the switch fabric:
- Eliminates endpoint processing for reductions
- Reduces AllReduce latency by 50–70% for large tensors
- Critical for large-scale LLM training where AllReduce is the dominant communication pattern

## NVLink vs InfiniBand Scope

| Interconnect | Scope | Bandwidth |
|-------------|-------|-----------|
| NVLink 5 (intra-rack) | 72 GPUs, 1 rack | 130 TB/s aggregate |
| Quantum-X800 XDR IB | Up to 20,000+ GPUs | 800 Gb/s per endpoint |
| EFA (AWS Trainium2) | 100,000+ chips | 400 Gb/s per node |
| Google ICI (TPU v7) | 134,000+ TPUs | 9.6 Tb/s per chip |

## Migration Path from NDR (400G) to XDR (800G)

- Quantum-2 (NDR, 400G): 64 ports, 25.6 Tb/s per switch
- Quantum-X800 (XDR, 800G): 144 ports, 115.2 Tb/s per switch
- Bandwidth increase: 4.5× per switch
- Port count increase: 2.25× per switch
- Reduces switch count by ~50% for same-scale deployment

## NVIDIA ConnectX-8 NIC (2025)

- Per-port: 800 Gb/s InfiniBand
- Host interface: PCIe Gen5 ×16
- GPUDirect RDMA: yes (direct GPU memory access over InfiniBand)
- Required for Quantum-X800 deployments

## Deployment in AI Context

800G XDR is the planning baseline for new AI cluster builds in 2025–2026. Existing 400G NDR deployments represent a 2–3 year lifecycle; major hyperscalers are deploying 800G in new builds while supporting existing 400G clusters during their operational life.
