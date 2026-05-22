# paper-002: NVIDIA Blackwell Architecture — GB200 NVL72 and B200 Specifications

**Tags:** transformer-accelerator, LLM-inference, systolic-array  
**Date:** 2025  
**Source:** NVIDIA Official Documentation, NVIDIA Technical Blog  
**URL:** https://www.nvidia.com/en-us/data-center/technologies/blackwell-architecture/

---

## Summary

NVIDIA's Blackwell GPU architecture represents the primary incumbent platform for AI training and inference in 2025. The flagship **B200** GPU and **GB200 NVL72** rack-scale system delivered 3–30x performance improvements over the prior Hopper generation.

## B200 Architecture

- **Transistors:** 208 billion (dual-die design)
- **HBM3e Memory:** 180 GB per GPU, 8 TB/s bandwidth
- **Training Throughput:** ~4x H100 AI training compute
- **Inference vs H200:** 3.1x higher throughput (Llama-2 70B, 8-GPU DGX test)
- **NVLink 5th Gen:** 1.8 TB/s bidirectional per GPU (18 links × 100 GB/s)

## GB200 NVL72 (Rack-Scale System)

- **Configuration:** 36 Grace Blackwell Superchips = 72 Blackwell GPUs + 36 Grace CPUs
- **NVLink Domain:** 72 GPUs fully interconnected; 130 TB/s aggregate NVLink bandwidth
- **GPT-OSS-120B Performance:** 1.5 million tokens/sec on a single NVL72 system
- **GPT-MoE-1.8T Training:** 4x faster training vs Hopper-equivalent
- **Llama 3.1 Inference:** 3.4x per-GPU and 30x system-level over Hopper on 405B model
- **FP8 Sparse Tensor Cores:** Leverage 2:4 sparsity for 2x effective throughput

## NVLink and Scale

NVLink 5 allows up to 576 GPUs in a single domain. The GB200 NVL72 forms a single logical unit — all 72 GPUs share unified address space. This effectively creates a 13.5 TB memory address space accessible at 576 TB/s aggregate bandwidth.

## Key Performance Numbers

| Metric | B200 Single GPU | GB200 NVL72 |
|--------|-----------------|-------------|
| HBM Capacity | 180 GB | 13.5 TB |
| HBM Bandwidth | 8 TB/s | 576 TB/s |
| FP8 TFLOPS | ~9,000+ | 720+ PFLOPS |
| Tokens/sec (GPT-120B) | ~20k | 1.5M |

## Manufacturing

- Dual-die GPU manufactured at TSMC N3/N4 with CoWoS-L packaging
- Power per GPU: up to 1,000W for B200 SXM configuration
- Each NVL72 rack requires direct liquid cooling; air cooling insufficient at this power density

## Significance

Blackwell established rack-scale design as the new norm for frontier AI infrastructure. The shift from GPU-level to rack-level optimization means individual GPU metrics are less relevant than system-level throughput and total cost of ownership.
