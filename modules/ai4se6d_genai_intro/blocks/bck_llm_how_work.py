"""Slide 6 — Transition: How does a machine generate text?"""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


_page_fill = s.project.containers.page_fill_center


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
