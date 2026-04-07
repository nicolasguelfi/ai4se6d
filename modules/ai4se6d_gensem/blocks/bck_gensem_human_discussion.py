"""Slide — Discussion: where did AI help or slow you down?"""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Discussion slide styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    question = Style.create(
        s.project.titles.body + s.project.colors.highlight + s.center_txt,
        "gs_disc_question",
    )

bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_center):
        st_write(bs.heading, "Discussion", tag=t.div, toc_lvl="1")
        st_space("v", 2)
        st_write(
            bs.question,
            "Based on your Days 1-2 experience: where on the junior-senior "
            "spectrum did AI help you most?",
        )
        st_space("v", 1)
        st_write(
            bs.question,
            "Where did it slow you down?",
        )
