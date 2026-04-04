"""Slide — The GenAI Landscape: balanced image + tool categories."""
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
    "landscape_cell",
)


class BlockStyles:
    """Slide: GenAI Landscape — maximize-viewport archetype: balanced."""
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(
        s.Large + s.text.wrap.hyphens,
        "landscape_body",
    )
    keyword = Style.create(
        s.Large + s.bold + s.project.colors.accent + s.text.wrap.hyphens,
        "landscape_keyword",
    )
bs = BlockStyles


# Master prompt components

_PROMPT = (
    f"{_PREFIX} A network constellation of interconnected glowing nodes arranged in four "
    "clusters. Each cluster is a different color: electric blue cluster (top-left), "
    "teal cluster (top-right), amber cluster (bottom-left), white cluster (bottom-right). "
    "Thin luminous lines connect nodes within and between clusters. Central hub node "
    f"slightly larger, connecting all four clusters. {_SUFFIX}"
)


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "The GenAI Landscape", tag=t.div, toc_lvl="1")

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
                        name="genai_landscape",
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
                                (bs.keyword, "Chat"),
                                (bs.body, " — ChatGPT, Claude, Gemini"),
                            )
                        with l.item():
                            st_write(
                                bs.body,
                                (bs.keyword, "Code"),
                                (bs.body, " — GitHub Copilot, Cursor, Claude Code"),
                            )
                        with l.item():
                            st_write(
                                bs.body,
                                (bs.keyword, "Image"),
                                (bs.body, " — DALL-E, Midjourney, Stable Diffusion"),
                            )
                        with l.item():
                            st_write(
                                bs.body,
                                (bs.keyword, "Enterprise"),
                                (bs.body, " — Microsoft 365 Copilot, Google Workspace AI"),
                            )
