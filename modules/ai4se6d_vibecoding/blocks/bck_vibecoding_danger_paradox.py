"""Slide — Stat-hero: AI Paradox — 7 hours/week lost."""
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
    """AI Paradox stat-hero styles."""
    heading = s.project.titles.slide_title + s.center_txt
    stat = s.project.titles.stat_hero
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.highlight
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles

_PROMPT = (
    f"{_PREFIX} Two clocks side by side: left clock runs forward smoothly in electric "
    "blue (time saved). Right clock is broken and spinning backwards in amber (time "
    "lost). A teal balance scale between them tips toward the right. Represents the "
    f"paradox of faster coding creating new bottlenecks. {_SUFFIX}"
)

def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "The AI Paradox", tag=t.div, toc_lvl="1")

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
                        name="vc_danger_paradox",
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
                            st_write(bs.stat, "7 hours")
                        with sg.cell():
                            st_hover_tooltip(
                                title="About this statistic",
                                entries=[
                                    (
                                        "7 hours/week",
                                        "Time lost per team member to AI-related "
                                        "inefficiencies \u2014 nearly a full workday "
                                        "every week.",
                                    ),
                                    (
                                        "3,266 professionals",
                                        "DevSecOps professionals surveyed (IT ops, "
                                        "security, development). Harris Poll for "
                                        "GitLab, 2025.",
                                    ),
                                    (
                                        "The paradox",
                                        "AI accelerates coding, but fragmented "
                                        "toolchains and new compliance complexity "
                                        "create bottlenecks that offset the speed "
                                        "gains.",
                                    ),
                                    (
                                        "Tool sprawl",
                                        "60% use more than 5 dev tools; 49% use "
                                        "more than 5 AI tools. Integration overhead "
                                        "eats productivity.",
                                    ),
                                ],
                                scale="2.2vw",
                                width="70vw",
                                position="left",
                            )
                    st_space("v", 1)
                    st_write(
                        bs.body,
                        "lost per team member weekly to AI-related "
                        "inefficiencies.",
                    )
                    st_space("v", 1)
                    st_write(
                        bs.body,
                        (bs.keyword, "Faster coding "),
                        "creates new bottlenecks: code review of AI output, "
                        "debugging hallucinations, fixing integration issues.",
                    )
                    st_space("v", 1)
                    # REF: https://about.gitlab.com/developer-survey/
                    st_write(bs.source, cite("gitlab-devsecops2025"))
