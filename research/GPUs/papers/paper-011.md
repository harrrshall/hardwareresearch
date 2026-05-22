# Paper 011: MLPerf Inference v5.1 — GPU Benchmark Results

**Source ID**: src-014, src-051  
**Tier**: 1 (Peer-reviewed benchmark)  
**Date**: 2025-09-10 (v5.1), 2026-02-15 (v6.0 AMD submission)  
**URL**: https://www.hpcwire.com/2025/09/10/mlperf-inference-v5-1-results-land-with-new-benchmarks-and-record-participation/

---

## One-Sentence Claim
MLPerf Inference v5.1 (September 2025), incorporating the new DeepSeek-R1 671B reasoning benchmark, shows NVIDIA HGX B200 leading across key LLM workloads while AMD MI355X achieves competitive results — with H200 8-GPU clusters reaching 31,391 tokens/second offline on Llama 3.1-70B.

## Methodology Summary
MLPerf Inference is an industry-standard benchmark consortium benchmark. v5.1 results published September 9, 2025. New workloads added: Llama-3.1-8B summarization and DeepSeek-R1 reasoning (first appearance). Submissions from NVIDIA (H200, B200, L40S), AMD (MI355X, MI350X, MI325X, MI300X), Intel, and others. Offline and server scenarios tested; server scenario reflects production latency constraints.

## Quantitative Results
**H200 performance (v5.1)**:
- **8x H200 offline Llama 3.1-70B**: 31,391 tokens/second (vs 27,950 in v5.0 — +12.3%)
- **Single H100 Llama 3.1-8B offline**: 5,777 tokens/second
- **Single H100 Llama 3.1-8B server**: 5,103 tokens/second  
- **Single L40S Llama 3.1-8B offline**: 1,642 tokens/second
- **HPE Cray XD670 (8x H200)**: 6 #1 results including RetinaNet, Llama 3.1-8B (server/offline), Mixtral-8x7B (server/offline), Whisper offline

**NVIDIA HGX B200 performance improvements**:
- +1.6% to +15.4% vs v5.0 results (same hardware, software optimization)

**AMD MI355X (MLPerf v5.1)**:
- Competitive across Llama 2 70B server/offline
- 2.7x more tokens/s vs MI325X FP8 submission
- AMD submitted 4 GPU generations in same round (MI300X through MI355X)

**v5.0 to v5.1 progression**:
- 8x H200 Llama 3.1-70B: 27,950 → 31,391 TPS (+12.3%)
- Improvement attributed to SGLang optimization, not hardware change

## Stated Limitations
- MLPerf is a best-effort benchmark; submissions can be tuned for the benchmark
- Not all hardware configurations are submitted by vendors; missing comparisons limit full competitive picture
- DeepSeek-R1 results are v5.1 first submission; baselines not fully established
- Some improvements (B200 +1.6-15.4%) reflect software optimization, not architectural advances

## Inferred Limitations
- H200 to B200 comparison requires different system configurations, making direct per-GPU comparison challenging
- AMD's MI355X competitive result uses latest ROCm 7 optimizations; older software would show different results
- The v5.1 benchmark set (Llama 3.1-8B, Llama 2 70B) uses models smaller than frontier models in production
- MLPerf server scenario SLA constraints (latency targets) may not reflect real production workload distributions

## Architectural Significance
MLPerf v5.1 is the first standardized benchmark to include DeepSeek-R1 671B reasoning model — the dominant open-source reasoning model of 2025. Its inclusion as a benchmark workload validates the shift from dense transformer inference to mixture-of-experts (MoE) sparse expert routing as the dominant large-scale inference pattern. The 12.3% throughput improvement on H200 between v5.0 and v5.1 purely from software (SGLang) optimization demonstrates that hardware efficiency is only partially exploited by current software stacks. AMD's competitive showing across 4 GPU generations in one round confirms that CDNA4 (MI355X) is now a legitimate datacenter GPU choice.

## Cross-Paper Connections
- src-016 (MLPerf training) covers the training-side benchmark results
- src-032 (InferenceMAX SemiAnalysis) provides real-world production complement to MLPerf
- src-015 (MI355X launch) covers AMD's hardware that achieved competitive MLPerf results
- src-035 (vLLM serving) covers the serving framework (SGLang) driving throughput improvements

## Theme Tags
`MLPerf`, `benchmark`, `inference`, `LLM-inference`, `H200`, `B200`, `MI355X`, `DeepSeek-R1`, `tokens-per-second`, `competitive-analysis`
