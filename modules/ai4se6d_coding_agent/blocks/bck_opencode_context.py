"""Slide — What fills the context window."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Context window styles."""
    heading = s.project.titles.heading
    layer = Style.create(s.project.titles.table_label + s.center_txt, "ctx_layer")
    body = s.project.titles.table_cell
    keyword = s.project.titles.table_label
bs = BlockStyles

_LAYERS = [
    "Rules — AGENTS.md",
    "Your prompt",
    "Files you @mention or it reads",
    "Conversation history",
    "Tool results — commands, tests, MCP",
]

_NOTES = [
    ("The message",
     "Everything the agent knows during a turn sits in one context window: rules, your prompt, files, the "
     "conversation so far and tool results."),
    ("Every turn",
     "All of it is sent to the model at every turn. The window has a fixed size."),
    ("The trap",
     "When the window is too full, early details get lost: the rule stated at the start of a long session is the "
     "first to fade."),
    ("The two commands",
     "/compact summarises the conversation to free space; /new starts a clean session — one task, one session."),
    ("What comes next",
     "@file mentions to choose what enters the window, then what NOT to put in it."),
    ("Ask the room",
     "« In your last long AI session, when did the answers start to drift? »"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "The Context Window", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — The Context Window", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "3vh")
        with st_zoom(130), st_grid(cols="5% 40% 50% 5%", gap="2vw",
                                    cell_styles=[s.none, s.none, s.project.containers.grid_cell_centered
                                                 + Style("text-align:left;", "txt_left"), s.none]) as g:
            with g.cell():
                pass  # left margin
            with g.cell():
                for layer in _LAYERS:
                    with st_block(s.project.containers.table_normal_cell + Style("margin-bottom:1.5vh;", "ctx_gap")):
                        st_write(bs.layer, layer)
            with g.cell():
                with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered,
                             text_align="left", item_gap=0.6) as l:
                    with l.item(): st_write(bs.body, "All of it is sent to the model, ", (bs.keyword, "every turn"))
                    with l.item(): st_write(bs.body, "The window has a ", (bs.keyword, "fixed size"))
                    with l.item(): st_write(bs.body, "Too full: early details get lost")
                    with l.item(): st_write(bs.body, (bs.keyword, "/compact"), " summarises, ",
                                            (bs.keyword, "/new"), " starts clean")
            with g.cell():
                pass  # right margin
