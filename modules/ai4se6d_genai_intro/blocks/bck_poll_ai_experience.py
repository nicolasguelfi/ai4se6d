"""Slide — How much AI is used by developers? Transition question."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.styles import Style as ns
from streamtex.enums import Tags as t
from custom.styles import Styles as s


# Viewport-filling container
_page_fill = ns(
    "display:flex;flex-direction:column;justify-content:center;"
    "align-items:center;min-height:85vh;gap:1.5rem;",
    "page_fill_poll_ai_experience",
)


class BlockStyles:
    """Slide: AI Poll — maximize-viewport archetype: single phrase."""
    question = Style.create(
        s.Giant + s.bold + s.center_txt + s.project.colors.accent,
        "poll_ai_experience_question",
    )
bs = BlockStyles


def build():
    with st_block(_page_fill):
        st_write(
            bs.question,
            "How much AI is used by developers?",
            tag=t.div,
            toc_lvl="1",
        )
