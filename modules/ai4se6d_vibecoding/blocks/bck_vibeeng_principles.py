"""Slide — 5 Principles of VibeEngineering."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.styles import Style as ns
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX


# Viewport-filling container
_page_fill = ns(
    "display:flex;flex-direction:column;justify-content:flex-start;"
    "min-height:85vh;gap:1.5rem;",
    "page_fill_vibeeng_principles",
)

# Cell centering for grid
_cell = Style.create(
    s.container.layouts.vertical_center_layout + s.center_txt,
    "vibeeng_principles_cell",
)


class BlockStyles:
    """VibeEngineering principles slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = Style.create(s.bold + s.project.colors.primary + s.Large, "vibeeng_pr_keyword")
    keyword_accent = Style.create(s.bold + s.project.colors.accent + s.Large, "vibeeng_pr_keyword_accent")
bs = BlockStyles


_PROMPT = (
    f"{_PREFIX} A sturdy bridge made of five glowing pillars connecting two platforms. "
    "Left platform is chaotic with scattered code fragments. Right platform is orderly "
    "with structured blueprints. Each pillar glows in alternating electric blue and teal. "
    "Amber light flows across the bridge top. Symbolizes engineering discipline "
    f"as the bridge from chaos to quality. {_SUFFIX}"
)


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "6 Principles of VibeEngineering", tag=t.div, toc_lvl="1")

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
                        name="vibeeng_principles",
                        prompt=_PROMPT,
                        provider="openai",
                        ai_size="1024x1536",
                    )

                with g.cell():
                    with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
                        with l.item():
                            st_write(bs.body, (bs.keyword, "Requirements Before Prompts"), " \u2014 define WHAT and WHY first")
                        with l.item():
                            st_write(bs.body, (bs.keyword, "Test-Driven Generation"), " \u2014 tests BEFORE implementation (TDD/BDD)")
                        with l.item():
                            st_write(bs.body, (bs.keyword, "Architectural Intent"), " \u2014 .cursorrules, CLAUDE.md constrain AI")
                        with l.item():
                            st_write(bs.body, (bs.keyword, "Iterative Refinement"), " \u2014 planned iterations with review gates")
                        with l.item():
                            st_write(bs.body, (bs.keyword, "Human Review at Boundaries"), " \u2014 review at critical points, not every line")
                        with l.item():
                            st_write(bs.body, (bs.keyword_accent, "Context Engineering"), " \u2014 systematic info management, not clever prompting")
