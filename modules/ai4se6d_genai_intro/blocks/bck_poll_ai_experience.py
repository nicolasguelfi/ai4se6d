"""Slide — How much AI is used by developers? Transition question."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


_page_fill = s.project.containers.page_fill_center


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
