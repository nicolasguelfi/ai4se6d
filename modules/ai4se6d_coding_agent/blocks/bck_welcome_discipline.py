"""Slide — Same tools, different discipline."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Framing slide styles."""
    heading = s.project.titles.heading
    line = Style.create(s.project.titles.body + s.center_txt, "disc_line")
    punch = Style.create(
        s.huge + s.bold + s.project.colors.highlight + s.center_txt, "disc_punch",
    )
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_center):
        with st_zoom(75):
            st_write(bs.heading, "Same Tools, New Discipline", tag=t.div, toc_lvl="+1")
        st_space("v", 2)
        st_write(bs.line, "Yesterday you explored. Today you engineer.", tag=t.div)
        st_space("v", 1)
        st_write(bs.line, "opencode is still opencode.", tag=t.div)
        st_space("v", 2)
        st_write(bs.punch, "What changes is how you drive it.", tag=t.div)
