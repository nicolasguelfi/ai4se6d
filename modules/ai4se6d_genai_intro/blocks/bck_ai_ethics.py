"""Slide 12 — Ethics & Responsibility: AI image + four key points."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.styles import Style as ns
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from custom.config import IS_EDITABLE


# Viewport-filling container
_page_fill = ns(
    "display:flex;flex-direction:column;justify-content:flex-start;"
    "min-height:85vh;gap:1.5rem;",
    "page_fill_ethics",
)

# AI image prompt components
_PREFIX = (
    "Minimalist digital illustration on a pure dark background (#1A1A2E). "
    "Flat vector style with soft gradients. Limited color palette: electric blue (#7AB8F5), "
    "teal (#2EC4B6), amber (#F39C12), white (#FFFFFF). Clean geometric shapes, no text, "
    "no watermarks, no photorealism. Ample negative space. Professional and modern aesthetic, "
    "suitable for tech conference projection."
)
_SUFFIX = (
    "No text, no letters, no words, no labels, no watermarks. "
    "2:3 portrait aspect ratio. Dark background #1A1A2E."
)

_PROMPT_ETHICS = (
    f"{_PREFIX} A balanced scale with one side holding a glowing circuit board "
    "and the other side holding a shield with a heart symbol. Geometric lines "
    "connecting them suggest interconnection between technology and ethics. "
    f"{_SUFFIX}"
)


class BlockStyles:
    """Slide: Ethics — maximize-viewport archetype: image + bullet list grid."""
    heading = s.project.titles.section_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.highlight
    cell_center = s.container.layouts.vertical_center_layout + s.center_txt


bs = BlockStyles


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "Ethics & Responsibility", tag=t.div, toc_lvl="1")

            with st_grid(
                cols="2fr 3fr",
                gap="32px",
                cell_styles=bs.cell_center,
            ) as g:
                with g.cell():
                    st_image(
                        s.none,
                        width="80%",
                        editable=IS_EDITABLE,
                        name="ethics_balance",
                        prompt=_PROMPT_ETHICS,
                        provider="openai",
                        ai_size="1024x1536",
                    )
                with g.cell():
                    with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                        with l.item(): st_write(bs.body, (bs.keyword, "Bias"), " — models reflect training data biases")
                        with l.item(): st_write(bs.body, (bs.keyword, "Privacy"), " — sensitive data in prompts leaks")
                        with l.item(): st_write(bs.body, (bs.keyword, "Copyright"), " — who owns AI-generated content?")
                        with l.item(): st_write(bs.body, (bs.keyword, "Transparency"), " — always disclose AI usage")
