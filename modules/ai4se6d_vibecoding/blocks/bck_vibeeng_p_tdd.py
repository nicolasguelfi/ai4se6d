"""Slide — P2: Test-Driven Generation."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX


_page_fill = s.project.containers.page_fill_top

_cell = Style.create(
    s.container.layouts.vertical_center_layout + s.center_txt,
    "ve_p2_cell",
)


class BlockStyles:
    """P2 slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    number = Style.create(
        s.Giant + s.bold + s.project.colors.highlight + s.center_txt,
        "ve_p2_number",
    )
bs = BlockStyles


_PROMPT = (
    f"{_PREFIX} A test tube or verification checkmark icon in amber standing tall "
    "on the left, casting a protective shadow over code blocks in electric blue. "
    f"{_SUFFIX}"
)


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "P2 — Test-Driven Generation", tag=t.div, toc_lvl="1")

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
                        name="ve_p2_tdd",
                        prompt=_PROMPT,
                        provider="openai",
                        ai_size="1024x1536",
                    )

                with st_zoom(130), g.cell():
                    st_write(bs.number, "2")
                    st_space("v", 1)
                    st_write(
                        bs.body,
                        "Tests written ",
                        (bs.keyword, "BEFORE"),
                        " implementation.<br>",
                        "Tests define the ",
                        (bs.keyword, "contract"),
                        ". AI generates code that must pass.",
                    )
                    st_space("v", 1)
                    st_write(
                        bs.body,
                        (s.project.colors.muted, "Taste at every step, not just "
                         "when the plate is served."),
                    )
