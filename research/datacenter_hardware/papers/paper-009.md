# Paper 009: AWS Project Rainier — UltraCluster AI Infrastructure (Oct 2025)

**Tags:** AI-cluster, rack-scale, hyperscale, power-delivery
**Source:** Amazon/AWS press releases, Data Center Frontier, The Register
**Date:** October 29, 2025 (activation date)
**Relevance:** High

## Overview

AWS activated Project Rainier on October 29, 2025 — one of the world's largest AI compute clusters. The system is built on custom Trainium2 silicon, representing Amazon's largest bet on vertically integrated AI infrastructure.

## Hardware Architecture

### UltraServer Unit
- 1 UltraServer = 4 physical Trainium2 servers × 16 Trainium2 chips = 64 chips per UltraServer
- Intra-UltraServer connectivity: NeuronLinks (high-bandwidth custom interconnect, distinctive blue cables)
- Inter-UltraServer connectivity: Elastic Fabric Adapter (EFA) networking (yellow cables)
- EFA connects UltraServers both within and across data centers

### Cluster Scale
- Project Rainier: nearly 500,000 Trainium2 chips at activation
- Target: >1 million Trainium2 chips by end-2025 (Anthropic expansion)
- Amazon EKS now supports clusters of up to 100,000 nodes for AI/ML workloads (announced separately)

## EC2 UltraCluster 2.0 Architecture

- UltraCluster 2.0 provides the backbone network fabric
- Sub-microsecond latency between nodes within a cluster
- Designed for scale-out training at 100,000+ chip scale
- EFA fabric provides 400 Gb/s per node network bandwidth

## Trainium2 Chip

- Custom-designed silicon (not GPU)
- 16 chips per physical server
- Interconnected via NeuronLinks within UltraServer
- Software stack: AWS Neuron SDK (compatible with PyTorch, JAX)
- Power: not publicly disclosed; estimated 250–350 W per chip

## Customer Use Case

- Anthropic: primary initial customer; uses Rainier for training and deploying Claude models
- Planned to expand to 1M+ chips by end-2025

## Strategic Significance

Project Rainier demonstrates AWS's long-term strategy of deep vertical integration:
1. Reduces dependence on NVIDIA GPUs for training workloads
2. Scales custom silicon to hyperscale without external GPU supply chain constraints
3. Custom interconnect (NeuronLink) enables UltraServer-level bandwidth without NVLink licensing
4. Enables lower per-token training cost for LLM customers

## Infrastructure Footprint

- Multiple data centers connected via EFA
- Physical footprint not disclosed; estimated at 50–100 MW across sites
- Cooling: traditional high-density liquid-cooled design, consistent with AWS standard hyperscale practices
