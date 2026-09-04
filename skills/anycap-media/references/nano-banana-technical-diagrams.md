# Nano Banana Complete Technical Diagram Contract

As of 2026-07-31. Read this after `generated-technical-diagrams.md` when the
selected route is a complete Chinese T1 technical diagram generated through
AnyCap Nano Banana, or when the user asks for the visual quality previously
obtained from an Image MCP backed by Nano Banana.

For a coordinated architecture-report set, also read
`architecture-report-diagram-playbook.md`; this file owns per-image generation,
while the playbook owns reuse, set consistency, HTML consumption, and delivery.

## Contents

1. [Use this route only when](#use-this-route-only-when)
2. [Why the better result works](#why-the-better-result-works)
3. [Production workflow](#production-workflow)
4. [Copyable fact graph](#copyable-fact-graph)
5. [Copyable generation prompt](#copyable-generation-prompt)
6. [Composition recipes](#composition-recipes)
7. [Copyable repair prompt](#copyable-repair-prompt)
8. [Copyable fact-graph audit](#copyable-fact-graph-audit)
9. [Optimization rules](#optimization-rules)
10. [AnyCap commands](#anycap-commands)
11. [Bounded evidence](#bounded-evidence)

## Use this route only when

All T1 conditions from `generated-technical-diagrams.md` must hold:

- one viewer question, one takeaway, one dominant relationship grammar;
- one primary reading path;
- normally no more than about 18 required visible labels;
- a frozen source packet lists every required node, edge, branch, independent
  set, boundary, and forbidden semantic;
- the raster is explanatory, not release, audit, security, metric, or runtime
  proof;
- a wrong candidate can be rejected without changing source truth.

Use deterministic SVG/HTML/C4/DFD when labels, topology, editability, or evidence
must be exact by construction.

## Why the better result works

Do not ask for “a beautiful architecture diagram” and do not translate a prose
section directly into pixels. Give the model three contracts:

1. **Fact contract**: exhaustive nodes, edges, independent sets, boundaries,
   required text, and forbidden semantics.
2. **Composition contract**: named canvas regions, reading direction, visual
   hierarchy, connector styles, and the role of each region.
3. **Pixel contract**: visual medium, palette, typography, whitespace,
   illustration density, and negative constraints.

An Image-MCP-style prompt is a production brief, not a bag of adjectives.
Explicit regions such as “far left / center boundary / upper right / lower
right” consistently outperform abstract requests such as “make it clear”.

## Production workflow

1. Freeze a renderer-neutral fact graph before writing the prompt.
2. Keep the decision receipt separate from the generation prompt; do not leak
   source paths, model notes, QA instructions, or layout IDs into visible text.
3. Set `Use case: infographic-diagram` and name the real consumer surface.
4. Define canvas regions and assign one semantic role to each.
5. Quote an exhaustive text whitelist and require every item exactly once.
6. List every required relationship again in plain `A -> B` form.
7. List parallel or non-sequential sets explicitly.
8. Use `nano-banana-pro`, normally `16:9`, `2k`, `png`, after checking live
   schema.
9. Generate two candidates from the same prompt. Do not change style between
   them; stochastic topology is what the comparison must reveal.
10. Inspect original pixels and consumer size, then run the complete fact-graph
    audit below.
11. Accept only a literal and semantic pass. Repair only when topology is
    already correct and the remaining defect is local.
12. After image-to-image repair, rerun the full audit, not only the repaired
    region.

## Copyable fact graph

Freeze this before writing the visual prompt:

```yaml
assurance: T1
viewer_question: <one question>
claim: <one-sentence takeaway>
required_text:
  - <literal label 1>
  - <literal label 2>
allowed_display_text: []
nodes:
  - {id: <stable-id>, label: <exact visible label>, type: actor | process | system | decision | outcome | boundary}
edges:
  - {from: <source-id>, to: <target-id>, relation: invokes | emits | verifies | depends-on | feedback | branch, label: <visible edge label>}
independent_sets:
  - [<peer-id-1>, <peer-id-2>]
forbidden:
  - <reverse edge>
  - <wrong ownership or boundary>
  - <invented node>
  - <false sequence between independent peers>
```

Every required label, node, edge and forbidden semantic must map to a source
fact. Keep proposed target architecture explicitly separate from observed
current state.

## Copyable generation prompt

Replace every `<...>` placeholder. Keep the section order.

```text
Use case: infographic-diagram
Asset type: Chinese engineering architecture report figure
Primary request: Draw one complete explanatory diagram showing <one relationship>. The one-sentence takeaway is: <claim>.
Audience: <specific readers> who need to understand <decision> in under 20 seconds.

Scene/backdrop:
<warm-white or dark technical canvas>, subtle blueprint detail only in the background, generous whitespace. No dashboard and no wall of repeated cards.

Style/medium:
Polished 2D vector technical illustration with restrained isometric system components, crisp Chinese typography, editorial architecture infographic. Use <authority color mapping>. Thin consistent connectors, minimal soft shadow, no photorealism.

Composition/framing:
- 16:9 landscape with one <left-to-right | top-to-bottom | center-out> reading path.
- Far left: <entry/subject region and its allowed content>.
- Center: <main system/boundary/hub and internal mechanisms>.
- Upper right: <provider/authority/decision region>.
- Lower right: <outcome/delivery/owner regions>.
- Draw <A> -> <B> labeled "<edge label>".
- Draw <B> -> <A> labeled "<feedback label>".
- Draw <C> and <D> as parallel peers, never one after the other.
- Make <boundary/ownership/decision> more important than decorative illustration.

Text (verbatim; render every item exactly once, and render no other words):
"<title>"
"<node 1>"
"<node 2>"
"<edge label 1>"
"<edge label 2>"
"<short conclusion>"

Required relationships:
- <A> -> <B> (<relation>)
- <B> -> <A> (<feedback>)
- <C> -> <D> (<relation>)

Independent/non-sequential sets:
- [<C>, <D>]

Constraints:
- All Chinese and English text must be large, sharp, horizontal and readable at report width.
- Preserve the exact arrow directions, ownership zones, branch count and boundary nesting.
- Use monospaced typography only for IDs, API names and code-like labels.
- Essential state must use text plus shape or connector style, not color alone.

Avoid:
extra labels, pseudo-text, duplicated labels, misspelled Chinese, broken underscores, reverse arrows, unlabeled arrows, invented nodes, provider logos, currency symbols, generic dashboards, card-wall UI, dense tables, tiny body text, sequence-diagram lifelines, neon cyberpunk, watermark.
```

## Composition recipes

Choose one recipe. Do not combine all three in one image.

### Authority boundary

- Far left: actor or business entry.
- Center: one large owned-system boundary with 2-4 internal mechanisms.
- Upper right: external provider authority.
- Lower right: separate final-effect owners.
- Solid arrow: synchronous command.
- Curved return arrow: webhook or feedback.
- Separate lower arrows: reliable downstream delivery.

The synchronous provider arrow must originate from the business/orchestration
mechanism, never from an Outbox block merely because the lines are nearby.

### Identity switchboard

- Far left: subject or scope identifiers.
- Center: one operation/index hub with the proposed lookup key embedded inside.
- Right: exactly 3-4 parallel authority branches, such as domain workflow,
  provider object, and event/delivery identity.
- End with a brace or ring meaning “one-to-many links, authorities preserved”.

Use a switchboard, routing index, or hub metaphor. Do not use a family tree
when the IDs are correlations rather than parent-child primary keys.

### Two-lane runtime mechanism

- Top lane: synchronous API/provider call and callback.
- Bottom lane: local transaction boundary containing business state plus
  durable pending work.
- After the transaction: parallel workers/relays and their exact targets.
- Use solid arrows for synchronous calls and dashed arrows for polling/claiming.
- Put acknowledgement versus final business effect at the far-right boundary.

Do not use sequence-diagram lifelines. Do not draw independent workers, targets,
or approval-gated actions as a sequence.

## Copyable repair prompt

Use image-to-image only when the base topology is already correct and the defect
is local. Make one semantic correction per pass.

```text
Edit this technical architecture diagram while preserving its overall composition, colors, title, ownership boundaries, typography, protected labels and every already-correct connector.

Make exactly these corrections:
1. <move/remove/replace one local element with an exact location and relation>.
2. Keep "<protected edge>" from "<source>" to "<target>".
3. Remove the unapproved text "<extra text>".

The complete allowed visible text whitelist is:
"<literal 1>"
"<literal 2>"
"<literal 3>"

Render no other words, letters or numbers. Keep all allowed text exactly once.
Do not introduce pseudo-text, logos, new nodes, reverse arrows or decorative
symbols. Preserve 16:9.
```

Do not repair missing nodes, wrong ownership, flattened hierarchy, false
sequence, or a wrong feedback loop with a local edit. Regenerate or retreat to
T0.

## Copyable fact-graph audit

Pass the complete source contract to `image-read`; do not ask only “is it
clear?”.

```text
你是技术架构图审计员。逐字、逐节点、逐连线检查图片，不要仅概括。

必须文字：<semicolon-separated exhaustive whitelist>。

必须节点：<node id/label/type list>。

必须关系：
- <A> -> <B>（<relation/edge label>）
- <B> -> <A>（<feedback/edge label>）

平行且不得画成顺序：<C>、<D>。

禁止语义：<reverse edge>；<wrong ownership>；<invented node>；<false sequence>；额外事实文字或伪文字。

输出 JSON 风格中文结论，字段：
missing_text、extra_text、malformed_text、missing_nodes、wrong_edges、
ambiguous_edges、false_sequences、invented_nodes、verdict。
verdict 只能是 PASS 或 FAIL；任一关键项非空即 FAIL。
```

Image-read assists acceptance; direct visual inspection remains authoritative.

## Optimization rules

### Improve information geometry

- Prefer one large boundary, one hub, one brace, or two lanes over many equal
  rounded rectangles.
- Use restrained illustration only when it reveals mechanism: a small database
  cylinder for persistence, rail for delivery, or switchboard for lookup. Keep
  the architecture itself as boundaries, boxes, trees, lanes, and connectors.
  Do not turn a ledger into a safe/wallet or issuance into a printing machine,
  factory, or conveyor belt. Decorative icons must not add factual text.
- Budget roughly 70% for semantic geometry, 20% for mechanism illustration,
  and 10% for background decoration.
- Keep the title short enough for one line and use 12-18 visible labels for the
  whole figure. Split the figure when that budget is exceeded.
- Make line origin visible. A correct label beside an ambiguous line is still
  a semantic failure.

### Improve prompt fidelity

- State the takeaway before style.
- Specify exact regions before palette.
- Quote every visible string and say “exactly once; no other words”.
- Repeat critical edges in both composition and required-relationships
  sections.
- Name independent sets. Models otherwise tend to convert peers into a
  left-to-right sequence.
- For IDs, explicitly protect underscores and prefixes.
- Ban text inside decorative icons unless that text is whitelisted.

### Improve iteration

- Generate two same-prompt candidates before rewriting the prompt.
- Select by semantic correctness first, reading order second, aesthetics third.
- A single extra word is repairable; a wrong arrow or missing node is normally
  regeneration.
- In repair prompts, list protected invariants and repeat the full whitelist.
- Stop after two repair attempts that introduce new drift; retreat to
  deterministic rendering.

### Reject these anti-patterns

- “No-text concept plate” for a question that requires a complete explanatory
  architecture diagram.
- A generic card wall with identical rectangles and no mechanism metaphor.
- Mermaid-like sequence lifelines when the user asked for an architecture or
  flow explanation.
- Prose pasted into the prompt without a frozen fact graph.
- Provider logos, bank/coin/card imagery, or pseudo-code that was not requested.
- Oversized safes, wallets, printing machines, factories, conveyor belts, or
  other literal props that replace rather than clarify the logical topology.
- Tiny full-table fields inside one raster diagram; keep dense schemas in HTML,
  SVG, or an appendix.

## AnyCap commands

Always fetch live schema:

```bash
anycap image models nano-banana-pro schema --mode text-to-image
anycap image models nano-banana-pro schema --mode image-to-image
```

Generate:

```bash
prompt=$(<"/absolute/path/diagram.prompt.txt")
anycap image generate \
  --prompt "$prompt" \
  --model nano-banana-pro \
  --param aspect_ratio=16:9 \
  --param resolution=2k \
  --param format=png \
  -o /absolute/path/diagram-a.png
```

Repair:

```bash
repair_prompt=$(<"/absolute/path/diagram-repair.prompt.txt")
anycap image generate \
  --prompt "$repair_prompt" \
  --model nano-banana-pro \
  --mode image-to-image \
  --param images=/absolute/path/diagram-a.png \
  --param aspect_ratio=16:9 \
  --param resolution=2k \
  --param format=png \
  -o /absolute/path/diagram-final.png
```

Audit:

```bash
audit_prompt=$(<"/absolute/path/diagram.audit.txt")
anycap actions image-read \
  --file /absolute/path/diagram-final.png \
  --instruction "$audit_prompt"
```

Keep prompt text in a local file so exact quotes and multiline structure survive
shell invocation.

## Bounded evidence

Production evidence from real report work (details stay in their owning
projects; the patterns are what transfer):

- Three 14–18-label fact graphs, first candidates: one failed because a
  synchronous edge visually originated from the wrong node and three extra
  labels appeared — one targeted image-to-image repair then passed the full
  audit; one of two same-prompt candidates passed every literal and
  relationship check while its twin invented one extra word; one candidate
  connected a relay past a broker to the result boundary. Same prompt, same
  model, different outcomes — every asset still requires its own
  fact-graph audit.

- A selective-restoration pattern: audit and restore previously accepted
  diagrams whose fact graphs still match instead of regenerating the whole
  set; generate only the missing views; reject misleading connectors, repair
  once, rerun the full audit; consume compressed JPGs in the report while
  retaining PNG masters, fact graphs, and deterministic truth layers outside
  the reader path; use captions to state non-structural limits such as
  “data-domain map, not ER”. A caption never excuses wrong ownership,
  direction, hierarchy, or current-versus-proposed state.

- A per-view retreat pattern: repeated overview figures were merged into one
  main interaction chain; a crowded generated poster was split into an exact
  hierarchy plus a separate materialization explanation; literal physical
  props (safes, wallets, machines) obscured architecture and were replaced by
  labeled logical boundaries; state figures needed trigger ownership, not only
  state names; a previously generated deterministic hierarchy tree was
  restored over a raster because it remained factually current and clearer.

This evidence supports choosing format and grammar per viewer question. It
does not make any single format the default, and it is evidence for the
workflow — not unconditional trust in the model.
