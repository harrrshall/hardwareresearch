# Opportunity Shortlist — Run #3 — 2026-05-23

**Regenerated every cycle. Signal-only. ALREADY-PRICED-IN items excluded entirely.**  
**Verification:** Independent Market Pricing Verification Agent (separate context, fresh web searches)  
**Tally this cycle:** 0 VERIFIED-NOT-PRICED-IN · 13 PARTIALLY-PRICED-IN · 3 ALREADY-PRICED-IN (purged)

---

## Tier 1 — Verified Non-Consensus

*No VERIFIED-NOT-PRICED-IN findings this cycle. Run #3 verification found zero items that are genuinely non-consensus across all major analyst, vendor, and financial press coverage. All surviving opportunities are PARTIALLY-PRICED-IN (Tier 2). This is an honest result — not every cycle produces Tier 1 opportunities.*

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

**Cross-reference:** cross_sector_alpha.md Finding 2; GPUs/research.md (paper-021, HBM4 Supply Transition); memory/research.md; packaging/research.md; chip_fabrication/research.md (Paper 012).

---

### T2-C: CG-HBM and CXL 4.0 Are Two Independent Attacks on the Silicon Interposer

**Opportunity:** Hedge against CoWoS scarcity premium (position to short CoWoS substrate suppliers in 2027–2028 timeframe) or position in memory disaggregation enablers (Ayar Labs optical chiplets, Astera Labs CXL switch ICs).

**The bet:** The entire AI hardware bull thesis has CoWoS interposer scarcity baked in. Two independent roadmap developments are demand-destroying for the interposer: (1) CG-HBM — Rubin's HBM4 stacked directly on the GPU logic die, eliminating the interposer for memory connection; (2) CXL 4.0 + optical disaggregation — if KV-cache and warm weights migrate to optically-attached CXL memory pools, each GPU needs fewer co-packaged HBM stacks. If either lands at volume, the scarce asset partially de-rates from within.

**Why still mispriced:** CG-HBM existence is known in trade press; CXL 4.0 is covered. The *investment thesis* — that both are demand-destroying for the interposer simultaneously — is not found in any mainstream sell-side note.

**Catalyst:** NVIDIA disclosing CG-HBM yield data in 2026 technical publications; or first production CXL 4.0 + optical memory disaggregation deployment at a hyperscaler (H2 2026 – 2027).

**Action window:** Medium-to-long.

**Falsifier:** NVIDIA publicly reports CG-HBM yield below 60% and abandons it for Rubin production; CXL 4.0 slips beyond 2029; optical memory disaggregation fails to close the latency gap vs co-packaged HBM.

**Cross-reference:** cross_sector_alpha.md Finding 4; GPUs/research.md (Rubin Architecture); interconnects/research.md (CXL 3.0/4.0, Optical sections); packaging/research.md.

---

### T2-D: CXL 4.0 Is Hostage to a PCIe 7.0 Compliance Slip — Memory-Wall Fix Expected 2027 May Be 2029

**Opportunity:** Position in CXL 3.0 infrastructure suppliers (Astera Labs CXL switches, Samsung/SK Hynix CXL memory modules) as the 2025–2027 bridge; avoid pricing in 2027-production assumptions for CXL 4.0. Short any thesis that assumes widespread CXL 4.0 AI memory pooling before 2028.

**The bet:** CXL 4.0 (1.5 TB/s bundled bandwidth) is built on the PCIe 7.0 physical layer. PCIe 7.0 compliance program slipped to 2028 (from 2027). The memory and accelerator sectors assume "CXL 4.0 multi-rack systems in late 2026–2027"; the interconnects sector's compliance-slip data implies 2028–2029 for production AI memory pooling at that bandwidth level. PCIe 8.0 Draft 0.5 (May 2026, paper-023) shows PCI-SIG advancing to the next generation even as PCIe 7.0 compliance remains unresolved.

**Why still mispriced:** PCIe 7.0 compliance delay is reported in mainstream tech press. The downstream implication — CXL 4.0 AI memory pooling slips to 2029 — has not been quantified in a sell-side report. CXL market forecasts project "$15B by 2028" without incorporating this risk.

**Catalyst:** PCIe 7.0 compliance test suite publication (expected 2028); CXL Consortium official CXL 4.0 device availability timeline update; any hyperscaler announcing a CXL 4.0 deployment delay.

**Action window:** Medium (12–30 months).

**Falsifier:** PCI-SIG issues PCIe 7.0 compliance program ahead of schedule (before end-2027); CXL 4.0 devices ship in volume via FPGA bridge chips that sidestep compliance requirements.

**Cross-reference:** cross_sector_alpha.md Finding 5; interconnects/research.md (PCIe 7.0, CXL sections, paper-023 PCIe 8.0); memory/research.md (CXL Memory Expansion).

---

### T2-E: CPO Laser Supply — EML Second Wave and Laser-Free Alternatives Are the Real Trade

**Opportunity:** Long EML second-wave qualifiers (II-VI/Coherent expanding 200G/lane capacity), integrated InP laser IP holders, GaN microLED companies (Avicena). Not Lumentum and Coherent at current multiples (those are the priced-in first wave).

**The bet:** CPO as an architecture is consensus and priced. The pick-and-shovel play — 200G/lane EML laser supply — is becoming mainstream (NVIDIA $4B Lumentum+Coherent investment). The non-consensus trade is: (a) second-wave EML qualifiers who benefit from the supply shortfall the priced-in duopoly creates, and (b) laser-free alternatives (Avicena GaN microLED at 80–200 fJ/bit, Intel OCI integrated InP) that become cost-competitive if the shortage persists through 2028. GF SCALE CPO (May 2026, paper-023 photonics) adds a second CPO platform that increases aggregate EML demand without solving supply — widening the shortfall.

**Why still mispriced:** Generic EML shortage and Lumentum/Coherent are priced. Second-wave EML qualifiers and laser-free alternatives are not in mainstream analyst coverage.

**Catalyst:** Any hyperscaler announcing multi-supplier EML qualification; first commercial GaN microLED CPO demonstration at >400G/lane; McKinsey 2026 optical supply chain update.

**Action window:** Short-to-medium (0–24 months).

**Falsifier:** Three additional EML manufacturers qualify 200G/lane before mid-2027, collapsing the supply premium; GaN microLED speed remains capped below 100G/lane.

**Cross-reference:** market_opportunities.md Opp 1; photonics/research.md (EML Laser Supply, GF SCALE CPO paper-023); interconnects/research.md (CPO section).

---

### T2-F: Edge AI Memory-Bandwidth Arbitrage — Dedicated NPU Co-Processor + Thermal Isolation Is the Winning Architecture

**Opportunity:** Long dedicated edge NPU co-processor suppliers (Hailo, NXP eIQ Neutron class), on-module LPDDR suppliers, and compiler-hardware co-design IP. Short integrated SoC NPU suppliers claiming TOPS leadership without addressing thermal and bandwidth constraints.

**The bet:** The edge AI hardware landscape is saturated with TOPS claims. Empirical data (arXiv 2604.24785) shows integrated SoC NPUs (Galaxy S24, Pixel 9) lose ≥50% throughput within 6 inference iterations due to shared thermal domain; dedicated NPU co-processors (Hailo-10H on Raspberry Pi 5) sustain near-zero variance across 20+ iterations via separate thermal domain + on-module LPDDR4X. LlamaWeb (arXiv 2605.20706, Run #3) confirms 2.7× best/worst GPU performance gap in WebGPU inference — thermal and bandwidth architecture matters more than raw TOPS.

**Why still mispriced:** Hailo is private. The thermal isolation advantage as an investment thesis has not appeared in Apple, Qualcomm, or MediaTek sell-side notes. The market values NPU TOPS in flagship SoC specs.

**Catalyst:** Large OEM announcing a dedicated NPU co-processor design win citing thermal sustainability; Hailo IPO or acquisition premium; mobile HBM (projected 2028) reaching qualification for first dedicated edge AI device.

**Action window:** Medium-to-long (12–48 months).

**Falsifier:** Apple or Qualcomm solve thermal NPU domain separation inside an integrated SoC at the next node; mobile HBM arrives before 2028 and gives integrated SoCs the bandwidth fix.

**Cross-reference:** market_opportunities.md Opp 2; edge_AI_hardware/research.md (paper-017, paper-023, paper-024 LlamaWeb); memory/research.md.

---

### T2-G: Processing-in-Memory at the JEDEC Standardization Inflection — Long the Tooling Layer

**Opportunity:** Long PIM controller IP, compiler tooling, and testing equipment companies (Rambus PIM IP, Synopsys PIM compiler tooling, Keysight for PIM validation). Not Samsung/SK Hynix directly (memory module margin is captured by standards).

**The bet:** Samsung and SK Hynix — direct competitors — are jointly standardizing LPDDR6-PIM through JEDEC with 2026 target. Standards convert PIM from niche to commodity module OEMs will demand. The asymmetric trade is on the controller IP, compiler, and testing layer that standardized PIM requires — small revenue today that scales with every LPDDR6-PIM socket shipped.

**Why still mispriced:** JEDEC standardization is publicly reported. No buy-side or sell-side note recommends PIM tooling names on the standardization-as-catalyst thesis.

**Catalyst:** JEDEC LPDDR6-PIM standard ratification (expected 2026); first OEM announcing LPDDR6-PIM support in a product roadmap; Samsung/SK Hynix announcing LPDDR6-PIM module availability.

**Action window:** Medium (12–36 months).

**Falsifier:** JEDEC LPDDR6-PIM delayed beyond 2027; memory vendors vertically integrate PIM controller IP in-house.

**Cross-reference:** market_opportunities.md Opp 3; memory/research.md (PIM/HBM-PIM, JEDEC section); AI_accelerators/research.md (paper-013 HPIM).

---

### T2-H: In-Die / In-Package Optical Routing — The Post-CPO Architectural Discontinuity

**Opportunity:** Long in-die optical routing IP beyond Marvell/Celestial AI — CEA-Leti licensees, TSMC CoWoS-Photonic roadmap suppliers, Ayar Labs (UCIe optical chiplet). The Marvell/Celestial AI acquisition is already priced into Marvell's multiple; the second-mover IP play is not.

**The bet:** CPO is consensus. The non-consensus architectural step is in-die optical I/O — routing signals inside the die at optical speeds, eliminating SerDes entirely. CEA-Leti demonstrated 3.19 pJ/bit electro-optical routing with 18 ns switching at ISSCC 2026 — below CPO on interposer (3.5 pJ/bit). This is a discontinuity: if in-die optical routing reaches production, it obsoletes CPO from the inside.

**Why still mispriced:** The Marvell/Celestial AI trade is ALREADY-PRICED-IN (33 Buy ratings). The broader in-die optical routing architectural disruption — beyond Marvell — is in no mainstream sell-side coverage.

**Catalyst:** TSMC announcing a photonic-integrated CoWoS variant; any hyperscaler announcing an in-die optical I/O qualification program; Ayar Labs UCIe optical chiplet entering production at a named customer.

**Action window:** Long (3–5 years).

**Falsifier:** CEA-Leti-type in-die optical routing fails to scale to production due to thermal or yield constraints; Ayar TeraPHY remains limited to niche HPC applications.

**Cross-reference:** market_opportunities.md Opp 4; interconnects/research.md (Celestial AI, Ayar TeraPHY, ISSCC 2026 electro-optical router); photonics/research.md.

---

### T2-I: Open-Interconnect (UALink / UEC / UCIe) Delayed-but-Real Window

**Opportunity:** Long UALink silicon switch IP vendors and UEC silicon vendors (Broadcom Tomahawk 7, Cisco G300 with UEC support) for 2026–2027 cluster build inflection. Also long UCIe IP licensees (Cadence, Synopsys) as chiplet adoption forces standardized die-to-die interfaces.

**The bet:** UALink 2.0 (April 7, 2026): 200 GT/s, supports 1,024+ GPUs. When UALink silicon ships (late 2026/2027), the switching-cost story inverts for new cluster builds — hyperscalers who backed the open standard start building non-NVIDIA clusters. Consensus over-prices the open-standard lag by assuming NVLink's head start is permanent.

**Why still mispriced:** UALink coverage is in specialist circles. The specific investment thesis — that consensus over-prices the lag — is not in mainstream sell-side. No NVIDIA sell-side bear case models the UALink silicon milestone as a concrete NVLink risk.

**Catalyst:** First production UALink silicon shipping to a named hyperscaler customer (late 2026); AMD MI500 cluster announcement using UALink fabric; UEC 1.0-certified Ethernet switch shipping at scale.

**Action window:** Medium (18–36 months).

**Falsifier:** UALink silicon availability slips beyond mid-2027; hyperscalers that backed UALink continue buying NVLink clusters for 2028+ anyway; UALink fails to achieve 1,024-GPU cluster interoperability in production.

**Cross-reference:** market_opportunities.md Opp 5; interconnects/research.md (UALink, UEC, UCIe sections).

---

### T2-J: Glass Substrates at the Qualification Inflection — Long Before the Transition Is Priced as Inevitable

**Opportunity:** Long glass substrate material suppliers (Absolics, LG Innotek, Corning's specialty glass division) and glass substrate tooling/equipment companies. The qualification inflection (Intel NEPCON January 2026 demo, AMD Absolics certification) is the highest-leverage entry point.

**The bet:** Intel demonstrated EMIB-on-glass at NEPCON Japan in January 2026; AMD is qualifying Absolics samples. The industry is at the inflection from R&D to qualification — exactly where materials transitions offer the highest leverage before "glass substrate is coming" becomes consensus.

**Why still mispriced:** Trade press covers the qualification milestones. No mainstream sell-side note recommends Absolics or LG Innotek specifically on this thesis. Analyst consensus frames glass substrates as "second half of the decade."

**Catalyst:** Intel or AMD announcing glass substrate production ramp dates at a packaging conference (mid-2026 through 2027); TSMC announcing glass substrate qualification for CoWoS-G; first volume production order for glass substrate AI packages.

**Action window:** Medium-to-long (18–48 months).

**Falsifier:** Intel or AMD delays glass substrate qualification beyond 2028; hybrid glass-organic substrates prove to offer equivalent performance at lower cost.

**Cross-reference:** market_opportunities.md Opp 6; packaging/research.md; chip_fabrication/research.md.

---

### T2-K: RISC-V Datacenter Silicon Post-Ventana — Open-ISA Moving Up-Market

**Opportunity:** Long RISC-V IP companies exposed to datacenter and AI (SiFive, Tenstorrent via RISC-V Tensix, Ventana now inside Qualcomm) and RISC-V toolchain/ecosystem enablers. The opportunity is pre-revenue-ramp positioning before datacenter RISC-V reaches analyst attention.

**The bet:** RISC-V crossed the datacenter credibility threshold in this window: Qualcomm paid $2.4B for Ventana, SiFive P570 Gen 3 achieved 21x AI improvement, RISC-V reached 25% CPU IP market share by end-2025. The market still prices RISC-V as embedded-only.

**Why still mispriced:** The Qualcomm/Ventana deal is priced into Qualcomm's stock narrative. The rerating of RISC-V from embedded-only to datacenter-capable is not in sell-side models. Ventana revenue is $37M in 2025.

**Catalyst:** Ventana Veyron V2 volume production announcement from Qualcomm (2026–2027); hyperscaler announcing RISC-V custom server SoC; RISC-V Linux kernel support reaching full parity with x86/ARM.

**Action window:** Long (2–5 years).

**Falsifier:** ARM responds with aggressive datacenter licensing cuts; x86/ARM incumbency in cloud software tooling proves too sticky without a major hyperscaler anchor customer by 2028.

**Cross-reference:** market_opportunities.md Opp 7; CPUs/research.md (Ventana, SiFive, RISC-V sections); AI_accelerators/research.md (Tenstorrent, Trend 5).

---

### T2-L: High-NA EUV First-Mover Window — Intel + Samsung vs TSMC's 2029 Delay *(NEW — Run #3)*

**Opportunity:** Long Intel Foundry Services capacity and Samsung Foundry's HBM5/memory differentiation; specifically, memory buyers who could access a Samsung High-NA advantage on HBM5 base-die density.

**The bet:** ASML CEO confirmed (May 20, 2026) first High-NA EUV products "within months" as Intel 14A and Samsung SF1.4 proceed. TSMC confirmed its High-NA delay to 2029 on April 24, 2026 earnings. This creates a 2-year window (2026–2028) where Samsung (HBM5 base die) and Intel (14A logic) access sub-8nm half-pitch patterns unavailable to TSMC customers. The non-consensus claim: Samsung HBM5 on High-NA could achieve tighter via pitch and higher density than TSMC-process-based HBM5 — a memory-specific capability delta no sell-side model has quantified.

**Why still mispriced:** TSMC's delay was flagged as "already priced in" by Bernstein *for TSMC stock*. The memory-specific implication — Samsung HBM5 on High-NA achieves a density/bandwidth delta vs TSMC-process-based HBM5 — has not been published in any sell-side memory or foundry note.

**Catalyst:** Samsung or SK Hynix announcing HBM5 base-die process details citing High-NA EUV (any conference H2 2026); Intel 14A customer silicon tape-out announcement; TSMC competitor winning an HBM5 base-die logic contract from an independent memory vendor.

**Action window:** Medium (12–36 months — window closes when TSMC adopts High-NA in 2029).

**Falsifier:** Samsung SF1.4 High-NA yield falls below 50%; HBM5 base-die architecture moves away from via-pitch-sensitive designs, nullifying the High-NA density advantage for memory.

**Cross-reference:** market_opportunities.md Opp 8; chip_fabrication/research.md (paper-026 ASML High-NA bifurcation, Intel 14A, Samsung SF1.4); memory/research.md (HBM5).

---

### T2-M: China Sovereign AI Chip Supply Chain at Scale — NVIDIA China TAM Subtraction Not in Sell-Side Models *(NEW — Run #3)*

**Opportunity:** Short any NVIDIA long thesis pricing in a China TAM rebound scenario. Long Chinese AI cloud infrastructure providers (Alibaba, Baidu, ByteDance infrastructure) that own sovereign compute fleets.

**The bet:** Alibaba T-Head Zhenwu M890 (May 2026): 560,000 units deployed in Alibaba Cloud, 3× performance vs prior-gen 810E, 144 GB HBM3, 800 GB/s inter-chip bandwidth, 3nm process. V900/J900 roadmap through 2028. NVIDIA Q1 FY2027 10-Q confirmed zero Data Center Hopper shipments to China (vs $4.6B in Q1 FY2026). Long-term NVIDIA bull theses implicitly assume China TAM reverts to NVIDIA once export controls are resolved. T-Head's 560K-unit deployment — available to 400+ external customers — means the China AI compute market has built a self-sustaining supply chain that reduces the ex-China rebound even in a scenario of export control normalization.

**Why still mispriced:** M890 announcement received broad mainstream coverage. Short-term China revenue collapse is fully priced. The *long-term TAM subtraction* — that China sovereign AI compute is now self-sustaining at scale — has not appeared in a sell-side NVIDIA model quantifying the installed base as a permanent demand-destruction component.

**Catalyst:** Any NVIDIA disclosure in Q2–Q3 FY2027 earnings that China Data Center revenue remains near-zero even after export control normalization talks; T-Head announcing V900 external customer wins outside Alibaba Cloud; sell-side analyst publishing a NVIDIA bear note that explicitly models China sovereign compute as a permanent TAM reduction.

**Action window:** Long (2–5 years).

**Falsifier:** US-China export control normalization leads to NVIDIA selling H20-successor products in volume to China (quantifiably larger than T-Head's installed base); T-Head M890 quality/reliability issues cause Alibaba Cloud to return to foreign silicon; US Treasury/Commerce restricts TSMC from supplying 3nm to T-Head.

**Cross-reference:** market_opportunities.md Opp 9; AI_accelerators/research.md (paper-026 Alibaba M890, section 11); GPUs/research.md (China Domestic GPU Sector, paper-021).

---

## What Changed from Run #2

**New opportunities this cycle (Run #3):**
- **T2-L** (High-NA EUV First-Mover Window): New from ASML CEO confirmation + TSMC delay to 2029. First appearance — PARTIALLY-PRICED-IN.
- **T2-M** (China Sovereign AI Chip Supply Chain): New from Alibaba Zhenwu M890 560K deployment. First appearance — PARTIALLY-PRICED-IN.

**Dropped off (ALREADY-PRICED-IN, removed from list):**
- **HBM4 Base-Die Logic** (was PARTIALLY-PRICED-IN in prior runs): DOWNGRADED. Samsung 40–50% price hike on base-die logic (TrendForce April 2026) + TSMC Q1 2026 earnings explicit callout as new N3 revenue category crossed the threshold.
- **Inference-Specialized ASICs for Prefill/Decode** (was PARTIALLY-PRICED-IN in prior runs): CONFIRMED ALREADY-PRICED-IN. GTC 2026 Groq 3 LPX announcement made this the defining architecture story of the year. Consistent with Run #1 direction.

**Downgraded tier (remained on list but status worsened):**
- **T2-A (Grid/TFLOPS-per-watt)**: Was VERIFIED-NOT-PRICED-IN in Run #1; now PARTIALLY-PRICED-IN because NVIDIA adopted "tokens per watt" as a GTC 2026 marketing metric, bringing the efficiency framing into mainstream investor vocabulary. Still on list, but window is narrowing.

**Unchanged from Run #2:** T2-B through T2-K all remain PARTIALLY-PRICED-IN with no material consensus shift per verification agent.

*Full audit trail with URLs and dated quotes: `research/verification_log.md`.*
