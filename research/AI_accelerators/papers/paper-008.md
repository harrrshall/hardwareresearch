# paper-008: SambaNova SN40L/SN50 — Reconfigurable Dataflow Architecture for Enterprise AI

**Tags:** dataflow, transformer-accelerator, LLM-inference  
**Date:** 2025  
**Source:** SambaNova Official, arXiv 2405.07518, SiliconANGLE  
**URL:** https://arxiv.org/pdf/2405.07518

---

## Summary

SambaNova's **Reconfigurable Dataflow Unit (RDU)** represents a commercially deployed dataflow architecture for AI inference and training. The SN40L introduced a novel three-tier memory hierarchy, while the SN50 (fifth-generation) focused on agentic AI workloads.

## SambaNova RDU Architecture

### Core Design

The RDU consists of a tiled array of **Programmable Compute Units (PCUs)** and **Programmable Memory Units (PMUs)** connected by a 3D on-chip switching fabric. Unlike von Neumann architectures, the RDU is programmed spatially — different operators are mapped to different regions of the chip, forming a pipeline.

### Dataflow Principle

While computation executes for one operator, data is fetched in parallel for the next. This "assembly line" model (similar to Groq) keeps intermediate activations local, eliminating memory round-trips between operators. The key benefit: no memory bottleneck between pipeline stages.

### Three-Tier Memory System (SN40L)

1. **Tier 1:** On-chip distributed SRAM — highest bandwidth, lowest capacity (~hundreds of MB)
2. **Tier 2:** On-package HBM — medium bandwidth, medium capacity (~100s GB)
3. **Tier 3:** Off-package DDR DRAM — lowest bandwidth, highest capacity (~TBs)

This three-tier system allows SambaNova to map extremely large models (multi-TB parameter spaces) while keeping active layers in faster memory tiers.

## SN40L Specifications

- **On-chip SRAM:** Distributed across PCU/PMU tile array
- **HBM Bandwidth:** 1 TB/s
- **DDR Capacity:** Multiple TB
- **Target Workloads:** Enterprise RAG pipelines, multi-tenant inference, agentic AI

## SN50 (Fifth Generation)

- Designed specifically for large-scale, agentic workloads
- Three-tier memory retained
- Reduced data movement as key architectural goal
- Improved energy efficiency and throughput for RAG + tool-calling inference

## arXiv Paper (2405.07518) Findings

The peer-reviewed study demonstrates:
- Codesigned for enterprise inference and training simultaneously
- Three-tier memory system eliminates traditional GPU inference bottleneck for large context
- Outperforms GPU baselines on RAG workloads where DDR tier enables cost-effective KV-cache storage

## Competitive Position

- Differentiated from GPUs: specializes in large-context, multi-document enterprise inference
- Differentiated from Groq: supports training, not just inference; larger effective model capacity via DDR tier
- Differentiated from Cerebras: programmable dataflow vs. fixed-function wafer-scale SRAM

## Significance

SambaNova's three-tier memory architecture addresses the memory wall problem from a different angle than HBM-heavy designs — by accepting lower-bandwidth DDR for inactive parameters while keeping hot activations in faster tiers. This makes it economically attractive for enterprises with very large model parameter sets.
