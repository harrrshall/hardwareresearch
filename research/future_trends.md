# Global Synthesis — Future Trends

**Generated:** 2026-05-22 | **Research window:** 2025-11-22 – 2026-05-22
**Inputs:** 10 sector research files. All projections are extrapolations from in-window evidence; no claims rest on data outside the 2025-11-22 – 2026-05-22 window.
**Confidence legend:** high · medium · speculative.

This file projects forward in three layers: (A) what is already hardening into reality, (B) a 12–24 month projection of what becomes mainstream, and (C) a 3–5 year directional inference with scenario branching where the evidence supports multiple futures.

---

## PART A — What Hardens into Reality Next (already locked in by in-window evidence)

These are not predictions so much as the playing-out of commitments already made. Confidence is high across the board because the silicon has taped out, the standards are ratified, or the capacity is committed.

### A1. HBM4 becomes the standard AI memory — **confidence: high**
All three vendors are in mass production with 2026 capacity sold out (memory/research.md, papers 001–003). Rubin and MI400 both ship on HBM4 in H2 2026 (GPUs/research.md src-009, src-026; AI_accelerators/research.md paper-004). This is locked.
- **Key signals to watch:** HBM4 16-Hi 48GB yield ramp; whether Samsung's SF4 base die sustains its 13 Gbps lead.
- **Falsifiers:** a 16-Hi stacking yield collapse forcing 12-Hi-only supply; an HBM4 thermal failure mode emerging in volume Rubin/MI400 deployment.

### A2. Rubin and MI400 ship in H2 2026 — **confidence: high**
Rubin entered full production at CES 2026 (AI_accelerators/research.md paper-004; interconnects/research.md paper 010); AWS and Google Cloud committed to Vera Rubin NVL72 deployment (GPUs/research.md src-046). MI400 confirmed at CES 2026 for 2026 (memory/research.md paper-008).
- **Key signals:** GTC/CES deployment confirmations; CoWoS-L allocation to AMD.
- **Falsifiers:** a CG-HBM (memory-on-die) yield problem delaying Rubin; HBM4 supply shortfall slipping either product.

### A3. Liquid cooling becomes the deployment default — **confidence: high**
76% of new AI servers liquid-cooled in 2026 (datacenter_hardware/research.md Paper 001); mandatory for all AI GPU racks (GPUs/research.md src-039); NVLink 6 switches require it (interconnects/research.md Implication 4).
- **Key signals:** CDU lead times (currently 20–36 weeks) compressing or extending.
- **Falsifiers:** an air-cooling breakthrough — none is visible in the corpus, so this is near-unfalsifiable for the window.

### A4. GAA nanosheet + backside power delivery universalize — **confidence: high**
GAA is in HVM at all three leading foundries; BSPDN ships in Intel 18A now, TSMC N2P H2 2026, universal by end-2027 (chip_fabrication/research.md Paper 001, Paper 015, Trend 2; CPUs/research.md paper-004, paper-014).
- **Key signals:** TSMC N2P BSPDN first-yield data (Q3–Q4 2026) as the leading indicator for A16.
- **Falsifiers:** a BSPDN thermal-dissipation problem (backside heat path partially blocked by power metal) forcing a retreat to frontside power for high-TDP parts.

### A5. Co-packaged optics ships at the switch layer — **confidence: high**
Broadcom TH6 (102.4 Tbps) began mass shipping October 2025; NVIDIA Quantum-X/Spectrum-X and TSMC COUPE in production 2026 (photonics/research.md sources 8, 6, 25; interconnects/research.md paper 007).
- **Key signals:** TSMC COUPE volume-production yield; CPO field reliability vs. pluggables.
- **Falsifiers:** CPO package yield (CTE-mismatch limited) staying far below pluggable's >99% (photonics Open Question 2).

### A6. The open-standard wave is ratified and deploying — **confidence: high**
CXL 4.0, UCIe 3.0, UALink 1.0, UEC 1.0, PCIe 7.0 all landed in-window (interconnects/research.md papers 001–004, 006, 012). Ratification is locked; deployment timing is the open variable (see Part C).

---

## PART B — 12–24 Month Projection: What Becomes Mainstream (mid-2026 → mid-2028)

### B1. FP4 inference becomes the production default, not just the architecture's design point — **confidence: high**
Today FP4 is natively supported (Blackwell NVFP4, CDNA4 MXFP4) but not universal in production — calibration tooling is still maturing (GPUs/research.md item under FP4 quantization; AI_accelerators/research.md Open Question 2). Over 12–24 months, automated FP4 calibration pipelines mature and FP4 becomes the default inference precision, mirroring how FP8 became default in 2023–2025. Edge follows with INT4-plus-entropy-coding (edge_AI_hardware/research.md paper-006).
- **Key signals to watch:** an "FP4 equivalent of LLM.int8()" automated calibration tool reaching production; MLPerf adding FP4-quality benchmarks.
- **Falsifiers:** FP4 quality degradation on reasoning-heavy tasks proving irreducible, keeping FP4 niche (AI_accelerators Open Question 2).

### B2. Inference workload share crosses two-thirds; inference-specialized silicon goes mainstream — **confidence: high**
Inference rises 33%→50%→67% of AI compute 2023→2026 (AI_accelerators/research.md Trend 1). Within 24 months, prefill/decode disaggregation and phase-specialized silicon (Groq-style LPUs, Rubin CPX, TPU v8's training/inference split) become standard deployment architecture (AI_accelerators/research.md Observation 1; GPUs/research.md Trend 1).
- **Key signals:** TPU v8 specifications; whether NVIDIA ships the Groq LPU integration in volume Vera Rubin.
- **Falsifiers:** SSM/Mamba-transformer hybrids becoming dominant and collapsing the prefill/decode distinction (AI_accelerators Open Question 3).

### B3. ARM crosses 30% of the PC market; RISC-V ships credible datacenter silicon — **confidence: medium**
ARM PC share is projected to reach ~30% by end-2026 from 13% in 2025 (CPUs/research.md paper-016). RISC-V, post-Ventana, ships server-class silicon targeting EPYC parity (CPUs/research.md paper-008). Within 24 months ARM laptops are mainstream and RISC-V is a credible third datacenter ISA.
- **Key signals:** Canalys ARM PC share quarterly data; native ARM64 performance parity for Office/Chrome/enterprise security software; first Qualcomm-branded RISC-V server announcement.
- **Falsifiers:** ARM PC share stalling below 20% on x86 application-compatibility and enterprise-adoption friction (CPUs Open Question 2); RISC-V datacenter silicon slipping to 2028+.

### B4. CXL memory pooling becomes standard for LLM inference serving — **confidence: medium**
CXL 4.0 (128 GT/s, 100+ TiB pools) released November 2025; production CXL pooling already shows 4.8x inference throughput and 82.7% TTFT reduction (interconnects/research.md paper 003, paper 021; memory/research.md paper-019). Within 24 months CXL KV-cache offload is a standard inference-serving technique.
- **Key signals:** CXL 4.0 multi-rack systems (expected late 2026–2027); hyperscaler CXL instance availability.
- **Falsifiers:** PCIe 7.0 compliance delays (now slipped to 2028) cascading into CXL 4.0 deployment slipping to 2029 (interconnects Open Question 5) — this would push B4 out of the 24-month window.

### B5. On-device 7B-class LLM inference becomes a routine smartphone feature — **confidence: medium**
Mobile NPUs crossed 100 TOPS in Q3–Q4 2025 (edge_AI_hardware/research.md paper-013, paper-014); 2026 flagships routinely ship 100–200 TOPS. But the memory-bandwidth wall keeps *sustained* inference at 1–4B models until LPDDR6 (~80+ GB/s, commercial late 2026) widens slightly (edge_AI_hardware/research.md Trend 1, Trend 6).
- **Key signals:** LPDDR6 commercial shipment; 5-minute sustained-throughput benchmarks (not burst peak).
- **Falsifiers:** thermal throttling proving unsolvable in phone form factors, capping practical on-device models at 3B (edge_AI_hardware Observation 2).

### B6. Rack power density 120 kW → 250–300 kW becomes routine; HVDC 800V emerges — **confidence: medium**
GB300 NVL72 already at 250kW+ (GPUs/research.md); OCP ORv3-HPR V3 at 300 kW/cabinet deployed by Meta/Google/Microsoft; ORv3-HPR V4 previews 800 kW with 800V HVDC (datacenter_hardware/research.md Paper 011, Trend 1). Within 24 months 250–300 kW racks are routine and 800V HVDC begins deployment.
- **Key signals:** OCP formalizing an 800V HVDC standard; SiC converter supply.
- **Falsifiers:** floor-loading, fire-suppression, or facility chilled-water constraints capping practical density below 300 kW (datacenter Open Question 1).

### B7. Glass substrates enter limited production for flagship parts — **confidence: medium**
Intel debuted EMIB-on-glass January 2026; AMD is qualifying (packaging/research.md Paper 004). Within 24 months glass appears in limited production for the highest-value Intel/AMD packages, at a 2–3x cost premium.
- **Key signals:** glass yield crossing 90%; Absolics/LG Innotek/Samsung capacity announcements.
- **Falsifiers:** glass brittleness/handling keeping yield below 90% and confining glass to samples (packaging Open Question 5).

### B8. CoWoS remains sold out; no supply relief inside the window — **confidence: high**
Even the 4x ramp to 130K wpm does not clear 2026 demand (packaging/research.md; chip_fabrication/research.md Open Question 7). CoPoS panel-level relief is a 2028–2029 story. For the full 24 months, packaging capacity stays the gating constraint.
- **Key signals:** TSMC quarterly CoWoS capacity vs. NVIDIA+AMD+hyperscaler demand; CoPoS pilot-line progress.
- **Falsifiers:** an AI capex correction collapsing demand (the 2023 transceiver-inventory precedent, photonics/research.md Trend 4).

---

## PART C — 3–5 Year Directional Inference (2028 → 2031) with Scenario Branching

Beyond ~24 months the evidence supports multiple futures. Each trend below is given as a directional bet with explicit scenario branches where the corpus shows genuine uncertainty.

### C1. The memory wall forces an architectural fork — **confidence: medium (direction); scenario-branched (resolution)**
HBM4 doubled the interface to 2,048-bit; the corpus is explicit that HBM5 *cannot* simply double again to 4,096-bit (memory/research.md Open Question 8, Scalability). Something has to give within 3–5 years.

- **Scenario C1-a (3D / PIM resolution).** HBM5 goes vertical: DRAM-on-logic monolithic stacking (imec/Kioxia IGZO 3D DRAM, IEDM 2025) plus PIM to cut transfer frequency. Supported by memory/research.md (3D DRAM research, LPDDR6-PIM standardization) and packaging/research.md (memory moving on-stack via SoIC-X at 2–3 µm). **Probability: moderate-to-high.**
- **Scenario C1-b (bandwidth-via-packaging resolution).** Interface width stalls; bandwidth growth shifts entirely to more stacks, higher pin speeds (HBM4E 16 Gbps), and CG-HBM direct die-stacking (GPUs/research.md, Rubin CG-HBM). **Probability: high as a bridge, insufficient alone past ~2030.**
- **Scenario C1-c (compute-near-memory resolution).** The decode phase migrates off the GPU entirely onto memory-resident compute (PIM, the Groq-LPU logic). Supported by AI_accelerators/research.md (HPIM, prefill/decode disaggregation). **Probability: moderate.**
- **Most likely:** a blend of C1-b near-term and C1-a/C1-c by 2030.
- **Key signals:** IGZO 3D DRAM appearing on a vendor production roadmap (not just IEDM); HBM5 interface architecture disclosure.
- **Falsifiers:** an algorithmic breakthrough (radically sub-quadratic attention, attention-free models) that relaxes the bandwidth demand and defers the wall.

### C2. The NVLink-vs-open-interconnect contest resolves — **confidence: medium (direction); scenario-branched (winner)**
The corpus is unanimous that open standards lag NVLink by 2–4 years, and equally clear that hyperscalers fund the open path as a hedge (GPUs/research.md Trend 4; interconnects/research.md Observation 6, Insight 1).

- **Scenario C2-a (NVLink holds).** UALink silicon (late 2026/2027) launches at 800 Gbps x4 into NVLink 6's 3.6 TB/s; the bandwidth deficit is too large; NVLink Fusion co-opts MediaTek/Marvell/Intel; NVIDIA maintains the interconnect clock. **Probability: moderate-to-high through 2028.**
- **Scenario C2-b (open ecosystem captures new builds).** UALink 2.0 closes the bandwidth gap; hyperscalers shift *new* cluster builds (not retrofits) to UALink/UEC for cost and multi-vendor freedom; custom ASICs (TPU, Trainium, Maia) anchor the open fabric. Supported by interconnects/research.md (75-member consortium) and AI_accelerators/research.md (Trend 5, Trend 6 custom silicon). **Probability: moderate, rising after 2028.**
- **Most likely:** bifurcation — NVLink dominant in merchant-GPU clusters, open fabrics dominant in hyperscaler custom-silicon clusters.
- **Key signals:** UALink 2.0 specification and bandwidth target; whether UALink silicon ships on schedule in Q4 2026.
- **Falsifiers:** UALink silicon slipping to 2028+ (the GenZ/CCIX/OpenCAPI pattern) would collapse C2-b.

### C3. Power becomes the permanent ceiling on AI scale — **confidence: high (direction)**
Datacenter/research.md states it directly: grid power has overtaken compute cost as the binding constraint, and the operators who locked GW-scale interconnections in 2022–2024 have a 5–10 year structural advantage. Over 3–5 years this hardens.
- **Scenario C3-a (concentration).** AI compute concentrates in a handful of operators with secured power; the 2-km-radius latency constraint (datacenter/research.md Observation 2) forces dense gigawatt campuses; new entrants are locked out by interconnection queues.
- **Scenario C3-b (relief via on-site generation).** Behind-the-meter generation (hydrogen fuel cells — Bloom/Brookfield $5B; SMRs not in-window so excluded) and BESS partially decouple AI build-out from the grid.
- **Most likely:** C3-a dominates through 2028; C3-b provides partial relief after.
- **Key signals:** hyperscaler on-site generation deals; grid interconnection queue lengths; transformer lead times.
- **Falsifiers:** large-scale regulatory reform compressing interconnection timelines; an AI demand plateau.

### C4. Custom hyperscaler silicon captures the majority of inference compute — **confidence: medium**
Every hyperscaler now has a custom program; the corpus argues custom silicon beats GPU TCO above ~$100B annual AI spend (AI_accelerators/research.md Trend 6, Insight; datacenter_hardware/research.md Insight 3). Direction: over 3–5 years, custom ASICs take the majority of *inference* compute while NVIDIA holds *training* via the CUDA moat.
- **Key signals:** TPU v8, Trainium4, Maia 200 deployment scale; Anthropic's 1M+ Ironwood commitment playing out.
- **Falsifiers:** NVIDIA's software ecosystem (CUDA, Dynamo) extending its inference lead; custom-silicon development costs proving uneconomic outside the top 3–4 hyperscalers.

### C5. Optical interconnect migrates from package boundary into the die — **confidence: medium**
The inward-migration trajectory is unanimous (photonics, interconnects, packaging). The 3–5 year directional bet: in-die optical I/O and dynamic in-package optical routing (CEA-Leti 3.19 pJ/bit, ISSCC 2026; Celestial AI/Marvell) move from research toward production, and >50 mm on-package interconnects become predominantly optical (interconnects/research.md Observation 4).
- **Key signals:** in-die optical router moving from 28nm research to 5nm production; optical weight memory breakthrough (the gating problem for photonic compute).
- **Falsifiers:** silicon-photonic resonator thermal sensitivity and 5nm integration yield staying unsolved (interconnects Open Question 3; photonics Open Question 4).

### C6. The 2nm-class foundry race stays a three-way contest; geographic diversification matures slowly — **confidence: medium**
Yield convergence within ~10% (chip_fabrication/research.md Trend 1) means foundry selection is driven by packaging, customer relationships, and geopolitics rather than raw process superiority over 3–5 years.
- **Scenario C6-a (Intel recovers).** Intel 18A/14A secures a Tier-1 external customer (Apple is the named highest-stakes outcome) by end-2026; Intel Foundry becomes a credible TSMC alternative (chip_fabrication/research.md Open Question 1; CPUs/research.md Insight on 18A).
- **Scenario C6-b (TSMC dominance persists).** Intel fails to land a Tier-1 customer; the CoWoS packaging moat keeps TSMC structurally ahead regardless of transistor parity.
- **Most likely:** C6-b through 2027, with C6-a possible thereafter conditional on the 14A customer decision.
- **Key signals:** Intel 14A external-customer commitment by end-2026; Rapidus 2027 mass-production yield; US/Japan/EU fab output ramps.
- **Falsifiers:** an Intel 18A/14A yield stall; a Taiwan supply disruption that forces an abrupt diversification.

### C7. Photonic and analog/PIM compute reach pre-commercial maturity but not GPU parity — **confidence: speculative**
Photonic neural networks crossed to multi-layer 64-channel chips and a 262 TOPS accelerator in-window (photonics/research.md sources 27, 44); analog in-memory and PIM show 30–34x research speedups (AI_accelerators/research.md paper-011, paper-013). The 3–5 year directional bet: these reach pre-commercial maturity for narrow workloads but do not reach broad GPU performance-per-watt parity within the window — gated by optical weight memory and the analog precision barrier (~6–8 bits vs the 8–16 bits commercial inference needs).
- **Key signals:** an optical/analog weight-memory material breakthrough; a photonic accelerator in a production data center server.
- **Falsifiers (would accelerate the trend):** a PCM or alternative material solving non-volatile optical/analog weight storage with adequate endurance.

---

## Cross-Cutting Falsifiers (would invalidate large parts of this projection)

1. **An AI capital-expenditure correction.** Multiple sectors cite the 2023 transceiver-inventory correction as precedent (photonics/research.md Trend 4). A demand collapse would simultaneously relieve CoWoS, HBM, laser, and power bottlenecks — invalidating most of Parts B and C's supply-constrained framing.
2. **An algorithmic breakthrough that relaxes the memory wall.** Radically sub-quadratic attention or attention-free architectures becoming dominant would defer C1 and reorder accelerator design (AI_accelerators/research.md Open Question 3).
3. **A Taiwan supply disruption.** The corpus repeatedly states the 2026–2028 window has no viable mitigation for Taiwan concentration (packaging/research.md Insight 6). A disruption would dominate every other trend.
4. **A power-availability ceiling hit sooner than projected.** If grid constraints bind harder than B6/C3 assume, AI compute growth slows regardless of silicon roadmaps.

---

## Summary Table

| # | Trend | Layer | Confidence | Primary falsifier |
|---|-------|-------|------------|-------------------|
| A1–A6 | HBM4 standard, Rubin/MI400 ship, liquid cooling default, GAA+BSPDN universal, CPO at switch, open standards ratified | Hardening now | high | Yield collapse / capex correction |
| B1 | FP4 becomes production-default inference precision | 12–24 mo | high | FP4 reasoning-quality degradation irreducible |
| B2 | Inference share >67%; phase-specialized silicon mainstream | 12–24 mo | high | SSM/hybrid models collapse prefill/decode split |
| B3 | ARM ~30% PC share; RISC-V credible in datacenter | 12–24 mo | medium | x86 compatibility friction; RISC-V slips |
| B4 | CXL memory pooling standard for inference | 12–24 mo | medium | PCIe 7.0 compliance delay cascades to CXL |
| B5 | On-device 7B-class LLM routine on smartphones | 12–24 mo | medium | Thermal throttling caps practical models at 3B |
| B6 | 250–300 kW racks routine; 800V HVDC emerges | 12–24 mo | medium | Floor/fire/water constraints cap density |
| B7 | Glass substrates in limited flagship production | 12–24 mo | medium | Yield stuck below 90% |
| B8 | CoWoS stays sold out; no in-window relief | 12–24 mo | high | AI capex correction |
| C1 | Memory wall forces 3D/PIM/near-memory fork | 3–5 yr | medium | Algorithmic relief of bandwidth demand |
| C2 | NVLink-vs-open contest bifurcates by cluster type | 3–5 yr | medium | UALink silicon slips to 2028+ |
| C3 | Power becomes the permanent AI scale ceiling | 3–5 yr | high | Regulatory reform / demand plateau |
| C4 | Custom silicon takes majority of inference compute | 3–5 yr | medium | CUDA moat extends to inference |
| C5 | Optical interconnect migrates into the die | 3–5 yr | medium | Photonic thermal/yield unsolved |
| C6 | Three-way foundry race; slow geo-diversification | 3–5 yr | medium | Intel yield stall / Taiwan disruption |
| C7 | Photonic/analog compute pre-commercial, not parity | 3–5 yr | speculative | Weight-memory breakthrough |
