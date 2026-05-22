# paper-001: Fast On-device LLM Inference with NPUs

**Tags:** `on-device-LLM` `mobile-NPU` `ASPLOS`
**Venue:** ASPLOS '25 (30th ACM ASPLOS, Rotterdam, March–April 2025)
**Authors:** Daliang Xu et al.
**DOI/URL:** https://dl.acm.org/doi/10.1145/3669940.3707239
**arXiv:** https://arxiv.org/abs/2407.05858
**Date:** 2025-03

---

## Summary

Presents **llm.npu**, the first LLM inference system that exploits on-device NPU offloading specifically to reduce *prefill* latency on smartphones. The core insight is that mobile NPUs carry lighter steady-state workloads than mobile GPUs (which are already busy with graphics rendering), making them better targets for LLM prefill computation.

## Key Technical Contributions

- Fully NPU-accelerated prefill pipeline bypassing the mobile GPU
- Operator mapping strategy for transformer blocks onto NPU compute primitives
- Demonstrated on Redmi K70 Pro (Snapdragon 8 Gen 3)

## Results

| Metric | Value |
|--------|-------|
| Prefill speedup vs llama.cpp-CPU (1024 tokens) | 18.17–38.4× |
| Energy savings vs baseline | 30.7× average |
| End-to-end application speedup | up to 32.8× |
| Peak prefill throughput | >1,000 tokens/sec (1B param model) |
| Average prefill speedup vs competitive baselines | 22.4× |

## Hardware Context

- **Device:** Redmi K70 Pro (Snapdragon 8 Gen 3, Hexagon NPU)
- **Models tested:** Billion-parameter scale models
- **Memory bandwidth note:** Mobile NPU has dedicated memory paths avoiding GPU contention

## Architectural Observations

NPUs have dedicated DMA (Direct Memory Access) engines optimized for streaming weight matrices — exactly what LLM decode requires. This architectural advantage over GPU compute pipelines is exploited by routing prefill (which is compute-bound) to NPU rather than decode (which is memory-bound).

## Significance

This is the first work to demonstrate >1000 tokens/sec prefilling on a smartphone NPU for billion-sized models, establishing a new performance frontier for on-device LLM deployment and opening the NPU as a first-class inference target.
