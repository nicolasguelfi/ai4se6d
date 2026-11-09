"""Slide — The METR Paradox: tasks took 19% longer with AI (early 2025) + Feb 2026 update."""
# @guideline: maximize-viewport
# @pattern: ptn_stat_hero
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
                                        "Randomized controlled trial (METR, July 2025). "
                                        "Each task randomly allowed or disallowed AI. "
                                        "16 devs, 246 real issues on mature open-source "
                                        "repos they knew well (5 years on average).",
                                    ),
                                    (
                                        "+19% time",
                                        "Tasks took 19% longer with AI allowed "
                                        "(95% CI: +2% to +39%). Time shifted to "
                                        "prompting, waiting on and reviewing AI output.",
                                    ),
                                    (
                                        "Perception gap",
                                        "Before: devs forecast a 24% speedup. "
                                        "After: they still believed AI had sped them "
                                        "up by 20%. Measured: 19% slower.",
                                    ),
                                    (
                                        "<44% accepted",
                                        "Developers accepted fewer than 44% of the "
                                        "AI generations they reviewed.",
                                    ),
                                    (
                                        "Tool used",
                                        "Cursor Pro with Claude 3.5/3.7 Sonnet "
                                        "\u2014 state-of-the-art AI coding tools "
                                        "at the time of the study (early 2025).",
                                    ),
                                    (
                                        "Feb 2026 update",
                                        "Late-2025 tools, returning devs: \u221218% time "
                                        "(CI \u221238% to +9%), not significant. METR: a "
                                        "speedup is now likely, but its size cannot "
                                        "be measured reliably (selection effects).",
                                    ),
                                ],
                                scale="2.2vw",
                                width="80vw",
                                position="left",
                            )
                    st_space("v", 0.5)
                    st_write(
                        bs.body,
                        "more time with AI \u2014 experienced devs, own repos, early 2025.",
                    )
                    st_space("v", 0.5)
                    st_write(
                        bs.body,
                        (bs.keyword, "Perception gap: "),
                        "forecast 24% faster; afterwards ",
                        (bs.keyword_warn, "still believed"),
                        " 20% faster.",
                    )
                    st_space("v", 0.5)
                    st_write(
                        bs.body,
                        (bs.keyword, "Feb 2026 update: "),
                        "newer tools likely faster, not yet measurable.",
                    )
                    st_space("v", 0.5)
                    # REF: METR, arXiv 2507.09089, July 2025 + METR blog 2026-02-24
                    st_write(bs.source, cite("metr2025"), " · ", cite("metr-uplift2026"))
