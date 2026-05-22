# paper-015: Benchmarking Energy and Latency in TinyML — A Novel Method for Resource-Constrained AI

**Tags:** `tinyML` `benchmark` `energy-efficiency`
**Venue:** arXiv preprint
**Authors:** (Multiple authors)
**arXiv:** https://arxiv.org/abs/2505.15622
**Date:** 2025-05

---

## Summary

Presents a novel standardized benchmarking methodology for precisely measuring energy consumption, latency, and system efficiency of ML models on resource-constrained devices (MCUs). Addresses the lack of reproducible, hardware-accurate benchmarks for TinyML deployments.

## Motivation

### Current Gaps

1. **Software proxy inaccuracies:** FLOP-based energy estimates underestimate real consumption by 2-6×
2. **Vendor inconsistency:** Each vendor measures on different models with different quantization
3. **System effects ignored:** Peripheral activity, memory controller behavior, and interrupt overhead omitted
4. **No reproducible methodology:** Different labs get incomparable results

## Methodology

### Hardware-Level Measurement

- Current shunt measurement at μA precision
- Synchronized with inference start/stop GPIO signals
- Captures complete system energy including memory controller and peripherals

### Benchmark Suite Structure

- **Workloads:** Keyword spotting, image classification (28×28 to 96×96), anomaly detection
- **Quantization levels:** FP32, INT8, INT4
- **Hardware abstraction:** Unified interface for cross-platform comparison
- **Reproducibility:** Open-source measurement framework

## Key Findings

### Energy Measurement Accuracy

- Hardware measurement vs FLOP proxy: real energy is **2-6× higher** than FLOP estimate
- Memory access energy dominates for small-medium models
- Peripheral activity accounts for 5-15% of total system energy during inference

### MCU-Class AI Performance 2025

| Task | Target Latency | Achievable on MCU-class |
|------|----------------|------------------------|
| Keyword spotting | <50ms | Yes (2-10ms with NPU) |
| Low-res image classification | <100ms | Yes (8-30ms with NPU) |
| Anomaly detection | <200ms | Yes (10-50ms with NPU) |

### MLPerf Tiny Context

This work extends and validates the MLPerf Tiny v1.3 benchmark (Sep 2025) methodology, providing the hardware measurement framework that enables MLPerf's standardized comparisons across:
- STMicroelectronics NUCLEO-U385RG-Q: 48+ inferences/sec at 245mW (keyword spotting)
- Renesas, Syntiant submissions with varying power/performance profiles

## Implications

The 2-6× energy underestimation by software proxies has significant practical consequences:
- Battery life projections for always-on AI applications are systematically over-optimistic
- Energy-based model selection decisions may be inverted (wrong model chosen as "efficient")
- Hardware-accurate measurement must become standard practice for edge AI deployment

## Connection to MLPerf Tiny v1.3

The benchmarking methodology aligns with MLPerf Tiny v1.3 (released Sep 2025), which added:
- 1D DS-CNN wake-word detection task
- Continuous audio stream processing evaluation
- Expanded vendor participation (Renesas, STMicro, Syntiant)
