# Paper 011: Intel Clearwater Forest — 288-Core E-Core Xeon on 18A at Hot Chips 2025 / MWC 2026

**Source ID**: src-021, src-022  
**Date**: 2025-08-26 (Hot Chips preview) / 2026-03-03 (MWC launch)  
**Venue**: Tom's Hardware, HotHardware

---

## One-Sentence Claim
Intel Clearwater Forest Xeon 6+ delivers 288 Darkmont E-cores across 12 Intel 18A compute tiles with 17% IPC improvement over Sierra Forest, 12-channel DDR5-8000 support, and 1,300 GB/s memory bandwidth, targeting scale-out cloud and network workloads.

## Methodology Summary
Disclosed at Hot Chips 2025 symposium (August 2025). Official launch at MWC 2026 (March 2026). Independent analysis by Tom's Hardware and HotHardware of die composition, core architecture, performance claims, and competitive positioning. Architecture compared against AMD EPYC 9965 (192 Zen 5c cores) and prior Intel Sierra Forest (Xeon 6 E-core, Intel 3 process).

## Quantitative Results
- **Total cores**: 288 Darkmont E-cores per socket
- **Compute tiles**: 12 (each built on Intel 18A)
- **Base tiles**: 3 (Intel 3 process)
- **I/O tiles**: 2 (Intel 7 process)
- **IPC improvement vs Sierra Forest (Darkmont vs prev-gen E-core)**: 17%
- **L2 cache bandwidth**: 2x vs Sierra Forest
- **Memory channels**: 12
- **Memory speed**: DDR5-8000
- **Max memory capacity**: 3 TB (dual-socket)
- **Memory bandwidth**: 1,300 GB/s
- **Combined L3 cache**: 1,152 MB
- **Dual-socket configuration**: 576 cores
- **Launch**: MWC 2026 (March 2026)
- **Process**: Intel 18A (compute tiles) — first server product on 18A

## Stated Limitations
Intel targets Clearwater Forest at scale-out workloads (network functions, cloud infrastructure) where throughput and efficiency per watt dominate. Not intended as a direct high single-thread performance competitor to EPYC 9654 (P-core focused configurations). Single-socket core density (288) vs AMD's 192 Zen 5c core comparison requires per-core performance normalization.

## Inferred Limitations
- 17% IPC improvement is meaningful but comes from the E-core (Darkmont) architecture which still trails AMD Zen 5c in per-core performance; higher core count partially compensates
- 12-tile chiplet assembly increases yield risk and package cost — Intel 18A yield challenges could limit supply through 2026
- DDR5-8000 support requires memory ecosystem readiness that is still developing for high-capacity server DIMMs
- 1,300 GB/s bandwidth is impressive but AMD EPYC 9965's combined SP5 memory subsystem can exceed this in certain configurations
- Clearwater Forest is an E-core-only design; Diamond Rapids (P-core Xeon) is the planned premium response which is delayed to 2027

## Architectural Significance
Clearwater Forest is Intel's most significant server product announcement in the 18A era. The 12-tile chiplet design pushing 288 E-cores represents Intel's answer to AMD's density leadership with EPYC Bergamo and Turin Dense (Zen 5c). The key insight is that E-cores — traditionally "efficiency" cores — have matured to the point where they are legitimate server-class compute units for scale-out workloads. The 17% IPC improvement in Darkmont E-cores over the previous generation is actually larger than some full P-core generation transitions. 12-channel DDR5-8000 with 1,300 GB/s bandwidth shows Intel catching up to AMD's memory subsystem leadership. As the first server product on Intel 18A, Clearwater Forest is also a validation of Intel's manufacturing recovery story.

## Cross-Paper Connections
- **paper-003 (EPYC Turin)**: Primary competitor — AMD's Zen 5c 192-core EPYC is the benchmark to beat
- **paper-004 (Panther Lake)**: Same 18A process; Panther Lake's yield ramp preceded Clearwater Forest production
- **paper-017 (Diamond Rapids)**: Intel's P-core Xeon companion/successor for high single-thread server workloads
- **paper-013 (UCIe 3.0)**: Chiplet interconnect standard relevant to Intel's multi-tile assembly methodology

## Theme Tags
`Intel`, `Clearwater-Forest`, `Xeon`, `E-core`, `18A-process`, `chiplet-CPU`, `server-CPU`, `DDR5-8000`, `data-center`, `scale-out`
