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
        "note_box_maria_exec",
    )
    note_label = s.project.titles.subtitle + ns(
        "text-transform: uppercase; letter-spacing: 1px;",
        "note_label_maria_exec",
    )
    note_tool = s.project.titles.body + s.bold + s.project.colors.primary


bs = BlockStyles


def build():
    st_write(bs.title, "Maria's Execution Flow", tag=t.div, toc_lvl="2")
    st_space(size=2)

    st_write(
        bs.content,
        "The complete 7-turn session: understand (read template), collect business data (Odoo MCP), "
        "parallel research (3 sub-agents with recursive spawning), write document, validate structure, "
        "distribute (Gmail + Calendar MCP), conclude with memory save.",
    )
    st_space(size=1)
    show_diagram("maria_sequence.mmd", height=2000, key="maria_seq")
    st_space(size=3)

    # ── Variants by Tool ──
    st_write(bs.subtitle, "Variants by Tool", tag=t.div, toc_lvl="+1")
    st_space(size=1)
    st_write(
        bs.content,
        "The 7-turn sequence leverages Claude Code's full capabilities. "
        "With other tools, the flow would collapse significantly:",
    )
    st_space(size=1)

    with st_block(bs.note_box):
        st_write(bs.note_label, "Execution flow differences")
        st_space(size=1)
        with st_list(list_type=lt.unordered, li_style=bs.content) as li:
            with li.item():
                st_write(
                    (bs.note_tool, "OpenAI Codex CLI"),
                    (bs.content, " — 7 turns → ~3 turns. No parallel sub-agent turns (2, 3). "
                     "No MCP turns (Odoo data, Gmail, Calendar). "
                     "The agent would read pre-provided data files and write the document sequentially."),
                )
            with li.item():
                st_write(
                    (bs.note_tool, "Cursor"),
                    (bs.content, " — 7 turns → ~4 turns. MCP turns possible (Odoo) if configured. "
                     "No parallel research — sequential conversation. "
                     "No Gmail/Calendar distribution step."),
                )
            with li.item():
                st_write(
                    (bs.note_tool, "GitHub Copilot"),
                    (bs.content, " — Not applicable. Copilot doesn't support multi-turn agentic workflows "
                     "with tool execution. The user would need to manually orchestrate "
                     "each step and paste results into the conversation."),
                )
