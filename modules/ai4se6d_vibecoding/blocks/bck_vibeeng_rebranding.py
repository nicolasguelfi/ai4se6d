"""Slide — From Coding to Engineering (skippable)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX


_page_fill = s.project.containers.page_fill_top

_cell = Style.create(
    s.container.layouts.vertical_center_layout + s.center_txt,
    "ve_rebrand_cell",
)


class BlockStyles:
    """Rebranding slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    accent = s.bold + s.project.colors.accent
    highlight = s.bold + s.project.colors.highlight
bs = BlockStyles


_PROMPT = (
    f"{_PREFIX} A loose fluid shape in teal morphing into a precise structured "
    "geometric form in electric blue. An amber arrow shows the transformation "
    f"direction. {_SUFFIX}"
)


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "From Coding to Engineering", tag=t.div, toc_lvl="1")

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
                        name="ve_rebranding",
                        prompt=_PROMPT,
                        provider="openai",
                        ai_size="1024x1536",
                    )

                with st_zoom(130), g.cell():
                    st_write(
                        bs.body,
                        (bs.keyword, "Kent Beck"),
                        " drew the line: ",
                        (bs.accent, '"vibe coding"'),
                        " is when you don't read the code. ",
                        "Engineering is when you ",
                        (bs.keyword, "own"),
                        " every decision.",
                    )
                    st_space("v", 1)
                    st_write(
                        bs.body,
                        "By early 2026, Karpathy's term evolved into ",
                        (bs.highlight, '"agentic engineering"'),
                        " — AI agents executing, humans steering.",
                    )
                    st_space("v", 1)
                    st_write(
                        bs.body,
                        (s.project.colors.muted, "The kitchen upgrades its tools — "
                         "but the chef still designs the menu."),
                    )
