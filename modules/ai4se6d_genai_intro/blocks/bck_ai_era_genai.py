"""Slide — 2022+ Generative AI: balanced image + key points."""
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
    "ai_era_genai_cell",
)


class BlockStyles:
    """Slide: Generative AI — maximize-viewport archetype: balanced."""
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(
        s.Large + s.text.wrap.hyphens,
        "ai_era_genai_body",
    )
    keyword = Style.create(
        s.Large + s.bold + s.project.colors.primary + s.text.wrap.hyphens,
        "ai_era_genai_keyword",
    )
bs = BlockStyles


# Master prompt components

_PROMPT = (
    f"{_PREFIX} An abstract explosion of creation: from a central electric blue core, "
    "streams of diverse shapes burst outward — code brackets, musical notes, image frames, "
    "document pages — all in teal and amber. Represents AI generating new content across "
    f"modalities. {_SUFFIX}"
)


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "2022+ — Generative AI", tag=t.div, toc_lvl="1")

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
                        name="ai_era_genai",
                        prompt=_PROMPT,
                        provider="openai",
                        ai_size="1024x1536",
                    )

                with g.cell():
                    with st_zoom(120):
                        with st_list(
                            list_type=lt.unordered,
                            li_style=bs.body,
                        ) as l:
                            with l.item():
                                st_write(
                                    bs.body,
                                    (bs.keyword, "Definition"),
                                    (bs.body, " — AI that generates new content "
                                    "(text, code, images, audio)"),
                                )
                            with l.item():
                                st_write(
                                    bs.body,
                                    (bs.keyword, "Scale"),
                                    (bs.body, " — Billions of parameters, trained "
                                    "on internet-scale data"),
                                )
                            with l.item():
                                st_write(
                                    bs.body,
                                    (bs.keyword, "Explosion"),
                                    (bs.body, " — ChatGPT: 100M users in 2 months "),
                                    (s.project.citation + s.Large, cite("altman2022chatgpt")),
                                )
                            with l.item():
                                st_write(
                                    bs.body,
                                    (bs.keyword, "Impact"),
                                    (bs.body, " — Transforms how we write, code, "
                                    "create, and reason"),
                                )
