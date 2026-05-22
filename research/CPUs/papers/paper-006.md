# Paper 006: Condor Computing Cuzco RISC-V Core at Hot Chips 2025

**Source ID**: src-016, src-018  
**Date**: 2025-08-25 to 2025-08-29  
**Venue**: Hot Chips 2025 (Peer-Reviewed Symposium), Chips and Cheese analysis

---

## One-Sentence Claim
Condor Computing's Cuzco RISC-V core introduces time-based instruction scheduling that eliminates CAM circuits and instruction replays, achieving 17.5+ SpecInt2006/GHz with only a 5.3% throughput penalty versus an ideal Tomasulo scheduler.

## Methodology Summary
Presentation at Hot Chips 2025 (peer-reviewed symposium) by Condor Computing (subsidiary of Andes Technology, 50-person team). Full hardware emulation completed July 2025, booting Linux. Performance characterization via SpecInt2006 at a range of clock frequencies. Independent analysis by Chips and Cheese of the time-based scheduling mechanism compared to conventional out-of-order approaches.

## Quantitative Results
- **SpecInt2006 per GHz**: >17.5 points/GHz
- **Throughput penalty vs ideal Tomasulo scheduler**: 5.3% on SpecInt2006
- **Pipeline depth**: 12 stages
- **Decode width**: Wide out-of-order (specific width not disclosed, estimated 6-8 wide)
- **Cluster size**: 8 cores per coherent cluster
- **Private L2 per core**: up to 8 MB
- **Shared L3**: 256 MB
- **Compliance**: RVA-23 RISC-V profile (datacenter high-performance)
- **ISA**: RISC-V RVA23 with Hypervisor (H) and Vector (V) extensions
- **Availability**: First customer Q4 2025
- **Team size**: 50 engineers (remarkably small for this performance level)

## Stated Limitations
Condor acknowledges the time-based approach sacrifices approximately 5.3% throughput vs. ideal scheduling (where data dependencies are resolved dynamically in real-time), and that the static/near-static nature of scheduling means code with irregular dependency patterns benefits less.

## Inferred Limitations
- 5.3% penalty vs ideal, but ideal Tomasulo is not achievable in practice due to power/area costs; real comparison should be against commercial out-of-order designs
- RVA23 software ecosystem is still developing — compilers, OS, and runtime support are less mature than x86 or ARM
- 50-engineer team implies limited resources for validation, security hardening, and ecosystem work
- Initial Q4 2025 availability is likely limited engineering samples/early access; broad deployment timeline unclear
- 17.5+ SpecInt2006/GHz is impressive but SPECint2006 is dated — SPECint2017 results not yet published

## Architectural Significance
Cuzco's time-based instruction scheduling is a novel contribution to microarchitecture research. Traditional out-of-order execution uses a Content Addressable Memory (CAM) structure for the reservation station — CAM is expensive in area and power. By predicting when data will be ready (based on cache latencies and pipeline timing) and scheduling instruction dispatch to a precise counter value, Cuzco eliminates the CAM entirely. This reduces both power and area while achieving near-ideal performance. If validated in silicon, this technique could influence future high-performance designs across RISC-V and potentially ARM/x86 architectures. The 50-engineer team achieving this demonstrates that hardware agility (short design cycles, small teams) is becoming viable in the RISC-V ecosystem.

## Cross-Paper Connections
- **paper-007 (SiFive P570 Gen 3)**: Contemporary RISC-V high-performance core using conventional OoO approach, providing baseline comparison
- **paper-008 (Ventana Veyron V2)**: More mature RISC-V server design demonstrating the commercial trajectory Cuzco targets
- **paper-018 (Hot Chips 2025 Session)**: Same venue, cross-architecture comparison context
- **paper-015 (ISCA 2025)**: Research venue context for time-based scheduling related academic work

## Theme Tags
`RISC-V`, `out-of-order`, `time-based-scheduling`, `branch-prediction`, `RVA23`, `Hot-Chips-2025`, `novel-microarchitecture`, `datacenter`, `cache-hierarchy`
