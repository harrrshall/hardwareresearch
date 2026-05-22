# Paper 020: vLLM Large-Scale Serving and DeepSeek Inference at 2,200 tok/s/H200

**Source ID**: src-035  
**Tier**: 2 (Industry Blog / Open Source)  
**Date**: 2025-12-17  
**URL**: https://blog.vllm.ai/2025/12/17/large-scale-serving.html

---

## One-Sentence Claim
Production DeepSeek MoE deployments on H200 clusters achieve 2,200 tokens/second per H200 GPU using wide expert parallelism (Wide-EP), demonstrating that algorithmic MoE routing optimizations — not just hardware improvements — drive state-of-the-art LLM inference throughput.

## Methodology Summary
vLLM team's production deployment measurements on H200 clusters connected via InfiniBand. Benchmarks are production-scale multi-node measurements, not laboratory conditions. SGLang independently achieved 52.3k input and 22.3k output tokens/second on comparable setups. DeepSeek R1 and V3 models tested (671B MoE architecture). Wide-EP is a technique for distributing MoE experts across more GPUs than standard model parallelism to reduce expert routing bottleneck.

## Quantitative Results
- **Sustained throughput**: 2,200 tokens/second per H200 GPU (multi-node Infiniband cluster)
- **vs. single-GPU**: Wide-EP enables near-linear scaling across GPU count
- **SGLang concurrent measurement**: 52,300 input tokens/second + 22,300 output tokens/second at large scale
- **Continuous batching vs static**: 3-5x throughput improvement
- **FP8 quantization**: 2x throughput improvement vs FP16 (negligible accuracy loss on DeepSeek)
- **Multi-token prediction**: DeepSeek V3 MTP heads generate 2-4 tokens per forward pass
- **KV cache efficiency**: Paged KV + continuous batching prevents cache thrash, lifts throughput 2-4x
- **Speculative decoding**: 2-3x speedup where draft model acceptance rate is high
- **NVIDIA Blackwell vs H200**: Up to 4x higher throughput at similar latency (InferenceMAX)
- **Expert parallelism scaling**: Linear up to 96 GPUs demonstrated (LMSYS blog, 96x H100)

## Stated Limitations
- 2,200 tok/s/H200 is output token throughput; prefill (input processing) throughput is different
- Wide-EP benefits are specific to MoE architectures; dense transformers don't benefit
- Production measurements depend on prompt distribution; average vs peak throughput differ
- InfiniBand fabric required for these results; Ethernet deployments see lower inter-GPU bandwidth

## Inferred Limitations
- 2,200 tok/s per GPU implies ~44k total tokens/s on 20 H200 GPUs — meaningful but not infinite scaling
- KV cache memory pressure is a real limitation: 671B MoE at FP8 requires ~130GB KV cache for long sequences
- Wide-EP increases GPU communication overhead; at very high expert counts, becomes communication-bound
- vLLM's Python-based scheduler introduces CPU overhead that limits sub-100ms latency at high concurrency

## Architectural Significance
This production deployment result is the most credible benchmark available for H200 LLM serving in 2025. The 2,200 tok/s/H200 figure, combined with NVIDIA Blackwell achieving 4x over this (theoretically ~8,800 tok/s/B200), sets quantitative benchmarks for GPU-based LLM inference economics. The Wide-EP technique demonstrates that MoE model inference benefits from spreading experts across more GPUs than the model's "natural" parallelism degree — a software-level optimization that requires no hardware change. The 36x improvement in DeepSeek-R1 throughput from January to end-2025 (src-033) shows that software (vLLM, TensorRT-LLM, SGLang, NVFP4 quantization) contributed the majority of the improvement on the same hardware generation.

## Cross-Paper Connections
- src-034 (memory bottleneck) provides the academic framework explaining why 2,200 tok/s is memory-bandwidth limited
- src-033 (NVIDIA DeepSeek benchmark) covers the competing Blackwell measurement (30,000+ tok/s on 8 GPUs)
- src-014 (MLPerf v5.1) provides standardized context for these production throughput measurements
- src-012 (GPU bottleneck IBM) identifies the bottleneck this work optimizes around

## Theme Tags
`vLLM`, `LLM-inference`, `DeepSeek`, `MoE`, `expert-parallelism`, `throughput`, `H200`, `production-serving`, `tokens-per-second`, `KV-cache`
