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
        "note_box_exec",
    )
    note_label = s.project.titles.subtitle + ns(
        "text-transform: uppercase; letter-spacing: 1px;",
        "note_label_exec",
    )
    note_tool = s.project.titles.body + s.bold + s.project.colors.primary


bs = BlockStyles


def build():
    st_write(bs.title, "How Does the Agent Loop Execute?", tag=t.div, toc_lvl="2")
    st_space(size=2)

    st_write(
        bs.content,
        "A typical 5-turn agent session: understand (Read), research (parallel sub-agents), "
        "act (Edit with permission gate), notify (remote MCP), conclude (text + memory save).",
    )
    st_space(size=1)
    show_diagram("generic_sequence.mmd", height=1500, key="gen_seq")
    st_space(size=3)

    # ── Variants by Tool ──
    st_write(bs.subtitle, "Variants by Tool", tag=t.div, toc_lvl="+1")
    st_space(size=1)
    st_write(
        bs.content,
        "The 5-turn sequence above shows the richest execution flow. "
        "Other tools would simplify this sequence:",
    )
    st_space(size=1)

    with st_block(bs.note_box):
        st_write(bs.note_label, "What changes per tool")
        st_space(size=1)
        with st_list(list_type=lt.unordered, li_style=bs.content) as li:
            with li.item():
                st_write(
                    (bs.note_tool, "OpenAI Codex CLI"),
                    (bs.content, " — Turn 2 disappears (no sub-agents). "
                     "Turn 4 disappears (no MCP). The sequence becomes: "
                     "Read → Edit (with permission) → Conclude. "
                     "Sandboxed execution — all file writes are in a temporary container."),
                )
            with li.item():
                st_write(
                    (bs.note_tool, "Cursor"),
                    (bs.content, " — No sub-agent turns. MCP turns possible if configured. "
                     "Permission gate is implicit (IDE applies changes, user reviews diff). "
                     "The loop is tighter: Read → Edit → Show diff → Conclude."),
                )
            with li.item():
                st_write(
                    (bs.note_tool, "GitHub Copilot"),
                    (bs.content, " — Simplest flow: prompt → LLM → code suggestion → user accepts/rejects. "
                     "No tool dispatch, no permission gate, no MCP. "
                     "Copilot Workspace adds file edits but no sub-agents or hooks."),
                )
