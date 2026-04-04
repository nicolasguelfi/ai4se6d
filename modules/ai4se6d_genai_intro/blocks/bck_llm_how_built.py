"""Slide — How LLMs Are Built: billboard transition."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


_page_fill = s.project.containers.page_fill_center


class BlockStyles:
    """Slide: How Built — billboard archetype: single phrase centered."""
    question = Style.create(
        s.Giant + s.bold + s.center_txt + s.project.colors.primary,
        "llm_how_built_question",
    )
bs = BlockStyles


def build():
    with st_block(_page_fill):
        st_write(
            bs.question,
            "How LLMs Are Built",
            tag=t.div,
            toc_lvl="1",
        )
