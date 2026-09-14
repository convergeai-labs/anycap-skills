# AnyCap MCP runtime routes

Choose exactly one proven transport. A guessed domain, old release note,
package name, localhost process, DNS record, or `/healthz` response
does not prove an MCP client can authenticate and call a tool.

| Evidence and intent | Route | Availability proof | Authentication boundary |
| --- | --- | --- | --- |
| Installed CLI exposes `anycap mcp` and the user wants a local client | CLI-embedded stdio | `anycap mcp --help`, then live handshake | AnyCap local credential runtime; never copy a remote OAuth token |
| Registry read-back proves `@anycap/mcp` is published, or the user explicitly requests its checked-out RC | package stdio | registry version + packed install smoke, or absolute local RC entry point | package auth tools and CLI-compatible local credential store |
| User supplies a Hosted MCP URL or deployment evidence | Hosted HTTP | HTTPS MCP endpoint + metadata + live handshake | endpoint OAuth/Bearer contract; adapter forwards bearer and AnyCap Server validates it |
| User supplies a configured gateway profile (their own hosted route) | gateway profile | current client/gateway profile + live handshake | client/gateway profile; no direct database or internal bypass |

The two stdio variants are alternatives under one local route. `@anycap/mcp` is
an MCP server package, not an HTTP client and not a wrapper around Hosted MCP.
Do not recommend `npx -y @anycap/mcp` until the npm registry, installed tarball,
and a real stdio host smoke prove the released package. If no row is proven,
stop with `anycap_mcp_route_gap`.

## Client configuration

Use the client-specific config surface, but preserve the transport contract:

```json
{
  "command": "anycap",
  "args": ["mcp"]
}
```

Add repeatable `--allow-root` arguments only for the narrow absolute directories
whose local media the MCP call must read. Do not commit a personal absolute path
to shared client configuration; prefer a user-local override.

For an explicitly requested checked-out npm RC, use `node` plus the absolute
`dist/index.js` path after its build passes. The post-publication shape uses
`npx -y @anycap/mcp`, but only after the publication proof above.

For Hosted HTTP, configure only the user-supplied HTTPS URL ending in `/mcp`.
Let an OAuth-capable client follow the `WWW-Authenticate` protected-resource
metadata challenge. Do not paste bearer tokens into shared config files. Opening
`/mcp` in a browser or issuing an unauthenticated `GET` is not a protocol smoke;
the adapter's MCP operation is authenticated JSON-RPC over `POST`.

## Authentication decisions

- CLI-embedded stdio reloads AnyCap local credentials. Prefer its explicit MCP
  auth tools when present; an external `anycap login` may also update the shared
  local store without copying a secret into client config.
- Package stdio must start without auto-login. Discover its live auth tools,
  then use status -> login -> human browser completion -> poll. Logout removes
  only its local persistent credential; it does not revoke a remote credential
  or remove a process environment variable.
- Hosted HTTP advertises protected-resource metadata and challenges for a bearer.
  The adapter's possession check is not final authorization: AnyCap Server
  remains the identity, feature-access, rate-limit, and business-policy boundary.
- A gateway profile's authentication belongs to its declared client profile. Never
  move its credential to another route.

## Protocol workflow

1. Freeze `route | client | redacted command/endpoint/profile | environment | availability claim | allowed side effects`.
2. Prove only the selected route's launch, registry/deployment, and auth boundary.
3. Run `initialize`, retain negotiated protocol/session details required by the
   client, then run `tools/list`.
4. Treat returned names, schemas, and annotations as the current contract; do
   not rely on remembered tool counts.
5. Call the smallest status/discovery/read tool that proves business routing.
   Side effects require the exact operation, target, and acceptance criteria.
6. Read back the result and report each availability layer separately.

## Public release gate

For Hosted MCP, a new public domain is necessary but insufficient. Report
`public_release_gap` until all of these are current:

1. The public hostname has DNS, trusted TLS, and routes to the intended runtime;
   `PublicURL`/resource metadata resolve back to the exact public `/mcp` URL.
2. OAuth issuer, audience, scopes, redirect/client registration, and a real
   supported client's login flow are verified without exposing credentials.
3. Authenticated `initialize`, `tools/list`, and a minimum read-only business
   call succeed through the public route; one explicitly authorized capability
   call proves the claimed non-read-only surface when that claim is required.
4. AnyCap Server feature access, rate limits, dependency health, request IDs,
   logs/alerts, owner, rollback identity, and client-facing documentation are
   established for the target environment.

The npm package has a separate publication gate: version/provenance/permissions,
packed install, supported Node runtime, real stdio client smoke, registry
read-back, and synchronized documentation. Hosted readiness never proves npm
publication, and npm publication never proves Hosted readiness.

## Failure classification

| Stage | Record | Do not do |
| --- | --- | --- |
| launch/connect | command or locator plus transport error | silently switch routes |
| auth challenge | status, metadata locator, missing scope/audience | print or broaden credentials |
| initialize | protocol/session error | call tools before negotiation |
| tools/list | live list/schema gap | reuse a remembered schema |
| tools/call | tool, redacted input, structured error/request reference | blind cross-model or cross-endpoint retry |

For a configured gateway profile returning HTTP 401 during `initialize`:

- if the same credential succeeds against another declared profile, report
  `profile_scope_denied` for this profile;
- otherwise report `token_invalid_or_expired_or_scope_unknown`;
- record `tools_list: not_run`;
- block retry until a confirmed credential/profile-scope change, then retry at
  most once;
- do not fall back to another route or lower-level endpoint to bypass auth.

Completion requires a live handshake, live tool discovery, and one
route-appropriate read-back. State the highest proven layer:
`implemented | installed/published | reachable | authenticated | business-call verified`.
