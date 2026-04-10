from streamtex import *  # noqa: F403
from streamtex.styles import Style as ns
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    title = s.project.titles.slide_title + s.center_txt
    subtitle = s.project.titles.subtitle
    content = s.project.titles.body
    emphasis = s.project.titles.body + s.bold + s.project.colors.primary
    mcp = s.project.titles.body + s.bold + s.project.colors.critical
    key = s.project.titles.body + s.bold
    note_box = s.project.titles.body + ns(
        "font-size: 0.85em; padding: 16px 20px; "
        "border-left: 4px solid #F39C12; "
        "background: rgba(243, 156, 18, 0.08); "
        "border-radius: 0 8px 8px 0;",
        "note_box_concepts",
    )
    note_label = s.project.titles.subtitle + ns(
        "text-transform: uppercase; letter-spacing: 1px;",
        "note_label_concepts",
    )
    note_tool = s.project.titles.body + s.bold + s.project.colors.primary


bs = BlockStyles


def build():
    st_write(bs.title, "Q/A: What is an AI Agent?", tag=t.div, toc_lvl="1")
    st_space(size=2)

    # ── What is an AI Agent? ──
    st_write(bs.subtitle, "Definition", tag=t.div, toc_lvl="+1")
    st_space(size=1)

    st_write(
        bs.content,
        "An AI agent is a program that uses a Large Language Model (LLM) as its decision engine "
        "to accomplish tasks autonomously. Unlike a simple chatbot that only generates text, "
        "an agent can take actions in the real world: read files, run commands, search the web, "
        "communicate with external services, and even spawn other agents.",
    )
    st_space(size=2)

    # ── The 4 Pillars ──
    st_write(bs.subtitle, "The 4 Fundamental Elements", tag=t.div, toc_lvl="+1")
    st_space(size=1)

    with st_list(list_type=lt.ordered, li_style=bs.content) as l:
        with l.item():
            st_write(
                (bs.emphasis, "The Orchestrator"),
                (bs.content, " — a local process that runs the agent loop: "
                 "build context, call the LLM, dispatch actions, collect results, repeat."),
            )
        with l.item():
            st_write(
                (bs.emphasis, "The LLM"),
                (bs.content, " — a remote, stateless service that only predicts tokens. "
                 "It has no memory, no filesystem access, no side effects. "
                 "It can only suggest what to do next."),
            )
        with l.item():
            st_write(
                (bs.emphasis, "Built-in Tools"),
                (bs.content, " — local capabilities hardwired into the agent: "
                 "file operations, shell/process execution, web access, and code intelligence."),
            )
        with l.item():
            st_write(
                (bs.mcp, "MCP Tools"),
                (bs.content, " — dynamically discovered via the Model Context Protocol (JSON-RPC 2.0). "
                 "Local MCP servers (stdio) for databases, GitHub, browsers. "
                 "Remote MCP servers (SSE/HTTP) for Slack, Jira, Gmail, cloud APIs."),
            )
    st_space(size=2)

    # ── Key Principles ──
    st_write(bs.subtitle, "Key Principles", tag=t.div, toc_lvl="+1")
    st_space(size=1)

    principles = [
        ("Stateless LLM", "The LLM has zero memory between calls. "
         "The full context is rebuilt and sent with every request."),
        ("Local execution", "All actions (read, write, execute, communicate) "
         "are performed by the local orchestrator, never by the LLM itself."),
        ("Permission model", "Destructive or sensitive actions require explicit user approval "
         "before execution (permission gate)."),
        ("Dynamic tool discovery", "MCP servers expose new tools at startup via tools/list. "
         "The agent merges them with built-in tools in the schema sent to the LLM."),
        ("Recursive sub-agents", "Some agents can spawn child agents with their own loop, "
         "context, tools, and LLM calls."),
        ("Persistent memory", "Since the LLM is stateless, the agent uses files on disk "
         "(project rules, memory files) to persist knowledge across sessions."),
        ("Hooks", "Some agents support shell commands triggered before/after each tool execution — "
         "middleware for logging, validation, or automation."),
    ]

    for title, desc in principles:
        st_write((bs.key, f"{title} — "), (bs.content, desc))
        st_space(size=1)

    # ── Notes: tool-specific variants ──
    st_space(size=2)
    with st_block(bs.note_box):
        st_write(bs.note_label, "Tool-specific variants")
        st_space(size=1)
        st_write(
            (bs.note_tool, "Claude Code"),
            (bs.content, " — Tools: Read, Write, Edit, Bash, Glob, Grep, WebSearch, WebFetch. "
             "Project rules: CLAUDE.md. Memory: .claude/memory/. "
             "Hooks: PreToolUse/PostToolUse. Sub-agents: yes (Agent tool)."),
        )
        st_space(size=0.5)
        st_write(
            (bs.note_tool, "OpenAI Codex CLI"),
            (bs.content, " — Tools: shell, file_read, file_write, file_edit. "
             "Project rules: AGENTS.md. Memory: N/A (stateless). "
             "Hooks: N/A. Sub-agents: N/A."),
        )
        st_space(size=0.5)
        st_write(
            (bs.note_tool, "Cursor"),
            (bs.content, " — Tools: edit, terminal, search (IDE-integrated). "
             "Project rules: .cursorrules. Memory: N/A. "
             "Hooks: N/A. Sub-agents: N/A. MCP via settings UI."),
        )
        st_space(size=0.5)
        st_write(
            (bs.note_tool, "GitHub Copilot"),
            (bs.content, " — Tools: internal (not exposed to user). "
             "Project rules: .github/copilot-instructions.md. Memory: N/A. "
             "Hooks: N/A. Sub-agents: N/A."),
        )
