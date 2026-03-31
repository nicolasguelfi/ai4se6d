"""Slide 9 — Balanced: Training vs Inference."""
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
    "page_fill_training",
)

# Cell centering: vertical + horizontal
_cell_center = Style.create(
    s.container.layouts.vertical_center_layout + s.center_txt,
    "training_cell_center",
)


class BlockStyles:
    """Slide: Training vs Inference — maximize-viewport archetype: balanced (image + list)."""
    heading = s.project.titles.section_title + s.center_txt
    body = Style.create(
        s.project.titles.body + s.text.wrap.hyphens,
        "training_body",
    )
    keyword = Style.create(
        s.project.titles.body_accent,
        "training_keyword",
    )
bs = BlockStyles

# Master prompt components

TRAINING_PROMPT = (
    f"{_PREFIX} A split composition: on the left, a massive funnel absorbing hundreds of "
    "tiny glowing data particles (electric blue) into a central glowing cube (the model), "
    "representing the training phase. On the right, the same cube emitting a single focused "
    "beam of teal light toward one small output node, representing inference. "
    "An amber arrow connects the two phases. The left side is dense and heavy, "
    f"the right side is light and fast. {_SUFFIX}"
)


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(
                bs.heading,
                "Training vs Inference",
                tag=t.div,
                toc_lvl="1",
            )

            with st_grid(
                cols="2fr 3fr",
                gap="24px",
                cell_styles=_cell_center,
            ) as g:
                # Left: AI image
                with g.cell():
                    st_image(
                        s.none,
                        width="80%",
                        editable=IS_EDITABLE,
                        name="training_vs_inference",
                        prompt=TRAINING_PROMPT,
                        provider="openai",
                        ai_size="1024x1536",
                    )

                # Right: 4 key points
                with g.cell():
                    with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                        with l.item():
                            st_write(bs.body, (bs.keyword, "Training"), (bs.body, " — months, billions of tokens, massive GPUs"))
                        with l.item():
                            st_write(bs.body, (bs.keyword, "Fine-tuning"), (bs.body, " — adapt to specific tasks, smaller dataset"))
                        with l.item():
                            st_write(bs.body, (bs.keyword, "Inference"), (bs.body, " — milliseconds, one prompt \u2192 one response"))
                        with l.item():
                            st_write(bs.body, (bs.keyword, "Cost"), (bs.body, " — training = millions $, inference = fractions of cents"))
