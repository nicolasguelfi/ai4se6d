"""Slide — 30,000-100,000 tokens: billboard with body text."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


_page_fill = s.project.containers.page_fill_center


class BlockStyles:
    """Slide: LLM Vocabulary — billboard with supporting body."""
    heading = Style.create(
        s.Giant + s.bold + s.center_txt + s.project.colors.highlight,
        "llm_vocabulary_heading",
    )
    body = Style.create(
        s.Large + s.italic + s.center_txt,
        "llm_vocabulary_body",
    )
bs = BlockStyles


def build():
    with st_block(_page_fill):
        st_write(
            bs.heading,
            "30,000 \u2014 100,000",
            tag=t.div,
            toc_lvl="1",
        )
        st_space("v", 1)
        st_write(bs.heading + s.text.sizes.pt52 + s.project.colors.accent, "tokens in a LLM vocabulary.", tag=t.div)
        st_space("v", 1)
        st_write(bs.body, "Rare words = more tokens,", tag=t.div)
        st_write(bs.body, "common words = fewer.", tag=t.div)
