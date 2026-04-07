"""Slide 12 — Ethics & Responsibility: AI image + four key points."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX


_page_fill = s.project.containers.page_fill_top

# AI image prompt components

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
                    with st_zoom(130):
                        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                            with l.item(): st_write(bs.body, (bs.keyword, "Bias"), " — models reflect training data biases")
                            with l.item(): st_write(bs.body, (bs.keyword, "Privacy"), " — sensitive data in prompts leaks")
                            with l.item(): st_write(bs.body, (bs.keyword, "Copyright"), " — who owns AI-generated content?")
                            with l.item(): st_write(bs.body, (bs.keyword, "Transparency"), " — always disclose AI usage")
