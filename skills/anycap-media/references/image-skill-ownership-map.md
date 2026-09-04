# Image Skill Ownership Map

As of 2026-08-13. Use this map when a request could match several image or
diagram Skills. It defines ownership, not model preference.

```text
What must the viewer understand?
  open/undecided visual      -> image-gen
  explanatory relationship  -> image-gen-system
  exact values/categories    -> chart-gen
  delegated AnyCap T1/T2     -> anycap-media
  exact evidence/map         -> authentic specialist
  Agent Skill human review   -> illustrate-skill -> image-gen
  expressive bitmap         -> imagegen, unless AnyCap is explicit
  explicit AnyCap media      -> anycap-media
  legacy MCP asset work      -> image-gen-guide
  animated exact explanation -> video-gen after a static truth source
```

## One owner per intent

| Intent | Primary owner | Producer or downstream owner | Do not route to |
|---|---|---|---|
| Generic `配图`, `image 配图`, report/article/talk explanation, undecided visual type | `image-gen` | `image-gen-system`, `chart-gen`, or a selected specialist | A provider chosen only from the word `image` |
| Architecture/process/state/decision/boundary explanation | `image-gen-system` | Deterministic canvas/Mermaid, or `anycap-media` for an eligible T1/T2 branch | A provider claiming the generic route |
| Exact values, trends, categories, ranking, distribution, or matrices | `chart-gen` | `chart-guide` or another deterministic renderer | Any generated raster as numeric truth |
| Ordinary photo, illustration, hero, texture, sprite, cutout, or bitmap edit with no AnyCap signal | `imagegen` | Built-in image generation/editing tool | `anycap-media` or the diagram router |
| Explicit AnyCap photo, product shot, decorative asset, image edit, video, music, speech, dialogue, or annotation/refinement loop | `anycap-media` | AnyCap CLI and selected live model | Generic explanatory semantics |
| Low-risk generated technical explanation selected by `image-gen-system` | `anycap-media` | `anycap-media` is only the delegated raster producer | Direct media production without a frozen fact graph |
| Human-review visuals for a non-trivial Agent Skill package | `illustrate-skill` | `image-gen` selects semantics; exact or generated producers stay delegated | Implicitly triggering Skill review from an ordinary image request |
| Exact topology, ER/schema, sequence, state, transaction boundary, ID tree, decision, numeric chart, or release evidence | Matching deterministic/evidence owner | `technical-diagram-canvas`, `architecture-decision-canvas`, `diagram-design`, `architecture-diagram`, Mermaid, chart, screenshot, map, or another exact specialist | Generated pixels as the sole truth source |
| Animated technical explanation | Static exact owner first, then `video-gen` | Deterministic renderer selected by the software-video contract | Image-to-video for text-heavy diagrams |
| Existing `mcp-image-gen` asset diagnosis, reproduction, or migration, or an explicit request to use that legacy MCP | `image-gen-guide` | Legacy MCP only when still available and authorized | New generic image work |
| Legacy ImageMCP visual style requested for a new figure | `anycap-media` | Current deterministic/AnyCap/imagegen producer selected by truth risk | Reactivating ImageMCP merely to recover a style |

## Observable trigger signals

- `用 image 配图`, `给报告配图`, `你决定图示形式` -> `image-gen`.
- `给这个 Skill 增加人类评审图`, `检查 Skill 的图示机会` -> explicit
  `illustrate-skill`, which returns semantic selection to `image-gen`.
- `image-gen-system` selects an eligible AnyCap T1/T2 technical branch, or the
  user explicitly requests an AnyCap technical diagram -> `anycap-media`.
- `生成一张陶瓷杯产品图`, `做无字 hero`, `编辑这张照片` with no AnyCap
  wording -> `imagegen`.
- `用 AnyCap`, `AnyCap CLI`, `用这个模型`, `圈选后继续改`, or a requested
  image/video/music/audio package -> `anycap-media`.
- `维护以前 mcp-image-gen 生成的图`, `复现旧 ImageMCP 资产`, or explicit
  legacy-provider diagnosis -> `image-gen-guide`.
- `像以前 ImageMCP 那种白底蓝图风格` -> style reference only; keep the
  current `image-gen-system` production route.
- Exact table fields, foreign keys, API names, IDs, transaction corridors,
  quantities, screenshots, or audit claims -> deterministic/evidence route even
  when the prompt also says AnyCap or image.

Do not inspect both expressive bitmap owners merely to invent a tie-break. The
presence or absence of an explicit AnyCap signal is sufficient.

## Legacy ImageMCP lessons worth keeping

Keep the transferable production evidence without reviving the provider:

- One diagram uses one relationship grammar and one clear reading path.
- Generated Chinese labels stay short and non-critical; exact text is rendered
  deterministically.
- A no-text plate must forbid letters, numbers, labels, logos, watermarks,
  pseudo-text, and UI traces, then receive an original-resolution read check.
- Generated models must never derive totals, split numbers, or invent schema,
  API, ID, state, arrow, or transaction facts.
- Local repair is preferable to full regeneration when the fact graph is
  already correct; re-check protected regions after every edit.
- 429, timeout, provider, and model availability are runtime failures, not
  reasons to weaken the truth contract or silently choose an incompatible
  Chinese-text model.

The old MCP configuration, timeout notes, and model table remain historical
diagnostic evidence in `image-gen-guide`. They are not current defaults.

## Handoff rule

The semantic owner stays responsible for the complete result. A delegated
producer returns the versioned asset, actual dimensions/duration, selected
model/tool, prompt or source spec, validation evidence, limitations, and
`return_to`. Producing pixels alone does not complete a report, deck, article,
or technical-diagram task.

Remote upload, Page publication, Drive delivery, Feishu whiteboard writes, and
provider reactivation require explicit target authorization; local generation
does not imply any of them.
