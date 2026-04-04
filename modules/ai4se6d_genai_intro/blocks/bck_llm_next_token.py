"""Slide — Next-Token Prediction: balanced image + key points."""
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
    "llm_next_token_cell",
)


class BlockStyles:
    """Slide: Next-Token Prediction — maximize-viewport archetype: balanced."""
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(
        s.Large + s.text.wrap.hyphens,
        "llm_next_token_body",
    )
    keyword = Style.create(
        s.Large + s.bold + s.project.colors.primary + s.text.wrap.hyphens,
        "llm_next_token_keyword",
    )
bs = BlockStyles


# Master prompt components

_PROMPT = (
    f"{_PREFIX} A sequence of 5 solid electric blue circles in a row followed by one "
    "pulsing amber circle with a question mark glow. A subtle arrow curves from all "
    "previous circles toward the amber one. Represents predicting the next token from "
    f"context. {_SUFFIX}"
)


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "Next-Token Prediction", tag=t.div, toc_lvl="1")

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
                        name="llm_next_token",
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
                                (bs.keyword, "The principle"),
                                (bs.body, " — Predict the most plausible next token"),
                            )
                        with l.item():
                            st_write(
                                bs.body,
                                (bs.keyword, "Reasoning"),
                                (bs.body, " — Emerges from prediction at massive scale"),
                            )
                        with l.item():
                            st_write(
                                bs.body,
                                (bs.keyword, "Code generation"),
                                (bs.body, " — Same principle, applied to source code"),
                            )
                        with l.item():
                            st_write(
                                bs.body,
                                (bs.keyword, "Creative writing"),
                                (bs.body, " — Fluency from statistical patterns"),
                            )
