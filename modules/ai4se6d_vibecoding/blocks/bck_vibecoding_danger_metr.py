"""Slide — The METR Paradox: experienced devs 19% slower with AI."""
# @guideline: maximize-viewport
# @pattern: stat-hero
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX
from shared_widgets import st_hover_tooltip

class BlockStyles:
    """METR Paradox stat-hero styles."""
    heading = s.project.titles.slide_title + s.center_txt
    stat = s.project.titles.stat_hero
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
                cols="1.5fr 3.5fr",
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
                    with st_grid(
                        cols="95fr 5fr",
                        gap="0px",
                        cell_styles=s.project.containers.grid_cell_centered,
                    ) as sg:
                        with sg.cell():
                            with st_zoom(60):
                                st_write(bs.stat, "+19%")
                        with sg.cell():
                            st_hover_tooltip(
                                title="METR Study Details",
                                entries=[
                                    (
                                        "Study design",
                                        "Randomized controlled trial. Each dev "
                                        "did some tasks with AI, some without. "
                                        "16 devs \u00d7 246 tasks on mature open-source "
                                        "projects they knew well (5+ years each).",
                                    ),
                                    (
                                        "\u221219% measured",
                                        "Tasks took 19% longer with AI than without. "
                                        "Time spent prompting, reviewing, testing, "
                                        "and discarding AI output exceeded the time saved.",
                                    ),
                                    (
                                        "Perception gap",
                                        "Before: devs predicted +24% speedup. "
                                        "After: they still believed +20% faster. "
                                        "Measured reality: 19% slower. "
                                        "Developers cannot feel the slowdown.",
                                    ),
                                    (
                                        "<44% accepted",
                                        "Over half of AI-generated code was rejected "
                                        "after review \u2014 wasted effort reviewing code "
                                        "that was ultimately discarded.",
                                    ),
                                    (
                                        "Tool used",
                                        "Cursor Pro with Claude 3.5/3.7 Sonnet "
                                        "\u2014 state-of-the-art AI coding tools "
                                        "at the time of the study (early 2025).",
                                    ),
                                ],
                                scale="2.2vw",
                                width="80vw",
                                position="left",
                            )
                    st_space("v", 0.5)
                    st_write(
                        bs.body,
                        "Experienced developers on well known projects.",
                    )
                    st_space("v", 0.5)
                    st_write(bs.body, (bs.keyword, "The perception gap:"))
                    st_write(
                        bs.body,
                        "Predicted AI would make them ",
                        (bs.keyword, "24% faster"),
                        ".",
                    )
                    st_write(
                        bs.body,
                        (bs.keyword_warn, "still believed"),
                        "@post they were 20% faster.")
                    st_space("v", 0.5)
                    st_write(
                        bs.body,
                        ">50% of AI-generated code ",
                        (bs.keyword_warn, "rejected after review"),
                        " \u2014 the time spent prompting, reviewing, and discarding "
                        "exceeded the time saved.",
                    )
                    st_space("v", 0.5)
                    # REF: METR, arXiv 2507.09089, July 2025
                    st_write(bs.source, cite("metr2025"))
