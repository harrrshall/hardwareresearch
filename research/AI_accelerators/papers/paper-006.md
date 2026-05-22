# paper-006: AMD Instinct MI355X — CDNA 4 Architecture and MLPerf Breakthrough

**Tags:** transformer-accelerator, LLM-inference, systolic-array  
**Date:** 2025 (ISSCC 2026 paper published)  
**Source:** AMD Official, Tom's Hardware (ISSCC 2026 disclosure), Oracle Cloud blog  
**URL:** https://www.amd.com/en/products/accelerators/instinct/mi350/mi355x.html

---

## Summary

The AMD Instinct **MI355X** is the flagship accelerator of the CDNA 4 architecture, delivering up to 10 PFLOPS FP4 per GPU and breaking AMD's 1 million tokens/sec barrier in MLPerf Inference benchmarks. An ISSCC 2026 paper disclosed that AMD halved Compute Unit count while doubling per-CU FP8 throughput — an unusual microarchitectural trade.

## Architecture (CDNA 4)

- **Transistors:** 185 billion
- **HBM3E Memory:** Up to 288 GB per GPU
- **FP4 Performance:** 10 PFLOPS
- **FP6 Performance:** 10 PFLOPS (shared spec)
- **FP8 Performance:** 5 PFLOPS (1.9x vs MI300X)
- **Max Model Size (single GPU):** Up to 520B parameter models

## ISSCC 2026 Microarchitecture Disclosure

AMD disclosed an unusual architectural decision:
- MI300X: 38 active Compute Units (CUs) per Accelerator Complex Die (XCD)
- MI355X: 32 active CUs per XCD (down 16%)
- Per-CU FP8 throughput: doubled
- Net FP8 result: 5 PFLOPS — a 1.9x gain on MI300X
- Claim: "matching performance of the more expensive and complex GB200" on key workloads

This trade suggests AMD found per-CU density improvements more efficient than adding more CUs, prioritizing die area for SRAM, memory interfaces, and interconnect.

## Training Performance

- **MLPerf 5.1 Training:** 2.8x faster time-to-train vs MI300X
- **Llama 2-70B LoRA FP8:** From 28 min (MI300X) to 10 min (MI355X)
- **Agent/Chatbot workloads:** 4.2x faster than MI300X

## Inference Performance

- **MLPerf Inference 6.0:** First AMD result exceeding 1 million tokens/sec
- **Llama 3.1-405B FP4 latency (8-GPU):** 50.6 ms (input: 32,768 tokens, output: 1,024 tokens)
- **Content generation/summarization:** 2.6x–3.8x faster than MI300X

## Key Numbers

| Metric | MI300X | MI355X | Improvement |
|--------|--------|--------|-------------|
| FP8 TFLOPS | ~2.6 PFLOPS | 5 PFLOPS | 1.9x |
| FP4 TFLOPS | — | 10 PFLOPS | new |
| HBM3E capacity | 192 GB | 288 GB | 1.5x |
| CUs per XCD | 38 | 32 | -16% |
| FP8 per-CU throughput | baseline | 2x | 2x |

## ROCm Ecosystem

AMD's ROCm 6.x with HIP support for PyTorch and JAX has materially closed the ecosystem gap with NVIDIA CUDA. MI355X ships with native vLLM, SGLang, and TensorRT-LLM (via ROCm port) compatibility for production inference.

## Significance

The ISSCC 2026 disclosure revealing AMD matched GB200 performance while using fewer, denser CUs marks a significant architecture evolution. AMD's path forward appears to be pushing compute per unit area rather than aggregate unit count, enabling better yield economics at advanced nodes.
