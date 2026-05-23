# Global Synthesis — Future Trends

**Generated:** 2026-05-23 (Run #3) | **Research window:** 2025-11-23 – 2026-05-23
**Inputs:** 10 sector research files. All projections are extrapolations from in-window evidence; no claims rest on data outside the 2025-11-23 – 2026-05-23 window.
**Confidence legend:** high · medium · speculative.

This file projects forward in three layers: (A) what is already hardening into reality, (B) a 12–24 month projection of what becomes mainstream, and (C) a 3–5 year directional inference with scenario branching where the evidence supports multiple futures.

---

## Run #3 Status (2026-05-23)

Run #3 executes approximately five hours after Run #2 on the same calendar date; no new validated papers were found in the 5-hour inter-run window. All trends carry forward from Run #2 unchanged.

| Trend | Status | Change vs. Run #2 |
|-------|--------|-------------------|
| A1 HBM4 standard | **UNCHANGED** | No new evidence |
| A2 Rubin/MI400 ship H2 2026 | **Run #3 CONFIRMED** | NVIDIA Q1 FY2027 earnings (paper-021 GPUs): Rubin "sampling with customers, production shipments H2 FY2027 (H2 calendar 2026)" — CEO confirmation locks this trend |
| A3 Liquid cooling default | **UNCHANGED** | No new evidence |
| A4 GAA+BSPDN universalize | **UNCHANGED** | No new evidence |
| A5 CPO at switch layer | **UNCHANGED** | GF SCALE CPO (from Run #2) already incorporated |
| A6 Open standards ratified | **UNCHANGED** | No new evidence |
| B1 FP4 default inference | **UNCHANGED** | No new evidence |
| B2 Inference >67%; phase-specialized silicon | **UNCHANGED** | No new evidence |
| B3 ARM ~30% PC; RISC-V datacenter | **UNCHANGED** | No new evidence |
| B4 CXL memory pooling standard | **UNCHANGED** | No new evidence |
| B5 On-device 7B-class LLM | **UNCHANGED** | arXiv 2604.24785 from Run #2 already incorporated |
| B6 250–300 kW racks routine | **UNCHANGED** | No new evidence |
| B7 Glass substrates limited production | **UNCHANGED** | No new evidence |
| B8 CoWoS sold out; no relief | **UNCHANGED** | Samsung 3.3D from Run #2 already incorporated |
| C1 Memory wall architectural fork | **UNCHANGED** | No new evidence |
| C2 NVLink-vs-open contest | **UNCHANGED** | No new evidence |
| C3 Power permanent ceiling | **UNCHANGED** | No new evidence |
| C4 Custom silicon majority of inference | **UNCHANGED** | No new evidence |
| C5 Optical interconnect into die | **UNCHANGED** | No new evidence |
| C6 Three-way foundry race | **Run #3 update** | ASML CEO confirms High-NA EUV products "within months" for Samsung/Intel while TSMC delays to 2029 (paper-026 chip_fabrication); scenario C6-a (Intel recovers) strengthened |
| C7 Photonic/analog pre-commercial | **UNCHANGED** | No new evidence |

---

## PART A — What Hardens into Reality Next (already locked in by in-window evidence)

These are not predictions so much as the playing-out of commitments already made. Confidence is high across the board because the silicon has taped out, the standards are ratified, or the capacity is committed.

### A1. HBM4 becomes the standard AI memory — **confidence: high** [Run #3: UNCHANGED]
All three vendors are in mass production with 2026 capacity sold out (memory/research.md, papers 001–003). Rubin and MI400 both ship on HBM4 in H2 2026 (GPUs/research.md src-009, src-026; AI_accelerators/research.md paper-004). This is locked.
- **Key signals to watch:** HBM4 16-Hi 48GB yield ramp; whether Samsung's SF4 base die sustains its 13 Gbps lead.
- **Falsifiers:** a 16-Hi stacking yield collapse forcing 12-Hi-only supply; an HBM4 thermal failure mode emerging in volume Rubin/MI400 deployment.

### A2. Rubin and MI400 ship in H2 2026 — **confidence: high** [Run #3: CONFIRMED — CEO lock]
Rubin entered full production at CES 2026 (AI_accelerators/research.md paper-004; interconnects/research.md paper 010); AWS and Google Cloud committed to Vera Rubin NVL72 deployment (GPUs/research.md src-046). MI400 confirmed at CES 2026 for 2026 (memory/research.md paper-008).

**Run #3 confirmation:** NVIDIA Q1 FY2027 earnings call (GPUs/paper-021, May 20, 2026, VALIDATED): Jensen Huang explicitly stated Vera Rubin is "sampling with customers" with "production shipments H2 FY2027" (i.e., H2 calendar 2026). Q2 FY2027 guidance of $91B (±2%) — beating consensus by ~$4B — is partially attributed to Vera Rubin production ramp. This is a primary CEO disclosure with $91B Q2 guidance attached; the hardware delivery timeline is now a financial commitment, not merely a roadmap statement. Confidence elevated to the highest tier of "already locked."

- **Key signals:** Q2 FY2027 NVIDIA earnings (August 2026) for first Rubin revenue; CoWoS-L allocation to AMD for MI400.
- **Falsifiers:** a CG-HBM (memory-on-die) yield problem delaying Rubin; HBM4 supply shortfall slipping either product (note: CEO explicitly acknowledged "constrained throughout entire life" — this is the supply constraint, not a delay).

### A3. Liquid cooling becomes the deployment default — **confidence: high** [Run #3: UNCHANGED]
76% of new AI servers liquid-cooled in 2026 (datacenter_hardware/research.md Paper 001); mandatory for all AI GPU racks (GPUs/research.md src-039); NVLink 6 switches require it (interconnects/research.md Implication 4).
- **Key signals:** CDU lead times (currently 20–36 weeks) compressing or extending.
- **Falsifiers:** an air-cooling breakthrough — none is visible in the corpus, so this is near-unfalsifiable for the window.

### A4. GAA nanosheet + backside power delivery universalize — **confidence: high** [Run #3: UNCHANGED]
GAA is in HVM at all three leading foundries; BSPDN ships in Intel 18A now, TSMC N2P H2 2026, universal by end-2027 (chip_fabrication/research.md Paper 001, Paper 015, Trend 2; CPUs/research.md paper-004, paper-014).
- **Key signals:** TSMC N2P BSPDN first-yield data (Q3–Q4 2026) as the leading indicator for A16.
- **Falsifiers:** a BSPDN thermal-dissipation problem (backside heat path partially blocked by power metal) forcing a retreat to frontside power for high-TDP parts.

### A5. Co-packaged optics ships at the switch layer — **confidence: high** [Run #3: UNCHANGED — GF SCALE CPO from Run #2 already incorporated]
Broadcom TH6 (102.4 Tbps) began mass shipping October 2025; NVIDIA Quantum-X/Spectrum-X and TSMC COUPE in production 2026 (photonics/research.md sources 8, 6, 25; interconnects/research.md paper 007). GlobalFoundries launched SCALE CPO (photonics/research.md paper-023, May 4, 2026, VALIDATED), establishing GF as a second OCI MSA-compliant CPO platform alongside TSMC COUPE — reducing single-source risk. A two-vendor CPO ecosystem is more durable than a single-source one.
- **Key signals to watch:** TSMC COUPE volume-production yield; GF SCALE CPO design wins from switch OEMs; CPO field reliability vs. pluggables.
- **Falsifiers:** CPO package yield (CTE-mismatch limited) staying far below pluggable's >99%; ring-modulator thermal sensitivity proving unmanageable in dense switch environments.

### A6. The open-standard wave is ratified and deploying — **confidence: high** [Run #3: UNCHANGED]
CXL 4.0, UCIe 3.0, UALink 1.0, UEC 1.0, PCIe 7.0 all landed in-window (interconnects/research.md papers 001–004, 006, 012). Ratification is locked; deployment timing is the open variable (see Part C).

---

## PART B — 12–24 Month Projection: What Becomes Mainstream (mid-2026 → mid-2028)

### B1. FP4 inference becomes the production default, not just the architecture's design point — **confidence: high** [Run #3: UNCHANGED]
Today FP4 is natively supported (Blackwell NVFP4, CDNA4 MXFP4) but not universal in production — calibration tooling is still maturing. Over 12–24 months, automated FP4 calibration pipelines mature and FP4 becomes the default inference precision, mirroring how FP8 became default in 2023–2025. Edge follows with INT4-plus-entropy-coding (edge_AI_hardware/research.md paper-006).
- **Key signals to watch:** an "FP4 equivalent of LLM.int8()" automated calibration tool reaching production; MLPerf adding FP4-quality benchmarks.
- **Falsifiers:** FP4 quality degradation on reasoning-heavy tasks proving irreducible, keeping FP4 niche.

### B2. Inference workload share crosses two-thirds; inference-specialized silicon goes mainstream — **confidence: high** [Run #3: UNCHANGED]
Inference rises 33%→50%→67% of AI compute 2023→2026 (AI_accelerators/research.md Trend 1). Within 24 months, prefill/decode disaggregation and phase-specialized silicon (Groq-style LPUs, Rubin CPX, TPU v8's training/inference split) become standard deployment architecture.
- **Key signals:** TPU v8 specifications; whether NVIDIA ships the Groq LPU integration in volume Vera Rubin.
- **Falsifiers:** SSM/Mamba-transformer hybrids becoming dominant and collapsing the prefill/decode distinction.

### B3. ARM crosses 30% of the PC market; RISC-V ships credible datacenter silicon — **confidence: medium** [Run #3: UNCHANGED]
ARM PC share is projected to reach ~30% by end-2026 from 13% in 2025 (CPUs/research.md paper-016). RISC-V, post-Ventana, ships server-class silicon targeting EPYC parity (CPUs/research.md paper-008). Within 24 months ARM laptops are mainstream and RISC-V is a credible third datacenter ISA.
- **Key signals:** Canalys ARM PC share quarterly data; native ARM64 performance parity for Office/Chrome/enterprise security software; first Qualcomm-branded RISC-V server announcement.
- **Falsifiers:** ARM PC share stalling below 20%; RISC-V datacenter silicon slipping to 2028+.

### B4. CXL memory pooling becomes standard for LLM inference serving — **confidence: medium** [Run #3: UNCHANGED]
CXL 4.0 (128 GT/s, 100+ TiB pools) released November 2025; production CXL pooling already shows 4.8x inference throughput and 82.7% TTFT reduction (interconnects/research.md paper 003, paper 021; memory/research.md paper-019). Within 24 months CXL KV-cache offload is a standard inference-serving technique.
- **Key signals:** CXL 4.0 multi-rack systems (expected late 2026–2027); hyperscaler CXL instance availability.
- **Falsifiers:** PCIe 7.0 compliance delays (now slipped to 2028) cascading into CXL 4.0 deployment slipping to 2029 — this would push B4 out of the 24-month window.

### B5. On-device 7B-class LLM inference becomes a routine smartphone feature — **confidence: medium** [Run #3: UNCHANGED — thermal falsifier partially addressed, from Run #2]
Mobile NPUs crossed 100 TOPS in Q3–Q4 2025; 2026 flagships routinely ship 100–200 TOPS. But the memory-bandwidth wall keeps *sustained* inference at 1–4B models until LPDDR6 (~80+ GB/s, commercial late 2026) widens slightly (edge_AI_hardware/research.md Trend 1, Trend 6).

arXiv 2604.24785 (edge_AI_hardware/research.md paper-023, April 24, 2026, VALIDATED) demonstrates a critical architectural distinction: mobile SoCs with integrated NPUs throttle to near-zero throughput within 6 inference iterations due to shared thermal domain; dedicated NPU co-processor designs (Hailo-10H on Raspberry Pi 5) achieve near-zero variance across 20+ iterations via separate thermal domain. This refines B5 toward a bifurcated outcome: routine sustained inference arrives first on dedicated-NPU form factors, later on smartphones.

- **Key signals:** LPDDR6 commercial shipment; 5-minute sustained-throughput benchmarks; SoC NPU thermal architecture disclosures.
- **Falsifiers for smartphones:** thermal throttling remaining fundamental to integrated-SoC architecture; practical on-device models capping at 3B on phones even with LPDDR6.
- **Partially mitigated falsifier for dedicated NPU:** the constraint shifts to memory bandwidth, not thermal.

### B6. Rack power density 120 kW → 250–300 kW becomes routine; HVDC 800V emerges — **confidence: medium** [Run #3: UNCHANGED]
GB300 NVL72 already at 250kW+; OCP ORv3-HPR V3 at 300 kW/cabinet deployed by Meta/Google/Microsoft; ORv3-HPR V4 previews 800 kW with 800V HVDC (datacenter_hardware/research.md Paper 011, Trend 1). Within 24 months 250–300 kW racks are routine and 800V HVDC begins deployment.
- **Key signals:** OCP formalizing an 800V HVDC standard; SiC converter supply.
- **Falsifiers:** floor-loading, fire-suppression, or facility chilled-water constraints capping practical density below 300 kW.

### B7. Glass substrates enter limited production for flagship parts — **confidence: medium** [Run #3: UNCHANGED]
Intel debuted EMIB-on-glass January 2026; AMD is qualifying (packaging/research.md Paper 004). Within 24 months glass appears in limited production for the highest-value Intel/AMD packages, at a 2–3x cost premium.
- **Key signals:** glass yield crossing 90%; Absolics/LG Innotek/Samsung capacity announcements.
- **Falsifiers:** glass brittleness/handling keeping yield below 90% and confining glass to samples.

### B8. CoWoS remains sold out; no supply relief inside the window — **confidence: high** [Run #3: UNCHANGED — Samsung 3.3D from Run #2 incorporated]
Even the 4x ramp to 130K wpm does not clear 2026 demand (packaging/research.md; chip_fabrication/research.md Open Question 7). CoPoS panel-level relief is a 2028–2029 story. For the full 24 months, packaging capacity stays the gating constraint.

Samsung's 3.3D advanced packaging (packaging/research.md paper-026, Digitimes May 14, 2026, VALIDATED) targeting mass production Q2 2026, combined with HCB improving thermal resistance by 20% for 16-Hi stacks, represents the most significant development toward a second advanced AI packaging supplier. This does not resolve the CoWoS sold-out thesis for the 24-month window: TSMC CoWoS is ~70% NVIDIA-allocated, and Samsung's 3.3D ramp primarily serves Samsung's own HBM4/HBM4E products — adding capacity on the memory-package side, not the GPU-package side.

- **Key signals:** TSMC quarterly CoWoS capacity vs. NVIDIA+AMD+hyperscaler demand; Samsung Q2 2026 3.3D mass-production confirmation; CoPoS pilot-line progress.
- **Falsifiers:** an AI capex correction collapsing demand; Samsung 3.3D expanding beyond HBM packaging to serve GPU-logic packages at scale.

---

## PART C — 3–5 Year Directional Inference (2028 → 2031) with Scenario Branching

Beyond ~24 months the evidence supports multiple futures. Each trend below is given as a directional bet with explicit scenario branches where the corpus shows genuine uncertainty.

### C1. The memory wall forces an architectural fork — **confidence: medium (direction); scenario-branched (resolution)** [Run #3: UNCHANGED]
HBM4 doubled the interface to 2,048-bit; the corpus is explicit that HBM5 *cannot* simply double again to 4,096-bit (memory/research.md Open Question 8, Scalability). Something has to give within 3–5 years.

- **Scenario C1-a (3D / PIM resolution).** HBM5 goes vertical: DRAM-on-logic monolithic stacking (imec/Kioxia IGZO 3D DRAM, IEDM 2025) plus PIM to cut transfer frequency. Supported by memory/research.md (3D DRAM research, LPDDR6-PIM standardization) and packaging/research.md. **Probability: moderate-to-high.**
- **Scenario C1-b (bandwidth-via-packaging resolution).** Interface width stalls; bandwidth growth shifts entirely to more stacks, higher pin speeds (HBM4E 16 Gbps), and CG-HBM direct die-stacking. **Probability: high as a bridge, insufficient alone past ~2030.**
- **Scenario C1-c (compute-near-memory resolution).** The decode phase migrates off the GPU entirely onto memory-resident compute (PIM, the Groq-LPU logic). **Probability: moderate.**
- **Most likely:** a blend of C1-b near-term and C1-a/C1-c by 2030.
- **Key signals:** IGZO 3D DRAM appearing on a vendor production roadmap; HBM5 interface architecture disclosure.
- **Falsifiers:** an algorithmic breakthrough (radically sub-quadratic attention) that relaxes bandwidth demand.

### C2. The NVLink-vs-open-interconnect contest resolves — **confidence: medium (direction); scenario-branched (winner)** [Run #3: UNCHANGED]
The corpus is unanimous that open standards lag NVLink by 2–4 years, and equally clear that hyperscalers fund the open path as a hedge.

- **Scenario C2-a (NVLink holds).** UALink silicon (late 2026/2027) launches at 800 Gbps x4 into NVLink 6's 3.6 TB/s; the bandwidth deficit is too large; NVLink Fusion co-opts would-be open-camp chipmakers. **Probability: moderate-to-high through 2028.**
- **Scenario C2-b (open ecosystem captures new builds).** UALink 2.0 closes the bandwidth gap; hyperscalers shift *new* cluster builds to UALink/UEC for cost and multi-vendor freedom; custom ASICs anchor the open fabric. **Probability: moderate, rising after 2028.**
- **Most likely:** bifurcation — NVLink dominant in merchant-GPU clusters, open fabrics dominant in hyperscaler custom-silicon clusters.
- **Key signals:** UALink 2.0 specification and bandwidth target; whether UALink silicon ships on schedule in Q4 2026.
- **Falsifiers:** UALink silicon slipping to 2028+ (the GenZ/CCIX/OpenCAPI pattern) would collapse C2-b.

### C3. Power becomes the permanent ceiling on AI scale — **confidence: high (direction)** [Run #3: UNCHANGED]
Datacenter/research.md states it directly: grid power has overtaken compute cost as the binding constraint, and the operators who locked GW-scale interconnections in 2022–2024 have a 5–10 year structural advantage.
- **Scenario C3-a (concentration).** AI compute concentrates in a handful of operators with secured power; the 2-km-radius latency constraint forces dense gigawatt campuses; new entrants are locked out by interconnection queues.
- **Scenario C3-b (relief via on-site generation).** Behind-the-meter generation (hydrogen fuel cells — Bloom/Brookfield $5B; BESS) partially decouple AI build-out from the grid.
- **Most likely:** C3-a dominates through 2028; C3-b provides partial relief after.
- **Key signals:** hyperscaler on-site generation deals; grid interconnection queue lengths; transformer lead times.
- **Falsifiers:** large-scale regulatory reform compressing interconnection timelines; an AI demand plateau.

### C4. Custom hyperscaler silicon captures the majority of inference compute — **confidence: medium** [Run #3: UNCHANGED]
Every hyperscaler now has a custom program; the corpus argues custom silicon beats GPU TCO above ~$100B annual AI spend. Direction: over 3–5 years, custom ASICs take the majority of *inference* compute while NVIDIA holds *training* via the CUDA moat.
- **Key signals:** TPU v8, Trainium4, Maia 200 deployment scale; Anthropic's 1M+ Ironwood commitment playing out.
- **Falsifiers:** NVIDIA's software ecosystem (CUDA, Dynamo) extending its inference lead; custom-silicon development costs proving uneconomic outside the top 3–4 hyperscalers.

### C5. Optical interconnect migrates from package boundary into the die — **confidence: medium** [Run #3: UNCHANGED]
The inward-migration trajectory is unanimous (photonics, interconnects, packaging). The 3–5 year directional bet: in-die optical I/O and dynamic in-package optical routing (CEA-Leti 3.19 pJ/bit, ISSCC 2026; Celestial AI/Marvell) move from research toward production, and >50 mm on-package interconnects become predominantly optical.
- **Key signals:** in-die optical router moving from 28nm research to 5nm production; optical weight memory breakthrough.
- **Falsifiers:** silicon-photonic resonator thermal sensitivity and 5nm integration yield staying unsolved.

### C6. The 2nm-class foundry race stays a three-way contest; geographic diversification matures slowly — **confidence: medium** [Run #3: UPDATED — High-NA bifurcation changes Intel/Samsung scenario]
Yield convergence within ~10% means foundry selection is driven by packaging, customer relationships, and geopolitics rather than raw process superiority over 3–5 years.

**Run #3 update:** ASML CEO Christophe Fouquet confirmed on May 20, 2026 (chip_fabrication/paper-026, VALIDATED) that the first High-NA EUV memory and logic products are expected "within months" — and simultaneously, TSMC confirmed a cost-driven delay to High-NA EUV deployment until 2029. This creates a previously unmodeled **2-year High-NA window (2026–2028)** where Samsung (HBM5, LPDDR6) and Intel (14A logic) are on High-NA while TSMC operates on conventional EUV. This materially changes the C6 scenario probabilities:
- High-NA EUV enables finer via pitch, higher memory density, and potentially better-controlled transistor geometries than TSMC's conventional EUV in the 2026–2028 window.
- Samsung's first High-NA memory products (HBM5 or LPDDR6 dies) may arrive before TSMC's process customers have access to equivalent lithography — a capability reversal for a specific technology class.
- Intel 14A with High-NA, if yield holds, closes the process gap with TSMC N2P/A16 for the 2027–2028 vintage.

- **Scenario C6-a (Intel recovers — strengthened).** Intel 18A/14A secures a Tier-1 external customer by end-2026; with High-NA first-mover advantage through 2028, Intel Foundry becomes a credible TSMC alternative for at least the leading-edge logic segment. **Probability: upgraded from moderate-to-possible toward moderate.**
- **Scenario C6-b (TSMC dominance persists — weakened for 2026–2028 window).** Intel fails to land a Tier-1 customer despite High-NA; the CoWoS packaging moat keeps TSMC structurally ahead anyway; TSMC's existing customer relationships absorb the 2-year lithography gap. **Probability: still moderate-to-high for overall dominance, but less certain for specific product categories where High-NA density matters.**
- **Scenario C6-c (Samsung HBM5 memory differentiation — new).** Samsung's High-NA HBM5 achieves measurably higher stack density or bandwidth than TSMC-manufactured HBM5 base dies during 2026–2028. SK Hynix shifts HBM5 base-die procurement preference toward Samsung Foundry. **Probability: speculative but newly plausible.**
- **Most likely:** C6-b overall through 2027 on total revenue; C6-a partially realized in High-NA-specific product categories (memory, Intel Foundry external logic); C6-c possible as a niche capability statement.
- **Key signals:** First Samsung/Intel High-NA EUV product tape-out confirmation; Intel 14A external-customer commitment by end-2026; TSMC's 2029 High-NA timeline holding vs. being pulled forward.
- **Falsifiers:** TSMC announces High-NA pull-forward to 2027 (cost curve improves faster than expected); Samsung High-NA yield disappoints relative to TSMC's conventional EUV; Intel 14A yield stall; a Taiwan supply disruption.

### C7. Photonic and analog/PIM compute reach pre-commercial maturity but not GPU parity — **confidence: speculative** [Run #3: UNCHANGED]
Photonic neural networks crossed to multi-layer 64-channel chips and a 262 TOPS accelerator in-window; analog in-memory and PIM show 30–34x research speedups. The 3–5 year directional bet: these reach pre-commercial maturity for narrow workloads but do not reach broad GPU performance-per-watt parity within the window — gated by optical weight memory and the analog precision barrier (~6–8 bits vs the 8–16 bits commercial inference needs).
- **Key signals:** an optical/analog weight-memory material breakthrough; a photonic accelerator in a production data center server.
- **Falsifiers (would accelerate the trend):** a PCM or alternative material solving non-volatile optical/analog weight storage with adequate endurance.

---

## Cross-Cutting Falsifiers (would invalidate large parts of this projection)

1. **An AI capital-expenditure correction.** Multiple sectors cite the 2023 transceiver-inventory correction as precedent. A demand collapse would simultaneously relieve CoWoS, HBM, laser, and power bottlenecks — invalidating most of Parts B and C's supply-constrained framing.
2. **An algorithmic breakthrough that relaxes the memory wall.** Radically sub-quadratic attention or attention-free architectures becoming dominant would defer C1 and reorder accelerator design.
3. **A Taiwan supply disruption.** The corpus repeatedly states the 2026–2028 window has no viable mitigation for Taiwan concentration. A disruption would dominate every other trend.
4. **A power-availability ceiling hit sooner than projected.** If grid constraints bind harder than B6/C3 assume, AI compute growth slows regardless of silicon roadmaps.

---

## Summary Table

| # | Trend | Layer | Confidence | Run #3 status | Primary falsifier |
|---|-------|-------|------------|---------------|-------------------|
| A1 | HBM4 becomes the standard AI memory | Near-term | high | UNCHANGED | 16-Hi yield collapse |
| A2 | Rubin + MI400 ship H2 2026 | Near-term | high | UNCHANGED | CG-HBM yield / HBM4 shortfall |
| A3 | Liquid cooling default | Near-term | high | UNCHANGED | Air-cooling breakthrough |
| A4 | GAA + BSPDN universalize | Near-term | high | UNCHANGED | BSPDN thermal problem |
| A5 | CPO at switch layer | Near-term | high | UNCHANGED | CTE-mismatch yield; ring-mod thermal |
| A6 | Open standards ratified | Near-term | high | UNCHANGED | (deployment timing open) |
| B1 | FP4 inference default | 12–24 mo | high | UNCHANGED | Reasoning-task quality loss |
| B2 | Inference-specialized silicon mainstream | 12–24 mo | high | UNCHANGED | SSM/Mamba dominance |
| B3 | ARM 30% PC; RISC-V datacenter | 12–24 mo | medium | UNCHANGED | x86 compatibility stickiness |
| B4 | CXL memory pooling standard | 12–24 mo | medium | UNCHANGED | PCIe 7.0 compliance slip to 2028 |
| B5 | On-device 7B LLM (bifurcated) | 12–24 mo | medium | UNCHANGED | Thermal/bandwidth on integrated SoC |
| B6 | 250–300 kW racks routine | 12–24 mo | medium | UNCHANGED | Floor-load / facility limits |
| B7 | Glass substrates limited production | 12–24 mo | medium | UNCHANGED | Yield stuck below 90% |
| B8 | CoWoS sold out, no relief | 12–24 mo | high | UNCHANGED | AI capex correction |
| C1 | Memory wall architectural fork | 3–5 yr | medium | UNCHANGED | Algorithmic bandwidth relaxation |
| C2 | NVLink-vs-open contest resolves | 3–5 yr | medium | UNCHANGED | UALink silicon delay |
| C3 | Power permanent ceiling | 3–5 yr | high | UNCHANGED | Grid reform / AI demand plateau |
| C4 | Custom silicon majority of inference | 3–5 yr | medium | UNCHANGED | NVIDIA software ecosystem extension |
| C5 | Optical into die | 3–5 yr | medium | UNCHANGED | 5nm resonator yield unsolved |
| C6 | Three-way foundry race + High-NA bifurcation | 3–5 yr | medium | Run #3 UPDATE | Intel 18A/14A yield stall; TSMC High-NA pull-forward |
| C7 | Photonic/analog pre-commercial only | 3–5 yr | speculative | UNCHANGED | Optical weight memory breakthrough |

*Compiled from all 10 hardware sector research files. Research window: 2025-11-23 to 2026-05-23 (Run #3).*
