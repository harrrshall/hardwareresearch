# Paper 016: AMD Instinct MI350 Series — Alternative GPU Ecosystem for AI Data Centers (2025)

**Tags:** AI-cluster, rack-scale, thermal-management
**Source:** AMD official blog, Data Center Dynamics, ServeTheHome
**Date:** June 2025 launch
**Relevance:** High

## MI350 Series Overview

AMD launched the Instinct MI350 series (MI350X, MI355X) at the "Advancing AI 2025" event in June 2025. Built on the new AMD CDNA 4 architecture and TSMC 3nm process.

## Key Specifications

| Parameter | MI350X | MI300X (prev gen) |
|-----------|--------|-------------------|
| Process | TSMC 3nm | TSMC 5nm |
| HBM Memory | 288 GB HBM3E | 192 GB HBM3 |
| Architecture | CDNA 4 | CDNA 3 |
| AI Inference perf | 35× vs MI300 | baseline |
| AI compute (gen-gen) | 3.9× | — |
| FP4/FP6 support | Yes | No |
| ROCm version | 7.0 | 6.x |

## Performance Claims

- 35× improvement in AI inference performance vs MI300 series (AMD claim)
- 3.9× generation-on-generation AI compute increase
- FP4 and FP6 datatypes: new low-precision formats matching NVIDIA's FP4 in Blackwell

## Physical Format

- Same Universal Baseboard server design as MI300 series
- Drop-in upgrade path for existing MI300X deployments
- Same physical dimensions and thermal interface

## Enterprise Adoption

- Microsoft Azure: deployed MI300X; MI350X in roadmap
- Meta: using MI300X for specific inference workloads
- Dell Technologies, HPE, Lenovo: server systems available
- Oracle Cloud Infrastructure: first to adopt AMD open rack-scale AI infrastructure with MI355X GPUs
  - Oracle announced Zettascale AMD clusters with up to 131,072 MI355X GPUs

## ROCm 7.0 Software

- Built from ground up for MI350 series
- Full support for PyTorch, JAX, TensorFlow, vLLM
- Improved compiler optimization for CDNA 4 architecture

## Power Envelope

- TDP: not officially disclosed for MI350X; estimated 750–900 W based on CDNA 4 design
- Requires liquid cooling for sustained operation at peak TDP
- CDU requirements similar to H100/H200 deployments

## Strategic Context

AMD is committing to annual cadence GPU releases (announced at same event). The MI350 reduces the performance gap with NVIDIA B200 to approximately 1.5–2× at competitive price points. Oracle's commitment to 131,072 MI355X GPU clusters validates AMD as a credible large-scale alternative.

## Implications for Infrastructure

AMD's Universal Baseboard compatibility means existing MI300X racks can be upgraded to MI350X without facility changes. This creates a meaningful upgrade path for the installed base of ~$5 billion of MI300X deployments globally. The 3nm migration reduces per-GPU power vs equivalent performance, slightly improving rack PUE.
