from streamtex import *  # noqa: F403
from streamtex.styles import Style as ns
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    title = s.project.titles.slide_title + s.center_txt
    subtitle = s.project.titles.subtitle
    content = s.project.titles.body
    emphasis = s.project.titles.body + s.bold + s.project.colors.primary
    key = s.project.titles.body + s.bold
    code_inline = s.project.titles.body + s.text.colors.lime
    note = s.project.titles.caption
    note_box = s.project.titles.body + ns(
        "font-size: 0.85em; padding: 16px 20px; "
        "border-left: 4px solid #F39C12; "
        "background: rgba(243, 156, 18, 0.08); "
        "border-radius: 0 8px 8px 0;",
        "note_box_tools",
    )
    note_label = s.project.titles.subtitle + ns(
        "text-transform: uppercase; letter-spacing: 1px;",
        "note_label_tools",
    )
    note_tool = s.project.titles.body + s.bold + s.project.colors.primary


bs = BlockStyles


def _note_box(notes):
    """Render a tool-variants note box."""
    with st_block(bs.note_box):
        st_write(bs.note_label, "Tool-specific variants")
        st_space(size=1)
        for i, (tool, desc) in enumerate(notes):
            st_write((bs.note_tool, tool), (bs.content, f" — {desc}"))
            if i < len(notes) - 1:
                st_space(size=0.5)


def build():
    st_write(bs.title, "How to Control Agent Tools?", tag=t.div, toc_lvl="2")
    st_space(size=2)

    st_write(
        bs.content,
        "The agent loop discovers and merges all available tools before each LLM call. "
        "But you rarely want an agent to have unrestricted access to every tool. "
        "This section covers the five mechanisms that let you control "
        "which tools are available, when they can run, and what happens around them.",
    )
    st_space(size=3)

    # ── 1. Permission Modes ──
    st_write(
        bs.subtitle, "1. Permission Modes",
        tag=t.div, toc_lvl="+1",
    )
    st_space(size=1)

    st_write(
        bs.content,
        "Most agentic tools offer permission modes that act as the first gate "
        "on tool execution. The typical tiers are:",
    )
    st_space(size=1)

    with st_list(list_type=lt.unordered, li_style=bs.content) as li:
        with li.item():
            st_write(
                (bs.emphasis, "Supervised mode"),
                (bs.content, " — every tool call that could modify the system "
                 "triggers a user approval prompt."),
            )
        with li.item():
            st_write(
                (bs.emphasis, "Read-only / Plan mode"),
                (bs.content, " — the agent can only read and search; "
                 "all write/execute tools are blocked."),
            )
        with li.item():
            st_write(
                (bs.emphasis, "Autonomous mode"),
                (bs.content, " — all tool calls are approved automatically. "
                 "Useful for CI pipelines or trusted automation."),
            )
    st_space(size=1)

    _note_box([
        ("Claude Code", "Default (supervised), Plan (read-only), Auto-accept (autonomous). "
         "Configured via CLI flags or settings.json."),
        ("OpenAI Codex CLI", "Suggest (supervised), Auto-edit (files only), Full-auto (autonomous). "
         "Configured via CLI flags."),
        ("Cursor", "Always autonomous within IDE — no explicit permission modes."),
        ("GitHub Copilot", "Always autonomous within IDE — no explicit permission modes."),
    ])
    st_space(size=3)

    # ── 2. Tool Allow/Deny Lists ──
    st_write(
        bs.subtitle, "2. Tool Allow/Deny Lists",
        tag=t.div, toc_lvl="+1",
    )
    st_space(size=1)

    st_write(
        bs.content,
        "Beyond global permission modes, some agents let you fine-tune "
        "which specific tools are available via allow/deny lists in their configuration file:",
    )
    st_space(size=1)

    with st_list(list_type=lt.unordered, li_style=bs.content) as li:
        with li.item():
            st_write(
                (bs.key, "Allow list (whitelist)"),
                (bs.content, " — only these tools can be invoked. All others are blocked."),
            )
        with li.item():
            st_write(
                (bs.key, "Deny list (blacklist)"),
                (bs.content, " — these tools are explicitly forbidden. All others are allowed."),
            )
    st_space(size=1)
    st_write(
        bs.note,
        "If both lists are present, the allow list typically takes precedence.",
    )
    st_space(size=1)

    _note_box([
        ("Claude Code", "allowedTools / disallowedTools in .claude/settings.json."),
        ("OpenAI Codex CLI", "allowList in codex.json (deny list not supported)."),
        ("Cursor", "No tool allow/deny lists — tool access is managed by the IDE."),
        ("GitHub Copilot", "No tool allow/deny lists."),
    ])
    st_space(size=3)

    # ── 3. MCP Server Configuration ──
    st_write(
        bs.subtitle, "3. MCP Server Configuration",
        tag=t.div, toc_lvl="+1",
    )
    st_space(size=1)

    st_write(
        bs.content,
        "MCP tools are not built into the agent — they are discovered dynamically "
        "from external servers declared in a configuration file. "
        "Adding or removing a server entry directly controls "
        "which external capabilities the agent can use.",
    )
    st_space(size=1)

    st_code(
        bs.content,
        code="""\
// Example: MCP server configuration (JSON format)
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": { "GITHUB_TOKEN": "ghp_..." }
    },
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": { "DATABASE_URL": "postgresql://..." }
    }
  }
}""",
        language="json",
    )
    st_space(size=1)

    st_write(
        bs.content,
        "Each server exposes its own set of tools via the MCP "
        "tools/list endpoint at startup. "
        "The orchestrator merges these with built-in tools into a single schema "
        "sent to the LLM. To remove a capability, simply remove "
        "the server entry — the tools vanish from the next agent loop iteration.",
    )
    st_space(size=1)

    _note_box([
        ("Claude Code", "MCP config in .mcp.json (project root). Supports stdio and SSE transports."),
        ("OpenAI Codex CLI", "No MCP support yet."),
        ("Cursor", "MCP servers configured via Settings > MCP. Supports stdio transport."),
        ("GitHub Copilot", "MCP servers configured via settings. Limited transport support."),
    ])
    st_space(size=3)

    # ── 4. Hooks: Pre/Post Tool Middleware ──
    st_write(
        bs.subtitle, "4. Hooks: Pre/Post Tool Middleware",
        tag=t.div, toc_lvl="+1",
    )
    st_space(size=1)

    st_write(
        bs.content,
        "Hooks are shell commands that execute before or after a tool call. "
        "They act as programmable middleware — you can log, validate, transform, "
        "or block any tool invocation.",
    )
    st_space(size=1)

    with st_list(list_type=lt.unordered, li_style=bs.content) as li:
        with li.item():
            st_write(
                (bs.key, "Pre-execution hooks"),
                (bs.content, " — run before the tool executes. "
                 "If the hook exits with a non-zero status, the tool call is blocked "
                 "and the error is fed back to the LLM."),
            )
        with li.item():
            st_write(
                (bs.key, "Post-execution hooks"),
                (bs.content, " — run after the tool completes. "
                 "Useful for logging, auditing, or triggering side effects."),
            )
        with li.item():
            st_write(
                (bs.key, "Matcher / filter"),
                (bs.content, " — selects which tools trigger the hook. "
                 'Typically by tool name, glob pattern, or wildcard.'),
            )
    st_space(size=1)

    st_write(
        bs.content,
        "The hook process receives the tool name, parameters, and context via stdin (JSON). "
        "This makes hooks a powerful control point: you can enforce policies like "
        '"no destructive commands", "no writes outside src/", '
        'or "require approval for database mutations".',
    )
    st_space(size=1)

    _note_box([
        ("Claude Code", "PreToolUse / PostToolUse hooks in .claude/settings.json. "
         "Matcher supports tool names, globs, and wildcards."),
        ("OpenAI Codex CLI", "No hook system."),
        ("Cursor", "No hook system."),
        ("GitHub Copilot", "No hook system."),
    ])
    st_space(size=3)

    # ── 5. Sub-Agent Tool Scoping ──
    st_write(
        bs.subtitle, "5. Sub-Agent Tool Scoping",
        tag=t.div, toc_lvl="+1",
    )
    st_space(size=1)

    st_write(
        bs.content,
        "When the orchestrator spawns a sub-agent, "
        "it can restrict which tools the child agent has access to. "
        "This is controlled by selecting a predefined agent profile with its own toolset:",
    )
    st_space(size=1)

    with st_list(list_type=lt.unordered, li_style=bs.content) as li:
        with li.item():
            st_write(
                (bs.emphasis, "Full-access profile"),
                (bs.content, " — full toolset (file I/O, shell, web, etc.)"),
            )
        with li.item():
            st_write(
                (bs.emphasis, "Read-only profile"),
                (bs.content, " — read and search tools only. "
                 "Cannot write files or run commands."),
            )
        with li.item():
            st_write(
                (bs.emphasis, "Planning profile"),
                (bs.content, " — read-only + planning tools. "
                 "Designed for architecture and design work without side effects."),
            )
    st_space(size=1)

    st_write(
        bs.content,
        "This creates a least-privilege model for sub-agents: "
        "a research agent only needs to read, a code-review agent only needs to read and comment, "
        "and only the main orchestrator or a dedicated executor agent gets write access.",
    )
    st_space(size=1)

    _note_box([
        ("Claude Code", "Agent tool with subagent_type parameter: general-purpose, Explore, Plan. "
         "Sub-agents inherit parent hooks and permissions."),
        ("OpenAI Codex CLI", "No sub-agent support."),
        ("Cursor", "No sub-agent support."),
        ("GitHub Copilot", "No sub-agent support."),
    ])
    st_space(size=3)

    # ── 6. Project Rules — Behavioral Directives ──
    st_write(
        bs.subtitle, "6. Project Rules — Behavioral Directives",
        tag=t.div, toc_lvl="+1",
    )
    st_space(size=1)

    st_write(
        bs.content,
        "The previous mechanisms operate at the infrastructure level — they physically "
        "enable or block tool calls. Project rules operate at the behavioral level: "
        "they shape the LLM's intent so it never attempts certain tool calls in the first place.",
    )
    st_space(size=1)

    st_code(
        bs.content,
        code="""\
# Project Rules — Example directives

## Tool Usage
- NEVER use shell to run `rm -rf`, `git push --force`, or `docker rm`
- ALWAYS use the file-edit tool instead of shell with `sed` for modifications
- NEVER call production MCP tools without user confirmation
- Prefer dedicated search tools over shell-based grep""",
        language="markdown",
    )
    st_space(size=1)

    st_write(
        bs.content,
        "These directives are injected into the system prompt at conversation start. "
        "The LLM reads them as instructions and follows them when generating tool calls. "
        "This is a soft control — it relies on the model's instruction-following ability "
        "rather than a hard gate. For critical restrictions, combine project rules "
        "with hooks or permission settings as defense in depth.",
    )
    st_space(size=1)

    _note_box([
        ("Claude Code", "CLAUDE.md in the project root. Loaded automatically into system prompt."),
        ("OpenAI Codex CLI", "AGENTS.md in the project root. Same mechanism."),
        ("Cursor", ".cursorrules in the project root. Loaded into system prompt."),
        ("GitHub Copilot", ".github/copilot-instructions.md. Loaded into system prompt."),
    ])
    st_space(size=3)

    # ── Summary ──
    st_write(bs.subtitle, "Control Layers Summary", tag=t.div, toc_lvl="+1")
    st_space(size=1)

    st_write(
        bs.content,
        "The six mechanisms form a layered defense model, from soft to hard:",
    )
    st_space(size=1)

    layers = [
        ("Project rules", "Soft",
         "Shapes LLM intent — prevents the model from attempting unwanted tool calls"),
        ("Permission modes", "Hard",
         "Global gate — controls whether write/execute tools require approval"),
        ("Allow/Deny lists", "Hard",
         "Per-tool gate — whitelist or blacklist specific tools"),
        ("MCP configuration", "Hard",
         "Discovery gate — tools that are not declared simply do not exist"),
        ("Hooks", "Hard",
         "Execution gate — intercept, validate, or block any tool call at runtime"),
        ("Sub-agent scoping", "Hard",
         "Delegation gate — child agents get a restricted toolset"),
    ]

    with st_list(list_type=lt.ordered, li_style=bs.content) as li:
        for name, kind, desc in layers:
            with li.item():
                st_write(
                    (bs.key, f"{name} "),
                    (bs.emphasis, f"[{kind}]"),
                    (bs.content, f" — {desc}"),
                )
    st_space(size=1)

    st_write(
        bs.content,
        "Not all agents support every layer. Claude Code is the most complete "
        "(all 6 layers). Codex CLI supports 3 (rules, permissions, allow lists). "
        "Cursor and Copilot support 2 (rules, MCP).",
    )
