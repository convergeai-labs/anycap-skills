---
name: anycap-brand-mark-lab
description: Produce a brand mark / logo / avatar set with AnyCap — from brief through candidate generation, i2i colorway exploration, no-text gate, small-size simulation, to a decision board. Use when designing avatars, app icons, org/profile pictures, or brand-adjacent marks with AnyCap image models.
---

# AnyCap Brand Mark Lab

A repeatable pipeline for producing a production-ready brand mark with AnyCap image generation, distilled from two shipped projects (a GitHub org avatar derived from a parent brand's geometry, and a full logo redesign for a developer-tools collective).

## The pipeline

```
brief ──▶ round 1: 4–6 composition candidates ──▶ no-text vision gate
  │              │                                        │
  │              ▼                                        ▼
  │      user rejects all? ──▶ round 2: NEW concept space (don't iterate on rejected elements)
  │                                                         │
  ▼                                                         ▼
i2i colorways on the winner (one variable at a time) ◀──────┘
  │
  ▼
64/44/32px decision board ──▶ final pick ──▶ delivery prep ──▶ provenance sidecar
```

## 1. Freeze the brief

One sentence of concept, required/forbidden elements (no text, no arrows, no reuse of existing logos), palette with **exact hex stops**, background, aspect (1:1, ≥1024px), and — most important — **the surfaces where it will display**. A GitHub org avatar lives at 32–44px; that constraint should shape every decision.

## 2. Generate candidates across the concept space, not around one idea

4–6 candidates, each a **different concept** (converging arcs, constellation, squircle container, pixel art, keycap, infinity loop…), not the same idea re-seeded. Varying only the seed wastes budget on one local optimum.

**If the user rejects the whole round, do not iterate on the rejected elements.** Explicitly jump to a disjoint concept space. Real example: after a round built on code brackets / circuit nodes / tools was rejected, the winning mark came from a deliberately disjoint round (pixel-art spark). Anchor prompt: "do NOT use any elements from the previous round".

## 3. Gate every candidate with vision read

```
anycap actions image-read --file <candidate.png> \
  --instruction "Any words, letters, numbers, watermarks, pseudo-text, or UI traces
   (borders/strokes around the icon background)? Answer CLEAN or HIT - <what>."
```

- Batch up to 10 files in one call.
- **Icon-template borders count as HIT.** A faint squircle stroke around the background is a UI trace; regenerate with "no border, no outline, no stroke — just clean flat background".
- Up to 10 images per call: include the composition question too ("does it keep the N-element ring?") when fidelity matters.

## 4. Explore colorways with i2i recolor — never re-roll from text

Once a composition wins, recolor it:

```
anycap image generate --mode image-to-image --param images=<winner.png> \
  --prompt "Recolor this exact logo mark, keep the composition and shapes 100%
   unchanged: replace the gradient with <hex A> to <hex B> … No text."
```

i2i preserves composition remarkably well. Change **one variable at a time** (hue family, mono vs color, dark vs light plate). State exact hex stops — `#22D3EE → #2563EB` follows orders; "blue-ish" doesn't.

## 5. Decide at real display sizes

Build a one-page HTML board: every candidate at 64/44/32px, plus the incumbent logo for contrast. **32px is the real canvas** — a mark that only looks good at 1024px is not a logo. Watch for:

- multi-element marks fusing into mush (the reason the incumbent got replaced)
- thin vertical compositions wasting a square frame
- generic符号 (infinity loops, rockets, orbit atoms) — elegant but un-ownable; prefer marks with a unique texture (e.g. chunky pixels read crisp at any size and are instantly recognizable in a sea of flat gradients)

## 6. Delivery prep (the steps everyone forgets)

- **Transparent corners.** AI-generated "rounded-square on white" PNGs carry opaque white corners that show as an ugly plate on dark pages. Flood-fill the corner background to alpha before shipping.
- **GitHub's camo proxy caches raw image URLs.** After replacing an image in a repo, bump the README reference (`logo.png?v=2`) or the old pixels linger.
- Upload the avatar / apply the profile only as a separately authorized step — asset approval ≠ publish approval.

## 7. Keep provenance

A sidecar markdown per project: brief, references, candidate table with gate results, colorway list, final decision rationale. It makes the work reviewable, teachable, and reusable — and it is what turns a PNG into a case study.

## Anti-patterns

- Re-rolling from text when only color must change (use i2i).
- Accepting a gate "CLEAN" from a previous round for a new edit — re-run the gate on every artifact.
- Asking the model for "a logo for X" with no concept direction — you'll get the industry's average logo.
- Judging candidates at full size only.
