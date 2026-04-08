"""Slide — The METR Paradox: experienced devs 19% slower with AI."""
# @guideline: maximize-viewport
# @pattern: stat-hero
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX

class BlockStyles:
    """METR Paradox stat-hero styles."""
    heading = s.project.titles.slide_title + s.center_txt
    stat = Style.create(
        s.GIANT + s.bold + s.project.colors.highlight + s.center_txt,
        "vc_danger_metr_stat",
    )
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    keyword_warn = s.bold + s.project.colors.highlight
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles

_PROMPT = (
    f"{_PREFIX} A brain split in two halves: left half is bright and optimistic with "
    "upward arrows in electric blue. Right half confronts a stopwatch showing delay "
    "in amber. A teal mirror between them reflects the disconnect. Symbolizes the gap "
    f"between perceived and actual AI productivity. {_SUFFIX}"
)


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "The METR Paradox", tag=t.div, toc_lvl="1")

            with st_grid(
                cols="2fr 3fr",
                gap="24px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    st_image(
                        s.none,
                        width="80%",
                        editable=IS_EDITABLE,
                        name="vc_danger_metr",
                        prompt=_PROMPT,
                        provider="openai",
                        ai_size="1024x1536",
                    )

                with g.cell():
                    st_write(bs.stat, "\u221219%")
                    st_space("v", 0.5)
                    st_write(
                        bs.body,
                        "Experienced developers completed tasks ",
                        (bs.keyword_warn, "19% slower"),
                        " with AI tools.",
                    )
                    st_space("v", 0.5)
                    st_write(
                        bs.body,
                        (bs.keyword, "16 developers"),
                        ", 246 tasks, 5+ years experience per project.",
                    )
                    st_write(
                        bs.body,
                        "Tool: Cursor Pro + Claude 3.5/3.7 Sonnet.",
                    )
                    st_space("v", 0.5)
                    st_write(
                        bs.body,
                        "Before: developers predicted ",
                        (bs.keyword, "+24%"),
                        " speedup.",
                    )
                    st_write(
                        bs.body,
                        "After: they ",
                        (bs.keyword_warn, "still believed"),
                        " they were 20% faster.",
                    )
                    st_write(
                        bs.body,
                        "Reality: <44% of AI generations accepted.",
                    )
                    st_space("v", 0.5)
                    # REF: METR, arXiv 2507.09089, July 2025
                    st_write(bs.source, cite("metr2025"))
