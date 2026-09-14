# Site Audit Evidence

Use this contract when the task asks for a measured website or SEO audit rather than planning from keywords alone.

## Local-first evidence

1. Record the target URL, final redirected URL, capture time, timezone, viewport/device mode, and authentication state.
2. Save crawl/search output and any measurement reports in a dated local workspace before interpretation.
3. Keep raw artifacts separate from summaries so another reviewer can reproduce the claim.
4. Upload, publish, rewrite repository references, or delete local artifacts only when the user explicitly requests that separate operation.

Do not make OSS or another public object store a prerequisite for diagnosis. A local path is a valid evidence location.

## Measurement selection

- Use the current AnyCap crawl/search surface for content, page structure, internal links, and live SERP evidence.
- Use project-provided Lighthouse, browser, or SEO rule tooling only when it is already available and the user needs measured technical output.
- Record tool version, mode, URL, and timestamp for every numeric result.
- Distinguish lab measurements from field data. Lighthouse desktop is not proof of mobile or real-user Core Web Vitals.
- Treat a rule engine finding as a lead to verify, not automatically as a defect.

## Claim discipline

Classify each important finding:

- **Observed:** present in saved crawl/browser/measurement output.
- **Inferred:** explanation supported by observed evidence and current code/config.
- **Unknown:** blocked by authentication, robots, rendering, sampling, missing field data, or unavailable tooling.

Never infer an indexation, ranking, or conversion outcome solely from one Lighthouse score or one crawler response.

## Minimum output

Include:

- scope and evidence timestamp;
- tested URLs and device/mode;
- raw artifact paths;
- findings grouped by crawl/index/render, content/intent, structured data, page experience, and trust/evidence;
- severity, confidence, and the exact observation behind each finding;
- gaps and the next measurement needed;
- explicit note when upload, publication, or cleanup was not performed.
