# paper-016: Mixture-of-Experts Hardware Acceleration — Sparse Inference at Scale

**Tags:** sparsity, LLM-inference, dataflow  
**Date:** 2025  
**Source:** Introl Blog, arXiv MoE papers, vLLM/TensorRT-LLM documentation  
**URL:** https://intuitionlabs.ai/articles/llm-inference-hardware-enterprise-guide

---

## Summary

Mixture-of-Experts (MoE) has become the dominant architecture for frontier LLMs in 2025, with over 60% of open-source model releases using MoE. This creates new hardware requirements: efficient expert routing, heterogeneous memory placement, and sparse activation dispatch.

## MoE Architecture Mechanics

### Expert Routing
Each input token is routed to a fixed subset of "expert" FFN blocks (typically 2-8 out of 64-128 experts). A gating network determines which experts activate.

### DeepSeek-V3 as Reference Point
- **Total Parameters:** 671 billion
- **Active Parameters per Token:** 37 billion (~5.5% of total)
- **Architecture:** MoE replacing dense FFN layers in transformer
- **Performance:** GPT-4 equivalent at fraction of compute cost

## Hardware Challenges

### 1. Expert Placement Problem
671B parameters cannot fit in a single GPU's HBM. Experts must be distributed across chips:
- Hot experts (frequently activated): keep in HBM
- Cold experts (rarely activated): store in CPU DRAM or DDR
- Expert migration between memory tiers during inference

### 2. Load Imbalance
Some experts activate far more frequently than others. Hardware must handle burst demand on popular experts without starvation of rare expert access.

### 3. KV-Cache Amplification
Each active expert has its own activations. The KV-cache grows proportionally to expert count, not just to token count.

### 4. Router Overhead
The gating network adds compute overhead. For 128 experts, the router softmax over expert logits is non-trivial.

## Hardware Memory Architecture Solutions

### GPU-Based (Dominant 2025 Solution)
- Active experts in HBM (fast tier)
- Inactive experts offloaded to CPU DRAM
- CPU-GPU PCIe bandwidth (64 GB/s) is the critical constraint for large expert counts
- vLLM and TensorRT-LLM added MoE-specific offloading in 2025

### SambaNova Three-Tier Memory
- Hot experts: on-chip SRAM
- Warm experts: HBM
- Cold experts: DDR DRAM
- Purpose-designed for exactly this MoE memory tiering problem

### IBM AIMC for MoE
- Analog in-memory computing naturally matches MoE structure
- Only active experts' analog crossbars are interrogated per token
- Demonstrates efficiency advantages specific to sparse activation patterns

## Framework Optimizations (2025)

**vLLM v1 (January 2025):**
- FlashInfer integration with autotuning for MoE kernels
- Expert-parallel scheduling
- MoE-aware KV-cache management

**TensorRT-LLM:**
- Fused MoE kernels for NVIDIA Blackwell FP8
- Expert-parallel tensor parallelism
- Top-K routing optimization for Blackwell Sparse Tensor Cores

## Performance Economics

| Model Type | Total Params | Active Params | Effective Compute Reduction |
|------------|-------------|---------------|---------------------------|
| Dense GPT-4 class | ~1T | 1T | 1x |
| DeepSeek-V3 MoE | 671B | 37B | 18x |
| GPT-MoE-1.8T (NVIDIA) | 1.8T | ~200B | 9x |

## Hardware Efficiency for MoE

Hardware evolution favors MoE economics: each accelerator generation improves memory bandwidth faster than compute TFLOPS, directly benefiting the memory-bound nature of expert weight loading.

Specific advantage by chip:
- Groq LPU: on-chip SRAM stores active expert weights at full bandwidth
- Cerebras WSE-3: all experts in 44GB SRAM if total active set fits
- SambaNova SN40L/SN50: explicit three-tier memory designed for expert placement

## Significance

MoE has created a new class of hardware requirement: efficient sparse dispatch. Traditional dense matrix accelerators waste cycles activating inactive expert paths. The most efficient MoE accelerators will be those that can load and execute only the activated expert parameters with minimal overhead — pointing toward SRAM-heavy, dataflow-oriented designs.
