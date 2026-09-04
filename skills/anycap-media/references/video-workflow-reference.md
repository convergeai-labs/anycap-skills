# Video Workflow Reference

## Source Pattern

The Xiaohongshu reference and related long-form article frame AI video work as a production line, not as one generation prompt.

Useful chain:

`素材 -> 粗剪 -> 字幕 -> 包装 -> 切片 -> 发布 -> 复盘`

For AnyCap promo work, translate that into:

`reference -> storyboard -> dynamic plates -> deterministic overlays -> packaging -> QA -> delivery`

## What To Borrow From Video Practice

- Treat raw media as a timeline to inspect, cut, score, and render.
- Keep captions deterministic and readable; never trust generated video text.
- Remove dead time; every scene needs visible human/subject action.
- Build shot inventories and EDL-like scene plans before rendering.
- Make final assembly, inspection, frame extraction, codec checks, and contact sheets deterministic (e.g. via ffmpeg).
- Add packaging after the cut works: titles, labels, lower thirds, callouts, and CTA.
- Use code-driven layout for exact text and animation when repeatability matters.
- Organize scenes around product promise, proof, and CTA instead of feature dumping.
- Treat video production as a workspace with scripts, assets, sidecars, and QA logs.

## AnyCap Promo Translation

Use generated video for the moving world:

- human hand movement
- robot head or arm movement
- camera dolly/pan/pullback
- monitor state changes
- console lights and switches
- visible artifact generation or delivery

Use deterministic local rendering for exact facts:

- AnyCap logo and wordmark
- Codex / Cursor / Claude Code labels
- subtitles, CTA, website URL
- capability names
- progress bars, routing labels, output proof cards

## Player-Safe Layout

Many reviews happen in QuickTime, browser previews, or social apps with playback controls. Design for that reality.

For 1920x1080:

- Outer margin: 96px.
- Primary title region: y=88 to y=360.
- Secondary side copy: y=160 to y=700.
- Avoid region for critical text: y=780 to bottom.
- Use bottom only for non-critical ambience, background, or temporary motion.
- Do not put important chips, CTAs, or subtitles under the center playback control area.

## Motion Acceptance Gate

Before final delivery, a scene must pass this gate:

- The background video changes even when overlays are hidden.
- At least one physical subject moves in each 8-10 second beat.
- At least one product-proof element changes state in each beat.
- Contact sheet shows distinct shot progression.
- A frame-difference check or visual scrub confirms motion is not only overlay text.

If any item fails, regenerate the dynamic plate or rewrite the beat. Do not keep refining typography on a static shot.
