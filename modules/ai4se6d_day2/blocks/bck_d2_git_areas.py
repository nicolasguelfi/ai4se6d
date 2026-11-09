"""Slide — The four areas of Git (diagram)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Diagram slide styles."""
    heading = s.project.titles.heading
    caption = Style.create(s.project.titles.body + s.center_txt, "d2_areas_caption")
    keyword = s.project.titles.keyword
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(75):
            st_write(bs.heading, "Where Your Changes Live", tag=t.div, toc_lvl="+1")
        st_space("v", 1)
        st_image(uri="images/am/bck_d2_git_areas_image_00.png", width="100%", max_vh=55, align="center")
        st_space("v", 1)
        st_write(
            bs.caption, (bs.keyword, "git add"), " chooses what goes into the next snapshot — ",
            (bs.keyword, "git commit"), " takes it.", tag=t.div,
        )
