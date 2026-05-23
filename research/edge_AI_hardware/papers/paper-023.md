# paper-023 — Cloud to Edge: Benchmarking LLM Inference on Hardware-Accelerated Single-Board Computers

**Validation status:** VALIDATED  
**Source:** arXiv:2604.24785, 2026-04-24  
**URL:** https://arxiv.org/html/2604.24785v1  
**Tier:** 2 (preprint — cross-referenced with paper-006 on mobile thermal constraints)  
**Run:** #1 (2026-05-23)

---

## One-Sentence Claim

Hardware-accelerated single-board computers (SBCs) with dedicated NPU co-processors can sustain LLM inference in the 1–5W power envelope, with the Hailo-10H NPU achieving near-zero-variance throughput that surpasses thermally-throttled mobile phones at sustained load.

## Methodology Summary

Empirical benchmark study across representative SBC platforms including Raspberry Pi 5 with Hailo-10H NPU co-processor. Compares throughput (tokens/second), power consumption (W), thermal steady-state behavior, and energy-per-token across repeated 20-iteration inference runs. Models tested include Qwen 2.5 1.5B (4-bit quantized), representing the smallest practical edge-class LLMs. Cross-references results against mobile phone (Samsung S24 Ultra, iPhone 16 Pro) and laptop GPU (RTX 4050) from companion paper arXiv:2603.23640.

## Quantitative Results

- **Hailo-10H NPU on Raspberry Pi 5:** thermally stable across 20+ iterations; near-zero throughput variance (no throttling observed)
- **Power envelope:** 1–5W total system power for SBC+NPU configuration
- **Mobile comparison:** iPhone 16 Pro loses ~44% throughput by iteration 2; S24 Ultra hits OS-enforced frequency floor; both thermally throttle within 6 iterations
- **Conclusion:** dedicated NPU co-processor outperforms integrated GPU on sustained inference by 2–4× in terms of variance-adjusted throughput at equal or lower power

## Stated Limitations

- Model scope limited to sub-2B parameter quantized models (practical limit of SBC RAM)
- Hailo-10H is a specialized NPU; results may not generalize to all SBC+NPU combinations
- Does not measure first-token latency (TTFT), only sustained throughput

## Inferred Limitations

- The 1–5W envelope precludes models >7B even at INT4 without additional memory expansion
- Hailo-10H is a dedicated AI accelerator not present in commodity SBCs — results reflect premium edge configurations
- Comparison to mobile assumes similar model/quantization; real-world deployment conditions differ

## Architectural Significance

Extends the prefill/decode thermal constraint story from phones (paper-006) to the emerging sub-phone power tier (1–5W IoT/embedded range). Key finding: the dedicated NPU co-processor form factor (SBC + external NPU module) solves the mobile phone's throttling problem by keeping AI compute on a separate thermal domain. This supports the architectural argument (cross_sector_alpha.md Finding 3) that prefill/decode disaggregation emerges as a structural law: even at the 1W scale, the separation of inference compute from general-purpose processing improves sustained throughput. The "SBC + NPU co-processor" paradigm could become the edge AI hardware template for always-on inference workloads (security cameras, automotive, agricultural sensing).

## Cross-Paper Connections

- Companion to paper-006 (arXiv:2603.23640) — extends mobile phone benchmarks to SBC tier
- Supports edge_AI_hardware Observation 1 on memory bandwidth gap between mobile and datacenter
- The Hailo-10H result (thermally stable, near-zero variance) directly validates the tinyML/IoT use case that paper-039 benchmarks identified
- Connects to AI_accelerators: validates that the prefill/decode NPU separation principle applies across 6 orders of magnitude in power (1W SBC to 1MW datacenter rack)

## Theme Tags

`edge-AI`, `SBC`, `NPU-coprocessor`, `Hailo-10H`, `thermal-stability`, `LLM-inference`, `embedded`, `always-on`, `IoT`, `sustained-throughput`
