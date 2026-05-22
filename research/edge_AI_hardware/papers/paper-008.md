# paper-008: Benchmarking Ultra-Low-Power μNPUs

**Tags:** `tinyML` `benchmark` `energy-efficiency`
**Venue:** arXiv preprint
**Authors:** Josh Millar, Yushan Huang et al. (Imperial College London + Anil Madhavapeddy group)
**arXiv:** https://arxiv.org/abs/2503.22567
**Date:** 2025-03

---

## Summary

First independent, standardized benchmark evaluation of multiple commercially-available micro-NPU (μNPU) platforms, addressing the critical gap in objective cross-platform comparison. Develops a unified model compilation pipeline supporting consistent benchmarking of quantized models across diverse microcontroller hardware.

## Motivation

- Hardware vendors report metrics using proprietary frameworks with different models, quantization strategies, and measurement methodologies
- No standardized cross-platform benchmark existed prior to this work
- Existing benchmarks (e.g., prior MLPerf Tiny iterations) focus on only one platform (MAX78000)

## Platforms Evaluated

| Platform | NPU TOPS | RAM | Flash | Notes |
|----------|---------|-----|-------|-------|
| MAX78000 (Analog Devices) | High for class | — | — | **Best overall energy-efficiency** |
| MCXN947 (NXP) | 4.8 GOPS | 512 KB | 2 MB | Lower-power applications |
| (Additional platforms) | Various | Various | Various | See paper for full table |

## Key Findings

### Energy Efficiency

- **MAX78000 largely outperforms** other μNPU platforms in energy-efficiency
- Particularly well-suited for battery-powered applications
- Other platforms show competitive latency but higher energy/inference

### Unexpected Disparities

- Certain μNPUs exhibit **unexpected non-linear scaling** behavior with model complexity
- Vendor-reported TOPS often poorly predicts real-world performance for specific model topologies
- Hardware-specific operator support gaps cause significant fallback to CPU for unsupported layers

### Performance Prediction

- Theoretical TOPS is unreliable for model-level performance prediction
- Memory access patterns and operator coverage matter as much as raw compute

## Methodology Contribution

- Unified compilation pipeline converts ONNX/TFLite models to platform-specific formats
- Consistent quantization (INT8) applied across all platforms
- Energy measured at hardware level (not estimated from FLOPS)
- Reproducible benchmark suite released publicly

## Architectural Observations

The MAX78000 uses a **memory-in-compute** (near-memory processing) architecture where weight memory is co-located with compute units, eliminating weight streaming overhead. This architectural choice explains its energy efficiency advantage over platforms using conventional SRAM with separate compute arrays.

## Implications

Hardware designers selecting μNPUs should run independent benchmarks on their specific models rather than relying on vendor TOPS claims. The 4.8 GOPS MCXN947 may outperform a nominally higher-TOPS device for specific small model topologies.
