# paper-014: Prefill-Decode Disaggregation — Architecture Shift in LLM Serving

**Tags:** LLM-inference, dataflow, transformer-accelerator  
**Date:** 2025  
**Source:** Groundy Blog, UCSD Hao AI Lab, arXiv 2510.08544  
**URL:** https://arxiv.org/pdf/2510.08544

---

## Summary

Prefill-decode disaggregation has become the **default serving architecture** at every major hyperscaler as of 2025. By running prompt processing (prefill) and token generation (decode) on physically separate hardware pools, operators independently optimize time-to-first-token (TTFT) and inter-token latency (ITL) — metrics that cannot be simultaneously tuned in co-located deployments.

## The Fundamental Problem

LLM inference has two phases with opposing hardware demands:

| Phase | Characteristic | Hardware Demand |
|-------|---------------|-----------------|
| Prefill | Process all input tokens in parallel | Compute-bound (TFLOPS) |
| Decode | Generate 1 token per forward pass | Memory-bandwidth-bound (GB/s) |

Sharing hardware means one phase always runs sub-optimally. A GPU cluster optimized for prefill (compute-heavy) is bandwidth-wasteful during decode. Optimized for decode, it underutilizes compute during prefill.

## Disaggregated Architecture

### Prefill Pool
- Compute-optimized hardware (high FLOPS)
- Processes entire input prompt in one forward pass
- Builds KV-cache for the sequence
- Transfers KV-cache to decode pool upon completion

### Decode Pool
- Memory-bandwidth-optimized hardware (high GB/s)
- Runs autoregressive token generation
- Receives KV-cache from prefill pool
- Can be different hardware (HBM-heavy vs compute-heavy)

### KV-Cache Transfer
The critical operation: transferring KV tensors between pools without bottlenecking latency. Research in 2025 explored:
- NVLink-based transfers within data centers
- CXL pooled memory for shared KV-cache access
- Compression before transfer (46.9% KV-cache size reduction via compression)

## NVIDIA Dynamo (GTC 2025)

NVIDIA's orchestration framework reaching GA with Dynamo 1.0:
- Sits above SGLang, vLLM, TensorRT-LLM
- Handles routing, auto-scaling, KV-transfer coordination
- Routes inference requests to correct pool (prefill vs decode) based on SLOs

## SPAD Paper (arXiv 2510.08544)

"SPAD: Specialized Prefill and Decode Hardware for Disaggregated LLM Inference":
- Proposes custom ASIC designs for each phase
- Prefill ASIC: optimized MXU with high FLOPS/mm²
- Decode ASIC: wide memory bus, minimal compute, maximum bandwidth
- Demonstrates significant area-efficiency gains vs unified GPU design

## Production Performance (SGLang, 96 H100s)

Test on DeepSeek-R1:
- 3 nodes (24 GPUs) for prefill
- 9 nodes (72 GPUs) for decode
- **Result:** 52.3k input tokens/sec + 22.3k output tokens/sec per node

## Framework Support (2025)

All major frameworks added PD disaggregation in 2025:
- vLLM v1 (Jan 2025): FlashInfer integration with PD disagg support
- SGLang: Native PD disaggregation with ROCm support for AMD MI300X
- LMCache, MoonCake: Distributed KV-cache management
- TensorRT-LLM: NVIDIA-optimized disaggregated serving

## Significance

PD disaggregation is not merely an optimization — it represents a fundamental change in how AI inference infrastructure is provisioned and operated. It implies that future accelerator roadmaps should consider separate hardware products for prefill vs decode, as SPAD proposes. This aligns with Ironwood's inference focus, Groq's decode-optimized LPU, and emerging specialized inference ASICs.
