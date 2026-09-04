---
name: anycap-research
description: "Run explicit AnyCap multi-source investigations, market or competitive research, technical deep dives, literature/state-of-the-art reviews, evidence-backed comparisons, and the specialized football/World Cup dossier and entertainment-only prediction route. Not for local code analysis, single-source lookup, ordinary article drafting, or betting advice."
---

# AnyCap Research

Choose one research depth before searching. General investigations and football
briefings share source verification and dated evidence, but load different
references and outputs.

## Route one research job

| Need | Read |
| --- | --- |
| scoped multi-source investigation | [01-plan.md](references/01-plan.md), then [02-gather.md](references/02-gather.md), [03-analyze.md](references/03-analyze.md), [04-synthesize.md](references/04-synthesize.md), and [05-deliver.md](references/05-deliver.md) |
| one footballer or ambiguous identity | [football-lookup.md](references/football-lookup.md) |
| verify a critical football fact | [football-verify.md](references/football-verify.md) |
| squad or two-team comparison | [football-batch.md](references/football-batch.md) |
| tournament and head-to-head history | [football-history.md](references/football-history.md) |
| current player/team statistics | [football-stats.md](references/football-stats.md) |
| requested winner/scoreline call | [football-predict.md](references/football-predict.md) |

Load only the selected route. Use `anycap-access` only for install/auth/schema or
low-level command failure; do not run status before every search.

## Shared evidence contract

1. Freeze the question, cutoff date, sub-questions, required accuracy, excluded
   sources, output, and delivery boundary. Clarify only omissions that would
   materially change the research.
2. Save raw search/crawl outputs, source URLs, retrieval dates, notes, and claim
   support locally. Separate source fact, inference, and prediction.
3. Prefer primary/current official sources for time-sensitive facts and
   cross-check important claims across independent sources. A login wall, bot
   challenge, or verification stub is not evidence.
4. Resolve conflicts and gaps explicitly. Use `null` or `unknown` instead of
   inventing data.
5. Synthesize the requested artifact with citations and claim-level caveats.

Generic report visuals begin at `image-gen`; exact systems at
`image-gen-system`; exact numbers at `chart-gen`; eligible explicit/delegated
AnyCap production routes to `anycap-media`. Generated imagery is explanation,
not proof of a UI state, metric, event, or source claim.

## Football prediction boundary

Facts come first and the prediction appears last in a clearly labeled block.
Never present odds or win probabilities as facts, place wagers, or advise the
user to bet. Include the required disclaimer from
[football-predict.md](references/football-predict.md), the dated signals used,
and the uncertainty. Treat current club, lineup, injuries, and form as
point-in-time facts requiring fresh verification.

## Delivery

Local files are the default. Drive upload/share, Page publication, or another
remote write requires current authorization for the exact operation, target,
and audience. Research approval alone does not authorize publication.
