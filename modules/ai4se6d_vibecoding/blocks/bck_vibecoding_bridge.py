"""Slide — Billboard bridge: Speed AND Quality?"""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s

class BlockStyles:
    """Bridge billboard styles."""
    question = Style.create(
        s.Huge + s.bold + s.center_txt,
        "vc_bridge_question",
    )
    highlight = Style.create(
        s.GIANT + s.bold + s.center_txt + s.project.colors.highlight,
        "vc_bridge_highlight",
    )
bs = BlockStyles

def build():
    with st_block(s.project.containers.page_fill_center_wide):
        with st_block(s.center_txt):
            st_write(
                bs.question,
                "Speed",
                tag=t.div,
                toc_lvl="1",
                label="Speed AND Quality?",
            )
            st_write(bs.highlight, "AND")
            st_write(bs.question, "Quality?")
