# Paper 019: Memory Disaggregation — CXL-Based TCO Reduction and LLM KV Cache

**Source ID**: 22, 54  
**Source Title**: SC25: XConn/MemVerge CXL KV Cache; arXiv Disaggregated Architectures Data Center  
**URLs**:  
- https://www.storagenewsletter.com/2025/11/21/sc25-xconn-technologies-and-memverge-to-deliver-breakthrough-scalable-cxl-memory-solution  
- https://arxiv.org/html/2511.04104v1  
**Date**: 2025-11 (SC25); 2025-11 (arXiv)  
**Tags**: disaggregation, CXL, KV-cache, TCO, LLM, SC25

---

## One-Sentence Claim
CXL-based memory disaggregation for LLM KV cache offload achieves 3.8x speedup vs 200G RDMA and 6.5x vs 100G RDMA (XConn/MemVerge at SC25), while arXiv modeling shows 20-40% TCO reduction over monolithic server designs at large scale.

## Methodology Summary
XConn Technologies and MemVerge demonstrated at SC25 (November 2025) a scalable CXL memory solution for LLM inference KV cache and prefill/decode disaggregation. The arXiv paper (2511.04104) provides a formal analysis of scheduling, pooling, and TCO trade-offs in disaggregated architectures. Astera Labs deployed Leo CXL Smart Memory Controllers at OCP Global Summit 2025.

## Quantitative Results
- CXL vs 200G RDMA speedup: 3.8x for LLM inference
- CXL vs 100G RDMA speedup: 6.5x for LLM inference
- CXL vs SSD caching: >5x performance improvement for KV cache
- Astera Labs Leo CXL: 3x concurrent LLM instances, 3x lower latency
- arXiv TCO model: 20-40% reduction vs monolithic servers at scale
- Commercial CXL pools of 100 TiB available in 2025

## Stated Limitations
- 3.8x/6.5x speedups are relative to RDMA baselines; absolute token throughput numbers are workload-specific
- CXL memory pooling is still Phase 2-3 technology (tiering 2025-2026; pooling 2026-2027)
- Software ecosystem for CXL memory management is fragmented across OS, hypervisor, and runtime layers

## Inferred Limitations
- CXL memory latency (100-200ns) is ~5-10x higher than local DRAM; benefits depend on workload memory access pattern
- KV cache offload to CXL is specifically suited to long-context LLM inference; short-context inference may not benefit
- 100 TiB commercial CXL pools are early-adopter deployments; production scale reliability data is limited

## Architectural Significance
Memory disaggregation via CXL represents a fundamental shift from the tightly-coupled CPU-memory model. The KV cache offload use case is architecturally significant because KV cache is the dominant memory bottleneck in long-context LLM inference (context windows of 100K-1M tokens). CXL memory pooling enables elastic scaling of memory capacity independent of compute, reducing stranded capacity and improving overall data center utilization.

## Cross-Paper Connections
- Built on CXL 4.0 specification (paper-005) for pooling infrastructure
- Addresses long-context LLM memory limitations documented in memory wall analysis (paper-018)
- Complements HBM4 (papers 001-003) for hot working sets while CXL handles cold/spilled KV cache
- JEDEC's LPDDR6 roadmap (paper-004) for data center SOCAMM2 (paper-013) forms the memory tier between CXL and HBM4

## Theme Tags
disaggregation, CXL, KV-cache, LLM, SC25, XConn, MemVerge, TCO, pooling
