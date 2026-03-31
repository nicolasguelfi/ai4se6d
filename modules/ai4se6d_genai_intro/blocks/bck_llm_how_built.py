"""Slide — How LLMs Are Built: billboard transition."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.styles import Style as ns
from streamtex.enums import Tags as t
from custom.styles import Styles as s


# Viewport-filling container — billboard: center
_page_fill = ns(
    "display:flex;flex-direction:column;justify-content:center;"
    "align-items:center;min-height:85vh;gap:1.5rem;",
    "page_fill_llm_how_built",
)


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
