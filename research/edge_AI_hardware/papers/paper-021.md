# paper-021: ExecuTorch — Unified PyTorch Solution for On-Device AI Deployment

**Tags:** `on-device-LLM` `mobile-NPU`
**Type:** Framework paper + production deployment report
**Sources:** Meta Engineering Blog, PyTorch Blog, arXiv
**URL:** https://engineering.fb.com/2025/07/28/android/executorch-on-device-ml-meta-family-of-apps/
**arXiv (framework paper):** https://arxiv.org/pdf/2605.08195
**Date:** 2025-07 (production report), 2026-05 (arXiv paper)

---

## Summary

**ExecuTorch** is Meta's production-grade on-device inference framework, now powering billions of users across Meta's app ecosystem (Instagram, WhatsApp, Quest 3, Ray-Ban Meta Smart Glasses). As of October 2025, ExecuTorch 1.0 GA represents the most widely deployed on-device AI runtime in history, with a 50KB base footprint enabling deployment from microcontrollers to flagship smartphones.

## Core Specifications

| Attribute | Value |
|-----------|-------|
| Base runtime footprint | **50 KB** |
| Supported hardware backends | **12+** |
| Hardware vendors supported | Apple, Qualcomm, ARM, MediaTek, Vulkan |
| HuggingFace edge LLM support | >80% of popular models |
| Supported models | Llama, Qwen 3, Phi-4-mini, LiquidAI LFM2 |

## Architecture

### Portability: Microcontroller to Smartphone

ExecuTorch's design principle is a zero-overhead abstraction:
- **50KB base:** No mandatory ML runtime infrastructure; backends loaded on demand
- **Delegate system:** Hardware-specific backends implement operator support
- **Fallback:** Unsupported operators automatically fall back to portable CPU implementation

### Backend Ecosystem

| Backend | Target Hardware |
|---------|----------------|
| CoreML | Apple Neural Engine (iOS/macOS) |
| QNN (Qualcomm Neural Networks) | Hexagon NPU |
| TFLM | ARM Cortex-M + Ethos |
| MediaTek NeuroPilot | Dimensity NPU |
| Vulkan | Cross-platform GPU |
| XNNPACK | CPU optimization (ARM NEON, x86 AVX) |

## Production Deployment Results (2025)

### Meta App Performance

- **Privacy improvement:** Sensitive data never leaves device (on-device content moderation, language detection)
- **Latency improvement:** Eliminates cloud round-trip (200-800ms → <50ms for local inference)
- **Cost reduction:** Server inference cost eliminated for deployable model classes
- **Offline capability:** AI features available without internet connection

### Ray-Ban Meta Smart Glasses

ExecuTorch powers always-on AI on the Ray-Ban Meta glasses — demonstrating deployment on severely power-constrained wearable hardware (effectively a tinyML deployment).

## Supported LLMs for Edge (2025-2026)

| Model | Parameters | Use Case |
|-------|-----------|----------|
| Llama 3.2 1B/3B | 1-3B | Mobile general use |
| Phi-4-Mini | 3.8B | Reasoning-capable edge |
| Qwen 3 (various) | 0.5-8B | Multilingual edge |
| LiquidAI LFM2 | <4B | Efficient inference |

## Significance

ExecuTorch's GA status validates that production-scale on-device AI is no longer experimental. The 50KB footprint means every smartphone and even MCU-class device can run Meta's inference stack without meaningful overhead. The 12+ hardware backend system creates a common abstraction layer — developers write once, deploy across Apple, Qualcomm, MediaTek, and ARM platforms.

This framework unification is arguably as significant as the hardware advances: it removes the software fragmentation barrier that previously made cross-platform edge AI deployment prohibitively complex.
