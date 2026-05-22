# Paper 021: Photonic Neuromorphic Chips for Spiking Reinforcement Learning (Optica 2026)

**Tags:** photonic-compute  
**Date:** 2026  
**Source:** Optica Newsroom  
**URL:** https://www.optica.org/about/newsroom/news_releases/2026/photonic_chips_advance_real-time_learning_in_spiking_neural_systems/

## Summary

Optica published research on photonic chips implementing nonlinear neuromorphic behavior for spiking neural networks performing reinforcement learning in real-time. The work demonstrates photonic SNN hardware that learns online without sending gradients to a host processor, with plans for a 128-channel fully functional photonic SNN chip.

## Key Technical Aspects

- **Compute paradigm:** Spiking neural network (SNN) with reinforcement learning
- **Key advance:** Real-time online learning implemented in photonic hardware
- **Channel count (current):** Demonstrated functional prototype
- **Roadmap:** 128-channel fully functional photonic SNN chip
- **Energy target:** <1 pJ per synaptic event (MAC equivalent)

## Architecture

Photonic SNN elements:
1. **Photonic spiking neurons:** Laser-based or SOA-based nonlinear elements that fire when threshold is exceeded
2. **Synaptic weights:** Microring resonators or attenuators with tunable coupling
3. **Online learning:** Spike-timing-dependent plasticity (STDP) implemented optically
4. **Reinforcement signal:** Optical feedback modulates synaptic weights in real-time

## Advantages vs Electronic SNNs

| Feature | Electronic SNN | Photonic SNN |
|---------|---------------|-------------|
| Neuron switching speed | ~1 ns | ~10 ps (100× faster) |
| Energy/spike | ~1-10 pJ | <1 pJ (target) |
| Fan-out | Limited by RC | Optical split (low loss) |
| Communication | Electrical bus | Wavelength-routed |

## Significance

Most photonic AI work focuses on feed-forward inference. This work demonstrates on-chip learning, which is critical for:
- Edge AI devices that must adapt without cloud connectivity
- Robotic control systems needing real-time adaptation
- Neuromorphic computing applications in autonomous systems

## Limitations

- SNN accuracy on standard benchmarks (ImageNet, CIFAR) still below electronic GPUs
- Weight storage (optical memory) remains an open challenge — currently uses phase-change materials with limited write cycles
- Temperature sensitivity of ring resonator weights requires thermal control overhead
