# Conditional media and page integration

### 1. Match the evidence type to the page's claim

- **Show the final outcome**: generate one polished hero or showcase image.
- **Show a transformation**: generate a rough source image, then a refined after-image from the same subject.
- **Show range or iteration**: generate a triptych or clean review board with multiple variations.
- **Support a time-based workflow**: generate a companion still or keyframe that represents the brief. Do not present a static image as the full video result.
- **Support an audio-based workflow**: generate a mood image or cover visual that supports the prompt. Do not imply the image is audio output.
- **Support an explanation**: start at `image-gen` so the viewer question
  selects a visual family. Exact system structure starts at
  `image-gen-system`; exact values start at `chart-gen`; evidence and maps keep
  their truth owners. Use `anycap-media` only for a selected AnyCap
  T1/T2 branch. Do not turn every explanation into a generated flow.

If the article already lands without media, do not force a proof block. This skill is for useful proof, not decorative filler.

### 2. Discover real model constraints before prompting

If the article needs media, inspect the live model catalog and schema first:

```bash
anycap image models
anycap image models <model> schema --operation generate --mode <mode>

anycap video models
anycap video models <model> schema --operation generate --mode <mode>

anycap music models
anycap music models <model> schema --operation generate
```

Never assume mode names, parameter names, or supported aspect ratios.

### 3. Generate assets into a reusable public path

Use descriptive filenames and keep related artifacts together:

```bash
mkdir -p <site-public-dir>/content-evidence

anycap image generate \
  --model <model> \
  --prompt "<brief from the semantic owner, or an explicitly requested hero/background brief>" \
  --param aspect_ratio=16:9 \
  -o web/public/content-evidence/<page-slug>-hero.png
```

Rules:
- Always use `-o` with a descriptive filename.
- Prefer `16:9` for hero or showcase blocks unless the layout needs another ratio.
- Version or split files clearly for before/after workflows.
- Keep assets topic-specific at generation time, but keep the skill itself topic-agnostic.
- If the page is localized through wrapper files, keep assets shared unless a locale-specific image is genuinely needed.

### 4. Verify the generated asset before wiring it into the page

Use AnyCap vision to validate the artifact:

```bash
anycap actions image-read \
  --file web/public/content-evidence/<page-slug>-hero.png \
  --instruction "Describe this image, confirm it matches the intended page claim, list visible labels and relationships, and flag an atmosphere-only result unless the brief explicitly requested a hero/background. Also flag any watermark, copyright mark, pseudo-text, or UI trace."
```

For edit workflows, compare source and revision:

```bash
anycap actions image-read \
  --file web/public/content-evidence/<page-slug>-before.png \
  --file web/public/content-evidence/<page-slug>-after.png \
  --instruction "Confirm whether the second preserves the same subject while improving composition and background cleanliness."
```

If verification reveals visible text, stray signage, wrong subject identity, or prompt drift, re-prompt and regenerate before editing code.

### 5. Optimize the asset and wire it into reusable code

- Compress oversized PNGs to JPG or WebP when the visual difference is acceptable.
- Prefer a reusable component plus a lookup table over duplicating large JSX blocks in every page.
- Keep captions factual:
  - static images can say the image was generated through AnyCap for the page
  - time-based or audio-based pages should explicitly label the visual as a companion still or cover visual
- If localized routes simply re-export the base page, edit the base page once instead of patching every localized copy.
- Keep the reusable block generic enough that it can be dropped into articles, guides, or landing pages without rewriting the component itself.

### 6. Verify the page integration

Run targeted checks on the files you touched:

Run the site's normal lint/typecheck on the files you changed.

If a full repo-wide typecheck fails because of pre-existing issues, record the exact blocking file and keep the skill output focused on what was actually validated.
