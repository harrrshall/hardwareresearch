# paper-003: Cerebras WSE-3 — Wafer-Scale Engine Performance and Architecture

**Tags:** transformer-accelerator, LLM-inference, wafer-scale  
**Date:** 2025  
**Source:** Cerebras Press Releases, Hot Chips 2024, arXiv 2503.11698  
**URL:** https://www.cerebras.ai/press-release/cerebras-announces-third-generation-wafer-scale-engine

---

## Summary

The **WSE-3** is Cerebras Systems' third-generation wafer-scale AI chip, containing 4 trillion transistors on a full 300mm TSMC 5nm wafer. It delivers 125 petaFLOPS of peak AI performance and holds 44 GB of on-chip SRAM with 21 PB/s internal bandwidth — 7,000x the memory bandwidth of an NVIDIA H100.

## Architecture

- **Wafer Die:** Full 300mm TSMC 5nm wafer — the largest chip ever manufactured
- **Transistors:** 4 trillion
- **AI Cores:** 900,000 AI-optimized compute cores
- **On-chip SRAM:** 44 GB with 21 PB/s internal fabric bandwidth
- **Peak Performance:** 125 PFLOPS AI inference
- **System Power:** 25 kW for full CS-3 system

## Why Wafer Scale Works for AI

The WSE-3 eliminates the off-chip memory bottleneck that limits conventional GPU clusters. All weights for moderately-sized models reside in 44 GB of SRAM, enabling data reuse without external memory accesses. The fabric bandwidth of 21 PB/s vastly exceeds anything achievable with HBM stacks.

## Inference Performance

- **Llama 4 Maverick (400B params):** 2,500 tokens/sec per user — more than 2x DGX B200
- AWS integration: 5x more high-speed token capacity in same hardware footprint
- The per-user token rate advantage is particularly pronounced on large-parameter MoE models

## Business Validation

- Meta partnership; six datacenter deployments in early 2025
- Customers: Mayo Clinic, Department of Defense, and others
- 2025 revenue: $510M (vs. $237.8M net income — swing from $481.6M net loss in 2024)
- Valuation: $8.1B
- Cerebras IPO completed early 2026 after restructuring investor base for U.S. federal security review

## Comparison vs arXiv Study (2503.11698)

The peer-reviewed comparison found WSE-3 outperforms GPU-based systems on compute-per-watt for inference workloads that fit within the 44 GB SRAM footprint. For larger models, multi-chip GPU clusters using HBM remain more flexible.

## Key Numbers

| Metric | WSE-3 |
|--------|-------|
| Transistors | 4 trillion |
| AI Cores | 900,000 |
| On-chip SRAM | 44 GB |
| Fabric Bandwidth | 21 PB/s |
| Peak Performance | 125 PFLOPS |
| Process Node | TSMC 5nm |
| Llama 4 Maverick tokens/sec/user | 2,500 |

## Significance

WSE-3 proves that the wafer-scale approach can achieve commercial viability. Its unique architecture eliminates the memory wall for models that fit its SRAM footprint, making it particularly competitive for high-user-count inference deployments at low latency.
