# anycap-skills

Claude Code skills for [AnyCap](https://anycap.ai) — the agent capability runtime. Personal projects by [@kevinten10](https://github.com/kevinten10), part of [convergeai-labs](https://github.com/convergeai-labs).

Each skill is a self-contained package under `skills/<name>/` — install one, ignore the rest.

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

## Install

Copy a skill directory into `~/.claude/skills/`, or symlink it:

```bash
ln -s "$PWD/skills/anycap-brand-mark-lab" ~/.claude/skills/anycap-brand-mark-lab
```

## Related

- Works produced with these skills: [anycap-examples](https://github.com/convergeai-labs/anycap-examples)
