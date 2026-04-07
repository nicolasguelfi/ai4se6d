"""Slide — Step 1: Tokenization: balanced image + key points."""
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
    "llm_tokenization_cell",
)


class BlockStyles:
    """Slide: Tokenization — maximize-viewport archetype: balanced."""
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(
        s.Large + s.text.wrap.hyphens,
        "llm_tokenization_body",
    )
    keyword = Style.create(
        s.Large + s.bold + s.project.colors.primary + s.text.wrap.hyphens,
        "llm_tokenization_keyword",
    )
bs = BlockStyles


# Master prompt components

_PROMPT = (
    f"{_PREFIX} A sentence represented as a continuous electric blue ribbon being cut by "
    "teal scissors into smaller segments. Each segment becomes a separate glowing tile. "
    f"Represents text being split into tokens. {_SUFFIX}"
)


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "Step 1: Tokenization", tag=t.div, toc_lvl="1")

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
                        name="llm_tokenization",
                        prompt=_PROMPT,
                        provider="openai",
                        ai_size="1024x1536",
                    )

                with g.cell():
                  with st_zoom(130):
                    with st_list(
                        list_type=lt.unordered,
                        li_style=bs.body,
                    ) as l:
                        with l.item():
                            st_write(
                                bs.body,
                                (bs.keyword, "Subword units"),
                                (bs.body, " \u2014 Text split into 3-4 character pieces"),
                            )
                        with l.item():
                            st_write(
                                bs.body,
                                (bs.keyword, "Example"),
                                (bs.body, " \u2014 'developer' \u2192 ['_develop', 'er']"),
                            )
                        with l.item():
                            st_write(
                                bs.body,
                                (bs.keyword, "Numerical IDs"),
                                (bs.body, " \u2014 Each token mapped to a unique number"),
                            )
