# AnyCap Image Workflow

Enter this workflow only after the routing layer and
[image-decision-system.md](image-decision-system.md) select an AnyCap or hybrid route. Do not use model
availability as a reason to replace a chart, Mermaid/state/sequence/DFD,
architecture decision canvas, authentic screenshot/trace, or real map.
The exception is an explicitly selected T1 validated-generated technical
candidate: it competes with, but does not replace, the reviewable T0 source.
Read `generated-technical-diagrams.md` before producing that branch.

## Check Readiness

```bash
anycap status
anycap image models
anycap image models <model> schema --mode text-to-image
```

Do not continue if `anycap status` is not `success`. A schema response can still
succeed while generation returns `AUTH_INVALID`, so status must precede schema.
Do not open an interactive login flow silently. If AnyCap is essential and the
user has not authorized browser-assisted login, ask them to complete the
documented login flow; otherwise use a semantically equivalent deterministic
route when the selected contract allows it and record the fallback. Never
replace the failed branch with an atmosphere image.

When authentication is required, use the `anycap-access` setup/auth route
(the nonblocking device flow: `anycap login --headless --no-wait --json`, open
`verification_uri`, enter `user_code`, poll, verify `anycap status`). The user
completes account selection, OTP, CAPTCHA, and consent steps. Authentication
approval does not authorize Drive/Page delivery or publication.

## Model Defaults

For model-specific strengths, cautions, aspect ratios, and bake-off rules, read
your model-selection contract. Use this section only as a short operational summary.

| Model | Use first when |
|---|---|
| `nano-banana-pro` | High-quality technical diagrams, business-facing graphics, polished Chinese infographics |
| `nano-banana-2` | Fast comparison for T1/T2 candidates, polished Chinese labels, bulk variants, storyboards |
| `gpt-image-2` | First T1 candidate for hierarchy-rich architecture/process diagrams; high-fidelity generation/editing |
| `seedream-5` | Image editing, style transfer, detail refinement, strong final/refinement candidate |
| `seedream-4.5` | Reliable image editing/transformation when `seedream-5` is not needed |
| `flux-kontext-max` | Creative/design-oriented generation and decoration-only backgrounds; never trust generated diagram geometry |
| `qwen-image` | Chinese prompt experiments only; a current single-sample test failed text and relationship QA, so never promote without an asset-level pass |

If the user explicitly names a model, use that model after checking schema and
explain any mismatch with the requested aspect/resolution/text risk. If they do
not care, use `gpt-image-2` first for a T1 hierarchy-rich technical candidate,
then `nano-banana-2` as a comparison. For T2/general exploration use
`nano-banana-2` at `1k/2k`; use `nano-banana-pro` at `2k` when its live schema
and recent evidence make it the better final-quality Chinese candidate. For
high-value visuals, run a same-prompt bake-off between the two best live
candidates and keep the selection receipt.

## Parameters

Always fetch live schema; model catalogs change.

Common params:

- `aspect_ratio`: usually `16:9` for technical slides; `3:4` or `9:16` for vertical cards; `1:1` for avatars/icons.
- `resolution`: start with `1k` for exploration; use `2k` for final if available.
  A T1 technical candidate may use `4k` when the live schema supports it and
  label density needs it, but 4K does not relax topology or text QA.
- `format`: prefer `png`.
- `images`: image-to-image references; pass local paths directly.

Schema responses can be nested. When checking params, inspect
`schemas[].schema.model_params` rather than assuming a flat JSON shape.

`aspect_ratio=16:9` is a provider composition request, not an exact pixel-size
contract. Live 1k outputs can differ by model and may be only approximately
16:9. Inspect actual dimensions; when a deck/report requires an exact canvas,
compose the accepted pixels into that canvas deterministically with an explicit
contain/crop decision instead of stretching the bitmap.

## Prompting Discipline

Use a structured prompt instead of a pile of adjectives:

```text
[Subject] + [Action/relationship] + [Context] + [Composition/layout] + [Style preset] + [Text strategy] + [Negative constraints]
```

Separate two artifacts:

1. **Decision receipt**: viewer question, source map, owner, renderer, rejected
   routes, model/schema, sensitive-data decision, and validation plan.
2. **Generation prompt**: only goal, composition, style, literal visible-text
   whitelist, required order/direction, and negative constraints.

Do not paste the receipt into the prompt. Operational fields such as owner,
renderer, layout/preset IDs, schema notes, or QA plans do not help the model
draw the asset and may leak into pixels.

Rules:

- Be specific and positive. Say what should appear, where it appears, and what it is doing.
- Control composition directly: foreground/background, left-to-right flow, camera angle, visual hierarchy, and empty zones for later overlay.
- Quote exact visible text when asking the model to render text. Keep generated labels short.
- Use reference images when style consistency matters. State the role of each reference: style reference, structure reference, edit target, or subject reference.
- Iterate one variable at a time: composition, then style, then labels/detail. Do not rewrite the whole prompt unless the direction is wrong.
- If the prompt needs exact facts or supports implementation/review evidence,
  switch to a no-text background plate or T0 deterministic rendering.
- In a T0 hybrid asset, the image model owns only non-semantic decoration.
  Containers, lanes, arrows, topology, titles, labels, and exact facts belong to
  the deterministic layer. Do not ask the model to create an "empty diagram
  skeleton" and assume later text overlay makes its geometry trustworthy.
- In a T1 validated-generated technical asset, the model may own the complete
  visible composition only after the router supplies a fact graph containing
  required nodes/edges/text, allowed display text, independent sets, and
  forbidden semantics. A candidate cannot self-certify.
- For text-heavy Chinese images, first make a visible text inventory. If the
  inventory is too long, route away from generated text before spending a run.
- Do not put prompt scaffolding in the visible text inventory. Words like
  `16:9`, `L9`, production/style IDs, and layout names are instructions, not
  output text.
- Give each region a non-overlapping role. When a left/right layout is used,
  explicitly say what is allowed in each region and that lists must not repeat.
- For edits, explicitly say what changes and what must stay unchanged. Repeat
  invariants such as identity, layout, lighting, camera, labels, and arrow direction.

## Style And Resolution Flow

1. Confirm the route is R1/R2 or an eligible T1 branch, then pick the independent
   style family from your style preset. Do not send R0/R3 work to a model because
   of style.
2. Generate a `1k` draft to validate composition and style.
3. If the draft is right, regenerate or refine at `2k` for final when available.
4. Use `4k` for short/no-text prompts, large visual plates, or a T1 candidate
   whose live schema supports it; inspect actual pixels in every case.
5. For Chinese text, accept the result only after visual inspection and image-read QA. If the text is unstable, keep the image as a no-text plate and overlay text deterministically.
6. If a final bitmap must sit beside old `2752x1536` assets, render the final at
   native target size when possible rather than stretching a smaller output.
7. If the asset matters and exact text is not the blocker, run a 2-3 model
   bake-off rather than spending all iterations on one weak model.

## Output Discipline

Use `-o` with an absolute path:

```bash
anycap image generate \
  --model nano-banana-pro \
  --prompt "$PROMPT" \
  --param aspect_ratio=16:9 \
  --param resolution=1k \
  --param format=png \
  -o /absolute/project/path/name.png
```

Parse only safe fields in chat summaries: `status`, `local_path`, `model`, `request_id`. Do not expose credentials. Avoid reporting billing/cost fields unless the user explicitly asks.

After generation, verify the actual file type with `file`. Some model/provider
paths may return JPEG bytes even when `format=png` and the filename ends in
`.png`. Convert/re-export or rename before embedding in HTML, reports, or upload
flows that depend on MIME correctness.

## QA With Image Read

For text-bearing generated diagrams, run a second-pass read before final delivery:

```bash
anycap actions image-read \
  --file /absolute/project/path/name.png \
  --instruction '请用中文简短检查这张图:列出能读到的主要文字,指出是否有错字、乱码、额外不相关文字、重复标签、箭头方向或布局问题。'
```

Use the result as evidence, not as the only check. Still inspect the image yourself. If the read flags duplicate labels, extra micro-text, or confusing direction, record it in the sidecar and regenerate or switch to deterministic rendering.

For no-text plates, change the instruction:

```bash
anycap actions image-read \
  --file /absolute/project/path/name.png \
  --instruction '请检查这张图是否存在任何可读文字、字母、数字、符号、伪代码、UI 标签、logo 或水印;如果有,逐项指出位置。'
```

No-text is a fail-closed contract. Reject the candidate if image-read or visual
inspection finds a watermark, copyright mark, pseudo-text, UI trace, tiny
alignment glyph, generated box/arrow that could be mistaken for information, or
another typographic artifact.

For text-bearing diagrams, pass the literal source contract or T1 fact graph to
image-read and require a binary result:

```bash
anycap actions image-read \
  --file /absolute/project/path/name.png \
  --instruction 'required_text:[...];allowed_display_text:[...];required_nodes:[...];required_edges:[A→B(type),...];independent_sets:[[...]];forbidden_semantics:[...]。列出实际全部文字、节点和关系;检查独立项是否被画成顺序;任一缺失、额外、重复、错连或禁义都判 FAIL。'
```

One passing sample does not make a model generally safe. Acceptance is
per-asset. If a candidate fails visible text or relationship QA, switch model or
route; do not repair a structurally wrong bitmap by merely covering one label.
Manual inspection may overturn an image-read false positive, but the sidecar
must record the disputed finding and visual evidence. Image-read may never
overturn a visible critical mismatch.

## Sidecar Template

Create `<asset-basename>.prompt.md` next to every generated asset:

```markdown
# <Asset Title>

- Date: YYYY-MM-DD
- Model: `<model>`
- Mode: `<text-to-image | image-to-image>`
- Output: `/absolute/path/to/output.png`
- Request ID: `<request_id>`
- Style preset:
- Route:
- Assurance class: `<T0 | T1 | T2>`
- Viewer question:
- Takeaway:
- Information increment beyond nearby prose:
- Decision/inference enabled:
- Relationship grammar:
- Visual family:
- Owner skill:
- Renderer:
- Rejected route alternatives:
- Paired visual set, if any:
- Reading order:

## Source Map

- `<visual node/label/relationship>` -> `<source path/section/data/evidence>`

## Fact Graph (required for T1)

- Required text:
- Allowed display text:
- Required nodes:
- Required edges:
- Independent sets:
- Forbidden semantics:

## Command

```bash
<exact command>
```

## Prompt

<final prompt>

## Validation

- File type:
- Dimensions:
- Visual inspection:
- Image-read QA:
- Fact-graph diff:
- Semantic contract QA:
- Text/number accuracy:
- Sensitive-info redaction:
- Rights/commercial review:

## Known Issues

- ...

## Rejected Directions

- ...

## Next Edit Prompt

...
```
