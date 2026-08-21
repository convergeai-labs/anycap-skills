---
name: anycap-architecture-diagrams
description: Produce architecture and system diagrams with AnyCap — fact-graph-first prompting, label fidelity audit via image-read, hybrid plates with deterministic labels, and a public-safety pass that strips internal system details before generation. Use when turning a system design into a shareable architecture figure with AnyCap image models.
---

# AnyCap Architecture Diagrams

Turn a system design into a clean architecture figure with AnyCap. Distilled from repeated real use; the loop below is the one that converges.

## 0. Sanitize the fact graph FIRST (public-safety pass)

An architecture diagram is a浓缩的系统地图 — it leaks exactly what scans can't see: internal system names, topology, data flows. Before anything is generated:

- Write the fact graph (nodes, edges, labels) in plain text.
- Replace every internal name with its **public role** (`内部订单库` → `orders DB`, `knlb-xxx` → `API gateway`). If a node's only honest name is an internal one, the diagram is not publishable — generalize the whole example or pick a synthetic system.
- Drop what the viewer question doesn't need. Each removed node is attack surface removed.
- For "example/teaching" diagrams, prefer a **synthetic reference system** (a generic RAG app, a URL shortener) over any real deployment.

## 1. Freeze the contract

- Viewer question + one takeaway (what should the reader understand in 10 seconds?)
- Fact graph: node list, edge list with direction, **exact label whitelist**
- Grammar: layered architecture / request flow / deployment / state machine — one per figure
- Surface: doc inline (16:9 or 4:3), slide, or README hero

## 2. Choose the production branch

| Branch | When | Trade-off |
|---|---|---|
| **T1 full generated** (labels in image) | short labels (≤4 chars each), ≤10 nodes, Chinese OK | beautiful, but label fidelity must be audited |
| **Hybrid** (no-text generated plate + deterministic text overlay) | long labels, many nodes, exact wording required | labels guaranteed; two-step work |
| **Retreat to deterministic** (Mermaid/SVG/D2) | topology must be exact, or two audits already failed | always correct, less pretty |

Never invent nodes, edges, arrows, or numbers beyond the frozen fact graph — and don't let the model do it either.

## 3. Generate with the fact graph in the prompt

Structure the prompt as: scene grammar → node inventory with exact labels → edges with direction → style (flat vector, dark/light plate) → constraints ("every label must be exactly as listed, no extra text").

```
anycap image generate --model <model> --prompt "..." -o candidate.png
```

For Chinese-labeled T1 candidates, models with strong short-label rendering (e.g. nano-banana class) beat general image models.

## 4. Audit with image-read — labels, not vibes

```
anycap actions image-read --file candidate.png \
  --instruction "List every text label in this diagram exactly as written, and every
   arrow with its direction. Then: (1) any label not in this whitelist: <list>;
   (2) any missing/duplicated label; (3) any arrow pointing the wrong way;
   (4) any pseudo-text. Answer AUDIT-PASS or AUDIT-FAIL - <details>."
```

Typical failure modes: misspelled labels, merged nodes, reversed arrows, hallucinated extra services, pseudo-text watermarks. **One concrete failure → regenerate with the failure named in the prompt. Two failed audits → switch branch (hybrid or deterministic).** Don't keep rolling the same branch.

Measured ceiling (two shipped projects): T1 full generation with inline labels is reliable up to **~6 nodes / ~6 edges**. At 8 nodes × 8 arrows, every roll drifted exactly one arrow — a different one each time (fix-one-break-another carousel). Layout-first prompt fixes (place a node so its required arrow is short and vertical) are a valid second-round move, but they don't move the ceiling. Retreating to a deterministic SVG/Mermaid for the densest view is a branch decision, not a failure — the deterministic source doubles as the editable truth layer.

## 5. Hybrid finishing when labels must be perfect

Generate a no-text plate (gate it CLEAN like any brand mark), then overlay labels deterministically (HTML/CSS, SVG, or an editor). The plate carries the mood; the overlay carries the truth.

## 6. Completion gate

- Every label matches the whitelist exactly; every edge direction verified
- No invented components; no internal names anywhere
- Readable at the consumer's real size (inline width, not 100% zoom)
- Provenance sidecar: fact graph, model, audit results, branch decisions

## Anti-patterns

- "Draw my company's architecture" as a prompt — semantic leak by design
- Accepting a diagram because it "looks professional" while two arrows point backwards
- More than ~12 nodes in one generated figure — split into views
- Shipping the raster without keeping the fact graph — the next edit restarts from zero
- Shipping a single overview when the system has distinct questions — a small-multiples **view set** (overview / request flow / data pipeline / deployment), all projecting one frozen fact model, beats one overloaded poster. Views share node names, palette, typography, and connector style; change the model in one view and you must change all.
