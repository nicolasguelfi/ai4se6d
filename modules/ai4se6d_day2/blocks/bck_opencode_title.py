"""Section title — Driving opencode (09:50, 55 min)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Section title styles."""
    section = Style.create(s.project.titles.section_title + s.center_txt, "sec_title")
    subtitle = Style.create(s.project.titles.subtitle + s.center_txt, "sec_subtitle")
    info = Style.create(s.project.titles.caption + s.center_txt, "sec_info")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_center):
        st_write(bs.info, "09:50 — 55 min · 3 short demos, each followed by 5 min of try-it", tag=t.div)
        st_space("v", 1)
        st_write(bs.section, "Driving opencode", tag=t.div, toc_lvl="1")
        st_write(bs.subtitle, "Give the agent what a new colleague would need", tag=t.div)
