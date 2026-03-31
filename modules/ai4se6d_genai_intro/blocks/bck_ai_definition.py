"""Slide — Transition: What is Artificial Intelligence?"""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.styles import Style as ns
from streamtex.enums import Tags as t
from custom.styles import Styles as s


# Viewport-filling container: content centered, fills 85vh
_page_fill = ns(
    "display:flex;flex-direction:column;justify-content:center;"
    "align-items:center;min-height:85vh;gap:1.5rem;",
    "page_fill_what_is_ai",
)


class BlockStyles:
    """Slide: Transition — maximize-viewport archetype: single phrase centered."""
    question = Style.create(
        s.Giant + s.bold + s.center_txt + s.project.colors.accent,
        "what_is_ai_question",
    )
bs = BlockStyles


def build():
    with st_block(_page_fill):
        st_write(
            bs.question,
            "What is Artificial Intelligence?",
            tag=t.div,
            toc_lvl="1",
        )
