# AnyCap local-agent daemon

## Agent Daemon (Feishu Chat)

When the human wants to chat with the current local coding agent from Feishu, start the AnyCap Feishu daemon for them. Treat these as trigger phrases:

- "用飞书跟你聊天"
- "开启飞书 IM 模式"
- "把你接到我的飞书 bot 上"
- "用 AnyCap 启动飞书机器人"
- "用飞书跟当前 agent 聊天"
- "我要使用飞书连接本地codex"
- "用飞书连接本地 Codex"
- "把飞书接到本地 Codex"
- "用飞书连接本地 Claude Code"
- "把飞书接到本地 Claude Code"
- "用飞书连接本地 Cursor"
- "把飞书接到本地 Cursor"
- "用飞书接入本地 agent"
- "把飞书接到本地 agent"
- "connect Feishu to local Codex"
- "connect Feishu to local Claude Code"
- "connect Feishu to local Cursor"
- "connect Feishu to local agent"
- "start AnyCap Feishu daemon"

Do not explain daemon internals first. Execute the setup flow below, asking only for missing required information.

Always remind the human to verify their **personal Feishu app bot** setup before starting the local connection, even when local Feishu credentials already exist. Stored credentials only prove App ID/App Secret are available locally; they do not prove the bot capability, event subscription, message event, permissions, or app release are configured correctly.

Ask the human to confirm these Feishu Open Platform steps and come back when done:

1. Create an internal/self-built app in Feishu Open Platform.
2. Enable the app's bot/robot capability.
3. In event subscriptions, choose long connection event delivery. Do not ask the human to configure a public webhook for the normal local setup.
4. Subscribe to the message receive event, shown in Feishu as "receive message" / `im.message.receive_v1`.
5. In permissions, use batch import for the tenant scopes below, then publish or release the app version so the permissions take effect.
6. Copy the App ID and App Secret locally. The human must never paste the App Secret into chat.

Recommended tenant scopes for chat plus Feishu resource read/write:

```json
{
  "scopes": {
    "tenant": [
      "bitable:app",
      "bitable:app:readonly",
      "docx:document",
      "docx:document.block:convert",
      "docx:document:create",
      "docx:document:readonly",
      "docx:document:write_only",
      "im:chat:readonly",
      "im:message",
      "im:message.group_at_msg:readonly",
      "im:message.p2p_msg:readonly",
      "sheets:spreadsheet",
      "sheets:spreadsheet.meta:read",
      "sheets:spreadsheet.meta:write_only",
      "sheets:spreadsheet:create",
      "sheets:spreadsheet:read",
      "sheets:spreadsheet:readonly",
      "sheets:spreadsheet:write_only",
      "wiki:node:copy",
      "wiki:node:create",
      "wiki:node:move",
      "wiki:node:read",
      "wiki:node:retrieve",
      "wiki:node:update",
      "wiki:wiki",
      "wiki:wiki:readonly"
    ]
  }
}
```

If Feishu still refuses bot replies, ask the human to search permissions for "send as bot" / "以机器人身份发送消息" and add the matching permission, commonly `im:message:send_as_bot`. If image or file downloads fail, ask them to add the message resource download permission shown by their console, commonly `im:resource`.

The human's Feishu app setup checklist is:

- created in Feishu Open Platform
- robot capability enabled
- long connection event delivery enabled
- message receive permissions granted
- app version published after permission/event changes
- App ID and App Secret available locally

Use the current working directory as `--workspace` unless the human provides a different repository path.

Infer the local agent from the current runtime. The user-facing `anycap connect feishu` path currently supports Codex, Claude Code, and Cursor:

- Codex runtime -> `--agent codex`
- Claude Code runtime -> `--agent claude-code`
- Cursor runtime -> `--agent cursor`
- If unsure, ask one concise question: "Use Codex, Claude Code, or Cursor as the local agent?"

Read Feishu credentials from the local daemon credential store first:

- stored by `anycap connect credentials set feishu`
- file location: AnyCap config dir, mode 0600

Reason: if the human exports `FEISHU_APP_ID` and `FEISHU_APP_SECRET` after the coding agent process has already started, this agent will not inherit those variables. The shared local credential file is the stable bridge between the human's terminal and the agent-started daemon.

Check credential status without printing secrets:

```bash
anycap connect credentials show feishu
```

If credentials are missing, ask the human to run this in their own terminal and tell you when it is done. If credentials already exist, still ask the human to confirm the Feishu Open Platform checklist above before starting the local connection. The human handles Feishu console setup and local credential storage; the agent starts the local Codex/Claude/Cursor connection after the human confirms setup is complete. Never ask the human to paste App Secret values into chat. Never write App Secret values into docs, code, logs, memory files, command history, or final summaries. Do not echo secrets back to the human.

Human terminal setup:

```bash
anycap connect credentials set feishu --app-id <FEISHU_APP_ID> --app-secret <FEISHU_APP_SECRET>
```

After the human says this is done, the agent continues the setup. Do not ask the human to run `anycap connect feishu` in the normal flow.

```bash
anycap status
```

If the CLI is not authenticated, run:

```bash
anycap login
```

Then start the local Feishu agent on the target repository:

```bash
anycap connect feishu --agent codex --workspace /path/to/repo
```

Claude Code is also supported as the local executor:

```bash
anycap connect feishu --agent claude-code --workspace /path/to/repo
```

Cursor Agent is also supported as the local executor:

```bash
anycap connect feishu --agent cursor --workspace /path/to/repo
```

The user-facing `connect feishu --agent cursor` path enables Cursor Agent `--force` automatically so URL access and shell-backed network checks can run non-interactively. Always tell the human that this lets Cursor Agent execute local commands and network requests unless Cursor explicitly denies them.

Codex is the default local executor. Before starting `connect feishu --agent codex`, tell the human that the default Codex mode is safe, which maps to Codex `--full-auto`.

If the human says they need MCP/plugin access, such as Computer Use, Figma, Canva, or custom MCP servers, ask whether to start the daemon with:

```bash
--codex-exec-mode danger-full-access
```

If they say yes, start the daemon with that explicit flag. Otherwise, keep the default safe mode.

For Claude Code, `--claude-permission-mode acceptEdits` is the default. If the human wants the Feishu bot to make Claude Code call AnyCap capabilities, access public internet APIs, or access local-network/VPN-only resources, use Claude Code's broader permission/tool flags, for example:

```bash
--claude-permission-mode bypassPermissions
--claude-allowed-tools Read,Edit,Bash
```

Reason: the daemon runs Claude Code non-interactively with no TTY for permission prompts. `acceptEdits` can be enough for editing, but shell commands and networked CLI calls may fail or block unless the required tools are explicitly allowed or permissions are bypassed.

For Cursor Agent, the user-facing connect path runs `cursor-agent -p --output-format json --trust --force`. Use `--cursor-model <model>` for explicit model selection. The lower-level `agent daemon start --executor cursor` path still requires explicit `--cursor-force` when force-allow command behavior is desired.

After startup, verify which local machine is currently connected:

```bash
anycap connect status feishu
```

Then tell the human to go back to Feishu and send a normal message to their personal bot. Use a concise success message like:

```text
飞书机器人已经连上当前本地 agent。现在去飞书给你的 personal bot 发普通消息即可。
```

Do not tell the human to:

- start `agent runners serve` manually
- copy a `runner_id`
- edit server env to bind bot -> runner
- use `/bind` as the normal setup flow
- configure the server-side shared Feishu bot unless they are explicitly debugging a legacy deployment

Helpful commands:

```bash
anycap connect status feishu
anycap agent runners list
```

Main notes:

- `anycap connect stop feishu` stops the local background connection for Feishu.
- If Feishu replies that the local agent is offline, restart the local daemon on the machine that should receive the chat.
- The local daemon now owns the Feishu long connection and sends final agent replies through the same personal bot. The server still stores conversation/session/mailbox state, but it does not need the user's Feishu App ID/App Secret for the normal `connect feishu` path.
- Feishu-triggered local executor sessions include an `anycap-local-session` context block. With Codex, if the human asks to continue/resume the local Codex session from Feishu, AnyCap scans local Codex session metadata, picks the most recent non-`exec` session for the daemon workspace, resumes it by explicit session id, and persists that thread as `executor_ref` for later Feishu turns. When the human asks how to open/view/recover the conversation on their Mac, reply with the precise local command using the current `executor_ref` or, if provided, `local_resume_ref`, for example `cd "/path/to/repo" && codex resume <id>`. Do not suggest `codex resume --last` unless no exact `executor_ref` or `local_resume_ref` is available.
- Default Codex mode for Feishu is safe, which maps to Codex `--full-auto`.
- If the human needs MCP/plugin access, such as Computer Use, Figma, Canva, or custom MCP servers, ask whether to start with `--codex-exec-mode danger-full-access`, and only use it when they explicitly choose it.
- `--agent claude-code` runs Claude Code with `claude -p --output-format json` and persists Claude Code `session_id` as `executor_ref` for follow-up turns.
- For Claude Code, use `--claude-permission-mode bypassPermissions --claude-allowed-tools Read,Edit,Bash` when the Feishu bot should call AnyCap commands or reach public/internal network resources from inside Claude Code.
- `--agent cursor` runs Cursor Agent with `cursor-agent -p --output-format json --trust --force` and persists Cursor Agent `session_id` as `executor_ref` for follow-up turns.
- For Cursor Agent, use `--cursor-model <model>` for explicit model selection. Tell the human that Cursor Agent runs with `--force` on the user-facing connect path and may execute local commands or network requests unless Cursor explicitly denies them.

## Legacy / Debug Only

`anycap agent daemon ...` remains available for debugging and compatibility, but `anycap connect ...` is the primary user-facing path.

Only use this section when the human is explicitly debugging an older shared-bot deployment.

- `anycap agent runners serve` is the low-level/debug path.
- `anycap agent im-bindings ...` is only for legacy/debug flows.
- `/bind` is a legacy/debug compatibility path.
- Treat server-side shared-bot webhook/long-connection setup as legacy compatibility only, not the preferred setup path.
