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
        "note_box_maria_arch",
    )
    note_label = s.project.titles.subtitle + ns(
        "text-transform: uppercase; letter-spacing: 1px;",
        "note_label_maria_arch",
    )
    note_tool = s.project.titles.body + s.bold + s.project.colors.primary


bs = BlockStyles


def build():
    st_write(bs.title, "Maria's Architecture in Detail", tag=t.div, toc_lvl="2")
    st_space(size=2)

    # ── Overview ──
    st_write(bs.subtitle, "High-Level Overview", tag=t.div, toc_lvl="+1")
    st_space(size=1)
    st_write(
        bs.content,
        "The agent architecture applied to Maria's case: Odoo as local MCP, "
        "Hetzner/Gmail/Calendar as remote MCPs, 3 specialized sub-agents.",
    )
    st_space(size=1)
    show_diagram("maria_overview.mmd", height=1000, key="maria_overview")
    st_space(size=3)

    # ── Agent Loop ──
    st_write(bs.subtitle, "Detail: Agent Loop", tag=t.div, toc_lvl="+1")
    st_space(size=1)
    st_write(
        bs.content,
        "The context accumulates Maria's prompt, Odoo business data, sub-agent research results, "
        "and the requirements template — all sent to the LLM at each turn.",
    )
    st_space(size=1)
    show_diagram("maria_agent_loop.mmd", height=900, key="maria_loop")
    st_space(size=3)

    # ── Tool Execution ──
    st_write(bs.subtitle, "Detail: Tool Execution & MCP", tag=t.div, toc_lvl="+1")
    st_space(size=1)
    st_write(
        bs.content,
        "Built-in tools handle the document (Read/Write template, WebSearch regulations). "
        "MCP local (Odoo) provides real business metrics. "
        "MCP remote (Hetzner, Gmail, Calendar) handles cloud sizing, delivery, and scheduling.",
    )
    st_space(size=1)
    show_diagram("maria_tool_execution.mmd", height=1200, key="maria_tools")
    st_space(size=3)

    # ── Sub-Agents ──
    st_write(bs.subtitle, "Detail: Sub-Agents & Recursion", tag=t.div, toc_lvl="+1")
    st_space(size=1)
    st_write(
        bs.content,
        "3 sub-agents work in parallel. The Cloud Architect (C) demonstrates recursion: "
        "it spawns C1 (Odoo volumetry) and C2 (Hetzner pricing) as sub-sub-agents "
        "before assembling the infrastructure proposal.",
    )
    st_space(size=1)
    show_diagram("maria_subagents.mmd", height=1400, key="maria_subs")
    st_space(size=3)

    # ── Variants by Tool ──
    st_write(bs.subtitle, "Variants by Tool", tag=t.div, toc_lvl="+1")
    st_space(size=1)
    st_write(
        bs.content,
        "This case study uses Claude Code (Opus/Haiku models) which provides the richest "
        "architecture. Here is how the same task would differ with other tools:",
    )
    st_space(size=1)

    with st_block(bs.note_box):
        st_write(bs.note_label, "Maria's WebShop with other tools")
        st_space(size=1)
        with st_list(list_type=lt.unordered, li_style=bs.content) as li:
            with li.item():
                st_write(
                    (bs.note_tool, "OpenAI Codex CLI"),
                    (bs.content, " — No sub-agents: the single agent handles all research sequentially. "
                     "No MCP: cannot query Odoo or Hetzner APIs directly — would need manual data input "
                     "or pre-fetched files. No Gmail/Calendar integration. "
                     "Models: o3 or codex-mini instead of Opus/Haiku."),
                )
            with li.item():
                st_write(
                    (bs.note_tool, "Cursor"),
                    (bs.content, " — IDE-bound: better suited for code generation than document writing. "
                     "Could query Odoo via MCP (if configured), but no parallel sub-agents. "
                     "No Gmail/Calendar MCP. The task would be done in a single sequential conversation."),
                )
            with li.item():
                st_write(
                    (bs.note_tool, "GitHub Copilot"),
                    (bs.content, " — Not designed for this type of task. Copilot excels at code completion "
                     "and inline suggestions, not multi-source requirements engineering. "
                     "No MCP, no sub-agents, no external API integration."),
                )
