"""Slide — Attention in Action: image-dominant visualization."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.styles import Style as ns
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_LANDSCAPE as _SUFFIX


# Viewport-filling container
_page_fill = ns(
    "display:flex;flex-direction:column;justify-content:flex-start;"
    "align-items:center;min-height:85vh;gap:1.5rem;",
    "page_fill_llm_attention_viz",
)


class BlockStyles:
    """Slide: Attention Viz — maximize-viewport archetype: image-dominant."""
    heading = s.project.titles.slide_title + s.center_txt
    caption = Style.create(
        s.project.titles.caption + s.center_txt + s.Large,
        "llm_attention_viz_caption",
    )
bs = BlockStyles


# Master prompt components

_PROMPT = (
    f"{_PREFIX} Two parallel rows of circles connected by crossing lines of varying intensity. "
    "Electric blue circles on top, teal circles on bottom. Lines glow brighter where attention "
    "is strongest (amber). Creates a complex but elegant web pattern. "
    f"{_SUFFIX}"
)


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "Attention in Action", tag=t.div, toc_lvl="1")

            st_image(
                s.none,
                width="80%",
                editable=IS_EDITABLE,
                name="llm_attention_viz",
                prompt=_PROMPT,
                provider="openai",
                ai_size="1536x1024",
            )

            st_write(
                bs.caption,
                "Every token computes how much to attend to every other token",
                tag=t.div,
            )
