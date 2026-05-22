# Paper 016: Near-Memory Computing — Architectures for AI Edge and LLM Inference

**Source ID**: (PatSnap near-memory analysis, arXiv near-memory review, Science China paper)  
**Source Title**: Near-Memory vs In-Memory Computing; Software-Defined Process-Near-Memory Architecture; APL Machine Learning Memory Review  
**URLs**:  
- https://www.patsnap.com/resources/blog/rd-blog/near-memory-vs-in-memory-computing-patsnap-eureka/  
- https://link.springer.com/article/10.1007/s11432-023-3965-1  
- https://pubs.aip.org/aip/aml/article/3/2/020901/3344006/Memory-technology-enabling-future-computing  
**Date**: 2025  
**Tags**: near-memory-computing, NMC, PNM, AI-edge, LLM, efficiency

---

## One-Sentence Claim
Near-memory computing (NMC) architectures that couple processing logic physically adjacent to DRAM — via TSV or hybrid bonding — achieve 306.7 GOPS/W in 8-bit matrix multiplications, dramatically reducing data movement energy by exploiting 3D-stacked DRAM's wide internal buses.

## Methodology Summary
Near-memory computing (NMC) integrates compute logic adjacent to (but not inside) memory arrays, typically within the memory controller or as an additional processing die in a 3D stack. A Software-Defined Process-Near-Memory (SDPNM) architecture using 3D hybrid bonding achieved high energy efficiency with dynamic reconfiguration. Google's work on 3D-DRAM chiplets for LLM serving uses NMC principles for bandwidth-optimized weight-loading.

## Quantitative Results
- Peak energy efficiency: 306.7 GOPS/W in 8-bit matrix multiplications
- SDPNM energy reduction: significant vs. conventional memory access (specific % proprietary)
- LLM benefit: NMC eliminates repeated DRAM-to-compute weight transfers during autoregressive decoding
- Access granularity improvement: reduces wasted bandwidth from 64B cache line to 4B-32B fine-grained access
- H100 weight transfer baseline: 42ms per token for 70B model at 3.35 TB/s peak bandwidth

## Stated Limitations
- NMC does not modify memory cells for computation; it requires additional logic die which adds cost and area
- Programmability: NMC logic must be tailored to specific workloads (matrix multiply, attention)
- Not yet standardized: each implementation is custom silicon

## Inferred Limitations
- NMC in HBM stacks (HBM-PIM) must balance compute die area vs. memory die count per stack
- Thermal challenges: adding compute to memory stacks increases heat generation in already thermally constrained HBM stacks
- The 306.7 GOPS/W figure is for edge/IoT scale, not datacenter scale; datacenter NMC efficiency ratios may differ

## Architectural Significance
NMC is architecturally positioned between conventional host-to-DRAM data movement and full processing-in-memory (PIM). It offers better programmability than PIM while still achieving substantial energy savings by eliminating long DRAM bus transfers. For LLM inference, NMC directly addresses the memory bandwidth bottleneck where each token generation requires loading all model weights.

## Cross-Paper Connections
- Extends PIM concepts (paper-011) with greater flexibility and without modifying memory cells
- Directly enabled by 3D stacking technologies used in HBM (papers 001-003) and IGZO DRAM (paper-009)
- Google's NMC work cited in context of Vera Rubin ecosystem (paper-007)
- Memory wall problem (paper-018) is what NMC architectures are designed to solve

## Theme Tags
NMC, near-memory-computing, 3D-DRAM, TSV, hybrid-bonding, AI-edge, LLM, efficiency, 306.7GOPS/W
