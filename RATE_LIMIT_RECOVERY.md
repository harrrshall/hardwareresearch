# Rate Limit Recovery Protocol

This document explains how to resume the hardware research pipeline after a rate limit pause.

---

## Quick Resume Command

Open Claude Code and run:
```
/goal complete this task  hardware_research_orchestration.md
```

Then immediately paste this into the prompt:
```
Resume the hardware research from CHECKPOINT.md — check which sectors are missing research.md and run only what's needed (don't redo completed work).
```

---

## Manual Resume Steps

### 1. Check current state
```bash
for d in GPUs CPUs memory chip_fabrication AI_accelerators packaging photonics interconnects datacenter_hardware edge_AI_hardware; do
  dir="/home/cybernovas/Desktop/2026/experiments/hardware/research/$d"
  echo -n "$d: "
  [ -f "$dir/research.md" ] && echo "DONE" || echo "NEEDS WORK (papers=$(ls $dir/papers/ 2>/dev/null | wc -l), vallog=$([ -f $dir/validation_log.md ] && echo Y || echo N))"
done
```

### 2. Resume logic (what to spawn per sector)

| Condition | Action |
|-----------|--------|
| `research.md` exists and has 11 sections | Skip — already done |
| `validation_log.md` exists, no `research.md` | Spawn Writer Agent only |
| `papers/` populated, no `validation_log.md` | Spawn Validator → Writer |
| No `sources.json` | Spawn full pipeline (Collector → Analyzer → Validator → Writer) |

### 3. After all 10 sectors have research.md
Spawn Global Synthesis Agent to produce:
- `conclusion.md`
- `market_opportunities.md`
- `future_trends.md`

### 4. Quality self-check
Verify each global file cites ≥2 sectors, no uncited claims.

---

## Why This Happens

Claude Code has per-hour token budgets. Long multi-agent research runs can hit these limits. The recovery system:

1. **Saves state** to `CHECKPOINT.md` before limits hit
2. **Idempotent pipeline** — each sector checks its own completion before doing work
3. **Scheduled resumption** — the `/schedule` skill queues the next run automatically
4. **Isolation** — a failed/paused sector doesn't affect completed ones

---

## Prevention Tips

- For large multi-agent runs, use `/schedule` to break into 3-4 hour chunks
- Sectors that need only a Writer run much faster than full pipelines
- Spawn Writer-only agents first (fastest completion), full-pipeline last
- Monitor with: `ls research/*/research.md` to see completions in real time
