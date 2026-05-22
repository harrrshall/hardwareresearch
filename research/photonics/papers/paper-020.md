# Paper 020: LPO Specification — Linear Pluggable Optics 100G/Lane Standard

**Tags:** optical-interconnect  
**Date:** 2025  
**Source:** LPO MSA / NewPhotonics / Connector Supplier  
**URL:** https://newphotonics.com/lpo-msa-membership-group-releases-linear-pluggable-optics-lpo-specification/

## Summary

The Linear Pluggable Optics Multi-Source Agreement (LPO MSA) Group released the 100G/lane LPO specification, standardizing a DSP-less optical transceiver architecture that halves power consumption vs traditional DSP-based modules. LPO moves signal processing to the host ASIC, eliminating the DSP chip inside the module.

## Specification Details

- **Lane rate:** 100 Gb/s (initial spec); roadmap to higher rates
- **Target:** 800G Ethernet connectivity (8 × 100G)
- **Form factors:** QSFP, QSFP-DD, OSFP (form factor agnostic spec)
- **Fiber type:** Single-mode fiber (SMF compatible)
- **Key elimination:** DSP chip inside the module

## Power Comparison

| Module Type | Power at 800G | DSP? |
|-------------|--------------|------|
| Traditional 800G (DSP) | >16 W | Yes |
| 800G LPO | <8.5 W | No |
| CPO 800G equiv. | ~4-5 W | No |

## Architecture

Traditional pluggable:
```
Host SERDES → DSP → EML Driver → EML Laser → Fiber
```

LPO:
```
Host SERDES (with EQ) → Linear Driver (TIA/Driver) → EML Laser → Fiber
```

LPO replaces DSP with:
- High-linearity Transimpedance Amplifier (TIA)
- Linear driver with equalization
- Signal processing pushed to host device's advanced CMOS (e.g., 5nm ASIC)

## Deployments (2025-2026)

- Arista Networks: LPO in AI cluster ToR switches
- Cisco: LPO-compatible transceivers in data center line
- Juniper: Router-based optics using LPO architecture
- Leading hyperscalers: Specifying LPO for new AI fabric pods

## LPO vs CPO Tradeoffs

| Feature | LPO | CPO |
|---------|-----|-----|
| Power | ~8.5W/800G | ~4-5W/800G |
| Upgrade | Hot-swap | Requires board change |
| Cost | Lower (near-term) | Lower (long-term) |
| Integration | Pluggable | On-package |
| Volume | Available now | 2026+ |

## Significance

LPO bridges the gap between today's high-power DSP pluggables and tomorrow's CPO. For existing data centers that cannot change switch ASICs, LPO provides an immediate 50% power savings path with zero changes to fiber plant or switch chassis.
