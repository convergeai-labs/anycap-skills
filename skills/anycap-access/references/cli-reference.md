# AnyCap CLI discovery reference

Use this page only when a narrower operation reference does not answer the
question. The installed binary and its live schemas are authoritative.

## Discover the current surface

```bash
anycap --help
anycap status
anycap <capability> --help
anycap <capability> models
anycap <capability> models <model-id> schema --operation <operation> --mode <mode>
```

Run `status` only when authentication or endpoint state is unknown. Inspect one
capability and one selected model/mode rather than dumping the full catalog.

## Stable operating rules

- Prefer JSON output for automation and parse only fields needed by the next step.
- Use explicit local output paths for generated or downloaded artifacts.
- Treat model IDs, modes, fields, limits, prices and providers as mutable.
- Preserve structured `error`, `message`, `hint` and `request_id` when returned.
- Do not print credentials, full headers, cookies or unrelated response payloads.
- A local generation request does not authorize Drive/Page publication.

If the live command differs from a reference, record the observed help/schema
and follow the live contract. Do not patch around a missing capability by
calling an undocumented endpoint.
