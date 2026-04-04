"""Slide — Dozens to 100+ Layers: balanced image + key points."""
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
    "llm_layers_cell",
)


class BlockStyles:
    """Slide: Layers — maximize-viewport archetype: balanced."""
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(
        s.Large + s.text.wrap.hyphens,
        "llm_layers_body",
    )
    keyword = Style.create(
        s.Large + s.bold + s.project.colors.primary + s.text.wrap.hyphens,
        "llm_layers_keyword",
    )
bs = BlockStyles


# Master prompt components

_PROMPT = (
    f"{_PREFIX} A vertical stack of translucent horizontal planes, each containing a network "
    "of connected nodes. Bottom plane in teal, middle planes in electric blue with increasing "
    "opacity, top plane in amber. Represents dozens of transformer layers. "
    f"{_SUFFIX}"
)


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "Dozens to 100+ Layers", tag=t.div, toc_lvl="1")

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
                        name="llm_layers",
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
                                (bs.keyword, "Stacked"),
                                (bs.body, " \u2014 Tokens pass through dozens of Transformer layers"),
                            )
                        with l.item():
                            st_write(
                                bs.body,
                                (bs.keyword, "Refinement"),
                                (bs.body, " \u2014 Each layer deepens contextual understanding"),
                            )
                        with l.item():
                            st_write(
                                bs.body,
                                (bs.keyword, "More layers"),
                                (bs.body, " \u2014 deeper reasoning and relationships"),
                            )
