# paper-009: Hybrid Systolic Array Accelerator for Edge LLM Inference (arXiv 2507.09010)

**Tags:** systolic-array, LLM-inference, NPU  
**Date:** July 2025  
**Source:** arXiv cs.AR  
**URL:** https://arxiv.org/abs/2507.09010

---

## Summary

This paper proposes a novel edge LLM inference accelerator featuring a **Hybrid Systolic Array (HSA)** architecture that independently optimizes the prefill and decode stages through configurable hardware. It achieves 247/117 token/s/mm² for 1.3B LLM on long-input/long-output scenarios — a 2.45x–13.5x improvement over prior approaches.

## Problem Statement

LLM inference has two computationally distinct phases:
- **Prefill:** Compute-intensive, parallelizable across all input tokens (matrix-matrix multiply)
- **Decode:** Memory-bandwidth-bound, sequential token generation (matrix-vector multiply)

Conventional systolic arrays optimize for one but not both. This creates fundamental under-utilization in at least one phase.

## Proposed Architecture: Hybrid Systolic Array (HSA)

### Dual Operating Modes

The HSA reconfigures at runtime:

1. **Prefill Mode:** Conventional 2D systolic array processing for dense GEMM; high core utilization for compute-bound operations

2. **Decode Mode:** Vector unit array configuration for memory-bandwidth-bound matrix-vector operations; skips unnecessary dot products for better decode throughput

### MXINT4 Quantization Integration

- Weight quantization to MXINT4 (MX block floating-point INT4) format
- Optimized dequantization dataflow ensures negligible overhead
- 100% hardware utilization with minimal accuracy loss
- Targets edge DRAM bandwidth constraints effectively

### Key Innovation

The paper demonstrates that the systolic and vector-unit array architectures can be **runtime-configurable**, enabling a single piece of silicon to efficiently handle both Transformer attention/MLP prefill and autoregressive decode generation.

## Performance Results

| Scenario | Performance | Improvement vs prior |
|----------|-------------|----------------------|
| Long input, long output | 247 token/s/mm² | 2.45x |
| Short input, long output | 117 token/s/mm² | 13.5x |
| Energy efficiency | — | Superior to all evaluated prior work |

## Hybrid Mamba-Transformer Support

The architecture also supports hybrid LLMs that interleave SSM (State Space Model) blocks with attention blocks — the paper describes runtime reconfiguration for Mamba layers using different systolic patterns.

## Significance

This work demonstrates that the next generation of edge AI accelerators can overcome the longstanding prefill/decode dichotomy. The reconfigurable systolic approach may influence NPU designs in mobile SoCs (Snapdragon, Apple Silicon, MediaTek) where a single chip must handle both prefill efficiency and decode throughput.
