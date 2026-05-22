# Paper 016: Acc-SpMM — Sparse Matrix-Matrix Multiplication on GPU Tensor Cores

**Source ID**: src-031  
**Tier**: 2 (arXiv Preprint)  
**Date**: 2025-01-16  
**URL**: https://arxiv.org/pdf/2501.09251

---

## One-Sentence Claim
Acc-SpMM achieves 2.52x average speedup (up to 5.11x) on RTX 4090 and 1.58x (up to 3.60x) on H100 over cuSPARSE by restructuring sparse matrix-matrix multiplication to exploit tensor core data alignment requirements, demonstrating that general-purpose SpMM performance on tensor cores is significantly under-exploited by existing libraries.

## Methodology Summary
Academic paper implementing optimized SpMM kernels for GPU tensor cores. Tested on RTX 4090, NVIDIA A800, and H100 GPUs. Comparison baseline: NVIDIA cuSPARSE library. The approach restructures sparse matrix storage formats to align with tensor core MMA instruction operand requirements. Benchmarked across diverse sparse matrices from SuiteSparse collection. Published January 2025 on arXiv.

## Quantitative Results
- **RTX 4090 speedup**: 2.52x average, up to 5.11x peak over cuSPARSE
- **A800 speedup**: 1.91x average, up to 4.68x peak over cuSPARSE
- **H100 speedup**: 1.58x average, up to 3.60x peak over cuSPARSE
- **Key insight**: Tensor cores require operand alignment; cuSPARSE does not exploit this
- **Test matrices**: SuiteSparse collection, diverse sparsity levels (0.1% - 10%)
- **Lower gains on H100**: H100 has larger base cuSPARSE throughput, leaving less relative room
- **Technique**: Data layout transformation + tensor core MMA instruction scheduling

## Stated Limitations
- Gains are matrix-dependent; extremely sparse (<0.01% density) matrices see less benefit
- Preprocessing cost (matrix reformatting) not always included in reported speedup
- H100 gains smaller (1.58x) vs RTX 4090 (2.52x) suggesting tensor core generation affects relative gain
- Not tested on Blackwell architecture (B200); 5th-gen tensor core characteristics may differ

## Inferred Limitations
- 2:4 structured sparsity (NVIDIA's hardware accelerated format) not evaluated — unstructured SpMM gains may be supplanted by hardware 2:4 sparsity for eligible workloads
- cuSPARSE is a general-purpose library; domain-specific implementations may close the gap
- Real-world GNN and transformer sparse attention use different sparsity patterns than SuiteSparse matrices
- The RTX 4090 vs H100 gap in gains suggests algorithm tuning needed per-architecture

## Architectural Significance
This work reveals a fundamental underutilization in production GPU sparse libraries: tensor cores are designed for dense MMA operations, and simply calling them with sparse data in standard CSR/CSC format leaves performance on the table. For GPU architecture evolution, this motivates dedicated sparse tensor core hardware (which Blackwell's 5th-gen tensor cores partially address with the structured sparsity engine). For practical applications — GNN training, sparse attention in transformers — the techniques here suggest that 2-5x speedup is achievable without new hardware, purely through smarter data layout and instruction scheduling.

## Cross-Paper Connections
- src-003 (Blackwell tensor cores) covers hardware-level sparsity acceleration that complements this software approach
- src-021 (Blackwell microbenchmarks) characterizes the tensor core capabilities Acc-SpMM exploits
- src-004 (CDNA4 sparsity) covers AMD's 2:4 sparsity hardware implementation
- src-034 (memory bottleneck) explains why reducing SpMM memory traffic via sparsity is critical

## Theme Tags
`sparsity`, `sparse-matrix`, `tensor-cores`, `SpMM`, `cuSPARSE`, `arXiv`, `GPU-optimization`, `performance`, `GNN`
