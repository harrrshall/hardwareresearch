# Opportunity Shortlist — Run #4 — 2026-05-23

**Regenerated every cycle. Signal-only. ALREADY-PRICED-IN items excluded entirely.**  
**Verification:** Independent Market Pricing Verification Agent (separate context, fresh web searches)  
**Tally this cycle:** 0 VERIFIED-NOT-PRICED-IN · 15 PARTIALLY-PRICED-IN · 0 ALREADY-PRICED-IN

---

## Tier 1 — Verified Non-Consensus

*No VERIFIED-NOT-PRICED-IN findings this cycle. Run #4 verification found zero items that are genuinely non-consensus across all major analyst, vendor, and financial press coverage. All surviving opportunities are PARTIALLY-PRICED-IN (Tier 2). This is an honest result — not every cycle produces Tier 1 opportunities.*

---

## Tier 2 — Partially Priced (window is closing; act before consensus catches up)

---

### T2-A: Grid Ceiling Converts the AI Race into a TFLOPS-per-Watt Contest — Market Still Scores FLOPS

**Opportunity:** Long efficiency-per-watt leaders (Google TPU via Alphabet, custom-silicon hyperscalers) against consensus which assigns AI hardware value capture primarily to NVIDIA's accelerator revenue share.

**The bet:** In a grid-constrained datacenter world (PJM load queue 10x oversubscribed; 5–7 year interconnect lead times), deployable intelligence = megawatts × TFLOPS/W. TPU v7 Ironwood at 29.4 TFLOPS/W vs B200 at 3.75 TFLOPS/W = ~8x efficiency delta. Hyperscalers running internal silicon at 8x efficiency capture a structurally growing share of deployed intelligence per megawatt while buying fewer NVIDIA chips. The market assigns ~90% of AI accelerator forward value to NVIDIA's accelerator revenue share; the compound efficiency math says this overstates NVIDIA's deployed-compute capture in a power-capped regime.

**Why still mispriced:** "Tokens per watt" framing entered mainstream investor vocabulary at GTC 2026 (NVIDIA's own marketing). The broad narrative is priced. The specific *portfolio implication* — long vertically-integrated efficiency leaders against NVIDIA's revenue-share-as-forward-value-capture — has not appeared in a sell-side model. No Goldman, Morgan Stanley, or Bernstein note was found re-weighting NVIDIA's forward value on a deployed-compute-per-megawatt axis.

**Catalyst:** NVIDIA Q2 FY2027 earnings (August 2026) — if data center revenue growth rate decelerates even modestly while hyperscaler CapEx continues rising, the delta becomes visible. Alternatively: any hyperscaler disclosing TPU-vs-GPU efficiency comparison in a public earnings call or infrastructure report.

**Action window:** Medium (12–36 months).

**Falsifier:** NVIDIA introduces a Vera Rubin-class architecture achieving >15 TFLOPS/W at rack level, narrowing the efficiency gap to <3x vs TPU v7. Or a hyperscaler announces return to NVIDIA-dominant compute strategy over internal silicon.

**Cross-reference:** cross_sector_alpha.md Finding 1; datacenter_hardware/research.md; AI_accelerators/research.md (3.4 Energy Efficiency, Trend 4); GPUs/research.md (paper-021).

---

### T2-B: Compound Packaging Yield (Not CoWoS wpm) Is the Real Compute Ceiling

**Opportunity:** Long CoWoS-adjacent supply chain precision plays — advanced substrate suppliers, die-attach process IP holders, HBM4 base-die yield improvement tooling. The CoWoS wpm expansion narrative overstates good-units output because the compound yield conversion ratio is falling.

**The bet:** Compound yield of a Rubin-class package = HBM4 16-Hi stack yield (~72.4%, per 0.98^16) × multi-chiplet assembly yield (~69–90%) × interposer yield (degrading above 5x reticle). TSMC's headline wpm expansion does not translate linearly to good accelerators. NVIDIA CEO confirmed "constrained throughout the entire life of Vera Rubin" — supply constraint is multi-year. The market models the constraint as a wpm problem; the compound yield math makes it a yield problem that wpm expansion alone cannot solve.

**Why still mispriced:** CoWoS scarcity is consensus and fully priced. The *mechanism* — that wpm-to-good-units conversion ratio is falling as HBM4 16-Hi and CG-HBM raise the compounding yield math — has not been modeled in sell-side. Specialist Substack pieces approach it; no Goldman/Bernstein note executes the multiplication.

**Catalyst:** TSMC N2/CoWoS yield data in H2 2026 earnings; NVIDIA Vera Rubin shipment ramp vs guidance delta in Q3/Q4 FY2027 (Nov 2026, Feb 2027).

**Action window:** Medium (12–24 months).

**Falsifier:** TSMC discloses Rubin-class CoWoS yield at or above 80% good-unit throughput; or CG-HBM yield validates at >85%, reducing the compounding assembly risk significantly.

**Cross-reference:** cross_sector_alpha.md Finding 2; GPUs/research.md (paper-021, HBM4 Supply Transition); memory/research.md; packaging/research.md; chip_fabrication/research.md (paper-012).

---

### T2-C: CG-HBM and CXL 4.0 Are Two Independent Attacks on the Silicon Interposer

**Opportunity:** Hedge against CoWoS scarcity premium (position to short CoWoS substrate suppliers in 2027–2028 timeframe) or position in memory disaggregation enablers (Ayar Labs optical chiplets, Astera Labs CXL switch ICs).

**The bet:** The entire AI hardware bull thesis has CoWoS interposer scarcity baked in. Two independent roadmap developments are demand-destroying for the interposer: (1) CG-HBM — Rubin's HBM4 stacked directly on the GPU logic die, eliminating the interposer for memory connection; (2) CXL 4.0 + optical disaggregation — if KV-cache and warm weights migrate to optically-attached CXL memory pools, each GPU needs fewer co-packaged HBM stacks. If either lands at volume, the scarce asset partially de-rates from within.

**Why still mispriced:** CG-HBM existence is known in trade press; CXL 4.0 is covered. The *investment thesis* — that both are demand-destroying for the interposer simultaneously — is not found in any mainstream sell-side note. The Register's "memory godboxes" piece (May 2026) is entering mainstream tech press but framed as a capacity-expansion play, not an interposer-disruption trade.

**Catalyst:** NVIDIA disclosing CG-HBM yield data in 2026 technical publications; or first production CXL 4.0 + optical memory disaggregation deployment at a hyperscaler (H2 2026 – 2027).

**Action window:** Medium-to-long.

**Falsifier:** NVIDIA publicly reports CG-HBM yield below 60% and abandons it for Rubin production; CXL 4.0 slips beyond 2029; optical memory disaggregation fails to close the latency gap vs co-packaged HBM.

**Cross-reference:** cross_sector_alpha.md Finding 4; GPUs/research.md (Rubin Architecture); interconnects/research.md (CXL 3.0/4.0, Optical sections); packaging/research.md.

---

### T2-D: CXL 4.0 Is Hostage to a PCIe 7.0 Compliance Slip — Memory-Wall Fix Expected 2027 May Be 2029

**Opportunity:** Position in CXL 3.0 infrastructure suppliers (Astera Labs CXL switches, Samsung/SK Hynix CXL memory modules) as the 2025–2027 bridge; avoid pricing in 2027-production assumptions for CXL 4.0. Short any thesis that assumes widespread CXL 4.0 AI memory pooling before 2028.

**The bet:** CXL 4.0 (1.5 TB/s bundled bandwidth) is built on the PCIe 7.0 physical layer. PCIe 7.0 compliance program slipped to 2028 (from 2027). The memory and accelerator sectors assume "CXL 4.0 multi-rack systems in late 2026–2027"; the interconnects sector's compliance-slip data implies 2028–2029 for production AI memory pooling at that bandwidth level. PCI-SIG advancing PCIe 8.0 Draft 0.5 (May 2026, paper-023) while PCIe 7.0 compliance remains unresolved confirms the pattern.

**Why still mispriced:** PCIe 7.0 compliance delay is reported in mainstream tech press (Tom's Hardware). The downstream implication — CXL 4.0 AI memory pooling slips to 2029 — has not been quantified in a sell-side report. CXL market forecasts project "$15B by 2028" without incorporating this risk.

**Catalyst:** PCIe 7.0 compliance test suite publication (expected 2028); CXL Consortium official CXL 4.0 device availability timeline update; any hyperscaler announcing a CXL 4.0 deployment delay.

**Action window:** Medium (12–30 months).

**Falsifier:** PCI-SIG issues PCIe 7.0 compliance program ahead of schedule (before end-2027); CXL 4.0 devices ship in volume via FPGA bridge chips that sidestep compliance requirements.

**Cross-reference:** cross_sector_alpha.md Finding 5; interconnects/research.md (PCIe 7.0, CXL sections, paper-023 PCIe 8.0); memory/research.md (CXL Memory Expansion).

---

### T2-E: CPO Laser Supply — EML Second Wave and Laser-Free Alternatives Are the Real Trade

**Opportunity:** Long EML second-wave qualifiers (II-VI/Coherent expanding 200G/lane capacity), integrated InP laser IP holders, GaN microLED companies (Avicena). Not Lumentum and Coherent at current multiples (those are the priced-in first wave).

**The bet:** CPO as an architecture is consensus and priced. The pick-and-shovel play — 200G/lane EML laser supply — is becoming mainstream (NVIDIA $4B Lumentum+Coherent investment). The non-consensus trade is: (a) second-wave EML qualifiers who benefit from the supply shortfall the priced-in duopoly creates, and (b) laser-free alternatives (Avicena GaN microLED at 80–200 fJ/bit, Intel OCI integrated InP) that become cost-competitive if the shortage persists through 2028. GF SCALE CPO (May 2026, photonics paper-023) adds a second CPO platform that increases aggregate EML demand without solving supply — widening the shortfall.

**Why still mispriced:** Generic EML shortage and Lumentum/Coherent are priced. Lumentum Q2 FY2026 8-K confirms monopoly-supplier status with 200G EML at ~5% of quarterly revenue, targeting 25% by end 2026. Second-wave EML qualifiers and laser-free alternatives are not in mainstream analyst coverage.

**Catalyst:** Any hyperscaler announcing multi-supplier EML qualification; first commercial GaN microLED CPO demonstration at >400G/lane; McKinsey 2026 optical supply chain update.

**Action window:** Short-to-medium (0–24 months).

**Falsifier:** Three additional EML manufacturers qualify 200G/lane before mid-2027, collapsing the supply premium; GaN microLED speed remains capped below 100G/lane.

**Cross-reference:** market_opportunities.md Opp 1; photonics/research.md (EML Laser Supply, GF SCALE CPO paper-023); interconnects/research.md (CPO section).

---

### T2-F: Edge AI Memory-Bandwidth Arbitrage — Dedicated NPU Co-Processor + Thermal Isolation Is the Winning Architecture

**Opportunity:** Long dedicated edge NPU co-processor suppliers (Hailo, NXP eIQ Neutron class), on-module LPDDR suppliers, and compiler-hardware co-design IP. Short integrated SoC NPU suppliers claiming TOPS leadership without addressing thermal and bandwidth constraints.

**The bet:** The edge AI hardware landscape is saturated with TOPS claims. Empirical data (arXiv 2604.24785) shows integrated SoC NPUs (Galaxy S24, Pixel 9) lose ≥50% throughput within 6 inference iterations due to shared thermal domain; dedicated NPU co-processors (Hailo-10H on Raspberry Pi 5) sustain near-zero variance across 20+ iterations via separate thermal domain + on-module LPDDR4X. LlamaWeb (arXiv 2605.20706) confirms 2.7× best/worst GPU performance gap in WebGPU inference — thermal and bandwidth architecture matters more than raw TOPS.

**Why still mispriced:** Hailo is private. The thermal isolation advantage as an investment thesis has not appeared in Apple, Qualcomm, or MediaTek sell-side notes. The market values NPU TOPS in flagship SoC specs. Market-size coverage of edge AI is broadening (Mordor Intelligence, IDTechEx) but thermal isolation as the specific moat is non-consensus.

**Catalyst:** Large OEM announcing a dedicated NPU co-processor design win citing thermal sustainability; Hailo IPO or acquisition premium; mobile HBM (projected 2028) reaching qualification for first dedicated edge AI device.

**Action window:** Medium-to-long (12–48 months).

**Falsifier:** Apple or Qualcomm solve thermal NPU domain separation inside an integrated SoC at the next node; mobile HBM arrives before 2028 and gives integrated SoCs the bandwidth fix.

**Cross-reference:** market_opportunities.md Opp 2; edge_AI_hardware/research.md (paper-017, paper-023, paper-024 LlamaWeb); memory/research.md.

---

### T2-G: Processing-in-Memory at the JEDEC Standardization Inflection — Long the Tooling Layer

**Opportunity:** Long PIM controller IP, compiler tooling, and testing equipment companies (Rambus PIM IP, Synopsys PIM compiler tooling, Keysight for PIM validation). Not Samsung/SK Hynix directly (memory module margin is captured by standards).

**The bet:** Samsung and SK Hynix — direct competitors — are jointly standardizing LPDDR6-PIM through JEDEC. JEDEC previewed the LPDDR6-PIM roadmap in April 2026 as "nearing completion" — the base LPDDR6 standard has been released; the PIM extension is in preview with no final board-approval date set. Standards convert PIM from niche to commodity module OEMs will demand. The asymmetric trade is on the controller IP, compiler, and testing layer that standardized PIM requires — small revenue today that scales with every LPDDR6-PIM socket shipped.

**Why still mispriced:** JEDEC standardization is publicly reported; the PIM extension is not yet ratified. No buy-side or sell-side note recommends PIM tooling names on the standardization-as-catalyst thesis. The catalyst has not yet fired — the trigger remains pending board approval.

**Catalyst:** JEDEC LPDDR6-PIM standard ratification (expected 2026–2027 per preview timeline); first OEM announcing LPDDR6-PIM support in a product roadmap; Samsung/SK Hynix announcing LPDDR6-PIM module availability.

**Action window:** Medium (12–36 months).

**Falsifier:** JEDEC LPDDR6-PIM delayed beyond 2027; memory vendors vertically integrate PIM controller IP in-house.

**Cross-reference:** market_opportunities.md Opp 3; memory/research.md (PIM/HBM-PIM, JEDEC section); AI_accelerators/research.md (paper-013 HPIM).

---

### T2-H: In-Die / In-Package Optical Routing — The Post-CPO Architectural Discontinuity

**Opportunity:** Long in-die optical routing IP beyond Marvell/Celestial AI — CEA-Leti licensees, TSMC CoWoS-Photonic roadmap suppliers, Ayar Labs (UCIe optical chiplet). The Marvell/Celestial AI acquisition is already priced into Marvell's multiple; the second-mover IP play is not.

**The bet:** CPO is consensus. The non-consensus architectural step is in-die optical I/O — routing signals inside the die at optical speeds, eliminating SerDes entirely. CEA-Leti demonstrated 3.19 pJ/bit electro-optical routing with 18 ns switching at ISSCC 2026 — below CPO on interposer (3.5 pJ/bit). This is a discontinuity: if in-die optical routing reaches production, it obsoletes CPO from the inside.

**Why still mispriced:** The Marvell/Celestial AI trade is ALREADY-PRICED-IN (33 Buy ratings, closed February 2, 2026). The broader in-die optical routing architectural disruption — beyond Marvell — is in no mainstream sell-side coverage. No new sell-side coverage of the CEA-Leti ISSCC 2026 in-die optical routing result as a distinct investable category beyond Marvell was found in Run #4 re-verification.

**Catalyst:** TSMC announcing a photonic-integrated CoWoS variant; any hyperscaler announcing an in-die optical I/O qualification program; Ayar Labs UCIe optical chiplet entering production at a named customer.

**Action window:** Long (3–5 years).

**Falsifier:** CEA-Leti-type in-die optical routing fails to scale to production due to thermal or yield constraints; Ayar TeraPHY remains limited to niche HPC applications.

**Cross-reference:** market_opportunities.md Opp 4; interconnects/research.md (Celestial AI, Ayar TeraPHY, ISSCC 2026 electro-optical router); photonics/research.md.

---

### T2-I: Open-Interconnect (UALink / UEC / UCIe) Delayed-but-Real Window

**Opportunity:** Long UALink silicon switch IP vendors and UEC silicon vendors (Broadcom Tomahawk 7, Cisco G300 with UEC support) for 2026–2027 cluster build inflection. Also long UCIe IP licensees (Cadence, Synopsys) as chiplet adoption forces standardized die-to-die interfaces.

**The bet:** UALink 2.0 (April 7, 2026): 200 GT/s, supports 1,024+ GPUs. When UALink silicon ships (late 2026/2027), the switching-cost story inverts for new cluster builds. Notable: The Register confirmed UALink 2.0 spec shipped *before* UALink 1.0 silicon — Upscale AI targets Q4 2026 for first switch product. Consensus over-prices the open-standard lag by assuming NVLink's head start is permanent.

**Why still mispriced:** UALink coverage is in specialist circles. The specific investment thesis — that consensus over-prices the lag — is not in mainstream sell-side. No NVIDIA sell-side bear case models the UALink silicon milestone as a concrete NVLink risk. The 2.0-spec-before-1.0-silicon pattern (same as GenZ/CCIX/OpenCAPI history) adds execution risk but does not extinguish the thesis.

**Catalyst:** First production UALink silicon shipping to a named hyperscaler customer (late 2026); AMD MI500 cluster announcement using UALink fabric; UEC 1.0-certified Ethernet switch shipping at scale.

**Action window:** Medium (18–36 months).

**Falsifier:** UALink silicon availability slips beyond mid-2027; hyperscalers that backed UALink continue buying NVLink clusters for 2028+ anyway; UALink fails to achieve 1,024-GPU cluster interoperability in production.

**Cross-reference:** market_opportunities.md Opp 5; interconnects/research.md (UALink, UEC, UCIe sections).

---

### T2-J: Glass Substrates at the Qualification Inflection — Long Before the Transition Is Priced as Inevitable

**Opportunity:** Long glass substrate material suppliers (Absolics, LG Innotek, Corning's specialty glass division) and glass substrate tooling/equipment companies. The qualification inflection (Intel NEPCON January 2026 demo, AMD Absolics volume samples) is the highest-leverage entry point.

**The bet:** Intel demonstrated EMIB-on-glass at NEPCON Japan in January 2026; AMD is receiving volume qualification samples from Absolics (MI400-series, January 2026 — not just R&D sampling). MIT Technology Review published "Future AI chips could be built on glass" (March 2026), signaling transition from specialist to mainstream conversation. The industry is at the inflection from qualification to ramp — exactly where materials transitions offer the highest leverage before "glass substrate is coming" becomes consensus.

**Why still mispriced:** Trade press and now mainstream science press cover the qualification milestones. The investable names (Absolics/SKC, LPKF, LG Innotek) remain in specialist/investor-newsletter coverage, not in formal Goldman/MS/Bernstein equity research. Analyst specialist LPKF piece explicitly flags timing risk ("S-Curve Is Bending Upward — But Timing Is Everything"). No mainstream sell-side initiation found.

**Catalyst:** Intel or AMD announcing glass substrate production ramp dates at a packaging conference (mid-2026 through 2027); TSMC announcing glass substrate qualification for CoWoS-G; first volume production order for glass substrate AI packages.

**Action window:** Medium-to-long (18–48 months).

**Falsifier:** Intel or AMD delays glass substrate qualification beyond 2028; hybrid glass-organic substrates prove to offer equivalent performance at lower cost.

**Cross-reference:** market_opportunities.md Opp 6; packaging/research.md; chip_fabrication/research.md.

---

### T2-K: RISC-V Datacenter Silicon Post-Ventana — Open-ISA Moving Up-Market

**Opportunity:** Long RISC-V IP companies exposed to datacenter and AI (SiFive, Tenstorrent via RISC-V Tensix, Ventana now inside Qualcomm) and RISC-V toolchain/ecosystem enablers. The opportunity is pre-revenue-ramp positioning before datacenter RISC-V reaches analyst attention.

**The bet:** RISC-V crossed the datacenter credibility threshold in this window: Qualcomm paid $2.4B for Ventana, SiFive P570 Gen 3 achieved 21x AI improvement, RISC-V reached 25% CPU IP market share by end-2025. Scaleway (European cloud provider) launched RISC-V cloud server instances in 2026 — the first concrete datacenter design win beyond proof-of-concept. The market still prices RISC-V as embedded-only.

**Why still mispriced:** The Qualcomm/Ventana deal is priced into Qualcomm's stock narrative. The rerating of RISC-V from embedded-only to datacenter-capable is not in sell-side models. Ventana revenue is $37M in 2025. Scaleway is a niche European provider — the revenue implication is minimal and no mainstream sell-side rerating was triggered.

**Catalyst:** Ventana Veyron V2 volume production announcement from Qualcomm (2026–2027); hyperscaler announcing RISC-V custom server SoC; RISC-V Linux kernel support reaching full parity with x86/ARM.

**Action window:** Long (2–5 years).

**Falsifier:** ARM responds with aggressive datacenter licensing cuts; x86/ARM incumbency in cloud software tooling proves too sticky without a major hyperscaler anchor customer by 2028.

**Cross-reference:** market_opportunities.md Opp 7; CPUs/research.md (Ventana, SiFive, RISC-V sections); AI_accelerators/research.md (Tenstorrent, Trend 5).

---

### T2-L: High-NA EUV ≥3-Year First-Mover Window — TSMC's Entire 2029 Roadmap Skips High-NA *(STRENGTHENED — Run #4)*

**Opportunity:** Long Intel Foundry Services capacity and Samsung Foundry's HBM5/memory differentiation; specifically, memory buyers who could access a Samsung High-NA advantage on HBM5 base-die density.

**The bet:** TSMC's 2026 North America Technology Symposium (April 22–23) is the primary source confirming that A12 *and* A13 — TSMC's two 2029-class nodes — both skip High-NA EUV. This extends the Samsung/Intel first-mover advantage from a "2-year window" (A14 only) to a **structural ≥3-year multi-node divergence** across TSMC's entire leading-edge roadmap through end of decade. A16 slipped to 2027; A13 and A12 (both 2029) confirmed no High-NA EUV. Intel retains ~15-month backside power delivery (BPD) lead over TSMC A16. Samsung is reportedly pursuing a 2nm base die for HBM5 (TrendForce, March 2026), where High-NA enables tighter via pitch and higher density than TSMC's conventional-EUV-process HBM5 — a capability delta no sell-side model has quantified. ASML CEO confirmed first High-NA memory and logic products "within months" (May 2026).

**Why still mispriced:** TSMC's delay facts are now broadly covered: TrendForce, Tom's Hardware, WCCFTech, Electronics Weekly, 01.co Research all reported the A12/A13 High-NA skip after the Symposium. Bernstein had previously flagged the A14 delay as "already baked in" for TSMC stock. The TSMC-stock-specific angle is close to fully priced. What remains non-consensus: (1) no sell-side note has quantified this as a **multi-node structural gap** (not just a single A14 delay); (2) no memory sell-side note has published a quantified HBM5 base-die capability delta (Samsung High-NA vs TSMC conventional EUV) as a vendor procurement decision variable.

**Catalyst:** Samsung or SK Hynix announcing HBM5 base-die process details citing High-NA EUV (IEDM 2026 / Hot Chips 2026); Intel 14A customer silicon tape-out announcement; TSMC competitor winning an HBM5 base-die logic contract from an independent memory vendor.

**Action window:** Medium (12–36 months — window closes when TSMC adopts High-NA in 2029).

**Falsifier:** Samsung SF1.4 High-NA yield falls below 50%; HBM5 base-die architecture moves away from via-pitch-sensitive designs, nullifying the High-NA density advantage for memory.

**Cross-reference:** market_opportunities.md Opp 8; cross_sector_alpha.md Finding 6; chip_fabrication/research.md (paper-026 ASML High-NA bifurcation, paper-027 TSMC Symposium); memory/research.md (HBM5).

---

### T2-M: China Sovereign AI Chip Supply Chain at Scale — NVIDIA China TAM Subtraction Not in Sell-Side Models *(Run #3)*

**Opportunity:** Short any NVIDIA long thesis pricing in a China TAM rebound scenario. Long Chinese AI cloud infrastructure providers (Alibaba, Baidu, ByteDance infrastructure) that own sovereign compute fleets.

**The bet:** Alibaba T-Head Zhenwu M890 (May 2026): 560,000 units deployed in Alibaba Cloud, 3× performance vs prior-gen 810E, 144 GB HBM3, 800 GB/s inter-chip bandwidth, 3nm process. V900/J900 roadmap through 2028. NVIDIA Q1 FY2027 10-Q confirmed zero Data Center Hopper shipments to China (vs $4.6B in Q1 FY2026). Long-term NVIDIA bull theses implicitly assume China TAM reverts to NVIDIA once export controls are resolved. T-Head's 560K-unit deployment — available to 400+ external customers — means the China AI compute market has built a self-sustaining supply chain that reduces the ex-China rebound even in a scenario of export control normalization. NVIDIA Q1 FY2027 Vera Rubin constraint admission adds pressure: NVIDIA cannot even supply unconstrained domestically, let alone China.

**Why still mispriced:** M890 announcement received broad mainstream coverage (CNBC, TrendForce, Business Standard). Short-term China revenue collapse is fully priced. The *long-term TAM subtraction* — that China sovereign AI compute is now self-sustaining at scale — has not appeared in a sell-side NVIDIA model quantifying the installed base as a permanent demand-destruction component. NVIDIA bull thesis pieces in financial press continue to treat China as a recoverable market (regulatory normalization scenario) rather than a permanently contracted TAM.

**Catalyst:** Any NVIDIA disclosure in Q2–Q3 FY2027 earnings that China Data Center revenue remains near-zero even after export control normalization talks; T-Head announcing V900 external customer wins outside Alibaba Cloud; sell-side analyst publishing a NVIDIA bear note that explicitly models China sovereign compute as a permanent TAM reduction.

**Action window:** Long (2–5 years).

**Falsifier:** US-China export control normalization leads to NVIDIA selling H20-successor products in volume to China (quantifiably larger than T-Head's installed base); T-Head M890 quality/reliability issues cause Alibaba Cloud to return to foreign silicon; US Treasury/Commerce restricts TSMC from supplying 3nm to T-Head.

**Cross-reference:** market_opportunities.md Opp 9; AI_accelerators/research.md (paper-026 Alibaba M890, section 11); GPUs/research.md (China Domestic GPU Sector, paper-021).

---

### T2-N: Apple-Intel/Samsung Foundry Discussions as TSMC N2 AI-Capacity Relief *(NEW — Run #4)*

**Opportunity:** Long NVIDIA and AMD on the specific thesis that a partial Apple-Intel deal unlocks TSMC N2 capacity for AI chips in 2027–2028. Intel Foundry Services as a potential asymmetric win if the deal materializes.

**The bet:** Apple currently consumes >50% of TSMC's initial N2 (2nm) capacity in 2026. Bloomberg (May 5, 2026) reported Apple in early-stage discussions with Intel (18A/14A foundry) and Apple executives visiting Samsung's Taylor, TX facility (SF4X/SF2 class processes). Analyst estimate: Intel could begin Apple processor production for lower-end devices (M-series non-Pro, iPad, lower iPhone tiers) as early as 2027–2028. No contracts signed; no orders placed as of May 5, 2026. If Apple shifts even 15–20% of silicon volume to Intel or Samsung, TSMC N2 allocation opens substantially for NVIDIA, AMD, and hyperscaler ASIC customers — the single largest demand-side relief mechanism for the "TSMC N2 100%-booked, Apple >50%" chokepoint that has constrained AI chip supply. An Apple tape-out would simultaneously be Intel IFS's most credible external design win and validate 18A as a Tier-1 foundry process.

**Why still mispriced:** EE Times explicitly named NVIDIA and AMD as TSMC N2 capacity beneficiaries from an Apple-Intel deal. SemiAnalysis acknowledged Apple-Intel as optionality for TSMC AI capacity. These are specialist publications — not Goldman/Morgan Stanley/Bernstein sell-side. The specific quantified claim — how much TSMC N2 capacity would be freed, and what that implies for NVIDIA/AMD unit shipment guidance — has not appeared in a mainstream sell-side semiconductor note. The market has modeled the TSMC N2/Apple constraint as a fixed structural input to AI chip supply; no model incorporates Apple foundry diversification as a supply-side unlock variable.

**Catalyst:** Apple-Intel foundry agreement announcement (2026–2027); Intel 18A achieving ≥70% yield on Apple-class designs (yield data at Hot Chips or IEDM); any NVIDIA or AMD guidance uplift citing improved TSMC N2 allocation in 2027.

**Action window:** Medium-to-long (12–36 months — deal is early-stage with a 2027–2028 production timeline).

**Falsifier:** Intel 18A yield remains at ~62-65% and Apple rejects the process for quality reasons; Apple executives conclude Samsung Texas facility is not ready for Apple-class silicon; Apple publicly reaffirms TSMC exclusivity for all nodes.

**Cross-reference:** market_opportunities.md Opp 10; cross_sector_alpha.md Finding 7; chip_fabrication/research.md (paper-028 Apple-Intel/Samsung, paper-009 N2 allocation, paper-027 TSMC Symposium).

---

## What Changed from Run #3

**Strengthened this cycle (Run #4):**
- **T2-L** (High-NA EUV first-mover window): STRENGTHENED from "2-year window (2026–2028)" to "≥3-year structural multi-node divergence." Primary source upgrade: TSMC 2026 North America Technology Symposium (April 22–23, paper-027) confirmed A12 *and* A13 (both 2029-class nodes) skip High-NA EUV — extending the window beyond A14 alone. This is a material upgrade to the thesis strength, not just a timeline extension.

**New opportunities this cycle (Run #4):**
- **T2-N** (Apple-Intel/Samsung foundry as TSMC N2 AI-capacity relief): Entirely new. Bloomberg May 5, 2026 primary source (paper-028). Apple >50% TSMC N2, early-stage discussions with Intel 18A and Samsung TX. EE Times names NVIDIA/AMD as beneficiaries in specialist press; no mainstream sell-side has quantified the AI supply unlock. This is the first credible demand-side relief mechanism for the TSMC N2 AI chip constraint.

**Dropped off (ALREADY-PRICED-IN, removed from list):**
- None this cycle. Run #4 verification found 0 ALREADY-PRICED-IN items. All 13 items from Run #3 remain on the list, none crossed the priced-in threshold.

**Unchanged from Run #3:** T2-A, T2-B, T2-C, T2-D, T2-E, T2-F, T2-G, T2-H, T2-I, T2-J, T2-K, T2-M — no material consensus shift per Run #4 verification agent for these 12 items.

*Full audit trail with URLs and dated quotes: `research/verification_log.md`. Prior opportunity lists: archived in `research/run_history.md`.*
