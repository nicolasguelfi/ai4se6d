"""Slide — Billboard bridge: Speed AND Quality?"""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

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

_NOTES = [
    ("The message", "The question that bridges the two halves of the module: the dangers we just saw (security, phantom "
                    "packages, debt, trust) versus the speed of AI. Must we choose?"),
    ("The answer coming next", "No: the next part (VibeEngineering) keeps the speed and adds the practices that bring "
                               "the quality back — requirements, tests, architecture, review."),
    ("The evidence later", "The Evidence slides show that a process around the agent improves results instead of "
                           "slowing them down."),
    ("Ask the room", "« Speed or quality: which one did you lose this afternoon? »"),
]

def build():
    with st_block(s.project.containers.page_fill_center_wide):
        with st_block(s.center_txt), st_zoom(130):   # fills the screen (NG, 2026-11-23)
            # the « i » on the first line (NG, 2026-11-23)
            with st_grid(cols="95% 5%", gap="0px", cell_styles=s.project.containers.grid_cell_centered) as h:
                with h.cell():
                    st_write(
                        bs.question,
                        "Speed",
                        tag=t.div,
                        toc_lvl="1",
                        label="Speed AND Quality?",
                    )
                with h.cell(), st_zoom(70):
                    st_hover_tooltip(title="Trainer notes — Speed AND Quality?", entries=_NOTES,
                                     position="left", width="50vw")
            st_write(bs.highlight, "AND")
            st_write(bs.question, "Quality?")
