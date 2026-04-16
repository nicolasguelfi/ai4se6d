"""Slide 2 — The Shifting Center of Gravity: yesterday vs tomorrow."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX
from shared_widgets import st_hover_tooltip

_page_fill = s.project.containers.page_fill_top
_cell = Style.create(
    s.container.layouts.vertical_center_layout + s.center_txt,
    "grav_cell",
)


class BlockStyles:
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(s.Large + s.text.wrap.hyphens, "grav_body")
    keyword = Style.create(
        s.Large + s.bold + s.project.colors.primary + s.text.wrap.hyphens,
        "grav_kw",
    )
    accent = Style.create(
        s.Large + s.bold + s.project.colors.accent + s.text.wrap.hyphens,
        "grav_acc",
    )
    highlight = Style.create(
        s.Large + s.bold + s.project.colors.highlight + s.text.wrap.hyphens,
        "grav_hl",
    )
bs = BlockStyles

_PROMPT = (
    f"{_PREFIX} A person standing at a crossroads. Left path shows lines of code "
    "in electric blue fading away. Right path shows glowing nodes (representing "
    "AI agents) arranged in a constellation pattern in teal and amber. "
    "The person faces the right path. "
    f"{_SUFFIX}"
)


def build():
    st_marker("The Shifting Center of Gravity")
    with st_block(_page_fill):
        with st_block(s.center_txt):
            with st_zoom(90):
                st_write(
                    bs.heading,
                    "The Shifting Center of Gravity",
                    tag=t.div, toc_lvl="1",
                )
            st_hover_tooltip(
                title="The Shifting Center of Gravity",
                entries=[
                    ("What changed", "A comprehensive analysis of 15 core SE tasks shows that 5 are either entirely new or radically elevated by generative AI (SOTA AI-4-SE, Section 9.1)."),
                    ("The shift", "Before GenAI, developers spent ~80% of their time writing code. Now, the dominant activities are specifying intent, engineering context, and validating AI output."),
                    ("Why it matters", "This means the skills that make a great developer are changing — orchestration and judgment replace typing speed and syntax knowledge."),
                ],
                scale="2vw", width="70vw", position="center",
            )
            with st_grid(cols="2fr 3fr", gap="24px", cell_styles=_cell) as g:
                with g.cell():
                    st_image(
                        s.none, width="80%",
                        editable=IS_EDITABLE,
                        name="gse_gravity_crossroads",
                        prompt=_PROMPT,
                        provider="openai",
                        ai_size="1024x1536",
                    )
                with g.cell():
                    with st_zoom(120):
                        st_write(
                            bs.body,
                            (bs.keyword, "Yesterday"),
                            (bs.body, " — write code, debug, deploy"),
                        )
                        st_space("v", 1)
                        st_write(
                            bs.body,
                            (bs.accent, "Tomorrow"),
                            (bs.body, " — specify intent, orchestrate agents, validate results"),
                        )
                        st_space("v", 1)
                        st_write(bs.highlight, "Code recedes. Orchestration advances.")
