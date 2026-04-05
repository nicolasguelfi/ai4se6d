"""Slide 31 — The Tools That Make It Real: billboard intro."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s

<<<<<<< HEAD

# Billboard centered container
_page_fill = s.project.containers.page_fill_center


=======
>>>>>>> a1435b5 (feat: vibecoding review fixes + CE integrate + style refactoring)
class BlockStyles:
    """IDE overview billboard styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body + s.center_txt
    emphasis = Style.create(
        s.Large + s.bold + s.italic + s.project.colors.accent + s.center_txt,
        "ide_overview_emphasis",
    )
bs = BlockStyles

<<<<<<< HEAD

def build():
    with st_block(_page_fill):
=======
def build():
    with st_block(s.project.containers.page_fill_center):
>>>>>>> a1435b5 (feat: vibecoding review fixes + CE integrate + style refactoring)
        with st_block(s.center_txt):
            st_write(bs.heading, "The Tools That Make It Real", tag=t.div, toc_lvl="1")
            st_space("v", 2)
            st_write(
                bs.emphasis,
                "VibeCoding and VibeEngineering are practices.",
            )
            st_space("v", 1)
            st_write(
                bs.body,
                "The TOOLS bring them to life.",
            )
