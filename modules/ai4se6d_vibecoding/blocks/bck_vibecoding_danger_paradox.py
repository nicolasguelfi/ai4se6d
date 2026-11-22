"""Slide — Stat-hero: AI Paradox — 7 hours/week lost."""
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
    """AI Paradox stat-hero styles."""
    heading = s.project.titles.slide_title + s.center_txt
    stat = s.project.titles.stat_hero
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.highlight
    source = s.project.citation + s.large
bs = BlockStyles

# Text cell: vertically centred, left-aligned (NG, 2026-11-23: recipes of the intro module)
_text_cell = Style.create(s.container.layouts.vertical_center_layout + Style("text-align:left;", "txt_left"), "vc_danger_paradox_text_cell")

_PROMPT = (
    f"{_PREFIX} Two clocks side by side: left clock runs forward smoothly in electric "
    "blue (time saved). Right clock is broken and spinning backwards in amber (time "
    "lost). A teal balance scale between them tips toward the right. Represents the "
    f"paradox of faster coding creating new bottlenecks. {_SUFFIX}"
)

def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            with st_grid(cols="95% 5%", gap="0px", cell_styles=s.project.containers.grid_cell_centered) as h:
                with h.cell(), st_zoom(80):   # one-line title
                    st_write(bs.heading, "The AI Paradox", tag=t.div, toc_lvl="1")
                with h.cell():
                    st_hover_tooltip(
                        title="Trainer notes \u2014 The AI Paradox",
                        entries=[
                            (
                                "7 hours/week",
                                "Time lost per team member to inefficient "
                                "processes \u2014 nearly a full workday "
                                "every week. GitLab calls it the 'AI paradox'.",
                            ),
                            (
                                "3,266 professionals",
                                "DevSecOps professionals surveyed (IT ops, "
                                "security, development). Harris Poll for "
                                "GitLab, published 10 Nov 2025.",
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
                        position="left", width="50vw",
                    )

            with st_grid(
                cols="1.5fr 3.5fr",
                gap="3vw",
                cell_styles=[s.project.containers.grid_cell_centered, _text_cell],
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
                    with st_zoom(110):   # text cell fills the slide (NG, 2026-11-23)
                        with st_zoom(60):
                            st_write(bs.stat, "7 hours")
                        st_space("v", 1)
                        st_write(
                            bs.body,
                            "lost per team member weekly to inefficient processes.",
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
