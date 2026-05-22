# paper-004: Orion — Characterizing and Programming Apple's Neural Engine for LLM Training and Inference

**Tags:** `on-device-LLM` `mobile-NPU` `Apple`
**Venue:** arXiv preprint
**Authors:** (Multiple authors)
**arXiv:** https://arxiv.org/abs/2603.06728
**Date:** 2026-03-06

---

## Summary

**Orion** is the first open, end-to-end system for programming Apple's Neural Engine (ANE) directly for both LLM inference and resumable training — bypassing CoreML entirely via Apple's private `_ANEClient` and `_ANECompiler` APIs. The work provides the most comprehensive public characterization of ANE constraints to date.

## Architecture Characterization

- **New discoveries:** 14 previously undocumented MIL IR, memory, and I/O constraints
- **Total constraint catalog:** 20 ANE restrictions documented
- **Compiler pipeline:** Lowers a 27-operation graph IR through 5 optimization passes to ANE-native MIL

## Key Technical Innovations

### Weight Baking Bottleneck Solution

The ANE requires compiled programs with baked weights. Orion solves the expensive recompilation step:
- Standard `ANECompile()` call: **4,200 ms** per training step
- Orion's delta compilation (unload → patch weights → reload): **494 ms** per step
- **Speedup: 8.5×** recompilation reduction
- **Training throughput speedup: 3.8×**

### I/O Pipeline

- Manages IOSurface I/O, program caching, and delta compilation natively
- Runtime avoids CoreML overhead entirely

## Performance Results

| Task | Hardware | Metric | Value |
|------|----------|--------|-------|
| GPT-2 124M inference | M4 Max | Throughput | 170+ tokens/sec |
| 110M transformer training | M4 Max | 1000 steps | 22 minutes |
| Training stability | M4 Max | NaN occurrences | 0 |

## Significance

- Unlocks ANE for research use without CoreML dependency
- Demonstrates stable multi-step LLM training on ANE hardware for the first time
- Provides roadmap for future Apple silicon AI software optimization
- Critical reference for anyone building efficient Apple-silicon inference pipelines

## Architectural Observations

The ANE is structured as a fixed-function neural accelerator with strict constraints on tensor shapes, memory layouts, and operation ordering. Its efficiency advantage comes from a deeply pipelined data path that eliminates CPU-GPU data transfer overhead — when accessed directly, it achieves dramatically higher utilization than through CoreML abstraction layers.
