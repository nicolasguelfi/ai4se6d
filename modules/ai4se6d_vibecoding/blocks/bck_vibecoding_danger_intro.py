"""Slide — Billboard: It Works... But at What Cost? (metaphor pivot)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

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

_NOTES = [
    ("The pivot",
     "Billboard that turns the session: after the appeal of VibeCoding, its cost. Pause on the question."),
    ("The metaphor",
     "« Your dish looked good. But the kitchen just got inspected… » — the customer only tasted the dish; the "
     "inspector looks at what happens behind the kitchen door."),
    ("What follows",
     "Seven slides of evidence: security vulnerabilities, phantom packages, technical debt, the AI paradox, the "
     "METR study, the trust crisis, demo vs production."),
    ("Ask the room",
     "« If a security auditor opened the code you generated last week, what would they find? »"),
]


def build():
    with st_block(s.project.containers.page_fill_center_wide):
        st_space("v", "15vh")   # the billboard sits in the middle of the screen
        # title on one line with the « i » (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(62):
                st_write(
                    bs.question+"zoom:1.3;",
                    "It Works\u2026 But at What Cost?",
                    tag=t.div,
                    toc_lvl="1",
                )
            with h.cell():
                st_hover_tooltip(title="Trainer notes — It Works… But at What Cost?", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", 3)
        with st_zoom(190), st_block(s.center_txt):
            st_write(
                bs.body,
                "Your dish looked good. But the kitchen just got inspected\u2026",
            )
