"""Slide — The Trust Crisis: developer confidence in AI is falling."""
# @guideline: maximize-viewport
# @pattern: ptn_stat_hero
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX
from shared_widgets import st_hover_tooltip

class BlockStyles:
    """Trust Crisis stat-hero styles."""
    heading = s.project.titles.slide_title + s.center_txt
    stat = s.project.titles.stat_hero
    sub_stat = Style.create(
        s.Large + s.project.colors.muted + s.center_txt,
        "vc_danger_trust_sub",
    )
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    keyword_warn = s.bold + s.project.colors.highlight
    source = s.project.citation + s.large + s.center_txt
    closing = Style.create(
        s.Large + s.bold + s.center_txt + s.project.colors.accent,
        "vc_danger_trust_closing",
    )
bs = BlockStyles

_PROMPT = (
    f"{_PREFIX} A large downward-trending graph line in amber, starting high on the left "
    "and dropping sharply to the right. A broken trust icon (handshake with a crack "
    "through it) in electric blue at the bottom of the curve. "
    "Represents declining developer confidence "
    f"in AI accuracy over time. {_SUFFIX}"
)


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "The Trust Crisis", tag=t.div, toc_lvl="1")

            with st_grid(
                cols="1.7fr 3.3fr",
                gap="24px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    st_image(
                        s.none,
                        width="80%",
                        editable=IS_EDITABLE,
                        name="vc_danger_trust",
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
                                st_write(bs.stat, "33%")
                        with sg.cell():
                            st_hover_tooltip(
                                title="About this statistic",
                                entries=[
                                    (
                                        "33% trust (2025)",
                                        "33% of developers trust the accuracy of AI "
                                        "output (2024: 43%), while AI use rose from "
                                        "76% to 84%. Only 3% trust it highly.",
                                    ),
                                    (
                                        "46% distrust",
                                        "More developers distrust AI accuracy "
                                        "(46%, up from 31% in 2024) than trust it.",
                                    ),
                                    (
                                        "66% frustrated",
                                        "Top frustration: AI solutions that are "
                                        "\"almost right, but not quite\".",
                                    ),
                                    (
                                        "45% debugging",
                                        "Debugging AI-generated code is more "
                                        "time-consuming (2nd frustration).",
                                    ),
                                    (
                                        "2026 survey",
                                        "Question reworded: 48% trust AI output only "
                                        "when they can easily verify it "
                                        "(published 6 Oct 2026).",
                                    ),
                                ],
                                scale="2.2vw",
                                width="55vw",
                                position="left",
                            )
                    st_write(
                        bs.sub_stat,
                        "of developers trust AI output accuracy (2025)",
                    )
                    st_write(
                        bs.sub_stat,
                        "down from 43% in 2024",
                    )
                    st_space("v", 0.5)

                    with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                        with l.item():
                            st_write(
                                bs.body,
                                (bs.keyword_warn, "46%"),
                                " ",
                                (bs.keyword_warn, "distrust"),
                                " the accuracy of AI output",
                            )
                        with l.item():
                            st_write(
                                bs.body,
                                (bs.keyword_warn, "66%"),
                                " top frustration: ",
                                "\u201calmost right, but not quite\u201d",
                            )
                        with l.item():
                            st_write(
                                bs.body,
                                (bs.keyword, "45%"),
                                ": ",
                                (bs.keyword_warn, "debugging AI code"),
" takes longer",
                            )

                    st_space("v", 0.5)
                    # REF: Stack Overflow Developer Surveys 2024, 2025, 2026
                    st_write(
                        bs.source,
                        cite("so-survey2025"), " · ", cite("so-survey2026"),
                    )
                    st_space("v", 0.5)
                    st_write(
                        bs.closing,
                        "Adoption is rising. Trust is falling. Verify before you trust.",
                    )
