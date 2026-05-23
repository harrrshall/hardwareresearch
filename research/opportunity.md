# Opportunity Shortlist — Live Action List

**Last regenerated**: 2026-05-23 (Run #1 verification basis)
**Source**: `research/verification_log.md` — only `VERIFIED-NOT-PRICED-IN` and `PARTIALLY-PRICED-IN` items kept.
**Excluded**: `ALREADY-PRICED-IN` items (dead leads). See `cross_sector_alpha.md` and `market_opportunities.md` for full context.

This file is **overwritten each run**. Items that get re-verified across cycles harden into conviction; items that drop into `ALREADY-PRICED-IN` disappear from the next cycle's list.

---

## Tier 1 — Verified non-consensus (act on these first)

### 1. PCIe 7.0 compliance slip → CXL 4.0 memory-wall fix delayed to 2028–29
- **The bet**: Short any thesis or capex plan that assumes CXL 4.0 multi-rack memory pooling is a 2026–27 reality. Underwrite memory-wall solutions that DON'T depend on PCIe 7.0 (HBM4E capacity-first designs, mobile PIM, direct-on-die memory). Conversely, fade the 2026–27 timeline implied by CXL Consortium marketing and CXL-pooling vendor decks.
- **Why still mispriced**: PCIe 7.0 compliance program slipped from 2027 to 2028 (Tom's Hardware, TechSpot confirm). CXL 4.0 deployment is hostage to that. Yet CXL-marketing pieces (introl.com, KAD8) and CXL-pooling vendors continue to promote 2026–27 reality. The downstream implication is genuinely uncombined in public coverage.
- **Catalyst**: First CXL 4.0 production deployment date slips publicly — likely in vendor earnings Q3–Q4 2026 or hyperscaler datacenter planning leaks.
- **Action window**: Medium (12–18 months until the slip is undeniable to mainstream).
- **Falsifier**: PCIe-SIG announces accelerated 7.0 compliance schedule, or Microsoft/Meta/Google publicly deploys CXL 4.0 multi-rack pooling in 2026.
- **Cross-reference**: `interconnects/research.md` (PCIe 7.0 spec) + `memory/research.md` (CXL 4.0 release Nov 2025). Synthesis: `cross_sector_alpha.md` Finding 6.

### 2. CG-HBM + CXL 4.0 jointly attack the silicon interposer — CoWoS may be a peaking asset
- **The bet**: Underweight pure-play CoWoS-leveraged narratives at the 3–5-year horizon. Long-hold the suppliers that pivot to hybrid-bonding / direct-on-die HBM (CG-HBM precursor) tooling and CXL optical disaggregation. Skeptical of capex models that assume CoWoS demand grows monotonically through 2029+.
- **Why still mispriced**: Mainstream models (financialcontent.com, sell-side capacity reports) extrapolate CoWoS demand forever. Both legs of the attack — CG-HBM (Rubin roadmap) and CXL 4.0 + optical disaggregation — exist publicly in isolation, but no analyst combines them as a *demand-destroyer* for the silicon interposer.
- **Catalyst**: First Rubin-class GPU shipped with direct-on-die HBM ≥ 2027, or first hyperscaler production CXL 4.0 fabric reducing per-GPU memory area requirement.
- **Action window**: Long (3–5 years).
- **Falsifier**: SemiEngineering confirms hybrid bonding postponed further (already noted as risk); TSMC CoWoS bookings extend through 2030 without softening; HBM stays on microbumps through HBM5.
- **Cross-reference**: `memory/research.md` (CG-HBM, HBM4E roadmap) + `packaging/research.md` (CoWoS demand) + `interconnects/research.md` (CXL 4.0). Synthesis: `cross_sector_alpha.md` Finding 5.

---

## Tier 2 — Partially priced (window is closing — act before consensus fully forms)

### 3. Edge ↔ datacenter prefill/decode mirror as a structural law
- **The bet**: Specialist research has fully priced the *datacenter* split (NVIDIA + Groq AFD). What's still rare in mainstream coverage is reading the SAME prefill/decode split appearing at the *edge* (Apple Silicon NPU prefill + GPU decode, on-device LLM offload) as evidence the GPU decomposition is a universal architectural law, not a Rubin-specific choice. Position around small companies building "prefill engines" or "decode engines" as separable products — not full-stack accelerators.
- **Why still mispriced**: Datacenter side is in VentureBeat, The Next Platform, Hao AI Lab. Edge mirror confirmation is in one SqueezeBits blog. The two have not been combined in any sell-side note.
- **Catalyst**: Second hyperscaler announces native prefill+decode disaggregation (e.g., Meta or Google AFD-equivalent) in late 2026; or Apple/Qualcomm publicly markets prefill-engine architecture in next mobile generation.
- **Action window**: Short–medium (6–18 months).
- **Falsifier**: NVIDIA Rubin+Groq performance disappoints and re-monolithizes inference at next refresh.
- **Cross-reference**: `AI_accelerators/research.md` (NVIDIA Groq AFD), `edge_AI_hardware/research.md` (NPU prefill, GPU decode). Synthesis: `cross_sector_alpha.md` Finding 3.

### 4. Power × efficiency: NVIDIA can hold ~90% merchant share AND lose deployed-intelligence share
- **The bet**: TPU v7-style efficiency (~29 TFLOPS/W) wins deployed-intelligence share inside power-capped datacenters, even while NVIDIA dominates merchant unit volume. Long Google TPU ecosystem; long custom-ASIC infrastructure (Broadcom AI ASIC, Marvell custom silicon). Skeptical of the implicit equation "NVIDIA share = NVIDIA value capture."
- **Why still mispriced**: SemiAnalysis (TPUv7), Goldman ("gigawatt ceiling"), Morgan Stanley (intelligence factory model) have each published the building blocks. The interpretive step — that merchant share decouples from deployed-intelligence share — is sharper than any single piece.
- **Catalyst**: First quarter where Google's TPU-driven AI compute capacity passes a major NVIDIA-customer in disclosed exaflops (estimated late 2026–2027); or hyperscaler capex re-allocation away from merchant GPUs in early 2027 earnings.
- **Action window**: Medium (12–24 months).
- **Falsifier**: New nuclear/SMR capacity unlocks the grid before 2028 and the gigawatt-ceiling thesis is removed.
- **Cross-reference**: `AI_accelerators/research.md` (TPU v7 Ironwood) + `datacenter_hardware/research.md` (grid constraint). Synthesis: `cross_sector_alpha.md` Finding 1.

### 5. Compound packaging yield, not CoWoS floor space, is the real ceiling
- **The bet**: Track HBM-stack yield × KGD yield × interposer yield as the binding multiplier for "good packages out per month." Long suppliers of KGD test (FormFactor, Onto Innovation) and HBM-stacking yield tooling. The synthesis's specific arithmetic isn't widespread.
- **Why still mispriced**: Epoch AI publishes the headline frame; Samsung HBM4 delays publicly disclosed. TSMC's May-2026 disclosure of 98% CoWoS yield muddies the interposer leg, but stacking/KGD compounding is real and underanalyzed.
- **Catalyst**: First quarter where CoWoS wpm grows but good-package shipments do NOT — visible in NVIDIA / Apple delivery slips or HBM vendor revenue gaps. Watch SK Hynix vs Samsung Q3–Q4 2026 HBM4 yields.
- **Action window**: Short (6–12 months).
- **Falsifier**: HBM4 16-Hi stack yields publicly disclosed > 85% by SK Hynix; or NVIDIA delivers Rubin volume at promised cadence without yield-related delays.
- **Cross-reference**: `packaging/research.md` + `memory/research.md` (HBM4 stacking). Synthesis: `cross_sector_alpha.md` Finding 2.

### 6. NVFP4 vs MXFP4 incompatibility creates consumer (not just datacenter) lock-in
- **The bet**: NVIDIA's NVFP4 (block size 16) outperforms open MXFP4 (block size 32) at finer granularity. The datacenter implications are discussed, but the *consumer-side lock-in* is not — local LLM users on NVIDIA hardware will get measurably better inference, deepening the consumer GPU moat. Long NVIDIA's consumer software stack moat (CUDA + NVFP4 + TensorRT-LLM).
- **Why still mispriced**: vLLM/SGLang community knows the format gap; ML systems papers (arXiv 2509.23202) confirm MXFP4 lags. Consumer-lock-in framing is rare in sell-side notes.
- **Catalyst**: A widely-shared benchmark in consumer-LLM communities (LocalLLaMA, r/MachineLearning) shows quantization quality gap; or Apple/Qualcomm announces hardware MXFP4 support and its limitations become visible.
- **Action window**: Medium (12–18 months).
- **Falsifier**: Industry converges on MXFP4 as the standard (e.g., Khronos / OCP forces NVIDIA to support MXFP4 natively); or post-training INT4 closes the quality gap.
- **Cross-reference**: `GPUs/research.md` (NVFP4) + `AI_accelerators/research.md`. Synthesis: matrix pair 9.

### 7. Foundry value migrates into HBM4 active base die
- **The bet**: HBM4 active base dies are 12nm class (TSMC) or 4nm (Samsung SF4) — a new advanced-node logic category that did not exist for HBM3. Long TSMC's specialty (mature-node) capacity *and* the leading-node base-die win share. Long Samsung Foundry SF4 capacity utilization. Underweight pure-DRAM exposure that misses the foundry-revenue migration into memory.
- **Why still mispriced**: Specialist coverage (Nomad Semi, TrendForce) discusses base-die node selection. Sell-side memory analysts still model HBM as a DRAM-pricing story, not a foundry-revenue story.
- **Catalyst**: SK Hynix or Samsung disclose specific TSMC wafer take for base die in 2026–27 earnings; or HBM4E base-die on N3-class node wins gets announced.
- **Action window**: Medium (12–18 months).
- **Falsifier**: HBM4E reverts to passive base die or in-house DRAM-fab base; foundry-revenue thesis collapses.
- **Cross-reference**: `memory/research.md` (HBM4 base die) + `chip_fabrication/research.md` (TSMC 12nm, Samsung SF4). Synthesis: matrix pair 28; `market_opportunities.md` #2.

### 8. Mobile PIM ships in phones before datacenter PIM ships clean — sequencing inversion
- **The bet**: LPDDR6-PIM is being JEDEC-standardized first (Samsung+SK Hynix joint 2024–2026); datacenter HBM-PIM is technically harder. The conventional wisdom that "datacenter validates, mobile inherits" is inverted here. Long the mobile NPU + PIM stack: Samsung MX + Memory Solutions, Apple A-series ANE, Qualcomm Hexagon NPU integration with LPDDR6-PIM.
- **Why still mispriced**: TrendForce / Tweaktown / Wccftech cover the standardization fact. Framing the sequencing inversion as a structural reversal of the usual "datacenter-first" pattern is rare.
- **Catalyst**: First commercial phone shipped with LPDDR6-PIM (expected late 2026 – 2027); JEDEC final LPDDR6-PIM standard approval.
- **Action window**: Short–medium (6–18 months).
- **Falsifier**: JEDEC standardization slips beyond 2027; Samsung+SK Hynix collaboration breaks down.
- **Cross-reference**: `memory/research.md` (LPDDR6-PIM, AiMX) + `edge_AI_hardware/research.md`. Synthesis: matrix pair 24; `market_opportunities.md` #6.

### 9. In-die optical routing (CEA-Leti ISSCC 2026) is the post-CPO discontinuity
- **The bet**: CPO is now mainstream — the next discontinuity is *in-die* optical routing (dynamic electro-optical router at 3.19 pJ/bit, 18 ns routing, ISSCC 2026 CEA-Leti). Long photonic interposer specialists (CEA-Leti spinouts, Celestial AI under Marvell, Lightmatter), watch for ISSCC 2027 follow-on papers.
- **Why still mispriced**: EE press (Electronics Weekly, Semiconductor Digest, EEJournal) covered the CEA-Leti paper. Sell-side has not connected it as the post-CPO step.
- **Catalyst**: ISSCC 2027 follow-up paper showing manufacturability; or Marvell + CEA-Leti spinout announcing product roadmap.
- **Action window**: Medium (12–24 months).
- **Falsifier**: Power/cost numbers don't improve at the next ISSCC; CPO timeline gets pushed back making "post-CPO" irrelevant.
- **Cross-reference**: `photonics/research.md` + `interconnects/research.md` (Marvell-Celestial AI $3.25B). Synthesis: matrix pair 40; `market_opportunities.md` #7.

### 10. Same heat-flux physics class at opposite scales (mobile + datacenter)
- **The bet**: Mobile thermal throttling and datacenter rack cooling are the SAME physics problem — heat-removal-per-unit-area — at different scales. Tooling and IP can cross over (TIM materials, vapor chambers, microfluidic cooling). Long thermal IP that spans both scales: heat-spreader materials, TIM vendors crossing from mobile to datacenter.
- **Why still mispriced**: Each side individually saturated in trade press. The "same physics class at opposite scales" framing is rare.
- **Catalyst**: Cross-over announcement — a mobile-thermal vendor wins a datacenter design slot, or a datacenter thermal company sells IP into a phone.
- **Action window**: Long (18–36 months).
- **Falsifier**: A genuinely different cooling architecture (e.g., on-chip refrigeration) wins datacenter, removing the cross-scale parallel.
- **Cross-reference**: `datacenter_hardware/research.md` (D2C liquid, 120kW racks) + `edge_AI_hardware/research.md` (mobile thermal throttling). Synthesis: matrix pair 45.

### 11. Avicena microLED short-reach optical I/O bridges edge interconnect
- **The bet**: Avicena LightBundle (microLED-based, no laser, 80–200 fJ/bit, 1 Tbps/mm) is targeted at datacenter, but the same architecture is naturally suited to short-reach automotive / edge AI compute interconnect. Long Avicena and its eKit ecosystem; watch for TSMC × Avicena collaboration depth.
- **Why still mispriced**: Photonics analysts know Avicena, but the "edge expansion" angle is in their own marketing, not in mainstream sell-side analysis.
- **Catalyst**: Automotive OEM design-win for microLED interconnect in 2027; or edge AI compute vendor adopts LightBundle for cross-board.
- **Action window**: Long (18–36 months).
- **Falsifier**: microLED-based interconnect fails to scale beyond demo, or laser-based optical I/O cost curve undercuts before Avicena reaches volume.
- **Cross-reference**: `photonics/research.md` (Avicena LightBundle) + `edge_AI_hardware/research.md`. Synthesis: matrix pair 42; `market_opportunities.md` #7.

### 12. Glass substrate qualification inflection
- **The bet**: Intel showcased glass-core EMIB January 2026; AMD has Absolics qualifying for MI400. +40% speed, –30% power vs organic substrate. Long Absolics (SKC subsidiary), watch for MI400 production confirmation; underwrite organic-substrate exposure as glass scales.
- **Why still mispriced**: Trade press covers (Wccftech, TrendForce, igorslab, photoncap Substack), but sell-side has not converged on glass as a 2027–28 mainstream substrate.
- **Catalyst**: AMD MI400 production launch with glass substrate confirmed; or Intel Panther Lake successor with glass core in volume.
- **Action window**: Medium (12–24 months).
- **Falsifier**: Glass-substrate yield doesn't ramp; AMD/Intel quietly revert to organic for next-gen products.
- **Cross-reference**: `packaging/research.md` (glass substrate, EMIB) + `chip_fabrication/research.md`. Synthesis: `market_opportunities.md` #9.

---

## What changed from previous run
This is Run #1 (baseline). All 12 opportunities are new. Next cycle will note which graduate to higher conviction, which downgrade, and which drop entirely.

**Verification provenance**: `research/verification_log.md` (Run #1 verification, 2026-05-23).
