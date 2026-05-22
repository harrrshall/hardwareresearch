# paper-003: CXL 4.0 Specification — 128 GT/s Memory Fabric for Multi-Rack AI

**Tags:** CXL-fabric  
**Date:** 2025-11-18  
**Source:** CXL Consortium / BusinessWire  
**URL:** https://www.businesswire.com/news/home/20251118275848/en/CXL-Consortium-Releases-the-Compute-Express-Link-4.0-Specification-Increasing-Speed-and-Bandwidth

---

## Summary

The CXL Consortium released CXL 4.0 on November 18, 2025, timed with Supercomputing 2025 (SC25). The specification doubles bandwidth over CXL 3.x by adopting the PCIe 7.0 physical layer at 128 GT/s and introduces key features enabling multi-rack memory pooling at unprecedented scale.

## Key Technical Specifications

| Parameter | CXL 3.x | CXL 4.0 |
|---|---|---|
| Signal rate | 64 GT/s (PCIe 6.0) | 128 GT/s (PCIe 7.0) |
| FLIT format | 256-byte | 256-byte (retained) |
| Max retimers | 2 | 4 |
| Native link widths | x1, x2, x4, x8, x16 | + bundled ports (x32, x64) |
| Port bundling | No | Yes — up to 1.5 TB/s |
| Latency vs 3.x | Baseline | Flat (same latency) |

## New Features

### Bundled Ports
Multiple physical links can be bonded into a single logical port, enabling connections delivering up to **1.5 TB/s** aggregate — critical for HBM-class memory expanders.

### Enhanced Memory RAS
- Extended machine check architecture for memory reliability, availability, and serviceability
- Improved error containment for persistent memory scenarios

### Extended Topology Support
- 4 retimers (vs 2 in CXL 3.x) enables building longer rack-to-rack and multi-rack topologies without signal integrity compromise
- Multi-rack disaggregated memory pools become viable at production scale

### CXL Fabric Persistence
CXL 4.0 retains full backward compatibility with CXL 1.x, 2.0, and 3.x devices, enabling gradual migration in deployed infrastructure.

## Use Case: AI Inference KV Cache Offload

Modern LLM inference with billion-parameter models requires 80–120+ GB per GPU for KV caches. CXL 4.0 enables:
- Access to **100+ terabytes of shared memory** with cache coherency across multiple racks
- 4.8x inference throughput improvement (vs RDMA approaches) per CXL Consortium benchmarks
- 82.7% reduction in Time-to-First-Token (TTFT) through local CXL memory access

## Vendor Response

- **Marvell** announced Structera S 30260 (260-lane CXL switch) at OFC 2026, enabling rack-level memory pooling
- **Panmnesia** shipped CXL 3.2 fabric switch supporting up to 4,096 nodes with port-based routing

## Strategic Observations

- CXL 4.0 alignment with PCIe 7.0 tightly couples the two standards' deployment timelines
- Bundled ports enable CXL to compete with proprietary coherent fabrics (NVLink, Infinity Fabric) at raw bandwidth
- Multi-rack memory pooling is the key differentiator for AI inference scaling, separating CXL from simpler memory expansion approaches
