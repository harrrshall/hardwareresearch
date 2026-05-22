# paper-005: Sustainable LLM Inference for Edge AI — Evaluating Quantized LLMs for Energy Efficiency, Output Accuracy, and Inference Latency

**Tags:** `quantization` `on-device-LLM` `energy-efficiency`
**Venue:** ACM Transactions on Internet of Things
**Authors:** (Multiple authors)
**DOI:** https://dl.acm.org/doi/10.1145/3767742
**arXiv:** https://arxiv.org/abs/2504.03360
**Date:** 2025-04

---

## Summary

Comprehensive empirical study evaluating 28 quantized LLMs from the Ollama library on a Raspberry Pi 4 (4GB RAM), measuring the three-way trade-off between energy efficiency, output accuracy, and inference latency across multiple quantization levels (q2–q8/FP16) and task types.

## Experimental Setup

- **Hardware:** Raspberry Pi 4, 4GB RAM (representative resource-constrained device)
- **Models evaluated:** 28 quantized LLMs from Ollama library
- **Quantization levels tested:** q2, q3, q4, q5, q6, q8, FP16
- **Task types:** General language tasks, mathematical reasoning, code generation

## Key Quantitative Findings

### Energy Reduction

| Quantization Level | Energy Reduction vs FP16 |
|-------------------|--------------------------|
| q3 | up to 79% |
| q4 | up to 79% |
| q5/q6 | 40-60% |
| q8 | 20-30% |

### Accuracy Trade-offs

- **Mathematical reasoning:** Significant degradation below q4; q3 models can be unreliable
- **General language tasks:** q4 maintains competitive accuracy; some q3 models acceptable
- **FP16 → q8:** Near-lossless for most tasks
- **Key finding:** Accuracy varies significantly by task type, not just quantization level

### Latency

- Lower quantization consistently reduces latency on memory-constrained devices
- q4 offers best latency/accuracy balance for general deployment

## Critical Findings

1. Quantization and pruning sometimes fail to reduce *total* inference energy on general-purpose hardware
2. Existing FLOP-based and GPU-utilization proxies underestimate real-world energy use by **2-6×** due to memory, I/O, and kernel-launch overheads
3. Hardware-level energy profiling is essential — software proxies are insufficient
4. Task-specific quantization selection is critical; one-size-fits-all levels cause unnecessary accuracy loss

## Implications for Edge Deployment

- q4 INT4 is the pragmatic sweet spot for most edge deployments
- Mathematical reasoning applications require q5+ or specialized model architectures
- Energy measurement must use hardware power counters, not computational proxies
- On Raspberry Pi 4 (proxy for IoT/edge SBC), quantized LLMs are viable for many NLP tasks
