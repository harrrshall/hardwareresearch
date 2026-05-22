# interconnects — Research Summary
Generated: 2026-05-22 | Window: 2025-11-22 – 2026-05-22 | Validated sources: 60

---

## Executive Summary

The November 2025 – May 2026 period marks a decisive inflection in semiconductor interconnect technology, characterized by three simultaneous forces: the arrival of rack-scale coherent GPU domains at terabyte-per-second bandwidth, the emergence of optical interconnects transitioning from prototype to production, and the release of major new open standards (CXL 4.0, UCIe 3.0, UALink 1.0, UEC 1.0, PCIe 7.0) that collectively reshape the architecture of AI infrastructure.

**The five defining events of this period:**

1. **CXL 4.0 released (November 18, 2025)** at 128 GT/s on PCIe 7.0 foundation, enabling multi-rack coherent memory pools at unprecedented scale — directly addressing the AI inference KV-cache memory wall.

2. **NVIDIA Vera Rubin platform announced (CES 2026)** with NVLink 6.0 at 3.6 TB/s per GPU, delivering 260 TB/s per rack and shipping H2 2026 — maintaining a 2:1 bandwidth lead over all alternative GPU scale-up fabrics.

3. **Broadcom Tomahawk 6 enters volume production (March 2026)**: first 102.4 Tbps Ethernet switch in production, enabling the scale-out networks required for Rubin and future AI clusters at 800G.

4. **Marvell acquires Celestial AI for $3.25B (November 2025)**: consolidates in-die optical I/O technology with switch ASICs and CXL switches — the most significant interconnect M&A in this period.

5. **HBM4 mass production commences (Q1 2026)**: Samsung (11.7 Gbps/pin, 3.3 TB/s/stack) and Micron shipping HBM4, enabling the NVIDIA Rubin and AMD MI400 platforms' memory bandwidth targets.

**Key quantitative thresholds reached in this period:**
- First 3.6 TB/s per-GPU scale-up bandwidth (NVLink 6)
- First 102.4 Tbps production switch ASIC (Tomahawk 6)
- First 64 GT/s chiplet die-to-die standard (UCIe 3.0)
- First 128 GT/s coherent memory fabric standard (CXL 4.0)
- First in-die optical I/O chiplet in production silicon (Celestial AI)
- First electro-optical router below 4 pJ/bit (CEA-Leti, ISSCC 2026: 3.19 pJ/bit)

---

## All Collected Findings

### NVLink and GPU Scale-Up Interconnect

**NVLink 5.0 (Production, 2025)**
- 1,800 GB/s per GPU via 18 links × 100 GB/s bidirectional
- GB200 NVL72: 72 GPUs, 130 TB/s aggregate, all-to-all via NVSwitch
- Scales to 576 GPUs at 1 PB/s non-blocking
- NVSwitch includes SHARP for in-network AllReduce and multicast
- Microsoft Azure GB300 cluster: 4,608 GPUs, NVLink 5 scale-up + 800G InfiniBand scale-out (October 2025)
- Stargate: 64,000 GB200 systems deployed from March 2025 on 800G InfiniBand

**NVLink 6.0 (Announced CES 2026, H2 2026)**
- 3,600 GB/s per GPU (3.6 TB/s) — doubles NVLink 5
- 400 Gbps SerDes per sub-link
- NVLink 6 switch chip: liquid cooling required
- Vera Rubin NVL72: 72 Rubin GPUs + 36 Vera CPUs = 260 TB/s rack aggregate
- Rubin NVL144: 144 GPUs, 3.6 ExaFLOPS FP4
- Rubin: TSMC 3nm, HBM4 at 288 GB/GPU, 13 TB/s per GPU
- Deployment: AWS, Google Cloud, Microsoft Azure, Oracle Cloud H2 2026

### UCIe (Universal Chiplet Interconnect Express)

**UCIe 3.0 (Released August 5, 2025 at FMS)**
- UCIe-S: 48 GT/s; UCIe-A: 64 GT/s (doubled from 2.0's 32 GT/s)
- New: runtime recalibration, early firmware download, priority sideband packets
- Sideband extended to 100 mm (from ~50 mm) — enables larger SiP topologies
- Fully backward compatible with UCIe 1.0, 1.1, 2.0
- UCIe-A on advanced packaging (CoWoS, EMIB-T) achieves 64 GT/s; UCIe-S on organic substrate achieves 48 GT/s

**First UCIe Optical Chiplet — Ayar Labs TeraPHY (March 2025)**
- 8 Tbps aggregate bandwidth per chiplet
- 200 Gbps/mm chip edge — 1,000x density of electrical I/O
- UCIe 2.0 standard package compliant
- Memory disaggregation to 2 km, latency = <2×5 ns + TOF
- SuperNova light source: 16 wavelengths

### CXL (Compute Express Link)

**CXL 4.0 (Released November 18, 2025 — SC25)**
- 128 GT/s on PCIe 7.0 physical layer (doubles CXL 3.x)
- Bundled ports: up to 1.5 TB/s per logical connection
- 4 retimers supported (vs 2 in CXL 3.x) — enables multi-rack topologies
- 256-byte FLIT retained from 3.x
- Native x2 link width added
- Fully backward compatible

**CXL Memory Pooling Performance (2025 Production)**
- 4.8x LLM inference throughput vs baseline
- 82.7% reduction in Time-to-First-Token
- 6.5x speedup vs 200G RDMA for LLM inference
- 8x memory capacity expansion per GPU via pooling
- Commercial 100+ TiB CXL pools available 2025

**CXL Switch Silicon**
- Panmnesia CXL 3.2 Fabric Switch: first port-based routing implementation, up to 4,096 nodes
- Marvell Structera S 30260: 260-lane CXL switch, rack-level memory pooling (announced OFC 2026, March 2026)

### PCIe

**PCIe 7.0 (Final Spec June 2025)**
- 128 GT/s (4× PCIe 5.0, 2× PCIe 6.0), x16 = 512 GB/s
- Compliance program delayed to 2028 (from 2027)
- Consumer products 2026–2027; enterprise/AI 2027–2028
- PCIe 8.0 already in early development

**PCIe 6.0 (Enterprise Deployment 2025)**
- 64 GT/s, PAM4 + FLIT, 256-byte FLIT with FEC
- FBER target: ≤10⁻⁶
- AMD consumer support: 2026
- Consumer SSDs: ~2030
- **Microchip Switchtec Gen 6 PCIe Switch (October 2025)**: First 3nm PCIe Gen 6 switch, 20 ports/160 lanes, post-quantum cryptography (CNSA 2.0), sampling Q4 2025

### Optical Interconnects

**Co-Packaged Optics (CPO) State 2025-2026**
- Energy efficiency: 3.5–6.75 pJ/bit (vs 14–24 pJ/bit pluggable)
- NVIDIA Quantum-X: 1.6T CPO (2H 2025), Spectrum-X Photonic: 3.2T CPO (2H 2026)
- Broadcom Tomahawk 6: CPO option at 102.4T, 3nm, Broadcom internal CPO (~6 pJ/bit)
- CPO market: $95M (2025) → $1.05B (2034), 30.6% CAGR

**Celestial AI Photonic Fabric (Hot Chips 2025)**
- World's first SoC with in-die optical I/O
- Photonic Fabric Module (PFM): TSMC 5nm + photonic interposer + 2× HBM3e + Fiber Array Unit
- 7.2 Tbps optical connectivity per module
- Standalone optical chiplet: 16 Tbps
- 25x more bandwidth, 10x lower latency vs CPO alternatives
- Marvell acquisition: $3.25B (November 2025)

**ISSCC 2026 — CEA-Leti Electro-Optical Router**
- 28nm CMOS on photonic interposer
- 18 ns optical path setup (frame-level dynamic routing)
- **3.19 pJ/bit** — below CPO on interposer (3.5 pJ/bit)
- 0.007 mm² per link
- 6 wavelengths per link (dynamic WDM selection)

**400G/lane Race (OFC 2025)**
- Accelink, Marvell, Broadcom demonstrating 224 GBaud PAM4 → 400 Gbps/lane
- Marvell: 400G PAM4 400G per lane, 1.6T silicon photonics LPO reference design
- TSMC COUPE: integrates optical engines within CoWoS substrate

### InfiniBand

- XDR 800G: production standard 2025; Quantum-X800: 144 × 800G ports
- In-network compute: 14.4 TFLOPS (9x vs NDR) via SHARP
- GDR 1.6T: appearing in 2026–2027 roadmaps
- Stargate: 64,000 GB200 on 800G InfiniBand from March 2025
- Oracle: 131,000 GB200 cluster planned on Quantum InfiniBand
- Market: $25.74B (2025) → $126.99B (2030), 37.6% CAGR

### Switch ASICs

- **Broadcom Tomahawk 6**: 102.4 Tbps, 3nm, CPO option, 200G SerDes, production March 2026
- **Cisco Silicon One G300**: 102.4 Tbps, announced February 2026
- **NVIDIA Spectrum-X Photonic**: 102.4 Tbps with native CPO, H2 2026
- **Marvell Teralynx 10**: 51.2 Tbps, 500 ns latency, volume production 2025
- Roadmap: Tomahawk 7 (204.8T, 2027), Tomahawk 8 (409.6T, ~2029)

### AMD Infinity Fabric

- **MI350/MI355X (2025)**: Gen4 Infinity Fabric, 7 links, 1,075 GB/s GPU-GPU, 5.5 TB/s AP bi-sectional
- **MI400 (2026)**: HBM4, 432 GB, 19.6 TB/s (est.), 300 GB/s scale-out, 40 PFLOPS FP4

### UALink

- **UALink 200G 1.0 (April 2025)**: 200 GT/s/lane, 800 Gbps x4, 1,024 accelerators, load/store model
- Consortium: AMD, Intel, Apple, Google, Meta, Microsoft, AWS, Cisco, HPE, Synopsys (75 members)
- First silicon: Q4 2026 (Upscale AI); meaningful deployments: 2027

### Ultra Ethernet Consortium

- **UEC 1.0 (June 2025)**: 560 pages, native RDMA, UET transport, QSFP-DD/OSFP physical
- Hardware shipping: fall 2025
- ESUN (OCP, October 2025): Ethernet for Scale-Up with 12-company backing

### Custom AI Accelerator Interconnects

- **Google Ironwood ICI**: 9.6 Tbps (4 links), 1.2 TB/s per chip, 3D Torus, 9,216-chip superpod, 1.77 PB HBM
- **AWS Trainium3 NeuronLinkv4**: 160 PCIe lanes, 2x bandwidth vs Trn2, Trn3 UltraServer: 706 TB/s aggregate from 144 chips
- **Intel Gaudi 3**: 24× 200 GbE RoCE, 21 scale-up + 3 scale-out, 25.6 Tbps throughput

### Advanced Packaging

- **Intel EMIB-T**: TSV-enabled EMIB for HBM4, UCIe compatible; Foveros Direct 3D <5 µm pitch (vs TSMC SoIC-X 9 µm)
- **TSMC CoWoS-L**: Multi-chiplet beyond reticle limit; CoWoS capacity 80% CAGR; NVIDIA >70% allocation
- **HBM4**: Samsung production Feb 2026 (11.7 Gbps/pin, 3.3 TB/s/stack); Micron Q1 2026; 2048-bit interface

### OIF CEI-224G

- XSR, VSR, MR, LR variants at 224 Gbps/lane
- 112 GBaud PAM4
- Interoperability demo at OFC 2025 (112G + 224G + 448G)
- <0.5 pJ/bit target for XSR
- Basis for UALink and future NVLink physical layers

---

## Summarized Papers

| # | Title | Theme | Key Metric |
|---|---|---|---|
| 001 | UCIe 3.0 Specification | UCIe | 64 GT/s, 100mm sideband |
| 002 | NVLink 5.0 / GB200 NVL72 | NVLink | 1.8 TB/s/GPU, 130 TB/s rack |
| 003 | CXL 4.0 Specification | CXL-fabric | 128 GT/s, 1.5 TB/s bundled |
| 004 | PCIe 7.0 & 6.0 Timelines | PCIe | 128 GT/s, PAM4 FLIT |
| 005 | Optical CPO / Silicon Photonics 2025-2026 | optical-switching | 3.5 pJ/bit CPO on interposer |
| 006 | UALink 200G 1.0 | chip-to-chip | 200 GT/s, 1024 accelerators |
| 007 | Switch ASIC 102.4T Race | chip-to-chip | 102.4 Tbps, 3nm, CPO option |
| 008 | InfiniBand XDR 800G | chip-to-chip | 800G XDR, 14.4 TFLOPS SHARP |
| 009 | AMD Infinity Fabric 4 | chip-to-chip | 1,075 GB/s, 5.5 TB/s AP |
| 010 | NVIDIA Rubin / NVLink 6.0 | NVLink | 3.6 TB/s/GPU, 260 TB/s rack |
| 011 | Google Ironwood TPU v7 | chip-to-chip | 9.6 Tbps ICI, 1.77 PB HBM |
| 012 | UEC 1.0 | chip-to-chip | UET transport, million-node scale |
| 013 | HBM4 Mass Production | chip-to-chip | 3.3 TB/s/stack, 2048-bit |
| 014 | AWS Trainium3 UltraServer | chip-to-chip | 706 TB/s aggregate, 144 chips |
| 015 | Intel EMIB-T / Foveros Direct 3D | chip-to-chip, UCIe | <5 µm pitch, HBM4 support |
| 016 | OIF CEI-224G XSR/USR | chip-to-chip | 224 Gbps/lane, <0.5 pJ/bit |
| 017 | TSMC CoWoS Advanced Packaging | chip-to-chip, UCIe | 80% CAGR, CoWoS-L for Blackwell |
| 018 | Celestial AI Photonic Fabric + Marvell Acq | optical-switching | 16 Tbps chiplet, $3.25B acq |
| 019 | 800G to 1.6T Ethernet Transition | chip-to-chip | 220% QoQ growth H1 2025 |
| 020 | ISSCC 2026 Electro-Optical Router | optical-switching | 3.19 pJ/bit, 18 ns switching |
| 021 | CXL Disaggregation AI Benchmarks | CXL-fabric | 4.8x throughput, 82.7% TTFT |
| 022 | Ayar TeraPHY UCIe Optical Chiplet | optical-switching, UCIe | 8 Tbps, 200 Gbps/mm, 1000x |

---

## Technical Analysis

### Bandwidth Density by Interconnect Type (2026)

| Technology | Bandwidth | Reach | Energy (pJ/bit) | Use |
|---|---|---|---|---|
| CEI-224G XSR (target) | 224 Gbps/lane | <50 mm | <0.5 | On-package die-to-die |
| UCIe 3.0 Advanced (64 GT/s) | 64 GT/s/lane | <50 mm | 0.5–1.5 | Chiplet-to-chiplet |
| NVLink 6.0 | 200 GB/s/link | <1 m | 1–2 | GPU-to-GPU |
| Infinity Fabric 4 | 1,075 GB/s total | <1 m | 1–2 | GPU-to-GPU |
| InfiniBand XDR | 800 Gbps/port | 100+ m | 8–12 | Rack-to-rack |
| Ethernet 800G LPO | 800 Gbps/port | 100+ m | 7–10 | Rack-to-rack |
| CPO (interposer) | varies | 0–1 m | **3.5** | Switch ASIC |
| CPO (MCM) | varies | 0–1 m | 6.75 | Switch ASIC |
| Pluggable 800G | 800 Gbps/module | 100 m–80 km | 14–18 | Rack-to-rack |
| TeraPHY UCIe Optical | 8 Tbps | 2 km | 2–4 | Die-to-far-memory |

### NVLink Bandwidth Trajectory

| Year | Version | BW/GPU | Rack BW | SerDes |
|---|---|---|---|---|
| 2021 | NVLink 4.0 | 900 GB/s | — | 50 Gbps |
| 2024 | NVLink 5.0 | 1,800 GB/s | 130 TB/s (NVL72) | 100 Gbps |
| 2026 | NVLink 6.0 | 3,600 GB/s | 260 TB/s (Rubin NVL72) | 200 Gbps |

NVLink doubles bandwidth every 18–24 months, tracking a "NVLink's Law" doubling cadence.

### Switch ASIC Bandwidth Trajectory

| Year | ASIC | Capacity |
|---|---|---|
| 2023 | Tomahawk 5 | 51.2 Tbps |
| 2026 | Tomahawk 6 | 102.4 Tbps |
| ~2027 | Tomahawk 7 | 204.8 Tbps |
| ~2029 | Tomahawk 8 | 409.6 Tbps |

Doubling every 18–24 months on 3nm → 2nm → 1.4nm node progression.

### Memory Bandwidth per GPU — AI Accelerators

| Platform | HBM | BW/GPU | Year |
|---|---|---|---|
| H100 | HBM3 | 3.35 TB/s | 2023 |
| MI300X | HBM3 | 5.3 TB/s | 2024 |
| GB200 | HBM3e | ~8 TB/s | 2024 |
| MI350X | HBM3e | ~9 TB/s | 2025 |
| Ironwood (aggregate estimate) | HBM | ~8 TB/s | 2025 |
| Rubin | HBM4 | **13 TB/s** | H2 2026 |
| MI400 | HBM4 | **19.6 TB/s** | 2026 |

AMD achieves higher per-GPU memory bandwidth with MI400 (19.6 TB/s) vs NVIDIA Rubin (13 TB/s), while NVIDIA leads on scale-up interconnect (3.6 TB/s NVLink 6 vs estimated ~1.5 TB/s AMD).

---

## Architectural Observations

### Observation 1: The Scale-Up/Scale-Out Boundary Is Dissolving

Traditional architecture:
- **Scale-up**: proprietary high-bandwidth fabric (NVLink, Infinity Fabric) within a fixed-size domain
- **Scale-out**: commodity Ethernet or InfiniBand between domains

2025-2026 shifts:
- ESUN initiative pushes Ethernet into scale-up territory
- UALink 1.0 is an open scale-up standard at 800 Gbps (x4)
- UEC 1.0 closes Ethernet's latency/bandwidth gap with InfiniBand for training
- UCIe optical chiplets extend die-level bandwidth to 2 km — effectively making die-to-die semantics apply to rack-scale distances

### Observation 2: NVSwitch Architecture Breaks GPU Locality

NVIDIA's NVL72 routes all GPU-to-GPU traffic through external NVSwitch fabric, deliberately eliminating within-tray locality. This design choice:
- Simplifies programming model (all GPUs are topologically equivalent)
- Requires 9 switch trays per 72-GPU rack (substantial overhead)
- Creates a single-vendor dependency at every switching level
- NVLink 6's liquid-cooled switches extend this architectural pattern at even higher power densities

### Observation 3: Memory Disaggregation Becomes Production-Grade

Three converging technologies make disaggregated memory viable in 2025-2026:
1. **CXL 3.x/4.0**: Hardware-coherent memory access at 64–128 GT/s with <300 ns add-in latency
2. **Ayar TeraPHY**: 8 Tbps UCIe-optical for far-memory up to 2 km
3. **CXL switches**: 4,096-node fabrics (Panmnesia), 260-lane rack switches (Marvell Structera S)

Benchmark evidence: 4.8x inference throughput and 82.7% TTFT reduction from CXL pooling.

### Observation 4: Optical Interconnect Crosses Energy Parity in 2026

Historical barrier: optical interconnects consumed more energy per bit than electrical within package distances, unjustified until bandwidth-distance product forced the tradeoff.

2026 crossover points:
- **CPO on interposer**: 3.5 pJ/bit — now below best pluggable electrical at comparable link count
- **CEA-Leti ISSCC 2026**: 3.19 pJ/bit with dynamic routing — below CPO
- **Target CEI-224G XSR**: <0.5 pJ/bit — electrical still wins at <50 mm

The crossover distance for "optical wins" is moving from 1 m down toward 100–300 mm with CPO, and toward 10–50 mm with in-die approaches (Celestial AI). Within 5 years, >50 mm interconnects in AI accelerators will be predominantly optical.

### Observation 5: CoWoS is the Invisible Constraint on All AI Interconnect Progress

Despite bandwidth milestones, the physical enabler for all high-density interconnects is TSMC's CoWoS advanced packaging:
- Every high-bandwidth GPU, TPU, or accelerator depends on CoWoS-L or CoWoS-S
- NVIDIA holds >70% of TSMC CoWoS capacity (2025)
- 80% CAGR growth cannot keep pace with NVIDIA's annual volume increase
- AMD, Google, AWS, Intel must compete for remaining 30%

This capacity constraint is a strategic weapon: it delays competitors' products and limits customer choice more than any technical gap.

### Observation 6: Open Standards Lag Proprietary Implementations by 2–4 Years

| Standard | Announced/Ratified | First Silicon | Deployment |
|---|---|---|---|
| UALink 1.0 | April 2025 | Late 2026 | 2027 |
| UEC 1.0 | June 2025 | Fall 2025 | 2026 |
| UCIe 3.0 | August 2025 | 2026 | 2027 |
| CXL 4.0 | November 2025 | 2027 | 2028 |
| PCIe 7.0 | June 2025 | 2027 | 2028 |

NVLink 6.0 ships H2 2026 while UALink — its open competition — won't see meaningful deployments until 2027. The standard-to-silicon lag is structural and reinforces NVIDIA's incumbency.

---

## Trend Analysis

### Trend 1: Bandwidth Doubling Every 18–24 Months Continues

Across all interconnect tiers (GPU scale-up, switch ASIC, memory bandwidth), bandwidth doubles on a 18–24 month cadence:
- NVLink: 900 GB/s (2021) → 1.8 TB/s (2024) → 3.6 TB/s (2026)
- Switch: 25.6T (2022) → 51.2T (2024) → 102.4T (2026)
- HBM: 460 GB/s (HBM2e) → 1.18 TB/s (HBM3e) → 3.3 TB/s (HBM4, Samsung)

This is structural: process node improvements (5nm → 3nm) enable more SerDes lanes at higher rates.

### Trend 2: pJ/bit Replaces Gbps as Primary Procurement KPI

Hyperscaler RFPs in 2025–2026 increasingly specify energy per bit as a primary metric, not raw bandwidth. Drivers:
- AI training clusters consuming 10–100 MW each
- Optical module power (14–20 W/port at 800G) dominates switch power consumption
- CPO at 3.5–6.75 pJ/bit vs pluggable at 14–24 pJ/bit represents 3–7x TCO improvement at scale
- IEEE 802.3df standardization of 800G LPO addresses the near-term without full CPO deployment

### Trend 3: Chiplet Architecture Becomes Universal

Every AI accelerator announced in this period uses chiplet disaggregation:
- NVIDIA Rubin: compute chiplets + HBM4 on CoWoS-L
- AMD MI400: CDNA 5 compute + I/O chiplets
- Google Ironwood: first multi-die TPU (2 compute chiplets)
- AWS Trainium3: chiplet-based with NeuronLink fabric
- Intel: EMIB 3.5D combining EMIB + Foveros Direct

UCIe 3.0 (64 GT/s) and OIF CEI-224G (<0.5 pJ/bit target) are the direct responses to this universal chiplet adoption, providing the die-to-die interconnect standards that enable multi-vendor assembly.

### Trend 4: Open Ecosystem Challenge to NVIDIA Deepens

2025-2026 sees the most coordinated open ecosystem challenge to NVIDIA's interconnect dominance:
- **UALink**: AMD, Intel, Apple, Google, Meta, Microsoft, AWS — 75 members
- **UEC 1.0**: 100+ companies, hardware shipping fall 2025
- **ESUN (OCP)**: 12 hyperscaler + silicon companies pushing Ethernet for scale-up
- **UCIe 3.0**: Enables multi-vendor chiplet fabrics without proprietary die-to-die

Yet NVLink 6 ships in H2 2026 with 3.6 TB/s while UALink won't see silicon until late 2026. The open ecosystem challenge is real but delayed.

### Trend 5: Optical Integration Moves Into the Die

The integration frontier for optical interconnects is moving inward:
- **2022–2024**: Pluggable optics at cage/port boundary
- **2025**: Co-packaged optics (CPO) at package boundary (Tomahawk 6, Quantum-X)
- **2025**: In-package optical I/O chiplet (Ayar TeraPHY, UCIe-compatible)
- **2025**: In-die optical I/O (Celestial AI Photonic Fabric Module)
- **2026**: Dynamic in-package optical routing (CEA-Leti ISSCC 2026)
- **2028+**: Wafer-level integrated optics (TSMC COUPE evolution)

The pJ/bit and Tbps/mm² metrics improve at each step inward.

### Trend 6: Memory and Compute Architecturally Separating

The combination of CXL 4.0 (coherent fabric), UCIe optical chiplets (2 km reach), and HBM4 (active base die) is enabling a fundamental architectural shift:
- Compute dies no longer need to be on the same physical package as memory
- A GPU can "own" HBM stacks located in a separate memory module on a different substrate, in a different tray, or even in a different rack
- This decoupling enables workload-specific memory ratios (inference needs more memory; training needs more compute) without redesigning the whole chip

---

## Manufacturing Implications

### Implication 1: Advanced Packaging is the New Semiconductor Bottleneck

The competition for TSMC CoWoS capacity reveals advanced packaging as the constraining resource in AI accelerator production, more limiting than leading-edge logic capacity in some cases:
- TSMC CoWoS 80% CAGR is not keeping pace with AI cluster buildout
- Intel EMIB-T and EMIB 3.5D are viable alternatives for non-TSMC customers
- Samsung S-Packing and SK Hynix HBM integration packaging will compete in 2026+

### Implication 2: HBM4 Active Base Die Changes OSAT Dynamics

HBM4's active base die (logic layer below memory stacks) transfers value from memory fab to logic fab:
- Samsung, SK Hynix, Micron all qualify logic processes for HBM4 base die
- TSMC's A16 and Intel's 18A could supply HBM4 base die logic for independent memory vendors
- This vertically integrates logic foundry with memory stack manufacturing, creating new competitive dynamics

### Implication 3: UCIe Enables Chiplet Supply Chain

UCIe 3.0's backward compatibility and 64 GT/s rate enables a chiplet supply chain:
- SoC designers can source compute dies, I/O dies, and memory from different vendors/foundries
- ISSCC 2025: Intel demonstrated 20-chiplet heterogeneous integration across 2 foundries in production
- This reduces single-vendor dependency on both foundry and chip design

### Implication 4: Liquid Cooling Becomes Mandatory for High-Speed Switch Fabric

NVLink 6's switch chip requires liquid cooling, following a trend:
- NVIDIA GB200 NVL72: already fully liquid-cooled system
- NVIDIA Rubin NVL72: extends liquid cooling to switch fabric
- 800G module power (14–20 W/port) already challenges air-cooled rack thermal budgets
- Data center operators must invest in direct liquid cooling (DLC) infrastructure as a prerequisite for deploying 2026 interconnects

### Implication 5: Optical Component Supply Chain Must Scale 100x

CPO adoption at 102.4T scale:
- Tomahawk 6 with CPO requires silicon photonic die integration at TSMC/Broadcom scale
- NVIDIA Quantum-X800 + Spectrum-X require Lumentum and Coherent laser supply
- OFC 2026 analysis projects optical components in AI data centers to scale 100x by 2030
- Wafer-level silicon photonics fabs (IMEC, CEA-Leti, TSMC photonics) need 2–3 year expansion lead

---

## Scalability Considerations

### GPU Cluster Scale: Hierarchy Required Above 576 GPUs

Current NVLink 5.0 / NVSwitch: 576 GPU non-blocking domain  
NVLink 6.0 / NVSwitch: expected to scale similarly (72 × 3.6 TB/s within NVL72)  
Beyond single NVLink domain: InfiniBand XDR 800G or Ethernet 800G (scale-out)

**Scaling stack 2025-2026 for 10k+ GPU clusters:**
1. Within NVL72 (72 GPUs): NVLink 5/6 full mesh via NVSwitch
2. NVL72 to NVL72 within rack group: InfiniBand QDR / Ethernet 800G leaf switch
3. Rack group to rack group: InfiniBand XDR spine / Tomahawk 6 Ethernet spine
4. Data center to data center: WAN (out of scope)

**Alternative for AMD/open ecosystem:**
1. 8-GPU node: Infinity Fabric 4
2. Node to node: UALink (2027) or Ethernet 800G (2025) or InfiniBand NDR
3. Cluster fabric: Ethernet 800G/1.6T via Tomahawk 6

### CXL Memory Pool Scalability

| Scale Level | Technology | Nodes | Status |
|---|---|---|---|
| Per-server | CXL 1.1/2.0 memory expander | 1 host | Production |
| Per-rack | CXL 3.x switch (Panmnesia) | up to 256 | 2025 |
| Multi-rack | CXL 3.x fabric (Panmnesia) | up to 4,096 | 2025 |
| Cross-rack | CXL 4.0 + 4 retimers | 10,000+ | 2027+ |

### UCIe Chiplet Scale Limits

UCIe 3.0 Advanced Package (64 GT/s):
- Practical per-link bandwidth: 64 GT/s × 16 bits (standard lane width) = 128 GB/s
- Multi-link bonding (future): 4 UCIe links = 512 GB/s — comparable to PCIe 5.0 x16
- Sideband reach (100 mm): enables 4–6 chiplet packages on a single organic substrate

UCIe optical (Ayar TeraPHY):
- Removes distance constraint entirely
- 8 Tbps per chiplet is 62.5x a single UCIe 3.0-A link at 128 GB/s
- Practical scalability: multiple TeraPHY chiplets per package edge, each to different memory or accelerator targets

### InfiniBand Scalability

XDR 800G fat-tree at exascale:
- 144 × 800G ports per Quantum-X800
- 3-level fat-tree: (144/2)³/2 = 1,492,992 / 2 ≈ 746,496 endpoints non-blocking
- Stargate (64k GPUs) occupies ~8.6% of a fully built-out 3-level XDR fabric
- GDR 1.6T doubles this further — exascale interconnects are no longer theoretical

---

## Strategic Insights

### Insight 1: NVIDIA Controls the Interconnect Clock Speed

NVIDIA's cadence — NVLink doubles every generation, NVSwitch tracks — means competitors perpetually chase a moving target. UALink 1.0 at 800 Gbps (x4) launches into a world where NVLink 6 at 3.6 TB/s is already shipping. The open ecosystem needs either:
(a) A 2x–3x bandwidth advantage to overcome 2-year silicon delay, or
(b) A cost/watt advantage sufficient to change purchasing decisions

Neither is currently demonstrated in production. UALink's 1,024-accelerator scale advantage (vs 576 for NVSwitch) is real but doesn't address the bandwidth gap.

### Insight 2: The $3.25B Marvell/Celestial AI Deal Defines the Optical Roadmap

Marvell's acquisition creates the only vendor offering:
- **Switch ASIC** (Teralynx 10 at 51.2T, roadmap to 102.4T)
- **CXL memory fabric** (Structera S 30260)
- **In-die optical I/O** (Celestial AI PFM, 16 Tbps chiplet)
- **Silicon photonics DSP** (existing Marvell portfolio)

This vertical integration at the interconnect layer mirrors what NVIDIA did with GPU + NVLink + NVSwitch. Broadcom (Tomahawk) and Cisco (Silicon One) will respond.

### Insight 3: AI Inference Memory Wall is the Forcing Function for CXL Adoption

Every LLM inference operator faces the same problem: trillion-parameter model KV caches require 80–120+ GB per serving instance. HBM3e tops out at 192 GB per GPU. CXL memory pooling's 4.8x throughput improvement and 82.7% TTFT reduction are not theoretical — they are measured in production 2025 deployments. CXL 4.0's multi-rack reach at 128 GT/s is specifically designed to scale this to hyperscaler workloads.

### Insight 4: pJ/bit as a Metric Will Reorder Vendor Rankings

If hyperscalers are spending $10–100B on power infrastructure for AI clusters, a 3x improvement in interconnect energy efficiency (CPO vs pluggable) is worth billions annually. Vendors who lead on pJ/bit (NVIDIA CPO switches, Broadcom Tomahawk 6 CPO, Celestial AI/Marvell in-die) will capture the hyperscaler segment even at premium per-unit pricing.

### Insight 5: TSMC CoWoS Capacity Is a Strategic Lever, Not Just Supply Chain Risk

NVIDIA's >70% CoWoS allocation is a proactive supply chain strategy, not an accident:
- It limits competitors' ability to ship competing AI accelerators even when the silicon is ready
- It motivates AMD, Intel, and others to develop/qualify alternative advanced packaging (EMIB-T, Samsung S-Packing)
- For startups (Tenstorrent, SambaNova, Groq), CoWoS access is a potential existential constraint

### Insight 6: CEA-Leti ISSCC 2026 Result Points to In-Package Optical as Next Disruption

The 3.19 pJ/bit, 18 ns dynamic electro-optical router at 0.007 mm² per link is a research result that, in 3–5 years, could enable:
- All-to-all optical interconnect within a chiplet package replacing 3D mesh wired topologies
- Optical switching within NVL-class systems, eliminating physical NVLink cables
- Dynamic reconfiguration of memory-compute partitioning at nanosecond timescales

This represents the next architectural discontinuity after CPO.

---

## Open Questions

1. **Will UALink silicon actually ship in Q4 2026, or will it slip to 2027–2028?** The history of open interconnect standards (GenZ, CCIX, OpenCAPI) is one of repeated delays. UALink's 75-member consortium involvement suggests broader commitment, but silicon tape-out schedules are not public.

2. **Can AMD MI400's 19.6 TB/s memory bandwidth overcome NVIDIA Rubin's 3.6 TB/s scale-up advantage for LLM training?** The answer depends heavily on workload mix: attention-bound models favor AMD's memory bandwidth; all-reduce-heavy distributed training favors NVIDIA's NVLink scale-up.

3. **When does the in-die optical router (CEA-Leti, 3.19 pJ/bit) move from 28nm research to 5nm production?** The thermal sensitivity of silicon photonic resonators and wafer yield at integration remain unresolved challenges. 5–7 year timeline is plausible.

4. **Will Marvell successfully integrate Celestial AI's in-die optical I/O into a switch ASIC?** The $3.25B acquisition's success hinges on co-design of Teralynx 20+ with photonic elements on the same interposer — a manufacturing challenge that has not been demonstrated at switch ASIC scale.

5. **What happens to CXL when PCIe 7.0 (128 GT/s) hits compliance delays?** CXL 4.0 is entirely dependent on PCIe 7.0 physical layer. PCIe 7.0 compliance testing is delayed to 2028. Does CXL 4.0 deployment slip to 2029+ for most deployments?

6. **Will the 400 Gbps/lane optical milestone be reached by OFC 2026?** Multiple vendors demonstrated 224 GBaud PAM4 at OFC 2025. The OFC 2026 outlook suggests 400G/lane commercial modules possible in 2026; the question is yield and cost at volume.

7. **Can Google Ironwood's 9,216-chip superpod model scale to even larger domains, and how does its ICI latency compare to NVIDIA NVSwitch at those scales?** At 1.77 PB shared HBM, Ironwood's superpod already exceeds many HPC installations in effective memory bandwidth. The ICI topology (3D Torus) has known diameter limitations at very large scales.

8. **Is CoWoS capacity the true limiting factor for AI infrastructure buildout through 2028?** Even with TSMC's 80% CAGR expansion, demand projections for Rubin and MI400 suggest the CoWoS constraint could persist through 2027. Samsung's packaging capacity becomes critical as a second source.

9. **How will ESUN's Ethernet-for-scale-up compete with NVLink 6.0 and UALink?** ESUN is backed by NVIDIA itself (paradoxically), suggesting Ethernet-based scale-up is viable for some workloads. The latency gap (<1 µs InfiniBand vs 1–3 µs Ethernet) remains the key question for training workloads.

10. **Will the Trainium4's 4x memory bandwidth target translate to competitive per-token economics vs NVIDIA Rubin?** AWS's PCIe-based NeuronLink trades bandwidth ceiling for ecosystem breadth. Trainium4's HBM4 adoption would put it in direct comparison with MI400 on memory bandwidth.

---

## Source Index

| # | Title | URL | Date | Theme |
|---|---|---|---|---|
| 1 | UCIe 3.0 Specification | https://www.uciexpress.org/post/ucie-3-0-specification-redefining-chiplet-interconnects | 2025-08-05 | UCIe |
| 2 | UCIe 3.0 BusinessWire | https://www.businesswire.com/news/home/20250805909613/en/UCIe-Consortium-Introduces-3.0-Specification-With-64-GTs-Performance-and-Enhanced-Manageability | 2025-08-05 | UCIe |
| 3 | UCIe 3.0 StorageNewsletter | https://www.storagenewsletter.com/2025/08/07/fms-2025-ucie-consortium-introduces-3-0-specification-with-64gt-s-performance-and-enhanced-manageability/ | 2025-08-07 | UCIe |
| 4 | UCIe 3.0 ServeTheHome | https://www.servethehome.com/ucie-3-0-spec-released-with-big-speed-up-for-chiplets/ | 2025-08-07 | UCIe |
| 5 | Ayar TeraPHY UCIe Chiplet | https://www.businesswire.com/news/home/20250331044779/en/Ayar-Labs-Unveils-Worlds-First-UCIe-Optical-Chiplet-for-AI-Scale-Up-Architectures | 2025-03-31 | UCIe, optical |
| 6 | NVLink Scale-Up 2025 | https://introl.com/blog/nvlink-scale-up-networking-gpu-interconnect-infrastructure-2025 | 2025 | NVLink |
| 7 | GB200 NADDOD Analysis | https://www.naddod.com/blog/nvidia-gb200-interconnect-architecture-analysis-nvlink-infiniband-and-future-trends | 2025 | NVLink |
| 8 | GB200 NVL72 Official | https://www.nvidia.com/en-us/data-center/gb200-nvl72/ | 2025 | NVLink |
| 9 | Rubin CES 2026 | https://www.servethehome.com/nvidia-launches-next-generation-rubin-ai-compute-platform-at-ces-2026/ | 2026-01 | NVLink |
| 10 | Rubin Platform Technical | https://developer.nvidia.com/blog/inside-the-nvidia-rubin-platform-six-new-chips-one-ai-supercomputer/ | 2026-01 | NVLink |
| 11 | PCIe 7.0 Final | https://overclock3d.net/news/misc/pcie-7-0-has-arrived-and-pcie-8-0-is-already-in-progress/ | 2025-06 | PCIe |
| 12 | PCIe 6.0 Launch | https://www.pcworld.com/article/2805679/pci-express-6-products-might-finally-ship-in-2025.html | 2025 | PCIe |
| 13 | Microchip Switchtec Gen 6 | https://www.microchip.com/en-us/about/news-releases/products/microchip-unveils-first-3-nm-pcie--gen-6-switch-to-power-modern | 2025-10-13 | PCIe |
| 14 | PCIe 6/7 Compliance Delays | https://www.tomshardware.com/tech-industry/pcie-60-and-70-standards-hit-a-roadblock-compliance-slowdown-could-lead-to-broader-delays | 2025 | PCIe |
| 15 | CXL 4.0 BusinessWire | https://www.businesswire.com/news/home/20251118275848/en/CXL-Consortium-Releases-the-Compute-Express-Link-4.0-Specification-Increasing-Speed-and-Bandwidth | 2025-11-18 | CXL |
| 16 | CXL 4.0 Blocks & Files | https://blocksandfiles.com/2025/11/24/cxl-4/ | 2025-11-24 | CXL |
| 17 | CXL 3.0 Production 2026 | https://www.colobird.com/blogs/cxl-3-memory-pooling-dedicated-servers/ | 2025-12 | CXL |
| 18 | CXL FMS 2025 | https://computeexpresslink.org/blog/expanding-your-memory-footprint-with-cxl-at-fms-2025-4133/ | 2025-08 | CXL |
| 19 | Marvell Structera S | https://investor.marvell.com/news-events/press-releases/detail/1017/marvell-launches-next-generation-cxl-switch-enabling-memory-pooling-to-break-through-the-ai-memory-wall | 2026-03 | CXL |
| 20 | ISSCC 2026 Optical Router | https://www.electronicsweekly.com/news/business/isscc-2026-02/ | 2026-02 | optical |
| 21 | Celestial AI Hot Chips 2025 | https://www.servethehome.com/celestial-ai-photonic-fabric-module-at-hot-chips-2025/ | 2025-08 | optical |
| 22 | Celestial AI TSMC 5nm | https://monthly-pulse.com/2025/12/16/breaking-the-bandwidth-barrier-enabling-celestial-ais-photonic-fabric-with-custom-esd-ip-on-tsmcs-5nm-platform/ | 2025-12 | optical |
| 23 | Marvell/Celestial AI Acquisition | https://optics.org/news/16/11/47 | 2025-11 | optical |
| 24 | NVIDIA CPO Scale-Up | https://optics.org/news/16/3/26 | 2025-03 | optical |
| 25 | Spectrum-X Silicon Photonics | https://www.tweaktown.com/news/107372/nvidias-new-spectrum-x-ethernet-silicon-photonics-enters-the-chat-a-game-changer-for-ai/index.html | 2025-03 | optical |
| 26 | NVIDIA Silicon Photonics Roadmap | https://www.hpcwire.com/2026/04/20/inside-nvidias-silicon-photonics-roadmap/ | 2026-04 | optical |
| 27 | InfiniBand NDR/XDR | https://ascentoptics.com/blog/infiniband-ndr-xdr-for-ai-and-hpc-data-centers/ | 2025 | IB |
| 28 | XDR 800G Spec | https://www.fibermall.com/news/ibta-launches-xdr-800g-infiniband-spec.htm | 2025 | IB |
| 29 | InfiniBand Roadmap | https://www.infinibandta.org/infiniband-roadmap-charting-speeds-for-future-needs/ | 2025 | IB |
| 30 | Tomahawk 6 Shipping | https://www.broadcom.com/company/news/product-releases/63146 | 2026-03-12 | switch |
| 31 | Cisco G300 | https://www.theregister.com/2026/02/10/cisco_challenges_broadcom_nvidia_switch_chips/ | 2026-02-10 | switch |
| 32 | Marvell Teralynx 10 | https://www.marvell.com/company/newsroom/marvell-teralynx-512t-ethernet-switch-enters-volume-production-for-global-ai-cloud-deployments.html | 2025 | switch |
| 33 | 102.4T Race | https://www.nextplatform.com/2025/06/03/the-ai-datacenter-is-ravenous-for-102-4-tb-sec-ethernet/ | 2025-06 | switch |
| 34 | AMD IF Hot Chips 2025 | https://convergedigest.com/hot-chips-2025-amd-boosts-infinity-fabric/ | 2025-08 | AMD IF |
| 35 | MI350X Datasheet | https://www.koicomputers.com/wp-content/uploads/2025/08/amd-instinct-mi350x-gpu-datasheet.pdf | 2025-08 | AMD IF |
| 36 | AMD MI400 Roadmap | https://newsletter.semianalysis.com/p/amd-advancing-ai-mi350x-and-mi400-ualoe72-mi500-ual256 | 2026-01 | AMD IF |
| 37 | UALink 200G 1.0 Spec | https://ualinkconsortium.org/wp-content/uploads/2025/04/UALink-1.0-White_Paper_FINAL.pdf | 2025-04 | UALink |
| 38 | UALink Silicon Timeline | https://www.hpcwire.com/2025/12/02/upscale-ai-eyes-late-2026-for-scale-up-ualink-switch/ | 2025-12 | UALink |
| 39 | UEC 1.0 Official | https://ultraethernet.org/ultra-ethernet-consortium-uec-launches-specification-1-0-transforming-ethernet-for-ai-and-hpc-at-scale/ | 2025-06-11 | UEC |
| 40 | UEC vs UALink Analysis | https://semianalysis.com/2025/06/11/the-new-ai-networks-ultra-ethernet-uec-ualink-vs-broadcom-scale-up-ethernet-sue/ | 2025-06-11 | UEC |
| 41 | Google Ironwood ICI | https://cloud.google.com/blog/products/compute/inside-the-ironwood-tpu-codesigned-ai-stack | 2025-05 | TPU |
| 42 | AWS Trainium3 | https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/ | 2025-12 | AWS |
| 43 | OFC 2025 Optical AI | https://nand-research.com/ofc-2025-optical-interconnects-take-center-stage-in-the-ai-first-data-center/ | 2025-03 | optical |
| 44 | Broadcom OFC 2025 | https://investors.broadcom.com/news-releases/news-release-details/broadcom-advances-optical-connectivity-ai-infrastructure | 2025-03 | optical |
| 45 | CPO Market 2026 | https://adtek-fiber.com/co-packaged-optics-cpo-market-trends-2026-ai-data-center-optical-interconnect-evolution/ | 2026 | optical |
| 46 | CPO 5 Trends 2026 | https://blogs.sw.siemens.com/semiconductor-packaging/2026/02/05/five-key-trends-of-co-packaged-optics-cpo-in-2026/ | 2026-02 | optical |
| 47 | CPO Status 2026 | https://www.edn.com/where-co-packaged-optics-cpo-technology-stands-in-2026/ | 2026 | optical |
| 48 | OIF CEI-224G | https://www.oiforum.com/technical-work/hot-topics/common-electrical-i-o-cei-224g/ | 2025 | SerDes |
| 49 | 224G SerDes Trend | https://semiengineering.com/224g-serdes-trend-and-solution/ | 2025 | SerDes |
| 50 | Intel EMIB-T | https://institutionofelectronics.ac.uk/intel-ups-the-advanced-packaging-ante-with-emib-t/ | 2025-11 | pkg |
| 51 | TSMC CoWoS Capacity | https://semiwiki.com/forum/threads/cowos-capacity-set-to-skyrocket-by-2026-massive-growth-in-advanced-packaging.21773/ | 2025-12 | pkg |
| 52 | HBM4 Production | https://www.oscoo.com/news/hbm4-the-memory-revolution-in-the-age-of-ai-computing/ | 2026-02 | HBM |
| 53 | OCP Summit 2025 | https://engineering.fb.com/2025/10/13/data-infrastructure/ocp-summit-2025-the-open-future-of-networking-hardware-for-ai/ | 2025-10 | OCP |
| 54 | ESUN OCP | https://www.opencompute.org/blog/introducing-esun-advancing-ethernet-for-scale-up-ai-infrastructure-at-ocp | 2025-10 | OCP |
| 55 | Google HC 2025 | https://www.servethehome.com/google-ironwood-tpu-swings-for-reasoning-model-leadership-at-hot-chips-2025/ | 2025-08 | TPU |
| 56 | CXL Inference Speedup | https://computeexpresslink.org/blog/overcoming-the-ai-memory-wall-how-cxl-memory-pooling-powers-the-next-leap-in-scalable-ai-computing-4267/ | 2025 | CXL |
| 57 | Panmnesia CXL Fabric | https://www.ai-buzz.com/enfabricas-cxl-fabric-breaks-ai-memory-wall-via-800gbe | 2025 | CXL |
| 58 | Ayar UCIe Optical Disagg | https://ayarlabs.com/blog/ai-scale-up-and-memory-disaggregation-two-use-cases-enabled-by-ucie-and-optical-io/ | 2025 | UCIe, optical |
| 59 | ISSCC 2025 Intel | https://www.allaboutcircuits.com/news/isscc-2025-intel-propels-chiplet-interconnect-speed-and-flexibility/ | 2025-02 | chiplet |
| 60 | 800G AI Networking | https://introl.com/blog/800g-networking-ai-gpu-fabric-planning-2025 | 2025 | Ethernet |
