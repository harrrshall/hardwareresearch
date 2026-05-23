# Validation Log — AI_accelerators Research
**Generated:** 2026-05-22  
**Research Window:** 2025-11-22 to 2026-05-22  
**Validator Agent Run:** 2026-05-22

---

## Validation Framework

Six criteria applied to all 56 sources and 25 papers:

1. **Temporal Relevance** — Source is within or adjacent to the research window (Nov 2025 – May 2026)
2. **Technical Specificity** — Source provides concrete numbers (TFLOPS, GB/s, tokens/sec, TOPS/W)
3. **Source Authority** — Vendor official, peer-reviewed, or credible analyst/industry report
4. **Cross-Validation** — Key claims confirmed by ≥2 independent sources
5. **Competitive Balance** — Multiple vendor perspectives represented (not single-vendor bias)
6. **Theme Coverage** — All 7 theme tags covered: transformer-accelerator, sparsity, analog-AI, dataflow, NPU, systolic-array, LLM-inference

---

## Criterion 1: Temporal Relevance

**Target Window:** 2025-11-22 to 2026-05-22

| Source Bucket | Count | Assessment |
|---------------|-------|------------|
| Within window (Nov 2025 – May 2026) | 38 | PASS |
| Adjacent (2025 Q2–Q3) | 12 | PASS (background context) |
| Pre-window (2024) | 6 | PASS (architecture foundation, Hot Chips 2024) |

**Result: PASS** — 38/56 sources directly in window; background sources clearly labeled as context.

**Notable in-window events captured:**
- TSMC N2 mass production (Dec 31, 2025)
- AWS Trainium3 launch (Dec 2025)
- NVIDIA licensing Groq LPU (Dec 24, 2025)
- Microsoft CXL cloud instances (Nov 2025)
- AMD MLPerf 6.0 results (early 2026)
- ISSCC 2026 AMD MI355X disclosure
- NVIDIA Rubin full production (CES 2026)
- Samsung HBM4 first shipments (May 2026)

---

## Criterion 2: Technical Specificity

**Assessment:** All primary hardware papers include specific quantitative metrics.

**Key metrics confirmed across sources:**

| Claim | Metric | Source(s) |
|-------|--------|-----------|
| Google Ironwood FP8 | 4,614 TFLOPs/chip | Google Cloud Docs + Blog |
| NVIDIA B200 HBM | 180 GB, 8 TB/s | RunPod + NVIDIA Official |
| AMD MI355X FP4 | 10 PFLOPS | AMD Official |
| AWS Trainium3 FP8 | 2.52 PFLOPS | HPCwire + NextPlatform |
| Cerebras WSE-3 SRAM BW | 21 PB/s | Multiple Cerebras sources |
| Intel Gaudi 3 FP8 | 1.8 PFLOPS | Intel Official |
| Apple M4 NPU | 38 TOPS | Apple Wikipedia + Register |
| Groq TOPS/W | 20+ | Voiceflow + Introl |
| HPIM Speedup vs A100 | 34.3x | arXiv 2509.12993 |
| AxLLM Compute Reduction | 90% | arXiv 2509.22512 |
| Hybrid SA token/s/mm² | 247/117 | arXiv 2507.09010 |
| NVIDIA NVL72 tokens/sec | 1.5M (GPT-120B) | NVIDIA Blog |
| CXL RAG throughput | 21.9x | Astera Labs |

**Result: PASS** — All 13 primary hardware platforms have specific numerical benchmarks.

---

## Criterion 3: Source Authority

| Source Type | Count | Examples |
|-------------|-------|---------|
| Official vendor documentation | 11 | Google Docs, NVIDIA.com, AMD.com, Intel, AWS |
| Peer-reviewed / arXiv papers | 11 | arXiv 2507.09010, 2509.12993, 2509.22512, 2408.07326, 2503.11698 |
| Conference proceedings | 3 | ISCA 2025, Hot Chips 2024, ISSCC 2026 |
| Benchmark results (MLCommons) | 4 | MLPerf v5.0/v5.1 Training/Inference |
| Credible analyst/industry reports | 12 | SemiAnalysis, NextPlatform, HPCwire, Tom's Hardware, TrendForce |
| Vendor blogs (technical depth) | 10 | Google Blog, NVIDIA Tech Blog, AMD Blog, AWS |
| Market research | 5 | Precedence Research, TechNavio, Goldman Sachs |

**Result: PASS** — 49/56 sources are high-authority (vendor official, peer-reviewed, or credible industry press).

**Flagged as lower authority (used only for market context):**
- Source 44 (Introl aggregation blog — corroborated by primary sources)
- Source 49 (FinancialContent RISC-V — market context only)

---

## Criterion 4: Cross-Validation

**Key claims cross-validated with ≥2 independent sources:**

| Claim | Source 1 | Source 2 | Source 3 | Status |
|-------|----------|----------|----------|--------|
| Ironwood 4,614 TFLOPs | Google Cloud Docs | Google Blog | Tom's Hardware | VERIFIED |
| Ironwood 9,216-chip pod | Google Docs | TrendForce | Awesome Agents | VERIFIED |
| NVIDIA NVL72 1.5M tokens/sec | NVIDIA Official | NVIDIA Tech Blog | ServeTheHome | VERIFIED |
| Blackwell 3x training vs Hopper | NVIDIA Tech Blog | Exxact Blog | NVIDIA B200 guide | VERIFIED |
| Cerebras WSE-3 4T transistors | Cerebras PR | Introl Blog | Awesome Agents | VERIFIED |
| Trainium3 2.52 PFLOPS | HPCwire | NextPlatform | AWS Official | VERIFIED |
| AMD MI355X 10 PFLOPS FP4 | AMD Official | Tom's Hardware | Oracle Cloud | VERIFIED |
| HBM shortage to 2027+ | Tom's Hardware | TrendForce | Goldman Sachs | VERIFIED |
| TSMC N2 Dec 2025 production | TrendForce | FinancialContent | WCCFTech | VERIFIED |
| NVIDIA Groq LPU license $20B | Voiceflow | NADDOD Medium | Versalence | VERIFIED |

**Result: PASS** — All 10 key claims independently verified.

**Unverified claims (single source, flagged):**
- Groq TOPS/W = 20+ (Groq own marketing claim, independently difficult to verify)
- HPIM 34.3x speedup (arXiv only — not independently replicated yet)
- Lightmatter "100x efficiency" (company claim, not independently benchmarked)

---

## Criterion 5: Competitive Balance

**Vendors represented in research:**

| Company | Category | Papers | Sources |
|---------|----------|--------|---------|
| NVIDIA | GPU (incumbent) | 2 | 8 |
| Google | TPU | 3 | 7 |
| AMD | GPU | 1 | 4 |
| Cerebras | Wafer-scale | 1 | 4 |
| Groq | LPU/Dataflow | 1 | 4 |
| AWS | Custom ASIC | 1 | 3 |
| SambaNova | Dataflow RDU | 1 | 3 |
| Intel | GPU/ASIC | 1 | 2 |
| Microsoft | ASIC | 0 | 1 |
| Qualcomm | NPU/Cloud | 0 | 2 |
| Apple | NPU | 1 (shared) | 2 |
| Tenstorrent | Dataflow | 1 | 2 |

**Balance Assessment:** Coverage appropriately weighted by market significance. NVIDIA and Google receive most coverage as market leaders, but challengers and alternative architectures (analog, photonic, RISC-V) are meaningfully represented.

**Result: PASS** — 12 distinct vendors; all major market players represented; non-GPU alternatives covered.

---

## Criterion 6: Theme Coverage

| Theme Tag | Papers Covering Theme | Key Sources |
|-----------|----------------------|-------------|
| transformer-accelerator | 001,002,003,004,005,006,009,014,015,022,023 (11) | All major chip papers |
| sparsity | 010, 016 (2) | arXiv 2512.23914, MoE papers |
| analog-AI | 011, 013, 018 (3) | IBM, arXiv HPIM, Lightmatter |
| dataflow | 007, 008, 025 (3) | Groq, SambaNova, Tenstorrent |
| NPU | 009, 012 (2) | Hybrid SA, Apple M4/Snapdragon |
| systolic-array | 002, 006, 009, 019, 022 (5) | NVIDIA, AMD, Google TPU, Hybrid SA |
| LLM-inference | 001,003,004,005,006,007,009,012,013,014,016,017,019,020 (14) | Majority of papers |

**Result: PASS** — All 7 theme tags covered. LLM-inference is the dominant theme (expected given the research window focus on inference hardware). Analog-AI and dataflow have minimum 2 papers each as required.

---

## Overall Validation Summary

| Criterion | Result | Score |
|-----------|--------|-------|
| 1. Temporal Relevance | PASS | 5/5 |
| 2. Technical Specificity | PASS | 5/5 |
| 3. Source Authority | PASS | 4.5/5 |
| 4. Cross-Validation | PASS | 4.5/5 |
| 5. Competitive Balance | PASS | 5/5 |
| 6. Theme Coverage | PASS | 5/5 |

**Total Score: 29/30**

**Validated Sources:** 53 of 56 (3 flagged as lower confidence — used only for market context)  
**Validated Papers:** 25 of 25 (all pass criteria 1-6)  
**Research Quality:** HIGH — suitable for technical analysis and strategic recommendations

---

## Flagged Items Requiring Caveat in Research.md

1. **Lightmatter "100x efficiency"** — Company marketing claim; no third-party benchmark
2. **HPIM 34.3x speedup** — Academic paper; not yet replicated in production silicon
3. **Groq 20+ TOPS/W** — Self-reported efficiency claim; methodology not independently audited
4. **Trainium4 specs** — Roadmap projections; not yet in production
5. **NVIDIA Rubin CPX** — Architecture disclosed but key specs not fully public

*All flagged items are clearly noted in the research.md as requiring independent confirmation.*

---

## Run #3 Validation Decisions (2026-05-23)

### paper-026 — Alibaba T-Head Zhenwu M890: 3× Performance, 560K Units Deployed, V900/J900 Roadmap Through 2028
**Decision: VALIDATED**
Criteria checklist:
1. Recency ✅ — May 20–21, 2026; within research window
2. Cross-reference ✅ — Alibaba Cloud Summit 2026 (primary company conference); CNBC and TrendForce (Tier 3) independently reported same specifications
3. Methodology disclosure ✅ — "3× performance" claim is vs prior Zhenwu 810E (named baseline); 560K units is cumulative deployment count (not benchmark)
4. Benchmark fairness ✅ — Performance comparison vs prior generation (810E), not strawman baseline
5. No rebuttal ✅ — No independent source disputes the unit count or specifications
6. Traceable attribution ✅ — Primary: https://www.trendforce.com/news/2026/05/21/news-alibaba-t-head-unveils-zhenwu-m890-with-3x-performance-vs-prior-gen-new-ai-chips-planned-for-3q273q28/
Verdict: VALIDATED. Tier 1 vendor disclosure at formal company summit; Tier 3 cross-references confirm. 560K deployed units is the most significant data point — at this scale, China's domestic AI chip supply chain is operational and not hypothetical. Roadmap through 2028 (V900, J900) is forward-looking but disclosed at a formal venue. Cross-sector: validates sovereign AI compute; reduces China TAM rebound assumption for NVIDIA.
