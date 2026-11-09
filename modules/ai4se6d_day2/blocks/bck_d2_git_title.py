"""Section title — Git first (09:15, 35 min)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Section title styles."""
    section = Style.create(s.project.titles.section_title + s.center_txt, "d2_sec_title")
    subtitle = Style.create(s.project.titles.subtitle + s.center_txt, "d2_sec_subtitle")
    info = Style.create(s.project.titles.caption + s.center_txt, "d2_sec_info")
    quote = Style.create(s.project.titles.body + s.italic + s.center_txt, "d2_sec_quote")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_center):
        st_write(bs.info, "09:15 — 35 min · show 12 · try 15 · debrief 5", tag=t.div)
        st_space("v", 1)
        st_write(bs.section, "Git First", tag=t.div, toc_lvl="1")
        st_write(bs.subtitle, "Your safety net — before the agent touches anything", tag=t.div)
        st_space("v", 2)
        st_write(bs.quote, "Coding without version control is a long game with no save button.", tag=t.div)
