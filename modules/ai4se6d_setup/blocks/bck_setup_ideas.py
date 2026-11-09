"""Slide — Three ideas to get started (or bring your own)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Ideas slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    name = Style.create(s.project.titles.body_accent + s.center_txt, "setup_idea_name")
    text = Style.create(s.project.titles.table_cell + s.center_txt, "setup_idea_text")
    body = Style.create(s.project.titles.body + s.center_txt, "setup_idea_body")
    keyword = s.bold + s.project.colors.highlight
    caption = Style.create(s.project.titles.caption + s.center_txt, "setup_idea_caption")
bs = BlockStyles

_IDEAS = [
    ("Recipe Finder", "type ingredients → get matching recipes"),
    ("Habit Tracker", "daily checklist with streaks"),
    ("Movie Watchlist", "browse, save and rate movies"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "Three Ideas", tag=t.div, toc_lvl="1")
        st_space("v", 1)
        with st_grid(
            cols="repeat(auto-fit, minmax(300px, 1fr))",
            gap="16px",
            cell_styles=s.project.containers.table_normal_cell,
        ) as g:
            for name, text in _IDEAS:
                with g.cell():
                    st_write(bs.name, name, tag=t.div)
                    st_write(bs.text, text, tag=t.div)
        st_space("v", 1)
        st_write(bs.body, (bs.keyword, "Your own idea?"), " Go for it — keep it small and personal.", tag=t.div)
        st_write(bs.caption, "Use made-up data: no real personal or company data.", tag=t.div)
