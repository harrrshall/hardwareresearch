# paper-003: LLM Inference at the Edge: Mobile, NPU, and GPU Performance Efficiency Trade-offs Under Sustained Load

**Tags:** `on-device-LLM` `mobile-NPU` `benchmark` `thermal`
**Venue:** arXiv preprint
**Authors:** (Multiple authors)
**arXiv:** https://arxiv.org/abs/2603.23640
**Date:** 2026-03

---

## Summary

Comprehensive empirical benchmark of sustained LLM inference across four representative edge platforms, measuring throughput, latency, power, and thermal behavior. Key finding: **thermal management is the primary binding constraint for mobile AI**, not peak TOPS.

## Experimental Setup

| Platform | Chip | Accelerator |
|----------|------|-------------|
| Raspberry Pi 5 | BCM2712 | Hailo-10H NPU (M.2) |
| Samsung Galaxy S24 Ultra | Snapdragon 8 Gen 3 | Adreno GPU |
| Apple iPhone 16 Pro | A18 Pro | Neural Engine |
| Laptop | Intel/AMD + NVIDIA RTX 4050 | GPU |

**Model tested:** Qwen 2.5 1.5B (4-bit quantized)

## Key Results

### Throughput and Thermal Behavior

| Platform | Peak Throughput | Sustained Behavior |
|----------|----------------|---------------------|
| iPhone 16 Pro | High (burst) | Loses ~50% throughput within 2 iterations |
| Galaxy S24 Ultra | High (burst) | Hard OS-enforced GPU floor; terminates inference |
| Hailo-10H (Pi 5) | Moderate steady | Limited by on-module memory bandwidth |
| RTX 4050 | Consistent | Limited by battery power ceiling |

### Thermal Findings

- iPhone 16 Pro: A18 Pro NPU throttles to ~60-70% peak after 2-3 minutes
- Galaxy S24 Ultra: Android thermal governor enforces hard GPU frequency floor, GPU reaches 78.3°C
- 1-second inter-iteration gap insufficient for thermal recovery on mobile

### NPU vs GPU Insights

- NPU excels at LLM inference (memory-bound matrix-vector multiply): efficient DMA utilization
- GPU excels at LSTM and compute-bound operations
- Dedicated NPU hardware avoids GPU contention that impairs both graphics and AI workloads

## Critical Conclusions

1. Peak TOPS is a poor predictor of sustained AI performance on smartphones
2. Always-on agents requiring queries more frequent than several minutes face sustained degradation
3. External dedicated NPU (Hailo-10H) shows more predictable sustained performance than integrated mobile NPUs
4. Memory bandwidth on edge devices (50-90 GB/s) vs data center (2-3 TB/s) creates 30-50x gap

## Design Implications

Future mobile SoC designs must prioritize thermal headroom and cooling architecture alongside raw TOPS. The Hailo-10H's dedicated on-module DRAM provides a more predictable performance envelope for always-on applications.
