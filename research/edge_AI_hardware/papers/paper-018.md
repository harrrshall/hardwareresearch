# paper-018: On-Device LLMs: State of the Union, 2026

**Tags:** `on-device-LLM` `mobile-NPU` `benchmark`
**Type:** Technical review/survey
**Author:** Vikas Chandra (Meta AI Research)
**URL:** https://v-chandra.github.io/on-device-llms/
**Date:** 2026 (January)

---

## Summary

Authoritative survey by a Meta AI Research leader reviewing the 2025-2026 on-device LLM landscape. Key thesis: **the dominant breakthroughs in 2025-2026 came from model architecture, compression, and deployment innovation rather than hardware advances alone.** Memory bandwidth is the primary binding constraint for LLM inference on all edge platforms.

## Hardware Performance Context (2026)

### Mobile NPU Performance

| Platform | NPU TOPS | Memory Bandwidth |
|----------|----------|-----------------|
| Snapdragon 8 Elite Gen 5 | ~100 TOPS | ~55 GB/s LPDDR5X |
| Apple M5 | ~133 TOPS | ~200 GB/s (M5 Max) |
| Samsung Exynos 2600 | >59 TOPS | ~55 GB/s |
| MediaTek D9400+ | NPU 890 | ~50-60 GB/s |

**Data center comparison:** V100 = 125 TOPS, A100 = 312 TOPS, H100 = 1979 TOPS

### The Memory Bandwidth Problem

For LLM decode (the user-facing generation step):
- Each token generation requires streaming **all model weights** through memory
- A 7B INT4 model requires ~3.5GB streamed per generated token
- At 55 GB/s: ~63ms/token = ~16 tokens/sec theoretical maximum
- Real throughput lower due to attention KV cache and overhead

**Mobile vs Data Center gap:** 50-90 GB/s vs 2-3 TB/s = **30-50× bandwidth gap**

## Recommended Models for Edge Deployment (2026)

### Capable Devices (>8GB RAM)

| Model | Params | Notes |
|-------|--------|-------|
| Qwen2.5-VL-7B-Instruct | 7B | Vision+language |
| Meta-Llama-3.1-8B-Instruct | 8B | General use |
| Qwen3-8B | 8B | Strong reasoning |

### Constrained Devices (<4GB RAM)

| Model | Params | Quality | Speed |
|-------|--------|---------|-------|
| Phi-4-Mini | 3.8B | 88.6% GSM8K, 83.7% ARC-C | ~22 tok/s M4 Air |
| Qwen2.5-3B | 3B | Best quality/param <4B | Fast |
| Gemma 3 1B | 1B | Strong for size | ~45 tok/s mobile |
| Llama 3.2 1B | 1B | Competitive | Very fast |

## Critical Bottlenecks Identified

1. **Available RAM:** Even high-end phones limit AI apps to <4GB due to OS + other apps
2. **Memory bandwidth:** The fundamental constraint, not TOPS
3. **Thermal throttling:** iPhone 16 Pro and S24 Ultra lose 50%+ performance under sustained load
4. **Model size vs quality tradeoff:** Sub-1B models inadequate for most real tasks

## Software Ecosystem Status (2026)

| Framework | Status |
|-----------|--------|
| ExecuTorch 1.0 | Production, ships in Meta apps |
| llama.cpp | Dominant for research/developer use |
| LiteRT (Google) | Qualcomm NPU optimized |
| Core ML | Apple ecosystem |
| MediaTek NeuroPilot | Dimensity ecosystem |

## Strategic Outlook

The state of on-device LLMs in 2026: capable enough for most NLP tasks at 4-8B parameter scale, constrained by thermal limits for sustained use, and rapidly improving via model efficiency research rather than hardware scaling alone. The next breakthrough will come from mobile-native model architectures trained specifically for bandwidth-constrained inference.
