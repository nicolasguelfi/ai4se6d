"""Title slide — Day 2: Driving a Coding Agent, CalcApp v0.1."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Title slide styles."""
    title = Style.create(
        s.Huge + s.bold + s.center_txt + s.project.colors.primary
        + Style("line-height:1.1;", "d2_title_lh"),
        "d2_title",
    )
    subtitle = Style.create(s.project.titles.subtitle + s.center_txt, "d2_title_subtitle")
    info = Style.create(s.project.titles.caption + s.center_txt, "d2_title_info")
    motto = Style.create(s.project.titles.body_accent + s.center_txt, "d2_title_motto")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_center):
        with st_block(s.center_txt):
            st_write(bs.info, "AI for Software Engineering — Day 2", tag=t.div)
            st_space("v", 1)
            st_write(
                bs.title, "Driving a Coding Agent", tag=t.div, toc_lvl="1",
                label="Day 2 — Driving a Coding Agent",
            )
            st_space("v", 1)
            st_write(bs.subtitle, "CalcApp v0.1 — planned, tested, reviewed, delivered", tag=t.div)
            st_space("v", 2)
            st_write(bs.motto, "Same tools as yesterday. A different discipline.", tag=t.div)
