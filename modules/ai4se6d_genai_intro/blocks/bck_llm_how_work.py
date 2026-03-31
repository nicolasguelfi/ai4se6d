"""Slide 6 — Transition: How does a machine generate text?"""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.styles import Style as ns
from streamtex.enums import Tags as t
from custom.styles import Styles as s


# Viewport-filling container: centered vertically
_page_fill = ns(
    "display:flex;flex-direction:column;justify-content:center;"
    "align-items:center;min-height:85vh;gap:1.5rem;",
    "page_fill_how_llms",
)


class BlockStyles:
    """Slide: Transition — maximize-viewport archetype: single question centered."""
    question = Style.create(
        s.project.colors.accent + s.bold + s.Giant + s.center_txt,
        "transition_question",
    )
bs = BlockStyles


def build():
    with st_block(_page_fill):
        st_write(
            bs.question,
            "How does a machine generate text?",
            tag=t.div,
            toc_lvl="1",
        )
