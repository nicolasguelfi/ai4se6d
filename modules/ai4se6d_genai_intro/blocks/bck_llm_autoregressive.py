"""Slide — Autoregressive Generation: balanced image + key points."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX


_page_fill = s.project.containers.page_fill_top

# Cell centering for grid
_cell = Style.create(
    s.container.layouts.vertical_center_layout + s.center_txt,
    "llm_autoregressive_cell",
)


class BlockStyles:
    """Slide: Autoregressive Generation — maximize-viewport archetype: balanced."""
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(
        s.Large + s.text.wrap.hyphens,
        "llm_autoregressive_body",
    )
    keyword = Style.create(
        s.Large + s.bold + s.project.colors.primary + s.text.wrap.hyphens,
        "llm_autoregressive_keyword",
    )
bs = BlockStyles


# Master prompt components

_PROMPT = (
    f"{_PREFIX} A spiral or growing chain: starting from a small teal circle, each step "
    "adds a new circle that is slightly larger, connected by electric blue arrows. The "
    "newest circle glows amber. The chain curves gently, suggesting continuous growth. "
    f"{_SUFFIX}"
)


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "Autoregressive Generation", tag=t.div, toc_lvl="1")

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
                        name="llm_autoregressive",
                        prompt=_PROMPT,
                        provider="openai",
                        ai_size="1024x1536",
                    )

                with g.cell():
                    with st_list(
                        list_type=lt.unordered,
                        li_style=bs.body,
                    ) as l:
                        with l.item():
                            st_write(
                                bs.body,
                                (bs.keyword, "Loop"),
                                (bs.body, " — Predict → append → repeat"),
                            )
                        with l.item():
                            st_write(
                                bs.body,
                                (bs.keyword, "Speed"),
                                (bs.body, " — Response time proportional to length"),
                            )
                        with l.item():
                            st_write(
                                bs.body,
                                (bs.keyword, "Cost"),
                                (bs.body, " — Each token = one full forward pass"),
                            )
