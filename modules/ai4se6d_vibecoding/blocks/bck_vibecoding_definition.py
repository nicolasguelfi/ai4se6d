"""Slide — Formal definition of VibeCoding."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s

class BlockStyles:
    """VibeCoding definition slide styles."""
    heading = s.project.titles.section_title + s.center_txt
    body = s.project.titles.body + s.center_txt
    highlight = Style.create(
        s.huge + s.bold + s.project.colors.highlight + s.center_txt,
        "vc_def_highlight",
    )
bs = BlockStyles

def build():
    with st_zoom(120),st_block(s.project.containers.page_fill_center_wide):
        with st_block(s.center_txt):
            st_write(bs.heading, "VibeCoding \u2014 Definition", tag=t.div, toc_lvl="1")
            st_space("v", 1)
            st_write(
                bs.body,
                "A practice where developers <br>describe tasks to LLMs, accept generated code",
            )
            st_write(
                bs.highlight,
                "without closely reviewing",
            )
            st_write(
                bs.body,
                "its internal structure, and rely on results "
                "<br>and follow-up prompts to guide changes.",
            )
