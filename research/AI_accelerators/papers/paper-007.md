# paper-007: Groq LPU — Deterministic Architecture for Ultra-Low Latency Inference

**Tags:** LLM-inference, dataflow, transformer-accelerator  
**Date:** 2025–2026  
**Source:** Groq Official, arXiv 2408.07326, Voiceflow Blog  
**URL:** https://groq.com/lpu-architecture

---

## Summary

Groq's **Language Processing Unit (LPU)** is a purpose-built inference accelerator that achieves ultra-low latency through deterministic static scheduling and massive on-chip SRAM. A landmark deal in December 2025 saw NVIDIA license Groq's LPU architecture for approximately $20 billion (non-exclusive), validating its significance.

## Core Architectural Principles

### 1. Programmable Assembly Line
Data moves along "conveyor belts" — SIMD function units with fixed scheduling. There are no dynamic schedulers, caches, or branch predictors. Execution is entirely determined at compile time by the compiler.

### 2. On-Chip SRAM as Primary Storage
LPU integrates hundreds of MB of SRAM as primary weight storage (not cache). This eliminates the HBM latency penalty that limits GPU-based inference, where weights must be read from external HBM on every forward pass.

### 3. Compiler-Driven Static Scheduling
Groq's software-first approach: the compiler knows exactly when every instruction executes, when data arrives, and when chips communicate. No runtime overhead.

### 4. Plesiosynchronous Multi-Chip Protocol (LPU v2)
Groq developed a protocol that cancels natural clock drift between chips, allowing hundreds of LPUs to act as a single logical core. All inter-chip communication latency is pre-computed by the compiler.

### 5. Process: Samsung 4nm (LPU v2)

## NVIDIA Licensing Deal (December 24, 2025)

- **Value:** ~$20 billion non-exclusive license
- **Scope:** Groq's LPU inference architecture
- **Personnel:** Groq founder Jonathan Ross and president Sunny Madra joined NVIDIA
- **Integration:** Groq 3 LPU integrated into NVIDIA's Vera Rubin platform alongside GPUs
- **Significance:** Validates LPU's deterministic approach as a complement to GPU computing

## Performance Metrics

- **Energy Efficiency:** 20+ TOPS/W (vs 5-10 for NVIDIA H100)
- **Power reduction:** 50-70% energy savings; 1/10th the energy usage in specific benchmarks
- **Latency:** Sub-millisecond time-to-first-token for many models
- **arXiv paper:** System achieves highest tokens/sec per user among all evaluated accelerators for inference

## Architecture vs GPU Comparison

| Aspect | Groq LPU | NVIDIA GPU |
|--------|----------|------------|
| Scheduling | Static (compiler) | Dynamic (hardware) |
| Weight storage | On-chip SRAM | External HBM |
| Cache hierarchy | None | L1/L2/L3 |
| TOPS/W | 20+ | 5–10 |
| Programmability | Inference-focused | General purpose |
| Context switching | Not supported | Supported |

## Limitations

- Cannot be repurposed for training workloads
- Model must be compiled ahead of time (no dynamic batching without recompilation)
- Context window limited by on-chip SRAM
- Ecosystem significantly smaller than NVIDIA CUDA

## Significance

The NVIDIA licensing deal is transformational: it incorporates LPU's deterministic execution philosophy into the world's dominant AI compute platform, and legitimizes the architectural principle that inference requires fundamentally different hardware from training.
