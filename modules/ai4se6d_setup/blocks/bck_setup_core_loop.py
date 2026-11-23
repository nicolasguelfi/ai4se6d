"""Slide — The core loop with opencode: describe, let the agent build, run, react."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Core loop slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    num = Style.create(s.project.titles.stat + s.center_txt, "setup_loop_num")
    name = Style.create(s.project.titles.body_accent, "setup_loop_name_left")
    hint = Style.create(s.project.titles.body, "setup_loop_hint_left")
    body = Style.create(s.project.titles.body + s.center_txt, "setup_loop_body")
    keyword = s.bold + s.project.colors.primary
    caption = Style.create(s.project.titles.caption + s.center_txt, "setup_loop_caption")
bs = BlockStyles

_LOOP = [
    ("1", "Describe", "what you want, in plain English"),
    ("2", "Let it build", "it reads, writes files, runs commands"),
    ("3", "Run", "open the result in your browser"),
    ("4", "React", "say what is wrong, or what is next"),
]

_NOTES = [
    ("The message",
     "Four steps, repeated: describe, let the agent build, run, react — then back to 1. That is all the "
     "participants need for this afternoon's workshop."),
    ("Describe",
     "In plain English, what you want — not how to code it. The agent decides the implementation."),
    ("Let it build",
     "opencode is an agent, not a chat: it reads the folder, writes files and runs commands on its own."),
    ("The trap",
     "opencode asks before some actions. Read the request before you accept: you stay responsible for what "
     "it does on your machine."),
    ("Link to the rest of the course",
     "Today the loop has no plan and no review — on purpose. Tomorrow (CalcApp) the same loop gets git, "
     "a plan and a code review."),
    ("Ask the room",
     "« Which step will take you the most time: describing, or reacting? »"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "The Core Loop", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — The Core Loop", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "3vh")

        # One numbered row per step, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        cols = "5% 5% 25% 60% 5%"
        cells = s.project.containers.rows(len(_LOOP), cols, filled=(2, 3, 4))
        with st_zoom(105), st_grid(cols=cols, gap="6vh 0.5vw", cell_styles=cells) as g:
            for num, name, hint in _LOOP:
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.num, num, tag=t.div)
                with g.cell():
                    st_write(bs.name, name, tag=t.div)
                with g.cell():
                    st_write(bs.hint, hint, tag=t.div)
                with g.cell():
                    pass  # right margin
        st_space("v", "6vh")
        with st_zoom(105):
            st_write(bs.body, "…and back to 1. That is ", (bs.keyword, "all you need today"), ".", tag=t.div)
            st_space("v", "1vh")
            st_write(bs.caption, "opencode asks before some actions: read the request before you accept.", tag=t.div)
