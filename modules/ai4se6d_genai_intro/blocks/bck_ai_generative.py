"""Slide — Generative Models: balanced image + key points."""
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
    "ai_generative_cell",
)


class BlockStyles:
    """Slide: Generative Models — maximize-viewport archetype: balanced."""
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(
        s.Large + s.text.wrap.hyphens,
        "ai_generative_body",
    )
    keyword = Style.create(
        s.Large + s.bold + s.project.colors.primary + s.text.wrap.hyphens,
        "ai_generative_keyword",
    )
bs = BlockStyles


# Master prompt components

_PROMPT = (
    f"{_PREFIX} A single electric blue seed/spark at the center, from which new unique "
    "geometric shapes bloom outward in teal and amber — each shape slightly different but "
    "harmonious. Represents creation of new content from learned patterns. "
    f"{_SUFFIX}"
)


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "Generative Models", tag=t.div, toc_lvl="1")

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
                        name="ai_generative",
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
                                (bs.body, " — Learn to produce new data from training distribution"),
                            )
                        with l.item():
                            st_write(
                                bs.body,
                                (bs.keyword, "Probability"),
                                (bs.body, " — Model P(x,y): what would plausible output look like?"),
                            )
                        with l.item():
                            st_write(
                                bs.body,
                                (bs.keyword, "Approach"),
                                (bs.body, " — Generate new content, not just classify existing"),
                            )
                        with l.item():
                            st_write(
                                bs.body,
                                (bs.keyword, "Examples"),
                                (bs.body, " — Code generation, text creation, image synthesis"),
                            )
