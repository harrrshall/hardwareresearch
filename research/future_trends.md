# Global Synthesis — Future Trends

**Generated:** 2026-05-23 (Run #4) | **Research window:** 2025-11-23 – 2026-05-23
**Inputs:** 10 sector research files. All projections are extrapolations from in-window evidence; no claims rest on data outside the 2025-11-23 – 2026-05-23 window.
**Confidence legend:** high · medium · speculative.

This file projects forward in three layers: (A) what is already hardening into reality, (B) a 12–24 month projection of what becomes mainstream, and (C) a 3–5 year directional inference with scenario branching where the evidence supports multiple futures.

---

## Run #4 Status (2026-05-23)

Run #4 adds two validated chip_fabrication papers: TSMC 2026 North America Technology Symposium (paper-027) and Apple-Intel/Samsung foundry discussions (paper-028). Both affect the C6 scenario and the A4/B7 near-term trends. All other trends carry forward unchanged.

| Trend | Status | Change vs. Run #3 |
|-------|--------|-------------------|
| A1 HBM4 standard | **UNCHANGED** | No new evidence |
| A2 Rubin/MI400 ship H2 2026 | **UNCHANGED** | CEO lock from Run #3 confirmed |
| A3 Liquid cooling default | **UNCHANGED** | No new evidence |
| A4 GAA+BSPDN universalize | **Run #4 update** | A16 slips to 2027 (paper-027); Intel 18A retains ~15mo BPD lead over TSMC's first commercial SPR node; BSPDN timeline revised |
| A5 CPO at switch layer | **UNCHANGED** | No new evidence |
| A6 Open standards ratified | **UNCHANGED** | No new evidence |
| B1 FP4 default inference | **UNCHANGED** | No new evidence |
| B2 Inference >67%; phase-specialized silicon | **UNCHANGED** | No new evidence |
| B3 ARM ~30% PC; RISC-V datacenter | **UNCHANGED** | No new evidence |
| B4 CXL memory pooling standard | **UNCHANGED** | No new evidence |
| B5 On-device 7B-class LLM | **UNCHANGED** | No new evidence |
| B6 250–300 kW racks routine | **UNCHANGED** | No new evidence |
| B7 Glass substrates limited production | **UNCHANGED** | No new evidence |
| B8 CoWoS sold out; no relief | **UNCHANGED** | No new evidence; A16 slip slightly worsens yield timeline |
| C1 Memory wall architectural fork | **UNCHANGED** | No new evidence |
| C2 NVLink-vs-open contest | **UNCHANGED** | No new evidence |
| C3 Power permanent ceiling | **UNCHANGED** | No new evidence |
| C4 Custom silicon majority of inference | **UNCHANGED** | No new evidence |
| C5 Optical interconnect into die | **UNCHANGED** | No new evidence |
| C6 Three-way foundry race + High-NA bifurcation | **Run #4 UPDATE** | TSMC Symposium confirms A12/A13 (2029) skip High-NA EUV; A16 slips to 2027; Apple considers Intel+Samsung foundry; Samsung High-NA window now ≥3 years |
| C7 Photonic/analog pre-commercial | **UNCHANGED** | No new evidence |

---

## PART A — What Hardens into Reality Next (already locked in by in-window evidence)

These are not predictions so much as the playing-out of commitments already made. Confidence is high across the board because the silicon has taped out, the standards are ratified, or the capacity is committed.

### A1. HBM4 becomes the standard AI memory — **confidence: high** [Run #4: UNCHANGED]
All three vendors are in mass production with 2026 capacity sold out (memory/research.md, papers 001–003). Rubin and MI400 both ship on HBM4 in H2 2026 (GPUs/research.md src-009, src-026; AI_accelerators/research.md paper-004). This is locked.
- **Key signals to watch:** HBM4 16-Hi 48GB yield ramp; whether Samsung's SF4 base die sustains its 13 Gbps lead.
- **Falsifiers:** a 16-Hi stacking yield collapse forcing 12-Hi-only supply; an HBM4 thermal failure mode emerging in volume Rubin/MI400 deployment.

### A2. Rubin and MI400 ship in H2 2026 — **confidence: high** [Run #4: UNCHANGED — CEO lock confirmed in Run #3]
Rubin entered full production at CES 2026 (AI_accelerators/research.md paper-004; interconnects/research.md paper 010); AWS and Google Cloud committed to Vera Rubin NVL72 deployment (GPUs/research.md src-046). MI400 confirmed at CES 2026 for 2026 (memory/research.md paper-008).

NVIDIA Q1 FY2027 earnings (GPUs/paper-021, May 20, 2026, VALIDATED): Jensen Huang explicitly stated Vera Rubin is "sampling with customers" with "production shipments H2 FY2027" (H2 calendar 2026). Q2 FY2027 guidance of $91B (±2%) is partially attributed to Vera Rubin production ramp. This is a financial commitment.

- **Key signals:** Q2 FY2027 NVIDIA earnings (August 2026) for first Rubin revenue; CoWoS-L allocation to AMD for MI400.
- **Falsifiers:** a CG-HBM yield problem delaying Rubin; HBM4 supply shortfall slipping either product.

### A3. Liquid cooling becomes the deployment default — **confidence: high** [Run #4: UNCHANGED]
76% of new AI servers liquid-cooled in 2026 (datacenter_hardware/research.md Paper 001); mandatory for all AI GPU racks; NVLink 6 switches require it (interconnects/research.md Implication 4).
- **Key signals:** CDU lead times (currently 20–36 weeks) compressing or extending.
- **Falsifiers:** an air-cooling breakthrough — none is visible in the corpus.

### A4. GAA nanosheet + backside power delivery universalize — **confidence: high** [Run #4: UPDATED — A16 slips to 2027]
GAA is in HVM at all three leading foundries. Backside power delivery is in production at Intel 18A (PowerVia, HVM Oct 2025) and arriving at TSMC N2P (H2 2026). 

**Run #4 update:** TSMC's A16 (Super Power Rail, its first full commercial BPD node) slipped from late 2026 to 2027 (chip_fabrication/paper-027, TSMC Symposium April 2026). Intel 18A now has a ~15-month backside-BPD lead over TSMC A16. The universalization of BPD is still inevitable — every leading foundry will have it by 2027-2028 — but the timeline has shifted slightly. N2P (H2 2026) carries TSMC's first partial BPD implementation; full SPR production is a 2027 event.

- **Key signals:** TSMC N2P first-yield data (Q3–Q4 2026) as the leading indicator for A16; Intel 18A-P production start (H2 2026) with further power improvements.
- **Falsifiers:** A BSPDN thermal-dissipation problem (backside heat path partially blocked by power metal) forcing a retreat to frontside power for high-TDP parts.

### A5. Co-packaged optics ships at the switch layer — **confidence: high** [Run #4: UNCHANGED]
Broadcom TH6 (102.4 Tbps) began mass shipping October 2025; NVIDIA Quantum-X/Spectrum-X and TSMC COUPE in production 2026 (photonics/research.md sources 8, 6, 25). GlobalFoundries launched SCALE CPO (photonics/research.md paper-023, May 4, 2026), establishing GF as a second OCI MSA-compliant CPO platform. A two-vendor CPO ecosystem is more durable than a single-source one.
- **Key signals:** TSMC COUPE volume-production yield; GF SCALE CPO design wins from switch OEMs.
- **Falsifiers:** CPO package yield staying far below pluggable's >99%; ring-modulator thermal sensitivity proving unmanageable.

### A6. The open-standard wave is ratified and deploying — **confidence: high** [Run #4: UNCHANGED]
CXL 4.0, UCIe 3.0, UALink 1.0, UEC 1.0, PCIe 7.0 all landed in-window (interconnects/research.md papers 001–004, 006, 012). Ratification is locked; deployment timing is the open variable.

---

## PART B — 12–24 Month Projection: What Becomes Mainstream (mid-2026 → mid-2028)

### B1. FP4 inference becomes the production default — **confidence: high** [Run #4: UNCHANGED]
Today FP4 is natively supported (Blackwell NVFP4, CDNA4 MXFP4) but not universal in production. Over 12–24 months, automated FP4 calibration pipelines mature and FP4 becomes the default inference precision.
- **Key signals:** an "FP4 equivalent of LLM.int8()" automated calibration tool reaching production; MLPerf adding FP4-quality benchmarks.
- **Falsifiers:** FP4 quality degradation on reasoning-heavy tasks proving irreducible.

### B2. Inference workload share crosses two-thirds; inference-specialized silicon goes mainstream — **confidence: high** [Run #4: UNCHANGED]
Inference rises 33%→50%→67% of AI compute 2023→2026. Within 24 months, prefill/decode disaggregation and phase-specialized silicon (Groq-style LPUs, Rubin CPX, TPU v8's training/inference split) become standard deployment architecture.
- **Key signals:** TPU v8 specifications; whether NVIDIA ships the Groq LPU integration in volume Vera Rubin.
- **Falsifiers:** SSM/Mamba-transformer hybrids becoming dominant and collapsing the prefill/decode distinction.

### B3. ARM crosses 30% of the PC market; RISC-V ships credible datacenter silicon — **confidence: medium** [Run #4: UNCHANGED]
ARM PC share projected to reach ~30% by end-2026 from 13% in 2025. RISC-V, post-Ventana, ships server-class silicon targeting EPYC parity.
- **Key signals:** Canalys ARM PC share data; first Qualcomm-branded RISC-V server announcement.
- **Falsifiers:** ARM PC share stalling below 20%; RISC-V datacenter silicon slipping to 2028+.

### B4. CXL memory pooling becomes standard for LLM inference serving — **confidence: medium** [Run #4: UNCHANGED]
CXL 4.0 released November 2025; production CXL pooling already shows 4.8x inference throughput. Within 24 months CXL KV-cache offload is a standard inference-serving technique.
- **Key signals:** CXL 4.0 multi-rack systems (expected late 2026–2027); hyperscaler CXL instance availability.
- **Falsifiers:** PCIe 7.0 compliance delays (now slipped to 2028) cascading into CXL 4.0 deployment slipping to 2029.

### B5. On-device 7B-class LLM inference becomes a routine smartphone feature — **confidence: medium** [Run #4: UNCHANGED]
Mobile NPUs crossed 100 TOPS in Q3–Q4 2025. The thermal bifurcation (dedicated NPU co-processor class vs. integrated SoC NPU class) is now empirically established (edge_AI_hardware/research.md paper-023 and paper-024).
- **Key signals:** LPDDR6 commercial shipment; 5-minute sustained-throughput benchmarks.
- **Falsifiers:** thermal throttling remaining fundamental to integrated-SoC architecture.

### B6. Rack power density 120 kW → 250–300 kW becomes routine; HVDC 800V emerges — **confidence: medium** [Run #4: UNCHANGED]
GB300 NVL72 already at 250kW+; OCP ORv3-HPR V3 at 300 kW/cabinet deployed by Meta/Google/Microsoft.
- **Key signals:** OCP formalizing an 800V HVDC standard; SiC converter supply.
- **Falsifiers:** floor-loading or facility constraints capping practical density below 300 kW.

### B7. Glass substrates enter limited production for flagship parts — **confidence: medium** [Run #4: UNCHANGED]
Intel debuted EMIB-on-glass January 2026; AMD qualifying (packaging/research.md Paper 004). Within 24 months glass appears in limited production.
- **Key signals:** glass yield crossing 90%; Absolics/LG Innotek/Samsung capacity announcements.
- **Falsifiers:** glass brittleness/handling keeping yield below 90%.

### B8. CoWoS remains sold out; no supply relief inside the window — **confidence: high** [Run #4: UNCHANGED]
Even the 4x ramp to 130K wpm does not clear 2026 demand. CoPoS panel-level relief is a 2028–2029 story.

Samsung's 3.3D advanced packaging (packaging/research.md paper-026, Run #2) targeting Q2 2026 mass production with HCB represents the most significant second-supplier development, but this does not resolve the CoWoS sold-out thesis for the 24-month window.
- **Key signals:** TSMC quarterly CoWoS capacity vs demand; Samsung Q2 2026 3.3D confirmation.
- **Falsifiers:** an AI capex correction collapsing demand; Samsung 3.3D expanding beyond HBM packaging.

---

## PART C — 3–5 Year Directional Inference (2028 → 2031) with Scenario Branching

Beyond ~24 months the evidence supports multiple futures.

### C1. The memory wall forces an architectural fork — **confidence: medium** [Run #4: UNCHANGED]
HBM4 doubled the interface to 2,048-bit; the corpus is explicit that HBM5 *cannot* simply double again to 4,096-bit. Something has to give within 3–5 years.

- **Scenario C1-a:** HBM5 goes vertical (DRAM-on-logic monolithic stacking + PIM). **Probability: moderate-to-high.**
- **Scenario C1-b:** Interface width stalls; bandwidth growth shifts to more stacks, higher pin speeds (HBM4E 16 Gbps), and CG-HBM. **Probability: high as bridge.**
- **Scenario C1-c:** Decode migrates off GPU onto memory-resident compute (PIM, Groq-LPU logic). **Probability: moderate.**
- **Most likely:** blend of C1-b near-term and C1-a/C1-c by 2030.
- **Falsifiers:** algorithmic breakthrough relaxing bandwidth demand.

### C2. The NVLink-vs-open-interconnect contest resolves — **confidence: medium** [Run #4: UNCHANGED]
- **Scenario C2-a (NVLink holds):** UALink silicon at 800 Gbps x4 vs NVLink 6's 3.6 TB/s; bandwidth deficit too large. **Probability: moderate-to-high through 2028.**
- **Scenario C2-b (open ecosystem captures new builds):** UALink 2.0 closes bandwidth gap; hyperscalers shift new cluster builds. **Probability: moderate, rising after 2028.**
- **Most likely:** bifurcation — NVLink dominant in merchant-GPU clusters, open fabrics dominant in hyperscaler custom-silicon clusters.

### C3. Power becomes the permanent ceiling on AI scale — **confidence: high** [Run #4: UNCHANGED]
Datacenter/research.md: grid power has overtaken compute cost as the binding constraint.
- **Scenario C3-a (concentration):** AI compute concentrates in operators with secured power.
- **Scenario C3-b (relief via on-site generation):** Behind-the-meter generation partially decouples AI from the grid.
- **Most likely:** C3-a dominates through 2028; C3-b provides partial relief after.

### C4. Custom hyperscaler silicon captures the majority of inference compute — **confidence: medium** [Run #4: UNCHANGED]
Direction: over 3–5 years, custom ASICs take the majority of *inference* compute while NVIDIA holds *training* via the CUDA moat.
- **Falsifiers:** NVIDIA's software ecosystem (CUDA, Dynamo) extending its inference lead.

### C5. Optical interconnect migrates from package boundary into the die — **confidence: medium** [Run #4: UNCHANGED]
The 3–5 year directional bet: in-die optical I/O (CEA-Leti 3.19 pJ/bit, ISSCC 2026; Celestial AI/Marvell) moves from research toward production.
- **Falsifiers:** silicon-photonic resonator thermal sensitivity and 5nm integration yield staying unsolved.

### C6. The 2nm-class foundry race stays a three-way contest; geographic diversification matures slowly — **confidence: medium** [Run #4: MAJOR UPDATE]

**Run #4 update:** TSMC's 2026 North America Technology Symposium (paper-027) confirms that A12 and A13 (both targeted for 2029, TSMC's leading nodes) will **not** use High-NA EUV. Combined with A16 slipping to 2027, the Samsung/Intel High-NA first-mover window is now structural and ≥3 years, not a single-node 2-year gap.

Furthermore, Apple's early-stage discussions with Intel Foundry Services and Samsung (paper-028, Bloomberg May 5, 2026) represent the first credible signal that Apple may diversify chip manufacturing away from TSMC exclusive — a development that, if realized, would simultaneously validate Intel IFS, strengthen Samsung Foundry's US presence, and free a portion of TSMC N2 for AI chip customers.

- **Scenario C6-a (Intel recovers — further strengthened):** Intel 18A yield ramps, lands Apple as a customer for lower-end chips by 2027; Intel 14A with High-NA first-mover advantage continues through 2028-2029 as TSMC's A12/A13 stay on conventional EUV. Intel Foundry becomes a credible TSMC alternative for at least leading-edge logic and memory base-die segments. **Probability: upgraded from moderate toward moderate-to-high for the foundry credibility question; timeline constrained by Apple design transfer complexity.**

- **Scenario C6-b (TSMC dominance persists — weakened for 2026-2029 window):** Intel fails to land Apple despite discussions; Samsung High-NA yield disappoints; TSMC's CoWoS packaging moat keeps customers locked regardless. **Probability: still moderate-to-high for total revenue; now more uncertain for process-leadership claims in specific product categories.**

- **Scenario C6-c (Samsung HBM5 memory differentiation — strengthened):** Samsung's High-NA HBM5 achieves measurably higher stack density or bandwidth than TSMC-manufactured HBM5 base dies. SK Hynix shifts HBM5 base-die procurement toward Samsung Foundry. **Probability: elevated from speculative to speculative-to-medium.** The TSMC Symposium's confirmation that TSMC's entire 2029 logic roadmap skips High-NA makes C6-c more concrete: Samsung (High-NA HBM5 base die) vs. TSMC conventional EUV is no longer speculative — it is the stated foundry trajectory.

- **Most likely:** C6-b overall through 2027 on total revenue; C6-a partially realized in specific categories (Apple lower-end, Intel Foundry external logic, High-NA niche); C6-c emerging as a Samsung memory differentiation story by 2027-2028.

- **Key signals:** Intel 14A external-customer tape-out announcement; Samsung or SK Hynix announcing HBM5 base-die process details; TSMC announcing any High-NA pull-forward to 2027 (would falsify C6-a/C6-c).
- **Falsifiers:** TSMC announces High-NA pull-forward to 2027; Samsung SF1.4 High-NA yield < 50%; Intel 14A yield stalls; Apple-Intel-Samsung discussions collapse.

### C7. Photonic and analog/PIM compute reach pre-commercial maturity but not GPU parity — **confidence: speculative** [Run #4: UNCHANGED]
Photonic neural networks crossed to multi-layer 64-channel chips and a 262 TOPS accelerator in-window; analog in-memory and PIM show 30–34x research speedups. The 3–5 year directional bet: these reach pre-commercial maturity for narrow workloads but do not reach broad GPU performance-per-watt parity within the window.
- **Falsifiers (would accelerate):** a PCM or alternative material solving non-volatile optical/analog weight storage.

---

## Cross-Cutting Falsifiers (would invalidate large parts of this projection)

1. **An AI capital-expenditure correction.** A demand collapse would simultaneously relieve CoWoS, HBM, laser, and power bottlenecks.
2. **An algorithmic breakthrough that relaxes the memory wall.** Radically sub-quadratic attention or attention-free architectures becoming dominant.
3. **A Taiwan supply disruption.** The corpus repeatedly states the 2026–2028 window has no viable mitigation for Taiwan concentration.
4. **A power-availability ceiling hit sooner than projected.** Grid constraints binding harder than B6/C3 assume.

---

## Summary Table

| # | Trend | Layer | Confidence | Run #4 status | Primary falsifier |
|---|-------|-------|------------|---------------|-------------------|
| A1 | HBM4 becomes the standard AI memory | Near-term | high | UNCHANGED | 16-Hi yield collapse |
| A2 | Rubin + MI400 ship H2 2026 | Near-term | high | UNCHANGED | CG-HBM yield / HBM4 shortfall |
| A3 | Liquid cooling default | Near-term | high | UNCHANGED | Air-cooling breakthrough |
| A4 | GAA + BSPDN universalize | Near-term | high | Run #4 UPDATE | BSPDN thermal problem; A16 slips to 2027 |
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
| C6 | Three-way foundry race + High-NA bifurcation | 3–5 yr | medium | Run #4 MAJOR UPDATE | Intel 18A/14A yield stall; TSMC High-NA pull-forward; Samsung SF1.4 yield < 50% |
| C7 | Photonic/analog pre-commercial only | 3–5 yr | speculative | UNCHANGED | Optical weight memory breakthrough |

*Compiled from all 10 hardware sector research files. Research window: 2025-11-23 to 2026-05-23 (Run #4).*
