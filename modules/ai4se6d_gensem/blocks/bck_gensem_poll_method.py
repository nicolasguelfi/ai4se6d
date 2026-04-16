"""Slide — Quick Poll: do you follow a method when coding with AI?"""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Poll slide styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    option_label = s.bold + s.project.colors.accent + s.project.titles.body
    option_text = s.project.titles.body

bs = BlockStyles


_OPTIONS = [
    ("A", "I just prompt and see what happens"),
    ("B", "I have informal habits"),
    ("C", "I follow a structured process"),
    ("D", "What AI?"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(90):
            st_write(bs.heading, "Quick Poll", tag=t.div, toc_lvl="1")
        st_space("v", 1)
        st_write(
            bs.body,
            "When coding with AI, do you currently follow a method?",
        )
        st_space("v", 2)

        with st_grid(
            cols="repeat(auto-fit, minmax(280px, 1fr))",
            gap="16px",
            cell_styles=s.project.containers.cell_primary_bg
            + s.project.containers.cell_pad_md,
        ) as g:
            for label, text in _OPTIONS:
                with g.cell():
                    st_write(bs.option_label, f"({label})", tag=t.div)
                    st_space("v", 0.5)
                    st_write(bs.option_text, text)
