# Paper 024 — LlamaWeb: Memory-Efficient Multi-Precision LLM Inference via WebGPU Across 16 Devices
**Validation status:** VALIDATED
**Source:** arXiv preprint 2605.20706 (ICML 2026 AdaptFM Workshop), May 20, 2026
**URL:** https://arxiv.org/abs/2605.20706
**Tier:** 2
**Theme tags:** edge-inference, WebGPU, on-device-LLM, quantization, INT4, mobile-NPU, llama.cpp, cross-platform

## One-sentence claim
LlamaWeb is a WebGPU backend for llama.cpp that enables in-browser LLM inference across 16 heterogeneous devices from 8 GPU vendors — including mobile NPUs and integrated GPUs — using static memory planning and tunable templated kernels, demonstrating that viable on-device LLM inference is achievable across diverse consumer hardware without cloud dependency.

## Methodology summary
Systems implementation paper with empirical evaluation across heterogeneous hardware. The authors built a WebGPU compute backend for llama.cpp, the dominant open-source LLM inference framework. Key design choices: static memory planning (pre-allocated buffers with no dynamic allocation during inference), a tunable kernel library for cross-device portability, and templated GPU kernels that compile to device-appropriate WGSL (WebGPU Shading Language). Evaluated across 16 devices from 8 GPU vendors spanning discrete GPUs, integrated GPUs, and mobile NPUs. Ten language models tested covering a range of parameter counts. Four weight formats evaluated: INT2, INT4, INT8, and FP16 quantization. Submitted to arXiv on May 20, 2026; affiliated with ICML 2026 AdaptFM Workshop.

## Quantitative results
- Devices evaluated: 16 devices from 8 GPU vendors (mix of discrete GPU, integrated GPU, mobile NPU)
- Language models tested: 10 distinct models
- Weight formats supported: INT2, INT4, INT8, FP16 (4 quantization levels)
- On-device inference demonstrated without cloud dependency across all 16 tested configurations
- Specific throughput (tokens/sec) and latency figures for individual device/model/quantization combinations are reported in the paper but not reproduced here — the device matrix characterization is the primary empirical contribution

## Stated limitations
- WebGPU may impose overhead relative to native inference backends (CUDA, Metal, Vulkan) — the paper acknowledges this as a portability-performance tradeoff.
- INT2 quantization quality depends on the quantization calibration method; LlamaWeb inherits llama.cpp's quantization implementations rather than introducing novel methods.
- Performance is bounded by WebGPU's API constraints; GPU features accessible via native APIs (e.g., CUDA cooperative groups, tensor cores) are not exposed through WebGPU.

## Inferred limitations
- The 8-vendor/16-device matrix, while broad, does not include the latest generation of dedicated mobile AI accelerators (e.g., Apple Neural Engine via Core ML, Qualcomm Hexagon NPU via QNN) — WebGPU typically routes to the GPU path rather than the NPU path on mobile devices, which means the paper may understate the performance available from purpose-built edge AI silicon on the same devices.
- Browser memory limits and GPU memory partitioning by the OS/browser runtime constrain maximum model size; practical deployment at scale faces model-size ceilings that native deployments do not.
- The paper evaluates inference throughput but does not characterize energy consumption per token, which is the primary constraint for mobile deployment and a key differentiator between hardware platforms at the edge.
- WGSL kernel portability across vendors is valuable but future WebGPU extensions (subgroup operations, cooperative matrix multiply) may require kernel rewrites to achieve competitive performance on newer hardware generations.

## Architectural significance
LlamaWeb's 16-device empirical matrix provides the first systematic characterization of LLM inference performance across the fragmented edge hardware landscape under a single unified software stack. This is valuable as a benchmark baseline: it establishes what is achievable today via the browser runtime path (WebGPU) across mobile NPUs, integrated GPUs, and discrete entry-level GPUs, without vendor-specific optimization. For the edge AI hardware sector, this characterization matters because it reveals which device classes are already capable of useful in-browser LLM inference (likely: discrete GPUs and high-end integrated GPUs) versus those that remain throughput-limited (likely: mobile NPUs constrained by WebGPU API routing). The static memory planning approach — pre-allocating all buffers and eliminating dynamic allocation during inference — is an architectural insight applicable beyond WebGPU: it reduces garbage collection pauses and memory fragmentation, which are significant in any memory-constrained runtime. The ICML 2026 AdaptFM Workshop affiliation provides peer review validation appropriate for a systems paper of this type.

## Cross-paper connections
- Contextualizes edge_AI_hardware papers on dedicated NPU silicon (Apple M-series Neural Engine, Qualcomm AI Engine, MediaTek APU): LlamaWeb's WebGPU path does not exploit NPU instruction sets, so the performance gap between LlamaWeb results and native NPU deployment on the same devices represents the headroom that dedicated edge AI accelerator software stacks can capture.
- Connects to AI_accelerators papers on quantization research (INT4, INT8): LlamaWeb's demonstration that INT2/INT4 are viable for in-browser inference on diverse hardware supports the broader thesis that quantization is closing the gap between server-grade and edge-grade inference quality, reducing the architectural justification for dedicated edge accelerators in medium-complexity inference tasks.
- Connects to GPUs/paper-021 (NVIDIA Vera Rubin / agentic AI): Vera CPU and Rubin are designed for datacenter agentic AI; LlamaWeb addresses the complementary edge case where agents must operate on-device without cloud access. The two represent opposite ends of the agentic AI compute deployment spectrum.
- The cross-vendor 8-GPU-vendor / 16-device matrix provides a reference baseline against which future dedicated edge AI accelerator papers (new NPU generations, custom inference silicon) can benchmark their incremental value over commodity hardware running WebGPU.
