# paper-022: Google Tensor G5 — NPU Architecture and Gemini Nano Integration

**Tags:** `mobile-NPU` `on-device-LLM`
**Type:** Product technical analysis
**Sources:** Nanoreview, Gizmochina, CPU-Monkey
**URL:** https://nanoreview.net/en/soc/google-tensor-g5
**Date:** 2025-08-20 (announcement)

---

## Summary

Google's **Tensor G5** (August 2025, Pixel 9 Pro series) marks a manufacturing pivot from Samsung to **TSMC 3nm**, delivering a 60% NPU performance improvement over G4 and expanding Gemini Nano's context window from 12K to 32K tokens with 50% lower power consumption.

## Manufacturing Change

| Attribute | Tensor G4 | Tensor G5 |
|-----------|-----------|-----------|
| Process | Samsung 4nm | **TSMC 3nm** |
| Manufacturing partner | Samsung | TSMC |
| Die size | Larger | Smaller (3nm) |

This represents Google's significant strategic shift: abandoning Samsung foundry for TSMC's more mature 3nm process. Improvement in NPU performance is primarily driven by this manufacturing change plus architectural updates.

## NPU and AI Performance

| Metric | Tensor G4 | Tensor G5 | Improvement |
|--------|-----------|-----------|-------------|
| NPU performance | Baseline | **+60%** | 60% faster |
| Gemini Nano speed | Baseline | **+260%** faster | 2.6× |
| Gemini Nano power | Baseline | **-50%** lower | 50% reduction |
| Context window | 12K tokens | **32K tokens** | 2.67× larger |

## CPU Architecture

| Attribute | Tensor G5 |
|-----------|-----------|
| Core configuration | 1+5+2 (1 Cortex-X4, 5 A725, 2 A520) |
| Max frequency | 3,780 MHz (X4), 3,050 MHz (A725) |
| CPU improvement | **+34%** vs G4 |

## GPU Change

Google switched from Arm Mali to **Imagination Technologies PowerVR DXT-48-1536** GPU — a notable departure from the ARM ecosystem, potentially driven by licensing/cost considerations.

## Gemini Nano Integration Significance

The 32K token context window (vs G4's 12K) is architecturally significant:
- 32K tokens ≈ ~24,000 words (~48 pages of text)
- Enables full document processing on-device
- Supports multi-turn conversations with extensive history
- Enables RAG (Retrieval Augmented Generation) over personal documents on-device

At 50% lower power, Gemini Nano can run more frequently without battery impact — critical for always-on AI assistants.

## Competitive Context

| Platform | Announced | TOPS/Context Window |
|----------|-----------|---------------------|
| Tensor G5 | Aug 2025 | ~40+ TOPS / 32K context |
| A19 Pro | Sep 2025 | 35+ TOPS / 16K context |
| Snapdragon 8 Elite Gen 5 | Sep 2025 | ~100 TOPS |
| Exynos 2500 | Jun 2025 | 59 TOPS |

## Significance

Google's focus on context window length (32K tokens) over raw TOPS reflects a different optimization philosophy: Tensor G5 is optimized for Google's specific Gemini Nano workload rather than general LLM benchmarks. The 260% Gemini Nano speedup at 50% lower power represents better workload-specific optimization than generic TOPS numbers suggest.

The manufacturing shift to TSMC also signals that Google, like Apple, prioritizes TSMC's yield and process maturity over Samsung Foundry for its most critical AI silicon.
