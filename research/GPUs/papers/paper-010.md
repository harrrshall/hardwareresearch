# Paper 010: TSMC CoWoS Capacity and Advanced Packaging Constraints

**Source ID**: src-025  
**Tier**: 3 (Industry Analysis)  
**Date**: 2025-12-10  
**URL**: https://www.digitimes.com/news/a20251210PD218/tsmc-cowos-capacity-nvidia-equipment.html

---

## One-Sentence Claim
TSMC CoWoS advanced packaging — required for all GPU-HBM integration including Blackwell and CDNA4 — remains critically oversubscribed through 2026, with NVIDIA claiming 60%+ of 650K annual wafers in 2025 and capacity only doubling to ~730K wafers by 2026, making it the tightest bottleneck in the AI semiconductor stack.

## Methodology Summary
Supply chain estimates from multiple analysts including Global Semi Research, DigiTimes, and X/Twitter supply chain intelligence (Ray Wang). TSMC official capacity guidance from earnings calls and technology symposia. NVIDIA and AMD CoWoS allocation figures from supply chain reporting. Outsourcing partner allocations from industry sources.

## Quantitative Results
- **2025 total CoWoS capacity**: ~650,000 wafers annually
- **NVIDIA 2025 allocation**: 370,000 wafers (>56% of total capacity)
- **Monthly capacity 2025**: 75,000–80,000 wafers/month
- **Target monthly capacity end-2026**: 120,000–130,000 wafers/month
- **2026 total target**: ~730,000 wafers (or higher with outsourcing)
- **NVIDIA 2025-2026 booking**: 60%+ of all CoWoS capacity
- **Outsourcing allocation**: 240,000–270,000 wafers/year to Amkor (~180-190K) and SPIL (~60-80K)
- **Market position**: CoWoS oversubscribed through at least 2026
- **Customer lead times**: 6-12 months for non-NVIDIA customers
- **TSMC CoPoS**: New packaging tech, equipment arriving mid-2026

## Stated Limitations
- Supply chain estimates have ±10-15% error margins; exact figures not publicly confirmed by TSMC
- NVIDIA's reported 60%+ CoWoS share may overstate actual allocation post-GB300 ramp
- Outsourcing to Amkor/SPIL involves yield and quality tradeoffs vs. TSMC's CoWoS
- Capacity figures don't distinguish between CoWoS-S and CoWoS-L variants (different GPU applications)

## Inferred Limitations
- ASIC customers (Google TPUs, AWS Trainium, etc.) are capacity-constrained by NVIDIA's CoWoS dominance
- AMD's MI350 and future MI400 availability constrained by CoWoS access when NVIDIA occupies most capacity
- CoWoS outsourcing to Amkor/SPIL may not match TSMC CoWoS-L quality for 8-stack HBM3E designs
- New entrant GPU companies (Moore Threads, Biren) face near-impossible CoWoS access in 2025-2026

## Architectural Significance
CoWoS is not a differentiating innovation — it is the commodity substrate on which GPU performance advances are built. The fact that NVIDIA secures 60%+ of TSMC's CoWoS limits the hardware availability of competing AI accelerators, making CoWoS capacity a strategic resource war rather than a purely technical matter. For GPU architecture, CoWoS-L (Local Silicon Interconnect, used in larger configurations) enables the multi-HBM stack designs that make B200 (192GB) and MI350X (288GB) possible. Without CoWoS-L, HBM counts are limited. The planned doubling of CoWoS capacity 2025→2026 is the primary supply lever for expanding GB300 NVL72 and MI400 availability.

## Cross-Paper Connections
- src-001 (GB200/GB300 performance) depends on CoWoS availability for production ramp
- src-002 (MI350X) similarly constrained by CoWoS allocation
- src-026 (MI400) will require CoWoS-L with HBM4 for 432GB capacity
- src-007 (HBM4) transition also requires CoWoS-L for wider 2048-bit HBM4 interface
- src-039 (cooling advances) shows that advanced thermal solutions co-evolve with packaging

## Theme Tags
`CoWoS`, `advanced-packaging`, `TSMC`, `supply-chain`, `HBM`, `chiplet-GPU`, `manufacturing`, `capacity`, `bottleneck`
