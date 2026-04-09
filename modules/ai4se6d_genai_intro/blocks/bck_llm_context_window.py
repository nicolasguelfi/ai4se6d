"""Slide — Context Windows: balanced image + key points."""
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
    "llm_context_window_cell",
)


class BlockStyles:
    """Slide: Context Windows — maximize-viewport archetype: balanced."""
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(
        s.Large + s.text.wrap.hyphens,
        "llm_context_window_body",
    )
    keyword = Style.create(
        s.Large + s.bold + s.project.colors.primary + s.text.wrap.hyphens,
        "llm_context_window_keyword",
    )
bs = BlockStyles


# Master prompt components

_PROMPT = (
    f"{_PREFIX} A vertical wall of dense horizontal lines in very dark gray, representing "
    "a massive body of text. A conical flashlight beam shines from the top, illuminating "
    "a portion of the lines. The illuminated zone is crisp and bright: a narrow teal cone "
    "at the top (small context, early models) gradually widening into a large amber cone "
    "at the bottom (huge context, current models). Lines inside the beam glow in electric "
    "blue and are clearly visible. Lines outside the beam fade into near-black darkness. "
    "The boundary between light and shadow is sharp and geometric, representing the hard "
    f"limit of what the model can see. {_SUFFIX}"
)


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "Context Windows", tag=t.div, toc_lvl="1")

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
                        name="llm_context_window",
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
                                    (bs.keyword, "Working memory"),
                                    (bs.body, " — Everything the model 'sees' at once"),
                                )
                            with l.item():
                                st_write(
                                    bs.body,
                                    (bs.keyword, "Early models"),
                                    (bs.body, " — 2,048-4,096 tokens"),
                                )
                            with l.item():
                                st_write(
                                    bs.body,
                                    (bs.keyword, "Current models"),
                                    (bs.body, " — 128,000 to 10,000,000 tokens"),
                                )
                            with l.item():
                                st_write(
                                    bs.body,
                                    (bs.keyword, "Boundary"),
                                    (bs.body, " — Defines what the model 'knows' per conversation"),
                                )
