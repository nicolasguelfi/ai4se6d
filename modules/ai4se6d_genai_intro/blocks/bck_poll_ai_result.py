"""Slide — You're Not Alone: AI adoption stats with image."""
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
    "page_fill_poll_ai_result",
)

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
    source = Style.create(
        s.project.titles.caption + s.center_txt,
        "poll_ai_result_source",
    )
bs = BlockStyles


# Master prompt components

_PROMPT = (
    f"{_PREFIX} A large circular progress chart at 84%, rendered as a glowing electric "
    "blue arc on dark background. Inside the circle, a simple developer silhouette icon "
    f"in teal. Amber accent dot marks the percentage endpoint. {_SUFFIX}"
)


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "You're Not Alone", tag=t.div, toc_lvl="1")

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
                        name="poll_ai_result",
                        prompt=_PROMPT,
                        provider="openai",
                        ai_size="1024x1536",
                    )

                with g.cell():
                    st_write(bs.stat_hero, "84%")
                    st_space("v", 0.5)
                    with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                        with l.item():
                            st_write(
                                bs.body,
                                (bs.keyword, "84%"),
                                (bs.body, " use or plan to use AI tools"),
                            )
                        with l.item():
                            st_write(
                                bs.body,
                                (bs.keyword, "51%"),
                                (bs.body, " use AI tools daily"),
                            )
                        with l.item():
                            st_write(
                                bs.body,
                                (bs.keyword, "85%"),
                                (bs.body, " regularly use AI for coding"),
                            )
                        with l.item():
                            st_write(
                                bs.body,
                                (bs.keyword, "90%"),
                                (bs.body, " will use AI assistants by 2028"),
                            )
                    st_space("v", 0.5)
                    st_write(bs.source, "Stack Overflow 2025 · JetBrains · Gartner")
