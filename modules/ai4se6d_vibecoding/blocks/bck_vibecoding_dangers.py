"""Slide — Dangers of naive VibeCoding."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX


# Viewport-filling container
_page_fill = s.project.containers.page_fill_top

# Cell centering for grid
_cell = Style.create(
    s.container.layouts.vertical_center_layout + s.center_txt,
    "vc_dangers_cell",
)


class BlockStyles:
    """VibeCoding dangers slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.highlight
    stat = Style.create(
        s.Large + s.bold + s.project.colors.primary,
        "vc_dangers_stat",
    )
    source = s.project.titles.caption
bs = BlockStyles


_PROMPT = (
    f"{_PREFIX} An iceberg in a digital ocean. The visible tip above water is a small "
    "clean code block in electric blue. Below the waterline, a massive tangled mess of "
    "red and amber warning symbols, broken connections, and vulnerability icons. "
    f"Symbolizes hidden technical debt in AI-generated code. {_SUFFIX}"
)


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "Dangers of Naive VibeCoding", tag=t.div, toc_lvl="1")

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
                        name="vc_dangers",
                        prompt=_PROMPT,
                        provider="openai",
                        ai_size="1024x1536",
                    )

                with g.cell():
                    with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                        with l.item():
                            st_write(bs.body, (bs.stat, "12\u201365%"), " vulnerability rates in AI-generated code")
                            # REF: https://arxiv.org/abs/2404.18353
                            st_write(bs.source, cite("tihanyi2024formai"))
                        with l.item():
                            st_write(bs.body, (bs.keyword, "Hallucinated dependencies: "), (bs.stat, "5.2%"), " (commercial) to ", (bs.stat, "21.7%"), " (open-source)")
                            # REF: https://arxiv.org/abs/2406.10279
                            st_write(bs.source, cite("spracklen2024packages"))
                        with l.item():
                            st_write(bs.body, (bs.keyword, "Technical debt iceberg"))
                            # REF: https://martinfowler.com/bliki/TechnicalDebt.html
                            st_write(bs.body, "\u201CAny fool can write code a computer can understand.\u201D")
                            st_write(bs.source, cite("fowler1999refactoring"))
                        with l.item():
                            st_write(bs.body, (bs.keyword, "AI paradox: "), (bs.stat, "7 hours/week"), " lost to AI-related inefficiencies")
                        with l.item():
                            st_write(bs.body, (bs.keyword, "Demo vs Production gap"), " \u2014 it works \u2260 it\u2019s ready")
