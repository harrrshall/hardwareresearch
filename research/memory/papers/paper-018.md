# Paper 018: The Memory Wall — LLM Inference is Memory Bandwidth-Bound

**Source ID**: 24, 55  
**Source Title**: AI Memory Bottleneck as Main LLM Inference Challenge; Memory Wall Bottleneck AI Compute Sparks Memory Supercycle  
**URLs**:  
- https://winbuzzer.com/2026/01/26/memory-bottleneck-llm-inference-hardware-challenge-xcxwbn/  
- https://www.trendforce.com/insights/memory-wall  
**Date**: 2026-01; 2025-2026  
**Tags**: memory-wall, LLM, inference, bandwidth-bound, AI, bottleneck

---

## One-Sentence Claim
LLM autoregressive inference is fundamentally memory bandwidth-bound — a 70B parameter FP16 model requires loading ~140 GB of weights per token on an H100 SXM5 at 3.35 TB/s peak, resulting in ~42ms latency per token from memory transfer alone, while GPU FLOPS have grown 80x vs. bandwidth only 17x over the 2012–2022 decade.

## Methodology Summary
Analysis based on arithmetic intensity calculations for autoregressive LLM decoding. For a 70B parameter FP16 model: 70B × 2 bytes = 140 GB per forward pass. At H100 SXM5's 3.35 TB/s peak bandwidth, memory transfer = 140 GB / 3.35 TB/s ≈ 42ms lower bound per token. GPU compute FLOPS scaling: 80x from 2012-2022. Memory bandwidth scaling: 17x over same period.

## Quantitative Results
- 70B model FP16 weight size: ~140 GB
- H100 SXM5 peak bandwidth: 3.35 TB/s
- Theoretical minimum token latency from memory: ~42 ms
- GPU FLOPS growth 2012-2022: 80x
- Memory bandwidth growth 2012-2022: 17x
- Memory bandwidth/FLOPS ratio divergence: ~4.7x widening over a decade
- HBM demand growth 2025: 130%+ YoY
- HBM demand forecast 2026: 70%+ YoY growth

## Stated Limitations
- 42ms is a lower bound; actual latency includes compute, memory controller, NVLink, and software overhead
- Batch inference partially amortizes memory bandwidth requirements
- Quantization (FP8, FP4, INT4) reduces model size and bandwidth requirements

## Inferred Limitations
- Bandwidth-bound analysis assumes sequential decode; parallel prefill phases are compute-bound
- Speculative decoding, KV cache compression, and FlashAttention partially mitigate the bandwidth wall
- The 80x vs 17x divergence is a historical trend; HBM4's 2x bandwidth vs HBM3E may narrow the gap temporarily

## Architectural Significance
The memory wall analysis provides the quantitative foundation for understanding why HBM4's 2 TB/s per stack represents a genuine architectural necessity rather than a marketing improvement. It also explains why AMD designed MI400 with 432 GB HBM4 capacity (more weights in-package = fewer bandwidth bottlenecks for large models) and why CXL memory pooling (paper-005) and PIM (paper-011) are receiving significant investment.

## Cross-Paper Connections
- Directly motivates HBM4 development (papers 001-003) — 2 TB/s per stack vs HBM3E's 1.28 TB/s
- Motivates AMD MI400 capacity-first design (paper-008) with 432 GB vs Vera Rubin's 288 GB
- CXL memory pooling (paper-005) offloads KV cache to extend effective memory bandwidth
- PIM/AiMX (paper-011) addresses memory bandwidth bottleneck by computation at memory

## Theme Tags
memory-wall, LLM, inference, bandwidth-bound, 70B, H100, FLOPS-bandwidth-gap, supercycle
