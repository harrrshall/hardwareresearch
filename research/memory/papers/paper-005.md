# Paper 005: CXL 4.0 Specification — Released November 18, 2025

**Source ID**: 20, 23  
**Source Title**: CXL Consortium Releases CXL 4.0 Specification at SC25; CXL 4.0 Infrastructure Planning Guide  
**URLs**:  
- https://www.businesswire.com/news/home/20251118275848/en/CXL-Consortium-Releases-the-Compute-Express-Link-4.0-Specification-Increasing-Speed-and-Bandwidth  
- https://computeexpresslink.org/wp-content/uploads/2025/11/CXL_4.0-White-Paper_FINAL.pdf  
**Date**: 2025-11-18  
**Tags**: CXL4.0, PCIe7, memory-pooling, disaggregation, interconnect

---

## One-Sentence Claim
The CXL Consortium released CXL 4.0 on November 18, 2025, doubling link bandwidth to 128 GT/s via PCIe 7.0 and introducing bundled ports for 1.5 TB/s aggregate connections, enabling 100+ TB coherent memory pools across AI data center infrastructure.

## Methodology Summary
CXL 4.0 builds on the 256-byte FLIT format from CXL 3.x but shifts the physical layer from PCIe 6.x (64 GT/s) to PCIe 7.0 (128 GT/s). New bundled port capability aggregates multiple physical ports into single logical attachments. Enhanced RAS features were added for production-grade deployment.

## Quantitative Results
- Link speed: 128 GT/s (PCIe 7.0), double the 64 GT/s of PCIe 6.x used in CXL 3.x
- Bundled port bandwidth: 1.5 TB/s per logical port via port aggregation
- Coherent memory pool scale: 100+ TB enabled by CXL 4.0 topology
- Phase 3 production deployment timeline: 2026–2027 for CXL switches with shared memory pools
- CXL memory pooling speedup vs 200G RDMA: 3.8x for LLM inference
- CXL memory pooling speedup vs 100G RDMA: 6.5x for LLM inference
- Astera Labs Leo CXL: 3x concurrent LLM instances at 3x lower latency

## Stated Limitations
- CXL 4.0 hardware products not yet available as of specification release date (Nov 2025)
- Multi-rack systems expected late 2026 to 2027
- Phase 3 memory pooling across racks requires CXL switches not yet in production

## Inferred Limitations
- PCIe 7.0 PHY silicon at 128 GT/s will require advanced packaging and signal integrity solutions not widely deployed
- Coherency protocol overhead at 100+ TB scales introduces latency considerations
- Software ecosystem for CXL memory pooling is immature; OS and hypervisor support is fragmented

## Architectural Significance
CXL 4.0 represents the transition from point-to-point memory expansion (CXL 1.1/2.0) to truly disaggregated, pooled, and dynamically reallocatable memory fabrics. The 1.5 TB/s bundled port bandwidth exceeds current HBM3E per-stack bandwidth, enabling CXL-attached memory expanders to serve as high-bandwidth memory tiers. This is architecturally transformative for LLM serving, where KV cache and model weights can be offloaded to pooled CXL memory.

## Cross-Paper Connections
- Enables LLM inference KV cache offload (paper-018, SC25 XConn/MemVerge work)
- Complements HBM4 (papers 001-003) which serves ultra-high-bandwidth needs while CXL serves capacity
- Disaggregation paper (paper-019) models 20-40% TCO reduction from CXL-based architectures
- CXL 3.1 MXC and CXL 4.0 enable the LPDDR6 data center expansion JEDEC previewed (paper-004)

## Theme Tags
CXL4.0, PCIe7, memory-pooling, disaggregation, bundled-ports, LLM-inference, RAS
