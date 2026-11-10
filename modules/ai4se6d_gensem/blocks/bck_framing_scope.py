"""Slide — Framing: one user, one problem, a minimum viable product (Ries) (CCSET15, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Scope styles."""
    heading = s.project.titles.heading
    lbl = Style.create(s.project.titles.table_label + s.center_txt, "scope_tl")
    txt = s.project.titles.table_cell
    source = s.project.citation + s.large + s.center_txt
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "scope_foot")
bs = BlockStyles

ROWS = [
    ("One user", "a real person you can picture — not \"everyone\""),
    ("One problem", "the pain, in one sentence"),
    ("2-4 requirements", "the smallest product that solves it: a minimum viable product"),
    ("Out of scope", "written down, in the backlog — not in the code"),
    ("Milestones", "card validated today · plan at 16:30 on day 5 · delivery at 11:30 on day 6"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(64):
            st_write(bs.heading, "Small Enough to Finish", tag=t.div, toc_lvl="+1", label="Framing the scope")
            for name, what in ROWS:
                with st_grid(cols="26% 70%", gap="6px", cell_styles=s.project.containers.table_normal_cell) as g:
                    with g.cell(): st_write(bs.lbl, name)
                    with g.cell(): st_write(bs.txt, what)
            st_write(bs.source, cite("ries-lean2011"), tag=t.div)
            st_write(bs.foot, "A finished small project teaches more than half of a big one.", tag=t.div)
