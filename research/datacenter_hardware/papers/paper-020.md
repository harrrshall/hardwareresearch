# Paper 020: SC25 Supercomputing Conference — AI Infrastructure Highlights (Nov 2025)

**Tags:** AI-cluster, liquid-cooling, power-delivery, rack-scale
**Source:** NAND Research, HPCwire, Data Center Knowledge, Vertiv, blog.glennklockwood.com
**Date:** November 2025 (SC25 held in St. Louis)
**Relevance:** High

## Conference Overview

SC25 (Supercomputing 2025) was held in St. Louis in November 2025. The conference shifted significantly toward AI infrastructure engineering, with power and cooling treated as primary design variables alongside compute performance.

## Key Themes from SC25

### 1. Networking Fabric as Primary Bottleneck

- **800G networks are the new planning baseline** for AI scale-out
- 102.4 Tb/s switch ASICs addressing higher radix and bandwidth requirements
- NVIDIA introduced NVQLink at SC25: enables microsecond-scale connections between GPUs and quantum processors
- NVIDIA Quantum-X photonics platform announced for future switch-to-switch optical links

### 2. Power and Cooling as Strategic Design Variables

- SC25 featured megawatt-scale CDU demonstrations
- High-voltage DC bus architectures shown as production-ready by multiple vendors
- Immersion-cooled optical interconnects demonstrated (first time at SC25 scale)
- Power and cooling now given equal floor time to compute in technical sessions

### 3. Storage for AI Workloads

- Traditional enterprise storage creates AI training pipeline bottlenecks
- DDN, VAST Data, WEKA: showing AI-native storage (metadata scalability, high-concurrency, framework integration)
- AI-specific data access patterns require purpose-built solutions

### 4. Supermicro SC25 Demonstrations

- High-performance DCBBS (Data Center Building Block Solution) architecture
- Direct liquid cooling at rack scale
- Rack-scale innovations including 250 kW CDU
- GB200 NVL72 SuperCluster live demo

### 5. Vertiv SC25 Presence

- Megawatt-class CDU demonstrations (CoolChip 2300)
- Prefabricated liquid cooling modules for rapid deployment
- Zero-water cooling technology preview

## SC25 Technical Paper Highlights

- **Sustainable Supercomputing for AI: GPU Power Capping at HPC Scale** (arxiv 2402.18593): demonstrated that GPU power capping can reduce cluster power 15–20% with <5% throughput impact for memory-bandwidth-limited workloads
- Multiple papers on network congestion control for all-reduce at 100,000+ GPU scale
- Papers on thermal modeling for heterogeneous liquid-cooled racks

## SCinet Infrastructure (SC25)

SCinet (SC's experimental network) deployed 800G optical links for the first time at SC25, providing the highest-bandwidth conference network in history at the event.

## Industry Announcements at SC25

- Supermicro: ramping full production of NVIDIA Blackwell rack-scale with HGX B200
- DDN: announcing AI storage solutions for 100 PB+ training datasets
- AMD: previewing ROCm 7.0 open-source AI software stack

## Key Observation (Glenn Klockwood SC25 Recap)

- The SC25 community is converging on the view that **network fabric** is the dominant constraint for AI scale-out, surpassing compute as the primary design challenge
- AI training at the frontier requires 10,000+ GPU jobs; HPC traditionally addressed 1,000–10,000 core jobs
- The jump in problem size creates qualitatively new engineering challenges in fault tolerance, job scheduling, and fabric congestion

## Implications

SC25 marked the point at which HPC conferences became primarily AI infrastructure conferences. The technical community consensus: 800G networks, liquid cooling, HVDC power delivery, and AI-optimized storage are the four pillars of next-generation AI infrastructure design.
