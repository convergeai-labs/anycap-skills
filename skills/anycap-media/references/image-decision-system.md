# Image Decision System

As of 2026-07-21. Use this before any image, diagram, report visual, cover,
video still, or generated visual package for the user.

The goal is to stop treating image generation as a prompt-writing task. It is a
production decision system:

```text
intent default -> delivery surface -> truth risk -> viewer question/claim
-> information increment -> relationship grammar/visual family
-> owner skill/renderer -> model strategy when needed -> QA/sidecar
```

## Nine Gates

| Gate | Question | Decision |
|---|---|---|
| G0 Intent default | Did the user explicitly ask for atmosphere/background/hero/no-text, or only say `配图` / `image 配图`? | Generic `配图` means an information-bearing visual with final visible text and structure. Atmosphere-only output is opt-in. |
| G1 Delivery surface | Where will this visual be consumed? HTML report, PPT/deck, social image, cover, video still, appendix, evidence pack? | The surface sets aspect ratio, fixed vs responsive canvas, density, caption needs, screenshot QA, and sidecar location. For Mermaid deck/report PNGs, use the D1 wrapper's exact `--canvas`; viewport size alone is insufficient. |
| G2 Truth risk | Does the visual carry exact numbers, API names, hashes, dates, table cells, provider icons, private IDs, screenshots, or audit/release evidence? | Exact or sensitive content routes to deterministic rendering, screenshot callout, or no-text plate plus deterministic overlay. Low-risk explanatory topology may continue to the generated-technical `T1` gate. |
| G3 Visual claim | What one claim must the viewer understand? | If no one-sentence claim exists, rewrite/split before making the visual. |
| G4 Information increment | What relationship, contrast, mechanism, boundary, evidence, or decision does the image add beyond nearby prose? | If the answer is "none", omit the image. Do not invent filler nodes to satisfy a visual quota. |
| G5 Relationship grammar | Is the source primarily about structure/boundary, interaction/time, lifecycle, data/trust, comparison/decision, causality, evidence, quantity, work flow, user journey, or geography? | Choose the family from context; do not default to architecture or flow. |
| G6 Visual contract | Which structure proves the claim and information increment? | Choose the minimum sufficient contract: C4/boundary, sequence, state, DFD/lineage, decision canvas, timeline/swimlane, causal graph, trace/evidence, value stream, journey, chart, map, or concept plate. |
| G7 Owner and production route | Which specialist skill and renderer own the result? | Route to chart, Mermaid, architecture decision canvas, browser/trace evidence, map, HTML/SVG, Remotion, AnyCap/hybrid, or annotation. Do not let a tool named by habit bypass this gate. |
| G8 Model and QA | If generation is still useful, which model candidates and validation checks are needed? | Schema check, bake-off when valuable, image-read/video-read, deterministic source check, visual inspection, semantic-value check, HTML/PPT screenshots, sidecar/provenance. |

## Route Ladder

Use the first matching route:

Generic `配图` requests must finish on routes 1-6 as a complete information
artifact. A no-text plate may appear inside route 5, but it is not the final
deliverable unless the user explicitly requested a background or no-text asset.

1. **Evidence route**: screenshots, logs, terminal output, browser captures, or
   exact evidence with deterministic callouts. Generated images cannot prove
   that something happened.
2. **Quantitative route**: exact magnitude, trend, ranking, distribution,
   conversion, or correlation goes to `chart-guide` plus a deterministic chart
   or table. `image` in the request does not change this.
3. **Deterministic diagram route**: architecture review, C4 source of truth,
   sequence, ER, state, requirement, timeline, event model, Gantt, exact/high-
   consequence topology, causal DAG, decision matrix, long labels, and provider-
   specific iconography. Use Mermaid, technical/architecture canvases, SVG,
   HTML, or another reviewable source.
4. **Specialist route**: real maps use `amap-real-map-image`; real UI/live proof
   uses browser capture and callouts; animated software diagrams use
   `video-gen`; explicit memes use `anycap-media`.
5. **Validated generated technical / hybrid route**: for low-risk report,
   article, or talk explanations with one reading path, freeze a fact graph and
   allow AnyCap to generate the complete diagram candidate. Accept only after
   literal text plus topology audit finds zero critical mismatch. If topology is
   already correct, image-to-image or deterministic overlay may repair a local
   label, legend, or safety callout. For `T0` exact work, the model still owns
   only non-semantic decoration and all truth-bearing geometry stays
   deterministic: make the image model produce only non-semantic pixels.
   Title, labels, containers, connectors, arrowheads, lanes, and boundaries are
   truth-bearing geometry and remain deterministic. Read
   `generated-technical-diagrams.md`.
6. **AnyCap concept route**: short non-critical labels and a conceptual mechanism
   with a visible final reading path. Cover, metaphor, and product mood are
   allowed only when explicitly requested. Use a visual brief, schema check,
   and often a small bake-off.
7. **Annotation iteration route**: the user or agent needs precise visual edits
   to a generated or existing image. Use AnyCap annotation, then image-to-image.

## Social, Cover, And Screenshot Metrics

- Social covers and thumbnails still run the same gates. The surface is usually
  `social image`, `carousel cover`, `video thumbnail`, or `manual publish page`.
- Exact hook text, author line, topic labels, captions, and compliance text must
  be deterministic HTML/SVG/PIL overlay text.
- Screenshots used as evidence must be redacted before they become cover or
  carousel material.
- Actual billing/account values should be omitted or redacted by default. Show
  cost/API-equivalent figures only when the user explicitly selected a
  usage/cost topic and the project guardrail allows it.

## Preference Synthesis

What "good" means for the user:

- The diagram helps with engineering or business communication, not decoration.
- A generic illustration has a visible title, useful labels, and a structural
  reading path; it is not merely an attractive background.
- The visual adds information beyond the section heading or nearby prose. A
  correct but redundant diagram is removed instead of polished further.
- One primary reading path is visible within a few seconds.
- The diagram type matches the question: state is not disguised as flow,
  chronology is not disguised as architecture, and evidence is not recreated.
- Short Chinese labels are clean and not duplicated.
- Exact facts are real text or deterministic SVG/HTML, not baked into generated
  pixels.
- Visual density is high enough for technical readers, but sections have a clear
  focal path.
- Historical references are pattern input, not current system truth.
- A high-value non-exact visual deserves multiple model candidates because
  AnyCap budget is not the limiting factor.
- Failures become routing/test improvements, not endless prompt tweaking.

## Model Strategy After Routing

Only choose the model after the production route is known:

| Need | Default model strategy |
|---|---|
| Validated technical architecture/process with hierarchy | `gpt-image-2` first candidate; compare with `nano-banana-2` and audit against the fact graph |
| Chinese technical concept with short labels | `nano-banana-pro` final candidate; consider `gpt-image-2` and `seedream-5` bake-off |
| Fast technical draft or wide exploration | `nano-banana-2`; check schema and do not promote topology without asset-level audit |
| Image edit with camera/viewpoint controls | `gpt-image-2` first candidate |
| High-res refinement or style transfer | `seedream-5` candidate, QA for pseudo-text |
| Chinese understanding experiment | `qwen-image` only as experiment; QA for prompt scaffolding leakage |
| No-text style/mood exploration | `flux-kontext-max` or another no-text candidate; keep it decorative and run strict watermark/pseudo-text QA |
| Exact factual card | No image model for final text; deterministic only or no-text plate plus overlay |

Always run the live schema before generation:

```bash
anycap image models <model> schema --mode text-to-image
anycap image models <model> schema --mode image-to-image
```

## Decision Receipt And Generation Prompt

Keep the full routing contract in the sidecar/receipt, not in the image-model
prompt:

```text
观众问题:
关系语法:
图示类型:
Owner Skill / Renderer:
未选路线及原因:
视觉合同:
生产路线:
真相来源:
敏感信息策略:
风格预设:
布局:
文字策略:
仅显示这些文字:
禁止:
验证计划:
```

The actual generation prompt should contain only execution-relevant material:

```text
Goal and viewer takeaway:
Composition and relationship:
Visual style:
Visible text whitelist:
Required order/direction:
Negative constraints:
```

Do not send `Owner Skill / Renderer`, rejected routes, model names, style/layout
IDs, source-review notes, or the validation plan as prompt scaffolding. They
belong in the receipt and can become accidental pixels without improving the
composition.

Quote literal visible labels and state that the whitelist is exhaustive. Keep
instructions outside that whitelist. If exact text or geometry is critical, move
it to deterministic rendering instead of making the prompt longer.

## Failure Response

| Failure | Correct response |
|---|---|
| Atmosphere-only image returned for a generic `配图` request | Reject it as incomplete. Extract the source takeaway and nodes, choose a structural contract, and produce a text-bearing final visual. |
| No-text plate looks good but has no final overlay | Keep it as an intermediate only; add deterministic title, labels, containers, connectors, and relationships before delivery. |
| Generated no-text plate invents boxes, lanes, arrows, ticks, or pseudo-UI | Reject it as a semantic skeleton. Regenerate a decoration-only background and build all information geometry deterministically. |
| Duplicate labels or wrong arrows | Simplify layout or switch to deterministic route |
| Generated technical candidate has a missing node, flattened hierarchy, detached feedback loop, or false sequence | Reject the candidate and retreat to deterministic rendering; do not cover a structural error with a local overlay |
| Chinese garbling or pseudo-text | Reduce generated text, use no-text plate plus overlay, or change model |
| Generic SaaS card wall | Re-state claim and choose a stronger visual contract |
| Architecture/flow was chosen only because the request said `配图` | Re-run relationship-grammar routing; select sequence, state, DFD, decision, timeline, causal, evidence, value-stream, journey, chart, or map as the context requires |
| One canvas mixes architecture, timeline, chart, cause tree, and checklist | Split by viewer question into a small visual set with one dominant grammar per asset |
| Text and arrows are correct but the image only repeats prose | Remove it, or rebuild around a source-backed relationship, contrast, mechanism, decision, or evidence point |
| Nodes were added only to hit a visual quota | Delete filler nodes and keep only source-mapped actors, stages, boundaries, or evidence |
| Too much prose in report visual | Convert to gate, matrix, timeline, swimlane, chart, or appendix |
| User asks to reference a historical archive | Extract the pattern, verify current facts elsewhere |
| Cloud icons look fake | Replace with official icon pack or generic deterministic symbols |
| Generated image contains exact fact drift | Rebuild the factual layer deterministically |
| Public schema succeeds but generation returns `AUTH_INVALID` | Treat AnyCap as unavailable. Do not silently start browser login or return filler; use an equivalent deterministic route when valid, otherwise report the authentication blocker and required user action. |
| Explicit no-text/atmosphere output contains a watermark, pseudo-text, or UI trace | Reject it. No-text finals still require image-read plus original-resolution inspection. |

## Minimum Sidecar Fields

Every generated or derived asset should record:

- surface and usage location
- intent default: information-bearing or explicitly atmosphere/no-text
- one-sentence visual claim
- viewer question, decision/inference, and information increment beyond nearby prose
- final visible text inventory and relationship structure
- generated-technical assurance class (`T0`, `T1`, or `T2`), required/allowed text, fact graph, independent sets, and forbidden semantics
- source mapping for every node, label, and relationship
- truth risk decision
- visual contract
- relationship grammar, visual family, owner skill, and renderer
- production route and rejected alternatives
- model candidates and selected model, if AnyCap was used
- command/prompt/spec/input files
- output path
- validation result
- rejected candidates or failure reason
