# paper-016: MediaTek Dimensity 9400 and 9400+ — NPU 890 and Agentic AI Platform

**Tags:** `mobile-NPU` `on-device-LLM`
**Type:** Product announcement + technical analysis
**Source:** MediaTek, RCR Wireless, Gear Diary
**URL:** https://www.mediatek.com/press-room/mediatek-enhances-flagship-ai-performance-with-dimensity-9400-mobile-platform
**Date:** 2025-04-10

---

## Summary

MediaTek announces the **Dimensity 9400+** featuring the NPU 890 — the most AI-capable mobile NPU in MediaTek's history. Introduces the **Dimensity Agentic AI Engine (DAE)** as a platform abstraction layer for building autonomous AI agents on mobile devices.

## NPU 890 Specifications and Capabilities

| Feature | Capability |
|---------|-----------|
| LLM support | Mixture-of-Experts (MoE) models |
| Attention architecture | Multi-Head Latent Attention (MLA) |
| Decoding strategy | Multi-Token Prediction (MTP) |
| Numerical precision | FP8 inferencing |
| Advanced feature | Speculative Decoding+ (SpD+) |

## Performance Improvements vs Dimensity 9400

| Metric | Improvement |
|--------|-------------|
| Agentic AI performance | **+20% faster** |
| With Speculative Decoding+ | Faster reasoning speeds |
| On-device video generation | **First** high-quality on-device video gen |
| On-device training | **First** on-device LoRA training |

## Architecture Innovations

### MoE Support

Mixture-of-Experts models (e.g., DeepSeek-style architectures) have most parameters in "expert" blocks that are only occasionally activated. NPU 890 natively supports MoE routing and selective expert activation — critical for running 20-30B effective parameter models with only 3-5B active parameters per token.

### FP8 Precision

FP8 inference provides ~2× throughput vs FP16 with near-lossless accuracy for LLMs, as established in research. NPU 890 is among the first mobile NPUs to support FP8 natively.

### Speculative Decoding+

SpD+ uses a small "draft" model to predict multiple tokens, verified by the larger target model. When drafts are correct (typically ~70-80%), throughput multiplies by the draft length. MediaTek's implementation integrates SpD+ with the NPU's parallel evaluation capabilities.

## Dimensity Agentic AI Engine (DAE)

A software platform layer enabling:
- Tool-use and function calling for on-device agents
- Context management across multi-step reasoning
- Integration with system apps (camera, calendar, contacts) without cloud round-trips
- Developer APIs for building agentic applications

## Diffusion Transformer (DiT) Support

First mobile platform supporting DiT-based image/video generation:
- Enables Stable Diffusion 3-class models on mobile
- Video generation (previously cloud-only) now on-device
- LoRA fine-tuning on-device (first in mobile)

## Significance

The Dimensity 9400+ represents the shift from "LLM on mobile" to "agentic AI on mobile" — moving beyond text generation to autonomous task completion with memory, planning, and tool use. The DAE provides the infrastructure layer that Google, Meta, and other app developers need to build persistent on-device AI agents.
