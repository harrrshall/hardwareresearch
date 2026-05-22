# paper-021: CXL Memory Disaggregation for AI Inference — Benchmark Results 2025

**Tags:** CXL-fabric  
**Date:** 2025  
**Source:** CXL Consortium, Panmnesia, Marvell, Enfabrica  
**URL:** https://computeexpresslink.org/blog/overcoming-the-ai-memory-wall-how-cxl-memory-pooling-powers-the-next-leap-in-scalable-ai-computing-4267/

---

## Summary

Production benchmarks in 2025 demonstrate CXL memory pooling delivering 4.8x inference throughput improvement and 82.7% TTFT reduction for LLM workloads, validating disaggregated memory as a production-viable solution for the AI memory wall problem. Commercial CXL memory pools at 100+ TiB became available in 2025.

## The AI Memory Wall Problem

Modern LLM inference requirements:
- **KV cache for 70B-parameter models**: 40–80 GB per request context
- **KV cache for 1T+ parameter models**: 80–120+ GB per request context
- **Current GPU HBM (2025)**: 96–192 GB per GPU (HBM3e)

The memory wall: inference throughput limited not by compute but by KV cache memory capacity and bandwidth.

## CXL Memory Pooling Benchmark Results

### vs. RDMA Approaches

| Approach | Speedup (vs baseline) |
|---|---|
| 100G RDMA | 1.0x (baseline) |
| 200G RDMA | 3.8x |
| CXL 3.0 pooling | **6.5x** |

### LLM Inference Metrics

| Metric | Baseline | CXL Pooling |
|---|---|---|
| Inference throughput | 1.0x | **4.8x** |
| Time-to-First-Token (TTFT) | 1.0x | **5.5x faster** (82.7% reduction) |
| Memory capacity per GPU | 192 GB | Up to 8x (1.5 TB with CXL pool) |

### Why CXL Outperforms RDMA
- **Cache coherency**: CXL 3.0 hardware-managed MESI coherence eliminates software-managed consistency overhead
- **Latency**: CXL add-in latency ~150–300 ns vs RDMA 1–3 µs
- **CPU transparency**: OS sees CXL memory as NUMA node — no application modification required

## Production Deployments 2025

- **Commercial 100 TiB CXL pools** available from Samsung, SK Hynix, Micron
- Large inference clusters deploying CXL memory expanders for KV cache offload
- Marvell Structera S 30260 (announced OFC 2026): 260-lane CXL switch for rack-level pooling

## CXL Switch Technology Evolution

| Product | Ports/Lanes | Nodes | Protocol | Status |
|---|---|---|---|---|
| Panmnesia Fabric Switch | Up to 4,096 nodes | CXL 3.2 | First silicon (port-based routing) | 2025 |
| Marvell Structera S 30260 | 260 lanes | Rack-scale | CXL 3.x | OFC 2026 announced |
| Next-gen (CXL 4.0) | TBD | Multi-rack | CXL 4.0 (128 GT/s) | 2027+ |

## Memory Pool Architecture

```
[GPU 1] [GPU 2] ... [GPU N]
         |
    [CXL Switch]
         |
[Memory Expander 1] [Memory Expander 2] ... [Memory Expander M]
   (HBM3e/DDR5)         (HBM3e/DDR5)
```

- Live rebalancing: memory slices reassigned without OS-level remapping
- NUMA awareness: OS scheduler allocates workloads to minimize CXL-hop latency
- Fault isolation: memory slice failures contained, no full-system impact

## CXL 4.0 Impact on Memory Pooling

With CXL 4.0 (128 GT/s, bundled ports at 1.5 TB/s):
- Multi-rack memory pools with bandwidth comparable to local PCIe 5.0 channels
- 100+ TB coherent memory pools accessible from thousands of compute nodes
- Target: single memory pool for entire AI cluster inference queue

## Strategic Observations

- CXL's 6.5x speedup over 200G RDMA and cache-coherent hardware model make it the correct architectural choice for disaggregated KV cache
- The 4,096-node CXL fabric from Panmnesia demonstrates that CXL can scale to data-center-wide memory disaggregation
- CXL 4.0's multi-rack reach + bundled ports enables architectures where memory-to-compute ratio is no longer fixed per server
