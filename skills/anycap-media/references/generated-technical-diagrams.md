# Generated Technical Diagram Contract

As of 2026-07-25. Read this only after the context router has selected an
architecture, process, control-loop, decision, or similarly structured
explanatory visual and generation would materially improve the composition.

AI image generation is now a valid production path for some technical diagrams.
It is not a replacement for the source model, authentic evidence, or
deterministic rendering where reviewability is the primary requirement.

## Assurance classes

| Class | Typical use | Generated topology | Final route |
|---|---|---|---|
| `T0 exact` | architecture review, release/audit evidence, security/trust boundary, provider icons, exact API/data/state semantics | prohibited as source of truth | deterministic SVG/HTML/canvas; generated pixels may be decoration only |
| `T1 validated explanatory` | report, article, talk, proposal, mechanism/process explanation with short labels and one reading path | allowed as a candidate | AnyCap full diagram candidate, accepted only after fact-graph diff and visual QA |
| `T2 concept` | opener, metaphor, early exploration, non-critical mechanism | allowed | AnyCap concept route with ordinary image QA |

Do not infer the class from the requested tool. The facts, consumer surface, and
consequence of a wrong arrow determine the class.

## Eligibility for `T1`

All conditions must hold:

- one dominant relationship grammar and one primary reading path;
- no authentic evidence claim, exact metric, hash, private ID, real map, or
  provider-specific icon requirement;
- short visible labels, normally no more than about 18 required labels;
- a frozen source packet lists every required node, edge, branch, boundary, and
  independent/non-sequential set;
- a wrong result can be rejected without changing production, audit, release,
  incident, or security truth;
- the final consumer accepts a raster illustration and does not require editable
  nodes.

If any condition fails, use `T0`.

## Freeze the fact graph first

Do not illustrate prose directly. Create a renderer-neutral contract:

```yaml
claim: one sentence
required_text: [literal labels]
allowed_display_text: [optional stage headings or legend words]
nodes:
  - id: stable-id
    label: exact visible label
    type: actor | process | system | decision | outcome | boundary
edges:
  - from: stable-id
    to: stable-id
    relation: invokes | emits | verifies | depends-on | feedback | branch
    label: visible edge label
independent_sets:
  - [push, deploy, db-write]
forbidden:
  - reverse edge
  - invented node
  - implied sequence between independent actions
```

The fact graph remains the source of truth even when the final pixels are fully
generated.

## Production workflow

1. Classify `T0`, `T1`, or `T2`.
2. For `T1`, freeze the fact graph and assign every reference image one role:
   `style reference`, `structure reference`, `subject reference`, or `edit
   target`.
3. Run `anycap status`, list live models, and read the selected model schema.
4. For a high-value `T1` asset, generate two candidates from the same fact graph.
   Prefer `gpt-image-2` when hierarchy and topology are the hard part; use
   `nano-banana-2` for fast drafts and alternate composition.
5. Inspect original pixels and intended consumer size.
6. Run `anycap actions image-read` with the literal text inventories, node/edge
   list, independent sets, and forbidden semantics. Ask for missing, extra,
   reversed, detached, duplicated, and falsely sequential relations.
7. Compare the image-read result with direct visual inspection. Image-read is an
   assistant, not the acceptance authority.
8. Accept, repair, or retreat using the rules below. Record the decision in the
   sidecar.

## Accept, repair, or retreat

Accept a `T1` candidate only when:

- all critical nodes and edges are present;
- no direction, branch, ownership, trust, or independence semantic is wrong;
- required text is legible and optional text is inside
  `allowed_display_text`;
- there are no invented factual nodes, provider logos, evidence marks, or
  pseudo-text;
- the diagram remains understandable at the actual report/deck/article size.

Repair is allowed when topology is already correct and the defect is local:

- one label typo or a non-factual legend;
- a safety callout that visually implies sequence where the fact graph says the
  actions are independent;
- spacing, hierarchy, or a decorative treatment that does not change meaning.

Use image-to-image for a generated-pixel repair, or a deterministic overlay when
the corrected text/legend must be exact. Re-run the complete fact-graph audit
after every edit because image editing can drift protected regions.

Retreat to `T0` when:

- a node is missing or invented;
- an edge is reversed, detached, merged, or attached to the wrong node;
- hierarchy is flattened;
- a feedback loop starts at the wrong decision;
- retries, guards, trust boundaries, async semantics, or independent actions are
  misrepresented;
- two repair attempts introduce new semantic drift.

Never hide a structural error with a white patch or local label overlay.

## Prompt skeleton

```text
Goal and takeaway: ...
Visual contract: architecture boundary | process/gate | control loop | decision
Reference roles: image 1 = style reference; image 2 = structure reference
Composition: one reading path, region roles, hierarchy, whitespace
Required text: exhaustive literal list
Allowed display text: exhaustive optional list
Required relationships: A -> B (relation); ...
Independent/non-sequential sets: ...
Negative constraints: no extra labels, reverse arrows, invented nodes, logos,
watermarks, pseudo-text, shadows, gradients, or decorative UI chrome
```

## Primary references

- C4 uses zoom levels to tell different stories to different audiences and says
  teams normally need only the levels that add value: `https://c4model.com/diagrams`.
- Azure recommends audience/message-first selection, labeled unidirectional
  relations, consistent notation, metadata, legends, progressive disclosure,
  and version-controlled source:
  `https://learn.microsoft.com/en-us/azure/well-architected/architect-role/design-diagrams`.
- Structurizr keeps a C4 architecture model in text-based DSL:
  `https://docs.structurizr.com/dsl`.
- Google documents advanced text rendering for diagrams and infographics, while
  also warning that image models do not always follow exact requested counts and
  work best when text is prepared first:
  `https://ai.google.dev/gemini-api/docs/image-generation`.
