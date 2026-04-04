"""Slide — Technical debt iceberg (balanced layout)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX


_page_fill = s.project.containers.page_fill_top

_cell = Style.create(
    s.container.layouts.vertical_center_layout + s.center_txt,
    "vc_danger_debt_cell",
)


class BlockStyles:
    """Tech debt iceberg slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.highlight
    keyword_ok = s.bold + s.project.colors.accent
    quote = Style.create(
        s.Large + s.italic + s.project.colors.primary,
        "vc_danger_debt_quote",
    )
    source = s.project.titles.caption
bs = BlockStyles


_PROMPT = (
    f"{_PREFIX} An iceberg: small clean tip visible above a waterline in electric blue. "
    "Massive hidden mass below the surface in teal with amber cracks running through "
    "the submerged portion. The visible part is shiny and polished, the hidden part "
    f"is chaotic with broken connections and warning symbols. {_SUFFIX}"
)


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "The Iceberg", tag=t.div, toc_lvl="1")

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
                        name="vc_danger_debt",
                        prompt=_PROMPT,
                        provider="openai",
                        ai_size="1024x1536",
                    )

                with g.cell():
                    st_write(
                        bs.body,
                        (bs.keyword_ok, "What you see: "),
                        "working prototype.",
                    )
                    st_space("v", 1)
                    st_write(
                        bs.body,
                        (bs.keyword, "What\u2019s hidden: "),
                        "unmaintainable code, missing error handling, "
                        "no tests, brittle architecture.",
                    )
                    st_space("v", 2)
                    st_write(
                        bs.quote,
                        "\u201COrganizations chasing short-term productivity gains "
                        "may face \u2018long-term catastrophe\u2019 from accumulated "
                        "technical debt in AI-generated code.\u201D",
                    )
                    # REF: https://martinfowler.com/bliki/TechnicalDebt.html
                    st_write(bs.source, cite("fowler1999refactoring"))
