---
name: anycap-brand-mark-lab
description: Produce a brand mark / logo / avatar set with AnyCap — from brief through candidate generation, i2i colorway exploration, no-text gate, small-size simulation, to a decision board. Use when designing avatars, app icons, org/profile pictures, or brand-adjacent marks with AnyCap image models.
---

# AnyCap Brand Mark Lab

A repeatable pipeline for producing a production-ready brand mark with AnyCap image generation. Distilled from a real project (a GitHub org avatar derived from a parent brand's geometry).

## Pipeline

1. **Freeze the brief**: concept (one sentence), required/forbidden elements (no text, no arrows, no reuse of existing logos), palette, background, aspect (1:1, ≥1024px), and the surfaces where it will display (e.g. 32–44px avatars).
2. **Collect brand references**: parent logo, product family marks. Write down the family DNA in one line (e.g. "geometric abstract mark + one hue per brand + dark plates"). References guide i2i — never copy them.
3. **Generate 4–6 composition candidates** with distinct concepts (radial convergence, orbit, squircle container, aperture, ripple...). Vary the concept, not just the seed.
4. **Gate every candidate** with `anycap actions image-read`: ask explicitly for words, letters, numbers, watermarks, pseudo-text, and **UI traces** (icon template borders/strokes count as HIT — regenerate without them).
5. **Explore colorways via i2i recolor** on the winning composition: "keep the composition and shapes 100% unchanged, replace the gradient with …". One variable at a time.
6. **Simulate real display sizes** (64/44/32px) side by side in a simple HTML decision board; a mark that reads at 32px wins over a mark that only looks good at 1024px.
7. **Keep provenance**: a sidecar markdown with brief, references, candidate table, gate results, and the final decision rationale.

## Practical notes

- i2i recolor preserves composition remarkably well — use it instead of regenerating from text when only color must change.
- State the exact hex stops in prompts (`#22D3EE → #2563EB`); models follow named hex anchors far better than "blue-ish".
- For dark-mode marks, always also check how the mark sits on GitHub/app light surfaces (or produce a light-mode twin).
- Count the source mark's elements before prompting ("keep the N-ellipse ring") — and re-count in the output; the vision gate catches drift.

## Delivery

Local files by default. Uploading to any remote surface (GitHub org avatar, profile settings) is a separate, explicitly authorized step — never implied by asset approval.
