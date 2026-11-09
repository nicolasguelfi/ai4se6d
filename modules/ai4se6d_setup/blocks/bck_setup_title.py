"""Title slide — Hands-on Setup & First Prototype (day 1 afternoon)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Title slide styles."""
    title = Style.create(
        s.Huge + s.bold + s.center_txt + s.project.colors.primary
        + Style("line-height:1.1;", "setup_title_lh"),
        "setup_title",
    )
    subtitle = Style.create(s.project.titles.subtitle + s.center_txt, "setup_title_subtitle")
    parts = Style.create(s.project.titles.body + s.center_txt, "setup_title_parts")
    part = s.bold + s.project.colors.accent
    info = Style.create(s.project.titles.caption + s.center_txt, "setup_title_info")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_center):
        with st_block(s.center_txt):
            st_write(bs.title, "Hands-on Setup & First Prototype", tag=t.div, toc_lvl="1")
            st_space("v", 2)
            st_write(bs.subtitle, "Day 1 — Afternoon", tag=t.div)
            st_space("v", 2)
            st_write(
                bs.parts,
                (bs.part, "Install"), "  →  ", (bs.part, "Build"), "  →  ", (bs.part, "Debrief"),
                tag=t.div,
            )
            st_space("v", 2)
            st_write(bs.info, "AI for Software Engineering · opencode 2 + GSE-One v0.90.0", tag=t.div)
