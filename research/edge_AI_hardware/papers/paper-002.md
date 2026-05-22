# paper-002: Scaling LLM Test-Time Compute with Mobile NPU on Smartphones

**Tags:** `on-device-LLM` `mobile-NPU` `quantization`
**Venue:** EuroSys '26 (21st European Conference on Computer Systems, Edinburgh, April 2026)
**Authors:** Zixu Hao et al.
**DOI/URL:** https://dl.acm.org/doi/10.1145/3767295.3769382
**arXiv:** https://arxiv.org/abs/2509.23324
**Date:** 2025-09 (published) / 2026-04 (presented)

---

## Summary

First work to explore **test-time scaling** of LLMs on mobile NPUs. Addresses the problem that smaller models run efficiently but lack reasoning quality, while larger models exceed mobile resource budgets. The approach applies parallel test-time compute scaling on NPUs to boost smaller model quality.

## Core Problem

Mobile NPU matrix multiplication units are underutilized during standard LLM inference (decode is memory-bound). Test-time scaling (running multiple solution candidates in parallel) can fill this compute gap while improving answer quality.

## Key Technical Challenges Addressed

1. **NPU fine-grained quantization support:** Mobile NPUs lack hardware support for per-group quantization. Solution: hardware-aware tile quantization scheme aligning group quantization with NPU memory access patterns.
2. **Complex operations (Softmax, dequant):** Replaced with efficient LUT-based approximations compatible with NPU pipeline.

## Results

| Metric | Value |
|--------|-------|
| Mixed-precision GEMM speedup | up to 19.0× |
| Softmax speedup | 2.2× |
| Platform | Qualcomm Snapdragon (multiple) |

## Architectural Observations

- NPU MAC arrays sit idle during memory-bound decode; test-time scaling reactivates them
- Tile quantization that matches NPU L1/L2 memory layout eliminates quantization overhead
- LUT-based op replacements critical for NPU-unfriendly transcendental functions

## Significance

Demonstrates a paradigm shift: instead of running one large model, run a small model multiple times with test-time scaling on the NPU to achieve comparable quality with better efficiency.
