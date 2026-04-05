"""Slide — Billboard: It Works... But at What Cost? (metaphor pivot)."""
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
    """Danger intro billboard styles."""
    question = Style.create(
        s.Giant + s.bold + s.center_txt + s.project.colors.highlight,
        "vc_danger_intro_question",
    )
    body = Style.create(
        s.Large + s.italic + s.center_txt,
        "vc_danger_intro_body",
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
                "It Works\u2026 But at What Cost?",
                tag=t.div,
                toc_lvl="1",
            )
            st_space("v", 2)
            st_write(
                bs.body,
                "Your dish looked good. But the kitchen just got inspected\u2026",
            )
