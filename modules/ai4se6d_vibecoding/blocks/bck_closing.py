"""Slide 40 — Questions? Closing billboard with landscape image."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_LANDSCAPE as _SUFFIX


# Billboard centered container
_page_fill = s.project.containers.page_fill_center


class BlockStyles:
    """Closing slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
bs = BlockStyles


_PROMPT = (
    f"{_PREFIX} A large question mark made of small glowing dots in electric blue, "
    "surrounded by subtle audience silhouettes in teal. Amber glow at the dot. "
    f"{_SUFFIX}"
)


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "Questions?", tag=t.div, toc_lvl="1")
            st_space("v", 1)

            st_image(
                s.none,
                width="90%",
                editable=IS_EDITABLE,
                name="closing_questions",
                prompt=_PROMPT,
                provider="openai",
                ai_size="1536x1024",
            )
