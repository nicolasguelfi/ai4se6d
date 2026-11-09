"""Slide — The core loop with opencode: describe, let the agent build, run, react."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Core loop slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    num = Style.create(s.project.titles.stat + s.center_txt, "setup_loop_num")
    name = Style.create(s.project.titles.body_accent + s.center_txt, "setup_loop_name")
    hint = Style.create(s.project.titles.table_cell + s.center_txt, "setup_loop_hint")
    body = Style.create(s.project.titles.body + s.center_txt, "setup_loop_body")
    keyword = s.bold + s.project.colors.primary
    caption = Style.create(s.project.titles.caption + s.center_txt, "setup_loop_caption")
bs = BlockStyles

_LOOP = [
    ("1", "Describe", "what you want, in plain English"),
    ("2", "Let it build", "it reads, writes files, runs commands"),
    ("3", "Run", "open the result in your browser"),
    ("4", "React", "say what is wrong, or what is next"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "The Core Loop", tag=t.div, toc_lvl="1")
        st_space("v", 1)
        with st_grid(
            cols="repeat(auto-fit, minmax(260px, 1fr))",
            gap="16px",
            cell_styles=s.project.containers.table_normal_cell,
        ) as g:
            for num, name, hint in _LOOP:
                with g.cell():
                    st_write(bs.num, num, tag=t.div)
                    st_write(bs.name, name, tag=t.div)
                    st_write(bs.hint, hint, tag=t.div)
        st_space("v", 1)
        st_write(bs.body, "…and back to 1. That is ", (bs.keyword, "all you need today"), ".", tag=t.div)
        st_write(bs.caption, "opencode asks before some actions: read the request before you accept.", tag=t.div)
