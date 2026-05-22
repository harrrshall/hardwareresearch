# paper-017: Hailo-10H — First Discrete Edge AI Accelerator for On-Device Generative AI

**Tags:** `mobile-NPU` `on-device-LLM`
**Type:** Product technical analysis
**Source:** Hailo AI, Awesome Agents, All About Circuits
**URL:** https://hailo.ai/
**Date:** 2025-07 (commercial availability)

---

## Summary

The **Hailo-10H** is the first discrete AI accelerator purpose-built for generative AI workloads at the edge — capable of running LLMs, VLMs, and multimodal AI directly on-device in an M.2 form factor drawing only 2.5W. Commercial availability July 2025; Raspberry Pi AI HAT+ 2 ($130) launched January 2026.

## Hardware Specifications

| Attribute | Value |
|-----------|-------|
| Peak AI performance | **40 TOPS INT4** / 20 TOPS INT8 |
| Power consumption | **2.5W** |
| Form factor | M.2 module |
| On-module memory | 4GB or 8GB LPDDR4/4X |
| Memory bandwidth (on-module) | Significantly higher than host I/O |
| Interface | PCIe |

## Key Design Insight: On-Module Memory

Unlike previous edge accelerators that rely on the host device's shared DRAM (typically 50-90 GB/s for mobile), the Hailo-10H integrates dedicated on-module LPDDR4X memory:

- **Benefit:** LLM decode (memory-bound) can stream weights from on-module memory without competing with host CPU/GPU for bandwidth
- **Constraint:** On-module memory bandwidth is the performance ceiling for large models
- **Practical limit:** 4GB on-module supports up to ~3B parameter FP16 or ~8B parameter INT4 models

## Performance Characteristics

| Workload | Performance |
|----------|------------|
| LLM inference (1-3B INT4) | Practical on-device at <2.5W |
| Sustained throughput | Consistent (no thermal throttling observed) |
| vs mobile phone NPU | More predictable sustained performance |

## Ecosystem Integration

### Raspberry Pi AI HAT+ 2

- Launched January 2026, $130
- Plug-and-play M.2 module for Raspberry Pi 5
- Target applications: home automation, edge servers, local AI assistants, robotics

### Enterprise Integration

- HP and Fujitsu integrated Hailo-10H into retail and enterprise products
- Hailo SDK enables ONNX/TFLite model deployment with optimized kernels

## Competitive Context

| Product | Form Factor | TOPS | Power | Memory |
|---------|------------|------|-------|--------|
| Hailo-10H | M.2 | 40 (INT4) | 2.5W | 4/8GB on-module |
| Axelera Metis (M.2) | M.2 | 214 (INT8) | 5-9W | No on-module |
| Qualcomm Cloud AI 100 | PCIe | 400+ | 75W | No on-module |

## Significance

The Hailo-10H fills a unique niche: the first sub-5W accelerator with enough on-module memory to run LLMs independently of the host system. This enables always-on AI inference in power-constrained edge scenarios (IoT gateways, edge servers, RPi-class platforms) that cannot accommodate higher-power accelerators.

The January 2026 Raspberry Pi integration is strategically significant: it democratizes LLM inference to the maker/developer community and creates a reference platform for edge agentic AI applications.
