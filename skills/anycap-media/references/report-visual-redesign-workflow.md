# Existing Report Visual Redesign Workflow

Use this workflow when an existing report, page, deck, or diagram set is
described as unclear, repetitive, overloaded, hard to read, or in need of a
comprehensive visual redesign.

The goal is to improve explanation, not merely styling. Keep business facts,
source authority, and remote-write safety unchanged.

## 1. Protect The Baseline

Before editing:

- record the current artifact path, consuming surface, viewport, and relevant
  source/evidence paths;
- capture current desktop and narrow-screen evidence when the artifact is
  renderable;
- inventory diagrams, charts, screenshots, tables, and repeated visual patterns;
- preserve old assets and use versioned paths for candidates and replacements;
- mark unknown or stale facts instead of redrawing them as current truth.

Do not overwrite the formal artifact while its content route or visual direction
is still under discussion.

## 2. Diagnose Before Redrawing

For every current visual, record:

- the viewer question and intended takeaway;
- its dominant relationship grammar;
- the facts, identifiers, counts, or evidence it claims;
- where it is consumed and the real available size;
- its actual defect: wrong grammar, semantic overload, duplicated prose,
  all-in-one panorama, weak hierarchy, connector ambiguity, unreadable text,
  repeated card-wall layout, inconsistent notation, or stale evidence.

An aesthetic complaint may expose a semantic defect. Do not assume color and
spacing are the whole problem.

## 3. Separate Two Decisions

Freeze these independently:

### Content architecture

Choose the reader route:

- journey-first for business operations and user scenarios;
- system-first for ownership, boundaries, and technical onboarding;
- evidence-first for validation, migration, incident, or release claims;
- progressive hybrid for executive summary → journeys → mechanisms → lookup
  appendix.

### Visual grammar

Choose the relationship needed by each asset: boundary/authority map, lifecycle
state model, decision canvas, data/evidence flow, causal map, quantity chart,
overview-plus-zoom, comparison matrix, or concept illustration.

Visual style is applied only after these two decisions. A palette is not a
content architecture, and a flowchart is not a universal grammar.

## 4. Build A Direction Lab When Needed

Create a local direction lab before formal rewrite when:

- the user rejects the current clarity or visual language;
- the user asks to see alternatives or references;
- the target audience or reading route is unresolved;
- a large report contains several visual families that must work as a set.

Compare content routes separately from visual treatments. Use concise
annotations to state what each direction optimizes, what it hides, and where it
fits. Do not present several recolors as distinct directions.

## 5. Produce Real Candidate Visuals

Create three to five source-backed candidates before approving the system:

- each candidate answers a distinct, important viewer question;
- together they exercise the main grammars required by the report;
- labels, topology, states, identifiers, and quantities come from current
  evidence, not generic placeholders;
- when comparing style alone, freeze the semantic packet and topology;
- exact technical facts remain deterministic; generated imagery is limited to
  concept or low-text framing unless it passes the generated-technical contract.

For a system report, a useful candidate set often includes boundary/authority,
lifecycle, decision, and evidence-flow views. This is a pattern, not a required
four-picture template.

## 6. Review The Set, Not Only Each Asset

Render an ordered gallery or contact sheet and inspect:

- semantic consistency across shared entities and arrows;
- duplicate layout patterns and notation drift;
- density balance across the set;
- titles, labels, connector direction, clipping, overlap, and contrast;
- actual readability at desktop and narrow consumer widths;
- accessibility name and structured long-description equivalence.

Keep a defect log. Complete at least one inspect → fix → re-check cycle for any
material defect. A non-empty export is not acceptance.

## 7. Freeze An Implementation Manifest

Before rewriting the formal artifact, create a manifest with:

| Field | Meaning |
|---|---|
| current asset/section | What exists now |
| viewer question | What the reader must learn |
| diagnosed defect | Why the current form fails |
| action | keep, refresh, redraw, split, merge, or remove |
| target grammar | Relationship syntax for the replacement |
| source/evidence | Current truth used to build it |
| candidate/baseline | Approved visual or direction |
| consumer | Section, viewport, and intended reading order |
| acceptance | Semantic, visual, responsive, and accessible checks |
| status | proposed, approved, implemented, verified |

The manifest is the boundary between discussion and implementation. It prevents
the formal report from becoming an uncontrolled visual experiment.

## 8. Rewrite And Verify

After the direction and manifest are frozen:

1. implement in reader order, starting with the smallest high-value slice;
2. retain versioned old assets until the replacement is accepted;
3. validate source mapping and literal text/data;
4. inspect the real HTML/deck/page at its target desktop and narrow widths;
5. check internal scrolling, clipping, browser console/network errors,
   accessibility bindings, and structured fallback content;
6. review the complete set once more for repetition and notation drift.

Do not publish, upload, overwrite a remote document, or replace a shared page
without explicit authorization for that target.

## Anti-Patterns

- starting a full rewrite immediately after “the diagrams are unclear”;
- keeping the same card wall and only changing colors;
- using a generated image as proof of exact technical truth;
- compressing API, DB, runtime, state, and evidence into one panorama;
- comparing styles while changing topology between candidates;
- approving a candidate set built from generic placeholder facts;
- mixing the direction lab into the formal report as if it were final content;
- deleting the old artifact before the replacement passes consumer-surface QA.
