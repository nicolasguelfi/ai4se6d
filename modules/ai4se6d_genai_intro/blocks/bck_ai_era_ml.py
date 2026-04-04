"""Slide — 1990s Machine Learning: balanced image + key points."""
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
    "ai_era_ml_cell",
)


class BlockStyles:
    """Slide: Machine Learning — maximize-viewport archetype: balanced."""
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(
        s.Large + s.text.wrap.hyphens,
        "ai_era_ml_body",
    )
    keyword = Style.create(
        s.Large + s.bold + s.project.colors.primary + s.text.wrap.hyphens,
        "ai_era_ml_keyword",
    )
bs = BlockStyles


# Master prompt components

_PROMPT = (
    f"{_PREFIX} A scatter plot of data points in teal, with a smooth electric blue curve "
    "fitting through them. A few amber outlier points. Clean axes without labels. "
    f"Represents learning patterns from data. {_SUFFIX}"
)


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "1990s — Machine Learning", tag=t.div, toc_lvl="1")

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
                        name="ai_era_ml",
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
                                (bs.keyword, "Data-driven"),
                                (bs.body, " — Algorithms learn from examples, not rules"),
                            )
                        with l.item():
                            st_write(
                                bs.body,
                                (bs.keyword, "Paradigms"),
                                (bs.body, " — Supervised, unsupervised, reinforcement"),
                            )
                        with l.item():
                            st_write(
                                bs.body,
                                (bs.keyword, "Limitation"),
                                (bs.body, " — Requires hand-crafted features"),
                            )
