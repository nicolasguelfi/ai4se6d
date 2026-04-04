"""Slide — AI vs Generative AI: balanced image + key points."""
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
    "ai_vs_genai_cell",
)


class BlockStyles:
    """Slide: AI vs GenAI — maximize-viewport archetype: balanced."""
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(
        s.Large + s.text.wrap.hyphens,
        "ai_vs_genai_body",
    )
    keyword = Style.create(
        s.Large + s.bold + s.project.colors.primary + s.text.wrap.hyphens,
        "ai_vs_genai_keyword",
    )
bs = BlockStyles


# Master prompt components

_PROMPT = (
    f"{_PREFIX} Split composition: left side shows rigid geometric gears, decision trees, "
    "and binary logic gates in cool blue tones representing traditional AI. Right side shows "
    "flowing organic shapes, paintbrush strokes, musical notes, and code brackets in warm "
    f"amber and teal tones representing generative AI. A glowing divider separates both halves. {_SUFFIX}"
)


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "AI vs Generative AI", tag=t.div, toc_lvl="1")

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
                        name="ai_vs_genai",
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
                                (bs.keyword, "Traditional AI"),
                                (bs.body, " — rules, classification, prediction"),
                            )
                        with l.item():
                            st_write(
                                bs.body,
                                (bs.keyword, "Generative AI"),
                                (bs.body, " — creates new content (text, code, images)"),
                            )
                        with l.item():
                            st_write(
                                bs.body,
                                (bs.keyword, "Key difference"),
                                (bs.body, " — pattern recognition vs content creation"),
                            )
                        with l.item():
                            st_write(
                                bs.body,
                                (bs.keyword, "Since 2022"),
                                (bs.body, " — GPT-3.5 sparked the revolution"),
                            )
