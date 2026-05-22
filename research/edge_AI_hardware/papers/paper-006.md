# paper-006: EntroLLM — Entropy Encoded Weight Compression for Efficient Large Language Model Inference on Edge Devices

**Tags:** `quantization` `on-device-LLM` `compression`
**Venue:** arXiv preprint
**Authors:** Corresponding: sanyal@utexas.edu
**arXiv:** https://arxiv.org/abs/2505.02380
**Date:** 2025-05 (submitted), 2026-01 (updated)

---

## Summary

**EntroLLM** combines mixed quantization with entropy coding (Huffman encoding) to achieve significantly greater storage compression than standard INT4/INT8 quantization alone, while preserving perplexity and accuracy. A parallel decoding strategy ensures minimal inference latency overhead.

## Technical Approach

### Stage 1: Quantization with Entropy-Reducing Effect

- Uses unsigned and asymmetric quantization formulation
- Tensor-level quantization increases weight compressibility (more compressible weight distributions)
- Improves downstream Huffman encoding efficiency:
  - **7× improvement** in Huffman entropy reduction for INT8
  - **11.3× improvement** for INT4 over state-of-the-art methods

### Stage 2: Huffman Coding

- Further reduces memory bandwidth demands
- Applied post-quantization to the entropy-optimized weight tensors

### Stage 3: Parallel Decoding

- Hardware-aware parallel decompression minimizes decode overhead at inference time
- Critical for achieving practical throughput on edge hardware

## Results

### Models Tested

| Model | Params |
|-------|--------|
| smolLM-1.7B | 1.7B |
| phi3-mini-4k | 3.8B |
| mistral-7B | 7B |

### Storage Savings

| Baseline | Storage Reduction |
|----------|------------------|
| vs uint8 | up to **30%** |
| vs uint4 | up to **65%** |

### Inference Speedup (NVIDIA Jetson P3450)

| Memory footprint | Speedup |
|-----------------|---------|
| Constrained memory device | 31.9% – 146.6% faster |

## Accuracy Preservation

- Perplexity maintained on language benchmark tasks
- Accuracy on standard NLP evaluations preserved

## Architectural Implications

The entropy-coding insight is significant: standard INT4 already reduces storage by ~8×, but the weight distributions after tensor-level asymmetric quantization become highly compressible, allowing Huffman coding to achieve an additional 30-65% on top of quantization. This suggests a systematic gap in current quantization approaches that ignore statistical redundancy in quantized weights.

## Significance

EntroLLM addresses the storage bottleneck that limits deployment of 3-7B models on memory-constrained edge devices like NVIDIA Jetson. The 65% reduction over INT4 could enable models that previously required external storage to fit entirely in on-chip SRAM.
