"""Slide — P6: Context Engineering (skippable)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX


_page_fill = s.project.containers.page_fill_top

_cell = Style.create(
    s.container.layouts.vertical_center_layout + s.center_txt,
    "ve_p6_cell",
)


class BlockStyles:
    """P6 slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    accent = s.bold + s.project.colors.accent
    number = Style.create(
        s.Giant + s.bold + s.project.colors.highlight + s.center_txt,
        "ve_p6_number",
    )
bs = BlockStyles


_PROMPT = (
    f"{_PREFIX} A central hub circle in amber surrounded by orbiting information "
    "spheres in electric blue and teal — documents, rules, tools. Lines connect "
    f"everything. {_SUFFIX}"
)


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "P6 — Context Engineering", tag=t.div, toc_lvl="1")

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
                        name="ve_p6_context",
                        prompt=_PROMPT,
                        provider="openai",
                        ai_size="1024x1536",
                    )

                with st_zoom(130), g.cell():
                    st_write(bs.number, "6")
                    st_space("v", 1)
                    st_write(
                        bs.body,
                        "Designing the ",
                        (bs.keyword, "optimal information environment"),
                        " for AI agents.",
                    )
                    st_space("v", 1)
                    st_write(
                        bs.body,
                        (bs.accent, "Project rules"),
                        ", ",
                        (bs.accent, "MCP servers"),
                        ", ",
                        (bs.accent, "memory systems"),
                        " — the agent sees what you curate.",
                    )
                    st_space("v", 1)
                    st_write(
                        bs.body,
                        (s.project.colors.muted, "Your mise en place — everything "
                         "prepared before the first flame."),
                    )
