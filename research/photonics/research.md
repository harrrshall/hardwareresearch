# Photonics — Research Summary

**Generated:** 2026-05-23 (Run #1) | **Window:** 2025-11-23 – 2026-05-23 | **Validated sources:** 54 (2 new this run: paper-023 VALIDATED, paper-024 CONTEXT-ONLY)

---

## Executive Summary

The six-month period from November 2025 to May 2026 represents the single most consequential inflection in silicon photonics commercialization since the technology emerged. Three forces converged simultaneously: NVIDIA and Broadcom shipped the first large-scale co-packaged optics (CPO) products at 400 Tb/s and 102.4 Tbps respectively; the AI optical transceiver market surged 57% YoY to reach $26B; and a foundry war erupted with GlobalFoundries, Tower, TSMC, and imec all expanding silicon photonics capacity aggressively.

**Run #1 update (2026-05-23):** GlobalFoundries launched SCALE (Silicon Photonics Co-packaged Advanced Light Engine) on May 4, 2026 — the industry's first OCI MSA-compliant CPO platform from a non-TSMC foundry. SCALE uses DWDM with 50 Gbps and 100 Gbps micro-ring modulators across 8λ and 16λ configurations, and targets AI data center scale-up architectures. GF expects SiPho revenue to double in 2026 and exceed $1B by 2028 (TrendForce, May 7, 2026). This confirms GF as a credible second CPO-foundry source alongside TSMC COUPE — directly addressing the Samsung CPO gap (target 2029) and partially resolving Open Question 10.

The central tension of the period is supply vs demand. The 1.6T transceiver transition — enabled by 200G/lane EML lasers — creates a structural bottleneck with McKinsey projecting 30-60% supply shortfalls through 2027-2029. NVIDIA's $4B investment in Lumentum and Coherent in March 2026 is the clearest signal that optical component supply security has become a strategic priority at the hyperscaler level.

On the compute side, photonic neural networks crossed from single-layer demonstrations to multi-layer, 64-channel end-to-end implementations on 17 mm² chips. A 262 TOPS photonic accelerator using a Si3N4 frequency comb demonstrated the viability of photonics for AI inference, though commercial parity with electronic accelerators remains 5-10 years away.

Energy efficiency improvements are real and significant: CPO saves 60-73% vs pluggable optics; LPO saves 50%; and research-stage microLED links achieve 80-200 fJ/bit — 25-60× below laser-based optical I/O. The gap between the best research results and commercial systems is narrowing, with Avicena's LightBundle evaluation kit (March 2026) beginning to bridge that gap.

---

## All Collected Findings

### Co-Packaged Optics (CPO) — Commercial Milestones

**NVIDIA GTC 2025 (March 2025):**
- Announced Spectrum-X Photonics (Ethernet) and Quantum-X Photonics (InfiniBand) switch families
- Aggregate bandwidth: 400 Tb/s per switch
- Per-port: 1.6 Tb/s (Spectrum-X); 800 Gb/s × 144 ports (Quantum-X InfiniBand at 200G/lane SerDes)
- Power efficiency: 3.5× improvement vs traditional pluggable optics
- Laser count: 4× reduction
- Signal integrity: 63× improvement over copper-pluggable
- Deployment: Quantum-X (late 2025); Spectrum-X (2026)
- Manufacturing: TSMC COUPE

**Broadcom TH6 Davisson (October 8, 2025):**
- Industry's first 102.4 Tbps CPO Ethernet switch
- 70% power reduction vs traditional solutions
- TSMC COUPE + SoIC-X die stacking
- Third-generation CPO platform (25.6T → 51.2T → 102.4T progression)
- Began mass shipping October 2025

**TSMC COUPE (2025-2026):**
- Compact Universal Photonic Engine using SoIC-X (electrical IC stacked on photonic die)
- Small form factor pluggables qualified 2025; CPO CoWoS integration in volume production 2026
- 5–10× power efficiency improvement vs conventional pluggable
- 10–20× lower latency
- First CPO samples delivered to NVIDIA and Broadcom in 2025

**Marvell/Celestial AI Acquisition (February 2, 2026):**
- $3.25B acquisition ($1B cash + $2.25B in MRVL shares)
- Photonic Fabric™ technology: 25× off-package bandwidth vs copper
- Thermal stability for multi-kW XPU environments
- NVIDIA invested $2B in Marvell to support this roadmap

### Optical Interconnect — 800G/1.6T Market

**Market Scale (2025-2026):**
- AI optical transceiver market: $16.5B (2025) → $26B (2026), +57% YoY
- 800G units: 24M+ shipped in 2025; 63M projected for 2026 (+2.6×)
- 1.6T units: <1M (2025, pilot); 5M+ (2026 forecast by Cignal AI)
- 1.6T module price: $1,300-1,500 per module
- OSFP-XD: 92% of hyperscale data center contracts in 2025

**Enabling Technology — 200G/Lane EML:**
- 100 GBaud EML modulation enables 200 Gbps per lane (PAM4)
- O-band CWDM wavelengths: 1271/1291/1311/1331 nm
- Only volume supplier at launch: Lumentum
- McKinsey: 40-60% 800G shortfall through 2027; 30-40% 1.6T shortfall through 2029
- NVIDIA $4B investment (Lumentum + Coherent, March 2026): strategic response to bottleneck

**LPO Specification (2025):**
- LPO MSA released 100G/lane standard
- 800G LPO: <8.5W vs >16W for DSP modules (50% power reduction)
- Eliminates DSP chip; replaces with high-linearity TIA + driver
- Form-factor agnostic (QSFP, QSFP-DD, OSFP)
- Deployed by Arista, Cisco, Juniper in AI cluster switches

**Silicon Photonics Market Share in Transceivers:**
- 800G: ~40-45% Si photonics
- 1.6T: ~60% Si photonics (modulator integration advantage)

### Optical I/O Chiplets

**Ayar Labs TeraPHY UCIe (March 31, 2025):**
- World's first UCIe-compliant optical chiplet
- Bandwidth: 8 Tbps bidirectional per chiplet
- Wavelengths: 16 (DWDM, C-band)
- Energy: 5 pJ/bit
- Protocols supported: CXL, NVLink, UALink, Ethernet (any UCIe streaming mode)
- Light source: SuperNova multi-wavelength chip
- Status: Prototypes complete; production samples in 2026
- Funding: $500M raise; investors include NVIDIA, Intel, AWS

**Intel OCI Chiplet:**
- 4 Tbps bidirectional throughput
- ~5 pJ/bit energy
- Fully integrated: InP on-chip laser + Si photonics IC + electrical IC
- First chiplet with integrated laser (eliminates external light source)
- Target: CPUs, GPUs, IPUs, SoCs

**Avicena LightBundle (March 2025 launch; March 2026 eKit):**
- Technology: GaN microLED arrays (vs laser-based optical I/O)
- I/O density: >1 Tbps/mm shoreline (roadmap: 10 Tbps/mm²)
- Energy: <1 pJ/bit system; 200 fJ/bit Tx demonstrated; 80 fJ/bit LED energy equivalent
- Per-lane rate: 4 Gbps (December 2025 operational)
- Reach: >10 meters
- TSMC partnership for PD array fabrication
- LightBundle eKit launched March 2026 (first evaluation platform for microLED optical interconnect)

### Silicon Photonics Foundry Ecosystem

**GlobalFoundries (November 2025 + May 2026 updates):**
- Acquired AMF (Singapore): largest pure-play SiPho foundry by revenue
- Acquired Infinilink (Egypt): monolithic SiPho design IP
- 2025 SiPho revenue: >$200M (doubled YoY)
- 2026 target: ~$400M (now revised upward with SCALE CPO ramp)
- Long-term target: >$1B run-rate by end 2028 (confirmed May 7, 2026, TrendForce/GF Q1 earnings)
- Manufacturing: AMF 200mm (roadmap to 300mm)
- Current capability: 200G/lane production
- Roadmap: 400G/lane and beyond
- US Photonics Center: New York Advanced Packaging and Photonics Center (Jan 2025)

**GF SCALE CPO Platform (May 4, 2026) — NEW (Run #1):**
- SCALE = Silicon Photonics Co-packaged Advanced Light Engine
- Industry's first OCI MSA (Optical Compute Interconnect Multi-Source Agreement)-compliant CPO platform
- CWDM and DWDM bi-directional transmission; 8λ and 16λ configurations
- 50 Gbps and 100 Gbps per lane via micro-ring modulators
- Ecosystem: SENKO wafer-level detachable fiber interface; Corning/EXFO testing; Siluxtek 200G/lane SiPho receiver chips
- Significance: First non-TSMC foundry to launch an OCI MSA CPO platform, directly competing with TSMC COUPE for AI accelerator interconnect sockets

**Tower Semiconductor:**
- CPO Foundry launched November 2025
- 300mm wafer bonding technology
- PH18DA platform: 400G/lane modulator demonstrated (>3.5 dB extinction ratio)
- Multi-wavelength on-chip laser (with Xscape Photonics): first optically pumped on-chip multi-λ source on mature high-volume SiPho
- Capacity tripling by mid-2026 (+300% vs 2025 equivalent period)

**imec / UMC (December 2025):**
- UMC licensed imec iSiPP300 silicon photonics process
- Risk production at UMC: 2026-2027
- iSiPP400 (400G/lane platform): in development, target mid-2026
- ECOC 2025: GeSi EAM >110 GHz bandwidth, 400 Gbps/lane on 300mm CMOS
- STARLight EU consortium (September 2025): imec + partners for 300mm SiPho advances

**LightCounting Forecast:**
- 2026 = "The Year of Silicon Photonics"
- Commercial breakthrough across data center, telecom, and defense markets converging

### Device Physics Advances

**Silicon Microring Modulator at 400 Gbps/λ (Laser & Photonics Reviews, 2025):**
- >110 GHz electro-optic bandwidth
- 400 Gbps per wavelength operation
- 4×400G WDM transmitter on 300mm CMOS (1.6 Tbps per chip)
- Platform: Standard CMOS silicon photonics
- O-band and C-band demonstrated

**TFLN Modulator >200 GHz at 0.1 V·cm (Advanced Photonics Research, 2026):**
- Vπ·L = 0.1 V·cm (record efficiency for TFLN)
- Bandwidth: >200 GHz (highest reported)
- Drive voltage: 1V at 1mm device length
- Technique: High-permittivity Bragg waveguide structure
- Industry: HyperLight (145 GHz, 448 Gbps PAM4); Liobate (1.6T coherent at OFC 2026)

**Hollow-Core Fiber 0.091 dB/km (Southampton/Microsoft, September 2025):**
- Attenuation: 0.091 dB/km at 1550 nm (below silica Rayleigh floor of 0.14 dB/km)
- Latency advantage: 30-47% lower propagation delay vs glass fiber
- Light speed: ~1.45× faster than silica fiber (propagates through air, n≈1)
- Deployment: Ciena CTO (March 2026) confirms HCF as "future generation"

### Photonic Computing

**End-to-End On-Chip Photonic DNN (Light: Science & Applications, 2025):**
- 17 mm² silicon photonic chip
- 64-channel optical input (largest demonstrated to date)
- Convolutional + fully connected layers on single chip
- On-chip optoelectronic nonlinear activation functions
- Platform: Standard CMOS silicon photonics

**262 TOPS Photonic Accelerator (arXiv, March 2025):**
- Architecture: Si3N4 microresonator frequency comb + hyperdimensional computing
- Throughput: 262 TOPS
- Frequency comb provides multi-wavelength parallel compute channels
- HDC naturally maps to WDM photonic hardware

**Lightmatter Envise:**
- 65.5 TOPS, 78W electrical (54% power vs A100 equivalent)
- 4 photonic chips, 512 light beams, 200,000+ optical components
- Production status: Commercial availability

**Photonic Spiking Neural Networks (Optica, 2026):**
- Real-time online learning in photonic SNN hardware
- Reinforcement learning without host processor gradient computation
- 128-channel SNN chip on roadmap
- <1 pJ per synaptic event target

### Optical Switching

**OCS Market (2025-2034):**
- Market size 2025: $3.8B → $9.7B (2034)
- AI workload traffic growth: ~120% YoY in hyperscale (2025)

**MEMS OCS for GPU Fabrics:**
- Sub-microsecond circuit provisioning
- Directed optical paths between GPU pods for all-reduce operations
- 15-25W/port savings vs multi-hop electronic switching
- OFC 2026: OCS presented as standard architecture for >10,000 GPU clusters

**NTT IOWN All-Photonics Network:**
- OFC 2025: 1 Tbps optical paths demonstrated
- Expo 2025 Osaka: APN deployment for pavilion connectivity
- 455 Tbps over 1,000 km demonstrated
- PEC-2 switch: 102.4 Tbps, Broadcom collaboration, commercial 2026
- MWC 2026: AI video analysis over APN demonstrated

---

## Summarized Papers

### Tier 1 — Commercial Products (TRL 8-9)

1. **NVIDIA Spectrum-X/Quantum-X Photonics**: 400 Tb/s CPO switches; 3.5× power efficiency; 200G/lane SerDes; 4× fewer lasers (GTC 2025)
2. **Broadcom TH6 Davisson**: 102.4 Tbps CPO Ethernet switch; 70% power savings; TSMC COUPE; shipping October 2025
3. **Ayar Labs TeraPHY UCIe**: 8 Tbps/chiplet; 5 pJ/bit; 16-wavelength DWDM; first UCIe optical chiplet (OFC 2025)
4. **Lightmatter Passage M1000**: 114 Tbps aggregate; 1.6 Tbps/fiber record; 3D photonic interposer (March 2025)
5. **Marvell/Celestial AI**: $3.25B acquisition; Photonic Fabric 25× bandwidth vs copper; Feb 2026
6. **GF + AMF**: Largest pure-play SiPho foundry; $200M+ revenue; 200G/lane production; Nov 2025

### Tier 2 — Prototypes/Near-Commercial (TRL 5-7)

7. **Intel OCI Chiplet**: 4 Tbps; 5 pJ/bit; integrated InP laser; first fully integrated OCI
8. **Avicena LightBundle**: >1 Tbps/mm; 80-200 fJ/bit; 4G/lane operational; eKit March 2026
9. **imec GeSi EAM (iSiPP300)**: >110 GHz; 400 Gbps/lane; 300mm CMOS; ECOC 2025
10. **Tower 400G Modulator (PH18DA)**: 400G/lane; >3.5 dB ER; multi-λ on-chip laser prototype
11. **TSMC COUPE**: SoIC-X; 5-10× efficiency; CPO CoWoS production 2026
12. **Hollow-Core Fiber**: 0.091 dB/km; 30-47% latency advantage; Sept 2025

### Tier 3 — Research Demonstrations (TRL 3-5)

13. **Si MRR 400 Gbps/λ**: >110 GHz EO bandwidth; 4×400G WDM = 1.6 Tbps/chip; Laser & Photonics Reviews 2025
14. **TFLN >200 GHz Modulator**: 0.1 V·cm; 1V drive at 1mm; Advanced Photonics Research 2026
15. **On-chip Photonic DNN**: 17 mm²; 64-channel; convolutional+FC on single chip; Nature 2025
16. **262 TOPS Photonic HDC**: Si3N4 comb; hyperdimensional computing; arXiv March 2025
17. **Photonic SNN Reinforcement Learning**: Online learning; 128-channel roadmap; Optica 2026
18. **Tiled Optical Matrix Multiply**: 96.6% accuracy at 50 Gbaud; PMC 2025
19. **Photonic ADC**: 321 MHz RF, 40 MS/s, 2-4 bit reconfigurable; JLT 2025-2026
20. **Si Photonic OCS on 300mm**: Large-scale O-band switches for AI/ML fabrics; PMC 2025-2026

---

## Technical Analysis

### Energy Efficiency Landscape

The photonics period shows a clear stratification of energy efficiency by technology class:

| Technology | Energy | Bandwidth | Distance | TRL |
|------------|--------|-----------|----------|-----|
| Avicena LightBundle (microLED) | 80-200 fJ/bit | 4 Gbps/lane | <10m | 6-7 |
| CPO (Broadcom TH6) | ~0.5 pJ/bit est. | 800G-1.6T | <100m | 9 |
| Ayar Labs TeraPHY | 5 pJ/bit | 8 Tbps/chiplet | <100m | 7-8 |
| Intel OCI Chiplet | ~5 pJ/bit | 4 Tbps | <100m | 7-8 |
| LPO 800G | ~10 pJ/bit est. | 800G | <2km | 9 |
| DSP Pluggable 800G | ~20 pJ/bit est. | 800G | 2-10km | 9 |

The ~100× gap between Avicena's microLED technology (80 fJ/bit) and DSP pluggables (~20 pJ/bit) reflects the fundamentally different physics: direct-modulation microLEDs eliminate laser threshold, driver amplifiers, and DSP.

### Bandwidth Scaling

**Achieved (2025-2026):**
- Per-wavelength modulation: 400 Gbps/λ (Si MRR, TFLN)
- Per-chiplet I/O: 8 Tbps (Ayar TeraPHY)
- Per-switch aggregate: 102.4 Tbps (Broadcom TH6)
- Per-fiber: 1.6 Tbps (Lightmatter CPO)
- System-level: 400 Tbps (NVIDIA Quantum-X)

**Projected (2027-2028):**
- Per-wavelength: 800 Gbps-1.6 Tbps (TFLN, advanced InP)
- Per-chiplet I/O: 16+ Tbps (next-gen TeraPHY)
- Per-switch: 200+ Tbps (next-gen CPO)

### Insertion Loss Budget

State-of-the-art measured values:
- Chip-to-fiber coupling: 0.34 dB (best demonstrated)
- Stacked-chip via interconnect: 0.94 dB at 1550nm
- Si waveguide propagation: <0.66 dB over practical chip lengths
- Grating coupler (standard): 2-4 dB (limiting component)
- SiN waveguide propagation: 0.034 dB/m (passive components)

CPO removes external coupling loss by integrating optics in-package, saving 3-6 dB vs pluggable fiber attach. This translates directly to power savings at the laser source.

### Wavelength Plans

- **O-band (1270-1350 nm):** Dominant for <2 km data center links (zero dispersion window); CWDM4 (1271/1291/1311/1331 nm), LWDM8 (8 channels)
- **C-band (1530-1565 nm):** Coherent long-haul; microring resonators tunable here; TSMC COUPE targets C-band
- **Multi-band WDM:** 16-wavelength DWDM in Ayar TeraPHY and Lightmatter CPO for maximum spectral utilization

---

## Architectural Observations

### 1. CPO Architecture Convergence

The industry has converged on a common CPO architecture pattern:
```
ASIC Die
    ↓ (SoIC-X / flip-chip / wire bond)
Photonic Engine (Si photonics: modulators, WGs, couplers)
    ↓ (wafer bonding / hybrid integration)
Laser Source (InP, externally supplied or on-chip)
    ↓
Fiber Array (MT/MPO connector)
```

TSMC COUPE implements this as a 3-layer package:
- Layer 1: Switch ASIC (electrical)
- Layer 2: Silicon photonic die (SoIC-X bonded to ASIC)
- Layer 3: Fiber attach and laser block

### 2. Scale-Up vs Scale-Out Optical Architectures

Two distinct photonic I/O use cases are emerging with different requirements:

**Scale-Up (GPU-to-GPU within pod):**
- Distance: <1m to 10m
- Bandwidth density: maximize (Tbps/mm²)
- Energy: minimize (fJ/bit range desired)
- Technology: microLED (Avicena), UCIe chiplet (Ayar), CPO (NVIDIA, Broadcom)
- Key metric: bandwdith density at lowest possible pJ/bit

**Scale-Out (pod-to-pod, rack-to-rack):**
- Distance: 10m to 2km
- Bandwidth: 800G-1.6T per link
- Energy: important but secondary to reach
- Technology: 1.6T pluggable, CPO switch ports, LPO
- Key metric: pJ/bit at target reach and reliability

### 3. Photonic Fabric Architecture Emergence

The Marvell/Celestial AI Photonic Fabric and NTT IOWN represent a third architectural pattern: **end-to-end photonic connectivity** from ASIC to network backbone without intermediate O-E-O conversion. This requires:
- On-package optical I/O (CPO or optical chiplet)
- Optical switching fabric (OCS or photonic switch)
- Coherent or direct-detect optical transmission
- Software-defined optical plane (wavelength assignment, path provisioning)

### 4. Laser Supply as Architectural Constraint

The EML supply crisis is forcing architectural decisions:
- CPO uses fewer lasers (4× fewer in NVIDIA implementation) → conserves scarce supply
- LPO uses standard EML but fewer watts → reduces power, not laser count
- MicroLED (Avicena) uses no laser → eliminates dependency entirely
- On-chip laser (Intel OCI) uses integrated InP → different supply chain

This creates a strategic bifurcation: laser-based CPO (NVIDIA, Broadcom, Ayar) vs laser-free approaches (microLED for short reach, InP-integrated for mid-range).

---

## Trend Analysis

### Trend 1: CPO Replaces Pluggable at Switch Layer (2025-2028)

The period marks the irreversible transition away from pluggable optics at the switch ASIC layer for leading AI fabrics. Once TSMC COUPE is in volume production (2026), every major switch ASIC designer (NVIDIA, Broadcom, Marvell) will offer CPO as the default. Pluggable optics migrate to edge ports and lower-bandwidth links.

**Evidence:** Broadcom TH6 (shipping), NVIDIA Quantum-X (late 2025), Spectrum-X (2026), TSMC COUPE production confirmed.

### Trend 2: 800G → 1.6T Transition Constrained by EML (2025-2027)

1.6T is technically ready but supply-constrained by 200G/lane EML scarcity. The market will sustain 800G as the volume workhorse through 2026-2027 while 1.6T ramps. This is consistent with prior technology transitions (400G → 800G took 2 years of supply buildup).

**Evidence:** TrendForce $26B market; Cignal AI 5M 1.6T units; McKinsey supply shortfall projections; NVIDIA $4B laser investment.

### Trend 3: Energy Efficiency as Primary Design Metric (2025+)

Power is the primary constraint for AI data center expansion (not raw bandwidth). All architectural innovations — CPO, LPO, microLED, OCS — are fundamentally driven by power reduction. The metric shift from "bits per second" to "bits per joule" is now complete at the system design level.

**Evidence:** Every major announcement quantifies power savings (CPO 60-73%, LPO 50%, microLED 25-60×). Hyperscaler infrastructure teams now specify pJ/bit as primary procurement criterion.

### Trend 4: Foundry Consolidation Creating SiPho Oligopoly (2025-2026)

Silicon photonics manufacturing is consolidating around 4 major players:
1. **TSMC**: Premium, leading-edge CPO (NVIDIA, Broadcom)
2. **GlobalFoundries (+ AMF)**: Pure-play SiPho for mid-tier and defense
3. **Tower Semiconductor**: High-volume transceiver components; 300mm CPO Foundry
4. **imec/UMC**: Licensed process for cost-effective 300mm production

Smaller players (AMF, Infinilink) absorbed by GF. This concentration will drive yield improvements and cost reduction but creates geopolitical supply risk.

### Trend 5: Photonic AI Compute Moves From Lab to Pre-Commercial (2025-2027)

The 17 mm² multi-layer photonic DNN chip, 262 TOPS photonic accelerator, and Lightmatter Envise commercial product represent a continuum from research to commercial. The missing link — optical weight memory — remains an active research problem preventing commercial inference systems from equaling GPU performance-per-watt across diverse workloads. Expected resolution: 2028-2030.

**Evidence:** Optica 2026 SNN, Nature 2025 DNN, arXiv HDC chip, Lightmatter $400M raise.

### Trend 6: Optical Circuit Switching Enters AI Fabric Standard (2026)

OCS transitions from telecom-only to AI factory standard in 2026. The MEMS-based OCS overlay creates dedicated optical paths for large all-reduce operations, with sub-microsecond reconfiguration. OFC 2026's language shift to "AI fabric" for OCS signals industry consensus.

**Evidence:** $3.8B OCS market, Cignal AI OCS analysis, NTT PEC-2, PMC 300mm OCS paper.

---

## Manufacturing Implications

### 1. 300mm Wafer Dominance

The period solidifies 300mm wafers as the silicon photonics manufacturing standard:
- GF acquired AMF (200mm) with explicit 300mm roadmap
- Tower CPO Foundry uses 300mm bonding
- imec iSiPP300 licensed to UMC at 300mm
- ST PIC100 at 300mm Crolles, France (production H2 2025)
- 65% of SiPho foundries now have 300mm capability

**Yield improvement:** Mature 300mm processes exceed 85% yield. Wafer-level testing reduces downstream failures by 30-35%. 300mm vs 200mm provides ~2.25× more die per wafer at same density, directly lowering cost.

### 2. Heterogeneous Integration Complexity

CPO requires co-packaging 3+ dissimilar die types:
- **ASIC**: advanced CMOS (5nm-3nm, TSMC)
- **Silicon photonic die**: SiPho process (65nm-90nm equivalent features)
- **III-V die**: InP laser on GaAs/InGaAsP (different CTE — coefficient of thermal expansion)
- **DRAM**: HBM on same substrate (Marvell XPU)

CTE mismatch between InP (~5 ppm/°C) and Si (~3 ppm/°C) creates packaging stress that limits yield. TSMC COUPE's SoIC-X approach addresses this by using interposers to buffer thermal stress. This is the primary yield-limiting mechanism for CPO at scale.

### 3. Laser Supply Chain Restructuring

The laser supply crisis is driving vertical integration and geographic diversification:
- NVIDIA: $2B in Lumentum + $2B in Coherent (March 2026)
- Broadcom: TSMC COUPE manages laser supply through packaging partnership
- Intel: Integrated InP laser in OCI chiplet (eliminates separate laser supply)
- Avicena: GaN microLED (eliminates III-V laser supply chain entirely)

Structural forecast: 2-3 additional EML manufacturers will qualify 200G/lane production by 2027, resolving the bottleneck. Until then, $4-5B in strategic investments will secure priority allocation for NVIDIA and Broadcom.

### 4. Foundry Wars and Capacity Racing

All major SiPho foundries are simultaneously expanding:

| Foundry | Expansion | Timeline |
|---------|-----------|---------|
| Tower | 3× capacity | Mid-2026 |
| GF (+ AMF) | 200mm → 300mm upgrade | 2026-2027 |
| TSMC COUPE | Volume production | 2026 |
| UMC (iSiPP300) | Risk production | 2026-2027 |
| ST PIC100 | 300mm Crolles | H2 2025 |

Risk: Simultaneous expansion may create overcapacity by 2027-2028 if AI capital expenditure moderates, similar to 2023 transceiver inventory correction.

---

## Scalability Considerations

### 1. Per-Wavelength Rate Scaling Roadmap

Current demonstrated rates and forward trajectory:

| Year | Si MRR | TFLN MZM | GeSi EAM |
|------|--------|----------|---------|
| 2025 | 400 Gbps/λ | 448 Gbps | 400 Gbps |
| 2026E | 400-800 Gbps/λ | 400G/lane (commercial) | 400-800 Gbps |
| 2027E | 800 Gbps/λ | 800 Gbps/λ | 800 Gbps/λ |
| 2028E | 1.6 Tbps/λ | 1.6 Tbps/λ | 1.6 Tbps/λ |

400 Gbps/lane × 8 lanes = 3.2 Tbps module (production 2027-2028)

### 2. WDM Channel Density Scaling

Wavelength division multiplexing allows linear bandwidth scaling per fiber:
- Current: 16 channels (Ayar TeraPHY, Lightmatter CPO)
- Near-term: 32-64 channels (with C-band + L-band extension)
- Each doubling of channels doubles per-fiber bandwidth at same lane rate
- Constraint: channel spacing (25-100 GHz) vs thermal stability of microring filters

### 3. CPO Scaling Limits

CPO bandwidth scales with switch ASIC SerDes density:
- 2025: 102.4 Tbps (128 × 800G ports)
- 2027E: 204.8 Tbps (128 × 1.6T or 256 × 800G)
- 2028E: 409.6 Tbps (256 × 1.6T)

Physical constraint: photonic die area on substrate scales with port count. At ~0.5 mm² per 800G optical engine, a 256-port CPO switch requires ~128 mm² of photonic silicon — feasible on 300mm wafers but approaching reticle size limits.

### 4. Photonic Computing Scale Challenges

| Challenge | Current State | Path to Resolution |
|-----------|-------------|-------------------|
| Optical weight memory | No efficient solution | PCM materials, ~2027-2028 |
| Analog precision | ~6-8 effective bits | Error correction, ~2027 |
| Loss accumulation at scale | Limits to ~64-128 neurons/layer | SOA amplification, ~2027 |
| Thermal sensitivity | Requires active heater feedback | Athermal waveguides, ~2026 |
| Fan-in/fan-out loss | 3-6 dB per splitting | Optimized splitter design |

The 128-channel photonic SNN roadmap (Optica 2026) and frequency comb approaches address loss accumulation by providing parallel channels rather than cascaded operations.

### 5. Data Center Infrastructure Scaling

At full AI factory scale (100,000+ GPU), photonic interconnect must handle:
- **Scale-up bandwidth:** 8-16 Tbps per GPU (NVLink-equivalent)
- **Scale-out bandwidth:** 800G-1.6T per GPU-to-network port
- **OCS reconfiguration:** Sub-microsecond to millisecond depending on traffic pattern
- **Fiber count:** 100,000 GPU × 8 fibers/GPU = 800,000 fiber connections per data hall

The fiber count challenge (not bandwidth or power) may become the primary physical infrastructure constraint at gigawatt-scale AI factories.

---

## Strategic Insights

### 1. Vertical Integration Wave

The period is characterized by aggressive vertical integration across the AI supply chain into optical components:
- NVIDIA: Switch photonics (Spectrum-X) + laser investment ($4B)
- Marvell: Optical interconnect IP ($3.25B Celestial AI)
- Broadcom: CPO switch (TH6) + TSMC partnership
- Intel: Integrated OCI chiplet (absorbs optical function onto chip)
- Microsoft: HCF (Lumenisity acquisition)

Companies that own their optical supply chain will have significant power per watt advantages over those dependent on commodity transceivers. This is the optical equivalent of Apple's vertical integration into SoC design.

### 2. The Power Budget Forcing Function

Every 100 MW AI factory can support:
- With DSP pluggables: ~50,000 GPUs (at ~2kW/GPU + ~500W networking)
- With LPO: ~55,000 GPUs (network power saved → more GPU power budget)
- With CPO: ~65,000+ GPUs (60-73% network power savings → substantially more compute density)

The power savings from CPO/LPO translate directly to additional GPU compute per dollar of data center infrastructure, creating a business case that fully justifies the technical complexity of CPO deployment.

### 3. Standards Race Favors Open Ecosystem

The emergence of competing standards (UCIe for optical chiplets, OIF for pluggables, LPO MSA) creates a tension between:
- **Proprietary ecosystems** (NVIDIA NVLink-Photonics, Broadcom CPO)
- **Open standards** (UCIe optical chiplets via Ayar, OIF 400ZR/800ZR)

Ayar's UCIe optical chiplet approach enables multi-vendor AI chip ecosystems; proprietary CPO (NVIDIA, Broadcom) locks customers into single vendor for optical and ASIC. Hyperscalers building custom AI silicon (Microsoft, Google, Amazon) are incentivized toward UCIe/open standards to avoid vendor lock-in.

### 4. Silicon Photonics as Geopolitical Asset

The January 2025 U.S. DoC investment in GF's New York photonics center and the STARLight EU consortium signal that silicon photonics is now a national security / strategic industry, not just a commercial technology. Defense, aerospace, and secure communications applications are growing alongside data center use cases.

U.S. and EU industrial policy is creating domestic SiPho manufacturing capacity outside of TSMC's Taiwan concentration — an explicit supply chain diversification strategy.

### 5. The Startup Consolidation Moment

Valuations at peak:
- Lightmatter: $4.4B (January 2025 Series D)
- Celestial AI: $3.25B acquisition (February 2026)
- Ayar Labs: ~$1B valuation; $500M+ raised

This represents peak startup era for photonic interconnect — the subsequent phase will be integration into large semiconductor companies. The $3.25B Celestial AI acquisition sets the M&A benchmark. Remaining independents (Lightmatter, Avicena) face pressure to either IPO or be acquired within 2-3 years.

---

## Open Questions

1. **Laser Supply Normalization Timing**: When will 200G/lane EML production normalize to meet demand? NVIDIA's $4B investment accelerates Lumentum and Coherent capacity, but process qualification takes 12-18 months. Best estimate: H2 2027.

2. **CPO Yield at Volume**: TSMC COUPE entering volume production in 2026, but CTE mismatch between InP laser blocks and Si substrate has not been quantified publicly. What is the CPO package yield at high volume, and how does it compare to pluggable module yield (typically >99%)?

3. **Photonic Weight Memory**: What material system will enable practical non-volatile optical weight storage for neural networks? PCM (Ge2Sb2Te5) shows promise at 2-4 bits/cell but cycle endurance (<10⁶ writes) limits training applications. No breakthrough demonstrated yet.

4. **Athermal Microring Design**: Temperature sensitivity of microring resonators (0.1 nm/°C wavelength drift) requires active heaters consuming ~5-10 mW/ring. At 16-channel WDM with hundreds of rings, heater power can dominate. When will athermal designs reach commercial viability?

5. **OCS Control Plane**: Nanosecond-to-microsecond OCS for AI GPU fabric requires sub-microsecond job scheduling visibility. What software stack enables the optical control plane to reconfigure paths in coordination with GPU job scheduler? No production solution exists as of May 2026.

6. **MicroLED Scale-Up Beyond 4G/Lane**: Avicena's LightBundle achieves remarkable energy efficiency at 4 Gbps/lane, but AI scale-up requires 100-400 Gbps/lane per die. What is the path to higher per-lane rates? Modulation bandwidth of GaN microLEDs is physically limited by carrier lifetime (~1 ns → ~1 GHz fundamental limit), suggesting multi-channel rather than higher-lane-rate architecture.

7. **HCF Commercial Deployment Infrastructure**: Hollow-core fiber requires different splicing equipment, connectors, and dust protection than SMF. When will a complete HCF infrastructure ecosystem be commercially available at data center scale?

8. **Photonic AI Precision Gap**: Demonstrating 6-8 effective bits of analog precision in photonic computing. What architecture closes the gap to INT8 (8-bit) parity with electronic accelerators while maintaining energy advantage?

9. **NTT IOWN vs Industry CPO**: NTT's all-photonic network vision requires eliminating OEO conversion at every network node. The rest of the industry is deploying CPO (E-O conversion at package level). Are these compatible architectures or competing paradigms?

10. **Samsung CPO Timeline**: Samsung targets CPO Turnkey not until 2029, 3 years behind TSMC. Does this create an opportunity for GF, Tower, or imec to capture Samsung's customers in the 2026-2029 window?

---

## Source Index

| # | Title | URL | Date | Tags |
|---|-------|-----|------|------|
| 1 | Silicon photonics set to make commercial breakthrough in 2026 | https://www.digitimes.com/news/a20251229PD203/siph-cpo-optical-communications-broadcom-nvidia-2026.html | Dec 2025 | silicon-photonics, co-packaged-optics |
| 2 | Where CPO technology stands in 2026 (EDN) | https://www.edn.com/where-co-packaged-optics-cpo-technology-stands-in-2026/ | Jan 2026 | co-packaged-optics |
| 3 | Five Key Trends of CPO in 2026 (Siemens) | https://blogs.sw.siemens.com/semiconductor-packaging/2026/02/05/five-key-trends-of-co-packaged-optics-cpo-in-2026/ | Feb 2026 | co-packaged-optics |
| 4 | Co-Packaged Optics Gain Traction in Data Centers (Mitsui) | https://www.mitsui.com/mgssi/en/report/detail/__icsFiles/afieldfile/2026/04/01/2601bt_tsuji_e.pdf | Apr 2026 | co-packaged-optics |
| 5 | LightCounting: 2026 — The Year of Silicon Photonics | https://www.lightcounting.com/newsletter/en/november-2025-the-year-of-silicon-photonics-2026-436 | Nov 2025 | silicon-photonics |
| 6 | NVIDIA Announces Spectrum-X/Quantum-X Photonics Switches | https://nvidianews.nvidia.com/news/nvidia-spectrum-x-co-packaged-optics-networking-switches-ai-factories | Mar 2025 | co-packaged-optics, optical-interconnect |
| 7 | NVIDIA: Scaling AI Factories with CPO (Technical Blog) | https://developer.nvidia.com/blog/scaling-ai-factories-with-co-packaged-optics-for-better-power-efficiency/ | Mar 2025 | co-packaged-optics, optical-IO |
| 8 | Broadcom Announces Tomahawk 6 — Davisson 102.4 Tbps CPO | https://investors.broadcom.com/news-releases/news-release-details/broadcom-announces-tomahawkr-6-davisson-industrys-first-1024 | Oct 2025 | co-packaged-optics, silicon-photonics |
| 9 | Broadcom CPO Strategy Analysis (TSPASemiconductor) | https://tspasemiconductor.substack.com/p/broadcoms-cpo-strategy-and-its-implications | Oct 2025 | co-packaged-optics |
| 10 | Intel Demonstrates First Fully Integrated Optical I/O Chiplet | https://newsroom.intel.com/artificial-intelligence/intel-unveils-first-integrated-optical-io-chiplet | 2025 | optical-IO, silicon-photonics |
| 11 | Ayar Labs Unveils World's First UCIe Optical Chiplet | https://ayarlabs.com/news/ayar-labs-unveils-worlds-first-ucie-optical-chiplet-for-ai-scale-up-architectures/ | Mar 2025 | optical-IO |
| 12 | OFC 2025: Ayar Labs UCIe Optical Chiplet | https://opticalconnectionsnews.com/2025/04/ofc-2025-ayar-labs-first-ucie-with-optical-chiplet-for-ai-scale-up-architectures/ | Apr 2025 | optical-IO |
| 13 | Ayar Labs UCIe Optical IO Retimer at Hot Chips 2025 | https://www.servethehome.com/ayar-labs-ucie-optical-io-retimer-at-hot-chips-2025/ | Aug 2025 | optical-IO |
| 14 | Ayar Labs Raises $500M (AI2Work) | https://ai2.work/blog/ayar-labs-raises-500m-to-replace-copper-with-light-in-ai-chips-2026 | 2026 | optical-IO |
| 15 | Lightmatter Passage M1000 Photonic Superchip | https://lightmatter.co/press-release/lightmatter-unveils-passage-m1000-photonic-superchip-worlds-fastest-ai-interconnect/ | Mar 2025 | photonic-compute, optical-interconnect |
| 16 | Lightmatter Achieves Record 1.6 Tbps Per Fiber | https://lightmatter.co/press-release/lightmatter-achieves-record-1-6-tbps-per-fiber-to-accelerate-ai-optical-interconnect/ | Mar 2026 | optical-interconnect, co-packaged-optics |
| 17 | Lightmatter 3D Photonic Interconnect (HPCwire) | https://www.hpcwire.com/2025/12/04/lightmatter-aims-to-leapfrog-i-o-limitations-with-3d-photonic-interconnect/ | Dec 2025 | optical-interconnect |
| 18 | Global AI Optical Transceiver Market $26B (TrendForce) | https://www.trendforce.com/presscenter/news/20260420-13017.html | Apr 2026 | optical-interconnect |
| 19 | 800G Optical Modules Drive Market Recovery in 2025 (HYC) | https://www.hyc-system.com/news/Industry/7177.html | 2025 | optical-interconnect |
| 20 | Optical Communication Trends 2026 (ADTEK) | https://adtek-fiber.com/optical-communication-industry-trends-2026-ai-800g-1-6t-and-future-data-center-connectivity/ | 2026 | optical-interconnect |
| 21 | Marvell Completes Acquisition of Celestial AI | https://www.marvell.com/company/newsroom/marvell-completes-acquisition-of-celestial-ai.html | Feb 2026 | optical-interconnect, silicon-photonics |
| 22 | TFLN Modulator >200 GHz, 0.1 V·cm | https://advanced.onlinelibrary.wiley.com/doi/10.1002/adpr.202500237 | 2026 | silicon-photonics |
| 23 | Top TFLN Modulator Companies in 2026 (Liobate) | https://en.liobate.com/news/top-tfln-modulator-companies-2026 | 2026 | silicon-photonics |
| 24 | 400 Gbps/λ Ultrafast Silicon Microring Modulator | https://onlinelibrary.wiley.com/doi/10.1002/lpor.202502840 | 2025 | silicon-photonics |
| 25 | TSMC COUPE 2026 Production (TrendForce) | https://www.trendforce.com/news/2026/04/01/news-silicon-photonics-race-intensifies-as-tsmc-targets-2026-coupe-production-samsung-eyes-2029-cpo-turnkey/ | Apr 2026 | co-packaged-optics, silicon-photonics |
| 26 | Photonic Chips: Real-Time Learning in SNN (Optica 2026) | https://www.optica.org/about/newsroom/news_releases/2026/photonic_chips_advance_real-time_learning_in_spiking_neural_systems/ | 2026 | photonic-compute |
| 27 | Scaling up On-Chip Photonic Neural Network Inference | https://www.nature.com/articles/s41377-025-02029-z | 2025 | photonic-compute |
| 28 | Neuromorphic Photonic Processor arXiv | https://arxiv.org/html/2504.15044v1 | Apr 2025 | photonic-compute, optical-interconnect |
| 29 | GlobalFoundries Acquires AMF (GF Press Release) | https://gf.com/gf-press-release/globalfoundries-acquires-advanced-micro-foundry-accelerating-silicon-photonics-global-leadership-and-expanding-ai-infrastructure-portfolio/ | Nov 2025 | silicon-photonics |
| 30 | GF Accelerates 400G Silicon Photonics Roadmap | https://convergedigest.com/gf-accelerates-400g-silicon-photonics-roadmap-as-ai-optics-demand-surges/ | 2025 | silicon-photonics |
| 31 | UMC Licenses imec iSiPP300 | https://www.businesswire.com/news/home/20251207617476/en/UMC-Licenses-imecs-iSiPP300-Technology-to-Extend-Silicon-Photonics-Capabilities-for-Next-Generation-Connectivity | Dec 2025 | silicon-photonics |
| 32 | imec 2025 Overview (ECOC GeSi EAM) | https://www.imec-int.com/en/articles/imec-2025-overview | 2025 | silicon-photonics |
| 33 | Tower Semiconductor PH18DA 400G Lane | https://www.sec.gov/Archives/edgar/data/0000928876/000117891325000998/zk2532915.htm | 2025 | silicon-photonics |
| 34 | HCF 0.091 dB/km (Phys.org) | https://phys.org/news/2025-09-hollow-core-optical-fiber-transmits.html | Sep 2025 | optical-interconnect |
| 35 | Avicena LightBundle >1Tbps/mm <1pJ/bit | https://avicena.tech/avicena-announces-modular-lightbundle-optical-interconnect-platform-with-1tbps-mm-i-o-density-and-1pj-bit/ | Mar 2025 | optical-IO |
| 36 | Avicena Launches MicroLED Evaluation Kit | https://avicena.tech/avicena-launches-the-worlds-first-microled-optical-interconnect-eval-kit/ | Mar 2026 | optical-IO |
| 37 | Avicena + TSMC PD Arrays | https://avicena.tech/avicena-works-with-tsmc-to-enable-pd-arrays-for-lightbundle-microled-based-interconnects/ | 2025 | optical-IO |
| 38 | OFC 2025 Optical Breakthroughs (Connector Supplier) | https://connectorsupplier.com/ofc-2025-looks-to-the-future-with-optical-breakthroughs/ | Apr 2025 | optical-interconnect |
| 39 | OFC 2026 AI Forces Optics Into Spotlight (Woodside Capital) | https://woodsidecap.com/ofc-2026-ai-forces-optics-into-the-spotlight/ | 2026 | optical-interconnect, co-packaged-optics |
| 40 | OFC 2026 OCS Reshaping AI Data Center (TSPASemiconductor) | https://tspasemiconductor.substack.com/p/from-packets-to-light-paths-ocs-reshaping | 2026 | optical-interconnect |
| 41 | Large-scale Si Photonic Switches 300mm CMOS (PMC) | https://pmc.ncbi.nlm.nih.gov/articles/PMC12717882/ | 2025-26 | silicon-photonics, optical-interconnect |
| 42 | NTT IOWN APN Evolution (IEEE ComSoc) | https://techblog.comsoc.org/2026/05/09/ntts-iown-is-finally-evolving-to-an-all-photonic-network-apn-physics-based-ai-for-enterprise-ot/ | May 2026 | optical-interconnect |
| 43 | Harnessing Photonics for Machine Intelligence (arXiv) | https://arxiv.org/html/2604.10841v1 | Apr 2026 | photonic-compute, optical-interconnect |
| 44 | 262 TOPS Photonic AI Accelerator Si3N4 (arXiv) | https://arxiv.org/pdf/2503.03263 | Mar 2025 | photonic-compute |
| 45 | Photonic Integrated Circuit Market 2026 (PatSnap) | https://www.patsnap.com/resources/blog/articles/photonic-integrated-circuit-technology-landscape-2026/ | 2026 | silicon-photonics |
| 46 | Analog Nanophotonic Computing Tiled Matrix Multiply (PMC) | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11501591/ | 2025 | photonic-compute |
| 47 | Reconfigurable Si Photonic ADC (JLT Optica) | https://opg.optica.org/jlt/abstract.cfm?uri=jlt-44-8-2996 | 2025-26 | silicon-photonics |
| 48 | AI Networking Arms Race: 800G Today 1.6T Tomorrow | https://tspasemiconductor.substack.com/p/ai-networking-arms-race-heats-up | 2025-26 | optical-interconnect |
| 49 | LPO MSA Releases Specification (NewPhotonics) | https://newphotonics.com/lpo-msa-membership-group-releases-linear-pluggable-optics-lpo-specification/ | 2025 | optical-interconnect |
| 50 | Photonic Neuromorphic Computing Landscape 2026 (PatSnap) | https://www.patsnap.com/resources/blog/articles/photonic-neuromorphic-computing-landscape-2026/ | 2026 | photonic-compute |
| 51 | CPO Market 2026-2036 (IDTechEx) | https://www.idtechex.com/en/research-report/co-packaged-optics-cpo/1138 | 2026 | co-packaged-optics |
| 52 | STARLight EU Consortium (imec) | https://www.imec-int.com/en/articles/imec-2025-overview | Sep 2025 | silicon-photonics |
| 53 | GlobalFoundries Launches SCALE CPO — Industry's First OCI MSA Platform | https://gf.com/gf-press-release/globalfoundries-accelerates-adoption-of-co-packaged-optics-for-advanced-ai-data-centers-with-scale-optical-module-solution/ | 2026-05-04 | CPO, silicon-photonics, OCI-MSA, DWDM |
| 54 | GlobalFoundries SiPho Revenue Doubling 2026, $1B by 2028 (TrendForce) | https://www.trendforce.com/news/2026/05/07/news-globalfoundries-reportedly-sees-silicon-photonics-revenue-doubling-in-2026-passing-1b-by-2028/ | 2026-05-07 | silicon-photonics, market-forecast, CPO |
