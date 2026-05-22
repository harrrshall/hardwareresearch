# paper-020: AxLLM — Computation Reuse for LLM Acceleration (arXiv 2509.22512)

**Tags:** transformer-accelerator, LLM-inference  
**Date:** September 2025  
**Source:** arXiv cs.AR  
**URL:** https://arxiv.org/abs/2509.22512

---

## Summary

AxLLM proposes an accelerator architecture for LLMs that exploits **computation reuse** — recognizing that similar token embeddings in long contexts produce similar intermediate activations that need not be recomputed from scratch. It achieves 90% reduction in computations with 28% lower energy and 1.7x speedup.

## Core Insight: Redundancy in LLM Computation

In long-context inference, the same or similar content frequently recurs across sequences, batches, and sessions:
- Shared system prompts processed multiple times
- Similar document embeddings in RAG pipelines
- Repeated instruction formats in agent loops

Traditional hardware recomputes everything from scratch. AxLLM caches and reuses matching intermediate computations.

## Architecture Design

### Computation Reuse Unit (CRU)
- Content-addressable memory storing intermediate layer activations indexed by input hash
- On lookup hit: skip computation, return cached result
- On miss: compute normally, store result for future reuse

### Hardware Integration
- CRU sits between attention heads and FFN layers
- Hash comparison hardware enables O(1) lookup in activation cache
- Cache management policy: LRU eviction with frequency weighting

### Reuse Granularity
- Per-token reuse: individual token embedding matches
- Per-chunk reuse: consecutive token spans with identical content
- Per-layer reuse: full layer output reuse when input matches

## Performance Results

| Metric | Improvement |
|--------|-------------|
| Computation reduction | up to 90% |
| Energy reduction | 28% |
| Speedup vs baseline | 1.7x |
| Accuracy impact | Negligible |

## Workload Suitability

Best suited for:
- Long-context inference with repeated content (document QA)
- Agent loops with fixed system prompts
- Batched inference with shared prefixes
- RAG with frequently retrieved chunks

Less suited for:
- Single-query inference with unique content
- Creative generation with no repetition
- Short contexts where reuse overhead exceeds benefit

## Relationship to KV-Cache

Traditional KV-cache stores attention keys/values per sequence. AxLLM's CRU stores **activation outputs** per content hash:
- KV-cache: sequence-specific, not reusable across different sequences
- CRU: content-specific, reusable across any sequence containing same content
- Complementary: AxLLM + KV-cache provide orthogonal speedups

## Implementation on Hardware

The paper evaluates AxLLM as an ASIC:
- SRAM-based CRU embedded in accelerator die
- Hash comparison in sub-nanosecond using TCAM-like structure
- Area overhead: ~5% of total die area for 10x capacity benefit

## Significance

Computation reuse addresses a different axis of LLM efficiency: instead of making each FLOP faster, it reduces the total number of FLOPs required. The 1.7x speedup and 28% energy reduction at 90% computation reduction is a significant finding that suggests production LLM serving wastes substantial compute on redundant calculations — an insight that should influence next-generation accelerator design.
