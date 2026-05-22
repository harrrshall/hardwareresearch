# Paper 022: HBM4 Standardization and Memory Architecture for Next-Generation Server CPUs

**Source ID**: src-033  
**Date**: 2025-04-15 (JEDEC HBM4 finalization)  
**Venue**: Tom's Hardware / JEDEC

---

## One-Sentence Claim
JEDEC's finalization of the HBM4 standard in April 2025 establishes a 2 TB/s per-stack memory bandwidth floor for the next generation of high-performance CPU and AI accelerator designs, with first HBM4 products shipping in late 2025/early 2026 from SK Hynix and Micron.

## Methodology Summary
JEDEC official HBM4 specification publication (April 15, 2025). Tom's Hardware reporting on Micron's product announcements including 256 GB DDR5-12800 server DIMMs. HBM3E current shipping performance data for baseline comparison. NVIDIA Rubin and AMD MI400 roadmap references establishing first HBM4 consumer products.

## Quantitative Results
- **HBM4 interface width**: 2048 bits per stack (double HBM3's 1024-bit)
- **HBM4 per-pin data rate**: up to 8 Gb/s
- **HBM4 bandwidth per stack**: ~2 TB/s
- **HBM4 stack height**: up to 16-Hi with 32 Gb dies = up to 64 GB per stack
- **JEDEC finalization date**: April 15, 2025
- **First HBM4 production**: Late 2025/early 2026 (SK Hynix, Micron)
- **HBM3E reference**: 9.6 Gb/s per pin, 1024-bit = 1.2 TB/s per stack (single-stack comparison)
- **HBM3E vs DDR5**: Single HBM3E stack provides 20x the bandwidth of a DDR5 channel
- **DDR5 expansion**: JEDEC expanded DDR5 spec to 8800 MT/s
- **Micron 256 GB DDR5-12800 RDIMM**: 2026 product based on monolithic 32 Gb DRAM ICs

## Stated Limitations
HBM4's 2 TB/s is per-stack; total system bandwidth depends on stack count per package (typically 4–8 for GPU, fewer for CPU). Die stacking to 16-Hi creates thermal management challenges. First-gen HBM4 products will ship in limited quantities for premium AI accelerators, not mainstream server CPUs.

## Inferred Limitations
- HBM4 will be used primarily in GPU/AI accelerator packages initially; mainstream server CPUs (Intel Diamond Rapids, AMD EPYC Venice) will use DDR5/LPDDR5 until packaging technology matures
- The 2048-bit interface requires extremely precise package assembly — yield challenges may limit early adoption
- HBM4 at 64 GB per stack with limited stack count may still constrain memory capacity vs. DDR5 LPDIMM servers with hundreds of GB
- Micron's 256 GB DDR5-12800 DIMMs are a more immediately practical advancement for server CPUs than HBM4

## Architectural Significance
HBM4's finalization sets the memory architecture trajectory for CPUs from 2026 through 2030. The ~2 TB/s bandwidth enables AI inference workloads with trillion-parameter models in HBM-equipped packages, potentially bringing large language model capabilities to specialized "CPU+HBM" configurations without discrete GPU cards. For mainstream server CPUs, the DDR5-8000/8800 standards (supported by Intel Clearwater Forest DDR5-8000, Diamond Rapids MRDIMM at 12800 MT/s) are the near-term path to higher memory bandwidth. The parallel evolution of HBM4 (for peak bandwidth) and DDR5-8800 (for capacity and cost-effective bandwidth) reflects the "right memory for right workload" design philosophy that will define CPU memory architecture through the decade.

## Cross-Paper Connections
- **paper-011 (Clearwater Forest)**: First server CPU to support DDR5-8000 (12 channels)
- **paper-017 (Diamond Rapids)**: MRDIMM at 12800 MT/s — highest DDR5 bandwidth for P-core Xeon
- **paper-003 (EPYC Turin)**: AMD's current server memory bandwidth with SP5 DDR5
- **paper-013 (UCIe)**: Advanced packaging that enables HBM+CPU integration in same package

## Theme Tags
`HBM4`, `DDR5-8000`, `memory-bandwidth`, `server-CPU`, `JEDEC`, `advanced-packaging`, `AI-inference`, `memory-architecture`
