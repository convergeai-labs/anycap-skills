# Architecture Report Diagram Playbook

Use this reference for a coordinated set of AnyCap architecture, process, data,
and future-state diagrams inside an HTML report or technical brief. It captures
reusable production evidence through 2026-08-03; project-specific facts must
remain in the project repository.

## Contents

1. [Reader contract](#reader-contract)
2. [Visual-set contract](#visual-set-contract)
3. [Per-view format and information-increment gate](#per-view-format-and-information-increment-gate)
4. [Preferred visual language](#preferred-visual-language)
5. [Reusable diagram grammars](#reusable-diagram-grammars)
6. [Production workflow](#production-workflow)
7. [HTML consumption contract](#html-consumption-contract)
8. [Acceptance and retreat rules](#acceptance-and-retreat-rules)
9. [Compact delivery](#compact-delivery)

## Reader contract

Optimize the report for one short first-read route:

1. Establish scale and system interaction: modules, interfaces, tables,
   authority, and external systems.
2. Explain canonical IDs and data responsibilities; keep exact fields and
   constraints in selectable HTML or linked references.
3. Explain current functions one viewer question at a time.
4. Separate proposed future architecture from current deployed behavior.
5. Move exhaustive API, DB, audit, and migration detail into folded or linked
   reference layers.

Use one strong diagram plus a short caption before adding prose. Do not make the
reader decode a visual atlas before understanding what the system is.

## Visual-set contract

Create an inventory before generation:

```yaml
view_key: stable-name
state: current-observed | current-unknown | target-proposed
viewer_question: one question
takeaway: one sentence
grammar: one relationship grammar
fact_ids: [stable-source-backed-facts]
truth_layer: code | schema | HTML table | deterministic diagram
consumer: report section + desktop/mobile behavior
generated_asset: optional T1 image
known_ambiguity: none | exact limitation requiring repair/caption
```

All views must project one stable system model. Shared actors, IDs, ownership,
and direction cannot drift between figures.

Generated pixels are the explanation layer. Repository code, schema, exact
tables, and deterministic source remain the truth layer. A generated data map
must not be called an ER diagram unless every displayed relation is an audited
database relation.

## Per-view format and information-increment gate

Do not choose `all raster` or `all SVG` as a report-design ideology. Decide each
view independently:

1. State what the reader will understand after seeing the figure that the
   nearby title, bullets, and previous figure do not already explain.
2. Mark the view `restore`, `generate`, `deterministic`, `repair`, `merge`, or
   `omit` before creating pixels.
3. Use AnyCap for an eligible explanation layer; use deterministic SVG/HTML for
   exact hierarchy, schema, IDs, or editable topology; omit or merge a repeated
   overview.
4. Apply the latest explicit user correction at its stated scope. A request to
   restore one clear SVG tree does not cancel a raster-first report, and an
   earlier report-wide no-SVG preference does not override that later scoped
   correction.

Visual consistency means one fact model, palette, typography, connector system,
and caption voice. It does not require one file format or one layout template.
Do not regenerate a correct, clearer deterministic tree merely to make the asset
folder look uniform.

## Preferred visual language

Use these defaults when the user has not selected another direction:

- warm-white or white editorial canvas;
- navy/indigo as the structural color, with restrained orange and teal for
  external authority, risk, proposed state, or secondary paths;
- crisp 2D technical illustration with limited isometric depth;
- one dominant focal boundary, hub, rail, switchboard, or transaction corridor;
- short Chinese labels, exact English IDs only when they materially help;
- visible reading order, strong region roles, thin unambiguous connectors;
- logical boundaries, labeled boxes, trees, lanes, and arrows before literal
  object metaphors; use a small icon only when it clarifies a mechanism;
- 16:9, normally `2k` PNG master plus compressed JPG consumer;
- shared palette, type, connector, and caption system across the set while each
  view keeps its correct relationship grammar.

Avoid graph-paper decoration, rainbow mastheads, pastel card walls, oversized
titles, repeated three-column templates, dashboard chrome, provider logos,
pseudo-code, tiny field lists, decorative arrows, and oversized safes, wallets,
printing machines, conveyor belts, or other physical props standing in for
software architecture.

Restore an audited historical asset before regenerating when all are true:

- its frozen facts still match the current baseline;
- its viewer question and grammar match the new report section;
- its selection/audit record is available;
- direct inspection at the new consumer size passes;
- any limitation is non-structural and is explicitly bounded by the caption.

Do not restore solely because the image looks better. Regenerate or retreat when
ownership, direction, hierarchy, or current/target state has changed.
After this reuse inventory freezes, generate only missing viewer questions;
do not regenerate the accepted set merely to make the run look uniform.

## Reusable diagram grammars

| Viewer question | Preferred grammar | Required emphasis | Common failure |
|---|---|---|---|
| Who authenticates, owns data, and calls whom now? | authority boundary | actor, owned system, external authority, retained product ownership | provider arrow looks like identity creation |
| How does one request choose create/reuse/merge/conflict? | decision gate and outcome convergence | fast path, guarded decision, 0/1/N, terminal outcomes | branch bypasses canonical result |
| How do provider-specific rules differ? | provider comparison orbit or aligned lanes | one key per provider, explicit non-merge rules | one field drawn as universal identity key |
| Why does verification not mutate state immediately? | two-rail contract separation | challenge rail and sync rail with no shortcut edge | provider appears to update state directly |
| What do the main tables/IDs own? | data-domain switchboard | domain groups, canonical ID, responsibility | domain arrows misread as FKs |
| How do owner/account/assets/evidence relate? | deterministic hierarchy tree | parent coordinate, aggregate root, asset IDs, audit snapshots | one generated poster mutates IDs or confuses parentage |
| How do catalogue definitions become an entitlement? | two figures: catalogue hierarchy, then materialization boundary | definition/version first; request inputs and resulting entitlement second | structure and issuance mechanism collapsed into one crowded figure |
| What changes an entity's lifecycle state? | trigger-ownership map plus compact state flow | API command, explicit batch action, scheduled sweeper, guard, terminal result | states shown without who or what can trigger them |
| How is a report query constructed? | query-construction pipeline | scope, group_by, metrics, filters, result | unrelated columns with no operational reading path |
| How do concurrent requests and transactions converge? | dual-request transaction corridor | lock order, re-read, CAS, commit/rollback | helper wording implies independent commit |
| How should products avoid direct vendor coupling? | provider-neutral boundary | stable gateway, adapter, managed vendor, internal session | future proposal shown as current deployment |
| How does browser login return to product session? | single login trust rail | browser/BFF, gateway, adapter, callback, one-time code | BFF and central gateway collapse into one actor |
| Why does one external identity yield separate tenant users? | tenant-isolated branches | reusable proof, explicit binding, isolated principals | same email drawn as shared authorization subject |

When two questions require different grammars, create two figures. Do not merge
boundary, sequence, ER, decision, and roadmap semantics into one poster.
For onboarding reports, do not default to sequence lifelines. Use them only when
message order, sync/async return, or actor handoff is the actual viewer question.

## Production workflow

1. Freeze the report outline and viewer-question inventory.
2. Audit historical assets, fact graphs, selection records, and known defects.
3. Remove or merge duplicated opening views, then mark each remaining view
   `restore`, `generate`, `repair`, `deterministic`, or `omit`.
4. For every generated T1 view, freeze required text, nodes, edges, independent
   sets, forbidden semantics, and current/proposed state.
5. Use one reference role per input image: style, structure, subject, or edit
   target. A historical report image is style evidence, not current truth.
6. Generate two same-prompt candidates. Select by semantic correctness,
   reading order, then aesthetics.
7. Run literal image-read plus direct original-pixel inspection. Reject wrong
   ownership, reverse/detached edges, invented nodes, false sequence, and
   pseudo-text.
8. Repair only one local defect when topology is already correct. Repeat the
   complete fact-graph audit after repair.
9. Build an ordered contact sheet and inspect the set for duplicated layouts,
   density drift, notation drift, and current/target confusion.
10. Embed the accepted web raster into the real report and validate desktop,
    narrow mobile, captions, links, console, and network.

Keep per-view evidence together:

```text
fact-graph.yaml
prompt.txt
candidates/*.png
final/<view>.png
final/<view>-web.jpg
final/<view>-web.prompt.md
final/<view>.audit.json
selection.yaml
```

The report package should reference only selected assets. Rejected candidates
remain local evidence and never become consumer dependencies.

## HTML consumption contract

Each report-facing figure needs:

- one visible viewer question;
- the compressed JPG/PNG with real intrinsic dimensions;
- short, source-equivalent alt text;
- one sentence stating the takeaway or ambiguity boundary;
- a folded source drawer linking code, schema, fact graph, or research;
- a full-resolution link only when the original is intentionally shipped.

On narrow screens, keep page-level horizontal overflow at zero. Allow local
horizontal scrolling inside a bounded figure viewport when shrinking the image
would make labels unreadable.

If the user prefers no SVG diagrams, consume only audited raster images in the
report and contact sheet. Retain deterministic SVG/HTML/source privately for
semantic verification; do not delete it or misrepresent the raster as exact
proof.

When the user later restores one deterministic view, treat that as a scoped
consumer override: keep the rest of the raster-first set unchanged and validate
the mixed-format report as one semantic system.

For responsive `<picture>` elements, validate `currentSrc` after the viewport is
stable. Source switching can cancel the old request with `ERR_ABORTED`; do not
report that cancellation as a broken image. Capture and inspect desktop and
mobile states independently.

Do not let captions silently legalize structural errors. A caption may bound a
non-structural interpretation risk, such as “domain grouping, not FK topology”.
Repair or reject wrong ownership, wrong direction, missing nodes, or false
transaction behavior.

## Acceptance and retreat rules

Accept the visual set only when:

- each figure answers a distinct viewer question;
- no opening or overview figure repeats the same boundary and interaction chain
  without adding a new relationship;
- all required current facts match the fixed baseline;
- proposed content is visibly marked proposed;
- generated labels, arrows, branches, and boundaries pass literal audit;
- every known limitation appears in the figure caption or source drawer;
- the set reads coherently without using one repeated template;
- all report images load at the deployed path;
- desktop and narrow-screen pages have no root overflow;
- the contact sheet exposes the complete selected set.

Retreat to deterministic rendering or selectable HTML when:

- exact fields, FKs, indexes, route counts, metrics, or implementation evidence
  must be inspected;
- more than about 18 required labels remain after splitting;
- two repairs introduce semantic drift;
- the generated asset requires prose to correct a structural falsehood;
- editability is part of the consumer contract.

## Compact delivery

Generation and publishing are separate authorizations. Hand Page delivery to
`anycap-access` only after the user authorizes the exact site and access mode.

Build a compact reader bundle instead of uploading the generation workspace:

- include HTML, selected web rasters, required reference documents, and the
  minimal public evidence needed by report links;
- exclude candidates, repair attempts, raw prompts, local paths, secrets, and
  unrelated historical evidence;
- rewrite or remove links to files not included in the bundle;
- run a sensitive-pattern scan and local-link check before upload;
- verify the live title, figure count, image natural dimensions, HTTP status,
  console, access mode, and mobile overflow after publication.

Keep full-resolution PNGs local unless the report intentionally exposes an
“open original” action and the Page size budget allows it.
