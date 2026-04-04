"""Slide — Discriminative Models: balanced image + key points."""
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
    "ai_discriminative_cell",
)


class BlockStyles:
    """Slide: Discriminative Models — maximize-viewport archetype: balanced."""
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(
        s.Large + s.text.wrap.hyphens,
        "ai_discriminative_body",
    )
    keyword = Style.create(
        s.Large + s.bold + s.project.colors.primary + s.text.wrap.hyphens,
        "ai_discriminative_keyword",
    )
bs = BlockStyles


# Master prompt components

_PROMPT = (
    f"{_PREFIX} A funnel shape in electric blue receiving mixed geometric shapes "
    "(circles, squares, triangles) on top and sorting them into two clean groups below, "
    "separated by a teal dividing line. Represents classification and analysis. "
    f"{_SUFFIX}"
)


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "Discriminative Models", tag=t.div, toc_lvl="1")

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
                        name="ai_discriminative",
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
                                (bs.body, " — Learn to distinguish between categories"),
                            )
                        with l.item():
                            st_write(
                                bs.body,
                                (bs.keyword, "Probability"),
                                (bs.body, " — Model P(y|x): what class does this belong to?"),
                            )
                        with l.item():
                            st_write(
                                bs.body,
                                (bs.keyword, "Approach"),
                                (bs.body, " — Map inputs to labels, not generate new data"),
                            )
                        with l.item():
                            st_write(
                                bs.body,
                                (bs.keyword, "Examples"),
                                (bs.body, " — Spam detection, image classification, sentiment"),
                            )
