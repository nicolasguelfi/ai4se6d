"""Slide — You're Not Alone: AI adoption stats with image.

Stack Overflow Developer Survey 2026 (AI section, all respondents; NG, 2026-11-22): 83% use at least one AI
tool at work (n = 17,464); 77% of them use AI daily (n = 14,478); 69.3% use AI to generate code in a familiar
area (n = 12,547). Gartner (2025): 90% of enterprise software engineers will use AI code assistants by 2028.
"""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.styles import Style as ns
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX


_page_fill = s.project.containers.page_fill_top

# Cell centering for grid
_cell = Style.create(
    s.container.layouts.vertical_center_layout + s.center_txt,
    "poll_ai_result_cell",
)


class BlockStyles:
    """Slide: AI Stats — maximize-viewport archetype: balanced."""
    heading = s.project.titles.slide_title + s.center_txt
    stat_hero = Style.create(
        s.project.colors.highlight + s.bold
        + ns("font-size:96pt;line-height:1.1;", "poll_stat_hero_size"),
        "poll_stat_hero",
    )
    body = Style.create(
        s.Large + s.text.wrap.hyphens,
        "poll_ai_result_body",
    )
    keyword = Style.create(
        s.Large + s.bold + s.project.colors.highlight + s.text.wrap.hyphens,
        "poll_ai_result_keyword",
    )
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles


# Master prompt components

_PROMPT = (
    f"{_PREFIX} A large circular progress chart at 83%, rendered as a glowing electric "
    "blue arc on dark background. Inside the circle, a simple developer silhouette icon "
    f"in teal. Amber accent dot marks the percentage endpoint. {_SUFFIX}"
)


def build():
    with st_block(_page_fill):
        with st_zoom(130),st_block(s.center_txt):
            st_write(bs.heading, "You're Not Alone", tag=t.div, toc_lvl="1")

            with st_grid(
                cols="1.5fr 3.5fr",
                gap="24px",
                cell_styles=_cell,
            ) as g:
                with g.cell():
                    st_image(
                        s.none,
                        width="80%",
                        editable=IS_EDITABLE,
                        name="poll_ai_result",
                        prompt=_PROMPT,
                        provider="openai",
                        ai_size="1024x1536",
                    )

                with g.cell():
                    st_write(bs.stat_hero, "83%")
                    st_space("v", 0.5)
                    with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered,item_gap=0.5) as l:
                        with l.item():
                            st_write(
                                bs.body,
                                (bs.keyword, "83%"),
                                (bs.body, " use AI tools at work"),
                            )
                        with l.item():
                            st_write(
                                bs.body,
                                (bs.keyword, "77%"),
                                (bs.body, " of them use AI daily"),
                            )
                        with l.item():
                            st_write(
                                bs.body,
                                (bs.keyword, "69%"),
                                (bs.body, " generate code with AI"),
                            )
                        with l.item():
                            st_write(
                                bs.body,
                                (bs.keyword, "90%"),
                                (bs.body, " will use AI assistants by 2028"),
                            )
                    st_space("v", 0.5)
                    st_write(
                        bs.source,
                        cite("so-survey2026"),
                        " ",
                        cite("gartner-se2025"),
                    )
