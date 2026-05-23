# Global Synthesis — Conclusion

**Generated:** 2026-05-22 | **Research window:** 2025-11-22 – 2026-05-22
**Inputs:** 10 sector research files (GPUs, CPUs, memory, chip_fabrication, AI_accelerators, packaging, photonics, interconnects, datacenter_hardware, edge_AI_hardware)
**Confidence legend:** high (≥3 sectors converge with Tier 1–3 sourcing) · medium (2 sectors, or 1 sector with strong sourcing) · speculative (roadmap/forecast-dependent or single-source)

---

## 1. Executive Overview Across All 10 Sectors

The six months from November 2025 to May 2026 were not ten separate stories. They were one story told ten ways: **the AI compute build-out has pushed every hardware sector simultaneously into the same physics, the same supply chain, and the same architectural answers.** Each sector independently identified memory bandwidth as the binding constraint, chiplet/advanced packaging as the new scaling vector, and inference (not training) as the workload that now sets design priorities.

The headline events, sector by sector:

- **GPUs** — NVIDIA Blackwell (GB200/GB300 NVL72) reached widespread deployment; Rubin entered full production at CES 2026 (336B transistors, HBM4, NVLink 6.0 at 3,600 GB/s); AMD reached credible inference parity with MI355X (GPUs/research.md, src-002, src-028).
- **CPUs** — Intel broke its node drought with 18A Panther Lake (Jan 2026) and 288-core Clearwater Forest; ARM laptop share is projected to 30% by end-2026; RISC-V crossed the datacenter credibility threshold via Qualcomm's $2.4B Ventana acquisition (CPUs/research.md, paper-004, paper-016, paper-008).
- **Memory** — All three HBM4 vendors entered mass production with 2026 capacity sold out; LPDDR6 standardized; CXL 4.0 released at SC25 (memory/research.md, papers 001–003, 005).
- **Chip fabrication** — GAA nanosheet transistors universalized across TSMC N2, Intel 18A, Samsung SF2P, all converging at 60–70% yield; backside power delivery commercialized (chip_fabrication/research.md, Paper 001, Paper 002, Paper 003).
- **AI accelerators** — Inference share of AI compute crossed from 33% (2023) toward a projected 67% (2026); NVIDIA's $20B Groq LPU license validated deterministic inference silicon (AI_accelerators/research.md, paper-007, Trend 1).
- **Packaging** — TSMC CoWoS scaled toward 130K wpm yet stayed sold out; hybrid bonding hit 6 µm in HVM; glass substrates moved to qualification (packaging/research.md, Paper 001, Paper 002, Paper 004).
- **Photonics** — Co-packaged optics shipped at scale (Broadcom TH6 102.4 Tbps, NVIDIA Quantum-X 400 Tb/s); AI optical transceiver market hit $26B; NVIDIA invested $4B in laser supply (photonics/research.md, sources 6, 8, 18).
- **Interconnects** — CXL 4.0, UCIe 3.0, UALink 1.0, UEC 1.0, and PCIe 7.0 all landed; NVLink 6.0 maintained a 2:1 bandwidth lead over open alternatives (interconnects/research.md, papers 001–004, 010).
- **Datacenter hardware** — Rack power crossed 120 kW (GB200 NVL72); grid power overtook compute cost as the binding constraint; PJM capacity prices rose 10x (datacenter_hardware/research.md, Paper 003, Insight 1).
- **Edge AI hardware** — Mobile NPUs crossed 100 TOPS (Snapdragon 8 Elite Gen 5, Apple M5 ~133 TOPS); on-device 7B-class LLM inference became practical; memory bandwidth identified as the throttle (edge_AI_hardware/research.md, paper-013, paper-014, Observation 1).

The unifying thesis: **2025–2026 is the period when AI hardware stopped being a chip story and became a systems story.** The deployable unit is now the rack or the pod, not the die. The competitive moat is now packaging capacity and supply allocation, not transistor design. And the limiting resource is now bandwidth and power, not FLOPS.

---

## 2. Cross-Sector Findings Correlation (claims appearing in ≥2 sectors)

### 2.1 Memory bandwidth is the binding constraint — **confidence: high (8 sectors)**
This is the single most-corroborated finding in the entire corpus. It appears, independently derived, in:
- **GPUs**: IBM Research measured attention kernels at 23.35% compute / 47.10% memory-bandwidth utilization (GPUs/research.md, src-034, paper-012).
- **Memory**: a 70B FP16 model has a 42ms/token floor on H100's 3.35 TB/s; "FLOPS grew 80x vs bandwidth 17x" (memory/research.md, paper-018).
- **AI accelerators**: LLM decode runs at ~0.2 FLOPs/byte against GPUs designed for ~100 FLOPs/byte (AI_accelerators/research.md, §3.2).
- **CPUs**: "Memory Bandwidth as the New Core Count" — diminishing returns past 16–32 cores (CPUs/research.md, Trend 2).
- **Interconnects**: AI bottleneck migrated compute → memory → interconnect (interconnects/research.md, Observation 3).
- **Edge AI**: mobile NPU TOPS grew 10x while mobile DRAM bandwidth grew 22% (edge_AI_hardware/research.md, Observation 1).
- **Datacenter** and **Packaging** both frame HBM bandwidth doubling as the central system metric.

### 2.2 HBM4 is the memory inflection of the window — **confidence: high (6 sectors)**
GPUs, memory, AI accelerators, packaging, interconnects, and CPUs all independently report HBM4 mass production in Q1 2026 with 2,048-bit interface. Cross-sector numeric agreement is strong: SK Hynix 2 TB/s/stack at 11.7 Gbps, Samsung 3.3 TB/s at 13 Gbps, Micron >2.8 TB/s (memory/research.md papers 001–003; packaging/research.md Paper 006; GPUs/research.md src-011, src-044). One cross-sector divergence worth noting: the per-GPU Rubin bandwidth figure varies across files (13 TB/s in interconnects, 22–22.2 TB/s in memory and AI accelerators) — the lower figure appears to be per-stack-class context vs. aggregate; treat aggregate ~20–22 TB/s as the reconciled value. **Confidence: high on HBM4 production; medium on exact Rubin aggregate.**

### 2.3 Chiplet/advanced packaging has replaced monolithic design — **confidence: high (7 sectors)**
GPUs ("GPU architecture has permanently departed from monolithic die design"), CPUs ("The Chiplet Architecture Has Won"), AI accelerators, packaging, interconnects, chip fabrication, and edge AI all state this independently. UCIe 3.0 (64 GT/s, ratified Aug 2025) is cited as the enabling standard in five sectors (CPUs paper-013, packaging Paper 009, interconnects paper 001, chip_fabrication Paper 006, AI_accelerators §5).

### 2.4 TSMC CoWoS is the industry-wide bottleneck — **confidence: high (5 sectors)**
GPUs (NVIDIA 57% of 650K 2025 wafers), packaging (35K→130K wpm, still sold out), AI accelerators (4x ramp to 130K wpm), chip fabrication (capacity tripling), and interconnects ("the invisible constraint on all AI interconnect progress," NVIDIA >70% allocation) all name CoWoS as the gating resource. Cross-sector numeric consistency: 2026 target 120–130K wpm appears in 4 files.

### 2.5 Inference has displaced training as the design driver — **confidence: high (5 sectors)**
AI accelerators (inference 33%→67% of compute 2023→2026), GPUs (GTC 2026 explicit pivot), memory (workload reshaping memory priorities toward long-context KV cache), datacenter (inference-optimized custom silicon), edge AI (on-device inference mainstreaming). The Groq LPU $20B NVIDIA license is cited in both GPUs and AI accelerators as the proof event.

### 2.6 Liquid cooling is now mandatory, not optional — **confidence: high (3 sectors)**
GPUs (liquid cooling mandatory for all AI GPU racks; market $4.9B→$21.3B), datacenter (15%→54%→76% penetration 2024→2026; Microsoft D2C mandate), interconnects (NVLink 6 switch chips require liquid cooling). Packaging adds the chip-level corollary: microfluidic embedded cooling for >500W 3D packages.

### 2.7 RISC-V crossed from embedded to datacenter/AI — **confidence: high (3 sectors)**
CPUs (Qualcomm $2.4B Ventana, 25% CPU IP share), AI accelerators (RISC-V AI market $6.1B 2023 → $92.7B 2030 projected; Tenstorrent), edge AI (129M RISC-V AI device shipments projected by 2030). All three frame open-ISA economics as the driver.

### 2.8 The open-standard vs. proprietary interconnect war — **confidence: high (3 sectors)**
GPUs, interconnects, and AI accelerators all document the NVLink (NVIDIA) vs. UALink/UEC/UCIe (AMD, Intel, hyperscalers) factional split, and all three reach the same conclusion: open standards lag proprietary silicon by 2–4 years, so NVLink 6.0 ships H2 2026 while UALink silicon waits until late 2026/2027.

### 2.9 Co-packaged optics is the external-bandwidth answer — **confidence: high (4 sectors)**
Photonics, interconnects, packaging, and datacenter all document CPO moving from prototype to production (Broadcom TH6 shipping Oct 2025, NVIDIA Quantum-X/Spectrum-X, TSMC COUPE). Energy figures agree across sectors: CPO at ~3.5 pJ/bit vs. 14–24 pJ/bit for pluggables.

### 2.10 Yield convergence at the 2nm node — **confidence: medium (3 sectors)**
Chip fabrication (TSMC N2 65–70%, Samsung SF2P 70%, Intel 18A 60–65% — a 10% band), CPUs (Intel 18A ~7%/month improvement), memory (TSMC N2 in mass production). Edge AI gives one dissenting data point: Samsung SF2 at ~40% yield vs. TSMC ~60% for the Exynos 2600 generation — suggesting yield convergence holds for the SF2P variant but not uniformly. **Confidence: medium due to that divergence.**

---

## 3. Cross-Industry Patterns

**Pattern A — The "system is the unit" inversion.** Every compute sector reports that the procurement and design unit has moved up a level: GPUs (rack-scale NVL72 "single logical compute device"), AI accelerators ("rack-scale as the unit of analysis"), datacenter ("the cluster-scale paradigm has replaced the server paradigm" — hyperscalers design at 10K–800K GPU scale and work backward). Confidence: high.

**Pattern B — Packaging eats process scaling.** GPUs ("GPU performance gains are increasingly driven by packaging, not process"), packaging ("packaging is the new process node"), chip fabrication ("advanced packaging replacing process node scaling for AI"), memory ("advanced packaging becomes the primary scaling vector"). Four sectors, identical claim. Confidence: high.

**Pattern C — Vertical integration into the supply chain.** NVIDIA invested $5B in Intel (GPUs/CPUs), $4B in Lumentum/Coherent lasers (photonics), $2B in Marvell (photonics/interconnects); Marvell acquired Celestial AI for $3.25B; GlobalFoundries acquired AMF and Infinilink; Qualcomm acquired Ventana for $2.4B. Five sectors document the same scramble to own scarce upstream supply. Confidence: high.

**Pattern D — Geographic/geopolitical diversification.** US-Taiwan $250B agreement (packaging), TSMC Arizona $165B (packaging, chip fab, AI accelerators), SK Hynix $13B Indiana plant (packaging, memory), Rapidus Japan 2nm (chip fabrication), GF New York photonics center (photonics). Every manufacturing-adjacent sector reports the same de-concentration push — and the same conclusion that it does not relieve the 2026–2028 supply window. Confidence: high.

**Pattern E — Energy efficiency replaces raw performance as the headline metric.** "pJ/bit replaces Gbps as primary procurement KPI" (interconnects); "energy efficiency as primary competitive axis" (AI accelerators); "bits per joule" shift (photonics); TOPS/W leaderboards (edge AI); PUE and grid economics (datacenter). Confidence: high.

---

## 4. Emerging Technological Shifts (≥3 sectors showing the same direction)

### Shift 1 — Precision compression to FP4/sub-8-bit as the default inference format
**Confidence: high.** GPUs (NVFP4/MXFP4 native in Blackwell and CDNA4), AI accelerators (FP16→FP8→FP4 trajectory; Rubin 50 PFLOPS NVFP4), edge AI (INT4 + entropy coding as the established edge standard), memory (narrow precision reduces bytes/token). Four sectors. Each precision halving yields ~2x throughput, ~2x effective capacity, ~2x effective bandwidth.

### Shift 2 — Optical interconnect moving inward (pluggable → co-packaged → in-die)
**Confidence: high.** Photonics, interconnects, packaging, and datacenter all chart the same inward migration: pluggable optics (2022–24) → co-packaged optics at the package boundary (2025) → in-die optical I/O (Celestial AI, 2025) → dynamic in-package optical routing (CEA-Leti ISSCC 2026, 3.19 pJ/bit). Direction is unanimous.

### Shift 3 — Memory disaggregation / pooling via CXL
**Confidence: high.** Memory (CXL 4.0 at SC25, 100+ TiB pools), interconnects (CXL 4.0, 4.8x inference throughput, 82.7% TTFT reduction), AI accelerators (CXL KV-cache expansion, $1.3B market 2025), CPUs (CXL memory expansion question for EPYC). Four sectors converge on compute and memory architecturally separating.

### Shift 4 — Backside power delivery as a universal node feature
**Confidence: high.** Chip fabrication (Intel PowerVia in HVM, TSMC A16 SPR, Samsung SF2Z — universal by end-2027), CPUs (Intel 18A PowerVia shipping; TSMC N2P BSPDN), memory (TSMC A16 GAA + backside power). Three sectors, consistent timeline.

### Shift 5 — Custom hyperscaler silicon as standard practice
**Confidence: high.** AI accelerators (Google TPU v7, AWS Trainium3, Microsoft Maia 200, Meta MTIA Gen 2, Alibaba Hanguang), datacenter (every major hyperscaler has a custom program), interconnects (Ironwood ICI, Trainium NeuronLink, custom fabrics). Three sectors agree custom silicon now beats commercial GPU TCO above ~$100B annual AI spend.

### Shift 6 — Processing-in-memory / near-memory compute moving toward standardization
**Confidence: medium.** Memory (LPDDR6-PIM JEDEC standardization targeted 2026; SK Hynix AiMX 10x speedup), AI accelerators (HBM-PIM, HPIM 34.3x A100 in research). Two sectors strongly; a third (edge AI) references near-memory compute only at research stage. Direction is consistent but production timing is unproven — hence medium.

### Shift 7 — Annual cadence for AI silicon
**Confidence: high.** GPUs (NVIDIA H100→H200→Blackwell→Blackwell Ultra→Rubin→Rubin Ultra; AMD MI300→MI325→MI350→MI400→MI500), AI accelerators (Trainium2→3→4, TPU generations), memory (HBM 2-year doubling cadence). The annual refresh has no precedent in semiconductor history and is now structural.

---

## 5. Identified Bottlenecks (multiple sectors hitting the same wall)

### Bottleneck 1 — Memory bandwidth (physical wall) — **confidence: high**
Eight sectors (§2.1). HBM4 doubles per-stack bandwidth but delays rather than removes the wall; HBM5 cannot simply double the interface again to 4,096-bit (memory/research.md, Open Question 8). At the edge, the 30–50x bandwidth gap between mobile (~55 GB/s) and datacenter (2–3 TB/s) caps on-device model size (edge_AI_hardware/research.md, Observation 1).

### Bottleneck 2 — TSMC CoWoS advanced packaging capacity (economic/supply wall) — **confidence: high**
Five sectors (§2.4). NVIDIA's 57–70% allocation structurally delays every competitor (AMD MI400, hyperscaler ASICs, startups). Even the 4x ramp to 130K wpm does not clear demand through 2026 (packaging/research.md, Open Question; interconnects/research.md, Observation 5).

### Bottleneck 3 — Grid power availability (physical/regulatory wall) — **confidence: high**
Datacenter ("power availability has surpassed compute cost as the binding constraint," PJM prices 10x, large-transformer lead times 2–3 years), GPUs (250kW+ racks, 100-rack cluster = 32.5 MW), AI accelerators (global DC electricity 460→1,000+ TWh). Three sectors agree power, not silicon, now caps AI capability growth — and a $10B check cannot compress a 5–7 year interconnection queue.

### Bottleneck 4 — Thermal density (physical wall) — **confidence: high**
GPUs (250kW+ racks; B200 at 1.4 W/mm² exceeds air-cooling ceiling), datacenter (D2C mandatory; two-phase cold plates needed above 2,000W/die), packaging (3D-stack bottom-die junction temps at 115°C reliability limit; microfluidic cooling roadmapped), CPUs (thermal-aware physical design). Four sectors hit the same heat-flux wall.

### Bottleneck 5 — HBM stack yield and supply (manufacturing/economic wall) — **confidence: high**
Memory (12-die stack at 98%/die = 78.5% stack yield; HBM costs 5–8x DDR5; 2026 capacity 100% sold), AI accelerators ("most severe memory shortage in 15 years," prices +171.8% YoY, shortage to 2027–2030), packaging (KGD testing adds 15–30% cost). Three sectors.

### Bottleneck 6 — 200G/lane EML laser supply (supply wall) — **confidence: medium**
Photonics (McKinsey: 30–60% supply shortfall through 2027–2029; only Lumentum at volume initially) and interconnects (optical component supply must scale 100x). Two sectors — high-confidence within those, but only two, hence medium overall.

### Bottleneck 7 — Open-standard-to-silicon lag (structural/competitive wall) — **confidence: high**
GPUs, interconnects, AI accelerators all independently quantify the same 2–4 year gap between standard ratification (UALink 1.0 April 2025, CXL 4.0 Nov 2025, PCIe 7.0 June 2025) and meaningful deployment. This is itself a bottleneck on the open ecosystem's ability to challenge NVIDIA.

### Bottleneck 8 — On-chip SRAM scaling (physical wall) — **confidence: medium**
AI accelerators (on-chip SRAM is "the hidden moat" but grows slowly — cannot keep pace with model parameter growth) and memory/chip fabrication (N2 at 38 Mb/mm² is the record; A16 may not add SRAM density; sub-A16 SRAM scaling is uncertain). Two-to-three sectors; medium because the wall is near-term-projected, not yet hit.

---

## 6. Confidence-Rated Conclusions

| # | Conclusion | Supporting sectors | Confidence |
|---|------------|--------------------|------------|
| C1 | Memory bandwidth, not compute, governs AI hardware design | GPUs, memory, AI accelerators, CPUs, interconnects, edge AI, datacenter, packaging | high |
| C2 | Advanced packaging (CoWoS/SoIC/hybrid bonding) has overtaken the process node as the primary AI performance scaling vector | packaging, GPUs, chip fabrication, memory | high |
| C3 | TSMC CoWoS capacity is the gating supply constraint for the entire AI accelerator industry through at least 2026 | GPUs, packaging, AI accelerators, chip fabrication, interconnects | high |
| C4 | Inference has displaced training as the dominant AI workload and the primary chip-design driver | AI accelerators, GPUs, memory, datacenter, edge AI | high |
| C5 | Grid power has become the binding constraint on AI capability growth, ahead of compute cost | datacenter, GPUs, AI accelerators | high |
| C6 | Chiplet architecture has fully displaced monolithic die design at the leading edge | CPUs, GPUs, AI accelerators, packaging, interconnects, chip fabrication, edge AI | high |
| C7 | FP4/sub-8-bit precision is the default inference compute format | GPUs, AI accelerators, edge AI, memory | high |
| C8 | Optical interconnect (CPO and beyond) is the production answer to external bandwidth and is migrating inward toward the die | photonics, interconnects, packaging, datacenter | high |
| C9 | Liquid cooling is now mandatory baseline infrastructure for frontier AI hardware | datacenter, GPUs, interconnects, packaging | high |
| C10 | RISC-V has crossed from embedded into datacenter and AI compute | CPUs, AI accelerators, edge AI | high |
| C11 | The 2nm-class node race has converged the three leading foundries within a ~10% yield band (with Samsung SF2 mobile a partial exception) | chip fabrication, CPUs, memory, edge AI | medium |
| C12 | NVIDIA retains structural dominance via the compounding of CUDA software depth, CoWoS supply allocation, and the NVLink ecosystem lock — the open-standard challenge is real but delayed 2–4 years | GPUs, interconnects, AI accelerators | high |
| C13 | Processing-in-memory is moving toward JEDEC standardization and commercial deployment | memory, AI accelerators, edge AI | medium |
| C14 | Geographic supply-chain diversification (US/Japan/EU) is underway but does not relieve the concentrated-in-Taiwan 2026–2028 window | packaging, chip fabrication, AI accelerators, memory, photonics | high |
| C15 | AMD has reached credible inference parity with NVIDIA on selected workloads; the remaining gap is ecosystem (ROCm long tail), not silicon | GPUs, AI accelerators | medium |
| C16 | HBM5/post-HBM4 memory scaling faces a genuine architectural cliff (interface width cannot double again) requiring 3D/PIM solutions | memory, packaging | speculative |

---

## 7. Cross-Sector Tensions and Unresolved Questions

Three places where the sectors do not fully agree:

1. **Rubin per-GPU HBM4 bandwidth** — interconnects reports 13 TB/s; memory and AI accelerators report ~22 TB/s. Likely a per-stack-context vs. aggregate confusion; flagged for the orchestrator. Reconciled value: aggregate ~20–22 TB/s.
2. **2nm yield convergence** — chip fabrication asserts a tight 60–70% band across foundries; edge AI reports Samsung SF2 at ~40%. The reconciliation is that SF2P (the refined variant) reached 70% while base SF2 mobile lagged — a node-variant distinction the orchestrator should preserve.
3. **CoWoS relief timing** — packaging and chip fabrication both flag CoPoS panel-level packaging (2028–2029) as potential relief, but neither commits; GPUs is more pessimistic (oversubscribed "through at least 2026"). No sector claims relief before 2027.

---

## 8. Bottom Line

Across all ten sectors the same conclusion emerges with high confidence: **the 2025–2026 window is the inflection where AI hardware became a unified, supply-constrained, systems-level industry.** The differentiators that mattered a decade ago — transistor design, raw FLOPS, process node — have been overtaken by packaging capacity, memory bandwidth, interconnect topology, and electrical power. The companies that win the next three years are those that secured CoWoS allocation, HBM4 supply, laser supply, and gigawatt-scale grid interconnections in 2023–2025. The technology roadmap (HBM4, FP4, CPO, GAA+BSPDN, chiplets) is remarkably legible and agreed-upon; the uncertainty is almost entirely in supply, yield, power, and the contest between NVIDIA's proprietary stack and the delayed open-standard coalition.

---

## Run #2 Additive Conclusions (2026-05-23)

*Research window extended by 1 day (2026-05-22 → 2026-05-23). Four new papers added (photonics paper-023 VALIDATED, photonics paper-024 CONTEXT-ONLY, edge_AI_hardware paper-023 VALIDATED, chip_fabrication paper-025 CONTEXT-ONLY, packaging paper-026 VALIDATED). The core thesis and all 16 C-conclusions above remain valid. The following are additive updates only.*

**[Run #2 — new conclusion]**: The CPO ecosystem is no longer a single-vendor story. GlobalFoundries SCALE CPO (paper-023 photonics, VALIDATED, May 4, 2026) establishes GF as a second OCI MSA-compliant CPO platform alongside TSMC COUPE, using DWDM micro-ring modulators at 50/100 Gbps. This incrementally strengthens C8 (optical interconnect as the production bandwidth answer) by demonstrating vendor-level CPO competition and OCI MSA interoperability. It does not relieve the EML laser supply constraint (Bottleneck 6) — ring-modulator CPO still requires external CW laser sources, and a second CPO platform increases aggregate laser demand. **Confidence: high (validated single source; consistent with cross_sector_alpha.md Finding 4 partial mitigation).**

**[Run #2 — new conclusion]**: Advanced packaging single-source concentration is measurably reduced, but not resolved. Samsung 3.3D packaging mass production targeting Q2 2026 (paper-026 packaging, VALIDATED) — enabled by HCB Hybrid Copper Bonding with 20% thermal improvement for 16-Hi HBM stacks — represents the clearest evidence this cycle that TSMC CoWoS is acquiring a credible second-source competitor at scale. However, Samsung 3.3D Q2 2026 serves Samsung's HBM4/HBM4E products (memory packaging), not GPU-logic packages where CoWoS-L is most constrained. C3 (CoWoS as the gating supply constraint) holds for the GPU-logic side; the memory-packaging side is more competitive than the initial synthesis indicated. **Confidence: high on partial mitigation; high on thesis persistence for GPU-logic packages.**

**[Run #2 — new conclusion]**: Dedicated NPU co-processor thermal domain isolation solves the edge AI thermal throttling problem for non-smartphone form factors. arXiv 2604.24785 (paper-023 edge AI, VALIDATED, April 24, 2026) demonstrates that integrated SoC NPUs (Galaxy S24, Pixel 9) lose ≥50% throughput within 6 inference iterations due to shared thermal domain; dedicated NPU co-processors (Hailo-10H on Raspberry Pi 5) sustain near-zero throughput variance across 20+ iterations via separate thermal domain. This refines the edge AI section of the initial corpus: the "thermal throttling caps practical on-device models" observation (Observation 2 in edge_AI_hardware/research.md) is architecture-specific, not universal. Hailo-10H-class architectures have solved it; integrated SoC architectures have not. The memory-bandwidth wall remains the primary edge constraint regardless of thermal design. **Confidence: high (validated empirical study; directly measured 20+ iteration variance).**

**[Run #2 — no new conclusion]**: The Meta/Broadcom/Synopsys $125M UCLA Semiconductor Research Hub (paper-025 chip_fabrication, CONTEXT-ONLY, May 22, 2026) is a long-horizon talent and EDA infrastructure investment (5–10 year payoff). It does not generate new near-term conclusions for the chip fabrication sector or modify any existing C-conclusion. Filed as context for future cycles.
