"""Slide — VibeCoding Principle 2: Trust in Output."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX


_page_fill = s.project.containers.page_fill_top

_cell = Style.create(
    s.container.layouts.vertical_center_layout + s.center_txt,
    "vc_trust_cell",
)


class BlockStyles:
    """Principle 2 slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    number = Style.create(
        s.Giant + s.bold + s.project.colors.highlight + s.center_txt,
        "vc_trust_number",
    )
bs = BlockStyles


_PROMPT = (
    f"{_PREFIX} A glowing checkmark in amber hovering over a code window outline in "
    "electric blue. The code lines inside are blurred and abstract, completely unread. "
    "The checkmark is crisp and confident. Represents accepting output without reading "
    f"the code, trusting the result over the implementation. {_SUFFIX}"
)


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "Trust in Output", tag=t.div, toc_lvl="1")

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
                        name="vc_trust",
                        prompt=_PROMPT,
                        provider="openai",
                        ai_size="1024x1536",
                    )

                with g.cell():
                    st_write(bs.number, "2")
                    st_space("v", 1)
                    with st_zoom(160):
                        st_write(
                                bs.body,
                                (bs.keyword, "If it works = good enough."),
                            )
                    st_space("v", 1)
                    st_write(
                        bs.body,
                        "The developer accepts generated code based on whether "
                        "the application works, not on whether the code is correct, "
                        "efficient, or maintainable.",
                    )
                    st_space("v", 1)
                    st_write(
                        bs.body,
                        "The code itself is not read.",
                    )
