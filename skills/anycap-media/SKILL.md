---
name: anycap-media
description: "Produce explicit AnyCap media: photos, product shots, brand marks, decorative images, image edits, non-software video, music/audio/speech, campaign and social/UGC films, memes with deterministic captions, and eligible AnyCap T1/T2 technical visuals selected by image-gen/image-gen-system or explicitly requested. Not for generic visual-family routing, exact charts/maps/evidence, software technical video, research, or publication."
---

# AnyCap Media

Own explicit AnyCap production after the medium or delegated technical branch is
clear. Keep detailed variants behind one-level references so only the selected
workflow enters context.

## Route one production job

| Need | Read |
| --- | --- |
| photo, product shot, hero, image edit | [image-production.md](references/image-production.md) |
| logo, avatar, app icon, small-size brand mark | [brand-mark-production.md](references/brand-mark-production.md) |
| text/image-to-video | [video-production.md](references/video-production.md) |
| narrow Gemini Omni video edit | [gemini-omni-video-edit.md](references/gemini-omni-video-edit.md) |
| music, speech, dialogue, audio scene | [audio-production.md](references/audio-production.md) |
| brand/launch film or hero loop | [style-reference.md](references/style-reference.md), [storyboard-template.md](references/storyboard-template.md), and [video-workflow-reference.md](references/video-workflow-reference.md) |
| reference-led social, UGC, repair, transformation, one-take promo | [social-video-production.md](references/social-video-production.md) |
| meme, reaction visual, exact caption | [meme-workflows.md](references/meme-workflows.md) |
| delegated or explicit AnyCap T1/T2 technical visual | [image-skill-ownership-map.md](references/image-skill-ownership-map.md), [image-decision-system.md](references/image-decision-system.md), and [anycap-image-workflow.md](references/anycap-image-workflow.md) |

For a technical branch, add only the relevant specialist reference:

- hybrid T1 explanation: [generated-technical-diagrams.md](references/generated-technical-diagrams.md)
- complete short-label Chinese candidate: [nano-banana-technical-diagrams.md](references/nano-banana-technical-diagrams.md)
- report visual redesign: [report-visual-redesign-workflow.md](references/report-visual-redesign-workflow.md)
- coordinated architecture set: [architecture-report-diagram-playbook.md](references/architecture-report-diagram-playbook.md)

## Semantic boundary

- Use this Skill only when AnyCap is explicit or an upstream semantic owner
  delegated an eligible branch. Ordinary bitmap work belongs to `imagegen`.
- Generic `配图` begins at `image-gen`; architecture/process/state/decision at
  `image-gen-system`; exact numeric charts at `chart-gen`; real maps at their
  map owner; software architecture/request/state/incident/release video at
  `video-gen`.
- Annotation or narrated/spatial human feedback routes to
  `anycap-human-interaction`. Use `anycap-access` only for setup/auth/schema or
  low-level command failure.
- When auth is required, delegate to
  `anycap-access` and reuse the current controlled Chrome Google session under
  its standing AnyCap-login authorization. Authentication does not authorize
  Drive/Page delivery or publication.

## Shared production workflow

1. Freeze asset role, consumer surface, subject/fact graph, composition, aspect,
   required/forbidden text, protected regions, references, rights, and
   acceptance checks.
2. Discover the selected live model/mode schema. Do not load a stale catalog or
   spend on unapproved variants/fallbacks.
3. Generate to descriptive local paths. Keep exact logo, UI, URLs, labels,
   captions, connectors, and truth-bearing geometry deterministic unless the
   T1 contract explicitly permits audited generated text.
4. Inspect the artifact at original and consumer size. Verify type,
   dimensions/duration, identity, composition, text/data, relationships,
   watermarks, sensitive content, motion/audio, and reference fidelity.
5. Fix concrete failures. A transport/download failure does not authorize a
   different paid model. Preserve prompt/provenance sidecars when exactness,
   delegation, rejection history, or reproducibility requires them.

For the compatibility Mermaid renderer and boundary tests, use the scripts in
`scripts/`; new exact system visuals remain owned by `image-gen-system`.

## Delivery

Local files are the default. Drive/Page upload/share, publication, account/logo
replacement, or another remote delivery runs only when the current user
authorizes the exact operation, destination, environment, and audience.
Production approval is not publication approval. When delegated, return asset
paths, editable source/spec, dimensions, validation, limitations, and
`return_to` to the semantic owner.
