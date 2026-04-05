"""Slide — Billboard bridge: Speed AND Quality?"""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s

<<<<<<< HEAD

# Billboard centered container
_page_fill = s.project.containers.page_fill_center_wide


=======
>>>>>>> a1435b5 (feat: vibecoding review fixes + CE integrate + style refactoring)
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

<<<<<<< HEAD

def build():
    with st_block(_page_fill):
=======
def build():
    with st_block(s.project.containers.page_fill_center_wide):
>>>>>>> a1435b5 (feat: vibecoding review fixes + CE integrate + style refactoring)
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
