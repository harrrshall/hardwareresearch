# paper-004: NVIDIA Rubin Architecture — Next-Generation AI Compute Platform (2026)

**Tags:** transformer-accelerator, LLM-inference, systolic-array  
**Date:** CES 2026 (announced at Computex 2024, full production 2026)  
**Source:** NVIDIA Newsroom, VideoCardz, ServeTheHome, SemiAnalysis  
**URL:** https://nvidianews.nvidia.com/news/nvidia-unveils-rubin-cpx-a-new-class-of-gpu-designed-for-massive-context-inference

---

## Summary

NVIDIA's **Rubin** GPU architecture, paired with the **Vera** CPU, entered full production at CES 2026. It targets 5x the inference performance of Blackwell per GPU and enables qualitatively new capabilities through the Rubin CPX variant for massive-context inference.

## GPU Architecture (R100)

- **Transistors:** 336 billion (dual reticle dies)
- **Process:** TSMC N3 (3nm)
- **Memory:** HBM4, 288 GB per GPU, 22 TB/s bandwidth
- **FP4 Inference:** 50 PFLOPS (NVFP4) per GPU
- **FP4 Training:** 35 PFLOPS (NVFP4) per GPU
- **Generation-on-generation vs Blackwell:** 5x inference, 3.5x training (NVFP4)

## Vera CPU

- **Transistors:** 227 billion
- **Core Architecture:** Custom Arm "Olympus", 88 cores, 176 threads (Spatial Multi-Threading)
- **Memory:** Up to 1.5 TB LPDDR5x (SOCAMM format), 1.2 TB/s bandwidth
- **Role:** Host processor replacing Grace; tightly coupled to Rubin GPU

## Interconnect — NVLink 6

- **Per-GPU Bandwidth:** 3.6 TB/s bidirectional (2x NVLink 5's 1.8 TB/s)
- **Domain Size:** Up to 576 GPUs (same as NVLink 5 domain size)

## Vera Rubin NVL72 Rack System

- **Configuration:** 72 Rubin GPUs + 36 Vera CPUs
- **Scale-Up Bandwidth:** 260 TB/s (2x vs Blackwell NVL72's 130 TB/s)
- **FP4 Inference:** 3.6 Exaflops NVFP4
- **FP4 Training:** 2.5 Exaflops NVFP4
- **HBM4 Capacity:** 20.7 TB per NVL72
- **HBM Bandwidth:** 1.6 PB/s
- **LPDDR5x Capacity:** 54 TB total (from Vera CPUs)

## Economic Claims

- 10x lower inference token cost vs Blackwell
- 4x fewer GPUs needed for MoE training vs Blackwell
- Qualitatively new capability: Rubin CPX specifically for "massive-context inference"

## Rubin CPX Variant

NVIDIA unveiled a specialized Rubin CPX variant designed for massive-context inference — enabling extremely long context windows that exceed what NVL72 can handle. Architecture specifics not fully disclosed but presumed to include extended NVLink domain or HBM4 augmentation.

## Key Numbers

| Metric | Rubin R100 | Vera Rubin NVL72 |
|--------|------------|------------------|
| Transistors | 336B | — |
| HBM4 per GPU | 288 GB | 20.7 TB |
| HBM4 BW | 22 TB/s/GPU | 1.6 PB/s |
| FP4 Inference | 50 PFLOPS/GPU | 3.6 EFLOPS |
| NVLink BW/GPU | 3.6 TB/s | 260 TB/s aggregate |

## Significance

Rubin establishes HBM4 as the next memory standard and confirms NVIDIA's sustained 2-year cadence. The 5x NVFP4 jump reflects both process (N3 → N3) and architectural improvements in tensor core design.
