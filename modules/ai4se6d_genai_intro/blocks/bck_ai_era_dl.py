"""Slide — 2010s Deep Learning: balanced image + key points."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX


_page_fill = s.project.containers.page_fill_top

# Cell centering for grid
_cell = Style.create(
    s.container.layouts.vertical_center_layout + s.center_txt,
    "ai_era_dl_cell",
)


class BlockStyles:
    """Slide: Deep Learning — maximize-viewport archetype: balanced."""
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(
        s.Large + s.text.wrap.hyphens,
        "ai_era_dl_body",
    )
    keyword = Style.create(
        s.Large + s.bold + s.project.colors.primary + s.text.wrap.hyphens,
        "ai_era_dl_keyword",
    )
bs = BlockStyles


# Master prompt components

_PROMPT = (
    f"{_PREFIX} Layered horizontal rows of interconnected circles forming a deep neural "
    "network. Input layer in teal, hidden layers in electric blue with increasing glow "
    "intensity, output layer in amber. Connections shown as thin white lines. "
    f"{_SUFFIX}"
)


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "2010s — Deep Learning", tag=t.div, toc_lvl="1")

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
                        name="ai_era_dl",
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
                                (bs.keyword, "Definition"),
                                (bs.body, " — Neural networks learn features "
                                 "automatically from raw data"),
                            )
                        with l.item():
                            st_write(
                                bs.body,
                                (bs.keyword, "Enablers"),
                                (bs.body, " — ReLU + GPU power + massive "
                                 "datasets + embeddings"),
                            )
                        with l.item():
                            st_write(
                                bs.body,
                                (bs.keyword, "Breakthrough"),
                                (bs.body, " — Transformer architecture "),
                                (bs.body, cite("vaswani2017attention")),
                            )
                        with l.item():
                            st_write(
                                bs.body,
                                (bs.keyword, "Limitation"),
                                (bs.body, " — Requires massive compute and "
                                 "data; models are black boxes"),
                            )
