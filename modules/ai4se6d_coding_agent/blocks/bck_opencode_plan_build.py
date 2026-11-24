"""Slide — Plan agent vs build agent (Shift+Tab)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Plan/build styles."""
    heading = s.project.titles.heading
    card_title = s.project.titles.subtitle
    text = s.project.titles.table_cell
    keyword = s.project.titles.table_label
    closing = Style.create(s.project.titles.body_accent + s.center_txt, "pb_closing")
bs = BlockStyles

_NOTES = [
    ("The message",
     "opencode has two agents: plan thinks, build does. Shift+Tab switches between them and opencode shows which "
     "one is active."),
    ("plan — think",
     "Reads, analyses and proposes; it can ask you questions; it does not edit your files. Safe to explore a task."),
    ("build — do",
     "All tools enabled: it edits files and runs commands, following the plan you approved."),
    ("The trap",
     "Staying in build for everything: the agent starts editing before you agreed on what to do, and you review "
     "a diff instead of a plan."),
    ("What comes next",
     "The plan-then-build workflow, step by step, and when a plan is worth it."),
    ("Ask the room",
     "« Which agent would you use to understand an unfamiliar codebase? »"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "Plan Agent, Then Build Agent", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Plan Agent, Then Build Agent", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "3vh")
        with st_zoom(128), st_grid(cols="5% 1fr 1fr 5%", gap="2vw") as g:
            with g.cell():
                pass  # left margin
            with g.cell():
                with st_block(s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md):
                    st_write(bs.card_title, "plan — think", tag=t.div)
                    with st_list(l_style=bs.text, li_style=bs.text, list_type=lt.unordered,
                                 text_align="left", item_gap=0.6) as l:
                        with l.item(): st_write(bs.text, "Reads, analyses, proposes")
                        with l.item(): st_write(bs.text, "Can ask you questions")
                        with l.item(): st_write(bs.text, "Does not edit your files")
            with g.cell():
                with st_block(s.project.containers.cell_active_bg + s.project.containers.cell_pad_md):
                    st_write(bs.card_title, "build — do", tag=t.div)
                    with st_list(l_style=bs.text, li_style=bs.text, list_type=lt.unordered,
                                 text_align="left", item_gap=0.6) as l:
                        with l.item(): st_write(bs.text, "All tools enabled")
                        with l.item(): st_write(bs.text, "Edits files, runs commands")
                        with l.item(): st_write(bs.text, "Follows the plan you approved")
            with g.cell():
                pass  # right margin
        st_space("v", "5vh")
        with st_zoom(123):
            st_write(bs.closing, "Press Shift+Tab to switch agents: opencode shows which one is active.", tag=t.div)
