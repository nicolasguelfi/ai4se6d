"""Slide — Formal definition of VibeCoding."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

class BlockStyles:
    """VibeCoding definition slide styles."""
    heading = s.project.titles.section_title + s.center_txt
    body = s.project.titles.body + s.center_txt
    highlight = Style.create(
        s.huge + s.bold + s.project.colors.highlight + s.center_txt,
        "vc_def_highlight",
    )
bs = BlockStyles

_NOTES = [
    ("The message",
     "A working definition, built from Karpathy's post: describe the task to an LLM, accept the generated code "
     "WITHOUT CLOSELY REVIEWING it, and steer by results and follow-up prompts."),
    ("The key words",
     "« without closely reviewing » is what makes it VibeCoding. Using an AI to write code is not enough: a "
     "developer who reads, tests and owns the code is doing something else."),
    ("What follows",
     "The next four slides unfold the definition into four principles: intent over implementation, trust in "
     "output, conversational iteration, low barrier to entry."),
    ("Ask the room",
     "« By this definition, who here has already vibe coded? »"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(85):
                st_write(bs.heading+"zoom:1.3;", "VibeCoding \u2014 Definition", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — VibeCoding — Definition", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "4vh")
        with st_zoom(125), st_block(s.center_txt):
            st_write(
                bs.body,
                "A practice where developers <br>describe tasks to LLMs, accept generated code",
            )
            st_space("v", "2vh")
            st_write(
                bs.highlight,
                "without closely reviewing",
            )
            st_space("v", "2vh")
            st_write(
                bs.body,
                "its internal structure, and rely on results "
                "<br>and follow-up prompts to guide changes.",
            )
