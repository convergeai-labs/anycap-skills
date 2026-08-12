# anycap-skills

Claude Code skills for [AnyCap](https://anycap.ai) — the agent capability runtime. Personal projects by [@kevinten10](https://github.com/kevinten10), part of [convergeai-labs](https://github.com/convergeai-labs).

[中文版本 → README.md](README.md)

Each skill is a self-contained package under `skills/<name>/` — install one, ignore the rest.

<p align="center">
  <img src="assets/pipeline.png" width="640" alt="pipeline from rough sketches to a polished logo">
</p>

## Skills

### 🎨 [anycap-brand-mark-lab](skills/anycap-brand-mark-lab/SKILL.md)

Produce a brand mark / avatar that survives real-world display — from brief to decision board:

```
brief ──▶ 4–6 composition candidates ──▶ no-text vision gate
   │              │
   │              └─ rejected? ──▶ NEW concept space (never iterate on rejected elements)
   ▼
i2i colorways (one variable at a time)
   ▼
64/44/32px decision board ──▶ final pick ──▶ delivery prep ──▶ provenance
```

Hard-won lessons baked in:

- **i2i recolor preserves composition** — never regenerate from text when only color must change
- **hex anchors beat adjectives** — `#22D3EE → #2563EB` follows orders; "blue-ish" doesn't
- **rejected round? change the concept space**, not the seed
- **icon-template borders are gate failures** — a faint squircle stroke is a UI trace, regenerate
- **32px is the real canvas** — a mark that only looks good at 1024px is not a logo
- **white corners ship by accident** — flood-fill them to alpha before publishing
- **GitHub camo caches images** — bump `?v=` after replacing a README asset

Battle-tested on two shipped marks: the [convergeai-labs rainbow ring](https://github.com/convergeai-labs/anycap-examples/tree/main/entries/2026-08-convergeai-labs-avatar) and the [kt-aicoding pixel spark](https://github.com/convergeai-labs/anycap-examples/tree/main/entries/2026-08-kt-aicoding-pixel-spark).

### 🏗 [anycap-architecture-diagrams](skills/anycap-architecture-diagrams/SKILL.md)

Architecture / system diagrams with AnyCap — fact-graph-first prompting with a public-safety pass:

```
sanitize the fact graph (internal names → public roles)
   ▼
freeze the contract (nodes / edges / exact label whitelist)
   ▼
branch: T1 full-generated / hybrid (no-text plate + deterministic labels) / deterministic retreat
   ▼
generate (fact graph in the prompt) ──▶ image-read label audit (not vibes)
   ▼
provenance
```

Core discipline: sanitize before generating (a diagram is a condensed system map), audit labels verbatim, one failure → regenerate naming it, two failures → switch branch, and use synthetic reference systems for teaching figures.

Proof: the [RAG reference architecture](https://github.com/convergeai-labs/anycap-examples/tree/main/entries/2026-08-rag-reference-architecture) passed audit on the first candidate.

## Install

Copy a skill directory into `~/.claude/skills/`, or symlink it:

```bash
ln -s "$PWD/skills/anycap-brand-mark-lab" ~/.claude/skills/anycap-brand-mark-lab
```

## Related

- Works produced with these skills: [anycap-examples](https://github.com/convergeai-labs/anycap-examples)
