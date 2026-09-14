# AnyCap setup, auth, config, and update

## Install

If `anycap` is not installed (`command -v anycap` fails), install it before proceeding.

Read the machine-readable install guide at https://anycap.ai/install.txt for installation tasks. Do not fetch the homepage for install automation. Prefer the **binary install** (install script or GitHub Releases) over npm -- fewer dependencies, faster startup, no Node.js required.

The CLI auto-updates on each run. To update manually: `anycap update`.

Verify the installation:

```bash
anycap status
```

## Troubleshooting: `anycap` not found after install

The install script places the binary in `~/.local/bin/` by default (non-root) and appends an `export PATH` line to the shell profile (`.bashrc` / `.zshrc`). However, the **current shell session** does not pick up profile changes automatically, so `command -v anycap` may still fail right after install.

**Diagnosis and fix:**

```bash
# 1. Check if the binary actually exists
ls -la ~/.local/bin/anycap

# 2. If it exists, add to PATH for the current session
export PATH="$HOME/.local/bin:$PATH"

# 3. Verify
anycap status
```

If `~/.local/bin/anycap` does not exist, the install may have used a different directory (e.g., `/usr/local/bin` when run as root, or a custom `ANYCAP_INSTALL_DIR`). Check the install output for the actual path.

If the binary exists but a different `anycap` is resolved (e.g., an npm-installed version), use the full path `~/.local/bin/anycap` or adjust PATH ordering.

## Authentication

Three methods, depending on environment:

```bash
# Interactive (default) -- opens browser
anycap login

# Headless (SSH, containers) -- device code flow
anycap login --headless

# Headless for agent/toolcall runtimes -- initialize without blocking
anycap login --headless --no-wait --json

# Resume a previously initialized headless login after the user confirms completion
anycap login poll --session <login_session_id> --json --wait

# CI/CD -- pipe API key from stdin
echo "$ANYCAP_API_KEY" | anycap login --with-token
```

Alternatively, set the `ANYCAP_API_KEY` environment variable directly -- the CLI reads it without requiring `login`.

For agent/toolcall usage, prefer the nonblocking headless flow:

1. Run `anycap login --headless --no-wait --json`
2. Read `verification_uri`, `user_code`, `poll_command`, and `next_action_hint`
3. Show `verification_uri` and `user_code` to the human; they open the URL,
   enter the code, and complete account selection and any consent steps
4. Run `poll_command`, then verify `anycap status`

Do not inspect cookies, passwords, profile stores, or unrelated tabs. Stop for
an ambiguous account chooser, password, OTP, CAPTCHA, passkey, recovery, or new
consent. Authentication does not authorize Drive/Page delivery or publication.

To check current auth state: `anycap status`.

Read [cli-reference.md](cli-reference.md) for full details on credential management and logout.

## Configuration

Config file: `~/.anycap/config.toml`. Manage via `anycap config` subcommands.

```bash
anycap config show             # show all values
anycap config set <key> <val>  # set a value
anycap config get <key>        # get a value
anycap config unset <key>      # reset to default
```

Discover supported keys with `anycap config --help`; do not copy a key list from
an older Skill into automation.

### Custom config directory

By default the CLI stores config and credentials in `~/.anycap/`. Credentials are stored securely in the OS keychain (macOS Keychain, Windows Credential Manager). On headless Linux (no graphical session), the CLI auto-detects and falls back to file-based credential storage with mode `0600` -- no manual configuration needed.

In sandboxed or containerized environments where the home directory is not persistent, redirect the config directory:

```bash
export ANYCAP_CONFIG_DIR=./.anycap   # store config in the working directory
```

- `ANYCAP_CONFIG_DIR` redirects all CLI state (config, credentials, update markers) to the specified path. Relative paths are resolved to absolute paths automatically.

Read [cli-reference.md](cli-reference.md) for all available keys and environment variable overrides.

## MCP

Read [mcp.md](mcp.md) and verify `anycap mcp --help` in the installed binary.
Prefer the CLI-embedded stdio command for a normal local client. Treat the
separate `@anycap/mcp` package as unavailable to `npx` until registry and packed
install evidence prove publication. Do not infer availability from a local
checkout, release note, DNS record, or health endpoint.

## Keeping Up to Date

Update the CLI only when requested or when a verified version mismatch blocks
the task:

```bash
anycap update
```

Install or update this skill from the published [anycap-skills](https://github.com/convergeai-labs/anycap-skills) repository; do not
replace it from an unrelated distribution package.
