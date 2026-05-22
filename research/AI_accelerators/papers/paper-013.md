# paper-013: HPIM — Heterogeneous Processing-In-Memory for LLM Inference (arXiv 2509.12993)

**Tags:** analog-AI, LLM-inference, systolic-array  
**Date:** September 2025  
**Source:** arXiv cs.AR  
**URL:** https://arxiv.org/abs/2509.12993

---

## Summary

HPIM (Heterogeneous Processing-In-Memory) is the first memory-centric heterogeneous PIM accelerator integrating both SRAM-PIM and HBM-PIM subsystems for LLM inference. It achieves a peak speedup of **34.3x** over NVIDIA A100 by co-optimizing compute placement at multiple memory tiers.

## Motivation

The fundamental challenge for LLM inference is the **arithmetic intensity bottleneck**:
- Prefill (prompt processing): ~2 FLOPs/byte — barely rooflined
- Decode (generation): ~0.2 FLOPs/byte — severely memory-bandwidth-bound

Conventional approaches move data from memory to compute. PIM inverts this: move compute to memory.

## Architecture Design

### SRAM-PIM Subsystem
- Processing elements embedded within on-chip SRAM banks
- Handles compute-bound operations: attention score computation, large dense layers
- High bandwidth due to proximity to SRAM arrays
- Targets prefill-phase operations

### HBM-PIM Subsystem  
- Processing elements embedded within HBM stack's DRAM banks
- Handles memory-bandwidth-bound operations: weight loading for decode phase
- Samsung HBM-PIM architecture provides the hardware foundation
- Targets decode-phase autoregressive token generation

### Heterogeneous Routing
A compiler analyzes each LLM operator and routes to either SRAM-PIM or HBM-PIM based on arithmetic intensity. The paper demonstrates that this heterogeneous routing is essential — using only one PIM type leaves performance on the table.

## Performance Results

| Comparison | Speedup |
|-----------|---------|
| vs NVIDIA A100 (peak) | 34.3x |
| vs A100 on memory-bound decode | 40x+ |
| vs A100 on compute-bound prefill | 8-12x |

Energy reduction: >70% vs A100 across full inference pipeline.

## Samsung HBM-PIM as Hardware Basis

Samsung's production HBM-PIM delivers:
- 2.5x system performance gain in Xilinx Alveo tests
- >60% energy consumption reduction
- SK Hynix disclosed 2025 patents for PIM targeting KV-cache attention operations within HBM banks

## Implications for LLM Serving

The paper identifies three key bottlenecks HPIM addresses:
1. **Weight loading (decode):** HBM-PIM handles weight reads without DRAM→compute data movement
2. **KV-cache access:** HBM-PIM processes attention over cached KV pairs in-situ
3. **Activation computation:** SRAM-PIM handles fast activation function evaluation

## Limitations

- SRAM-PIM capacity is small (hundreds MB); large models still require HBM tier
- HBM-PIM precision currently limited to INT8/INT16 for most commercial implementations
- Compiler complexity is high; model partitioning across PIM tiers is non-trivial

## Significance

HPIM's 34.3x speedup over A100 represents the most dramatic LLM inference performance claim in the research window. It validates the PIM thesis for the memory-bound decode phase specifically, and the heterogeneous approach addresses a key limitation of single-tier PIM designs. Commercial PIM for LLM inference appears 2-3 years away at production scale.
