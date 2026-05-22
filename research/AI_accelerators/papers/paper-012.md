# paper-012: Mobile NPU Landscape — Apple M4, Snapdragon, and On-Device LLM

**Tags:** NPU, LLM-inference  
**Date:** 2025  
**Source:** Apple M4 Wikipedia, AI2Work Analysis, arXiv 2509.23324  
**URL:** https://arxiv.org/pdf/2509.23324

---

## Summary

Mobile neural processing units (NPUs) have become central to on-device AI in 2025, with Apple's M4 Neural Engine (38 TOPS) and Qualcomm's Hexagon NPU (45 TOPS) leading consumer silicon. A September 2025 arXiv paper demonstrates feasibility of LLM test-time compute scaling on smartphone NPUs.

## Apple M4 Neural Engine

- **TOPS:** 38 trillion operations per second (INT8 equivalent)
- **Generation-on-generation:** 2x vs M3 Neural Engine; 60x vs A11 Bionic; 3x vs M1
- **Architecture:** 16-core Neural Engine on TSMC 3nm (N3E)
- **Integration:** Tight coupling with Core ML framework
- **Use cases:** On-device Siri, image generation, LLM quantized inference (<7B models)

## Snapdragon X Elite (Hexagon NPU)

- **TOPS:** 45 INT8 TOPS
- **Architecture:** Hexagon 7th-gen DSP + dedicated tensor accelerators
- **Platform:** AI PC, targeting Windows on Arm
- **Gap vs Apple:** Higher TOPS but real-world performance often behind M4 due to software integration

## NPU Comparison (2025 Consumer Silicon)

| Chip | NPU TOPS | Process | Primary Use |
|------|----------|---------|-------------|
| Apple M4 | 38 (INT8) | TSMC N3E | iOS/macOS on-device AI |
| Qualcomm Snapdragon X Elite | 45 (INT8) | TSMC N4P | AI PC Windows |
| Intel Lunar Lake | 48 (INT8) | Intel 18A | AI PC |
| AMD Strix Point | 50 (INT8) | TSMC N4P | AI PC / Ryzen AI |
| Samsung Exynos 2500 | 29 (INT8) | Samsung 3nm | Galaxy S25 |

## arXiv 2509.23324: LLM Test-Time Compute on Mobile NPU

Published September 2025:
- **Problem:** LLM inference quality scales with test-time compute (chain-of-thought, search)
- **Approach:** Map reasoning steps to NPU-resident quantized LLM
- **Finding:** On-device NPU can execute 7B parameter models at usable token rates
- **Key constraint:** TOPS/W efficiency matters more than peak TOPS for battery-powered deployment
- **Result:** Enables reasoning-capable on-device AI without cloud round-trips

## Quantization for Mobile Deployment

For practical on-device LLM inference:
- **INT8:** Broad hardware support, ~2x efficiency vs FP16
- **INT4:** 4x memory reduction, 4x inference speed with <1% accuracy loss (well-calibrated)
- **Gap:** Edge toolchains support INT8 primarily; INT4 requires specialized kernels
- **Apple ANE:** Supports FP16 natively; INT8/INT4 requires Core ML quantization

## The TOPS Metric Limitation

The industry widely reported TOPS as the primary NPU comparison metric. However, real-world performance depends critically on:
1. Model architecture compatibility
2. Software framework integration (Core ML vs ONNX Runtime vs QNN)
3. Memory bandwidth (often the actual bottleneck)
4. Thermal limits (sustained vs burst TOPS)

Apple M4's real-world advantage over higher-TOPS competitors validates this distinction.

## Significance

NPU capabilities in consumer devices are now sufficient to run meaningful LLM inference locally. The Apple M4's tight hardware-software integration illustrates the path forward: raw TOPS matters less than system-level efficiency. This trend will intensify as on-device privacy requirements and latency constraints drive more inference to edge silicon.
