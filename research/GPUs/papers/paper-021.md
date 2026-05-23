# Paper 021 — NVIDIA Q1 FY2027 Earnings: Vera Rubin Supply Constraint + Vera CPU Disclosure
**Validation status:** VALIDATED
**Source:** NVIDIA Q1 FY2027 Earnings Call + CEO Statements, NVIDIA Investor Relations / TechCrunch, May 20, 2026
**URL:** https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-first-quarter-fiscal-2026
**URL2 (Vera CPU):** https://techcrunch.com/2026/05/20/jensen-huang-says-hes-found-a-brand-new-200b-market-for-nvidia/
**Tier:** 1
**Theme tags:** Rubin, supply-constraint, Vera-CPU, agentic-AI, earnings-disclosure, NVLink-6, HBM4

## One-sentence claim
NVIDIA reported $81.6B Q1 FY2027 revenue (+85% YoY) driven by $75.2B in Data Center sales, guided Q2 to $91B, and disclosed that Vera Rubin GPU supply will remain constrained for its entire product life while simultaneously announcing the Vera CPU as a purpose-built agentic-AI processor targeting a $200B addressable market.

## Methodology summary
Primary disclosure via SEC 8-K filing and live earnings call transcript on May 20, 2026. CEO Jensen Huang provided direct forward guidance on Vera Rubin production timelines and supply outlook. Vera CPU details disclosed simultaneously via executive commentary and corroborated by TechCrunch reporting from the same event. Revenue figures are audited quarterly financials; guidance is management's forward estimate with ±2% stated range. Every major hyperscaler confirmed as Vera CPU deployment partner via customer reference list disclosed on the call.

## Quantitative results
- Q1 FY2027 revenue: $81.6B (+85% YoY)
- Data Center segment: $75.2B (+92% YoY)
- Q2 FY2027 guidance: $91B ±2% (vs. consensus ~$87B — approximately $4B beat)
- Vera Rubin production shipments: H2 FY2027 (calendar H2 2026); sampling with customers as of disclosure date
- Vera CPU performance vs. x86: 1.5× perf/core, 2× perf/watt, 4× rack density
- Vera CPU total addressable market: $200B
- Vera CPU FY2027 revenue projection: $20B
- Vera CPU architecture: custom ARM cores

## Stated limitations
- Jensen Huang explicitly stated NVIDIA "will be constrained throughout the entire life of Vera Rubin" — supply, not demand, is the binding constraint at current and forecasted demand levels.
- Vera CPU sampling is underway but full production shipments are not yet in-period; FY2027 $20B projection is forward guidance, not realized revenue.
- No per-customer Vera CPU volume disclosures made.

## Inferred limitations
- The "constrained for entire product life" statement implies that CoWoS advanced packaging yield and HBM4 supply remain the binding chokepoints; NVIDIA cannot simply ramp fab capacity at will because the constraint is upstream at TSMC packaging and SK Hynix/Micron/Samsung HBM4 supply.
- The $200B TAM figure for Vera CPU is CEO-stated and uses a broad definition of the server CPU market; realized capture depends on hyperscaler willingness to displace AMD EPYC and Intel Xeon at scale across general workloads, not only agentic AI.
- The 4× rack density claim for Vera CPU vs. x86 may be measured under agentic AI workload assumptions rather than general-purpose server workloads — the comparison base matters for applicability beyond AI inference.
- Vera CPU custom ARM cores compete directly with AWS Graviton, Ampere Altra, and Microsoft Cobalt; hyperscaler endorsement while also running proprietary ARM CPUs suggests workload segmentation rather than full incumbent displacement.

## Architectural significance
Two structurally distinct signals emerge from this single earnings call. First, the supply-constraint confirmation for Vera Rubin's entire product life is the most important data point for the packaging and memory supply chain sectors: it means CoWoS and HBM4 capacity are structurally undersupplied relative to NVIDIA demand through at least 2027, creating durable pricing power for TSMC packaging and HBM suppliers (SK Hynix, Micron, Samsung). Second, the Vera CPU represents NVIDIA's first direct entry into the $200B general server CPU market — not as a co-processor but as a primary CPU — targeting agentic AI workloads where memory bandwidth, power efficiency, and tight CPU-GPU coupling matter more than legacy ISA compatibility. The 2× perf/watt advantage, if sustained at production, represents a credible challenge to x86 incumbents in the fastest-growing server workload category. The co-design of Vera CPU with NVLink 6 is architecturally meaningful: agentic workloads require low-latency control-plane compute tightly coupled to the GPU memory fabric, which a purpose-built CPU can optimize in ways that x86 cannot.

## Cross-paper connections
- Connects directly to prior GPU papers on CoWoS capacity constraints and HBM4 supply ramp: Vera Rubin's acknowledged supply constraint is downstream of those packaging and memory chokepoints, and the earnings call confirms the constraint extends multi-year rather than resolving at ramp.
- Connects to AI_accelerators/paper-026 (Alibaba Zhenwu M890): the Rubin supply constraint directly accelerates sovereign AI compute programs — customers who cannot secure Rubin allocations face multi-year wait queues; Chinese hyperscalers with domestic alternatives are partially insulated from this constraint.
- Connects to chip_fabrication/paper-026 (ASML High-NA EUV bifurcation): Vera Rubin production at TSMC relies on conventional EUV through 2028 (TSMC delayed High-NA to 2029); packaging yield at CoWoS, not lithography node, is the binding constraint for Rubin supply.
- Connects to interconnects/paper-023 (PCIe 8.0): at ~1.8 TB/s aggregate per GPU, NVLink 6 remains well ahead of PCIe 8.0's target 1 TB/s x16, reinforcing NVIDIA's proprietary interconnect moat for dense GPU clusters through at least 2028.
