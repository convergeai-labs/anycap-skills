# Annotation runtime and session access

## Command Quick Reference

```bash
# Blocking -- opens browser, waits for Done click, outputs result
anycap annotate <target> [-o output.png]

# Non-blocking -- starts background server, returns session info
anycap annotate <target> --no-wait [-o output.png]

# Poll for result after human confirms done
anycap annotate poll --session <session_id>

# Stop background server
anycap annotate stop --session <session_id>

# List all active sessions (useful for recovery after context loss)
anycap annotate list
```

`<target>` is auto-detected by content: image file, URL (`http://` or `https://`), video file, or audio file.

### Key Flags

| Flag | Description |
|------|-------------|
| `--no-wait` | Non-blocking mode (recommended for agents) |
| `-o, --output` | Save annotated image to this path |
| `--port <port>` | Bind to a fixed port (default: random) |
| `--bind <addr>` | Bind address (default: `127.0.0.1`) |

**Tip:** Use `--port` with a consistent value (e.g., `--port 8888`) across sessions. The browser stores each user's display name in localStorage, which is scoped by origin (host + port). A fixed port means returning collaborators are recognized automatically without re-entering their name.

### Browser Auto-Open

Both blocking and non-blocking modes automatically attempt to open the annotation URL in the default browser. In headless environments (SSH, container), the CLI prints the URL to stderr instead. No error is raised.

### Presenting to the Human -- Guidelines

When presenting an annotation session to the human, adapt your message based on context. Key points to communicate:

- **Browser auto-open**: On desktop, the page opens automatically -- acknowledge this ("the review page should already be open"). In headless/SSH, share the URL and tell them how to access it.
- **Always mention Done**: Tell the human to click **Done** when finished. This is how feedback gets saved.
- **Recording for URL mode**: Emphasize recording (Rec button) because URL mode cannot export an annotated screenshot. The recording is the primary artifact.
- **Multi-user**: If multiple reviewers will participate, mention real-time collaboration and that each person can save independently. **Exception: URL/iframe mode is single-user** (recording is the primary feedback artifact, and multiple users' cursors would make it confusing).
- **Headless access**: When using `--bind 0.0.0.0`, share the URL with the actual host IP. If behind SSH, suggest port forwarding.
- **What to annotate**: Briefly describe what tools are available (Rect, Arrow, Point, Freehand) and that each annotation can have a text label.

Do NOT use canned messages. Compose naturally based on the situation (what you just generated/modified, whether it is desktop or headless, single or multi-reviewer).

### Headless / Remote Access

When running in a headless environment (SSH, container, cloud VM), the human cannot access `127.0.0.1` directly. Use `--bind` and `--port` to make the annotation server accessible:

```bash
# Bind to all interfaces on a fixed port
anycap annotate screenshot.png --no-wait --bind 0.0.0.0 --port 8888
```

The human can then access the annotation UI via:

- **Direct access:** `http://<server-ip>:8888` (if the port is exposed)
- **SSH port forward:** `ssh -L 8888:localhost:8888 user@host`, then open `http://localhost:8888`
- **Container port mapping:** `docker run -p 8888:8888 ...`, then open `http://localhost:8888`
- **Reverse proxy:** expose through nginx, Caddy, or any reverse proxy with a path prefix

Always use `--port` with a fixed number in headless environments so the URL is predictable and forwardable. Keep the default `127.0.0.1` binding unless the current user explicitly authorizes network exposure. Before `--bind 0.0.0.0`, explain the reachable interface, target artifact, expected reviewers, and shutdown plan; never expose secrets or private pages without access controls.

### Reverse Proxy Compatibility

The annotation UI works behind reverse proxies with arbitrary path prefixes. All asset, API, and WebSocket URLs are resolved relative to the page URL, so setups like the following work out of the box:

```
https://yourserver.com/tools/annotate/  ->  http://localhost:8888/
```

If your proxy passes access-control query parameters (for example,
`?access_key=...`), they are preserved on all internal requests automatically.
No additional configuration is needed on the annotation server side.
