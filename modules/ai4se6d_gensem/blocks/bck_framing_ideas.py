"""Slide — Need inspiration? Five project ideas (CCSET15, edition 2; adapted from the edition-1 day-5 deck)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Ideas styles."""
    heading = s.project.titles.heading
    hdr = Style.create(s.project.titles.table_header + s.center_txt, "ideas_th")
    lbl = Style.create(s.project.titles.table_label + s.center_txt, "ideas_tl")
    txt = s.project.titles.table_cell
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "ideas_foot")
bs = BlockStyles

ROWS = [
    ("Shift planner", "scheduling for a small team, flags conflicts"),
    ("Recipe keeper", "personal recipes, ingredient search, shopping list"),
    ("Inventory tracker", "stock of a small business, low-stock alerts"),
    ("Study buddy", "flashcards with spaced repetition"),
    ("Incident logger", "support incidents with severity and resolution time"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(66):
            st_write(bs.heading, "Need Inspiration?", tag=t.div, toc_lvl="+1", label="Project ideas")
            with st_grid(cols="30% 66%", gap="6px", cell_styles=s.project.containers.table_header_cell) as g:
                with g.cell(): st_write(bs.hdr, "Idea")
                with g.cell(): st_write(bs.hdr, "In one line")
            for name, line in ROWS:
                with st_grid(cols="30% 66%", gap="6px", cell_styles=s.project.containers.table_normal_cell) as g:
                    with g.cell(): st_write(bs.lbl, name)
                    with g.cell(): st_write(bs.txt, line)
            st_write(bs.foot, "Sparks, not assignments: pick one, adapt one, or ignore them all.", tag=t.div)
