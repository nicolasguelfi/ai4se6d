"""Slide — The GenAI Revolution: image-dominant timeline."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.styles import Style as ns
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_LANDSCAPE as _SUFFIX


# Override: flex-start + align-items:center combo not in centralized styles
_page_fill = ns(
    "display:flex;flex-direction:column;justify-content:flex-start;"
    "align-items:center;min-height:85vh;gap:1.5rem;",
    "page_fill_genai_revolution",
)


class BlockStyles:
    """Slide: GenAI Revolution — maximize-viewport archetype: image-dominant."""
    heading = s.project.titles.slide_title + s.center_txt
    caption = Style.create(
        s.project.titles.caption + s.center_txt + s.Large,
        "genai_revolution_caption",
    )
bs = BlockStyles


# Master prompt components

_PROMPT = (
    f"{_PREFIX} A dramatic horizontal timeline flowing left to right, represented as a "
    "luminous electric blue beam that starts thin on the left (2020) and explodes into a "
    "massive starburst of teal and amber rays on the right (2026). Along the beam, "
    "progressively larger glowing nodes mark milestones. The explosion on the right "
    "radiates countless small geometric shapes — circles, triangles, hexagons — "
    f"symbolizing the exponential growth of AI capabilities. {_SUFFIX}"
)


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "The GenAI Revolution", tag=t.div, toc_lvl="1")

            st_image(
                s.none,
                width="80%",
                editable=IS_EDITABLE,
                name="genai_revolution_timeline",
                prompt=_PROMPT,
                provider="openai",
                ai_size="1536x1024",
            )

            st_write(
                bs.caption,
                "From GPT-3.5 (2022) to multimodal agents (2026) — the fastest technology adoption in history",
                tag=t.div,
            )
