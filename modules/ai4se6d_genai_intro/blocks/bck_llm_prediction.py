"""Slide — Step 4: Prediction: balanced image + key points."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.styles import Style as ns
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX


# Viewport-filling container
_page_fill = ns(
    "display:flex;flex-direction:column;justify-content:flex-start;"
    "min-height:85vh;gap:1.5rem;",
    "page_fill_llm_prediction",
)

# Cell centering for grid
_cell = Style.create(
    s.container.layouts.vertical_center_layout + s.center_txt,
    "llm_prediction_cell",
)


class BlockStyles:
    """Slide: Prediction — maximize-viewport archetype: balanced."""
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(
        s.Large + s.text.wrap.hyphens,
        "llm_prediction_body",
    )
    keyword = Style.create(
        s.Large + s.bold + s.project.colors.primary + s.text.wrap.hyphens,
        "llm_prediction_keyword",
    )
bs = BlockStyles


# Master prompt components

_PROMPT = (
    f"{_PREFIX} A horizontal bar chart with about 8 bars of different heights. "
    "Tallest bar glows in amber (highest probability), others in electric blue of "
    "decreasing brightness. Below the bars, a subtle row of small squares represents "
    f"the vocabulary. {_SUFFIX}"
)


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "Step 4: Prediction", tag=t.div, toc_lvl="1")

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
                        name="llm_prediction",
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
                                (bs.keyword, "Distribution"),
                                (bs.body, " \u2014 Probability over the entire 30K-100K vocabulary"),
                            )
                        with l.item():
                            st_write(
                                bs.body,
                                (bs.keyword, "Selection"),
                                (bs.body, " \u2014 Sample or pick the most probable next token"),
                            )
                        with l.item():
                            st_write(
                                bs.body,
                                (bs.keyword, "Reasoning"),
                                (bs.body, " \u2014 Emerges from prediction at massive scale"),
                            )
                        with l.item():
                            st_write(
                                bs.body,
                                (bs.keyword, "Code & writing"),
                                (bs.body, " \u2014 Same principle, applied to any language"),
                            )
