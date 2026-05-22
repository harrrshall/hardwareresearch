# Paper 003: NVIDIA GB200 NVL72 Rack-Scale System — Technical Deep Dive

**Tags:** rack-scale, liquid-cooling, AI-cluster, power-delivery
**Source:** NVIDIA official documentation, Supermicro datasheet, Tone Cooling, Sunbird DCIM
**Date:** 2025–2026
**Relevance:** High

## System Configuration

The GB200 NVL72 is NVIDIA's flagship rack-scale AI compute product for the Blackwell generation:

- **Rack contents:** 18x 1RU compute trays, each with 2 Grace CPUs + 4 Blackwell B200 GPUs
- **Total:** 36 Grace ARM CPUs + 72 Blackwell GPUs in a single 48U rack
- **Memory:** 13.4 TB unified GPU memory (HBM3e); 72 × 192 GB per GPU
- **NVLink domain:** Largest ever offered — 72 GPUs interconnected
- **Aggregate NVLink bandwidth:** 130 TB/s GPU-to-GPU

## Compute Performance

- **FP4 peak:** 1.44 ExaFLOPS
- **FP8 training:** ~720 PFLOPS
- **NVSwitch fabric:** 14.4 TB/s non-blocking switching capacity per switch (3 NVSwitches per rack)
- **NVLink 5 per GPU:** 1.8 TB/s bidirectional

## Power Specifications

- **Total rack TDP:** 120 kW (sustained); some OEM configs reach 132 kW
- **Input voltage:** 200–480V AC or 240–400V DC
- **Per-GPU TDP:** ~1,200 W (B200 GPU alone)
- **Per-CPU TDP:** ~500 W (Grace CPU)

## Physical Dimensions

- **Dimensions:** 600 mm (W) × 1,068 mm (D) × 2,236 mm (H)
- **Weight:** 1.36 metric tons (3,000 lbs)
- **Rack height:** 48U

## Liquid Cooling Architecture

- Fully liquid-cooled (no air cooling of compute elements)
- Cold plates on each GPU and CPU die surface
- Coolant runs vertically through integrated manifolds in rack
- **CDU requirement:** 150–200 kW facility-rated CDU
- **Coolant supply temperature:** 25–45°C depending on configuration
- **Facility interface:** Chilled water supply + return, typical supply at 18–22°C
- Vertiv holds ~70% volume share for CDUs shipped with first GB200 NVL72 racks

## Networking

- Rack-integrated NDR InfiniBand (NVIDIA Quantum-2) or Spectrum-X 400G/800G Ethernet
- Per-node dual-port 400G NDR InfiniBand (ConnectX-7 or ConnectX-8)

## Deployment Considerations

- Floor loading: requires structural assessment (1.36 metric tons concentrated load)
- Chilled water infrastructure: mandatory — cannot deploy with air cooling
- Power delivery: requires 3-phase high-voltage feed; 120 kW per rack at 400A+
- Service aisle: CDU + manifold connections require rear access clearance

## Market Impact

- Cost per rack: approximately $3.9M average (2025) vs $500K for traditional rack
- Standard becomes a 132 kW deployment; facility operators must plan for 150 kW per rack slot to include cooling overhead
