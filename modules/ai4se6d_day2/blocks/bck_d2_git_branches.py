"""Slide — Pattern 3: one branch per task (diagram)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Branch pattern styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.center_txt, "d2_gitbr_body")
    keyword = s.project.titles.keyword
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(75):
            st_write(bs.heading, "3 · One Branch per Task", tag=t.div, toc_lvl="+1")
        st_image(uri="images/am/bck_d2_git_branches_image_00.png", width="100%", max_vh=62, align="center")
        st_write(
            bs.body, (bs.keyword, "git switch -c feat/&lt;task&gt;"),
            " — works? merge it back. Doesn’t? delete it: nothing is lost.", tag=t.div,
        )
