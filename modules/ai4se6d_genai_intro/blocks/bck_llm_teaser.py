"""Slide — One Token at a Time: key LLM insight billboard."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


_page_fill = s.project.containers.page_fill_center


class BlockStyles:
    """Slide: LLM Teaser — billboard with supporting quote."""
    heading = Style.create(
        s.huge + s.bold + s.center_txt + s.project.colors.highlight,
        "llm_teaser_heading",
    )
    body = Style.create(
        s.Large + s.italic + s.center_txt,
        "llm_teaser_body",
    )
bs = BlockStyles


def build():
    with st_block(_page_fill):
        st_write(
            bs.heading,
            "One Token at a Time...",
            tag=t.div,
            toc_lvl="1",
        )
        st_space("v", 2)
        st_write(
            bs.body,
            "An LLM is fundamentally a next-token prediction engine: "
            "given all preceding tokens, it predicts the statistically "
            "most plausible continuation.",
            tag=t.div,
        )
