# paper-019: MLPerf Benchmarks 2025 — Training v5.0/v5.1 and Inference v5.0/v5.1

**Tags:** transformer-accelerator, LLM-inference, systolic-array  
**Date:** 2025 (v5.0 June, v5.1 September/November 2025)  
**Source:** MLCommons  
**URL:** https://mlcommons.org/2025/09/mlperf-inference-v5-1-results/

---

## Summary

MLCommons released four MLPerf benchmark rounds in 2025 (Training v5.0, Inference v5.0, Inference v5.1, Training v5.1), establishing critical industry benchmarks. Performance improvements outpaced Moore's Law, and new models like Llama 3.1-405B, DeepSeek-R1, and Whisper were added.

## MLPerf Training v5.0 (June 2025)

**New Benchmark:** Llama 3.1-405B pretraining — the largest model ever in the training benchmark suite.
**Record Submissions:** Most submissions in suite history.
**New Models:** Despite being newly introduced, Llama 3.1-405B received more submissions than GPT-3 benchmark ever did.
**Key Finding:** Performance improvements for generative AI scenarios outpacing Moore's Law predictions.

## MLPerf Inference v5.0 (April/June 2025)

**New Workloads Added:**
- DeepSeek-R1 reasoning model inference
- Llama-3.1-8B chat
- OpenAI Whisper Large V3 speech recognition

**Participation:** Broadest silicon participation yet (AMD, NVIDIA, Intel, Qualcomm, Cerebras, SambaNova).

## MLPerf Inference v5.1 (September 2025)

**Performance Headline:** In some scenarios, best systems improved **50% over v5.0** in just 6 months.
**AMD Milestone:** MI355X first AMD submission exceeding 1 million tokens/sec.
**NVIDIA Blackwell:** Maintained leadership across compute-bound workloads.
**Qualcomm QAic:** Competed on power efficiency metrics.

## MLPerf Training v5.1 (November 2025)

**Headline:** Substantial performance improvements; "significant evolution" of AI ecosystem.
**Generative AI Scenarios:** Two benchmarks improved beyond Moore's Law prediction rate.
**Increased Richness:** More hardware vendors submitting; more model types covered.

## Key Performance Trends Across 2025 Benchmarks

### Training
| Benchmark | Best System | Key Improvement |
|-----------|-------------|-----------------|
| ResNet-50 | NVIDIA GB200 NVL72 | ~16 min (vs hours on Hopper) |
| BERT | NVIDIA GB200 NVL72 | Sub-1 minute |
| Llama 3.1-405B | NVIDIA GB200 NVL72 | New record |
| GPT-3 175B | NVIDIA GB200 / AMD MI355X | Significant gains |

### Inference
| Model | Best Throughput | Champion |
|-------|----------------|----------|
| Llama 3.1-405B (server) | 1M+ tokens/sec | AMD MI355X |
| GPT-OSS-120B | 1.5M tokens/sec | NVIDIA GB200 NVL72 |
| DeepSeek-R1 (new) | Competitive results | Multiple vendors |
| Whisper V3 | New benchmark | Multiple vendors |

## Energy Efficiency Data

MLPerf added power efficiency tracking in 2025:
- Qualcomm QAic: 20x lower power than 8x A100 on 70B models
- Cerebras WSE-3: Strong tokens/watt on models fitting 44GB SRAM
- NVIDIA Blackwell: Best absolute throughput; moderate efficiency

## Significance

The MLPerf data provides the industry's most reliable cross-vendor comparison:
1. Performance improvements are genuinely outpacing Moore's Law (40% improvement in 6 months)
2. AMD MI355X has closed the gap with NVIDIA to near-parity on specific workloads
3. Specialist accelerators (QAic, Cerebras) demonstrate superior efficiency for targeted tasks
4. The addition of Llama 3.1-405B and DeepSeek-R1 as benchmarks reflects that production workloads are now frontier-model scale
