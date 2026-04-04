"""Slide — Demo vs Production gap (balanced layout)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX


_page_fill = s.project.containers.page_fill_top

_cell = Style.create(
    s.container.layouts.vertical_center_layout + s.center_txt,
    "vc_danger_demo_prod_cell",
)


class BlockStyles:
    """Demo vs prod slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword_ok = s.bold + s.project.colors.accent
    keyword_warn = s.bold + s.project.colors.highlight
    emphasis = Style.create(
        s.Large + s.italic + s.project.colors.primary + s.center_txt,
        "vc_danger_demo_prod_emphasis",
    )
bs = BlockStyles


_PROMPT = (
    f"{_PREFIX} Split screen: left side shows a perfect, shiny application interface "
    "in electric blue (demo). Right side shows the same interface crumbling with error "
    "symbols and warning triangles in amber (production reality). A teal curtain "
    f"separates the two halves. Represents the gap between demo and production. {_SUFFIX}"
)


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "Demo vs. Production", tag=t.div, toc_lvl="1")

            with st_grid(
                cols="2fr 3fr",
                gap="24px",
                cell_styles=_cell,
            ) as g:
                with g.cell():
                    st_image(
                        s.none,
                        width="80%",
                        editable=IS_EDITABLE,
                        name="vc_danger_demo_prod",
                        prompt=_PROMPT,
                        provider="openai",
                        ai_size="1024x1536",
                    )

                with g.cell():
                    st_write(
                        bs.body,
                        (bs.keyword_ok, "The demo works."),
                    )
                    st_space("v", 1)
                    st_write(
                        bs.body,
                        (bs.keyword_warn, "Production requires: "),
                        "security, scalability, maintainability, monitoring, "
                        "error handling, edge cases, compliance.",
                    )
                    st_space("v", 2)
                    st_write(
                        bs.emphasis,
                        "The gap between \u201Cit works\u201D and "
                        "\u201Cit\u2019s production-ready\u201D "
                        "is where engineering lives.",
                    )
