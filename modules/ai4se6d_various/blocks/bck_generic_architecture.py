from streamtex import *  # noqa: F403
from streamtex.styles import Style as ns
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from blocks._diagram_export import show_diagram


class BlockStyles:
    title = s.project.titles.slide_title + s.center_txt
    subtitle = s.project.titles.subtitle
    content = s.project.titles.body
    note_box = s.project.titles.body + ns(
        "font-size: 0.85em; padding: 16px 20px; "
        "border-left: 4px solid #2EC4B6; "
        "background: rgba(46, 196, 182, 0.08); "
        "border-radius: 0 8px 8px 0;",
        "note_box_arch",
    )
    note_label = s.project.titles.subtitle + ns(
        "text-transform: uppercase; letter-spacing: 1px;",
        "note_label_arch",
    )
    note_tool = s.project.titles.body + s.bold + s.project.colors.primary


bs = BlockStyles


def build():
    st_write(bs.title, "How is an Agent Architected?", tag=t.div, toc_lvl="2")
    st_space(size=2)

    # ── Overview ──
    st_write(bs.subtitle, "High-Level Overview", tag=t.div, toc_lvl="+1")
    st_space(size=1)
    st_write(bs.content, "The complete agent architecture at a glance. Each component is detailed below.")
    st_space(size=1)
    show_diagram("generic_overview.mmd", height=1000, key="gen_overview")
    st_space(size=3)

    # ── Agent Loop Detail ──
    st_write(bs.subtitle, "Detail: Agent Loop", tag=t.div, toc_lvl="+1")
    st_space(size=1)
    st_write(
        bs.content,
        "The core cycle: build context from history + tool results + memory, "
        "call the LLM, dispatch the response (text → done, tool_call → execute, agent → spawn).",
    )
    st_space(size=1)
    show_diagram("generic_agent_loop.mmd", height=900, key="gen_loop")
    st_space(size=3)

    # ── Tool Execution Detail ──
    st_write(bs.subtitle, "Detail: Tool Execution", tag=t.div, toc_lvl="+1")
    st_space(size=1)
    st_write(
        bs.content,
        "When the LLM returns a tool_call: permission gate → pre-hook → router "
        "(built-in or MCP) → execute → post-hook → reinject result into context.",
    )
    st_space(size=1)
    show_diagram("generic_tool_execution.mmd", height=1200, key="gen_tools")
    st_space(size=3)

    # ── Sub-Agents Detail ──
    st_write(bs.subtitle, "Detail: Sub-Agent Spawning", tag=t.div, toc_lvl="+1")
    st_space(size=1)
    st_write(
        bs.content,
        "The Agent tool forks a new process with its own loop, context, tools, and LLM calls. "
        "Sub-agents run in parallel, can use different models, and may spawn recursively.",
    )
    st_space(size=1)
    show_diagram("generic_subagents.mmd", height=1000, key="gen_subs")
    st_space(size=3)

    # ── Variants by Tool ──
    st_write(bs.subtitle, "Variants by Tool", tag=t.div, toc_lvl="+1")
    st_space(size=1)
    st_write(
        bs.content,
        "The diagrams above show the most complete architecture (Claude Code). "
        "Other agentic tools implement subsets of this architecture:",
    )
    st_space(size=1)

    with st_block(bs.note_box):
        st_write(bs.note_label, "What changes per tool")
        st_space(size=1)
        with st_list(list_type=lt.unordered, li_style=bs.content) as li:
            with li.item():
                st_write(
                    (bs.note_tool, "OpenAI Codex CLI"),
                    (bs.content, " — Single-loop agent, no sub-agents. "
                     "Tools: shell, file_read, file_write, file_edit (4 tools vs. 8+). "
                     "No MCP client — no external tool discovery. "
                     "Memory box disappears (stateless between sessions)."),
                )
            with li.item():
                st_write(
                    (bs.note_tool, "Cursor"),
                    (bs.content, " — Agent loop is embedded in the IDE, not a standalone process. "
                     "No sub-agent spawning. MCP client exists but configured via UI, not file. "
                     "Built-in tools are IDE-native (edit, terminal, search). "
                     "No hooks layer in the tool execution pipeline."),
                )
            with li.item():
                st_write(
                    (bs.note_tool, "GitHub Copilot"),
                    (bs.content, " — Agent loop embedded in IDE or CLI. "
                     "No sub-agents. Limited MCP support. "
                     "Tools are internal and not directly exposed to the user. "
                     "No permission gate, no hooks. Simplest architecture of the four."),
                )
