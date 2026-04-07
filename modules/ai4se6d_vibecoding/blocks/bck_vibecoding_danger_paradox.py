"""Slide — Stat-hero: AI Paradox — 7 hours/week lost."""
# @guideline: maximize-viewport
# @pattern: stat-hero
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX

class BlockStyles:
    """AI Paradox stat-hero styles."""
    heading = s.project.titles.slide_title + s.center_txt
    stat = Style.create(
        s.GIANT + s.bold + s.project.colors.highlight + s.center_txt,
        "vc_danger_paradox_stat",
    )
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
                    st_write(bs.stat, "7 hours")
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
                    st_write(bs.source, cite("gitlab2024devsecops"))
